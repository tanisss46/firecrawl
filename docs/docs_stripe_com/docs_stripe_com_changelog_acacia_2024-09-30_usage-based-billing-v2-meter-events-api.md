# Adds Meter Event v2 API endpoints

## What’s new

Introduces the [Meter Event
Stream](https://docs.stripe.com/api/v2/billing-meter-stream) /v2 resource to
support high-throughput usage reporting. You can send up to 10k events per
second to a meter event stream. [Contact
sales](https://stripe.com/contact/sales) for higher rate-limits.

First, you must create a [Meter Event
Session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create)
to get a short-lived authentication token. You can then use the session
authentication token to report usage to the [Meter Event
Stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create).

Learn more about [API v2](https://docs.stripe.com/api-v2-overview).

## Impact

This meter event stream endpoint supports up to 100,000 events per second for a
single business, an increase compared to the [current /v1
endpoint](https://docs.stripe.com/api/billing/meter-event).

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETChangeResourcesAdded[V2.Billing.MeterEvents](https://docs.stripe.com/api/v2/billing-meter)[V2.Billing.MeterEventSession](https://docs.stripe.com/api/v2/billing-meter-stream)[V2.Billing.MeterEventStream](https://docs.stripe.com/api/v2/billing-meter-stream)
+ 1 more
 Endpoints

ChangeResourcescreateAdded[V2.Billing.MeterEvents](https://docs.stripe.com/api/v2/billing-meter)createAdded[V2.Billing.MeterEventSession](https://docs.stripe.com/api/v2/billing-meter-stream)createAdded[V2.Billing.MeterEventStream](https://docs.stripe.com/api/v2/billing-meter-stream)createAdded[V2.Billing.MeterEventAdjustments](https://docs.stripe.com/api/v2/billing-meter-adjustment)
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
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)

## Links

- [Meter Event Stream](https://docs.stripe.com/api/v2/billing-meter-stream)
- [Contact sales](https://stripe.com/contact/sales)
- [Meter Event
Session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create)
- [Meter Event
Stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create)
- [API v2](https://docs.stripe.com/api-v2-overview)
- [current /v1 endpoint](https://docs.stripe.com/api/billing/meter-event)
- [V2.Billing.MeterEvents](https://docs.stripe.com/api/v2/billing-meter)
-
[V2.Billing.MeterEventAdjustments](https://docs.stripe.com/api/v2/billing-meter-adjustment)
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
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)