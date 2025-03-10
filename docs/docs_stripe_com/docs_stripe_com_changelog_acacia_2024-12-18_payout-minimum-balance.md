# Adds new balance transaction types to support minimum balance

## What’s new

This update introduces two new [balance transaction
types](https://docs.stripe.com/reports/balance-transaction-types#balance_related)
to support payout reconciliation for Stripe accounts that limit automatic
payouts by setting a minimum balance.

## Impact

The `payout_minimum_balance_hold` transaction type is a negative value
representing the amount withheld from a payout to maintain an account’s minimum
balance. The `payout_minimum_balance_release` transaction type is a positive
value representing the amount added back to the account balance, and always
corresponds to the hold value from the same payout. For example, if an account
with a minimum balance of 100 USD contains 1000 USD to pay out, a
`payout_minimum_balance_hold` of -100 USD is applied to the payout, resulting in
a payout of 900 USD. Then, a matching `payout_minimum_balance_release` of 100
USD is added to the account balance.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValuesChangeEnumpayout_minimum_balance_holdpayout_minimum_balance_releaseAdded[BalanceTransaction.type](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-type)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-12-18.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Related changes

- [Adds SDK support for trace
IDs](https://docs.stripe.com/changelog/acacia/2024-12-18/trace-id-sdk)

## Links

- [balance transaction
types](https://docs.stripe.com/reports/balance-transaction-types#balance_related)
-
[BalanceTransaction.type](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-type)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)
- [Adds SDK support for trace
IDs](https://docs.stripe.com/changelog/acacia/2024-12-18/trace-id-sdk)