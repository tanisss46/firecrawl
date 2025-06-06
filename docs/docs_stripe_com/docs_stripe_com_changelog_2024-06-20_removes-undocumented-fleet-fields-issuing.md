# Removes undocumented fleet fieldsBreaking changes

## What’s new

Removes the following undocumented `fleet` fields from the [Issuing
Transaction](https://docs.stripe.com/api/issuing/transactions/object) resource
in favor of their corresponding `_decimal` equivalents:

- `purchase_details.fleet.reported_breakdown.fuel.gross_amount`
- `purchase_details.fleet.reported_breakdown.non_fuel.gross_amount`
- `purchase_details.fleet.reported_breakdown.tax.local_amount`
- `purchase_details.fleet.reported_breakdown.tax.national_amount`

## Impact

This change removes undocumented fleet fields from the `Issuing Transaction`
resource, replacing them with decimal equivalents. You need to update your code
to use the new `_decimal` fields for more precise financial reporting.

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