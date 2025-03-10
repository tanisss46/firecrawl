# Query card issuing data

## Use Sigma or Data Pipeline to retrieve card issuing information.

The Issuing objects represented within Sigma or Data Pipeline includes
[Authorizations](https://docs.stripe.com/api/issuing/authorizations/object),
[Transactions](https://docs.stripe.com/api/issuing/transactions/object),
[Cards](https://docs.stripe.com/api/issuing/cards/object), and
[Cardholders](https://docs.stripe.com/api/issuing/cardholders/object).
Issuing-specific tables can be found within the Issuing section of the schema.

Issuing data for your connected accounts can be found within tables prefaced
with `connected_account_`, for
example,`connected_account_issuing_authorizations`. More information about using
[Connect](https://docs.stripe.com/connect) with Sigma or Data Pipeline can be
found in the [Connect](https://docs.stripe.com/stripe-data/query-connect-data)
section of the documentation.

## Authorizations

Whenever an issued card is used to make a purchase, an
[Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
object is created. Each row within the `issuing_authorizations` table represents
data about this object. The same information can be retrieved through the API
and is available in the [Stripe
Dashboard](https://dashboard.stripe.com/test/issuing/authorizations). Note that
the [request
history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history)
field isn’t currently available. Every authorization that has been created on
your account is available in Sigma or Data Pipeline.

The `card_id` column of this table stores the ID of the card used to make the
purchase. You can find additional information about the card that initiated the
authorization by joining the column with the `issuing_cards` table.

To access the transactions associated with a particular authorization, you can
join the `authorization_id` column in the `issuing_transactions` table.

!

The following query computes counts of authorizations grouped by approval
status.

```
select
 date_trunc('month', created) as month,
 count(case when approved then 1 end) as num_approved_authorizations,
 count(*) as total_num_authorizations
from issuing_authorizations
where date_trunc('month', created) between date_trunc('month', date_add('month',
-13, date(data_load_time)))
and date_trunc('month', date_add('month', -1, date(data_load_time)))
group by 1
order by 1 desc, 2
limit 2
```

monthapprovednum_authorizations2025-03-01false5062025-03-01true10,045
## Transactions

An Issuing
[Transaction](https://docs.stripe.com/api/issuing/transactions/object) object
represents any use of an issued card that results in funds entering or leaving
your Stripe account, such as a completed purchase or refund. The
`issuing_transactions` table stores information about these objects. You can
retrieve the same information through the API, and it’s also available in the
[Stripe Dashboard](https://dashboard.stripe.com/test/issuing/transactions).

For additional details about the transaction, such as the fee, you can access
the associated [balance
transaction](https://docs.stripe.com/api#balance_transaction_object). You can do
this by joining the `balance_transaction_id` column with the `id` column of the
`balance_transactions` table. Balance transactions are not Issuing-specific
objects. More information about working with balance transactions in Sigma or
Data Pipeline can be found in the
[Transactions](https://docs.stripe.com/stripe-data/query-transactions) section
of the documentation.

The `authorization_id` column allows you to access the
[Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
object associated with the Transaction by joining on the `id` column of the
`issuing_authorizations` table. This can provide additional details about how
the transaction was authorized. The `authorization_id` column on an Issuing
transaction can be empty in the event of [force
capture](https://docs.stripe.com/issuing/purchases/transactions#handling-other-transactions)
and for some instances of
[refunds](https://docs.stripe.com/issuing/purchases/transactions).

You can also access both the card and cardholder involved in the transaction via
the `card_id` and `cardholder_id` columns. Information about the card is stored
in the `issuing_cards` table, and information about the cardholder is stored in
the `issuing_cardholders` table. The
[Card](https://docs.stripe.com/api/issuing/cards/object) and
[Cardholder](https://docs.stripe.com/api/issuing/cardholders/object) objects can
provide additional details about who initiated the transaction.

!

The following query returns information about the three most recent [over
captures](https://docs.stripe.com/issuing/purchases/transactions#handling-other-transactions).
It joins the `issuing_authorizations` table to determine if this transaction is
an over capture by comparing the amounts of the two objects.

```
select
 date_format(it.created, '%Y-%m-%d') as day,
 it.id,
 ia.amount as authorized_amount,
 -1 * it.amount as captured_amount
from issuing_transactions it
join issuing_authorizations ia
on it.authorization_id=ia.id
where
 it.type='capture' and
-1 * it.amount > ia.amount --- This checks if this transaction was overcaptured
order by day desc
limit 3
```

dayidauthorized_amountcaptured_amount2025-03-09ipi_EH4V4EdBC7QpGHH1501512025-03-09ipi_krzD8rfVgIfmN3X01,0002025-03-09ipi_pPMfwusTcNRKqTC14501050
One of the benefits of using Sigma or Data Pipeline with Issuing is the ability
to aggregate data. The following example joins the `balance_transactions` table
and aggregates each of the types of fees for Issuing transactions by month.

```
select
 date_trunc('month', it.created) as month,
 fd.type as fee_type,
 sum(fd.amount) as net_fees,
 sum(it.amount) as net_amount
from issuing_transactions it
inner join balance_transactions bt
on bt.id=it.balance_transaction_id
inner join balance_transaction_fee_details fd
on fd.balance_transaction_id=bt.id
group by 1,2
order by month desc, fee_type
```

monthfee_typenet_feesnet_amount2025-03-01stripe-fee59010,0002025-04-01stripe-fee591,0002025-05-01stripe-fee59010,000
## Cards

The `issuing_cards` table contains data about an individual
[Card](https://docs.stripe.com/api/issuing/cards/object) object. The same
information is available through the API and within the [Stripe
Dashboard](https://dashboard.stripe.com/test/issuing/cards). The [spending
controls](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls)
field isn’t currently available.

Every issued card has an associated
[Cardholder](https://docs.stripe.com/api/issuing/cardholders), which can be
accessed by joining the `issuing_cardholders` table on the `cardholder_id`
column.

!

## Cardholders

[Cardholder](https://docs.stripe.com/api/issuing/cardholders/object) data is
stored within the `issuing_cardholders` table. The same information can be
retrieved through the API or with the [Stripe
Dashboard](https://dashboard.stripe.com/test/issuing/cardholders). The [spending
controls](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls)
field isn’t currently available.

This table can be joined to other tables to provide information about the entity
that initiated a transaction or owns an issued card.

!

The following example retrieves information about the three most recently
created active cardholders.

```
select
 date_format(created, '%Y-%m-%d') as day,
 id,
 email,
 type
from issuing_cardholders
where status='active'
limit 3
```

dayidemailtype2025-03-01ich_54O2ChSJfDJZtbFj.smith@example.comindividual2025-03-01ich_rLOKWqLRSAjvhFpentity@example.combusiness_entity2025-03-01ich_boI9l4ZiUkQpSySj.doe@example.comindividual
### Metadata

Metadata for each Issuing object is stored in a separate table. The names of
these tables is the name of the object’s table with the addition of `_metadata`
to the end, for example, `issuing_transactions_metadata`. The metadata table
contains a foreign key to the corresponding object in the primary table that you
can use to join the two tables. For example, every row in the
`issuing_transactions_metadata` table has the column `issuing_transaction_id`
that references the `id` column of a row in the `issuing_transactions` table.

The following example creates a dictionary from the `issuing_transactions`
table’s metadata table. It then uses it to access the value of the metadata key
`'my_label'` for several transactions.

```
with transactions_metadata_dictionary as (
 select
 issuing_transaction_id,
 map_agg(key, value) metadata_dictionary
 from issuing_transactions_metadata
 group by 1
)

select
 date_format(it.created, '%Y-%m-%d') as day,
 it.id,
 it.amount,
 metadata_dictionary['my_label'] as my_label_value
from issuing_transactions it
left join transactions_metadata_dictionary
 on it.id = transactions_metadata_dictionary.issuing_transaction_id
where element_at(metadata_dictionary, 'my_label') is not null
order by day desc
limit 3
```

dayidamountmy_label_value2025-03-01ipi_Za8nLWjhq1YnYdt2000true2025-03-01ipi_HRtCXzltA0hLoPk100true2025-03-01ipi_2l23sGt1fdze5VK10000false

## Links

- [Authorizations](https://docs.stripe.com/api/issuing/authorizations/object)
- [Transactions](https://docs.stripe.com/api/issuing/transactions/object)
- [Cards](https://docs.stripe.com/api/issuing/cards/object)
- [Cardholders](https://docs.stripe.com/api/issuing/cardholders/object)
- [Connect](https://docs.stripe.com/connect)
- [Connect](https://docs.stripe.com/stripe-data/query-connect-data)
- [Stripe Dashboard](https://dashboard.stripe.com/test/issuing/authorizations)
- [request
history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history)
- [Stripe Dashboard](https://dashboard.stripe.com/test/issuing/transactions)
- [balance transaction](https://docs.stripe.com/api#balance_transaction_object)
- [Transactions](https://docs.stripe.com/stripe-data/query-transactions)
- [force
capture](https://docs.stripe.com/issuing/purchases/transactions#handling-other-transactions)
- [refunds](https://docs.stripe.com/issuing/purchases/transactions)
- [Stripe Dashboard](https://dashboard.stripe.com/test/issuing/cards)
- [spending
controls](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls)
- [Cardholder](https://docs.stripe.com/api/issuing/cardholders)
- [Stripe Dashboard](https://dashboard.stripe.com/test/issuing/cardholders)