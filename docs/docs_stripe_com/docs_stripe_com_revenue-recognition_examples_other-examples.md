# Other examples

## Learn about revenue recognition with other examples.

Unless stated otherwise, these examples assume that revenue recognition takes
place on a per-day basis.

## External asset

When you manually mark invoices as paid outside of Stripe, the external asset
account increases. All other accounts operate as if the invoice is paid, but the
cash account doesn’t change. You can import third party transaction data and
consolidate all your revenue sources into your Stripe reporting by using the
[Data Import feature](https://docs.stripe.com/revenue-recognition/data-import).

This example involving the external asset account uses the following
assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a monthly subscription that
costs 31 USD.
- The subscription generates an invoice, and the invoice finalizes on the same
day.
- The invoice is manually marked as paid outside of Stripe on February 5.
AccountJanFebAccountsReceivable+31.00-31.00Revenue+31.00CashExternalAsset+31.00
## Fees

[Stripe fees](https://stripe.com/en-ca/pricing) are booked against the Fees
account on a cash basis.

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes and the customer pays 90 USD.
- This payment has a Stripe processing fee of 0.02 USD.

If you view the summary after March ends, you’ll see something like this:

AccountJanFebMarRevenue+31.00+28.00+31.00DeferredRevenue+59.00-28.00-31.00Cash+89.98Fees+0.02

## Links

- [Data Import feature](https://docs.stripe.com/revenue-recognition/data-import)
- [Stripe fees](https://stripe.com/en-ca/pricing)