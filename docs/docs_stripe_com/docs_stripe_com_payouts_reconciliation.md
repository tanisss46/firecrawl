# Payout reconciliation

## Know which transactions are included in a given payout.

Sending funds from your Stripe available balance to your bank account generates
a payout object. Automatic payouts occur routinely according to your [payout
schedule](https://docs.stripe.com/payouts#payout-schedule) and can include funds
from multiple transactions.

Stripe provides the following ways to review the transactions included in an
automatic payout:

- Open a payout in the [Stripe
Dashboard](https://dashboard.stripe.com/test/payouts).
- View or download the [payout reconciliation
report](https://docs.stripe.com/reports/payout-reconciliation).
- Retrieve the payout details through the Stripe API as documented in this
guide.

#### Reconciliation for manual payouts

You control the timing and amount of manual payouts, so Stripe can’t identify
which transactions are included in each payout. You’re responsible for
reconciling payouts you create against your transaction history.

[Find the Payout ID](https://docs.stripe.com/payouts/reconciliation#payout-id)
You need a payout’s `id` (`po_xxx`) to retrieve information about the payout’s
transactions. To get it:

- Listen to the `payout.reconciliation_completed` webhook event.
- Call [List Payouts](https://docs.stripe.com/api/payouts/list) to review a list
of payouts.
- Retrieve it from your own database.

You could [retrieve the Payout](https://docs.stripe.com/api/payouts/retrieve) to
access its properties, but this won’t include the individual transactions that
make up the total amount.

```
{
 "id": "po_001",
 "amount": 8000,
 "currency": "usd",
 "status": "paid",
 ...
}
```

[List
BalanceTransactions](https://docs.stripe.com/payouts/reconciliation#list-balancetransactions)
Every funds movement in or out of your Stripe account creates a
[BalanceTransaction](https://docs.stripe.com/api/balance_transactions). Pass the
payout ID in your [list
BalanceTransaction](https://docs.stripe.com/api/balance_transactions/list)
request to filter the results by only transactions associated with that payout.

```
curl -G https://api.stripe.com/v1/balance_transactions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payout=po_xxx
```

If you need more results than the default 10, set the
[limit](https://docs.stripe.com/api/balance_transactions/list#balance_transaction_list-limit)
parameter in the request or use Stripe’s
[auto-pagination](https://docs.stripe.com/api/pagination/auto).

The response returns an array of BalanceTransactions objects for the specified
payout:

```
{
 "object": "list",
 "data": [
 {
 "id": "txn_001",
 "amount": 10000,
 "type": "charge",
 "source": "ch_001",
 ...
 },
 {
 "id": "txn_002",
 "amount": -2000,
 "type": "refund",
 "source": "re_001",
 ...
 },
 ...
```

The `type` property identifies the underlying activity that generated the
transaction. for example:

- `charge`: A payment from your customer.
- `refund`: Funds you returned to your customer.
- `stripe_fee`: A Stripe fee you paid.
- `payout`: The payout itself, which is also a transaction that moved funds from
your Stripe account to your bank account.

See [balance transaction
types](https://docs.stripe.com/reports/balance-transaction-types#types) for a
complete list.

[Expand balance transaction
resources](https://docs.stripe.com/payouts/reconciliation#expand-resources)
The `source` property of each BalanceTransaction identifies the underlying
object representing the transaction type, such as `ch_xxx` for a Charge or
`re_xxx` for a Refund. To retrieve these objects without making extra API calls,
update the previous code using [expand](https://docs.stripe.com/expand).

```
curl -G https://api.stripe.com/v1/balance_transactions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payout=po_xxx \
 -d "expand[]"="data.source"
```

The response contains the expanded `source` object for each BalanceTransaction
in the payout:

```
{
 "object": "list",
 "data": [
 {
 "id": "txn_001",
 "amount": 10000,
 "type": "charge",
 "source": {
 "id": "ch_001",
 "amount": 10000,
 "metadata": { ... },
 ...
 },
 ...
 },
 {
 "id": "txn_002",
 "amount": -2000,
 "type": "refund",
 "source": {
 "id": "re_001",
 "amount": 2000,
 "reason": "requested_by_customer",
 ...
 },
 ...
```

Use the following code to access the `source` object properties such as `id` and
`amount`.

```
balance_transactions['data'].each do |txn|
 obj = txn['source']
 puts "#{obj['id']} #{obj['amount']}"
end
```

## Links

- [payout schedule](https://docs.stripe.com/payouts#payout-schedule)
- [Stripe Dashboard](https://dashboard.stripe.com/test/payouts)
- [payout reconciliation
report](https://docs.stripe.com/reports/payout-reconciliation)
- [List Payouts](https://docs.stripe.com/api/payouts/list)
- [retrieve the Payout](https://docs.stripe.com/api/payouts/retrieve)
- [BalanceTransaction](https://docs.stripe.com/api/balance_transactions)
- [list
BalanceTransaction](https://docs.stripe.com/api/balance_transactions/list)
-
[limit](https://docs.stripe.com/api/balance_transactions/list#balance_transaction_list-limit)
- [auto-pagination](https://docs.stripe.com/api/pagination/auto)
- [balance transaction
types](https://docs.stripe.com/reports/balance-transaction-types#types)
- [expand](https://docs.stripe.com/expand)