# Data freshness

## Learn how Sigma and Data Pipeline handle data.

Sigma and Data Pipeline allow you to analyze and export the same underlying data
that’s accessible through the [Stripe API](https://docs.stripe.com/api), but
through different interfaces. While the Stripe API provides programmatic access
to your data, Sigma offers a SQL-based interface for custom queries and
analysis, and Data Pipeline enables bulk data exports.

Additionally, Sigma and Data Pipeline provide access to certain data that isn’t
available through the Stripe API, such as
[reports](https://docs.stripe.com/stripe-reports).

## Data freshness

Sigma and Data Pipeline make most of your transaction data available to query
within one day.

SigmaData Pipeline
Sigma makes most of your Stripe transaction data available to query within three
hours. All API activity is available to query approximately three hours after it
occurs. For example, data from 12:00am UTC is available by 3:00am UTC on the
same day.

### Query data load times

The interface in the Dashboard displays the date and time of the last payments
data. You can use `data_load_time` as a value in your queries to represent when
data is most recently processed on your account. For example, if payment tables
were last updated on 3/9/2025, the `data_load_time` is interpreted as
`2025-03-06 00:00:00 +0000`. At times, Sigma may reflect activity that is more
recent than `data_load_time`. For example, a charge authorized just before
midnight, but captured soon after, may show as captured.

Making data available requires additional time. You can use `data_load_time` as
a value in your queries that represents when data is most recently processed on
your account. Use this value to dynamically set a date range in your scheduled
queries.

For example, consider the following scheduled query that returns a list of
balance transactions created one month before `data_load_time`.

```
select
 id,
 amount,
 fee,
 currency
from balance_transactions -- this table is the canonical record of changes to
your Stripe balance
where
 created < data_load_time and
 created >= data_load_time - interval '1' month
order by created desc
limit 10
```

The following timeline illustrates how this works based on data availability:

DateTimeline for results2025-03-06- `data_load_time` is interpreted as
`2025-03-06`
- The scheduled query includes transaction data through EOD 2025-03-05
- Query results are available on 2025-03-06 by 2pm UTC

Now, consider the following scheduled query that returns a list of charge_ids
and interchange billing amounts associated with each fee balance debit created
one month before `data_load_time`.

```
select
 ic.charge_id,
 ic.billing_currency,
 ic.billing_amount,
 ic.balance_transaction_id,
 ic.balance_transaction_created_at
from icplus_fees as ic
join balance_transactions as bt
 on ic.balance_transaction_id = bt.id
where bt.created >= data_load_time - interval '1' month
 and bt.created < data_load_time
```

If this query is scheduled to recur daily, the following timeline illustrates
when you can expect the results:

DateTimeline for results2025-03-09- `data_load_time` is interpreted as
`2025-03-06 00:00:00 +0000`
- The scheduled query includes transaction data through EOD 2025-03-05
- Query results are available on 2025-03-09 by 2am UTC

## Dataset freshness

View the following table for information on data freshness for specific
datasets:

DatasetExample tablesSigma freshnessData Pipeline freshnessCore API tables
(including Connect versions)`balance_transactions`, `charges`,
`connected_account_balance_transactions`3 hours12 hoursDaily refreshed
tables`exchange_rates_from_usd`, `radar_rules`, `radar_rule_attributes`,
`tax_transactions`28 hours28 hours
## Data schema

You can view the complete [schema](https://dashboard.stripe.com/stripe-schema),
which closely follows our API conventions, in a split-view format that shows
details on table relationships. It displays all the available data that you can
use in your queries, organized by category. Each category contains a set of
tables that represents the available data. Many tables correspond to specific
API objects, with each column representing a reported attribute. For example,
the `charges` table represents information about
[Charge](https://docs.stripe.com/api#charge_object) objects, which appears in
the **Payments** section of the Dashboard.

You can select a table to expand it and reveal its available columns, along with
a description of the type of data it contains (for example, `Boolean` ,
`Varchar`, and `Foreign key`). Hover the cursor over any column to reveal a
description. Use the search field at the top of the schema to find specific
tables and columns. When writing queries, refer to our [API
reference](https://docs.stripe.com/api) for additional context and values.

## Links

- [Stripe API](https://docs.stripe.com/api)
- [reports](https://docs.stripe.com/stripe-reports)
- [schema](https://dashboard.stripe.com/stripe-schema)
- [Charge](https://docs.stripe.com/api#charge_object)