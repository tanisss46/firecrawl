# Allows Link card-only integrations to accept non-card payments under Link card brand

## What’s new

Adds support for `link` as an available card brand and network to expand support
for non-card payment methods to all Link integrations.

## Impact

Prior to this API version, if you accepted only `card` in your integration and
had Link turned on, you’d always get real cards. Now, you can get non-card
payment methods under the Link card brand with [different
properties](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-card-integrations).

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumslinkAdded[PaymentIntent#confirm.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network)[PaymentIntent#create.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card-network)[PaymentIntent#update.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-card-network)
+ 8 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-11-20.acacia`
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

- [Adds support for enabling Adaptive Pricing per Checkout
Session](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param)
- [Customize the submit button recurring Payment Links and Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)

## Links

- [different
properties](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-card-integrations)
-
[PaymentIntent#confirm.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network)
-
[PaymentIntent#create.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card-network)
-
[PaymentIntent#update.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-card-network)
-
[PaymentIntent.payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-card-network)
-
[SetupIntent#confirm.payment_method_options.card.network](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-card-network)
-
[SetupIntent#create.payment_method_options.card.network](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-card-network)
-
[SetupIntent#update.payment_method_options.card.network](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_options-card-network)
-
[SetupIntent.payment_method_options.card.network](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options-card-network)
-
[Subscription#create.payment_settings.payment_method_options.card.network](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-payment_method_options-card-network)
-
[Subscription#update.payment_settings.payment_method_options.card.network](https://docs.stripe.com/api/subscriptions/update#update_subscription-payment_settings-payment_method_options-card-network)
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
- [Adds support for enabling Adaptive Pricing per Checkout
Session](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param)
- [Customize the submit button recurring Payment Links and Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)