# Record usage for billing with the API

## Learn how to record usage using the Stripe API.

You must record usage in Stripe in order to bill your customers the correct
amounts each billing period. To record usage, first [configure your
meter](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter),
and then send meter events that include the event name configured on the meter,
customer ID, numerical value, and a timestamp (optional).

You can decide how often you record usage in Stripe, for example as it occurs or
in batches. Stripe processes meter events asynchronously, so aggregated usage in
meter event summaries and on upcoming invoices might not immediately reflect
recently received meter events.

## Create meter events

Create a [Meter Event](https://docs.stripe.com/api/billing/meter-event/create)
using the API.

```
curl https://api.stripe.com/v1/billing/meter_events \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d event_name=alpaca_ai_tokens \
 -d "payload[value]"=25 \
 -d "payload[stripe_customer_id]"={{CUSTOMER_ID}}
```

### Idempotency

Use [idempotency keys](https://docs.stripe.com/api/idempotent_requests) to
prevent reporting usage for each event more than one time because of latency or
other issues. Every meter event corresponds to an
[identifier](https://docs.stripe.com/api/billing/meter-event/create#create_billing_meter_event-identifier)
that you can specify in your request. If you don’t specify an identifier, we
auto-generate one for you.

### Event timestamps

Make sure the timestamp is within the past 35 calendar days and isn’t more than
5 minutes in the future. The 5-minute window is for clock drift between your
server and Stripe systems.

### Usage values

The numerical usage value in the payload only accepts whole number values. If
the overall cycle usage is negative, Stripe reports the invoice line item usage
quantity as 0.

### Rate limits

The [Meter Event](https://docs.stripe.com/api/billing/meter-event/create)
endpoint allows 1000 calls per second in live mode, and one concurrent call per
customer per meter. If your service might exceed this limit, you can “bundle”
your product into amounts. For example, if you charge per 1000 requests, you can
bundle your product into “per 1000 transactions” and then send 1 usage record
every 1000 times.

In test mode and sandbox mode, calls to the `meter event` and `meter event
stream` endpoint count toward the [basic
limit](https://docs.stripe.com/rate-limits#rate-limiter).

#### Note

If you’re a Connect platform making requests on behalf of a connected account
using the `Stripe-Account` header, you’re subject to [regular Stripe rate
limits](https://docs.stripe.com/rate-limits), which is 100 operations per
second.

You can monitor for `429` status codes and implement a retry mechanism with an
exponential back-off schedule to manage request volume.

### High-throughput ingestion with higher rate limits API v2

With the [API v2](https://docs.stripe.com/api-v2-overview), you can send up to
10,000 events per second to Stripe using meter event streams. This works in live
mode only.

This endpoint uses stateless authentication sessions. First, create a [Meter
Event
Session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create)
to receive an authentication token. Authentication tokens are only valid for 15
minutes, so you must create a new meter event session when your token expires.

Next, use the returned authentication token to create your high-throughput meter
events with the [Meter Event
Stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create).

#### Note

Because of the large volume of API requests, we don’t include meter event stream
requests in the [Workbench Logs
tab](https://docs.stripe.com/workbench#request-logs).

You can monitor for `429` status codes and implement a retry mechanism with an
exponential backoff schedule to manage request volume.

```
require 'stripe'
require 'date'

class MeterEventManager
 attr_accessor :api_key
 attr_accessor :meter_event_session

 def initialize(api_key)
 @api_key = api_key
 @meter_event_session = nil
```

See all 47 lines
## Handle meter event errors

Stripe asynchronously processes meter events. If we find an error, we create one
of the following [Events](https://docs.stripe.com/api/events):

EventDescriptionPayload type`v1.billing.meter.error_report_triggered`This event
occurs when a meter has invalid usage
events.`thin``v1.billing.meter.no_meter_found`This event occurs when usage
events have missing or invalid meter IDs.`thin`
#### Warning

To create an event destination that subscribes to thin events, enable Workbench
in your [Developer settings](https://dashboard.stripe.com/settings/developers).

### Example payloads

Example error report eventExample error event for an incorrect meter
The following is an example payload for a
`v1.billing.meter.error_report_triggered` event.

```
{
 "id": "evt_test_65R2GpwDsnmpzihMjdT16R2GDhI4SQdXJGRbvn7JA8mPEm",
 "object": "v2.core.event",
 "created": "2024-08-28T20:54:12.051Z",
 "data": {
 "developer_message_summary": "There is 1 invalid event",
 "reason": {
 "error_count": 1,
 "error_types": [
 {
```

See all 35 lines
### Error codes

The `reason.error_types.code` provides the error categorization that triggered
the error. Possible error codes include:

- `meter_event_customer_not_found`
- `meter_event_no_customer_defined`
- `meter_event_dimension_count_too_high`
- `archived_meter`
- `timestamp_too_far_in_past`
- `timestamp_in_future`
- `meter_event_value_not_found`
- `meter_event_invalid_value`
- `no_meter` (supported only for the `v1.billing.meter.no_meter_found` event
type)

### Listen to events

You can listen to events by setting up a [webhook endpoint or another type of
event destination](https://docs.stripe.com/event-destinations).

- On the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench,
click **Create new destination**. Alternatively, use this
[template](https://dashboard.stripe.com/webhooks/create?payload_style=thin&events=v1.billing.meter.error_report_triggered%2Cv1.billing.meter.no_meter_found)
to configure a new destination in Workbench with the two event types
pre-selected.
- Click **Show advanced options**, then select the **Thin** payload style.
- Select `v1.billing.meter.error_report_triggered` and
`v1.billing.meter.no_meter_found` from the list of events.
- Create a handler to process the event.

```
import os
from stripe import StripeClient
from stripe.events import V1BillingMeterErrorReportTriggeredEvent

from flask import Flask, request, jsonify

app = Flask(__name__)
api_key = os.environ.get('STRIPE_API_KEY')
webhook_secret = os.environ.get('WEBHOOK_SECRET')

```

See all 35 lines
- Test your handler by configuring a [local
listener](https://docs.stripe.com/cli/listen) with the [Stripe
CLI](https://docs.stripe.com/stripe-cli) to send events to your local machine
for testing before deploying the handler to production. Use the
`--forward-thin-to` flag to specify which URL to forward the `thin` events to
and the `--thin-events` flag to specify which thin events to forward. You can
forward all thin events with an asterisk (`*`), or a subset of thin events to
your application.

```
$ stripe listen --forward-thin-to localhost:4242/webhooks --thin-events "*"

```
- Trigger test events to your handler. Use the [trigger
function](https://docs.stripe.com/cli/trigger) to run the following commands,
which simulates the respective events in your account for testing.

```
$ stripe trigger v1.billing.meter.error_report_triggered --api-key
<your-secret-key>
$ stripe trigger v1.billing.meter.no_meter_found --api-key <your-secret-key>

```
- If you process events with a webhook endpoint, [verify the webhook
signatures](https://docs.stripe.com/webhooks#verify-official-libraries) to
secure your endpoint and validate all requests are from Stripe.
- Correct and resend invalid events for re-processing.

## Links

- [configure your
meter](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter)
- [Meter Event](https://docs.stripe.com/api/billing/meter-event/create)
- [idempotency keys](https://docs.stripe.com/api/idempotent_requests)
-
[identifier](https://docs.stripe.com/api/billing/meter-event/create#create_billing_meter_event-identifier)
- [basic limit](https://docs.stripe.com/rate-limits#rate-limiter)
- [regular Stripe rate limits](https://docs.stripe.com/rate-limits)
- [API v2](https://docs.stripe.com/api-v2-overview)
- [Contact sales](https://stripe.com/contact/sales)
- [Meter Event
Session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create)
- [Meter Event
Stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create)
- [Workbench Logs tab](https://docs.stripe.com/workbench#request-logs)
- [Events](https://docs.stripe.com/api/events)
- [Developer settings](https://dashboard.stripe.com/settings/developers)
- [webhook endpoint or another type of event
destination](https://docs.stripe.com/event-destinations)
- [Webhooks](https://dashboard.stripe.com/webhooks)
-
[template](https://dashboard.stripe.com/webhooks/create?payload_style=thin&events=v1.billing.meter.error_report_triggered%2Cv1.billing.meter.no_meter_found)
- [local listener](https://docs.stripe.com/cli/listen)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [trigger function](https://docs.stripe.com/cli/trigger)
- [verify the webhook
signatures](https://docs.stripe.com/webhooks#verify-official-libraries)