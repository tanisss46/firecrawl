# One-off Invoices no longer automatically collect payment by defaultBreaking changes

## What’s new

`auto_advance` now also defaults to `false` for one-off invoices, allowing you
to control how long their
[status](https://docs.stripe.com/invoicing/overview#invoice-statuses) stays a
`draft`. To learn more, see [Automatic advancement
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection).

## Impact

Seting the default `auto_advance` value to `false` for one-off invoices gives
you more control over how long these invoices remain in draft status. You can
now manually manage the advancement of one-off invoices, potentially allowing
for more review time or customization before finalization.

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

- [status](https://docs.stripe.com/invoicing/overview#invoice-statuses)
- [Automatic advancement
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
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