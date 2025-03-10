# Adds a new enum value representing a ReceivedDebit failure due to an international transaction

## What’s new

Treasury financial accounts can’t send or receive funds from international
sources, including international ACH transactions. This update introduces the
`international_transaction` enum value on `ReceivedDebit.failure_code`.

Addedfailure_code.international_transactionnullable enum
International transactions can’t pull funds from the FinancialAccount.

## Impact

Users can now identify
[ReceivedDebit](https://docs.stripe.com/api/treasury/received_debits)
transactions that have failed due to coming from an international source.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValuesChangeEnumsinternational_transactionAdded[Treasury.ReceivedDebit.failure_code](https://docs.stripe.com/api/treasury/received_debits/object#received_debit_object-failure_code)international_transactionAdded[Treasury.ReceivedCredit.failure_code](https://docs.stripe.com/api/treasury/received_credits/object#received_credit_object-failure_code)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
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

## Links

- [ReceivedDebit](https://docs.stripe.com/api/treasury/received_debits)
-
[Treasury.ReceivedDebit.failure_code](https://docs.stripe.com/api/treasury/received_debits/object#received_debit_object-failure_code)
-
[Treasury.ReceivedCredit.failure_code](https://docs.stripe.com/api/treasury/received_credits/object#received_credit_object-failure_code)
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