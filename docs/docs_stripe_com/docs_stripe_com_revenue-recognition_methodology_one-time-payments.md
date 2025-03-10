# Revenue Recognition with one-time payments

## Manage revenue recognition for one-time payments by importing custom service periods.

With one-time payments created in the Dashboard or through the Charges or
Payment Intents APIs, Stripe has data on the transaction amount and payment
time, but no explicit service period data. By default, Stripe Revenue
Recognition immediately recognizes the revenue from one-time payments, but you
can override this behavior by
[importing](https://docs.stripe.com/revenue-recognition/data-import) a custom
service period.

This example is for a one time payment of 10 USD.

The journal entries generated might look like the following:

DebitCreditAmountAccountsReceivablesDeferredRevenue+10.00CashAccountsReceivables+10.00DeferredRevenueRevenue+10.00
This nets out to leave the following end state:

AccountAmountCash+10.00Revenue+10.00
#### Caution

To incorporate a fulfillment schedule into your Revenue Recognition reports, you
must first [import the
data](https://docs.stripe.com/revenue-recognition/data-import).

## Links

- [importing](https://docs.stripe.com/revenue-recognition/data-import)