# Lets the description and email fields be null on several objectsBreaking changes

## What’s new

Allows the `description` property on `Customer`, `Charge`, `InvoiceItem`, and
`Recipient` objects, and the `email` property on `Customer` and `Recipient`
objects, to be set to null by providing empty string values in POST requests.

## Impact

Allows setting `description` and `email` to null on various objects, providing
more flexibility in how you manage data.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2013-08-12`
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