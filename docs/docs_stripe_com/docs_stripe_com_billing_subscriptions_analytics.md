# Analytics

## Use the Stripe Dashboard to monitor and analyze your recurring revenue.

[Stripe Billing’s](https://dashboard.stripe.com/billing) analytics and
[downloadable
reports](https://docs.stripe.com/billing/subscriptions/analytics#downloadable-reports)
provide a comprehensive view of your business’s performance. You can monitor
performance at a glance, audit performance changes by drilling down into data,
and compare segment performance with filtering and grouping. You can also use
benchmarking to compare your performance against similar businesses on Stripe.

## Preview features

Stripe offers early access to some upcoming features. To get early access to a
beta feature, enter your email.

Preview programDescriptionSign upUsage MRRAccess usage-based MRR and reporting
featuresClick here to sign up for our preview.
## Downloadable reports

To build financial models and begin downstream reporting, download your billing
metrics data. The export is in CSV format and includes the following reports:

ReportDescriptionMRR per subscriber per monthIncludes the Monthly Recurring
Revenue (MRR) for each subscriber at the end of each month.Subscription metrics
summaryA summary of your monthly subscription metrics. The report includes your
MRR roll-forward report, active subscriber roll-forward report, trial conversion
metrics, and lifetime value metrics.Customer MRR changesIncludes a log of every
MRR change for each customer, including new subscribers, upgrades, downgrades,
reactivations, and churn.
## Configure your metrics definitions

You can configure metrics from the [Billing
overview](https://dashboard.stripe.com/billing) page. Click **Configure** to
change how Stripe calculates Monthly Recurring Revenue (MRR), Churn, and Active
Subscribers. Changes take 24-48 hours to appear in your configuration.

### Discounts

You can configure whether to include or exclude discounts in your MRR
calculation. Subtracting discounts from MRR is considered a more conservative
approach to reporting MRR because it more closely reflects the present value of
these customers.

You can adjust two settings to exclude discounts:

- **Subtract recurring discounts from MRR**: Turn this on for your MRR to
reflect any recurring discounts applied.
- **Subtract one-time discounts from MRR**: Turn this on for your MRR to reflect
any one-time discounts applied.

These settings apply the same way to all coupons you use on Stripe, including
subscription-level coupons, line-item level coupons, and stacked coupons.
Permanent recurring discounts, are always subtracted from MRR.

### Active subscribers

You can configure when Stripe considers a subscriber to be active:

- **At the start of the subscription**: If you select this option, a
subscription is considered active when the first billing period begins. This is
the most common option.
- **When the first payment is received**: If you select this, the subscription
is considered active when the first payment is received. Use this if you don’t
want to consider subscribers active until they’ve paid their first invoice.

## Audit your metrics with drill-downs

You can interact with billing charts using the **Explore** functionality.

Some charts, like **MRR growth** and **Churned revenue**, allow you to drill
down into data points to see the underlying data. To do this, click **Explore**
on a chart to see the chart and a table of related data points. If a cell in the
table is clickable, you can click into it to reveal the underlying events for
that data point. This is particularly helpful to understand things like which
customers churned or expanded their subscription in a given period.

#### Public preview

This feature is currently available for a subset of billing metrics.

## Analyze your metrics with filtering and grouping

You can interact with billing charts using the **Explore** functionality.

Some charts, like **MRR growth** and **Churned revenue**, allow you to filter
and group by **Product** or **Price**. To do this, click **Explore** on a chart
to see the chart and a table of related data points below and options for
filtering and grouping above.

#### Public preview

This feature is currently available for a subset of billing metrics. This
feature is not yet available to users processing subscription volume in multiple
currencies.

## Links

- [Stripe Billing’s](https://dashboard.stripe.com/billing)