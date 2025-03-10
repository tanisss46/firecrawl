# Deprecates the bank_transfer_payments capability type in favor of newer capability typesBreaking changes

## What’s new

Deprecates the `bank_transfer_payments` capability type in favor of newer
capability types per buyer’s location in the Capabilities API. The newer
capability types are:

- `gb_bank_transfer_payments` for UK Bank Transfers (GBP customer balance
payments)
- `jp_bank_transfer_payments` for JP Bank Transfers (JPY customer balance
payments)
- `mx_bank_transfer_payments` for MX Bank Transfers (MXN customer balance
payments)
- `sepa_bank_transfer_payments` for SEPA Bank Transfers (EUR customer balance
payments)
- `us_bank_transfer_payments` for USD Bank Transfers (USD customer balance
payments)

## Impact

Deprecates the the `bank_transfer_payments` capability type in favor of newer
capability types per buyer’s location in the Capabilities API. This gives you
more specific, location-based capabilities.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-06-20`
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