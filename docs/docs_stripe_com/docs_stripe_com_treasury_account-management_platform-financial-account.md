# Platform financial accounts

## Learn about the financial account for your platform.

After you’ve [gained API access](https://docs.stripe.com/treasury/access) to
Stripe Treasury, we automatically provision your platform with two financial
accounts, one for test mode and one for live mode.

The test mode platform financial account enables you to set up and test your
integration without actually affecting either your platform account balance or
the balance of your live mode platform financial account.

The live mode platform financial account is where you store your own funds as
working capital for your Treasury program. The live mode platform financial
account has its own routing number and account number and supports most of the
same types of money movement as the financial accounts attached to your
platform’s connected accounts.

## Platform financial account differences

The financial accounts (live mode and test mode) for your platform are
essentially the same as the financial accounts attached to your platform’s
connected accounts. You use the same API requests regardless of which financial
account is involved; however, you don’t include a [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
when making API calls against your platform financial account. The
`Stripe-Account` header signals that a request is for the associated connected
account’s financial account rather than your platform’s.

The following list itemizes the differences between platform financial accounts
and financial accounts attached to connected accounts:

- You can’t attach Stripe Issuing cards to platform financial accounts.- You can
attach Stripe Issuing cards to the financial accounts attached to connected
accounts.
- You can’t transfer funds from your platform financial account balance directly
to the account balance of a connected account.- You can transfer funds from your
platform financial account balance directly to the balance of a financial
account attached to a connected account.
- You must use the Stripe Dashboard (rather than the API) to set the platform
financial account as a `BankAccount` object that you can use for payouts from or
top-ups to the platform payments balance.- See the [Payouts and
top-ups](https://docs.stripe.com/treasury/moving-money/payouts#financial-accounts-as-external-accounts)
guide for more information.
- You can’t accelerate payouts from the platform account balance to the platform
financial account balance.

## Retrieving platform financial account details

You can find your platform financial account routing number, account number, and
balance in the **Treasury balance** section under the **Balances** tab of your
Stripe [Dashboard](https://dashboard.stripe.com/test/treasury). Use the API to
view the other details of your platform financial account.

![Treasury balance section of the Dashboard showing account number, routing
number, and total amount of
balance.](https://b.stripecdn.com/docs-statics-srv/assets/treasury-balance.1647f7e2fdd3492e4bdab81cfced4b8b.png)

Treasury balance

Use `GET /v1/treasury/financial_accounts` to list all the details of your
platform financial accounts through the API. A `Stripe-Account` header isn’t
included, signaling this request is for the platform financial account.

```
curl https://api.stripe.com/v1/treasury/financial_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

If successful, the response includes your platform financial account `id`. You
can use the financial account ID to directly retrieve your platform financial
account details using `GET
/v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}`.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

The `FinancialAccount` object displays the data that defines your financial
account, including your balance and the balance of any pending transactions.

```
{
 "object": "treasury.financial_account",
 "created": 1612927106,
 "id": "fa_123",
 "country": "US",
 "supported_currencies": ["usd"],
// Arrays of active, pending and restricted features summarize the status of all
requested features
 "active_features": ["financial_addresses.aba", "deposit_insurance"],
 "pending_features": ["inbound_transfers.ach"],
"restricted_features": ["intra_stripe_flows", "outbound_payments.ach",
"outbound_payments.us_domestic_wire"],
```

See all 48 lines
## Create additional financial accounts for your platform

You can create up to 3 financial accounts on your platform account. Use `POST
/v1/treasury/financial_accounts` without a `Stripe-Account` header to create a
new financial account.

## Platform default financial account

Your platform has one financial account that is the default financial account.
That financial account is used by Stripe to service your platform. For example,
a default financial account is used by Stripe to remediate negative balances
incurred by connected accounts.

By default, your default financial account is the first financial account
created on your platform account. Your default financial account is denoted by
the `is_default` field set to `true` on the financial account.

## Retrieving platform financial account features

Use `GET /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}/features` to
retrieve your platform’s financial account feature information.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

If successful, the response itemizes the features assigned to your platform
financial account.

```
{
 "object": "treasury.financial_account_features",
 "card_issuing": {
 "requested": true,
 "status": "active",
 "status_details": []
 },
 "deposit_insurance": {
 "requested": true,
 "status": "active",
```

See all 44 lines
## Moving money between the Treasury financial accounts of the platform and its connected accounts

Use `OutboundPayments` over the `stripe` network to instantly move funds between
a platform Treasury financial account and the Treasury financial accounts of
connected accounts associated with the same platform. See [Creating an
OutboundPayment to a financial
account](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments#create-obp-for-fa)
for more information.

## See also

- [Treasury account
structure](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
- [Working with connected
accounts](https://docs.stripe.com/treasury/account-management/connected-accounts)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [Working with Stripe Issuing
cards](https://docs.stripe.com/treasury/account-management/issuing-cards)
- [Working with
balances](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions)
- [Moving money into Treasury financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-into-financial-accounts)
- [Moving money out of Treasury financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-out-of-financial-accounts)

## Links

- [gained API access](https://docs.stripe.com/treasury/access)
- [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [Payouts and
top-ups](https://docs.stripe.com/treasury/moving-money/payouts#financial-accounts-as-external-accounts)
- [Dashboard](https://dashboard.stripe.com/test/treasury)
- [Creating an OutboundPayment to a financial
account](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments#create-obp-for-fa)
- [Treasury account
structure](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
- [Working with connected
accounts](https://docs.stripe.com/treasury/account-management/connected-accounts)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [Working with Stripe Issuing
cards](https://docs.stripe.com/treasury/account-management/issuing-cards)
- [Working with
balances](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions)
- [Moving money into Treasury financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-into-financial-accounts)
- [Moving money out of Treasury financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-out-of-financial-accounts)