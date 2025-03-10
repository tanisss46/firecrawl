# Migrate to billing meters

## Learn how to migrate from usage records to billing meters.

Stripe is deprecating usage-records billing. Moving forward, you can migrate to
billing meters, our only solution for usage-based billing. Billing meters
provide the following advantages:

- High-throughput usage reporting
- One-hour reporting [grace
period](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period)
for generating invoices
- [Collect
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#record-usage)
before creating a subscription

However, we don’t support the following features:

- `max`, `last_ever`, and `last_during_period`
[aggregation](https://docs.stripe.com/api/prices/object#price_object-recurring)
- Reporting usage in the Dashboard

You can continue to use usage records as you adopt billing meters.

## Billing meter overview

Billing meters allow you to track usage of a particular event. It supports
high-throughput event ingestion and aggregation.

Unlike usage records, billing meters don’t require customers to have
subscriptions before reporting usage and a single meter can track usage across
multiple customers.

Learn more about billing meters in our [implementation
guide](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide).

[Create a
meter](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide#create-meter)
Create a [billing meter](https://docs.stripe.com/api/billing/meter). Learn more
about [configuring
meters](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter).

```
curl https://api.stripe.com/v1/billing/meters \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d display_name="Alpaca AI" \
 -d event_name=api_request \
 -d "default_aggregation[formula]"=sum
```

[Create a new
price](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide#create-price)
Create a new price associated with the billing meter. Make sure that the new
price is on the same product as your old price.

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d product={{PRODUCT_ID}} \
 -d "recurring[interval]"=month \
 -d "recurring[usage_type]"=metered \
 -d "recurring[meter]"={{METER_ID}} \
 -d currency=usd \
 -d unit_amount=100
```

[Start recording
usage](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide#start-recording-usage)
#### Note

You must continue to send [usage
records](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/recording-usage)
to Stripe until the migration is completed.

Start reporting usage to the Billing Meter API. Stripe doesn’t reflect this
usage on customer invoices until they’re subscribed to the new price.

```
curl https://api.stripe.com/v1/billing/meter_events \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d event_name=api_request \
 -d timestamp=1712096183 \
 -d identifier={{IDEMPOTENCY_KEY}} \
 -d "payload[stripe_customer_id]"={{CUSTOMER_ID}} \
 -d "payload[value]"=1
```

Learn more about [recording
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#record-usage).

[OptionalQuery reported
usage](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide#query-reported-usage)[Plan
subscription
schedules](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide#plan-subscription-schedules)
Use subscription schedules to automatically migrate to the new price at the end
of the billing cycle. Learn more about [subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules).

List the subscriptions associated with the old price.

```
curl -G https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d price={{OLD_PRICE_ID}} \
 -d "expand[]"="data.schedule"
```

Stripe returns a list of subscriptions associated with the old price. For
example:

```
{
 "object": "list",
 "data": [
 {
 "id": "sub_1P1Y6gDxxK6kAaV0rS7ojBjh",
 "object": "subscription",
 ...
 "items": {
 "object": "list",
 "data": [
 {
 "id": "si_PrGdqMmuM1DGbQ",
 "object": "subscription_item",
 ...
 "price": {
 "id": "{{OLD_PRICE_ID}}",
 "object": "price",
 ...
 "recurring": {
 "aggregate_usage": "sum",
 "interval": "month",
 "interval_count": 1,
 "trial_period_days": null,
 "usage_type": "metered"
 },
 ...
 },
 ...
 }
 ],
 ...
 },
 ...
 "schedule": {
 "id": "sub_sched_1P1XxjDxxK6kAaV0YygN4tf7",
 "object": "subscription_schedule",
 ...
 "current_phase": {
 "end_date": 1714759200,
 "start_date": 1712167200
 },
 ...
 "phases": [
 {
 ...
 "end_date": 1714759200,
 ...
 "items": [
 {
 ...
 "price": "{{OLD_PRICE_ID}}",
 ...
 }
 ],
 ...
 "start_date": 1712167200,
 ...
 "trial_end": 1712772000
 }
 ],
 ...
 },
 ...
 },
 ...
 ],
 "has_more": false,
 "url": "/v1/subscriptions"
}
```

If a subscription has a
[schedule](https://docs.stripe.com/api/subscriptions/object#subscription_object-schedule),
you must update the existing [subscription
schedule](https://docs.stripe.com/api/subscription_schedules) to migrate to the
new price at the end of a billing cycle. If no schedule exists for a
subscription, create a new one.

Create subscription schedulesUpdate existing subscription schedules
Create a subscription schedule for each subscription associated with the old
price.

```
curl https://api.stripe.com/v1/subscription_schedules \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d from_subscription={{SUBSCRIPTION_ID}}
```

Stripe returns a new subscription schedule object:

```
{
 "id": "sub_sched_1P1H37DxxK6kAaV0Iggc537m",
 "object": "subscription_schedule",
 ...
 "current_phase": {
 "end_date": 1714693634,
 "start_date": 1712101634
 },
 ...
 "phases": [
 {
 ...
 "end_date": 1714693634,
 ...
 "items": [
 {
 ...
 "price": "{{OLD_PRICE_ID}}",
 ...
 }
 ],
 ...
 "start_date": 1712101634,
 ...
 }
 ],
 ...
 "status": "active",
 ...
}
```

Update the subscription schedule to add a `phase` with the new price.

```
curl
https://api.stripe.com/v1/subscription_schedules/sub_sched_1P1H37DxxK6kAaV0Iggc537m
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "phases[0][start_date]"=1712101634 \
 -d "phases[0][end_date]"=1714693634 \
 -d "phases[0][items][0][price]"={{OLD_PRICE_ID}} \
 -d "phases[1][items][0][price]"={{NEW_PRICE_ID}}
```

## Test the migration

Create a test customer with a subscription associated with the old price.

DashboardAPI- Navigate to the [Customers
tab](https://dashboard.stripe.com/test/customers).
- Click **+ Add customer**.
- Enter the name of the customer.
- Navigate to the new customer.
- Next to the Subscriptions header, click **+** to open the subscription drawer.
- Select the old price.
- Click **Create test subscription**.

Create a subscription schedule from the subscription.

```
curl https://api.stripe.com/v1/subscription_schedules \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d from_subscription={{SUBSCRIPTION_ID}}
```

Add a `phase` to the subscription schedule to migrate to the new price.

```
curl
https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "phases[0][start_date]"=1710952582 \
 -d "phases[0][end_date]"=1713630982 \
 -d "phases[0][items][0][price]"={{OLD_PRICE_ID}} \
 -d "phases[1][items][0][price]"={{NEW_PRICE_ID}}
```

[Simulate the subscription
change](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions)
with a test clock.

Learn more about [testing subscriptions
integrations](https://docs.stripe.com/billing/testing). You can use test clocks
to test different scenarios, including mock usage reporting. Learn more about
[test clocks](https://docs.stripe.com/billing/testing/test-clocks).

## Links

- [grace
period](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period)
- [Collect
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#record-usage)
-
[aggregation](https://docs.stripe.com/api/prices/object#price_object-recurring)
- [implementation
guide](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide)
- [billing meter](https://docs.stripe.com/api/billing/meter)
- [configuring
meters](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter)
- [usage
records](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/recording-usage)
- [subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
-
[schedule](https://docs.stripe.com/api/subscriptions/object#subscription_object-schedule)
- [subscription schedule](https://docs.stripe.com/api/subscription_schedules)
- [Customers tab](https://dashboard.stripe.com/test/customers)
- [Simulate the subscription
change](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions)
- [testing subscriptions integrations](https://docs.stripe.com/billing/testing)
- [test clocks](https://docs.stripe.com/billing/testing/test-clocks)