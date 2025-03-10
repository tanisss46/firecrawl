# Stripe invoices in NetSuite

## Learn about how the connector syncs Stripe invoices to NetSuite.

The Stripe Connector for NetSuite automatically syncs the invoices that you
create from Stripe Billing
[subscriptions](https://docs.stripe.com/billing/subscriptions/overview) or
[Stripe Invoicing](https://docs.stripe.com/invoicing/overview) into NetSuite.
The connector creates a representation of these subscription invoices (including
product prices) as NetSuite invoices. When using Stripe subscriptions, Stripe
creates an invoice each period (for example, every month or year), which results
in the connector creating an invoice in NetSuite to represent the subscription.

StatusActionInvoice paidThe connector creates a NetSuite customer payment and
applies it against the NetSuite invoice.Invoice unpaidThe invoice in NetSuite
remains open or is automatically marked as uncollectible.Refund initiatedThe
connector creates a credit memo and customer refund, and applies the credit memo
to the refund to reverse the cash and income for the invoice and
payment.Subscription changedSubscription changes (such as a different product or
quantity purchased) aren’t represented on the invoice for the current
subscription. The invoice for the next subscription cycle includes prorations
and product changes.
## Subscription changes in Stripe

Your customers might want to [upgrade or
downgrade](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)
their subscriptions.

Subscription changes won’t modify the Stripe and NetSuite invoice for the
initial invoice. The initial invoice continues to generate revenue during the
specified billing period. The new invoice generates revenue during the new
subscription period.

### Subscription upgrades

If your customer wants to upgrade their subscription, you charge the difference
between the unused time proration of the current subscription and the cost of
the new subscription. In NetSuite this appears as additions to the subscription
invoice.

### Subscription downgrades

If your customer wants to downgrade their subscription and the new subscription
costs less, you apply a credit for the unused amount of the original
subscription to the next invoice. The customer isn’t refunded, and the balance
gets added to the customer in Stripe.

When the next billing period occurs, Stripe uses the customer balance to pay the
invoice. The connector creates a credit memo against the invoice to represent
the amount applied with the customer balance. If the customer balance is greater
than the invoice amount, Stripe applies the remaining balance to subsequent
invoices.

## Subscription changes in NetSuite

The approach you use to handle subscription changes depends on how you want to
recognize revenue in NetSuite.

SituationSubscription changesRevenue recognitionA customer signs up for a yearly
subscription but wants to switch to a monthly subscription.In Stripe, do the
following:- Fully refund the original subscription.
- Cancel the original subscription.
- Create a new subscription with the updated period.
Use this approach if you don’t want to recognize any revenue in NetSuite for the
original yearly subscription.A customer signs up for a yearly subscription but
wants to switch to a monthly subscription. Or a customer wants to switch their
subscription period in the middle of their subscription.In Stripe, do the
following:- Partially refund the original subscription for the prorated unused
time on the subscription.
- Cancel the original subscription.
- Create a new subscription with the updated period.
Use this approach if you want to partially recognize revenue in NetSuite for the
new monthly subscription.A customer wants to switch their subscription period in
the middle of their subscription.In Stripe, change the original yearly
subscription term to the new monthly subscription term.Ask your implementation
partner to discuss using this approach with the connector.
## Trial invoices

Stripe subscriptions with [trial
periods](https://docs.stripe.com/billing/subscriptions/trials) create
zero-balance invoices in Stripe. The connector can either sync these trial
period invoices into NetSuite or ignore them.

Trial invoices use a special invoice structure in Stripe. All line items on the
invoice are set to zero, so the invoice doesn’t impact accounting. This differs
from coupons or discount codes, which creates an invoice with a net total of
zero.

The connector still syncs invoices that have non-zero line items, because the
invoice might have a net total of zero but contain line items that have general
ledger impact.

## Customer balance or credit

The connector supports paying an invoice with a Stripe [customer credit
balance](https://docs.stripe.com/billing/customer/balance), but this approach
isn’t recommended.

If your customer has a negative account balance, they can use their credit
balance to partially or fully pay an invoice. For example, if they downgrade
their subscription to a lower cost plan, it creates a negative invoice in
Stripe. The unused, prorated value gets added to the customer balance. The
credit memo applies to the next invoice to represent the portion of the invoice
paid using the customer balance. If the invoice has multiple line items, the
connector uses the generic `Stripe Customer Balance Item`. The connector uses
the generic Stripe item because it can’t identify which portion of the customer
balance to apply to each item, even if the customer balance pays the full
invoice amount.

A positive account balance might occur if a plan change or manual adjustment
creates a balance that’s less than the minimum payment amount in the invoice
currency. In this case, the connector uses a unique `Stripe Customer Balance
Debit Item` to represent the balance amount on the next invoice. If the invoice
amount is below the minimum, the invoice isn’t created in NetSuite.

## Manage Stripe invoices

When you [edit an invoice](https://docs.stripe.com/invoicing/invoice-edits) in
Stripe, the connector voids the original NetSuite invoice with a credit memo.
The connector then creates a new invoice to reflect the changes made to the
Stripe invoice.

### Negative Stripe invoices

NetSuite doesn’t allow negative invoices. Because of this, Stripe represents
negative invoices as a zero-dollar invoice in NetSuite, with the negative amount
applied on the next invoice as a customer balance credit.

### Invoice payment failures

Stripe attempts multiple payments on an invoice. If a [payment
fails](https://docs.stripe.com/billing/subscriptions/webhooks#payment-failures),
the invoice remains unpaid in Stripe and open in NetSuite. You must do one of
the following:

- Manually pay the invoice.
- Mark the invoice as uncollectible.
- Mark the invoice as void.

You can also [configure
Stripe](https://dashboard.stripe.com/settings/billing/automatic) to
automatically mark the invoice as
[uncollectible](https://docs.stripe.com/connectors/netsuite/stripe-invoices-netsuite#uncollectible-invoices),
and the connector closes it in NetSuite.

### One-time prices

You can create one-time price objects as lines on an invoice by passing
`price_data`. The price object is automatically archived after it’s used on the
invoice. The connector uses the global `Stripe Item` for one-time price objects.

## Uncollectible invoices

You can mark an open, unpaid invoice as
[uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible) if
payment fails on a subscription that’s past due.

Marking an invoice as uncollectible results in the following:

- Stripe treats the subscription as if the user paid and stops attempting to
collect payment.
- The user’s subscription continues as normal, but the subscription status
remains as `past_due`.
- The connector automatically creates and applies a credit memo in NetSuite by
default. The credit memo reverses the entries to accounts receivable and makes
the entry to an income account. If you don’t want the connector to automatically
close an invoice, enable the `Keep unpaid invoices open` feature.

If your payment retry setting for Stripe subscriptions is to cancel the
subscription, it marks the associated invoice as uncollectible.

The connector doesn’t support reopening invoices that are marked as
uncollectible in Stripe.

The connector doesn’t support reopening invoices marked as uncollectible in
Stripe.

### Mark an invoice as uncollectible

- On the [Subscriptions and
emails](https://dashboard.stripe.com/settings/billing/automatic) tab in the
Dashboard, navigate to the **Manage failed payments for subscriptions** section.
- For the **Invoice status**, select **mark the invoice as uncollectible** if
all retries for a payment fail.

This setting affects how the connector records an invoice’s final state in
NetSuite.

You might not need to enable this setting if your system has additional
requirements, or you have a custom process to close unpaid invoices in NetSuite.
If you don’t enable this setting, any open, unpaid invoices with failed payment
attempts remain open in NetSuite.

### Revenue recognition and bad debt

When creating a credit memo to close an invoice, the connector uses the same
revenue recognition schedules as used on the original invoice items. On the
credit memo, you can represent all bad debt that’s marked as uncollectible with
either of the following:

- The original items on the invoice
- A unique global item to override the default item

Using a bad debt item allows you to customize the account that the bad debt
posts to. If you use a unique global item to represent bad debt, the schedules
from the original invoice aren’t copied to the credit memo.

The connector reports to NetSuite the date that Stripe records the following
invoice statuses: `paid`, `uncollectible`, or `void`. If you use a customized
dunning system to handle payment retries and invoice status changes, the closing
date for the invoice might differ from the Stripe closing date.

## Shipping cost

The connector’s invoice syncing feature supports Stripe [shipping
rates](https://docs.stripe.com/api/shipping_rates). If a Stripe invoice has a
shipping cost, the connector creates a `Stripe Shipping` global item in your
NetSuite instance and uses this item to create a NetSuite invoice line item that
represents the shipping cost.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Subscription invoices](https://docs.stripe.com/billing/invoices/subscription)
- [How subscriptions
work](https://docs.stripe.com/billing/subscriptions/overview)

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Stripe Invoicing](https://docs.stripe.com/invoicing/overview)
- [upgrade or
downgrade](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)
- [trial periods](https://docs.stripe.com/billing/subscriptions/trials)
- [customer credit balance](https://docs.stripe.com/billing/customer/balance)
- [edit an invoice](https://docs.stripe.com/invoicing/invoice-edits)
- [payment
fails](https://docs.stripe.com/billing/subscriptions/webhooks#payment-failures)
- [configure Stripe](https://dashboard.stripe.com/settings/billing/automatic)
-
[uncollectible](https://docs.stripe.com/connectors/netsuite/stripe-invoices-netsuite#uncollectible-invoices)
- [uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible)
- [shipping rates](https://docs.stripe.com/api/shipping_rates)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Subscription invoices](https://docs.stripe.com/billing/invoices/subscription)