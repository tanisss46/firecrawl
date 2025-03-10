# Adds support for retrieving thin events

## What’s new

You can now [retrieve thin
Event](https://docs.stripe.com/api/v2/core/events/retrieve) objects for each
notification from the `/v2/core/events` endpoint.

Thin events are lightweight events you can access through the [API
v2](https://docs.stripe.com/api-v2-overview) API. Thin events have a more
granular permissions model and their payloads contain no API-versioned data.
This makes it easier to update integrations that receive events and are built
with a well-typed Stripe SDK. Thin Event objects include a `data` property that
can include additional information about the event.

The [Meters API](https://docs.stripe.com/api/billing/meter) is the first API to
use thin events. Currently, you can only retrieve the following [Events
v2](https://docs.stripe.com/api/v2/events) related to [usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based):

-
[v1.billing.meter.error_report_triggered](https://docs.stripe.com/api/v2/core/events/event-types#v2_types_events-v1.billing.meter.error_report_triggered)
-
[v1.billing.meter.no_meter_found](https://docs.stripe.com/api/v2/core/events/event-types#v2_types_events-v1.billing.meter.no_meter_found)

Here’s an example of an `v1.billing.meter.error_report_triggered` event. The
`related_object` field includes the `id` of the object, but doesn’t include the
object record itself.

```
{
 "id": "evt_test_65R9Ijk8dKEYZcXeRWn16R9A7j1FSQ3w3TGDPLLGSM4CW0",
 "object": "v2.core.event",
 "type": "v1.billing.meter.error_report_triggered",
 "livemode": false,
 "created": "2024-09-17T06:20:52.246Z",
 "related_object": {
 "id": "mtr_test_61R9IeP0SgKbYROOx41PEAQhH0qO23oW",
 "type": "billing.meter",
 "url": "/v1/billing/meters/mtr_test_61R9IeP0SgKbYROOx41PEAQhH0qO23oW"
 }
}
```

Learn more about
[events](https://docs.stripe.com/event-destinations#events-overview).

## Impact

Thin events have several benefits. They make it easier to maintain future
webhook integrations because the payloads are unversioned. You can send thin
events to [event destinations](https://docs.stripe.com/event-destinations). Thin
events are fully typed in the SDKs for API v2. Finally, if your application
needs a corresponding API object related to an event (for example, the
[Meter](https://docs.stripe.com/api/billing/meter/retrieve)), you must call the
Stripe API for the object’s latest state. This helps prevent application errors
caused by outdated object data (for example, race conditions). The SDKs for API
v2 contain helper methods that allow you to retrieve records associated with an
event.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETChangeResourceAdded[V2.Event](https://docs.stripe.com/api/v2/events)
 Endpoints

ChangeResourceretrievelistAdded[V2.Event](https://docs.stripe.com/api/v2/events)
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

## Links

- [retrieve thin Event](https://docs.stripe.com/api/v2/core/events/retrieve)
- [API v2](https://docs.stripe.com/api-v2-overview)
- [Meters API](https://docs.stripe.com/api/billing/meter)
- [Events v2](https://docs.stripe.com/api/v2/events)
- [usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)
-
[v1.billing.meter.error_report_triggered](https://docs.stripe.com/api/v2/core/events/event-types#v2_types_events-v1.billing.meter.error_report_triggered)
-
[v1.billing.meter.no_meter_found](https://docs.stripe.com/api/v2/core/events/event-types#v2_types_events-v1.billing.meter.no_meter_found)
- [events](https://docs.stripe.com/event-destinations#events-overview)
- [event destinations](https://docs.stripe.com/event-destinations)
- [Meter](https://docs.stripe.com/api/billing/meter/retrieve)
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