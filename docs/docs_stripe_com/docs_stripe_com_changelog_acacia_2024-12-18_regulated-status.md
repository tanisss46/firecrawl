# Adds regulated status field to card objects in several APIs

## What’s new

Provides the regulated status of a card, which indicates whether a card falls
under a regulated account range. You can see this status in the
`regulated_status` field of several API resources,
[Charge](https://docs.stripe.com/api/charges), [Payment
Methods](https://docs.stripe.com/api/payment_methods) and
[Tokens](https://docs.stripe.com/api/tokens).

## Impact

The regulated status indicates whether a card falls under a regulated account
range.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsregulated_statusAdded[Card](https://docs.stripe.com/api/issuing/cards/object)[Charge.payment_method_details.card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card)[ConfirmationToken.payment_method_preview.card](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card)
+ 1 more
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

- [Charge](https://docs.stripe.com/api/charges)
- [Payment Methods](https://docs.stripe.com/api/payment_methods)
- [Tokens](https://docs.stripe.com/api/tokens)
- [Card](https://docs.stripe.com/api/issuing/cards/object)
-
[Charge.payment_method_details.card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card)
-
[ConfirmationToken.payment_method_preview.card](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card)
-
[PaymentMethod.card](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card)
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