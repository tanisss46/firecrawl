# Enables automatic payment methods by default for PaymentIntents and SetupIntentsBreaking changes

## What’s new

[PaymentIntents](https://docs.stripe.com/api/payment_intents) and
[SetupIntents](https://docs.stripe.com/api/setup_intents) now have
`automatic_payment_methods` enabled by default, which allows you to configure
payment method settings from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). The previous
default was to accept only card payments when both `payment_method_types` and
`automatic_payment_methods` were not specified. For more information, see the
[upgrade guide](https://docs.stripe.com/upgrades/manage-payment-methods).

- When confirming a PaymentIntent, you’re now required to provide a
`return_url`, unless `off_session=true`.
- When confirming a PaymentIntent, you can’t use `error_on_requires_action`. Use
`payment_method_types` with `error_on_requires_action` if you want to fail
payment attempts when PaymentIntents transition into `requires_action`.
- When confirming a SetupIntent, you’re now required to provide a `return_url`.
- You can bypass the `return_url` requirement using
`automatic_payment_methods[allow_redirects]=never`, this will automatically
filter payment methods that [require
redirect](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)
even if they’re enabled in the Dashboard.

## Impact

PaymentIntents and SetupIntents now use automatic payment methods by default,
allowing for configuration through the Stripe Dashboard.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2023-08-16`
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

- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [SetupIntents](https://docs.stripe.com/api/setup_intents)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [upgrade guide](https://docs.stripe.com/upgrades/manage-payment-methods)
- [require
redirect](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)
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