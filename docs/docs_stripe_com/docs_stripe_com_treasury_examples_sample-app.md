# Issuing and Treasury sample app

## Use the Stripe Next.js sample app to start your own Issuing and Treasury integration.

In addition to a full suite of documentation and SDKs for Stripe Issuing and
Treasury, we offer a Next.js sample app.

See a demo of our sample app at [baas.stripe.dev](https://baas.stripe.dev/), or
check out the [GitHub
repository](https://github.com/stripe-samples/issuing-treasury).

## Accessing code

The sample app is a Next.js app that leverages TypeScript, React, and Material
UI. You can fork the project from the [Stripe samples GitHub
repository](https://github.com/stripe-samples/issuing-treasury) and use the
included components as a starting point for your own app.

## App features

The app provides many how-to examples, including:

- Leverage Stripe Connect Onboarding to collect Know Your Customer (KYC)
information for onboarding connected accounts compliantly
- Display account information and balance
- Display transactions on the Treasury Financial Account
- Simulate sending funds to an external account using ACH or wire
- Simulate receiving an ACH credit
- Visualize the volume of inbound and outbound money flows using
[ApexCharts](https://github.com/apexcharts/apexcharts.js)
- Create cardholders compliantly
- Create cards using the Treasury Financial Account as an issuable balance
- Show sensitive card numbers in a PCI-compliant way
- Simulate card authorizations
- Get paid through a payment link, then transfer funds from your Stripe payments
balance to the Financial Account
- Use test helpers to simulate actions impacting the account

## Component breakdown

The following sections provide an overview of how each component in the sample
app works.

You can learn more about [Issuing APIs and
features](https://docs.stripe.com/issuing) or [Treasury
APIs](https://docs.stripe.com/api/treasury/financial_accounts) and
[features](https://docs.stripe.com/treasury).

### Account creation

The account creation flow consists of four steps:

- Create a [connected
account](https://docs.stripe.com/treasury/account-management/connected-accounts)
with the following capabilities: `transfers`, `card_issuing`, and `treasury`.

```
const account = await stripe.accounts.create({
 country: 'US',
 email: email,
 capabilities: {
 transfers: {requested: true},
 treasury: {requested: true},
 card_issuing: {requested: true},
 },
 controller: {
 dashboard: {type: "none"},
 losses: {payments: "application"},
 requirement_collection: "application",
 fees: {payer: "application"}
 },
});
```

- Create a Stripe Treasury [Financial
Account](https://docs.stripe.com/treasury/account-management/financial-accounts).

```
const financialAccount = await stripe.treasury.financialAccounts.create(
 {
 supported_currencies: ['usd'],
 features: {
 card_issuing: {requested: true},
 deposit_insurance: {requested: true},
 financial_addresses: {aba: {requested: true}},
 inbound_transfers: {ach: {requested: true}},
 intra_stripe_flows: {requested: true},
 outbound_payments: {
 ach: {requested: true},
 us_domestic_wire: {requested: true},
 },
 outbound_transfers: {
 ach: {requested: true},
 us_domestic_wire: {requested: true},
 },
 },
 },
 {stripeAccount: account.id},
);
```

- Create a Connect Onboarding link and use it to redirect new connected accounts
to collect the necessary profile information for the requested capabilities.

```
const { url } = await stripe.accountLinks.create({
 type: 'account_onboarding',
 account: accountId,
 refresh_url: host + '/onboard',
 return_url: host + '/onboard',
 collect: 'eventually_due',
});
```

### Account balance

The account balance card uses only the `stripe.treasury.financialAccounts.list`
API.

```
const financialAccounts = await stripe.treasury.financialAccounts.list({
 stripeAccount: StripeAccountID,
});
const financialAccount = financialAccounts.data[0];
```

The payload of the above command contains a balance object consisting of the
current
[balance](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions)
(cash) and outbound funds.

```
{
 "id": "fa_...",
 ...
 "balance": {
 "cash": { "usd": 534214 },
 "inbound_pending": { "usd": 0 },
 "outbound_pending": { "usd": 2200 }
 },
 ...
 "supported_currencies": [ "usd" ]
}
```

### Funds in and funds out chart

The funds movement chart uses only the `stripe.treasury.transactions.list` API.

```
const fa_transactions = await stripe.treasury.transactions.list(
 {
 financial_account: financialAccount.id,
 order_by: 'created',
 limit: 100,
 },
 {stripeAccount: StripeAccountID},
);
```

The responses are grouped by positive or negative balances and creation date.
The data is then ported into
[ApexCharts](https://github.com/apexcharts/apexcharts.js) to create a dynamic
display of the funds flow.

```
{
 "id": "{{TRANSACTION_ID}}",
 "object": "treasury.transaction",
 "created": "{{T}}",
 ...
 "flow": "{{OUTBOUND_PAYMENT_ID}}",
 "flow_type": "outbound_payment",
 "status": "open",
 "amount": -1000,
 "currency": "usd",
 "balance_impact": {
 "cash": -1000,
 "inbound_pending": 0,
 "outbound_pending": 1000,
 },
 "entries": {
 "data": [
 {
 "id": "{{TRANSACTION_ENTRY_ID}}",
 "object": "treasury.transaction_entry",
 ...
 "created": "{{T}}",
 "effective_at": "{{T}}",
 "currency": "usd",
 "balance_impact": {
 "cash": -1000,
 "inbound_pending": 0,
 "outbound_pending": 1000,
 }
 }
 ],
 "has_more": false,
 "object": "list",
"url":
"/v1/treasury/transaction_entries?financial_account={{FINANCIAL_ACCOUNT_ID}}&transaction={{TRANSACTION_ID}}"
 }
}
```

### Transaction list

The transaction list uses the `stripe.treasury.transactions.list` API.

```
const fa_transactions = await stripe.treasury.transactions.list(
 {
 financial_account: financialAccount.id,
 order_by: 'created',
 limit: 100,
 },
 {stripeAccount: StripeAccountID},
);
```

The columns in the transactions table are parsed from the `transaction` object
using the following mapping:

- `created` → Date
- `amount` → Amount / Currency
- `flow_type` → Type
- `status` → Status
- `description` → Description

### Send money interface

The money sending feature in the sample app uses the Stripe Treasury
`OutboundPayment` feature. You can use
[OutboundPayments](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments)
to send money to a third party’s external account.

```
const outboundPayment = await stripe.treasury.outboundPayments.create(
 {
 financial_account: financialAccount.id,
 amount: amount,
 currency: 'usd',
 statement_descriptor: req.descriptor,
 destination_payment_method_data: {
 type: 'us_bank_account',
 us_bank_account: {
 account_holder_type: 'individual',
 routing_number: '110000000',
 account_number: '000000000009',
 }
 }
 },
 {
 stripeAccount: StripeAccountId
 },
);
```

### Issuing cardholder creation

You must create a `Cardholder` before you can issue a card using Stripe Issuing
to spend funds from the Treasury Financial Account. Use the
`stripe.issuing.cardholders.create` API to create cardholders.

```
const cardholder = await stripe.issuing.cardholders.create(
 {
 type: 'individual',
 name: firstName + ' ' + lastName,
 email: email,
 individual: {
 first_name: firstName,
 last_name: lastName,
 dob: {day: day, month: month, year: year}
 },
 billing: {
 address: {
 city: city,
 line1: address1,
 state: state,
 postal_code: postalCode,
 country: country,
 },
 },
 },
 {
 stripeAccount: StripeAccountId,
 }
);
```

### Issuing cards

After you create a `Cardholder`, you can issue a card to the `Cardholder` using
the `stripe.issuing.cards.create` API.

```
const card = await stripe.issuing.cards.create(
 {
 cardholder: req.body.cardholderid,
 financial_account: financialAccount.id,
 currency: 'usd',
 type: 'virtual',
 status: 'active',
 },
 {stripeAccount: StripeAccountId},
);
```

### Cards list

The cards list renders using data from the `stripe.issuing.cards.list` API.

```
const cards = await stripe.issuing.cards.list(
 {limit: 10},
 {stripeAccount: StripeAccountID},
);
```

### Card authorization list

Use the `stripe.issuing.authorizations.list` API to retrieve authorizations for
a specific card. The following example limits the list to the 10 most recent
authorizations.

```
const card_authorizations = await stripe.issuing.authorizations.list(
 {
 card: cardId,
 limit: 10,
 },
 {stripeAccount: StripeAccountID},
);
```

The columns in the authorization table are parsed from the response object using
the following mapping:

- `created` → Date
- `amount` → Amount / Amount Currency
- `card.cardholder.name` → Name on Card
- `card.last4` → Last 4
- `approved` → Approved
- `status` → Status
- `merchant_data.name` → Merchant
- `merchant_data.category` → Merchant Category

## Test mode helpers

The sample app features test mode helpers that enable you to perform certain
actions, such as funding your account, creating a payment link to collect funds
in a connected account, and paying out funds to the Financial Account. You can
access most of the test helpers by clicking the **Generate Test Data** button or
clicking **Test Data**.

### Received Credit test helper

In test mode, you can add funds to a Treasury Financial Account using the
[ReceivedCredit Test
Helpers](https://docs.stripe.com/api/treasury/received_credits/test_mode_create).
This test helper simulates receiving a transfer from an external bank account
into your Financial Account.

```
const receivedCredit = await stripe.testHelpers.treasury.receivedCredits.create(
 {
 amount: 50000,
 currency: 'usd',
 financial_account: financialAccount.id,
 network: 'ach',
 },
 {stripeAccount: StripeAccountId},
);
```

### Payment links and payouts

You can use payment links to add funds to the connected account that’s
associated with a Financial Account:

- Create a `Price` that determines the amount deposited into the connected
account after completion of payment.

```
const prices = await stripe.prices.list(
 {
 limit: 1,
 active: true,
 type: 'one_time',
 },
 {stripeAccount: StripeAccountId,},
);

let price;

if (prices.data.length < 1) {
 price = await stripe.prices.create(
 {
 unit_amount: 1000,
 currency: 'usd',
 product_data:
 {
 name: 'Unit',
 },
 },
 {stripeAccount: StripeAccountId,},
 );
} else {
 price = prices.data[0];
}
```

- After obtaining the price, Stripe creates a `PaymentLink`, and you redirect
the customer to complete the payment. Use the `Price` `id` from the previous
step to set the value for the `price` parameter. Alternatively, you can exclude
the parameter to use a default value instead.

```
const paymentLink = await stripe.paymentLinks.create(
 {
 line_items: [
 {
 price: price.id,
 quantity: 1,
 adjustable_quantity: {enabled: true},
 },
 ],
 },
 {stripeAccount: StripeAccountId,},
);
```

### Payout from the connected account payments balance

[Payouts](https://docs.stripe.com/treasury/moving-money/payouts#payouts) can
send funds from a connected account’s payments balance to their Treasury
Financial Account. Do the following to execute a payout:

- Check if there’s an external account configured for the connected account. To
do so, use the
[accounts.retrieve](https://docs.stripe.com/api/accounts/retrieve) API to obtain
the [account object](https://docs.stripe.com/api/accounts/object) and verify if
the `external_account` property is populated.

```
const responseAccount = await stripe.accounts.retrieve(StripeAccountID);
const accountExternalAccount = responseAccount.external_accounts.data[0];

let hasExternalAccount = false;

if (accountExternalAccount) {
 hasExternalAccount = true;
}
```

- If the connected account doesn’t have an external account, they can set up the
Treasury Financial Account as their external account.

```
const financialAccounts = await stripe.treasury.financialAccounts.list(
 {expand: ['data.financial_addresses.aba.account_number']},
 {
 stripeAccount: StripeAccountId,
 },
);

const financialAccount = financialAccounts.data[0];

await stripe.accounts.createExternalAccount(StripeAccountId, {
 external_account: {
 object: 'bank_account',
 country: 'US',
 currency: 'usd',
 account_number:
 financialAccount.financial_addresses[0].aba.account_number,
 routing_number:
 financialAccount.financial_addresses[0].aba.routing_number,
 },
});
```

- Initiate a payout to the connected account’s external account. In this case,
the external account is the Treasury Financial Account.

```
const balance = await stripe.balance.retrieve({
 stripeAccount: StripeAccountId,
});

const payout = await stripe.payouts.create(
 {
 amount: balance.available[0].amount,
 currency: 'usd',
 },
 {stripeAccount: StripeAccountId},
);
```

## Links

- [baas.stripe.dev](https://baas.stripe.dev)
- [GitHub repository](https://github.com/stripe-samples/issuing-treasury)
- [ApexCharts](https://github.com/apexcharts/apexcharts.js)
- [Issuing APIs and features](https://docs.stripe.com/issuing)
- [Treasury APIs](https://docs.stripe.com/api/treasury/financial_accounts)
- [features](https://docs.stripe.com/treasury)
- [connected
account](https://docs.stripe.com/treasury/account-management/connected-accounts)
- [Financial
Account](https://docs.stripe.com/treasury/account-management/financial-accounts)
-
[balance](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions)
-
[OutboundPayments](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments)
- [ReceivedCredit Test
Helpers](https://docs.stripe.com/api/treasury/received_credits/test_mode_create)
- [Payouts](https://docs.stripe.com/treasury/moving-money/payouts#payouts)
- [accounts.retrieve](https://docs.stripe.com/api/accounts/retrieve)
- [account object](https://docs.stripe.com/api/accounts/object)