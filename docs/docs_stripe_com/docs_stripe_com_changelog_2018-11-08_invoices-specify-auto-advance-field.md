# Invoices now specify their automatic collection behavior using the auto_advance fieldBreaking changes

## What’s new

The `closed` property on the [Invoice](https://docs.stripe.com/api/invoices)
object controls [automatic
collection](https://docs.stripe.com/invoicing/overview#invoice-lifecycle).
Deprecates `closed` in favor of the more specific `auto_advance` field. Where
you might have set `closed=true` on invoices in the past, set it to
`auto_advance=false`.

## Impact

Replacing the `closed` property with the new `auto_advance` field on `Invoice`
objects to control automatic collection lets you have more specific control over
the invoice lifecycle, allowing you to use `auto_advance=false` instead of
`closed=true` to prevent automatic collection.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2018-11-08`
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

- [Invoice](https://docs.stripe.com/api/invoices)
- [automatic
collection](https://docs.stripe.com/invoicing/overview#invoice-lifecycle)
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