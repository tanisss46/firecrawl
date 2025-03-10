# Instant Payouts with advance funding

## Let Instant Payouts access pending balances with trackable balance activities.

Instant payout users benefit from quick access to their pending balances. To use
these funds safely, explicit actions like advance funding are necessary for
accurate bookkeeping when fund availability changes.

## How Instant Payouts with advance funding works

Stripe enables Instant Payouts users to access pending balances through the
`advance` and `advance_funding`
[type](https://docs.stripe.com/reports/balance-transaction-types) balance
transactions. When you create an instant payout that exceeds your available
balance, funds are added to your available balance and subtracted from your
pending balance to cover the difference.

### Granular advance funding

To align advance funding with the original availability of payments, Stripe
creates multiple `advance_funding`
[type](https://docs.stripe.com/reports/balance-transaction-types) balance
transactions when it pulls funds from multiple days’ worth of payments balances.

For example, if you have the following:

- 0 USD in your available balance today
- 25 USD available on tomorrow (T+1)
- 15 USD available on the day after (T+2)

When you request a 40 USD instant payout, you’ll see two separate
`advance_funding`
[type](https://docs.stripe.com/reports/balance-transaction-types) balance
transactions:

- One that deducts 25 USD from your T+1 balance
- One that deducts 15 USD from your T+2 balance
- And one `advance`
[type](https://docs.stripe.com/reports/balance-transaction-types) balance
transaction that credits 40 USD to your available balance

### Reversal of failed or canceled Instant Payouts

When an instant payout fails or gets canceled, the corresponding `advance` and
`advance_funding`
[type](https://docs.stripe.com/reports/balance-transaction-types) balance
transactions are reversed by offsetting balance transactions. In the example
above, if the 40 USD instant payout fails, we:

- Credits 25 USD to your T+1 balance
- Credits 15 USD to your T+2 balance
- Deducts 40 USD from your available balance

### Negative available balance recovery

When your available balance is negative, advance funding does not restore it.
Instead, it only provides funding for the requested instant payout amount,
leaving your negative available balance unchanged. We’ll choose the right bucket
of pending balances to allow your negative available balance to phase out
gradually. This funding is drawn from future days where the cumulative balance
is positive. For example:

- -25 USD in your available balance today (available balance)
- 20 USD available tomorrow (T+1)
- 30 USD available the day after (T+2)

In this scenario, the cumulative balance on T+1 is -5 USD, while T+2 shows a
cumulative balance of 25 USD. If you request a 10 USD instant payout, we:

- Deduct 10 USD from your T+2 balance
- Credit 10 USD to your available balances for the Instant Payouts

This method retains more recent pending balances, aiding recovery from a
negative balance. The cumulative balance recovers on T+2.

## Filter balance transactions by source

Use the `source` field to find the `advance` and `advance_funding`
[type](https://docs.stripe.com/reports/balance-transaction-types) balance
transactions for the Instant Payout. You can access the `source` field in the
Dashboard when you filter transactions or through the [Balance Transactions
API](https://docs.stripe.com/api/balance_transactions).

DashboardAPI- Go to the **Balances > All activity** page.
- Click the **Export** button and select a time range.
- Open the downloaded balance history CSV file.
- Locate the **source** column in the export file.
- The related `advance` and `advance_funding` balance transactions will have a
`source` field that matches the instant payout token.

## Links

- [type](https://docs.stripe.com/reports/balance-transaction-types)
- [Balance Transactions API](https://docs.stripe.com/api/balance_transactions)