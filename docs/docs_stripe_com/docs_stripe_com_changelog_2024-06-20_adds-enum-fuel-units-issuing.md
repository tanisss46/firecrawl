# Adds enum values for fuel unitsBreaking changes

## What’s new

Adds new values to the [Issuing
Transaction](https://docs.stripe.com/api/issuing/transactions/object)
`purchase_details.fuel.unit` enum:

- `imperial_gallon`
- `kilogram`
- `pound`
- `charging_minute`
- `kilowatt_hour`

## Impact

Adds new values to the
[purchase_details.fuel.unit](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-purchase_details-fuel-unit)
property for the [Issuing
Transaction](https://docs.stripe.com/api/issuing/transactions) resource.

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

- [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions/object)
-
[purchase_details.fuel.unit](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-purchase_details-fuel-unit)
- [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions)
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