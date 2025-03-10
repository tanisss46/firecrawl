# Adds support for enabling Adaptive Pricing per Checkout Session

## What’s new

We added support for enabling and disabling [Adaptive
Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing) per
Checkout Session with a new API parameter. This parameter overrides your
Adaptive Pricing [Dashboard
setting](https://dashboard.stripe.com/settings/adaptive-pricing).

## Impact

With this parameter, you can enable Adaptive Pricing programmatically per
session, allowing for incremental rollouts and granular control when working
with multiple integrations.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsadaptive_pricingAdded[Checkout.Session#create](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session)[Checkout.Session](https://docs.stripe.com/api/checkout/sessions/object)
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

- [Customize the submit button recurring Payment Links and Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)

## Links

- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)
- [Dashboard setting](https://dashboard.stripe.com/settings/adaptive-pricing)
-
[Checkout.Session#create](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session)
- [Checkout.Session](https://docs.stripe.com/api/checkout/sessions/object)
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
- [Customize the submit button recurring Payment Links and Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)