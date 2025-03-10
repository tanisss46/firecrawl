# Stripe credit notes and NetSuite credit memos

## Learn how the Stripe Connector for NetSuite creates credit memos in NetSuite for Stripe credit notes.

The Stripe Connector for NetSuite supports credit note automation to handle
out-of-band payments, refunds, discounts, revenue recognition, and to decrease
invoice amounts. The automation process also allows coupons, taxes, and custom
information on the credit memo in NetSuite. You can learn more about how to
issue credit notes in the
[Dashboard](https://docs.stripe.com/invoicing/dashboard/credit-notes) or using
the
[API](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes).

## Credit notes for open invoices

After you finalize a Stripe invoice, you can’t [edit the amount
due](https://docs.stripe.com/invoicing/invoice-edits). If you need to change the
amount after invoice finalization, you can use a credit note. [Credit
notes](https://docs.stripe.com/invoicing/dashboard/credit-notes) are documents
that decrease the amount of an `open` or `paid` invoice, but don’t void or
replace the original invoice.

When you apply a credit note to an open invoice, the connector creates a credit
memo in NetSuite and applies it to the invoice after it’s paid. The final
invoice in NetSuite includes the adjusted amount due. The connector waits to
apply the credit memo to prevent an irreconcilable state (voided invoice and
credit note) in Stripe, which NetSuite doesn’t support.

## Credit notes for paid invoices

When you apply a credit note to a paid invoice, the following occurs depending
on the action. You can apply credit notes in multiple ways simultaneously, and
the connector reflects the applications in NetSuite.

ActionDescriptionNetSuite statusCreate a refundRefund the invoice payment to the
customer’s payment method.The connector creates a refund and credit memo and
applies them to the payment and invoice.Link a refundLink an existing refund for
the invoice payment.The connector creates and applies a credit memo to the
customer refund.Out-of-band creditCredit the invoice for an adjustment amount
made outside of Stripe.The connector creates a credit memo for you to manually
apply to a customer refund.Credit the customer balanceCredit the customer’s
credit balance, which automatically applies to their future invoices.The
connector creates a credit memo when the balance credit gets applied to a future
invoice.
### Out-of-band payments

Out-of-band refunds can occur if your customer pays an invoice outside of Stripe
(for example, a check or cash) and then receives a credit note. The connector
creates an unapplied credit memo in NetSuite that you can manually apply to a
customer refund. The credit memo indicates that the credit represents an
out-of-band payment. This allows you to create queries to identify and resolve
these types of credit memos.

### Customer balance credit notes

If you issue a credit note for an invoice that has a credit balance applied to
it, you might see funds credited to a customer’s credit balance instead of their
original payment method.

## Credit notes for previous transactions

If you have a history of Stripe transactions that you want to exclude from
NetSuite, your implementation partner can configure a start date for records to
sync on your account. The connector won’t sync any records before this date,
including credit notes, payments, refunds, chargebacks, invoices, or payouts.

If you need to issue a credit note for a transaction created before the record
sync start date, you can do so manually:

- Create the credit note in Stripe.
- Manually create the credit memo in NetSuite and apply it to the same
transaction, invoice, or refund.
- Manually reconcile the refund to the bank deposit. During the reconciliation
process, the connector automatically skips the refund with the attached credit
note.

Alternatively, you can post the credit notes to a single income account:

- Create the credit note in Stripe.
- The connector creates an entry on the deposit that represents the refund
attached to the credit note. This entry isn’t tied to the original invoice, and
the credit memo isn’t created.

## Credit notes and taxes

If you calculate tax and use credit notes, you must use the following connector
representation method: `Taxes as a separate line item`. Representing taxes on
every line item isn’t supported because of limitations in NetSuite that prevent
setting the tax rate on credit memo line items.

## Data synced from credit notes to credit memos

The connector syncs credit notes to NetSuite with the credit note ID, creation
date, currency, and includes any notes in the memo field. The connector uses the
NetSuite customer that’s associated with the Stripe customer to create the
credit memo. Any manual changes to the NetSuite customer can cause the credit
memo to fail.

### Invoice line items

The connector maps invoice line items as follows:

- **Product price**

- If included on a credit note line item and linked to a NetSuite item, the
connector uses that item on the credit memo.
- If the product price isn’t linked to a NetSuite item, the connector creates an
item for the price or uses the generic line item called `Stripe Unallocated
Invoice Item`.
- **Description**

- If present on the credit note line item, the connector adds it to the credit
memo line item description.
- If the description is empty, the connector uses the invoice line item
description.
- **Quantity**: The connector maps the quantity, start date, and end date for
revenue recognition calculations.
- **Amount**: The connector syncs the amount specified on the line item.
- **Discounts**: The connector syncs any discounts specified on the line item.

For UK businesses that use the gross amount in NetSuite, the connector uses that
field for the credit memo. If you don’t use the gross amount, the connector uses
the amount field.

### Custom line items

You can add a custom line to a credit note that isn’t associated with a specific
plan or item. The connector creates an item called `Stripe Custom Credit Note
Line Item` and maps the custom line to this NetSuite item. The description and
amount map to the NetSuite credit memo line. The connector can’t map metadata or
custom fields.

### No line items

You can create a credit note without line items. If the amount is less than the
original invoice total, the connector uses a global credit note item.

### Invoice line items with revenue recognition

The NetSuite revenue recognition engine can use the information contained in the
credit memo to calculate revenue recognition. If associated with an invoice line
item, the connector adds the start date and end date from the invoice to the
credit memo.

## Links

- [Dashboard](https://docs.stripe.com/invoicing/dashboard/credit-notes)
- [API](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes)
- [edit the amount due](https://docs.stripe.com/invoicing/invoice-edits)