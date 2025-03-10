# Adds discounts field to Checkout Sessions

## What’s new

Adds the
[discounts](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-discounts)
field to the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/object) object. The
`discounts` field is an array of discounts applied to the Checkout Session.

## Impact

You can use `discounts` to retrieve the discounts applied to a Checkout Session,
including those applied by you or the customer when creating the Checkout
Session.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsdiscountsAdded[Checkout.Session](https://docs.stripe.com/api/checkout/sessions/object)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2025-01-27.acacia`
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

## Related changes

- [Adds Sudan to allowed shipping countries for
Checkout](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sudan-shipping-support)

## Links

-
[discounts](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-discounts)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object)
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
- [Adds Sudan to allowed shipping countries for
Checkout](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sudan-shipping-support)