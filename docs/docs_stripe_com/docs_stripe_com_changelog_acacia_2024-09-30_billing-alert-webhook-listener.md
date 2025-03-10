# Adds support for listening to triggered billing alerts

## What’s new

Adds support for creating listeners for the new
[billing.alert.triggered](https://docs.stripe.com/api/events/types#event_types-billing.alert.triggered)
event type.

## Impact

Lets you create or update webhook
[listeners](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#listen-for-webhooks)
with the new
[billing.alert.triggered](https://docs.stripe.com/api/events/types#event_types-billing.alert.triggered)event
type.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsbilling.alert.triggeredAdded[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)

## Links

-
[billing.alert.triggered](https://docs.stripe.com/api/events/types#event_types-billing.alert.triggered)
-
[listeners](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#listen-for-webhooks)
-
[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)
-
[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)