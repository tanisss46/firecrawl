# Reporting and reconciliation

## Use Stripe to generate financial reports and perform reconciliation.

Learn about the different payout types, balance transactions, and the advanced
reporting features within the Sigma platform.

## Reporting and payouts

To simplify reporting and reconciliation, use automatic
[payouts](https://docs.stripe.com/payouts), because they maintain the
association between each transaction and the payout they’re included in.

If you’re building custom reporting using the APIs, use the [balance transaction
endpoint](https://docs.stripe.com/api/balance_transactions/list) and the
`payout` parameter to list all transactions included in an automatic payout. A
best practice is to retrieve payouts automatically and asynchronously when the
[payout.paid](https://docs.stripe.com/api#event_types-payout.paid) or
[payout.reconciliation_completed](https://docs.stripe.com/api/events/types#event_types-payout.reconciliation_completed)
event is received by your [webhook](https://docs.stripe.com/connect/webhooks)
handler.

The number of balance transactions can exceed the maximum limit. In that case,
we recommend using the [auto pagination
feature](https://docs.stripe.com/api/pagination/auto) to fetch the list of all
balance transactions without having to manually paginate results and perform
subsequent requests.

Here’s an example balance history API call to retrieve transactions from a
payout:

```
curl -G https://api.stripe.com/v1/balance_transactions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payout={{PAYOUT_ID}} \
 -d limit=100
```

Stripe

Server

`payout.paid` or `payout.reconciliation_completed` event

payout.paid
`GET /v1/balance_transactions`

Returns list of transactions

An example balance history API call to retrieve transactions from a payout
Automatic payouts supports [Instant
Payouts](https://docs.stripe.com/payouts#instant-payouts) that instantly send
funds to a supported debit card. You can request Instant Payouts 24/7, including
weekends and holidays, and funds typically appear in the associated bank account
within 30 minutes. See the [Instant Payout
documentation](https://docs.stripe.com/payouts/instant-payouts-banks) to see if
it is available in your region.

### Manual payouts

You can use [manual
payouts](https://docs.stripe.com/connect/payouts-connected-accounts) if desired.
However, Stripe does not support transaction-level reporting for the funds that
comprise your manual payouts because you specify the amount you want to get paid
out.

Here’s an example manual payout on your account:

```
curl https://api.stripe.com/v1/payouts \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST" \
 -d "amount"=1000 \
 -d "currency"="usd"
```

## Financial Reports

Stripe supports many out-of-the-box
[reports](https://docs.stripe.com/stripe-reports) for financial analysis:

- [Balance](https://docs.stripe.com/reports/balance): You can view and download
summarized and itemized balance transaction data, helping you to close books on
a daily, weekly, or monthly basis. These reports help you understand changes to
your Stripe balance.
- [Reconciliation](https://docs.stripe.com/reports/payout-reconciliation): You
can see which transactions have already been paid out and which ones are yet to
be paid out using this report. The Reconciliation tab displays the same type of
data you see in the Balance tab but grouped in different ways to help you
reconcile payouts.

All reports are available in the Stripe Dashboard, and with the API. You can
programmatically request and download any of Stripe’s prebuilt reports using the
[Reporting API](https://docs.stripe.com/reports/api).

To fully automate this process, follow our [four-step integration
pattern](https://docs.stripe.com/reports/api#integration-pattern), which
includes listening for events that tell you when new reporting data becomes
available and running your reports at that time.

Here’s an example API call to generate a “Itemized payout reconciliation report
for a single payout” (aka “Settlement file”). Make this API call after you’ve
been notified that new data is available:

```
curl https://api.stripe.com/v1/reporting/report_runs \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST" \
 -d "report_type"="payout_reconciliation.by_id.itemized.4" \
 -d "parameters[interval_start]"=1577865600 \
 -d "parameters[interval_end]"=1580544000
```

## Balance transactions

[Balance
transactions](https://docs.stripe.com/reports/balance-transaction-types) are the
building blocks of all activity on Stripe. These objects:

- Represent everything that affected your Stripe balance (credits and debits).
- Are automatically created by Stripe (for example, each successful
PaymentIntent generates a separate BalanceTransaction object, as does each
payout).
- Are immutable (a refund is associated with a new BalanceTransaction negating
the original).
- Can act as your ledger (to understand your balance at any point in time, you
can replay all BalanceTransactions up to that point).

BalanceTransactions (`txn_***` objects) are also the basis of all of our
reporting—in most reports, the line-level data point is a `txn_***` object.

## Advanced reporting with Sigma

[Sigma](https://docs.stripe.com/stripe-data) makes all of your business data
available in an interactive SQL environment in the Dashboard. You can write
queries that leverage its extensive schema, allowing you to create fully
customized reports using information about your transactions.

With Sigma, you have the ability to export data directly to CSV, and schedule
queries to deliver results by email or
[webhook](https://docs.stripe.com/webhooks). You can generate datasets for your
business intelligence tools, reconcile transactional data, and generate custom
reports.

To [activate Sigma](https://dashboard.stripe.com/test/get-started/sigma),
navigate to **Settings > Sigma** from the Dashboard. After you activate it, data
takes up to 24 hours to load and be queryable. Sigma uses standard ANSI SQL and
a broad range of reporting functions. Anyone on your account with permission to
view reports can write and run queries.

## Links

- [payouts](https://docs.stripe.com/payouts)
- [balance transaction
endpoint](https://docs.stripe.com/api/balance_transactions/list)
- [payout.paid](https://docs.stripe.com/api#event_types-payout.paid)
-
[payout.reconciliation_completed](https://docs.stripe.com/api/events/types#event_types-payout.reconciliation_completed)
- [webhook](https://docs.stripe.com/connect/webhooks)
- [auto pagination feature](https://docs.stripe.com/api/pagination/auto)
- [Instant Payouts](https://docs.stripe.com/payouts#instant-payouts)
- [Instant Payout
documentation](https://docs.stripe.com/payouts/instant-payouts-banks)
- [manual payouts](https://docs.stripe.com/connect/payouts-connected-accounts)
- [reports](https://docs.stripe.com/stripe-reports)
- [Balance](https://docs.stripe.com/reports/balance)
- [Reconciliation](https://docs.stripe.com/reports/payout-reconciliation)
- [Reporting API](https://docs.stripe.com/reports/api)
- [four-step integration
pattern](https://docs.stripe.com/reports/api#integration-pattern)
- [Balance
transactions](https://docs.stripe.com/reports/balance-transaction-types)
- [Sigma](https://docs.stripe.com/stripe-data)
- [webhook](https://docs.stripe.com/webhooks)
- [activate Sigma](https://dashboard.stripe.com/test/get-started/sigma)