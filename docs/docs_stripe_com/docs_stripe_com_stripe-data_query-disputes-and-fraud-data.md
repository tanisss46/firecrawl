# Query disputes and fraud data

## Use Sigma or Data Pipeline to retrieve information about disputes and fraud.

The `disputes` table contains data about all
[disputes](https://docs.stripe.com/disputes) on your account. Each row
represents a [Dispute](https://docs.stripe.com/api#dispute_object) object, which
is created when a charge is disputed. Each dispute also includes any available
data about dispute evidence that you’ve submitted.

!

The following example provides some preliminary information about the five most
recent lost disputes. It joins the `disputes` and `charges` tables together
using the `disputes.charge_id` and `charges.id` columns. Along with a dispute
ID, each row contains an associated charge ID, the amount, and the outcome of
the ZIP and CVC checks.

```
select
 date_format(date_trunc('day', disputes.created), '%m-%d-%Y') as day,
 disputes.id,
 disputes.charge_id,
 disputes.amount,
 charges.card_address_zip_check as zip,
 charges.card_cvc_check as cvc
from disputes
inner join charges
on charges.id=disputes.charge_id
where disputes.status = 'lost'
and disputes.reason = 'fraudulent'
order by day desc
limit 5
```

dayidcharge_idamountzipcvc3/9/2025dp_8WEg4Cis6n7GuaQch_2UwzyhF3xhbmx6x1,000pass3/9/2025dp_XZrnaX4mL65ynPTch_OeUCQu0YDI4mmKf1,000passfail3/9/2025dp_Ez2b7o0slS2IfPCch_8XQReVcKlwTKXsj1,000failfail3/9/2025dp_mEmP893yhTxowXzch_zzLouulYcNWDltj1,000pass3/9/2025dp_nmBB5pFTvgpsTwDch_bPq1qYTRTKFJgvg1,000pass
Using Sigma or Data Pipeline to create reports about your disputes can help you
identify fraudulent payments, which you can prevent by using
[Radar](https://docs.stripe.com/radar).

## Radar for Fraud Teams Data

If you use Radar for Fraud Teams, you have a table `radar_rules` that contains
all Radar custom rules with their action and predicate. You can use this to
obtain the `rule_id` which can then be used in `rule_decisions` table to find
all charges affected by rules. This is more flexible than looking at the
`outcome_rule_id` attribute in the `charges` table, as it also shows 3DS Rules
triggered for Payment Intents and Setup Intents. Radar’s [built-in
rules](https://docs.stripe.com/radar/rules#built-in-rules) have fixed rule IDs.

The following example shows recent payments allowed by an allow-list and their
Radar score to check if potentially fraudulent payments were allowed:

```
select
 outcome_type,
 card_cvc_check,
 count(*) as cnt,
 avg(outcome_risk_score) as avg_risk_score
from
 charges
where
 outcome_rule_id = 'allow_if_in_allowlist'
 and created >= current_date - interval '14' day
group by
 1,
 2
```

### Platform data

Multiparty payment businesses such as Connect platforms have [particular risk
management requirements](https://docs.stripe.com/connect/risk-management).
Here’s an example of listing [destination
charge](https://docs.stripe.com/connect/destination-charges) businesses on your
platform by their dispute rate:

```
select
 m.value as merchant_external_account_id,
 c.destination_id,
 arbitrary(a.business_name) as destination_name,
 count(*) as cnt_charges,
 count_if(c.paid) as cnt_success_charges,
 count_if(c.paid) * 1.0 / count(*) as success_rate,
 if(
 count_if(dispute_id is not null) > 0,
 count_if(c.paid) * 1.0 / count_if(c.paid),
 0.0
 ) as dispute_rate
from
 charges c
 left join charges_metadata m on m.charge_id = c.id
 and m.key = 'merchant_external_account_id'
 join connected_accounts a on a.id = c.destination_id
where
 c.created >= current_date - interval '120' day
group by
 1,2
order by dispute_rate desc
```

### 3D Secure Data

Sigma and Data Pipelines contains data on 3D Secure Authentication
([3DS](https://docs.stripe.com/payments/3d-secure)). This more complex example
shows for each 3DS Rule how many times it triggered 3DS and what the outcomes
were, considering there might be more than one attempt:

```
select
 rd.rule_id,
 count(distinct rd.id) as cnt_rule_triggered,
count(distinct rd.payment_intent_id) * 1.0 / count(distinct rd.id) * 100.0 as
pct_pis,
count_if(at.is_final_attempt) * 1.0 / count(distinct rd.id) * 100.0 as
pct_final_attempts,
 count_if(
 at.is_final_attempt
 and at.threeds_outcome_result = 'authenticated'
 ) * 1.0 / count(distinct rd.id) * 100.0 as pct_3ds_final_authenticated,
 count_if(
 at.threeds_outcome_result = 'authenticated'
 and at.charge_outcome = 'authorized'
 ) * 1.0 / count(distinct rd.id) * 100.0 as pct_3ds_authorized
from
 rule_decisions rd
left join authentication_report_attempts at on at.intent_id =
rd.payment_intent_id
where
 action = 'request_credentials'
 and rd.created >= current_date - interval '30' day
group by
 1
```

### All Radar Rule Attributes and Decisions

You also have access to the `radar_rule_attributes` table. Each row contains
most of the [Radar rule
attribute](https://docs.stripe.com/radar/rules/reference#supported-attributes)
values for a single [charge](https://docs.stripe.com/api/charges/object). You
can join the `radar_rule_attributes` and `disputes` tables together using the
`radar_rule_attributes.transaction_id` and `disputes.charge_id` columns, which
allows you to write rules targeting your disputes and understand trends in your
good and bad customers.

```
select
 card_3d_secure_support,
 is_3d_secure_authenticated,
 cvc_check,
 avg(risk_score) as avg_risk_score,
avg(total_charges_per_card_number_all_time) as
avg_total_charges_per_card_number_all_time,
 count(*) as cnt_disputes
from
 radar_rule_attributes r
 join disputes d on r.transaction_id = d.charge_id
where
 d.created >= current_date - interval '60' day
group by
 1,2,3
order by
 cnt_disputes desc
```

For more details on columns available see our guide on [How to continuously
improve your fraud management with Radar for Fraud Teams and Stripe
Data](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data).
It explains, for instance, where to find Radar scores per Charges and so on.

## Tracking Monitoring Programs

[Card brand monitoring
program](https://docs.stripe.com/disputes/monitoring-programs) metrics are
difficult to track because rules are very specific. Some details are crucial,
such as when to use volume or transaction count. Tracking them is required to
estimate fraud and chargeback levels and take action promptly, because
monitoring program notifications don’t happen immediately. We recommend a
[continous
process](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
to track and estimate chargeback and fraud metrics.

With Sigma, you can write a query to estimate fraud levels that simulate how
card monitoring programs might assess your payments. The query below isn’t
perfect (for example, we assume this is a US merchant where domestic and
cross-border payments are counted, but you can adjust the query for your use
case). Most importantly, it takes FX (currency exchange rates) into account, and
applies the same method of counting payment and fraud periods independently as
the monitoring programs typically do.

```
with exchange_rates as (
 select
 date,
 currency,
 rate
 from
 exchange_rates_from_usd
 cross join unnest (
 cast(
 json_parse(buy_currency_exchange_rates) as map(varchar, double)
 )
 ) as t(currency, rate)
 where
 date = (
 select
 max(date)
 from
 exchange_rates_from_usd
 ) -- note the calculation for jpy is decimal and may look off
),
payments as (
 select
-- technically these values are calculated per statement descriptor for CNP but
we assume this equals merchant
 date_format(p.captured_at, '%Y-%m-01') as start_of_month,
 if(
 p.card_brand = 'Visa'
 or p.card_brand = 'MasterCard',
 p.card_brand,
 'Other'
 ) as network,
 count(*) as sales_count,
 -- For US, both Cross-Border and Domestic charges are counted
 -- we can ignore this in CBMP but show it here just to get a magnitude
 count_if(p.card_country != 'US') as sales_count_crossborder,
 count_if(pmd.card_3ds_succeeded) as sales_count_3ds,
 sum(p.amount / fx.rate / 100.0) as sales_volume_usd,
 sum(
 if(
 p.card_country != 'US',
 p.amount / fx.rate / 100.0
 )
 ) as sales_volume_crossborder_usd,
 sum(
 if(
 p.card_country = 'US'
 and pmd.card_3ds_succeeded,
 p.amount / fx.rate / 100.0
 )
 ) as sales_volume_3ds_us_usd
 from
 charges p
 join exchange_rates fx on p.currency = fx.currency
 left join payment_method_details pmd on pmd.charge_id = p.id
 -- for more information you may use
 -- left join authentication_report_attempts aa on attempt_id intent_id
 where
 p.captured_at >= date_trunc('month', current_date - interval '150' day)
-- CBMPs only consider cleared amounts; refunds still count in the volume unless
reversed
 and p.status = 'succeeded'
 and p.payment_method_type = 'card'
 group by
 1,
 2 -- used for VFMP
),
efw as (
 select
 date_format(e.created, '%Y-%m-01') as start_of_month,
 if(
 c.card_brand = 'Visa'
 or c.card_brand = 'MasterCard',
 c.card_brand,
 'Other'
 ) as network,
 -- For US, both Cross-Border and Domestic charges are counted
 -- count_if(card_country != 'US') as efw_count_crossborder
 count(distinct c.id) as efw_count,
 count(distinct if(pmd.card_3ds_succeeded, c.id)) as efw_count_3ds,
 sum(c.amount / fx.rate / 100.0) as efw_volume_usd,
 sum(
 if(
 pmd.card_3ds_succeeded,
 c.amount / fx.rate / 100.0
 )
 ) as efw_volume_3ds_usd,
 -- for VFMP-3DS
 sum(
 if(
 c.card_country = 'US'
 and pmd.card_3ds_succeeded,
 c.amount / fx.rate / 100.0
 )
 ) as efw_volume_3ds_us_usd
 from
 early_fraud_warnings e
 join charges c on e.charge_id = c.id
 join exchange_rates fx on c.currency = fx.currency
 left join payment_method_details pmd on pmd.charge_id = c.id
 where
 e.created >= date_trunc('month', current_date - interval '150' day)
 group by
 1,
 2 -- used for VDMP and ECM/ECP
),
disputes as (
 select
 date_format(d.created, '%Y-%m-01') as start_of_month,
 if(
 c.card_brand = 'Visa'
 or c.card_brand = 'MasterCard',
 c.card_brand,
 'Other'
 ) as network,
 -- For US, both Cross-Border and Domestic charges are counted
 -- count_if(card_country != 'US') as dispute_count_crossborder
 -- Because a payment can have multiple disputes, we count the disputes here
 count(distinct d.id) as dispute_count_all,
count(distinct if(d.reason = 'fraudulent', d.id)) as fraud_dispute_count_all,
 count(
 distinct if(
 d.network_details_visa_rapid_dispute_resolution,
 d.id
 )
 ) as dispute_count_rdr,
 count(
 distinct if(
 d.network_details_visa_rapid_dispute_resolution is null
 or not d.network_details_visa_rapid_dispute_resolution,
 d.id
 )
 ) as dispute_count_exrdr,
 count(distinct if(pmd.card_3ds_succeeded, d.id)) as dispute_count_3ds,
 count(
 distinct if(
 d.reason = 'fraudulent'
 and pmd.card_3ds_succeeded,
 d.id
 )
 ) as fraud_dispute_count_3ds,
 count(
 distinct if(
 d.reason = 'fraudulent'
 and (
 d.network_details_visa_rapid_dispute_resolution is null
 or not d.network_details_visa_rapid_dispute_resolution
 ),
 d.id
 )
 ) as fraud_dispute_count_exrdr,
 count_if(d.status = 'won') * 1.0 / count_if(
 d.status = 'won'
 or d.status = 'lost'
 ) as win_rate,
 -- The sum of disputes should match and cannot exceed the payment
 sum(d.amount / fx.rate / 100.0) as dispute_volume_usd_all,
 sum(
 if(
 reason = 'fraudulent',
 d.amount / fx.rate / 100.0
 )
 ) as fraud_dispute_volume_usd_all,
 sum(
 if(
 (
 d.network_details_visa_rapid_dispute_resolution is null
 or not d.network_details_visa_rapid_dispute_resolution
 ),
 d.amount / fx.rate / 100.0
 )
 ) as dispute_volume_usd_exrdr,
 sum(
 if(
 d.reason = 'fraudulent'
 and (
 d.network_details_visa_rapid_dispute_resolution is null
 or not d.network_details_visa_rapid_dispute_resolution
 ),
 d.amount / fx.rate / 100.0
 )
 ) as fraud_dispute_volume_usd_exrdr
 from
 disputes d
 join charges c on d.charge_id = c.id
 join exchange_rates fx on c.currency = fx.currency
 left join payment_method_details pmd on pmd.charge_id = c.id
 where
 -- current month data will usually be off due to dispute delays,
 -- we still show it as an indicator but it's better tracked weekly
 d.created >= date_trunc('month', current_date - interval '150' day)
 group by
 1,
 2
)
select
 -- theoretically this might cause gaps if there is a month
-- without payments but a helper table with continuous dates would complicate
this example query
 p.start_of_month,
 p.network,
 -- Used for VDMP/ECP/ECM/HEC
 p.sales_count,
 lag(p.sales_count, 1) over (
 order by
 p.network,
 p.start_of_month
 ) as sales_count_prior_month,
 p.sales_count_crossborder,
 p.sales_count_3ds,
 -- Used for VFMP
 p.sales_volume_usd,
 p.sales_volume_crossborder_usd,
 p.sales_volume_3ds_us_usd,
 e.efw_count,
 e.efw_count_3ds,
 -- Used for VFMP
 e.efw_volume_usd,
 e.efw_volume_3ds_usd,
 -- Used for VFMP-3DS
 e.efw_volume_3ds_us_usd,
 -- Used for VDMP/ECP/ECM/HEC
 d.dispute_count_all,
 d.dispute_count_rdr,
 d.fraud_dispute_count_all,
 d.dispute_count_exrdr,
 d.dispute_count_3ds,
 d.fraud_dispute_count_3ds,
 d.fraud_dispute_count_exrdr,
 d.dispute_volume_usd_all,
 -- Used for EFM
 d.fraud_dispute_volume_usd_all,
 d.dispute_volume_usd_exrdr,
 d.fraud_dispute_volume_usd_exrdr,
 d.win_rate,
-- we show all the values below for all networks for comparison but they're only
relevant for the indicated ones
 -- VDMP deducting RDR actuals
 if(
 p.network = 'visa',
 d.dispute_count_exrdr,
 d.dispute_count_all
 ) * 1.0 / p.sales_count as rdr_chargeback_ratio_for_visa,
 -- ECP/ECM/HECM based on prior month sales
 d.dispute_count_all * 1.0 / lag(p.sales_count, 1) over (
 order by
 p.network,
 p.start_of_month
 ) as all_chargeback_ratio_for_mastercard,
 -- VDMP ignoring RDR and ECP/ECM/HECM for crosscheck
d.dispute_count_all * 1.0 / p.sales_count as
all_chargeback_ratio_for_visa_and_mastercard,
 -- VFMP
 e.efw_volume_usd * 1.0 / p.sales_volume_usd as fraud_ratio_for_visa,
 -- VFMP-3DS
e.efw_volume_3ds_us_usd * 1.0 / p.sales_volume_3ds_us_usd as
fraud_ratio_for_visa_3ds,
 -- EFM based on prior month sales
 d.fraud_dispute_count_all * 1.0 / lag(p.sales_count, 1) over (
 order by
 p.network,
 p.start_of_month
 ) as fraud_ratio_for_mastercard
from
 payments p
 left join efw e on p.start_of_month = e.start_of_month
 and p.network = e.network
 left join disputes d on p.start_of_month = d.start_of_month
 and p.network = d.network
order by
 start_of_month desc,
 network;
```

## Links

- [disputes](https://docs.stripe.com/disputes)
- [Dispute](https://docs.stripe.com/api#dispute_object)
- [Radar](https://docs.stripe.com/radar)
- [built-in rules](https://docs.stripe.com/radar/rules#built-in-rules)
- [particular risk management
requirements](https://docs.stripe.com/connect/risk-management)
- [destination charge](https://docs.stripe.com/connect/destination-charges)
- [3DS](https://docs.stripe.com/payments/3d-secure)
- [Radar rule
attribute](https://docs.stripe.com/radar/rules/reference#supported-attributes)
- [charge](https://docs.stripe.com/api/charges/object)
- [How to continuously improve your fraud management with Radar for Fraud Teams
and Stripe
Data](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [Card brand monitoring
program](https://docs.stripe.com/disputes/monitoring-programs)