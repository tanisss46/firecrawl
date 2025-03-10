# Modify trial subscriptions created by Payment Links

## What’s new

Updates the
[subscription_data.trial_period_days](https://docs.stripe.com/api/payment-link/create#create_payment_link-subscription_data-trial_period_days)
parameter so that it adjusts the number of free trial days for subscriptions
created by that Payment Link.

## Impact

You can now modify the length of free trial days for subscriptions created by a
Payment Link. This change affects only subscriptions created after updating this
value, leaving existing subscriptions unchanged.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointstrial_period_daysAdded[PaymentLink#update.subscription_data](https://docs.stripe.com/api/payment-link/update)
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

## Related changes

- [Adds support for reinstating Billing Credits on Invoice
voiding](https://docs.stripe.com/changelog/acacia/2024-12-18/billing-credits-invoice-voiding)
- [Billing Portal Configuration always returns period end date in
responses](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required)

## Links

-
[subscription_data.trial_period_days](https://docs.stripe.com/api/payment-link/create#create_payment_link-subscription_data-trial_period_days)
-
[PaymentLink#update.subscription_data](https://docs.stripe.com/api/payment-link/update)
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
- [Adds support for reinstating Billing Credits on Invoice
voiding](https://docs.stripe.com/changelog/acacia/2024-12-18/billing-credits-invoice-voiding)
- [Billing Portal Configuration always returns period end date in
responses](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required)