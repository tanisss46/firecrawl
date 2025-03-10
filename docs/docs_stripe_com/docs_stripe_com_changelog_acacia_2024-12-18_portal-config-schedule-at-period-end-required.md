# Billing Portal Configuration always returns period end date in responses

## What’s new

The [Customer Portal Configuration
API](https://docs.stripe.com/api/customer_portal/configurations) now always
includes the
[schedule_at_period_end](https://docs.stripe.com/api/customer_portal/configurations/update#update_portal_configuration-features-subscription_update-schedule_at_period_end)
property in API responses. This means that you don’t have to handle null values
in responses.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETFieldChangeFrom →
toBillingPortal.Configuration.features.subscription_update.schedule_at_period_endChanged`optional
→ required`
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
- [Modify trial subscriptions created by Payment
Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api)

## Links

- [Customer Portal Configuration
API](https://docs.stripe.com/api/customer_portal/configurations)
-
[schedule_at_period_end](https://docs.stripe.com/api/customer_portal/configurations/update#update_portal_configuration-features-subscription_update-schedule_at_period_end)
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
- [Modify trial subscriptions created by Payment
Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api)