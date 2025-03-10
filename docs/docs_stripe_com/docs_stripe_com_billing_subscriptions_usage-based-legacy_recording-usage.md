# Record usage for billingLegacy

## Learn how to record and report usage for your customers.

#### Note

We’ve updated the way usage-based billing works. See the [updated usage-based
billing docs](https://docs.stripe.com/billing/subscriptions/usage-based).

Learn how to
[migrate](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide).

Throughout each billing period, you need to report usage to Stripe so that
customers are billed the correct amounts. You can maintain your own system for
recording customer usage and provide usage information for subscriptions to
Stripe.

You can share usage information with Stripe by creating [usage
records](https://docs.stripe.com/api#usage_record_create) with a subscription
item, quantity used, and a timestamp. How often you report usage is up to you.
For example, you can run the code on an interval (for example, every 24 hours)
for each active metered subscription. At the end of the billing period, Stripe
automatically calculates the total price and
[invoices](https://docs.stripe.com/billing/invoices/subscription) for all usage
during the billing period.

```
curl
https://api.stripe.com/v1/subscription_items/{{SUBSCRIPTION_ITEM_ID}}/usage_records
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X POST \
 -d quantity=100 \
 -d timestamp=1741539399 \
 -d action=increment
```

## Best practices for recording usage

- You need to write some of your own business logic before creating the usage
record. Pull a record of a customer from your database and extract the
customer’s Stripe subscription item ID and usage for the day. If you aren’t
storing subscription item IDs, retrieve the subscription and check for
[subscription
items](https://docs.stripe.com/api/subscriptions/object#subscription_object-items).
- Use [idempotency keys](https://docs.stripe.com/api/idempotent_requests) to
ensure usage isn’t reported more than once in case of latency or other issues.
- The `timestamp` has to be within the current billing period, otherwise the
call fails.
- The default value for the `action` parameter is `increment`. This value
assumes that the price is configured with `aggregate_usage=sum` and that you
write usage as it occurs, passing it to Stripe with the current `timestamp`.
- A `set` value for the `action` parameter supports the case where you aggregate
usage yourself, and configure the price with
`aggregate_usage=last_during_period` or `aggregate_usage=last_ever`.
- The usage reporting endpoint is rate-limited, and the Stripe API has a rate
limit of 100 calls per second per account. We can increase this to 200 calls per
second per account, on request. If you have a service that you expect to exceed
this limit, consider “bundling” your product into amounts. For example, if you
charge per 1000 requests, consider basing your product on “per 1000
transactions” and send 1 usage record per 1000.

### Clock drift

Reporting usage outside of the current billing period results in an error. To
account for clock drift between your server and Stripe’s systems, we provide a
short grace period in the default aggregation mode (`aggregate_usage` = `sum`).
For all other aggregation modes, the `timestamp` must be within the current
period.

During the first few minutes of each billing period, you can report usage that
occurred within the last few minutes of the previous period. If the invoice for
the previous period isn’t finalized, we add that usage to it. Otherwise, we bill
that usage in the current period. After the grace period, you can’t report usage
from the previous billing period.

Don’t rely on the grace period for reporting usage outside of a billing period.
It’s intended only to account for possible clock drift, and we don’t guarantee
it.

## Retrieve current usage

To retrieve total usage for the current period, you can [retrieve the upcoming
invoice](https://docs.stripe.com/api#upcoming_invoice) for the subscription. The
usage is reflected as the `quantity` of the [invoice
item](https://docs.stripe.com/api#invoiceitems) for a `subscription_item`. The
total usage value may not be the most up-to-date quantity because slight
processing delays can occur.

```
curl -G https://api.stripe.com/v1/invoices/upcoming \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d subscription={{SUBSCRIPTION_ID}}
```

## Links

- [updated usage-based billing
docs](https://docs.stripe.com/billing/subscriptions/usage-based)
-
[migrate](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide)
- [usage records](https://docs.stripe.com/api#usage_record_create)
- [invoices](https://docs.stripe.com/billing/invoices/subscription)
- [subscription
items](https://docs.stripe.com/api/subscriptions/object#subscription_object-items)
- [idempotency keys](https://docs.stripe.com/api/idempotent_requests)
- [retrieve the upcoming invoice](https://docs.stripe.com/api#upcoming_invoice)
- [invoice item](https://docs.stripe.com/api#invoiceitems)