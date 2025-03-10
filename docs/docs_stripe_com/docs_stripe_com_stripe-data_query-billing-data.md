# Query billing data

## Use Sigma or Data Pipeline to retrieve billing information.

Billing is made up of different components that work together to provide one-off
[invoices](https://docs.stripe.com/api/invoices) and periodic billing, with
different aspects of billing data available across a number of tables. All
billing-specific tables are in the **Billing** section of the schema, with the
primary tables being `subscriptions` and `invoices`.

To explore billing data further, you can use the additional tables that
represent the components of subscriptions and invoices, such as `prices`,
`products`, or `coupons`. In addition, the `customers` table is a fundamental
part of billing, and contains data you might need to report on.

## Subscriptions

Each row within the `subscriptions` table represents data about an individual
[Subscription](https://docs.stripe.com/api#subscription_object) object—the same
information that the API retrieves or is available in the [Stripe
Dashboard](https://dashboard.stripe.com/test/subscriptions). You can report on
every subscription that you create on your account.

This table is our recommended starting point for creating reports about your
current subscribers. You can join this to other related tables, allowing you to
explore your data in more detail.

!

The following example retrieves a list of subscriptions that have been marked as
unpaid, along with any available contact information for the customer.

```
select
 subscriptions.id,
 subscriptions.customer_id,
 customers.email
from subscriptions
inner join customers
 on customers.id = subscriptions.customer_id
where
 subscriptions.status = 'unpaid'
limit 5
```

idcustomer_idemailsub_SxpjMlQgvZZ8ofjcus_87bMt18IORpkNt0jenny.rosen@example.comsub_YsNdmQ0yFOhQFeDcus_fsucVFdcBpYFio0noah.wilson@example.comsub_VbomXNGp0RUpVipcus_m5r0wqkzoP6RHvJjoshua.miller@example.comsub_emx0gd34RzifhKScus_OHuLqPEDMfmhJg4madison.jackson@example.comsub_0zACzOECHHvXI77cus_tUTHZC4EPY5ZG95elijah.smith@example.com
## Customers

Data about [Customer](https://docs.stripe.com/api#customers) objects are
contained in the `customers` table (this isn’t part of the Billing Tables
group). It’s commonly used as part of billing-based reports and can be joined to
a number of tables. It’s also useful if you’re creating
[charges](https://docs.stripe.com/stripe-data/query-transactions) with saved
payment information.

!

The following example retrieves a list of customers with subscriptions that are
currently in a trial period. It retrieves both the ID and email address for each
customer.

```
select
 customers.id,
 customers.email,
 subscriptions.price_id
from subscriptions
inner join customers
on customers.id = subscriptions.customer_id
where subscriptions.status = 'trialing'
limit 5
```

idemailprice_idcus_KtePdZXEiRJWH1Tjenny.rosen@example.comruby-pro-522cus_fu1l3GBsdrUVm4Snoah.wilson@example.comruby-pro-522cus_vGnHKoNf18B8lHirichard.jones@example.comgold-basic-221cus_Yu6zeqKpMkm8sX1madison.jackson@example.comgold-basic-221cus_yF8ivJdxcBdpBixelijah.smith@example.comsilver-pro-498
## Products and prices

Products describe items that your customers can purchase with a subscription.
Prices are tied to products and set out the cost, billing interval, and
currency. When you view data from the `subscriptions` table, you can join it
with `subscription_items`. Additionally, you can join it to `products.id` by
using the `price_product_id` from the item.

The following example returns a list of active subscriptions along with the
product name and its statement descriptor:

```
with active_subscriptions as (
 select
 s.id as subscription_id,
 p.name as product_name,
 p.statement_descriptor
 from subscriptions s
 join subscription_items si on s.id = si.subscription_id
 join products p on si.price_product_id = p.id
 where s.status = 'active'
)
select
 subscription_id,
 subscription_item_id,
 price_id,
 product_name,
 statement_descriptor
from active_subscriptions
order by 1,2
```

idnamestatement_descriptorsub_SGEkF4tmKVnMUwlruby-pro-522Ruby
Prosub_sYTzRpuXc28Pe1Ggold-basic-221Gold
Basicsub_spzBiZsTolzGnKZsilver-pro-498Silver
Prosub_pxyLUVfj8LeShU8diamond-mid-244Diamond
Midsub_aHY164oTBQMvBzeruby-standard-196Ruby Standard
## Price tiers

While using prices with
[tiers](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
in your subscriptions, the `price_tiers` table can provide specific data about
each tier. For instance, if you want to understand the initial tier of your
subscriptions, including the maximum quantity for the first tier and the used
unit amount, refer to the following query:

```
with subscription_item_prices as (
 select
 si.subscription_id,
 si.price_id,
 p.currency
 from
 subscription_items si
 join prices p on si.price_id = p.id
),
price_tier_details as (
 select
 sp.subscription_id,
 pt.price_id,
 pt.upto,
 stringify_amount(sp.currency, pt.amount, '.') as tier_price,
 sp.currency
 from
 subscription_item_prices sp
 join price_tiers pt on sp.price_id = pt.price_id
)
select
 ptd.subscription_id,
 ptd.price_id,
 ptd.upto,
 ptd.tier_price,
 ptd.currency
from
 price_tier_details ptd
order by
 ptd.subscription_id,
 ptd.price_id,
 ptd.upto asc
```

subscription_idprice_iduptotier_pricecurrencysub_pzzGxfGDvxBRZy6price_IEyS0q5Dt1gcDDy302.00usdsub_ZRne6VQuus7UDfsprice_cqzzTbMeLFkdYem601.00usdsub_W8X58k6DY5PJYgyprice_UakHxJpheQG6VT4900.50usd
## Invoices

The `invoices` table contains data about individual
[Invoice](https://docs.stripe.com/api#invoice_object) objects. Each subscription
generates an invoice on a recurring basis that represents the amount the
customer owes. This automatically includes the amount required for the
subscription, and any additional [invoice
items](https://docs.stripe.com/api#invoiceitems) that might have been created
(listed as line items).

Invoices are comprised of individual ([invoice) line
items](https://docs.stripe.com/api#invoice_line_item_object). These line items
represent any subscriptions that the customer is billed for, and invoice items
that have been created and applied to the invoice. To break down an invoice and
analyze each of its line items, use the `invoice_line_items` table.

The `source_id` column of this table contains the **ID** of either the
subscription (for example, `sub_HPfmFbLLWdeHCNs`) or invoice item (for example,
`ii_QMcvCqGgXqOkgjC`) that the line item corresponds to. The `source_type`
column reflects whether the line items represent a subscription or an invoice
item.

Unlike other foreign keys, the `subscription` column of the `invoice_line_items`
table isn’t always populated. If the corresponding invoice item is a
subscription, this column is blank—its **ID** already appears in the `source_id`
column.

### Invoice items

Data about [Invoice items](https://docs.stripe.com/api#invoiceitems) is provided
in the `invoice_items` table. Invoice items are commonly used to specify an
additional amount (or deduct an amount) that’s applied on the next invoice at
the beginning of the next billing cycle. For example, you would create an
invoice item if you need to bill your customer for exceeding their monthly
allowance, or if you need to provide a credit on the next invoice for unused
service.

!

The following example retrieves all the invoices and associated charge IDs for a
particular subscription.

```
select
 id,
 charge_id,
 amount_due
from invoices
where subscription_id = 'sub_ALJXL9gBYtv6GJ'
```

idnamein_NxAYzGLVhgrGqfrch_57bw8qMc5yPcjqj1999in_jclHyunFsOjbLpsch_Yrts3pVMACSRGYC1999in_viXWIBsEh2JpAuZ1999ch_RkBvZgQvqYhyX72in_6obC7vri5Kr6bXx1999ch_XuAoeXpU5i1SIjmin_pDbtvmeNtEg4Z741999ch_M2xh6bWmewyJaxi
### Invoice totals and discounts

The invoice subtotal represents the amount of all subscriptions, invoice items,
and prorations on the invoice before any discount is applied. The invoice total
is the amount after discounts and tax have been applied:

`invoice.total` = `invoice.subtotal` - `discount` + `invoice.tax`

There is no column to represent the discount amount on an invoice. Instead, you
can calculate this by aggregating the line items’ discount amounts. The
following query returns a list of invoices, their period start and end, the
total discounted amount for the invoice.

```
with invoices_with_discounts as (
 select
 invoice_id,
 sum(amount) as total_discount_amount
 from
 invoice_line_item_discount_amounts
 group by
 invoice_id
)
select
 i.id as invoice_id,
 i.period_start,
 i.period_end,
stringify_amount(i.currency, ilda.total_discount_amount, '.') as
total_discount_amount
 i.currency
from
 invoices i
 join invoices_with_discounts ilda on i.id = ilda.invoice_id
order by i.id
```

invoice_idperiod_startperiod_endtotal_discount_amountcurrencyin_DFm0gJ8PUqsugg82024-05-012024-06-0124.66usdin_PfY45SduNk4gnO02024-06-012024-07-0124.34usdin_WHBE03lxz7IKgcQ2024-04-012024-05-0145.96usd
### Working with invoice dates and periods

Subscription invoices are pre-billed, meaning the customer makes the payment at
the beginning of a billing cycle. This is represented in a line item’s `period`
value. For example, a customer with a monthly subscription is billed at the
start of each month. If they choose to
[cancel_at_period_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-cancel_at_period_end),
their subscription stays active until the month’s end, after which the
subscription ends.

The `period_start` and `period_end` values of an invoice represents when invoice
items might have been created–it’s not always definitive of the period of
service that the customer is being billed for. For example, if a customer is
billed on the 1st of each month and exceeds their monthly allowance on the 15th,
you might create an invoice item for any additional costs that the customer is
charged for. This invoice item is then included in the next invoice, which is
created on the 1st of the next month. When the next invoice is generated, the
`period_start` date would be the 15th of the previous month—the date the
additional line item is first created.

## Usage based billing

[Usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based)
enables you to charge customers based on their usage of your product or service.

### Billing meters

A [Meter](https://docs.stripe.com/api/billing/meter) object specifies how to
aggregate meter events over a billing period. Meter events represent all actions
that customers take in your system (for example, API requests). Meters attach to
prices and form the basis of what’s billed. These objects are available through
the `billing_meters` table.

The following query returns all active billing meters.

```
select
 id,
 status,
 display_name,
 default_aggregation_formula
from
 billing_meters
where
 status = 'ACTIVE'
 and livemode
```

IDstatusdisplay_namedefault_aggregation_formulamtr_BFRDIsNMEalZysZACTIVEalpaca_ai_tokenSUMmtr_5ebzRp0N6h1J97XACTIVEalpaca_ai_image_tokenCOUNT
### Billing meter event summaries

A [Billing Meter Event
Summary](https://docs.stripe.com/api/billing/meter-event-summary) object
represents an aggregated view of a customer’s billing meter events within a
specified timeframe. It represents how much usage a customer accrues for that
period. These objects are available through the `billing_meter_event_summaries`
table. Hourly summaries are available, as indicated by the
`value_grouping_window` column.

The following query returns a sum of billing meter events for a specific
customer.

```
select
 billing_meters.display_name,
 sum(billing_meter_event_summaries.aggregated_value) AS total_usage
from
 billing_meter_event_summaries
join billing_meters on billing_meters.id =
billing_meter_event_summaries.meter_id
where
 billing_meter_event_summaries.customer_id = 'cus_EDQkYj7P2Jf3sJ1'
 and billing_meter_event_summaries.start_time >= timestamp '2025-02-01 08:00'
 and billing_meter_event_summaries.end_time <= timestamp '2025-02-01 20:00'
 and value_grouping_window = 'hourly'
group by
 display_name
```

display_nametotal_usagealpaca_ai_token928943alpaca_ai_image_token50
### Billing meter invalid events

A [Billing Meter Invalid
Event](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#handle-meter-event-errors)
object represents a billing meter event that isn’t successfully validated. These
objects are available through the `billing_meter_invalid_events` table. The
associated `billing_meter_invalid_events_payload` table contains the event
payload from the original event.

The following query returns all invalid billing meter events for a specific
customer.

```
SELECT
 billing_meter_invalid_events.id as event_id,
 billing_meter_invalid_events.error_code,
 billing_meter_invalid_events.error_message
FROM
 billing_meter_invalid_events
JOIN billing_meter_invalid_events_payload ON
billing_meter_invalid_events_payload.event_id = billing_meter_invalid_events.id
WHERE
 billing_meter_invalid_events_payload.key = 'stripe_customer_id'
 AND billing_meter_invalid_events_payload.value = 'cus_EDQkYj7P2Jf3sJ1'
```

event_iderror_codeerror_messageudQnNCr2_CcVC_sBb4_Z4gk_5Dc6EQbd5otxMETER_NOT_FOUNDNo
meter found matching event_name
mtr_QkD7t5nqIUp621p.9hGo9KRJ_mPFl_B1Jn_EkOl_Nx5pkHqyht6pMETER_NOT_FOUNDNo meter
found matching event_name mtr_3dHLDTwDOPHJLIY.
## Coupons

A [Coupon](https://docs.stripe.com/billing/subscriptions/coupons) object
represents an amount or percentage-off discount that you can apply to
subscriptions or customers.

```
select
 coupons.id,
 coupons.amount_off,
 coupons.percent_off
from coupons
where valid = false
limit 5
```

idamount_offpercent_off10FF10SUMMER252510FREE1015OFF15FALL3030
## Discounts

A discount is the application of a coupon, represented by a
[Discount](https://docs.stripe.com/api#discounts) object. The following query
returns a list of subscriptions and their associated discounts and coupons:

```
select
 subscriptions.id as subscription_id,
 t.discount_id,
 coupons.id as coupon_id
from
 subscriptions
 cross join unnest(split(subscriptions.discounts, ',')) as t(discount_id)
 join discounts on discounts.id = t.discount_id
 join coupons on coupons.id = discounts.coupon_id
limit 3
```

subscription_iddiscount_idcoupon_idsub_RIn5T5gk8wHEzqAdi_lj1OG91I5FPPgyS10OFFsub_k1ODFwB6yikeL0fdi_uH5driyVKblVAXN25OFFsub_8PzSWpFOuNk8lbQdi_uihvCPpCkknMxTe10FREE
## Promotion codes

A [promotion code](https://docs.stripe.com/api/promotion_codes) represents a
customer-redeemable code for a
[coupon](https://docs.stripe.com/billing/subscriptions/coupons). The following
query provides a list of promotion codes pertaining to a specific coupon and
displays the number of times each code has been redeemed:

```
select
 promotion_codes.id as promotion_code_id,
 promotion_codes.code as promotion_code,
 promotion_codes.times_redeemed
from
 promotion_codes
limit 3
```

promotion_code_idcodetimes_redeemedpromo_1LziIu6opFRCIrz10OFF1promo_1ZRCQw2SRF7ug8X25OFF2promo_HS7xjxu4h8V81Ui10FREE3
## Subscription Item Change Events

The `subscription_item_change_events` table tracks changes to subscription items
that affect [Monthly Recurring Revenue
(MRR)](https://support.stripe.com/questions/calculating-monthly-recurring-revenue-(mrr)-in-billing)
and subscription quantities. Use this table to calculate MRR for individual
customers, products, or plans, to create custom metric definitions for your
business models, and to track subscription quantity changes.

#### Caution

This table provides more up-to-date data than the source driving the MRR metrics
on the Billing overview in the Stripe Dashboard. This means the data for the
last and current day’s MRR here could be more accurate and could differ from
what you see in the Dashboard.

### local_event_timestamp and event_timestamp

This table includes two timestamp columns:

- `event_timestamp`: This is the UTC timestamp.
- `local_event_timestamp`: This timestamp is in your local timezone, typically
the timezone of the person who created your Stripe account.

### currency

Here, you’ll find the subscription item’s settlement currency as a three-letter
[ISO currency code](https://docs.stripe.com/currencies) in lowercase. The
currency must be one that Stripe [supports](https://docs.stripe.com/currencies).

### mrr_change

The `mrr_change` column shows the positive or negative impact of an event on
your MRR in the subscription item’s settlement currency’s minor unit (such as
cents for USD).

### quantity_change

The `quantity_change` column shows the associated positive or negative change in
the quantity of a subscription item that a customer subscribes to.

### event_type

Event typeDefinitionACTIVE_STARTThe subscription item started contributing to
MRR.ACTIVE_ENDThe subscription item stopped contributing to
MRR.ACTIVE_UPGRADEThe MRR contribution of the subscription item increased. This
can occur when the price of a subscription item increases or if the quantity of
that subscription item increases.ACTIVE_DOWNGRADEThe MRR contribution of the
subscription item decreased. This can occur when the price of a subscription
item decreases or if the quantity of that subscription item
decreases.ACTIVE_QUANTITY_INCREASEThe quantity of the subscription item
increased, but the MRR wasn’t impacted. You might see this if you use tiered
pricing and the quantity needs to exceed a certain threshold before the price
changes.ACTIVE_QUANTITY_DECREASEThe quantity of the subscription item decreased,
but the MRR wasn’t impacted. You might see this if you use tiered pricing and
the quantity needs to go below a certain threshold before the price changes.
#### Note

Some user actions can create multiple events, so you could see an event with an
`event_type` of `ACTIVE_END` on one item and then immediately an event with an
`event_type` of `ACTIVE_START` on another item for the same `subscription_id`.

### Other columns

Other columns (`product_id`, `price_id`, `customer_id`, `subscription_id`, and
`subscription_item_id`) hold IDs related to the subscription item change event.

### Example queries

For additional and most up to date examples, please reference the [Subscriptions
section of query template library in Sigma
sidebar](https://dashboard.stripe.com/sigma/queries).

To calculate the monthly recurring revenue (MRR) and the number of active
subscribers from this table, you’ll need to use window functions. Additionally,
if you have customers using different currencies, you’ll need to perform foreign
currency exchange calculations. The calculation aims to track monthly MRR and
the evolution of active subscribers, distinguishing between new additions,
reactivations, expansions, contractions, and churns. The final results are
presented in minor currency units, such as cents for USD.

```
WITH ts_grouped_sub_item_events AS (
 SELECT
 local_event_timestamp,
 customer_id,
 currency,
 sum(mrr_change) AS mrr_change
 FROM
 subscription_item_change_events
 GROUP BY
 1,
 2,
 3
),
ts_grouped_sub_item_events_with_mrr AS (
 SELECT
 *,
 date_trunc(
 'day',
 date(local_event_timestamp)
 ) AS local_event_date,
 -- Stripe defines an "active subscriber" as a customer with non-zero MRR.
-- Therefore instead of summing up event_type to get subscription count (and its
diff),
-- We count the amount of revenue on each customer instead and later check its
movement from / to zero
 sum(mrr_change) over (
 PARTITION by customer_id
 ORDER BY
 local_event_timestamp ASC
 ) AS mrr,
-- We count the # of times MRR has actually changed, and use nullif to ignore
events that do not impact MRR
 -- Otherwise we may confuse between new vs. reactivation
 count(nullif(mrr_change, 0)) over (
 PARTITION by customer_id
 ORDER BY
 local_event_timestamp ASC
 ) AS mrr_change_count
 FROM
 ts_grouped_sub_item_events
),
ts_grouped_sub_item_events_with_previous_mrr AS (
 SELECT
 *,
 coalesce(
 last_value(mrr) IGNORE nulls OVER (
 PARTITION by customer_id
 ORDER BY
 local_event_timestamp ASC ROWS BETWEEN UNBOUNDED PRECEDING
 AND 1 PRECEDING
 ),
 0
 ) AS previous_mrr
 FROM
 ts_grouped_sub_item_events_with_mrr
),
customer_events AS (
 SELECT
 *,
 CASE
 WHEN mrr = 0
 AND previous_mrr > 0 THEN 'ACTIVE_END'
 WHEN mrr > 0
 AND previous_mrr = 0
 AND mrr_change_count = 1 THEN 'ACTIVE_START'
 WHEN mrr > 0
 AND previous_mrr = 0
 AND mrr_change_count > 1 THEN 'REACTIVATE'
 WHEN mrr > previous_mrr THEN 'ACTIVE_UPGRADE'
 WHEN mrr < previous_mrr THEN 'ACTIVE_DOWNGRADE'
 ELSE NULL
 END AS cus_event_type
 FROM
 ts_grouped_sub_item_events_with_previous_mrr
),
date_grouped_customer_events AS (
 SELECT
 local_event_date,
 currency,
 sum(mrr_change) AS mrr_change,
 sum(
 CASE
 cus_event_type
 WHEN 'ACTIVE_START' THEN mrr_change
 ELSE 0
 END
 ) AS new_mrr,
 sum(
 CASE
 cus_event_type
 WHEN 'REACTIVATE' THEN mrr_change
 ELSE 0
 END
 ) AS reactivation_mrr,
 sum(
 CASE
 cus_event_type
 WHEN 'ACTIVE_UPGRADE' THEN mrr_change
 ELSE 0
 END
 ) AS expansion_mrr,
 sum(
 CASE
 cus_event_type
 WHEN 'ACTIVE_DOWNGRADE' THEN mrr_change
 ELSE 0
 END
 ) AS contraction_mrr,
 sum(
 CASE
 cus_event_type
 WHEN 'ACTIVE_END' THEN mrr_change
 ELSE 0
 END
 ) AS churn_mrr,
 sum(
 CASE
 WHEN mrr = 0
 AND previous_mrr > 0 THEN -1
 WHEN mrr > 0
 AND previous_mrr = 0 THEN 1
 ELSE 0
 END
 ) AS active_subscribers_change,
 sum(
 CASE
 cus_event_type
 WHEN 'ACTIVE_END' THEN 1
 ELSE 0
 END
 ) AS churned_subscribers,
 sum(
 CASE
 cus_event_type
 WHEN 'ACTIVE_START' THEN 1
 ELSE 0
 END
 ) AS new_subscribers,
 sum(
 CASE
 cus_event_type
 WHEN 'REACTIVATE' THEN 1
 ELSE 0
 END
 ) AS reactivated_subscribers
 FROM
 customer_events
 GROUP BY
 1,
 2
),
-- Prepare the multi dimensional table with all days + currency combinations and
conversion rate metadata
-- note that exchange_rates_from_usd contains one row for every date from
2010-01-07 until today
-- which is why we don't need to generate a separate date series for the full
table
dates_with_rate_per_usd AS (
 SELECT
 -- We use previous day's closing rates in precomputed metrics
 date - INTERVAL '1' DAY AS fx_date,
 cast(
 json_parse(buy_currency_exchange_rates) AS map(varchar, double)
 ) AS rate_per_usd
 FROM
 exchange_rates_from_usd
),
currencies AS (
 SELECT
 DISTINCT(currency)
 FROM
 subscription_item_change_events
),
first_default_currency AS (
 SELECT
 default_currency
 FROM
 accounts
 WHERE
 default_currency IS NOT NULL
 LIMIT
 1
),
dates_x_currencies_with_conversion_rate AS (
 SELECT
 fx_date as local_date,
 currency,
 default_currency,
1 / rate_per_usd [currency] * rate_per_usd [coalesce(default_currency, 'usd')]
AS conversion_rate
 FROM
 dates_with_rate_per_usd
 CROSS JOIN currencies
 CROSS JOIN first_default_currency
 ORDER BY
 1,
 2
),
daily_metrics_by_currency AS (
 SELECT
 dpc.local_date,
 dpc.currency,
 dpc.conversion_rate,
 coalesce(
 sum(mrr_change) over (
 PARTITION by dpc.currency
 ORDER BY
 dpc.local_date ASC
 ),
 0
 ) AS mrr,
 coalesce(
 round(
 sum(mrr_change) over (
 PARTITION by dpc.currency
 ORDER BY
 dpc.local_date ASC
 ) * dpc.conversion_rate
 ),
 0
 ) AS converted_mrr,
 coalesce(round(new_mrr * conversion_rate), 0) AS converted_new_mrr,
coalesce(round(reactivation_mrr * conversion_rate), 0) AS
converted_reactivation_mrr,
coalesce(round(expansion_mrr * conversion_rate), 0) AS converted_expansion_mrr,
coalesce(round(contraction_mrr * conversion_rate), 0) AS
converted_contraction_mrr,
 coalesce(round(churn_mrr * conversion_rate), 0) AS converted_churn_mrr,
 coalesce(dgce.mrr_change, 0) AS mrr_change,
 coalesce(dgce.new_mrr, 0) AS new_mrr,
 coalesce(dgce.reactivation_mrr, 0) AS reactivation_mrr,
 coalesce(dgce.expansion_mrr, 0) AS expansion_mrr,
 coalesce(dgce.contraction_mrr, 0) AS contraction_mrr,
 coalesce(dgce.churn_mrr, 0) AS churn_mrr,
 coalesce(
 sum(active_subscribers_change) over (
 PARTITION by dpc.currency
 ORDER BY
 dpc.local_date ASC
 ),
 0
 ) AS active_subscribers,
 coalesce(dgce.active_subscribers_change, 0) AS active_subscribers_change,
 coalesce(dgce.churned_subscribers, 0) AS churned_subscribers,
 coalesce(dgce.new_subscribers, 0) AS new_subscribers,
 coalesce(dgce.reactivated_subscribers, 0) AS reactivated_subscribers
 FROM
 dates_x_currencies_with_conversion_rate dpc
LEFT JOIN date_grouped_customer_events dgce ON dpc.local_date =
dgce.local_event_date
 AND dpc.currency = dgce.currency
),
daily_metrics AS (
 SELECT
 local_date,
 sum(converted_mrr) AS mrr,
 sum(converted_new_mrr) AS new_mrr,
 sum(converted_reactivation_mrr) AS reactivation_mrr,
 sum(converted_expansion_mrr) AS expansion_mrr,
 sum(converted_contraction_mrr) AS contraction_mrr,
 sum(converted_churn_mrr) AS churn_mrr,
-- Customer can only have active subscription in a single currency at a time, as
a result this does not result in over-counting subscriber changes
-- This also matches the precomputed metrics logic in billing dashboard / CSV
download
 sum(active_subscribers) AS active_subscribers,
 sum(churned_subscribers) AS churned_subscribers,
 sum(new_subscribers) AS new_subscribers,
 sum(reactivated_subscribers) AS reactivated_subscribers
 FROM
 daily_metrics_by_currency
 GROUP BY
 1
),
daily_metrics_with_derived AS (
 SELECT
 *,
 mrr - lag(mrr) over (
 ORDER BY
 local_date
) - new_mrr - reactivation_mrr - expansion_mrr - contraction_mrr - churn_mrr AS
fx_adjustment_mrr,
 lag(mrr) over (
 ORDER BY
 local_date
 ) AS previous_mrr
 FROM
 daily_metrics
),
-- Turn daily into monthly metrics
monthly_metrics_with_derived AS (
 SELECT
 date_trunc('month', local_date) AS local_month_start,
 max_by(mrr, local_date) AS ending_mrr,
 sum(new_mrr) AS new_mrr,
 sum(reactivation_mrr) AS reactivation_mrr,
 sum(expansion_mrr) AS expansion_mrr,
 sum(contraction_mrr) AS contraction_mrr,
 sum(churn_mrr) AS churn_mrr,
 sum(fx_adjustment_mrr) AS fx_adjustment_mrr,
 max_by(active_subscribers, local_date) AS ending_subscribers,
 sum(churned_subscribers) AS churned_subscribers,
 sum(new_subscribers) AS new_subscribers,
 sum(reactivated_subscribers) AS reactivated_subscribers
 FROM
 daily_metrics_with_derived
 GROUP BY
 1
)
SELECT
 local_month_start,
ending_mrr - fx_adjustment_mrr - churn_mrr - contraction_mrr - expansion_mrr -
reactivation_mrr - new_mrr AS beginning_mrr,
 new_mrr,
 reactivation_mrr,
 expansion_mrr,
 contraction_mrr,
 churn_mrr,
 fx_adjustment_mrr,
 ending_mrr,
-- Churned subscribers is a positive number in CSV reports instead of negative
for churn / contraction mrr
ending_subscribers - (-1 * churned_subscribers) - reactivated_subscribers -
new_subscribers AS beginning_subscribers,
 new_subscribers,
 reactivated_subscribers,
 churned_subscribers,
 ending_subscribers
FROM
 monthly_metrics_with_derived
ORDER BY
 1 DESC
```

local_month_startbeginning_mrrnew_mrrreactivation_mrrexpansion_mrrcontraction_mrrchurn_mrrfx_adjustment_mrrending_mrrbeginning_subscribersnew_subscribersreactivated_subscriberschurned_subscribersending_subscribers2024-05-011000721491040000400000001002161499300122024-04-011000651497180000-18001000721497300122024-03-01100066099124000-10740100065149720272024-02-011000660991000000-10000100066099710172024-01-011000381022921601998-175-30420100066099540272023-12-01100038102000000100038102500052023-11-01100037102100000000100038102410052023-10-01100037102000000100037102400042023-09-01100037102000000100037102400042023-08-011000339020050000-18000100037102500142023-07-011000370650000-3159-4100033902600152023-06-0110003640235336900-27421100037065613462023-05-011000348982748030437-83-315980100036402730462023-04-01100034065933000-1000100034898620172023-03-011000027153135000000100034065420062023-02-011000060486086060880-155070100002715520342023-01-011000060483043000-30430100006048510152022-12-011001521342591001363600-30000-1505574-221000060489601052022-11-01100178232486883333621878-10600-689397010015213471611592022-10-0110003619313633312000020600-10000-124894010017823274267

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [Subscription](https://docs.stripe.com/api#subscription_object)
- [Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions)
- [Customer](https://docs.stripe.com/api#customers)
- [charges](https://docs.stripe.com/stripe-data/query-transactions)
- [tiers](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
- [invoices](https://docs.stripe.com/invoicing/overview)
- [Invoice](https://docs.stripe.com/api#invoice_object)
- [invoice items](https://docs.stripe.com/api#invoiceitems)
- [invoice) line items](https://docs.stripe.com/api#invoice_line_item_object)
-
[cancel_at_period_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-cancel_at_period_end)
- [Usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)
- [Meter](https://docs.stripe.com/api/billing/meter)
- [Billing Meter Event
Summary](https://docs.stripe.com/api/billing/meter-event-summary)
- [Billing Meter Invalid
Event](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#handle-meter-event-errors)
- [Coupon](https://docs.stripe.com/billing/subscriptions/coupons)
- [Discount](https://docs.stripe.com/api#discounts)
- [promotion code](https://docs.stripe.com/api/promotion_codes)
- [Monthly Recurring Revenue
(MRR)](https://support.stripe.com/questions/calculating-monthly-recurring-revenue-(mrr)-in-billing)
- [ISO currency code](https://docs.stripe.com/currencies)
- [Subscriptions section of query template library in Sigma
sidebar](https://dashboard.stripe.com/sigma/queries)