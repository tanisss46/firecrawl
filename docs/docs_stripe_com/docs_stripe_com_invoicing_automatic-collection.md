# Automatic collection

## Learn about Stripe's automatic recovery features for Invoicing.

Stripe provides a number of automated revenue recovery features for one-off
invoices to help collect payments that might have failed otherwise. These
include automatically updating your users’ saved cards, sending emails when a
failed payment occurs, and retrying cards at strategic times.

## Smart Retries

Using machine learning, Smart Retries chooses the best times to retry failed
payment attempts to increase the chance of successfully paying an invoice. The
machine learning system behind Smart Retries uses time-dependent, dynamic
signals, such as:

- The number of different devices that have presented a given payment method in
the last *N* hours.
- The best time to pay (payments made for debit cards in certain countries might
be slightly more successful at 12:01 AM in local time zones).

Based on a combination of these factors, Stripe intelligently assesses when to
retry payments. We continuously learn from new purchaser behaviors and
transactions, which provide for a more targeted approach over traditional
rules-based payment retry logic. Any invoice with the
[auto_advance](https://docs.stripe.com/api/invoices/create#create_invoice-auto_advance)
attribute set to `true` goes through the Smart Retries flow (if enabled),
regardless of the selected payment method.

Smart Retries reattempts the charge according to your specifications for the
number of retries and the maximum duration. You can also use
[automations](https://docs.stripe.com/billing/automations) to create different
retry policies for different customer segments.

You can override this behavior by [disabling Smart
Retries](https://dashboard.stripe.com/revenue_recovery/retries) and defining
your own custom retry rules. When you enable dunning, the
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
attribute on the `invoice.payment_failed`
[webhook](https://docs.stripe.com/webhooks) indicates when Stripe attempts the
next collection.

## Failed payment notifications

In the [Subscriptions and emails tab of your billing
settings](https://dashboard.stripe.com/settings/billing/automatic), scroll to
the **Manage failed payments for subscriptions** section. The setting **Send
emails when card payments fail** turns on automatic customer emails for failed
payments.

If a payment failure occurs on a one-off invoice and **Link to a Stripe-hosted
page** is selected, Stripe sends a link to the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page) to the customer.

You can customize the color, icon, and logo of your customer emails and
Stripe-hosted page in the [Branding
settings](https://dashboard.stripe.com/settings/branding).

## Manage invoices sent to customers

In the [Subscriptions and emails tab of your billing
settings](https://dashboard.stripe.com/settings/billing/automatic), scroll to
the **Manage invoices sent to customers** section to:

- **Email finalized invoices to customers**—You can turn this option on to
always email your customers a finalized invoice. This setting only affects
invoices where the
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
is set to `send_invoice`.
- **Change a past due invoice’s status**—You can mark an invoice as
uncollectible if it’s past due by 30, 60, or 90 days. You can also leave the
invoice past-due.
- **Automatically reconcile partial payments that meet a minimum**—You can
instruct Stripe to mark an invoice as paid if ​​it’s partially paid within the
set amount. For example, if the payment received from your customer is within 20
USD or less of the total (or at whatever amount you configure), then this
setting applies a credit to the invoice for the outstanding amount. It then
marks the invoice as paid.

### Automatic reminders for one-off invoices

To turn on automatic reminders for unpaid, one-off invoices, navigate to the
[Invoices tab of your billing
settings](https://dashboard.stripe.com/settings/billing/invoice), scroll to the
**Manage advanced invoicing features** section, and turn on **Send reminders if
a one-off invoice hasn’t been paid**. For each reminder you want to send, click
**Add reminder** and select a schedule from the dropdown list. You can schedule
reminders for before, on, or after the invoice due date.

## Links

-
[auto_advance](https://docs.stripe.com/api/invoices/create#create_invoice-auto_advance)
- [automations](https://docs.stripe.com/billing/automations)
- [disabling Smart
Retries](https://dashboard.stripe.com/revenue_recovery/retries)
-
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
- [webhook](https://docs.stripe.com/webhooks)
- [Subscriptions and emails tab of your billing
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Branding settings](https://dashboard.stripe.com/settings/branding)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Invoices tab of your billing
settings](https://dashboard.stripe.com/settings/billing/invoice)