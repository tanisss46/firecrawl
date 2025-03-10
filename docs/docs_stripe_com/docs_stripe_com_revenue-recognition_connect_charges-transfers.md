# Revenue Recognition for separate charges and transfersPrivate preview

## Learn how Revenue Recognition works with separate charges and transfers.

With Connect, you can make charges on your platform account on behalf of
connected accounts, perform transfers separately, and retain funds in the
process.

Stripe Revenue Recognition manages separate charges on the platform account in
the same manner we handle charges and invoices. Stripe books separate transfers
as contra revenue, and transfer reversals cancel out the contra revenue. Revenue
Recognition doesn’t automatically link [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
because they might not always have a direct connection.

In this example, `amount="1000"` is set on the separate transfer.

- On January 1, you create a charge of 15 USD.
- On January 2, you create a transfer of 10 USD.
- On February 1, you create a refund of 15 USD.
- On February 2, you create a transfer reversal of 10 USD.

If you view the summary after February ends, your data might resemble the
following:

AccountJanFebRevenue+15.00Refund+15.00Transfer+10.00-10.00Cash+5.00-5.00

## Links

- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)