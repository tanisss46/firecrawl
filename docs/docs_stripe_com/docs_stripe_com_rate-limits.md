# Rate limits

## Learn about API rate limits and how to work with them.

The Stripe API uses a number of safeguards against bursts of incoming traffic to
help maximize its stability. If you send many requests in quick succession, you
might see error responses with status code `429`.

## API limiters

We have several limiters in the API, including a rate limiter and a concurrency
limiter.

Treat the limits as maximums, and don’t generate unnecessary load. To prevent
abuse, we might reduce the limits.

For advice on handling 429 errors, see [Handling limiting
gracefully](https://docs.stripe.com/rate-limits#handling-limiting-gracefully).
If you suddenly see a rising number of rate-limited requests, [contact Stripe
Support](https://support.stripe.com/).

You can request a limit increase to enable a high-traffic application by
[contacting Stripe Support](https://support.stripe.com/). If you’re requesting a
large increase, contact us at least 6 weeks in advance.

### Rate limiter

The basic rate limiter restricts the number of API requests per second as
follows:

- **Live mode**: 100 read operations and 100 write operations
- **Test mode**: 25 read operations and 25 write operations

Calls to certain resources have stricter limits, and also count against the
basic limits. These stricter limits apply separately to live mode and test mode.

- [Files API](https://docs.stripe.com/api/files): 20 read operations and 20
write operations per second
- [Search API](https://docs.stripe.com/search#rate-limits): 20 read operations
per second

Calls to the [Meter events
endpoint](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#rate-limits)
in live mode are subject to a separate rate limit, and don’t count against the
basic limits. The limit is 1000 calls per second per Stripe account. In test
mode, calls to the Meter events endpoint count toward the basic limit. For
Connect platforms, calls on a connected account to the Meter events endpoint
also count toward the basic limit.

### Concurrency limiter

The concurrency limiter restricts the number of concurrent active requests.
Problems with this limiter are less common than with the rate limiter, but they
likely indicate the existence of resource-intensive, long-lived requests.

Calls to the [Meter events
endpoint](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#rate-limits)
are limited to one concurrent call per customer per meter.

## Common causes and mitigations

Rate limiting can occur under a variety of conditions, but it’s most common in
these scenarios:

- Running **a large volume of closely-spaced requests** can lead to rate
limiting. Often this is part of an analytical or migration operation. When
engaging in these activities, you should try to control the request rate on the
client side (see [Handling limiting
gracefully](https://docs.stripe.com/rate-limits#handling-limiting-gracefully)).
- Issuing **many long-lived requests** can trigger limiting. Requests vary in
the amount of Stripe’s server resources they use, and more resource-intensive
requests tend to take longer and run the risk of causing new requests to be shed
by the concurrency limiter. Resource requirements vary widely, but list requests
and requests that include expansions generally use more resources and take
longer to run. We suggest profiling the duration of Stripe API requests and
watching for timeouts to try and spot those that are unexpectedly slow.
- A sudden increase in charge volume like a **flash sale** might result in rate
limiting. We try to set our rates high enough that legitimate payment traffic
never exceeds the limits, but if you suspect that an upcoming event might push
you over the limits listed above, [contact Stripe
Support](https://support.stripe.com/).

## Handling limiting gracefully

A basic technique for integrations to gracefully handle limiting is to watch for
`429` status codes and build in a retry mechanism. The retry mechanism should
follow an exponential backoff schedule to reduce request volume when necessary.
We’d also recommend building some randomness into the backoff schedule to avoid
a [thundering herd
effect](https://en.wikipedia.org/wiki/Thundering_herd_problem).

You can only optimize individual requests to a limited degree, so an even more
sophisticated approach would be to control traffic to Stripe at a global level,
and throttle it back if you detect substantial rate limiting. A common technique
for controlling rate is to implement something like a [token bucket rate
limiting algorithm](https://en.wikipedia.org/wiki/Token_bucket) on the
client-side. Ready-made and mature implementations for token bucket are
available in almost any programming language.

## Object lock timeouts

Integrations might encounter errors with HTTP status `429`, code `lock_timeout`,
and this message:

This object cannot be accessed right now because another API request or Stripe
process currently accessing it. If you see this error intermittently, retry the
request. If you see this error frequently and are making multiple concurrent
requests to a single object, make your requests serially or at a lower rate.

The Stripe API locks objects on some operations so that concurrent workloads
don’t interfere and produce an inconsistent result. The error above is caused by
a request trying to acquire a lock that’s already held elsewhere, and timing out
after it couldn’t be acquired in time.

Lock timeouts have a different cause than rate limiting, but their mitigations
are similar. As with rate limiting errors, we recommend retrying on an
exponential backoff schedule (see [Handling limiting
gracefully](https://docs.stripe.com/rate-limits#handling-limiting-gracefully)).
But unlike rate limiting errors, the automatic retry mechanisms built into
Stripe’s [SDKs](https://docs.stripe.com/sdks) retry `429`s caused by lock
timeouts:

```
Stripe.max_network_retries = 2
```

Lock contention is caused by concurrent access on related objects. Integrations
can vastly reduce this by making sure that mutations on the same object are
queued up and run sequentially instead. Concurrent operations against the API
are still okay, but try to make sure simultaneous operations operate only on
unique objects. It’s also possible to see lock contention caused by a conflict
with an internal Stripe background process—this should be rare, but because it’s
beyond user control, we recommend that all integrations are able to retry
requests.

## Load testing

It’s common for users to prepare for a major sales event by load testing their
systems, with the Stripe API running in test mode as part of it. We generally
discourage this practice because API limits are lower in test mode, so the load
test is likely to hit limits that it wouldn’t hit in production. Test mode is
also not a perfect stand-in for live API calls, and that can be somewhat
misleading. For example, creating a charge in live mode sends a request to a
payment gateway and that request is mocked in test mode, resulting in
significantly different latency profiles.

As an alternative, we recommend building integrations so that they have a
configurable system for mocking out requests to the Stripe API, which you can
enable for load tests. For realistic results, they should simulate latency by
sleeping for a time that you determine by sampling the durations of real live
mode Stripe API calls, as seen from the perspective of the integration.

## API read request allocations

Stripe provides access to its read (GET) API requests to facilitate reasonable
lookup activity related to payment integrations. To maximize quality of service
for all users, Stripe provides the following allocations for read requests based
on transaction count:

- Read API requests shouldn’t exceed an average ratio of **500 requests per
transaction** for an account. For example, if an account processes 100
transactions in a 30-day period, they shouldn’t exceed 50,000 read API requests
during that same period.
- When using Connect, a platform and its connected accounts have distinct read
API allowances:- Each connected account has their own allocation for requests
they initiate (500 requests per transaction).
- Connect platforms use a separate allocation to make read requests on behalf of
their connected accounts using either their secret API key or OAuth access
tokens. This allocation is also 500 requests per transaction based on the
aggregate transaction count across its connected accounts.
- Ratios are measured on a rolling 30-day basis.
- Every account, regardless of transaction count, has a minimum allocation of
10,000 read requests per month.
- Write API requests have no allocation limit.

Calls to the following API endpoints are excluded from the above allocation
limits:

- [Data products](https://docs.stripe.com/stripe-data)
- [Reporting products](https://docs.stripe.com/stripe-reports)
- [Tax products](https://docs.stripe.com/tax)

To reduce your API request volume, consider using [Stripe Data
Pipeline](https://stripe.com/data-pipeline) for a complete export of API data to
your local database or provider.

#### Filter requests to limit paginated calls

Some list endpoints return [multiple
pages](https://docs.stripe.com/api/pagination) of results and might require
multiple requests to return the full set of API objects for a list operation.
Apply filters when possible to narrow your list results.

## Links

- [contact Stripe Support](https://support.stripe.com/)
- [Files API](https://docs.stripe.com/api/files)
- [Search API](https://docs.stripe.com/search#rate-limits)
- [Meter events
endpoint](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#rate-limits)
- [thundering herd
effect](https://en.wikipedia.org/wiki/Thundering_herd_problem)
- [token bucket rate limiting
algorithm](https://en.wikipedia.org/wiki/Token_bucket)
- [SDKs](https://docs.stripe.com/sdks)
- [Data products](https://docs.stripe.com/stripe-data)
- [Reporting products](https://docs.stripe.com/stripe-reports)
- [Tax products](https://docs.stripe.com/tax)
- [Stripe Data Pipeline](https://stripe.com/data-pipeline)
- [multiple pages](https://docs.stripe.com/api/pagination)