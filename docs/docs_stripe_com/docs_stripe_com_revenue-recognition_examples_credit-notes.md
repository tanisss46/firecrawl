# Credit note examples

## Learn about revenue recognition with credit note examples.

Unless stated otherwise, these credit note examples assume that revenue
recognition takes place on a per-day basis.

## Credit note before a payment

A pre-paid credit note is issued before the customer makes a payment or before
the invoice is fully paid. It is used to adjust the amount the customer owes or
to provide a discount upfront. Here’s an example:

In this example, a customer starts a subscription for a 3 month period on
January 1 at 00:00:00 UTC that costs 120 USD. Before a payment is received, you
offer a pre-payment credit note of 30 USD that is applied to the customer
balance. This is treated like an upfront discount and reduces your overall
invoice to 90 USD. The invoice is then paid in February for 90 USD. Your summary
for March would look something like this:

AccountStartingJan 2024Feb 2024Mar
2024EndingAccountsReceivable0.00+90.00-90.000.00Cash0.00+90.0090.00Revenue0.00+31.00+28.00+31.0090.00DeferredRevenue0.00+59.00-28.00-31.000.00
## Credit note after a payment

You can use a refund, a customer credit, or an out-of-band credit to issue a
credit note to a customer after they’ve made a payment.

In this example, a customer starts a subscription for a 3 month period on
January 1 at 00:00:00 UTC that costs 90 USD. The subscription generates an
invoice and the customer pays it immediately. On February 1, you issue a credit
note of 45 USD where you: refund 15 USD; credit 10 USD to the customer balance;
and credit 20 USD to an external customer balance (an out-of-band credit). Your
summary for March would like something like this:

AccountJan 2024Feb 2024Mar
2024Cash+90.00-15.00Revenue+31.00+14.00+15.50DeferredRevenue+59.00-43.50-15.50Refunds+5.10CreditNotes+10.40CustomerBalance+10.00ExternalCustomerBalance+20.00
## Credit note without line items

This example uses the following assumptions:

- On January 1 at 00:00:00 UTC, a customer starts a 6 month subscription that
costs 181 USD.
- The subscription generates an invoice.
- The invoice finalizes, but the customer has not paid yet.
- On February 1, you issue a credit note of 90.50 USD.

When the credit note is issued:

- The accounts receivable account is reduced according to the credit note’s
amount.
- Recognized revenue is offset by contra revenue proportionally in the credit
notes account.
- Deferred revenue from the subscription that hasn’t been recognized is reduced
proportionally to the credit note amount.

If you viewed the summary after March ends, it might look something like this:

AccountStartingJan 2024Feb 2024Mar 2024Ending Mar
2024AccountsReceivable0.00+181.00-90.5090.50Revenue0.00+31.00+14.00+15.5060.50DeferredRevenue0.00+150.00-89.00-15.500.00CreditNotes0.00+15.5015.50
When the credit note is voided on May 3:

- Reverses the credit notes account.
- Increases accounts receivable back to the original invoice due amount.
- Recognizes the reduced revenue in May instead of February, March, and April.
- Reinstates the reduced deferred revenue in May.

The summary after June end might look something like:

AccountStartingJan 2024Feb 2024Mar 2024Apr 2024May 2024Jun
2024EndingAccountsReceivable0.00+181.00-90.50+90.50181.00Revenue0.00+31.00+14.00+15.50+15.00+75.50+30.00181.00DeferredRevenue0.00+150.00-89.00-15.50-15.00-0.50-30.000.00CreditNotes0.00+15.50-15.5015.50
A credit note without line items doesn’t match with a specific invoice line
item. Rather, the amount of the credit note is divided proportionally among the
invoice line items.

## Credit note with line items

A credit note with line items works similarly to a [credit note without line
items](https://docs.stripe.com/revenue-recognition/examples/credit-notes#credit-note-without-line-items),
except that a credit note line item is used for adjusting the revenue and other
accounts for a corresponding invoice line item.

## Credit note with negative line items

Adjustments to accounts for a credit note with negative line items are the
reverse of those for a credit note with positive line items.

Learn how to [credit negative invoice line items in the
Dashboard](https://docs.stripe.com/invoicing/dashboard/credit-notes#negative-line-items)
or [programmatically with the
API](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes#negative-line-items).

## Links

- [credit negative invoice line items in the
Dashboard](https://docs.stripe.com/invoicing/dashboard/credit-notes#negative-line-items)
- [programmatically with the
API](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes#negative-line-items)