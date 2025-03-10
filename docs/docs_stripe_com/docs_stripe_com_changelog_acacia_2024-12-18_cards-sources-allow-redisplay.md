# Supports redisplaying payment methods for Cards and Sources

## What’s new

Supports `allow_redisplay` on [Cards](https://docs.stripe.com/api/cards) and
[Sources](https://docs.stripe.com/api/sources) through the [v1/payment_method
update](https://docs.stripe.com/api/payment_methods/update) endpoint.

## Impact

This field indicates whether this payment method can be shown again to its
customer in a checkout flow. Stripe products such as Checkout and Elements use
this field to determine whether a payment method can be shown as a saved payment
method in a checkout flow.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsallow_redisplayAdded[Card](https://docs.stripe.com/api/issuing/cards/object)[Source](https://docs.stripe.com/api/sources/object)
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

## Links

- [Cards](https://docs.stripe.com/api/cards)
- [Sources](https://docs.stripe.com/api/sources)
- [v1/payment_method update](https://docs.stripe.com/api/payment_methods/update)
- [Card](https://docs.stripe.com/api/issuing/cards/object)
- [Source](https://docs.stripe.com/api/sources/object)
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