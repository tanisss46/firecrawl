# Stripe charges in NetSuite

## Use the connector to automatically reconcile Stripe charges and payments to NetSuite.

The Stripe Connector for NetSuite automates the reconciliation process for any
charges or payments processed by Stripe. The connector represents these charges
or payments in NetSuite based on how they’re created.

In NetSuite, a charge always represents the payment amount, not the amount
that’s deposited to your bank account. The charge is in the currency of the
customer’s payment method, and doesn’t include any Stripe fees. Fees and
currency conversion appear on the deposit record, because charges in NetSuite
are often applied against a NetSuite invoice. This ensures that the payment
eliminates the accounts receivable balance created by the NetSuite invoice.

## How it works

When you use the connector, the automated reconciliation process occurs as
follows:

- A Stripe payment initiates through your back-end system or the Dashboard.
- The connector creates a payment in NetSuite and, if applicable, applies it to
a NetSuite invoice.
- After 2 days, the connector creates a deposit for the payment and moves it to
the correct general ledger account.

Stripe

Connector

NetSuite

GL account

Stripe initiates a payment

The connector creates a payment in NetSuite and applies it to a NetSuite invoice

The connector creates a deposit for the payment and moves it to a general ledger
account

A high level overview of the reconciliation process for charges or payments
## Charges for invoices

If you use [Stripe Billing](https://docs.stripe.com/billing), invoices
automatically generate at the end of each billing period. The connector syncs
that invoice to NetSuite, and then creates a payment that it applies to the
invoice. If you enabled revenue recognition, the connector syncs the start and
end dates of the subscription to NetSuite.

## Charges without an invoice

All charges that initiate from [Stripe Billing
subscriptions](https://docs.stripe.com/subscriptions) have an associated
invoice. If needed, you can also create a single charge that’s associated with a
customer instead of an invoice. For example, you can use this method if your
support representative needs to charge a customer an additional one-off fee.

## Charges for Stripe customers

The connector syncs charges to NetSuite as a `CustomerPayment` under the
customer associated with the charge. If specified, the connector adds the
charge’s `description` attribute to the `CustomerPayment` memo.

### Charges and accounts receivable

The connector creates transaction records in NetSuite for charges applied to an
invoice. These transaction records debit the accounts receivable account.

If a charge isn’t applied to a Stripe invoice or created through the [invoice
payment page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page),
the following happens:

- The connector won’t create the NetSuite transaction record nor debit accounts
receivable.
- The payment creates credits to accounts receivable, without a corresponding
debit.

For charges without an invoice, you need to manually debit the accounts
receivable account by creating a journal entry or creating a NetSuite invoice
for the customer.

### Asynchronous payments

Stripe supports [asynchronous
capture](https://docs.stripe.com/payments/payment-intents/asynchronous-capture)
of certain payment methods (for example, [ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit). These payment methods
don’t provide immediate notification of a successful or failed payment.

Payment statusNetSuite actionPendingThe connector syncs the payment immediately
into NetSuite. This ensures that payment applications in NetSuite remain on
schedule and don’t impact other automated NetSuite workflows.FailedThe connector
creates a customer refund and applies it to the original charge. If applied to a
NetSuite invoice, the connector unapplies the payment. The invoice status
changes from `Paid in full` to `Open`, and the reason for payment failure gets
added to the customer refund.
Balance transactions represent actual money movement and determine at which
point you can account for them in an accounting system like NetSuite. When a
payment has a balance transaction ID (for example, `txn_123`), the connector can
create the payment in NetSuite. The balance transaction ID can post to the
payment hours after it’s created, and is confirmation from the bank that the
payment is valid. The actual funds for asynchronous payments won’t transfer
immediately.

If a payment fails and doesn’t generate a balance transaction ID, the connector
takes no action in NetSuite. There’s no confirmation of money movement, so the
connector can’t close the payment with a refund or credit memo.

## Charges without Stripe customers

You can create a charge without providing additional information about the
charge. For example, if you create a charge without creating a customer first,
the charge won’t associate with a customer. The connector then syncs the charge
to NetSuite as a customer payment under the `Stripe Unallocated Charges` global
customer.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)

## Links

- [Stripe Billing](https://docs.stripe.com/billing)
- [Stripe Billing subscriptions](https://docs.stripe.com/subscriptions)
- [invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [asynchronous
capture](https://docs.stripe.com/payments/payment-intents/asynchronous-capture)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)