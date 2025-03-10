# Stripe refunds in NetSuite

## Use the connector to automatically reconcile Stripe refunds to NetSuite bank deposits.

The Stripe Connector for NetSuite automates the refund reconciliation process
(for example, for subscriptions, credit notes, revenue recognition, and so on).
The connector syncs refunds from Stripe into NetSuite and represents the refunds
based on the payment status (applied, partially applied, not applied, and so
on).

## How it works

When you use the connector, the automated refund reconciliation process occurs
as follows:

- Stripe issues a refund through the Stripe API or Dashboard.
- The connector evaluates whether or not the charge applies to a transaction. If
not, the connector creates a customer refund directly against the customer
payment.
- If the charge applies to a transaction, the connector evaluates whether or not
the charge applies to an invoice. If not, the charge is a cash sale, which the
connector doesn’t support.
- If the charge applies to an invoice, the connector creates a credit memo and
customer refund to represent the refund.

## Refunds for charges applied to an invoice

The connector creates a credit memo and customer refund and applies the credit
memo to the customer refund for any charge applied to an invoice that’s
refunded. This happens so that entries are made to income and cash accounts.

If a payment applies to an invoice that differs from the invoice it was
originally applied to, the connector uses the new invoice to create a credit
memo.

If you remove a payment from an invoice and refund the amount, the connector
detects this action and won’t create a credit memo. Instead, the refund applies
directly to the unapplied payment.

## Refunds for charges without an invoice

The connector won’t create a credit memo if you create a refund for a charge
that isn’t associated with an invoice. Instead, the refund applies directly to
the unapplied payment.

## Refunds caused by failed asynchronous payments

Payment methods with delayed notification, such as [ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit), can take days to
receive acknowledgement of success or failure. The connector applies these
payments immediately and considers them successful until proven failed.

If a payment fails, the connector:

- Unapplies the payment that previously showed as pending from the invoice.
- Refunds the failed payment in NetSuite. To reverse the impact of the original
failed payment on the general ledger, the connector creates a refund and applies
it to the payment.

The refund in NetSuite shows a message with details from Stripe about why the
original payment failed.

## Refunds on transactions prior to the record sync start date

If you have data from the past that you want to sync to NetSuite, ask your
implementation partner to set a record sync start date on your account. Make
sure the record sync start date includes the transactions (payments, refunds,
chargebacks, invoices, and payouts) that you want to import into NetSuite.

If you need to issue a refund for a transaction created before the record sync
start date, you must do so manually:

- Create the refund in Stripe.
- Manually create the refund in NetSuite by creating a credit memo and a
customer refund.
- The connector automatically skips the refund during the reconciliation
process. You’ll need to manually reconcile this refund to the bank deposit.

Alternatively, you can create the refund in Stripe and then allow the connector
to create an entry on the deposit (payout) to an income account to represent the
refund. This method posts the refund to a single income account instead of
controlling the revenue account used. The entry isn’t connected to the original
invoice and the connector doesn’t create a credit memo or customer refund
record.

To have refunds summarized on the deposit, ask your implementation partner to
enable the `Summarize transactions before backfill` feature in your Stripe app
settings. Consult with your implementation partner to understand all accounting
and technical implications.

## Refunds and deposit automation

The connector uses the `CustomerRefund` record to post refunds to an
`Undeposited Funds` account in your NetSuite instance. After Stripe includes the
refund in a payout, the connector links the refund to a NetSuite deposit and the
refund moves from the `Undeposited Funds` account to the cash account.

## Stripe fee refunds

Refunds for Stripe fees aren’t represented on the `CustomerRefund` or
`CreditMemo` records. The connector records these fees as line items on the
NetSuite deposit in the `Other Deposits` list. Learn more about how the
connector handles different [types of
fees](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite#fee-types).

## Partial refunds

The connector supports partial refunds and handles invoices based on the number
of items:

- If the invoice contains a single item, the connector creates a credit memo
using the single line item on the original invoice, and the refund amount.
- If the invoice contains multiple items, the connector can’t determine which
line items to refund. Because Stripe doesn’t associate a refund with specific
line items, the connector represents the refund with a non-inventory sale item
called a `Stripe Partial Refund Item`. If you enabled revenue recognition on
your account, the item uses the schedule and deferred revenue account specified
in your settings.

## Customize the refund general ledger impact

When creating a credit memo for a refund, the connector includes the original
items on the invoice, by default.

You can’t specify a refund account for an item in NetSuite. When you issue the
credit memo with the original items on an invoice, the contra-income entries
(reversal of the revenue) apply to the same account as the original items.

If you don’t want to use the same income account, you can delete the original
items on the credit memo. If configured, the connector automatically creates
credit memos with a unique global item (the `Stripe Refund Item`) instead of the
original items on the invoice.

Use this approach if you want the refund to post to a specific account, or you
sell physical products and don’t want the refund’s credit memo to affect
inventory levels.

The `Stripe Refund Item` posts to your default income account. You can customize
where to post refund items and credit memos. To do so, edit the account of the
item in NetSuite. You can also edit the name or any other aspect of the item,
and the connector won’t override those modifications.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Stripe payouts in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)

## Links

- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [types of
fees](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite#fee-types)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Stripe payouts in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)