# Adds billing alert resources and endpoints

## What’s new

Adds new methods for activating, archiving, creating, deactivating, listing, and
retrieving the new [Alert](https://docs.stripe.com/api/billing/alert) resource.

## Impact

Lets you configure and manage [usage-based billing
alerts](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds).
With these new methods, you can set up a webhook and [listen to
events](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#listen-for-webhooks)
and take actions based on your customers’ billing usage.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NET
 Endpoints

ChangeResourceactivatearchivecreatedeactivatelistretrieveAdded[Billing.Alert](https://docs.stripe.com/api/billing/alert/object)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
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

- [Adds contextual filters to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters)
- [Adds an Alerts API for usage-based
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)

## Links

- [Alert](https://docs.stripe.com/api/billing/alert)
- [usage-based billing
alerts](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds)
- [listen to
events](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#listen-for-webhooks)
- [Billing.Alert](https://docs.stripe.com/api/billing/alert/object)
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
- [Adds contextual filters to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters)
- [Adds an Alerts API for usage-based
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)