# Create custom reports

## Use Sigma to generate custom reports for charges, refunds, disputes, and more.

[Sigma](https://dashboard.stripe.com/sigma/queries) makes all your transactional
data available within an interactive SQL environment in the Stripe Dashboard. It
lets you create fully customized
[reports](https://docs.stripe.com/stripe-reports) using information about your
payments, subscriptions, customers, payouts, and so on.

With Sigma, you can:

- Get information that best reflects your business and Stripe integration.
- Export in CSV format to import into your tools.
- Fetch data on a schedule of your choosing.

## Create a custom report

Reports give you the data required for your accounting and reconciliation
workflows. To create a report, query the assistant or write your own report with
SQL. The reports you generate can differ from those you generate on the Stripe
Dashboard in the following ways:

- **Data availability:** For financial reports, you can find the most recent day
of available data by selecting **month to date** or opening the date picker
calendar. In Sigma, the `data_load_time` parameter provides the timestamp that
data is available through.
- **Time zone:** Financial reports in the Stripe Dashboard filter reports by the
local time zone by default, but you can switch them to use the UTC time zone.
Sigma filters templates by the UTC time zone.
- **Date range:** A selected date range for Stripe Dashboard financial reports,
such as Jan. 13 to Jan. 14, filters reports from January 13 00:00:00 up to
January 14 23:59:59. A chosen date range filter for Sigma templates for January
13 to January 14 filters reports from Jan 13 00:00:00 up to January 13 23:59:59.
- **Currency:** Financial reports in the Stripe Dashboard always filter data to
a single currency. By default, the Sigma report templates return all currencies.
You can add a `WHERE` clause to your Sigma query to restrict your results to a
single currency.
- **Metadata:** Financial reports allow you to include metadata. Sigma templates
don’t include it. You can add metadata to your reports by following the
`Metadata to column` Sigma template.

Reports follow the same availability rules as the Stripe Dashboard. Payout
Reconciliation reports are only available for users with the **Automatic
payouts** setting enabled, and connect variants of reports are only available
for users on [Stripe Connect](https://docs.stripe.com/connect).

### Report templates

You can also create a report using a
[template](https://docs.stripe.com/stripe-data/write-queries#templates). By
default, these reports run on the last completed month that all data is
available for. To change the dates, make a copy of the template and edit the
report date intervals. Use the listed templates to generate their related
reports and their connected variants:

Report groupSigma template nameAPI report typeBalance report Itemized balance
change from activity`balance_change_from_activity.itemized.3`Itemized
payouts`payouts.itemized.3`Payout reconciliation report Itemized payout
reconciliation`payout_reconciliation.itemized.5`Itemized ending balance
reconciliation`ending_balance_reconciliation.itemized.4`
## Create and manage metrics

Create metrics from your Sigma reports and organize them in [metric
groups](https://dashboard.stripe.com/custom-metrics) to monitor your most
important metrics daily. Edit the [Sigma
chart](https://docs.stripe.com/stripe-data/write-queries#view-download-query-results)
on your metric to customize the metric preview. Metric groups that don’t have a
chart enabled display the number of rows in the report.

![Demonstrates Sigma custom report
groups](https://b.stripecdn.com/docs-statics-srv/assets/custom-reports.537d49b1fa1765a58d7237cf251d4a01.png)

You can create up to 50 metric groups for your account, with up to 12 Sigma
reports in each metric group. Only the author of the metric group can edit or
delete the metric group. If you delete a metric group, it doesn’t impact the
reports in that group.

## Unsubscribing from Sigma

If you currently have an active Sigma subscription and want to cancel it, go to
your [Sigma settings](https://dashboard.stripe.com/settings/sigma) and click
**Cancel Stripe Sigma subscription**. You can continue using Sigma until the end
of the billing cycle, at which point the subscription ends.

## See also

- [Query transaction
data](https://docs.stripe.com/stripe-data/query-transactions)
- [Query Billing data](https://docs.stripe.com/stripe-data/query-billing-data)
- [Sigma and Data Pipeline for Connect
platforms](https://docs.stripe.com/stripe-data/query-connect-data)
- [Query Issuing data](https://docs.stripe.com/stripe-data/query-issuing-data)
- [Query all fees data](https://docs.stripe.com/stripe-data/query-all-fees-data)
- [Schedule queries with
Sigma](https://docs.stripe.com/stripe-data/schedule-queries)
- [Migrate queries onto the new Sigma
version](https://docs.stripe.com/stripe-data/migrate-queries)

## Links

- [Sigma](https://dashboard.stripe.com/sigma/queries)
- [reports](https://docs.stripe.com/stripe-reports)
- [Stripe Connect](https://docs.stripe.com/connect)
- [template](https://docs.stripe.com/stripe-data/write-queries#templates)
- [metric groups](https://dashboard.stripe.com/custom-metrics)
- [Sigma
chart](https://docs.stripe.com/stripe-data/write-queries#view-download-query-results)
- [Sigma settings](https://dashboard.stripe.com/settings/sigma)
- [Query transaction
data](https://docs.stripe.com/stripe-data/query-transactions)
- [Query Billing data](https://docs.stripe.com/stripe-data/query-billing-data)
- [Sigma and Data Pipeline for Connect
platforms](https://docs.stripe.com/stripe-data/query-connect-data)
- [Query Issuing data](https://docs.stripe.com/stripe-data/query-issuing-data)
- [Query all fees data](https://docs.stripe.com/stripe-data/query-all-fees-data)
- [Schedule queries with
Sigma](https://docs.stripe.com/stripe-data/schedule-queries)
- [Migrate queries onto the new Sigma
version](https://docs.stripe.com/stripe-data/migrate-queries)