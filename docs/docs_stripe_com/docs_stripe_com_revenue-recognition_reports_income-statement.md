# Income statement

## Learn about the income statement report.

The income statement provides a detailed revenue and contra revenue breakdown by
month. It shows revenue, contra revenue, expenses, gains, and losses. Contra
revenue adjustments are deductions from gross revenue. Applying the contra
revenue to your gross revenue results in your net income. Use this report to
better understand your net revenue and determine how you want to track contra
revenue items.

The report is available to download from our [accounting
reports](https://dashboard.stripe.com/revenue-recognition/accounting-reports)
page with multiple format options.

## Replication in Sigma

To replicate the income report in
[Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard), use the
`revenue_recognition_debits_and_credits` table.

### Group By Account

This sample query generates the report for revenue booked for the accounting
period of October 2023 and grouped by account. You can adjust the dates to your
desired time frame as well as different grouping parameters.

```
with zero_decimal_currencies as (
 values
 'bif',
 'clp',
 'djf',
 'gnf',
 'jpy',
 'kmf',
 'krw',
 'mga',
 'pyg',
 'rwf',
 'vnd',
 'vuv',
 'xaf',
 'xof',
 'xpf'
),
formatted_changes as (
 select
 booked_date,
 date_format(accounting_period_date, '%Y-%m-%d') as accounting_period,
 is_accounting_period_open,
 debit,
 credit,
 debit_account_type,
 credit_account_type,
 invoice_id,
 product_id,
 customer_balance_transaction_id,
 event_type,
 currency,
 presentment_currency,
 if(
 lower(currency) in (
 select
 *
 from
 zero_decimal_currencies
 ),
 cast(presentment_amount as decimal(18, 0)),
 cast(0.01 * presentment_amount as decimal(18, 2))
 ) as decimalized_presentment_amount,
 if(
 lower(currency) in (
 select
 *
 from
 zero_decimal_currencies
 ),
 cast(amount as decimal(18, 0)),
 cast(0.01 * amount as decimal(18, 2))
 ) as decimalized_settlement_amount
 from
 revenue_recognition_debits_and_credits
),
raw_net_changes as (
 select
 debit as account,
 debit_account_type as account_type,
 decimalized_settlement_amount as raw_net_change,
 decimalized_presentment_amount as presentment_raw_net_change,
 *
 from
 formatted_changes
 union all
 select
 credit as account,
 credit_account_type as account_type,
 - decimalized_settlement_amount as raw_net_change,
 - decimalized_presentment_amount as presentment_raw_net_change,
 *
 from
 formatted_changes
),
net_changes as (
 select
 (
 case
when account_type in ('Assets', 'ContraRevenue', 'Expenses', 'Losses') then
raw_net_change
 else - raw_net_change
 end
 ) as net_change,
 (
 case
when account_type in ('Assets', 'ContraRevenue', 'Expenses', 'Losses') then
presentment_raw_net_change
 else - presentment_raw_net_change
 end
 ) as presentment_net_change,
 *
 from
 raw_net_changes
),
ungrouped_results as (
 select
 case
 when is_accounting_period_open then accounting_period
 else null
 end as open_accounting_period,
 case
 when is_accounting_period_open then null
 else accounting_period
 end as accounting_period,
 currency,
 presentment_currency,
 account_type,
 account,
 booked_date,
 product_id,
 invoice_id,
 event_type,
 presentment_net_change,
 net_change
 from
 net_changes
 where
 account_type in ('Revenue', 'ContraRevenue', 'Expenses', 'Gains', 'Losses')
and accounting_period >= date_format(timestamp '2023-10-01 00:00:00',
'%Y-%m-%d')
 and accounting_period <= date_format(
 date_add('second', -1, timestamp '2023-11-01 00:00:00'),
 '%Y-%m-%d'
 )
)
select
 currency,
 presentment_currency,
 open_accounting_period,
 accounting_period,
 account_type,
 account,
sum(net_change * (case when account_type in ('Revenue', 'Gains') then 1 else -1
end)) as net_income,
sum(presentment_net_change * (case when account_type in ('Revenue', 'Gains')
then 1 else -1 end)) as presentment_net_income
from
 ungrouped_results
group by
 currency,
 presentment_currency,
 open_accounting_period,
 accounting_period,
 account_type,
 account
```

### Group By Line Item

This sample query generates the report for revenue booked for the accounting
period of Feb 2024 and grouped by line item. You can adjust the dates to your
desired time frame as well as different grouping parameters.

To retrieve customer address information, join the results of this Sigma query
with the
[invoices](https://docs.stripe.com/stripe-data/query-billing-data#invoices)
Sigma table.

#### Note

If you’re using our [chart of
accounts](https://docs.stripe.com/revenue-recognition/chart-of-accounts) beta
feature, be sure to update the `unbilled_ar_accounts` mapping in the query below
to reflect the accounts in your general ledger.

```
select "accounting_period", "presentment_currency", "transaction_model_id",
"account_type", "account", "booked_date", "presentment_net_income",
"invoice_id", "line_item_id", "invoice_item_id", "charge_description",
"invoice_line_item_description" from (
 select
 original.*
 , charges.description as charge_description
 , invoice_line_items.description as invoice_line_item_description
FROM
 (
 with unbilled_ar_accounts as (
 values 'UnbilledAccountsReceivable'
 )
 , formatted_changes as (
 select
 livemode,
 invoice_id,
 line_item_id,
 invoice_item_id,
 subscription_item_id,
 customer_balance_transaction_id,
 charge_id,
 refund_id,
 debit,
 credit,
 debit_account_type,
 credit_account_type,
 debit_gl_code,
 credit_gl_code,
 accounting_period_date,
 presentment_amount,
 presentment_currency,
 date_format(accounting_period_date, '%Y-%m-%d') as accounting_period,
 date_format(booked_date, '%Y-%m-%d') as booked_date,
 coalesce(
 invoice_id,
 invoice_item_id,
 charge_id,
 refund_id,
 subscription_item_id,
 customer_balance_transaction_id,
 customer_id
 ) as linked_invoice_id,
 coalesce(
 invoice_item_id,
 line_item_id,
 invoice_id,
 charge_id,
 refund_id,
 subscription_item_id,
 customer_balance_transaction_id,
 customer_id
 ) as linked_invoice_line_item_id
 ,
if(lower(presentment_currency) in ('bif', 'clp', 'djf', 'gnf', 'jpy', 'kmf',
'krw', 'mga', 'pyg', 'rwf', 'vnd', 'vuv', 'xaf', 'xof', 'xpf'),
cast(presentment_amount as decimal(18, 0)), cast(0.01 * presentment_amount as
decimal(18, 2))) as decimalized_amount,
case when debit in (select * from unbilled_ar_accounts) OR credit in (select *
from unbilled_ar_accounts) then true else false end AS is_unbilled
 from revenue_recognition_debits_and_credits
)

, raw_net_changes as (
 select
 debit as account,
 debit_gl_code as gl_code,
 debit_account_type as account_type,
 decimalized_amount as presentment_raw_net_change,
 *
 from formatted_changes
 union all
 select
 credit as account,
 credit_gl_code as gl_code,
 credit_account_type as account_type,
 -decimalized_amount as presentment_raw_net_change,
 *
 from formatted_changes
)

, net_changes as (
 select
 (case when account_type in ('Assets', 'ContraRevenue', 'Expenses', 'Losses')
then presentment_raw_net_change else -presentment_raw_net_change end) as
presentment_net_change,
 *
 from raw_net_changes
)

, ungrouped_results as (
 select
 presentment_currency,
 	accounting_period,
 linked_invoice_line_item_id as transaction_model_id,
 account_type,
 account,
 gl_code,
 booked_date,
 invoice_id,
 line_item_id,
 invoice_item_id,
 charge_id,
 presentment_net_change
 from net_changes
 where
 account_type in ('Revenue', 'ContraRevenue', 'Expenses', 'Gains', 'Losses')
and accounting_period >= date_format(timestamp '2024-02-01 00:00:00',
'%Y-%m-%d')
and accounting_period <= date_format(date_add('second', -1, timestamp
'2024-03-01 00:00:00'), '%Y-%m-%d')
),
results as (
 select
 presentment_currency,
 accounting_period,
 transaction_model_id,
 account_type,
 account,
 gl_code,
 booked_date,
 arbitrary(invoice_id) as invoice_id,
 arbitrary(line_item_id) as invoice_line_item_id,
 arbitrary(invoice_item_id) as invoice_item_id,
 max(charge_id) as charge_id,
sum(presentment_net_change * (case when account_type in ('Revenue', 'Gains')
then 1 else -1 end)) as presentment_net_income
 from ungrouped_results
group by presentment_currency, accounting_period, transaction_model_id,
account_type, account, gl_code, booked_date
)

select
 accounting_period,
 presentment_currency,
 transaction_model_id,
 account_type,
 account,
 gl_code,
 booked_date,
 invoice_id,
 invoice_line_item_id as line_item_id,
 invoice_item_id,
 charge_id,
 presentment_net_income
from results
where
 presentment_net_income != 0

order by accounting_period, presentment_currency, transaction_model_id,
account_type, account, gl_code, booked_date

 ) original
 left join charges on charges.id = original.charge_id
 left join invoices on original.invoice_id = invoices.id
left join invoice_line_items on invoice_line_items.id = original.line_item_id

)
```

## Links

- [accounting
reports](https://dashboard.stripe.com/revenue-recognition/accounting-reports)
- [Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard)
- [invoices](https://docs.stripe.com/stripe-data/query-billing-data#invoices)
- [chart of
accounts](https://docs.stripe.com/revenue-recognition/chart-of-accounts)