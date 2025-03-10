# Removes deprecated tax information fields from the Customer objectBreaking changes

## What’s new

Deprecates tax information for `Customers`. To learn more, see the [migration
guide](https://docs.stripe.com/billing/taxes/tax-rates#migration).

- Removes the deprecated `tax_info` and `tax_info_verification` fields on the
`Customer` object in favor of `tax_ids`.
- Removes the deprecated `tax_info` parameter on the `Customer` create and
update methods in favor of `tax_id_data`.

## Impact

This change simplifies the `Customer` object and associated methods by removing
the deprecated `tax_info` and `tax_info_verification` fields in favor of the
`tax_ids` field. This consolidation and removal of deprecated fields lets you
work with a more streamlined and up-to-date `Customer` object, aligning with
Stripe’s latest tax handling capabilities.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-12-03`
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

- [migration guide](https://docs.stripe.com/billing/taxes/tax-rates#migration)
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