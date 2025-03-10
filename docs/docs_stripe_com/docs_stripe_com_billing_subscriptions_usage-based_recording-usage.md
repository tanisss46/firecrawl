# Record usage for billing

## Learn how to record customer usage data.

Throughout each billing period, you must record usage in Stripe to bill your
customers the correct amounts. You can decide how often you record usage in
Stripe.

To record usage in Stripe, first [configure your
meter](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter)
and then add the recorded usage through the Stripe Dashboard or API.

## Configure your meter

Before you can record customer usage, you must configure your
[Meter](https://docs.stripe.com/api/billing/meter/object). After you configure
the meter, you can’t make any changes aside from the display name.

Meter attributeDescriptionEvent nameThe name of the meter event that you want to
record usage for with the meter. When you send usage to Stripe, specify this
event name in the `event_name` field for the [Meter
Event](https://docs.stripe.com/api/billing/meter-event/object). This allows the
correct meter to record and aggregate the usage. You can only use an event name
with a single meter.
Event ingestion

Specify how to send events to Stripe:

- **Raw**: Handle all meter events as standalone events. Multiple events sent
for the same timestamp don’t overwrite each other. The aggregation includes the
multiple events. This is the default option if you don’t specify anything.
- **Pre-aggregated**: If you send events for a specific time interval (hourly or
daily), Stripe only uses the most recently received meter event in that time
interval. A newer event sent within the same hourly or daily window overwrites
the previous one. The meter event timestamp in UTC dictates the hour and day
boundaries.

Aggregation formula

Specify how to aggregate usage over the billing period:

- **Sum**: Bill customers based on the sum of all usage values for the billing
period.
- **Count**: Bill customers based on the count of all usage for the billing
period.

Payload key overrides

Specify which keys in the event payload refer to the customer and numerical
usage values:

- **value_settings**: Use this parameter to define the key in the event payload
that refers to the numerical usage value. The default key is `value`, but you
can specify a different key, such as tokens.
- **customer_mapping**: Use this parameter to define the key in the event
payload that refers to the [Customer
ID](https://docs.stripe.com/api/customers/object#customer_object-id). The
default key is `stripe_customer_id`, but you can specify a different key, such
as `customer_id`.

## Record usage

Record usage in Stripe using the Dashboard or API.

Stripe processes meter events asynchronously, so aggregated usage in meter event
summaries and on upcoming invoices might not immediately reflect recently
received meter events.

[Using the APIUse the Stripe API to record customer usage
data.](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api)[Using
the Stripe DashboardUse the Dashboard to upload a CSV file with usage
data.](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk-dashboard)[Using
Amazon S3Use Amazon S3 to add customer usage data in
bulk.](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk)
## Fix incorrect usage data

If you identify incorrectly recorded events in the current billing period, you
can create a [Meter Event
Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment/create)
to cancel those events. You must specify the
[identifier](https://docs.stripe.com/api/billing/meter-event/object#billing_meter_event_object-identifier)
for the meter event.

You can only cancel events sent to Stripe within the last 24 hours. If you
cancel usage that’s included on a finalized invoice, we won’t update the invoice
or issue a corrected invoice for the canceled usage. We don’t support billing
adjustments for canceled usage on a finalized invoice sent to a customer.

You can also fix incorrectly recorded usage data by recording negative
quantities. If the overall cycle usage is negative, Stripe reports the invoice
line item usage quantity as 0.

```
curl https://api.stripe.com/v1/billing/meter_event_adjustments \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=cancel \
 -d event_name=alpaca_ai_tokens \
 -d "cancel[identifier]"={{METER_EVENT_IDENTIFIER}}
```

## Links

- [legacy
documentation](https://docs.stripe.com/billing/subscriptions/usage-based-legacy)
- [configure your
meter](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter)
- [Meter](https://docs.stripe.com/api/billing/meter/object)
- [Meter Event](https://docs.stripe.com/api/billing/meter-event/object)
- [Customer ID](https://docs.stripe.com/api/customers/object#customer_object-id)
- [Using the APIUse the Stripe API to record customer usage
data.](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api)
- [Using the Stripe DashboardUse the Dashboard to upload a CSV file with usage
data.](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk-dashboard)
- [Using Amazon S3Use Amazon S3 to add customer usage data in
bulk.](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk)
- [Meter Event
Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment/create)
-
[identifier](https://docs.stripe.com/api/billing/meter-event/object#billing_meter_event_object-identifier)