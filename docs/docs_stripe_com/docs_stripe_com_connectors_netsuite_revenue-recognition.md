# Revenue recognition

## Learn about using the NetSuite revenue recognition engine with Stripe Billing.

The Stripe Connector for NetSuite automatically syncs data from subscription
invoices to NetSuite to enable revenue recognition calculation. The connector
passes the start and end dates from the Stripe subscription periods to the
NetSuite invoice lines.

#### Note

The connector supports NetSuite Advanced Revenue Management (ARM) only. NetSuite
classic revenue recognition (also called legacy revenue recognition) and [Stripe
Revenue Recognition](https://docs.stripe.com/revenue-recognition) aren’t
supported. If you don’t use NetSuite ARM, no action is needed from you.

## How it works

- During onboarding, you specify a revenue recognition rule that the connector
uses when it creates an item. You can set up this rule using a [field
mapping](https://docs.stripe.com/connectors/netsuite/field-mappings).
- When the connector [creates an
invoice](https://docs.stripe.com/connectors/netsuite/invoice-automation) from a
Stripe subscription, it specifies a period start and end date. The connector
copies these dates to the NetSuite invoice at the line item level.
- When the connector creates a full or partial refund for an invoice, the credit
memo created against the invoice uses the same revenue recognition schedule as
the invoice.
- At the end of each accounting period, you manually create a revenue
recognition journal entry. When this occurs, revenue moves from the deferred
revenue account to your earned income account.

## Revenue date range

Stripe and NetSuite define the revenue date range differently. While Stripe
defines the date range as up to *but not including* the end date, NetSuite
defines the date range as up to *and including* the end date.

This means the last day of the revenue period in NetSuite is one day less than
the corresponding end date of the revenue period in Stripe. The connector
handles this difference to comply with the NetSuite date range definition by
adding a day to the Stripe end date and using that value as the NetSuite end
date.

## Invoice and line item dates

Each line item on a Stripe invoice contains a period start and end date. These
dates get copied to the NetSuite invoice line item’s Stripe start and end dates,
by default. If you require another set of start and end date fields in NetSuite,
you can create a script or workflow to copy the dates from the Stripe start and
end dates.

## Modified revenue recognition dates

When the connector creates a NetSuite transaction based on another transaction
(for example, a credit memo created from an invoice), the revenue recognition
schedule copies directly from the original transaction. Because this is a
point-in-time copy, any subsequent changes to the revenue recognition schedule
on the new transaction won’t reflect on the original source transaction. This
applies even if a revenue recognition journal entry hasn’t generated for the
original transaction.

For example, you have an invoice in your NetSuite account with a revenue
recognition schedule of January 1 to June 1. If you create a credit memo for the
invoice on February 15 and manually update the revenue recognition dates, the
dates on the invoice won’t change.

## Closed accounting periods and earned revenue

When using revenue recognition, open accounting periods affect how refund
revenue for credit memos earn over time.

For example, if the September accounting period closes before you can create the
credit memo, the September refund revenue moves to October. Two identical
entries for October appear in the credit memos revenue recognition schedule.

You must create the revenue recognition journal entries before closing the
period. If you don’t, the following occurs:

- Refund revenue for credit memos created after the last journal entry for
invoices with revenue earned in the closing period won’t be accounted for.
- Revenue in the period about to close won’t move out of the deferred revenue
account.
- Revenue recognition looks like it’s attempting to book revenue for a month
that’s already closed.

## Coupons

Coupons appear as non-posting discount items. Instead of posting to an income
account, these items bundle with the applicable NetSuite item. When calculating
the revenue recognition impact for a product item in a NetSuite invoice, the
non-posting discount amount subtracts from the total.

## Refunds and credit memos

When the connector creates a full or partial refund for a Stripe subscription
invoice, it also creates a credit memo and customer refund. The credit memo uses
the same revenue recognition schedule as the invoice, regardless of the revenue
already earned on the invoice.

For example, in September you created an invoice for 120 USD with a 12 month
straight-line by accounting period revenue recognition schedule. The current
date is October 15, and the September accounting period isn’t closed yet. The
connector creates a credit memo for the total amount of the invoice created in
September. The revenue recognition schedule for the credit memo is the same as
the invoice schedule, despite different creation months. This means the credit
memo contains a refund of 10 USD for September and 10 USD for October.

## Credit memos created by customer balance

Credit memos represent the payments against an invoice by a customer balance.
You can recognize the credit against the invoice because the credit memo copies
the invoice’s revenue recognition schedule.

## Manual revenue recognition

You can use the connector’s revenue recognition system without using NetSuite
Advanced Revenue Management (ARM). The connector can import revenue recognition
data (the revenue period for a specific line item) into NetSuite. Then you can
set up manual or custom automated systems to recognize revenue.

## Customize the deferred revenue account

You can customize the deferred revenue account using [field
mappings](https://docs.stripe.com/connectors/netsuite/field-mappings). For
example, you might integrate the following, where the metadata value is the
internal ID of the deferred revenue account:

```
service_sale_item: {
 "metadata.netsuite_deferred_revenue_account" : "deferred_revenue_account_id"
}

```

## Links

- [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition)
- [field mapping](https://docs.stripe.com/connectors/netsuite/field-mappings)
- [creates an
invoice](https://docs.stripe.com/connectors/netsuite/invoice-automation)