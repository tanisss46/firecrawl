# Send customer emails

## Configure and send invoicing emails to your customers.

Set up Stripe to send important email notifications and reminders to your
customers. Certain email notifications contain a link to a Stripe-hosted page
that customers can use to confirm or update their payment details.

In your [Email settings](https://dashboard.stripe.com/settings/emails), you can
opt out of sending your customers emails for successful payments. If you’re
[automatically charging](https://docs.stripe.com/invoicing/automatic-charging) a
customer and you’ve turned off emails for successful payments, they won’t
receive an [email
receipt](https://docs.stripe.com/invoicing/dashboard#invoice-receipts). To learn
how to send automatic email receipts, see [Email receipts and paid
invoices](https://docs.stripe.com/receipts#automatically-send-receipts).

To turn on automatic reminders, navigate to your [Invoicing
settings](https://dashboard.stripe.com/test/settings/billing/invoice) and scroll
down to **Manage advanced invoicing features** > **Send reminders if a one-off
invoice hasn’t been paid**. Select if you want Stripe to send the reminder
before, when, or after the invoice is due. You can choose from a set of
predefined options.

If you’ve set up and verified a [custom email
domain](https://docs.stripe.com/get-started/account/email-domain), we send
invoicing emails from that domain.

## Customer emails

You can configure Stripe to send email notifications or reminders to your
customer:

- Upon failed payment attempts.
- After Stripe
[finalizes](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
an invoice.
- With [receipts](https://dashboard.stripe.com/settings/emails) after invoices
are paid.
- When a payment requires [3D
Secure](https://docs.stripe.com/payments/3d-secure).
- When a card on file is about to expire.
- If a one-off invoice hasn’t been paid.
- When a credit note is created.
- When refund is issued.
- When a subscription trial is ending.
- Upon cancellation of subscription.

Before you start sending email notifications and reminders, you can customize
your [branding](https://dashboard.stripe.com/account/branding).

![Update card
information](https://b.stripecdn.com/docs-statics-srv/assets/update-card-information.da9d6be4f5bad9e7eb686cc2ba205af6.png)

Remind your customers to update their card information

### Email reminders

You can send one-off invoice email reminders to your customers using the
Dashboard or API. If you’d like to send an email reminder about an expiring
card, go to [Prevent failed
payments](https://dashboard.stripe.com/settings/billing/automatic).

DashboardAPI
To send a one-off invoice email reminder, go to the [Invoices
page](https://dashboard.stripe.com/test/invoices). Click on the customer’s
invoice, followed by **Send invoice**. Before you resend an invoice, Stripe
shows you a preview of the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page). You can download
the associated invoice PDF by clicking **Invoice PDF** on the **Invoice
details** page.

![Hosted Invoice
Page](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-guide.df3cc5a1e4180c338269aacdfa792180.png)

Hosted Invoice Page

![Invoice
PDF](https://b.stripecdn.com/docs-statics-srv/assets/invoice-pdf-guide.d79c407ca08ee4b14dc0519fb3772309.png)

Invoice PDF

### Email notifications

You can send email notifications to your customers by configuring your Dashboard
settings:

- To send an email notification when a card payment fails, go to [Manage failed
payments](https://dashboard.stripe.com/settings/billing/automatic).
- To send an email reminder for an unpaid one-time invoice, go to [Advanced
invoicing features](https://dashboard.stripe.com/settings/billing/invoice).
- To email finalized invoices, navigate to [Manage invoices sent to
customers](https://dashboard.stripe.com/settings/billing/automatic).
- To send an email notification with a receipt after a successful payment, go to
your **Email settings**.

#### Note

Learn more about how you can use customer emails to [recover
revenue](https://docs.stripe.com/billing/revenue-recovery/customer-emails).

#### 3D Secure payments

If charging a customer’s card on file requires them to complete 3D Secure
authentication and you’ve enabled **Send a Stripe-hosted link for cardholders to
authenticate when required** in your [3D Secure
settings](https://dashboard.stripe.com/settings/billing/automatic), Stripe sends
an email. The email links to a Stripe-hosted page where they can confirm the
payment.

## Additional email recipients

You can provide additional recipients to your customer’s Billing emails
(including receipts sent after successful payments) using the Dashboard.

#### Note

The Stripe API doesn’t currently support adding recipients to Billing emails.

- Go to the [Customers page](https://dashboard.stripe.com/test/customers) in
your Dashboard.
- Click the customer you want to add email recipients for to open the customer’s
detail page.
- Click the **Edit** link in the **Details** section of the left pane to open
the **Update customer** dialog.

![Details section with Edit link
highlighted.](https://b.stripecdn.com/docs-statics-srv/assets/edit-emails.18a5f678dc05901c6d1e5ade713afdc1.png)
- In the **Billing information** section of the **Update customer** dialog,
unselect the **Same as account email** checkbox.

![Billing section with same as account checkbox
unselected.](https://b.stripecdn.com/docs-statics-srv/assets/additional-emails.df018f8ddec164bb58653a0ede84d1a8.png)
- *(Optional)* Set the value of the displayed field to a comma-separated list of
emails that should be in the “To” line of Billing emails. If you leave this
field blank, Stripe continues to use the account email.
- Click the **Add more recipients** link to access the **Emails to CC** field.
Set the value of the field to a comma-separated list of email addresses that you
want in the CC line of Billing (Invoice and Subscription) emails.

If you add recipients to the Customer using the previous steps, Stripe
automatically pre-populates these emails to invoices you send through the
Dashboard.

## Change the Stripe invoice template

You can create your own custom email template to replace the Stripe prebuilt
email by [configuring the invoice
template](https://dashboard.stripe.com/settings/billing/invoice). Stripe applies
your custom template to all new invoices.

## Disable Stripe invoice emails and send your own

Stripe can use [webhooks](https://docs.stripe.com/webhooks) to notify you of
changes to your invoices—when they’re finalized, paid, marked uncollectible, and
so on. For each event that you receive, you can construct and deliver your own
emails. If you disable finalized invoice emails, Stripe continues to send
webhooks as a reminder for your own email solution. Learn more about [webhook
endpoints and
invoices](https://docs.stripe.com/billing/subscriptions/webhooks#understand).

## Email PDF attachments

When Stripe emails an invoice, we automatically include a PDF attachment of the
same invoice to assist your customer with record keeping. If you turn on emails
for successful payments—and an invoice is set to charge automatically—the
receipt email includes a PDF attachment of both the original invoice and the
invoice receipt. Visit the [Invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) to disable this
behavior.

## Email logs

For the customer emails sent within the last 30 days, their logs are available
to view within the [customer](https://dashboard.stripe.com/customers) page.

## See also

- [Use the Dashboard](https://docs.stripe.com/invoicing/dashboard)
- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Automate customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails)

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [customizable](https://docs.stripe.com/invoicing/customize)
- [Email settings](https://dashboard.stripe.com/settings/emails)
- [automatically charging](https://docs.stripe.com/invoicing/automatic-charging)
- [email receipt](https://docs.stripe.com/invoicing/dashboard#invoice-receipts)
- [Email receipts and paid
invoices](https://docs.stripe.com/receipts#automatically-send-receipts)
- [Invoicing
settings](https://dashboard.stripe.com/test/settings/billing/invoice)
- [custom email
domain](https://docs.stripe.com/get-started/account/email-domain)
-
[finalizes](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [branding](https://dashboard.stripe.com/account/branding)
- [Prevent failed
payments](https://dashboard.stripe.com/settings/billing/automatic)
- [Invoices page](https://dashboard.stripe.com/test/invoices)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Advanced invoicing
features](https://dashboard.stripe.com/settings/billing/invoice)
- [recover
revenue](https://docs.stripe.com/billing/revenue-recovery/customer-emails)
- [Customers page](https://dashboard.stripe.com/test/customers)
- [webhooks](https://docs.stripe.com/webhooks)
- [webhook endpoints and
invoices](https://docs.stripe.com/billing/subscriptions/webhooks#understand)
- [customer](https://dashboard.stripe.com/customers)
- [Use the Dashboard](https://docs.stripe.com/invoicing/dashboard)