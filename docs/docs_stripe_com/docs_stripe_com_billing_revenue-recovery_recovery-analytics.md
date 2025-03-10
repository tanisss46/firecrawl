# Revenue recovery analytics

## Use the Stripe Dashboard to understand your subscription payment failure rate and how effectively you are able to recover failed subscription payments.

The [revenue recovery overview](https://dashboard.stripe.com/revenue_recovery)
provides key performance indicators (KPIs), trends, and reports to help you
understand how failed subscription payments are impacting your business. This
data can be helpful in optimizing your revenue recovery strategy and keeping
track of changes in performance.

#### Note

Data in the revenue recovery overview represents recurring subscription payments
only and excludes the first invoice payment following a trial.

## Key performance indicators (KPIs)

- **Failed payments:** The volume of subscription payments that failed on the
first attempt. Use this metric to identify and monitor the volume of failed
payments over time.
- **Failure rate:** The percentage of subscription payment volume that failed on
the first attempt. If your failure rate is high, you can send proactive
reminders ahead of payment dates to prevent failed payments.
- **Recovered payments:** The volume of subscription payments recovered through
retries or emails managed by Stripe, as well as other recovery methods you may
be using. Monitoring the volume of recovered payments can help you measure the
effectiveness of your recovery strategies.
- **Recovery rate:** The percentage of subscription payment volume successfully
recovered by any means after a failure. If your recovery rate is lower than
expected, consider turning on Stripe
[retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) and
failed payment
[emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails).

## Breakdowns

These are specific charts that provide more granular insights on payment
failures, recovery methods, and decline codes enabling you to tailor your
recovery strategies to fit your needs.

### Recovery breakdown

- **Not recovered:** The volume of subscription payments that failed and could
not be recovered.
- **Recovered:** The volume of subscription payments recovered through retries
or emails managed by Stripe, as well as other recovery methods you may be using.
Monitoring the volume of recovered payments can help you measure the
effectiveness of your recovery strategies.
- **In recovery:** The volume of subscription payments that have recently failed
but are still being retried by Stripe. You’re likely to see payment volume in
recovery for the current month and the previous month as the retry window
concludes.
- **Recovery rate:** The percentage of subscription payment volume that is
successfully recovered by any means after a failure. You may see a temporary
drop in your recovery rate for the current and previous month if not all
automatic retries have been attempted yet.

### Recovered volume by method

- **Retries:** The volume of failed payments recovered by Stripe retries.
- **Emails:** The volume of failed payments recovered by Stripe emails.
- **Other:** The volume of failed payments recovered by charge attempts made via
API or in the Dashboard. Can include third-party email campaigns, in-app flows,
other retry algorithms, and other recovery methods.

### Failed volume by decline reason

This chart shows you the top five decline codes by failed payment volume.
Recognizing the types of decline codes can help diagnose common issues and
propose corrective measures to reduce failures. [Learn more about decline
codes](https://docs.stripe.com/declines/codes).

## Top customers in recovery

This table showcases customers whose payments have recently failed and are still
being attempted by Stripe. The table shows the failure amount and how long the
subscriber has been a customer. Consider reaching out to these customers
manually depending on their value to potentially save revenue.

## Links

- [revenue recovery overview](https://dashboard.stripe.com/revenue_recovery)
- [retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries)
- [emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails)
- [Learn more about decline codes](https://docs.stripe.com/declines/codes)