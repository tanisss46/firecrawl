# Query fees data

## Use Sigma or Data Pipeline to retrieve information about transaction and product fees.

Use the `itemized_fees` table to get a comprehensive, granular breakdown of
every fee charged or deducted from your Stripe balance. For example, if a
balance transaction indicates a 2 USD fee for a card payment, you can query this
transaction within the `itemized_fees` table to understand the breakdown. You
can also use the table to understand the total fees paid to Stripe over a given
period of time.

The `itemized_fees` table can include the following columns:

ColumnDescription`balance_transaction_created`Time (in UTC) at which the balance
transaction affected your Stripe balance.`balance_transaction_id`The ID of the
balance transaction that debited the fee from your
balance.`balance_transaction_description`The description of the balance
transaction containing the fee.`incurred_by`The ID of the object that incurred
this fee, if any. Use the `incurred_by_type` field to determine the type of this
object.`incurred_by_type`The object type which `incurred_by` references. Matches
the object field in the API ([Charge](https://docs.stripe.com/api/charges),
[Refund](https://docs.stripe.com/api/refunds),
[Invoice](https://docs.stripe.com/api/invoices), etc).`amount`Fee incurred for
this activity, expressed in major units of the currency. The amount excludes the
tax amount.`tax`Tax component of the fees paid, expressed in major units of the
currency.`currency`Three-letter [ISO code for the
currency](https://docs.stripe.com/currencies) in which the amount and tax are
defined.`incurred_at`Time (in UTC) at which the fee was incurred, by the date of
its originating event.`activity_start_date`For fees calculated from activity
spanning a period of time, this will be the activity’s starting date (in
UTC).`activity_end_date`For fees calculated from activity spanning a period of
time, this will be the activity’s ending date (in
UTC).`product_feature_description`The product or feature associated with the
fee.
The following example shows how to extract information about the five most
recent fee transactions:

```
select
 date_format(date_trunc('day', incurred_at), '%m-%d-%Y') as day,
 balance_transaction_id,
 amount,
 tax,
 product_feature_description
from
 itemized_fees
order by
 incurred_at desc
limit 5;
```

To get a more granular view of your activity, join the `itemized_fees` table
with other tables in the schema . For example, join the `balance_transactions`
table with the `itemized_fees` table to retrieve fee information for each
balance transaction.

Here is an example of how to join these tables together, returning different
types of fees applied, and detailed descriptions of the fees:

```
select
date_format(date_trunc('day', itemized_fees.balance_transaction_created),
'%m-%d-%Y') as day,
 balance_transactions.id as balance_transaction_id,
 balance_transactions.reporting_category as reporting_category,
 itemized_fees.amount as fee_amount,
 itemized_fees.tax as tax_amount
from
 balance_transactions
inner join
itemized_fees on balance_transactions.id = itemized_fees.balance_transaction_id
order by
 day desc
limit 5;
```

## Fees paid by connected accounts

If you have a platform account with Stripe Connect, use the
`connected_account_itemized_fees` table to get insight on fees paid by your
connected accounts.

Like the `itemized_fees table`, the `connected_account_itemized_fees` table
provides a granular record of fee transactions, but from the perspective of your
connected accounts. These datasets mostly share common attributes, though the
`connected_account_itemized_fees` dataset has an additional `account` column.
This `account` column enables platform accounts to track and report on the fees
paid by each of their connected accounts.

To identify all fee transactions associated with a specific connected account
over a particular time period, use the `connected_account_itemized_fees` table .
Here’s an example of a query that can retrieve the top 10 connected accounts
based on the total fees they have paid:

```
select
 account,
 sum(amount) as total_fees
from
 connected_account_itemized_fees
where
 incurred_at between 'start_date' and 'end_date'
group by
 account
order by
 total_fees desc
limit 10;
```

Replace `start_date` and `end_date` with the specific dates you want to analyze
in the format `YYYY-MM-DD`. This query sums the total fees paid by each
connected account within the specified date range and returns the top 10
accounts with the highest total fees.

## Links

- [Charge](https://docs.stripe.com/api/charges)
- [Refund](https://docs.stripe.com/api/refunds)
- [Invoice](https://docs.stripe.com/api/invoices)
- [ISO code for the currency](https://docs.stripe.com/currencies)