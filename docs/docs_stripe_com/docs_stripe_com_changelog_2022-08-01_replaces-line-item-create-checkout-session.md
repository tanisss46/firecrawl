# Replaces line item parameters from the Create Checkout Session endpointBreaking changes

## What’s new

Removes the following parameters from the [Create Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create) endpoint:

- `line_items[amount]`
- `line_items[currency]`
- `line_items[name]`
- `line_items[description]`
- `line_items[images]`

Use the `price` and `price_data` parameters instead.

## Impact

Defines line items for Checkout Sessions using the `price` and `price_data`
parameters, instead of the previously available individual `line_items`
parameters. This simplifies the Checkout Session creation process by providing a
more consolidated way to specify line item details.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2022-08-01`
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

- [Create Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create)
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