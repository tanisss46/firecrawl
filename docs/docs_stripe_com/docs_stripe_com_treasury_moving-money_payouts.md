# Payouts and top-ups from Stripe Payments

## Learn how to move money between Payments account balances and Treasury financial account balances.

You can move money from Stripe Payments to Stripe Treasury with
[payouts](https://docs.stripe.com/treasury/moving-money/payouts#payouts), and
from Stripe Treasury back to Stripe Payments with
[top-ups](https://docs.stripe.com/treasury/moving-money/payouts#top-ups).

## Financial accounts as external accounts

Before you can send payouts to a Treasury financial account or receive top-ups
from a Treasury financial account, you must set the financial account as an
external account (BankAccount object) connected to the relevant Stripe account.

- Connected accounts: Use [POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/external_accounts](https://docs.stripe.com/api/external_account_bank_accounts/create)
with the financial account `routing_number` and `account_number` to create a
`BankAccount` object you can use for payouts from a connected account
- Platform accounts: Use the Stripe Dashboard to create a `BankAccount` object
you can use for payouts from, or top-ups to, your platform account

If there isn’t a default external account set for the `usd` currency, the
financial account becomes the account’s default payout destination. If there is
one, you can make the financial account the default for a connected account by
setting
[default_for_currency](https://docs.stripe.com/api/external_account_bank_accounts/create?lang=node#account_create_bank_account-default_for_currency)
to true, as in the following example. If you have an automatic payout schedule
enabled, that changes the target of the payouts to the financial account.

```
curl
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/external_accounts \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "external_account[object]"="bank_account" \
 -d "external_account[routing_number]"="{{FINANCIAL_ACCOUNT_ROUTING_NUMBER}}" \
 -d "external_account[account_number]"="{{FINANCIAL_ACCOUNT_ACCOUNT_NUMBER}}" \
 -d "external_account[country]"="US" \
 -d "external_account[currency]"="usd" \
 -d "default_for_currency"="true"
```

If successful, the response returns the newly created `BankAccount` object.

```
{
 "id": "{{BANK_ACCOUNT_ID}}",
 "object": "bank_account",
 "account": "{{CONNECTED_ACCOUNT_ID}}",
 "account_holder_name": null,
 "account_holder_type": null,
 "available_payout_methods": [
 "standard",
 "instant"
 ],
 ...
 "default_for_currency": true,
 ...
}
```

### Fifth Third financial accounts as external accounts

#### Private preview

Access to Fifth Third is currently limited to preview users. [Reach out to
us](mailto:treasury-support@stripe.com) if you’re interested in trying it out.

You now have the option to set up an external account by specifying the
financial account `id`. You must also request the
[intra_stripe_flows](https://docs.stripe.com/api/treasury/financial_accounts/object#financial_account_object-features-intra_stripe_flows)
feature on your Financial Account.

```
curl
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/external_accounts \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "external_account[object]"="bank_account" \
 -d "external_account[financial_account]"="{{FINANCIAL_ACCOUNT_ID}}" \
 -d "external_account[country]"="US" \
 -d "external_account[currency]"="usd" \
 -d "default_for_currency"="true"
```

## Payouts

Every Stripe platform account and connected account has an account balance (also
called a payments balance or acquiring balance) that stores their money. Those
funds aren’t directly accessible for use outside Stripe. Payouts move funds from
an account balance to an externally accessible Treasury financial account
balance or external bank account.

You can fund a Treasury financial account using automatic or manual payouts. For
more information about Treasury accounts, see the [Stripe Treasury accounts
structure
guide](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure).

To learn more about how payouts work with Connect, see the [Pay out money
guide](https://docs.stripe.com/connect/add-and-pay-out-guide).

## Automatic payouts

If you have connected accounts on your platform with an automatic payout
schedule, you can change the target of direct payouts from their external bank
accounts to their financial accounts. It requires the Treasury financial account
to be set up as a `BankAccount` object; see the [Financial accounts as external
accounts](https://docs.stripe.com/treasury/moving-money/payouts#financial-accounts-as-external-accounts)
section for more information.

## Automatic payout speeds

By default, when using automatic payouts, funds from incoming card payments
become available in the financial account balance two business days after the
payment is received (T+2 schedule). Other payment types, such as ACH payments
take longer.

After a platform-level credit approval, you can enable T+1 faster payouts on a
per-account basis for connected accounts. You can set the `interval` and
`delay_days` parameters with `POST /v1/accounts` to accelerate payout schedules
automatically (or you can manually trigger faster payouts as described below).
Contact [treasury-support@stripe.com](mailto:treasury-support@stripe.com) if you
want to request access to faster payouts (manual, automated, or both) for the
connected accounts on your platform.

T+1 faster payout schedules apply to all payment types, including card payments
and ACH payments.

### T+1 automatic payout schedule

To have incoming payments automatically available in the financial account on
the next business day, send a request with `interval` set to `daily` and
`delay_days` set to `1`.

Use [POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-schedule)
to update the payout schedule.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "settings[payouts][schedule][interval]"=daily \
 -d "settings[payouts][schedule][delay_days]"=1
```

The response confirms the updated settings.

```
{
 ...
 "settings": {
 "payouts": {
 "schedule": {
 "interval": "daily",
 "delay_days": 1,
 },
 },
 ...
 }
 ...
}
```

## Manual payouts

You can use manual payouts to send specific portions of an account balance to
that account’s Treasury financial account.

Use [POST /v1/payouts](https://docs.stripe.com/api/payouts/create) with the bank
account `id` associated with your financial account specified as the
`destination` parameter value. If you don’t have a `BankAccount` object
associated with your Treasury financial account yet, see the [Financial accounts
as external
accounts](https://docs.stripe.com/treasury/moving-money/payouts#financial-accounts-as-external-accounts)
section for more information.

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d method=standard \
 -d amount=1000 \
 -d currency=usd \
 -d destination={{BANK_ACCOUNT_ID}}
```

If successful, the response returns the newly created [Payout
object](https://docs.stripe.com/api/payouts/object).

```
{
 "id": "{{PAYOUT_ID}}",
 "object": "payout",
 "amount": 1000,
 ...
 "currency": "usd",
 "destination": "{{BANK_ACCOUNT_ID}}",
 ...
 "method": "standard",
 ...
}
```

## Manual payout speeds

Two speed methods are available for manual payouts - `standard` and `instant`.

Manual payouts using `standard` speed can only draw on the `available` balance,
and funds will generally arrive in the financial account in one business day
(T+1 schedule).

If your platform is enabled for faster payouts, you can use `instant` manual
payouts to move funds to a connected account’s financial account within an hour.
You can request instant manual payouts at any time, including weekends and
holidays, and instant manual payouts can draw on the `instant_available` balance
of a Stripe account. If your platform is not enabled for faster payouts and
you’re interested in adding the ability, contact
[treasury-support@stripe.com](mailto:treasury-support@stripe.com) to request the
feature.

To request an instant manual payout rather than a standard manual payout, change
the `method` parameter in the payout request from `standard` to `instant`.

## Testing payouts

You can simulate a payout to a connected account financial account using test
mode API keys.

You can only simulate a payout to a platform financial account using the
Dashboard. While in test mode, click the **Add money** button in the upper right
of the [Balances](https://dashboard.stripe.com/test/treasury) view of your
Dashboard to open the **Add Money** dialog. Follow the prompts to simulate
sending money from your platform account balance to your financial account
balance.

![Stripe Dashboard open to the Treasury balance page in test mode with the Add
money button
highlighted.](https://b.stripecdn.com/docs-statics-srv/assets/test-payout.31e4405710a6d92e3592f570ac86f0be.png)

Add money button

## Top-ups

As the owner of a [Connect](https://docs.stripe.com/connect) platform, you can
use an eligible Treasury financial account balance to top-up your platform
account balance instead of using an external bank account. Your financial
account must have the
[financial_addresses.aba](https://docs.stripe.com/treasury/account-management/financial-account-features#available-features)
feature active to be eligible. To top-up a platform account balance, you must
set the platform’s Treasury financial account as the platform’s default external
`BankAccount` using the Stripe Dashboard as described in the [Adding funds to
your platform balance](https://docs.stripe.com/connect/top-ups) guide.

Unlike true external bank accounts, new `BankAccount` objects with Treasury
financial account details owned by the merchant with the BankAccount object are
automatically verified upon creation so they don’t require verification with
microdeposits.

After you set the Treasury financial account as your platform’s default external
bank account, use `POST /v1/topups` to create the top-up.

```
curl https://api.stripe.com/v1/topups \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2000 \
 -d currency=usd \
 -d description=Top-up \
 -d statement_descriptor=Top-up
```

If successful, the response returns the `Top-Up` object.

```
{
 "id": "{{TOP_UP_ID}}",
 "object": "topup",
 "amount": 2000,
 "currency": "usd",
 "description": "Top-up",
 ...
}
```

Learn more about [adding funds to your platform account
balance](https://docs.stripe.com/connect/top-ups) with Stripe Connect.

## Links

- [payouts](https://docs.stripe.com/treasury/moving-money/payouts#payouts)
- [top-ups](https://docs.stripe.com/treasury/moving-money/payouts#top-ups)
- [POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/external_accounts](https://docs.stripe.com/api/external_account_bank_accounts/create)
-
[default_for_currency](https://docs.stripe.com/api/external_account_bank_accounts/create?lang=node#account_create_bank_account-default_for_currency)
-
[intra_stripe_flows](https://docs.stripe.com/api/treasury/financial_accounts/object#financial_account_object-features-intra_stripe_flows)
- [Stripe Treasury accounts structure
guide](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
- [Pay out money guide](https://docs.stripe.com/connect/add-and-pay-out-guide)
- [POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-schedule)
- [POST /v1/payouts](https://docs.stripe.com/api/payouts/create)
- [Payout object](https://docs.stripe.com/api/payouts/object)
- [Balances](https://dashboard.stripe.com/test/treasury)
- [Connect](https://docs.stripe.com/connect)
-
[financial_addresses.aba](https://docs.stripe.com/treasury/account-management/financial-account-features#available-features)
- [Adding funds to your platform
balance](https://docs.stripe.com/connect/top-ups)