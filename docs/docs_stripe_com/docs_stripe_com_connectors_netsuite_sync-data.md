# Sync Stripe data to NetSuite

## Learn how the connector syncs Stripe data to NetSuite.

Use the Stripe Connector for NetSuite to sync your data from Stripe to NetSuite.
The table below describes how the connector handles these [webhook
events](https://docs.stripe.com/webhooks).

Webhook eventNetSuite
actionaccount.updatedNoneaccount.application.deauthorizedNoneaccount.external_account.createdNoneaccount.external_account.deletedNoneaccount.external_account.updatedNoneapplication_fee.createdNoneapplication_fee.refundedNoneapplication_fee.refund.updatedNonebalance.availableNonecharge.capturedThe
connector creates a `CustomerPayment`. For charges associated with a Stripe
invoice, the connector also creates a NetSuite invoice. If one doesn’t exist,
the connector creates a `Customer`.charge.failedNone. The connector only syncs
successful payments.charge.refundedFor charges associated with a Stripe invoice,
the connector creates a `CreditMemo` for the invoice and a `CustomerRefund` for
the credit memo. For charges that aren’t associated with a Stripe invoice, the
connector creates a `CustomerRefund` for the
`CustomerPayment`.charge.succeededThe connector creates a `CustomerPayment`. For
charges associated with a Stripe invoice, the connector also creates a NetSuite
invoice. If one doesn’t exist, the connector creates a
`Customer`.charge.updatedThe connector creates a `CustomerPayment`. For charges
associated with a Stripe invoice, the connector also creates a NetSuite invoice.
If one doesn’t exist, the connector creates a
`Customer`.charge.dispute.closedNone. Disputed funds appear as a line item on
the payout they’re included in.charge.dispute.createdFor disputes associated
with a Stripe invoice, the connector creates a `CreditMemo` for the invoice and
a `CustomerRefund` for the credit memo. For disputes that aren’t associated with
a Stripe invoice, the connector creates a `CustomerRefund` for the
`CustomerPayment`.charge.dispute.funds_reinstatedNone. Reinstated funds appear
as a line item on the payout they’re included
in.charge.dispute.funds_withdrawnFor disputes associated with a Stripe invoice,
the connector creates a `CreditMemo` for the invoice and a `CustomerRefund` for
the credit memo. For disputes that aren’t associated with a Stripe invoice, the
connector creates a `CustomerRefund` for the
`CustomerPayment`.charge.dispute.updatedThe connector follows the logic for
`charge.dispute.created` or `charge.dispute.funds_reinstated`, depending on the
updates.coupon.createdNone. The connector only syncs coupons associated with an
invoice and represents them as a NetSuite `DiscountItem`.coupon.deletedNone. The
connector doesn’t mark records as inactive nor delete any records in your
NetSuite instance.coupon.updatedNone. The connector only syncs coupons
associated with an invoice and represents them as a NetSuite `DiscountItem`.
customer.created

The connector does one of the following, depending on your settings:

- Creates a `Customer` in NetSuite
- Does nothing, if you enabled the global customer workflow setting
- Associates the customer with an existing NetSuite customer ID, if you enabled
customer matching or created the customer with the `netsuite_customer_id`
metadata key
customer.deletedNone. The connector doesn’t mark records as inactive nor delete
any records in your NetSuite
instance.customer.updatedNonecustomer.discount.createdNonecustomer.discount.deletedNonecustomer.discount.updatedNonecustomer.source.createdNone.
The connector doesn’t represent customer payment sources in
NetSuite.customer.source.deletedNonecustomer.source.updatedNonecustomer.subscription.createdNone.
The connector doesn’t represent customer subscriptions in NetSuite. Instead, it
syncs invoices created by customer
subscriptions.customer.subscription.deletedNonecustomer.subscription.trial_will_endNonecustomer.subscription.updatedNoneinvoice.createdNone.
The connector only syncs finalized invoices.invoice.payment_succeededThe
connector creates the customer and invoice in NetSuite, and represents each
Stripe `InvoiceItem` as a `ServiceSaleItem`. The connector applies a
`CustomerPayment` to the created NetSuite invoice.invoice.payment_failedThe
connector creates the customer and invoice in NetSuite. The invoice remains open
until it’s paid.invoice.updatedThe connector checks the invoice for updates that
might affect the general ledger and updates NetSuite as
needed.invoice.item.createdNoneinvoice.item.deletedNoneinvoice.item.updatedNone
price.created

The connector does one of the following, depending on your settings:

- Creates a `ServiceSaleItem` in NetSuite
- Does nothing, if you enabled the global price workflow setting
- Associates the price with an existing NetSuite item ID, if you enabled price
matching or created the price with one of the following metadata keys:

- `netsuite_service_sale_item_id`
- `netsuite_service_resale_item_id`
- `netsuite_non_inventory_sale_item_id`
- `netsuite_non_inventory_resale_item_id`
price.deletedNone. The connector doesn’t modify the item status to prevent
creating issues with the business logic in your
account.price.updatedNoneproduct.createdNone. The connector doesn’t sync
products, only their child prices.product.updatedNonepayout.createdThe connector
validates the payout’s underlying transactions, but doesn’t sync the payout.
This includes connect payouts.payout.failedNone. The connector ignores failed
payouts.payout.paidThe connector validates the payout’s underlying transactions,
and creates deposits for successful payouts.payout.reversedNonepayout.updatedThe
connector syncs the payout, if it hasn’t already synced successfully.

## Links

- [webhook events](https://docs.stripe.com/webhooks)