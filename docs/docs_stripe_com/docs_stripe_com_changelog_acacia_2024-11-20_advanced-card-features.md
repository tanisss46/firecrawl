# Adds support for advanced card features on Checkout Sessions

## What’s new

Adds advanced card features [incremental
authorization](https://docs.stripe.com/payments/incremental-authorization?platform=web&ui=stripe-hosted),
[extended
authorization](https://docs.stripe.com/payments/extended-authorization?platform=web&ui=stripe-hosted),
[multicapture](https://docs.stripe.com/payments/multicapture?platform=web&ui=stripe-hosted),
and
[overcapture](https://docs.stripe.com/payments/overcapture?platform=web&ui=stripe-hosted)
for
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
users creating `mode: 'payment'` and `capture_method: 'manual'` Checkout
Sessions.

## Impact

These features were previously only available for Payment Intents. Users can now
adapt to these [flexible payment
scenarios](https://docs.stripe.com/payments/flexible-payments) on Checkout
Sessions.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsrequest_extended_authorizationrequest_incremental_authorizationrequest_multicapturerequest_overcaptureAdded[Checkout.Session#create.payment_method_options.card](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card)[Checkout.Session.payment_method_options.card](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-card)
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
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)

## Links

- [incremental
authorization](https://docs.stripe.com/payments/incremental-authorization?platform=web&ui=stripe-hosted)
- [extended
authorization](https://docs.stripe.com/payments/extended-authorization?platform=web&ui=stripe-hosted)
-
[multicapture](https://docs.stripe.com/payments/multicapture?platform=web&ui=stripe-hosted)
-
[overcapture](https://docs.stripe.com/payments/overcapture?platform=web&ui=stripe-hosted)
-
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [flexible payment
scenarios](https://docs.stripe.com/payments/flexible-payments)
-
[Checkout.Session#create.payment_method_options.card](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card)
-
[Checkout.Session.payment_method_options.card](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-card)
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
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)