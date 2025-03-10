# Adds specific error codes for failed Klarna paymentsBreaking changes

## What’s new

Adds more specific error codes to the
[PaymentIntent](https://docs.stripe.com/api/payment_intents) API for when a
[Klarna](https://docs.stripe.com/payments/klarna) payment fails:

- `payment_method_customer_decline`
- `payment_method_not_available`
- `payment_method_provider_decline`
- `payment_intent_payment_attempt_expired`

## Impact

Adding specific error codes for when a
[Klarna](https://docs.stripe.com/payments/klarna) payment fails gives you more
detailed information about why the payment failed, enabling better error
handling.

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

- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [Klarna](https://docs.stripe.com/payments/klarna)
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