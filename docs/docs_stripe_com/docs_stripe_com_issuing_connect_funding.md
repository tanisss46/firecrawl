# Funding Issuing balances with Connect

## Learn how to fund connected accounts for Issuing.

Before an issued card can be used for transactions, you must first allocate
funds to the connected account’s [Issuing
balance](https://docs.stripe.com/issuing/funding/balance) associated with the
card. An Issuing balance holds funds reserved for the card and is safely
separated from earnings, [payouts](https://docs.stripe.com/payouts), and funds
from other Stripe products.

## Fund from a bank account

You have two options for funding an Issuing balance from an external account
that each have different setups: pull funding and push funding.

- **Pull funding** is the default funding option in the US and isn’t available
in the EU or the UK. You need to verify external bank accounts, which usually
causes a delay in transferring funds (up to 5 business days). This option allows
you to control and identify which bank your top-up originates from.
- **Push funding** is available in the UK and EU and as a beta in the US. This
options allows you to originate the funds from your own bank account to Stripe.
You might be able to receive funds the same day with push funding, which depends
on the process you use (for example, ACH or wire transfer).
Pull funding (US)Push funding (US)Push funding (Euro)Push funding (UK)
Before you can top-up a connected account from your user’s bank account, you
must first collect and verify their account information. Stripe provides the
option of collection through
[Stripe.js](https://docs.stripe.com/payments/elements) with verification using
microdeposits.

### Collecting your users’ information

To debit the user’s bank account for funding, you will need to collect their
bank account information and submit evidence of their authorization to debit
their account. This is known as a
[mandate](https://docs.stripe.com/api/sources/create#create_source-mandate), and
ensures both you and Stripe remain compliant with ACH network rules, as well as
provide you with access to evidence to ease in any dispute resolution.

Create a form that captures:

- Name
- Routing number
- Account number

As your customers submit the mandate, you should record:

- IP address
- User agent
- Date

If instead you prefer to collect mandates from your users *offline* (such as via
phone or a paper agreement), you won’t upload evidence of acceptance to Stripe.
You should maintain your own record of the acceptance and provide us a contact
email in case the evidence is requested.

### Creating the token and source

Create a token using the [Bank Account Token
API](https://docs.stripe.com/api/tokens/create_bank_account), and then use it to
create a source. Create both the bank account token and `source` on the
connected account you want to fund.

#### Caution

Store these `Source` tokens in your own system where your integration can
retrieve them. Stripe currently doesn’t provide a way to programmatically
retrieve or list the tokens after they’re created.

```
curl https://api.stripe.com/v1/tokens \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "bank_account[country]"=US \
 -d "bank_account[currency]"=usd \
 -d "bank_account[account_holder_name]"="Jenny Rosen" \
 -d "bank_account[account_holder_type]"=individual \
 -d "bank_account[routing_number]"=110000000 \
 -d "bank_account[account_number]"=000000000009
```

Create a `source` using the token you obtained:

```
curl https://api.stripe.com/v1/sources \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d type=ach_debit \
 -d currency=usd \
 -d token={{TOKEN_ID}} \
 -d "owner[address][line1]"="510 Townsend Street" \
 -d "owner[address][city]"="San Francisco" \
 -d "owner[address][state]"=California \
 -d "owner[address][country]"=US \
 --data-urlencode "owner[email]"="jenny.rosen@example.com" \
 -d "owner[name]"="Jenny Rosen" \
 -d "owner[phone]"=5554443333
```

### Verifying sources with microdeposits

Two small deposits with the statement description **ACCTVERIFY** are sent to the
bank account within 1-2 days. You should collect these two amounts from your
user to verify the bank account.

```
curl https://api.stripe.com/v1/sources/{{SOURCE_ID}}/verify \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "values[]"=32 \
 -d "values[]"=45
```

### Top-up a connected account’s Issuing balance

Fund the Issuing balance on your connected account with top-ups by passing in
the `source` that was made and setting the `destination_balance` to `issuing`.

```
curl https://api.stripe.com/v1/topups \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -d "amount"=2000 \
 -d "currency"="usd" \
 -d "description"="Top-up for week of May 31" \
 -d "destination_balance"="issuing" \
 -d "statement_descriptor"="Top-up" \
 -d "source"="{{SOURCE_ID}}"
```

## Fund from a connected account’s Stripe balance

You must [sign up for the Balance Transfer API private
beta](https://docs.stripe.com/issuing/connect/funding#request-early-access) to
transfer funds from your Stripe balance into your Issuing balance.

```
curl https://api.stripe.com/v1/balance_transfers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d "source_balance[type]"=payments \
 -d "destination_balance[type]"=issuing
```

Transfers from your connected account’s Stripe balance are instant and available
24x7 in the US, or take 1 business day in the UK and euro area countries. This
allows you to quickly and easily utilize earned funds from Stripe Payments for
spend with Stripe Issuing.

You can only move an amount up to the available Stripe balance. Funds won’t be
available in the Issuing balance while the transfer is pending.

Use the [retrieve balance](https://docs.stripe.com/api/balance/balance_retrieve)
endpoint to get your available Stripe balance amounts broken down by
[source_type](https://docs.stripe.com/api/balance/balance_object#balance_object-available-source_types).

### Request early access

Access to the Balance Transfer API is currently limited to beta users. You must
be an Issuing customer to join the beta. To request access to the beta, log in
to your Stripe account and refresh the page. [Contact
Stripe](https://stripe.com/contact/sales) for more information.

## Retrieve an Issuing balance

To check the current Issuing balance of a connected account, call the [Balance
API](https://docs.stripe.com/api/balance/balance_retrieve) GET endpoint and pass
the connected account ID into the header.

```
curl https://api.stripe.com/v1/balance \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

The`balance` object is returned with a corresponding `issuing` object that
includes the current available balance:

```
{
 "object": "balance",
...
 "issuing": {
 "available": [
 {
 "amount": 100,
 "currency": "usd"
 }
 ]
 },
 "livemode": false
}
```

## Pay out an Issuing balance to an external account

The funds in an Issuing balance can also be paid out to a connected account’s
[external bank account](https://docs.stripe.com/api/external_accounts) using the
[Payouts API](https://docs.stripe.com/api/payouts/create) POST endpoint and
specifying the `source_balance` of the payout as `issuing.`

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d source_balance=issuing \
 -d amount=100 \
 -d currency=usd
```

## Links

- [Issuing balance](https://docs.stripe.com/issuing/funding/balance)
- [payouts](https://docs.stripe.com/payouts)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [mandate](https://docs.stripe.com/api/sources/create#create_source-mandate)
- [Bank Account Token
API](https://docs.stripe.com/api/tokens/create_bank_account)
- [retrieve balance](https://docs.stripe.com/api/balance/balance_retrieve)
-
[source_type](https://docs.stripe.com/api/balance/balance_object#balance_object-available-source_types)
- [Contact Stripe](https://stripe.com/contact/sales)
- [external bank account](https://docs.stripe.com/api/external_accounts)
- [Payouts API](https://docs.stripe.com/api/payouts/create)