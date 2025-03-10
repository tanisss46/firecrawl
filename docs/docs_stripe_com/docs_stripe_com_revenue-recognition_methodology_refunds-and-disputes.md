# Revenue Recognition with refunds and disputes

## Understand how refunds and disputes impact your revenue.

Refunds and disputes can happen to any transaction on Stripe, which affects your
revenue numbers.

## Handling a refund or dispute

Stripe handles refunds and disputes in a similar manner, but the contra revenue
generated go to the refunds and disputes accounts respectively.

When a refund or dispute is made,

- Cash is returned to the customer.
- Prior recognized revenue is offset by contra revenue in the refund or dispute
account.
- Deferred revenue that hasn’t been recognized is cleared.

This next example is a one-time payment refund.

- On January 1, a customer made a one-time payment for 90 USD.
- On February 1, the transaction was refunded.

In this situation, the full amount of 90 USD is recognized as revenue, and
subsequently the full amount of 90 USD is added to the refunds contra revenue
account.

AccountJanFebRevenue+90.00Refunds+90.00
In this example, the [invoice](https://docs.stripe.com/api/invoices) for a
subscription was disputed.

- On January 1, a customer starts a three month subscription for 90 USD, which
generates and finalizes an invoice.
- The customer pays 90 USD.
- On February 1, the customer disputes the transaction.

In this case, the customer received 31 days worth of service, so 31 USD is
placed in the disputes account. The dispute also reduces the cash by 90 USD, and
the remaining 59 USD of deferred revenue is cleared. At the end of February, the
account balances looks like the following:

AccountJanFebRevenue+31.00DeferredRevenue+59.00-59.00Cash+90.00-90.00Disputes+31.00
## Winning a dispute

Disputes are different from refunds in one way—you can win disputes.

When you win a dispute,

- Cash is returned to you.
- Recognized and deferred revenue don’t change.
- Cash is offset by an increase in the recoverables account.

In the previous example, assume that you win the dispute on March 1. If you then
looked at the account balances at the end of March, you’d see that cash
increased by 90 USD, which is offset by recoverables.

AccountJanFebMarRevenue+31.00DeferredRevenue+59.00-59.00Cash+90.00-90.00+90.00Disputes+31.00Recoverables+90.00

## Links

- [invoice](https://docs.stripe.com/api/invoices)