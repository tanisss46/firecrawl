# Customize the submit button recurring Payment Links and Checkout Sessions

## What’s new

You can now [customize the submit
button](https://docs.stripe.com/payments/checkout/customization/behavior#submit-button)
for [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions) and
[Payment Links](https://docs.stripe.com/api/payment-link) with recurring items.

We added support for the
[submit_type](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-submit_type)
parameter when you create a Session where the
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
is set to `subscription`. This change also includes support for making updates
to the `submit_type` on existing Payment Links.

## Impact

Users can now [customize the behavior of
Checkout](https://docs.stripe.com/payments/checkout/customization/behavior?payment-ui=embedded-form#submit-button)
to use `donate` as the text for the submit button for recurring payments.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointssubmit_typeAdded[PaymentLink#update](https://docs.stripe.com/api/payment-link/update)ValueChangeEnumssubscribeAdded[Checkout.Session#create.submit_type](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-submit_type)[Checkout.Session.submit_type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-submit_type)[PaymentLink#create.submit_type](https://docs.stripe.com/api/payment-link/create#create_payment_link-submit_type)
+ 1 more
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
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)

## Links

- [customize the submit
button](https://docs.stripe.com/payments/checkout/customization/behavior#submit-button)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Payment Links](https://docs.stripe.com/api/payment-link)
-
[submit_type](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-submit_type)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
- [customize the behavior of
Checkout](https://docs.stripe.com/payments/checkout/customization/behavior?payment-ui=embedded-form#submit-button)
- [PaymentLink#update](https://docs.stripe.com/api/payment-link/update)
-
[Checkout.Session.submit_type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-submit_type)
-
[PaymentLink#create.submit_type](https://docs.stripe.com/api/payment-link/create#create_payment_link-submit_type)
-
[PaymentLink.submit_type](https://docs.stripe.com/api/payment-link/object#payment_link_object-submit_type)
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
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)