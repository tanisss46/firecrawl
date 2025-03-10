# Payouts

## Settle with your sellers.

The amount and frequency of each [payout](https://docs.stripe.com/payouts) to
your sellers is controlled by Mirakl based on your settings.

You can customize your billing cycles under **Settings** > **Shops** > **Billing
Cycles**. By default, your sellers receive their payouts on the 1st, 11th, and
21st of each month.

## Seller settlement

The workflow starts when Mirakl generates a new
[invoice](https://docs.stripe.com/api/invoices).

- The [payout job](https://docs.stripe.com/connectors/mirakl/reference#payout)
fetches newly created Mirakl invoices.
- The connector performs the following actions based on the invoice attributes:
Invoice attributeAction takentotal_other_credits_incl_taxTransfer from the
operator to the seller.total_other_invoices_incl_taxTransfer from the seller to
the operator.total_subscription_incl_taxTransfer from the seller to the
operator.amount_transferredPayout to the Seller.
#### Note

Commissions are already handled during the [payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split).

!

## See also

- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps).

## Links

- [payout](https://docs.stripe.com/payouts)
- [invoice](https://docs.stripe.com/api/invoices)
- [payout job](https://docs.stripe.com/connectors/mirakl/reference#payout)
- [payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split)
- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps)