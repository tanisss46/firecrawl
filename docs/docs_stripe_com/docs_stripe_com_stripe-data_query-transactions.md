# Query transactional data

## Create custom reports for charges, refunds, transfers, and more.

Use the data in the tables within the
[schema](https://docs.stripe.com/stripe-data/write-queries) for reporting on
your account’s balance activity. The tables in the **Payment Tables** sections
represent funds that flow between your customers and your Stripe account, such
as charges or refunds. The **Transfer Tables** section has information about
transfers of your Stripe account balance to your bank account
([payouts](https://docs.stripe.com/payouts)).

Use the `balance_transactions` table as a starting point for accounting
purposes. Unlike using separate tables (such as `charges` or `refunds`), it
provides a ledger-style record of every
[type](https://docs.stripe.com/api#balance_transaction_object-type) of
transaction that comes into or flows out of your Stripe account balance. Use
balance transactions to generate frequently used reports and to simplify how you
report on financial activity. Some common types of balance transactions include:

- `charges`
- `refunds`
- `transfers`
- `payouts`
- `adjustments`
- `application_fees`

Each balance transaction row represents an individual
[balance_transaction](https://docs.stripe.com/api#balance_transaction_object)
object that doesn’t change after it’s created. For example, creating a charge
also creates a corresponding balance transaction of type `charge`. Refunding
this charge creates a separate balance transaction of type `refund`—but it
doesn’t modify the original balance transaction. Similarly, receiving a payout
in your bank account (represented as a transfer) creates a balance transaction.

The following example query uses this table to retrieve some information about
the five most recent balance transactions.

```
select
 date_format(created, '%m-%d-%Y') as day,
 id,
 amount,
 currency,
 source_id,
 type
from balance_transactions
order by day desc
limit 5
```

dayidamountcurrencysource_idtype3/9/2025txn_nGFTGdnLhOwxVNp-1,000usdre_rIQeSzIlxFQqIdorefund3/9/2025txn_LjU2wPLuC5XdCQW1,000usdch_vYzuShCq1Lws7ipcharge3/9/2025txn_WGz3wQibqnsAO4F1,000usdch_dEWj6boZM6GfGbIcharge3/9/2025txn_P8j42okLTIIY8Ma1,000eurch_06g0DRfHlguDOLycharge3/9/2025txn_hEbLuJZAewMLfpS-1,000usdre_UJlGBrqRt60Jubhrefund
You can calculate the most common financial summaries by joining the
`balance_transactions` table with other tables containing the appropriate
information. Some of our query templates (such as the [daily
balance](https://dashboard.stripe.com/sigma/queries/templates/Daily%20balance)
and [monthly summary and
balance](https://dashboard.stripe.com/sigma/queries/templates/Monthly%20summary%20and%20balance))
work by joining this table to others.

!

## Balance transaction fee details

The `balance_transaction_fee_details` table provides fee information about each
individual balance transaction. Joining this table to `balance_transactions` in
the manner below allows you to return fee information for each balance
transaction.

!

The following query joins the `balance_transactions` and
`balance_transaction_fee_details` tables together. Each balance transaction item
returned includes the amount, fee, type of fee applied, and a description of the
fee.

```
select
date_format(date_trunc('day', balance_transactions.created), '%m-%d-%Y') as day,
 balance_transactions.id,
 balance_transactions.amount,
 balance_transactions.fee,
 balance_transaction_fee_details.type
from balance_transactions
inner join balance_transaction_fee_details
on
balance_transaction_fee_details.balance_transaction_id=balance_transactions.id
order by day desc
limit 5
```

dayidamountfeetype3/9/2025txn_Vm07hI7eYdFf3xH1,00059stripe_fee3/9/2025txn_0IPMQng37XykZQ41,00059stripe_fee3/9/2025txn_jTaWzjALykg6d081,00059stripe_fee3/9/2025txn_dvrSvTQyviMIYs71,00059stripe_fee3/9/2025txn_exphJrQYyR39nq11,00059stripe_fee
## Charges

The `charges` table contains data about
[Charge](https://docs.stripe.com/api#charge_object) objects. Use this table for
queries that focus on charge-specific information rather than for accounting or
reconciliatory purposes. It also supplements accounting reports with additional
customer data. For example, the [payment card
breakdown](https://dashboard.stripe.com/sigma/queries/templates/Payment%20card%20breakdown)
template query uses the `charges` table to report on the different types of
cards your customers have used.

You can join the `charges` table to a number of others to retrieve more
information with your queries.

!

The following example uses the `charges` table to report on failed charges,
returning the card brand and a failure code and message.

```
select
 date_format(date_trunc('day', created), '%m-%d-%Y') as day,
 id,
 card_brand,
 failure_code,
 failure_message
from charges
 where status = 'failed'
order by day desc
limit 5
```

day
idcard_brandfailure_codefailure_message3/9/2025ch_gInkfMQ5QIyML6SVisacard_declinedYour
card was declined.3/9/2025ch_oucQO3o1vUMniKjMasterCardcard_declinedYour card
doesn’t support this type of
purchase.3/9/2025ch_xc36YCPjmE2v6UkVisacard_declinedYour card has insufficient
funds.3/9/2025ch_eOJPhP8K583EZvFVisacard_declinedYour card was
declined.3/9/2025ch_wbaJWY6qJFFuyKuMasterCardcard_declinedYour card was
declined.
## Customers

The `customers` table contains data about
[Customer](https://docs.stripe.com/api#customers) objects (this table isn’t part
of the **Payment Tables** group). Use it if you’re creating charges using
customers (for example, with saved payment information). It’s also useful if
you’re using
[subscriptions](https://docs.stripe.com/stripe-data/query-billing-data).

!

The following example retrieves a list of failed charges, with the ID and email
address for each customer.

```
select
 date_format(date_trunc('day', charges.created), '%m-%d-%Y') as day,
 customers.id,
 customers.email,
 charges.id
from charges
inner join customers
on customers.id=charges.customer_id
where charges.status = 'failed'
order by day desc
limit 5
```

## Refunds

Charges and refunds are separate objects within the API. Refunding a charge
creates a [Refund](https://docs.stripe.com/api#refund_object). This data is
available in the `refunds` table and provides in-depth information about
completed refunds. Similar to reporting on charges, a best practice is to start
with information about balance transactions. If necessary, you can then gather
additional details using the `refunds` table.

You can join the `refunds` table to the `balance_transactions` and `charges`
tables to further explore refund data.

!

The following example joins the `balance_transactions` and `refunds` tables
together using the `refunds.balance_transaction_id` and
`balance_transactions.id` columns. Each balance transaction item returned is a
refund, displaying the charge ID and amount. Only balance transactions created
after a certain date are returned.

```
select
date_format(date_trunc('day', balance_transactions.created), '%m-%d-%Y') as day,
 balance_transactions.source_id,
 refunds.charge_id,
 balance_transactions.amount
from balance_transactions
inner join refunds
on refunds.balance_transaction_id=balance_transactions.id
 where balance_transactions.type = 'refund'
order by day desc
limit 5
```

daysource_idcharge_idamount3/9/2025re_yoSxBGarxBgxoVJch_5rMNkNWSJkIbWCQ-1,0003/9/2025re_QoS8LoHKuCs3CAech_qLztRLbgcTJq7CR-1,0003/9/2025re_Lk5fVsYshc4Is6gch_HkXnZuTQWkPFHCr-1,0003/9/2025re_XYENhbCOkX0UzyKch_AAA9NRQuQXggQ4a-1,0003/9/2025re_gFsukbxzoxMuJ7gch_dIRSJDkXDxRKXVD-1,000
## Partial capture refunds

Using [auth and capture](https://docs.stripe.com/charges/placing-a-hold) and
capturing only some of the authorized amount creates both a charge and a refund.
An authorized charge creates a `charge` and an associated balance transaction
for the full amount. After a partial capture is complete, the uncaptured amount
is released and a `refund` is created with a `reason` field of `partial_capture`
along with an associated balance transaction.

For example, authorizing a 10 USD charge but only capturing 7 USD creates a
`charge` for 10 USD. This also creates a `refund` with the reason
`partial_capture` for the remaining 3 USD.

Take this into account if your business is performing auth and capture charges
as you’re creating reports to review customer refund rates. Without
consideration, auth and capture can misrepresent the number of refunds on your
account. Use the refund’s `reason` field to filter out partial capture refunds
when retrieving payment information.

```
select
 balance_transactions.id,
 balance_transactions.amount
from balance_transactions
inner join refunds
on refunds.id=balance_transactions.source_id
where reason != 'partial_capture'
limit 5
```

## Transfers and payouts

The `transfers` table contains data about
[payouts](https://docs.stripe.com/payouts) made from your Stripe balance to your
bank account. You can use this table to reconcile each payout with the specific
charges, refunds, and adjustments that comprise it, as long as you’re using
[automatic payouts](https://docs.stripe.com/payouts).

For [Connect](https://docs.stripe.com/connect) platforms, this table also
includes data about transfers of funds to connected Stripe accounts.

!

If you’re performing payouts manually, the amount in each payout to your bank
account is arbitrary. As such, you can’t reconcile it to specific balance
transactions and it only reflects the amount you requested to pay out to your
bank account.

The following example joins the `balance_transactions` and `transfers` tables
together. It returns a list of charges and refunds, the payout they relate to,
and the date that the payout is scheduled to arrive into your bank account.

```
select
date_format(date_trunc('day', balance_transactions.created), '%m-%d-%Y') as
bt_created,
 balance_transactions.source_id,
 balance_transactions.type,
 balance_transactions.net as net_amount,
 balance_transactions.automatic_transfer_id as transfer_id,
 date_format(date_trunc('day', transfers.date), '%m-%d-%Y') as transfer_date
from balance_transactions
inner join transfers
on balance_transactions.automatic_transfer_id=transfers.id
where balance_transactions.type = 'charge'
and balance_transactions.type != 'refund'
order by bt_created desc
limit 5
```

daysource_idtypenet_amounttransfer_idtransfer_date05-22-2017ch_dBtKpDrp1RuAUescharge941po_RLc0x2MGxLQDLzg05-24-201705-22-2017ch_FDJFrA3WASOPsrRcharge941po_yFSL14RSnNDsV7105-24-201705-21-2017ch_bc5On61N6sTt1h7charge941po_8cSawgdEGUL6ndY05-23-201705-21-2017ch_Si50Vfh7Gd0wMMqcharge941po_Sl82Kqt1XeE0nOa05-23-201705-21-2017ch_NNRzDtcK777eF1dcharge941po_QIMfc9Q0AO8KZhb05-23-2017
#### Caution

Payouts before 04-06-2017 have a TRANSFER_ID with a `tr_` prefix.

## Transfer reversals

You can reverse a manually created payout (or transfer to a connected Stripe
account) if it hasn’t been paid out yet by using funds returned to the available
balance in your account. These are represented as
[Transfer_reversal](https://docs.stripe.com/api#transfer_reversal_object)
objects and reside in the `transfer_reversals` table.

Transfer reversals only apply to payouts and transfers that have been created
manually—you can’t reverse automatic payouts.

## Links

- [schema](https://docs.stripe.com/stripe-data/write-queries)
- [payouts](https://docs.stripe.com/payouts)
- [type](https://docs.stripe.com/api#balance_transaction_object-type)
- [balance_transaction](https://docs.stripe.com/api#balance_transaction_object)
- [daily
balance](https://dashboard.stripe.com/sigma/queries/templates/Daily%20balance)
- [monthly summary and
balance](https://dashboard.stripe.com/sigma/queries/templates/Monthly%20summary%20and%20balance)
- [Charge](https://docs.stripe.com/api#charge_object)
- [payment card
breakdown](https://dashboard.stripe.com/sigma/queries/templates/Payment%20card%20breakdown)
- [Customer](https://docs.stripe.com/api#customers)
- [subscriptions](https://docs.stripe.com/stripe-data/query-billing-data)
- [Refund](https://docs.stripe.com/api#refund_object)
- [auth and capture](https://docs.stripe.com/charges/placing-a-hold)
- [Connect](https://docs.stripe.com/connect)
- [Transfer_reversal](https://docs.stripe.com/api#transfer_reversal_object)