# Use invoices

## Send an invoice your customers can pay online.

Automatically charge your customer’s payment method on file, or email them the
[invoice](https://docs.stripe.com/api/invoices) with or without a link to a
payment page. You can also send the invoice or payment page link manually.

#### Note

To learn about managing subscriptions and recurring revenue, see the
[Subscriptions](https://docs.stripe.com/billing) docs.

![Hosted Invoice
Page](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-guide.df3cc5a1e4180c338269aacdfa792180.png)

Hosted Invoice Page

![Invoice
PDF](https://b.stripecdn.com/docs-statics-srv/assets/invoice-pdf-guide.d79c407ca08ee4b14dc0519fb3772309.png)

Invoice PDF

[Set up your business
brandOptional](https://docs.stripe.com/no-code/invoices#establish-business)
Before you start using Stripe Invoicing, help your future customers understand
your products and terms of service by [adding your business
details](https://dashboard.stripe.com/settings/account?support_details) and
[customizing how your brand
appears](https://dashboard.stripe.com/settings/branding).

Customers see these business and branding details on the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page) when they pay an
invoice online. To let customers manage past invoices and their own billing
information, set up the [customer
portal](https://docs.stripe.com/no-code/customer-portal).

![Brand your
business](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page.79b4c18913fe9fb30f47ad8a5f062b6f.png)

Brand your business

[Choose your payment
methodsOptional](https://docs.stripe.com/no-code/invoices#payment-methods)
By default, customers can pay invoices with any of the payment methods that you
enable in your [invoice
template](https://dashboard.stripe.com/settings/billing/invoice). If you’re a
first-time user, Stripe automatically enables card,
[Link](https://docs.stripe.com/payments/link), bank transfers, Cash App Pay, and
WeChat Pay payment methods. To enable additional payment methods, you need to
activate them in your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

In some situations, restrictions might prevent payment methods from being used
for an invoice. For instance, a payment method might only operate in one
currency, or have limitations on the amount that can be paid. Stripe doesn’t
automatically select a payment method when these limitations prevent it from
being used. To learn more, read about [supported payment
methods](https://docs.stripe.com/invoicing/payment-methods#supported).

![Choose additional payment
methods](https://b.stripecdn.com/docs-statics-srv/assets/supported-payment-methods.949a2d41b8da98f93ad94c95c986e75c.png)

Choose additional payment methods

[How to get paid](https://docs.stripe.com/no-code/invoices#get-paid)
You can [create and send](https://dashboard.stripe.com/invoices/create) an
invoice from the Dashboard. Invoices provide an itemized list of goods and
services rendered, which includes the cost, quantity, and taxes. You can also
use them as a tool to collect payment. [Learn
more](https://docs.stripe.com/invoicing/dashboard).

![Create and send an
invoice](https://b.stripecdn.com/docs-statics-srv/assets/create-send-invoices.985a3078348be3c2591f8d5e2d96e21c.png)

Create and send an invoice

[Set up a custom
templateOptional](https://docs.stripe.com/no-code/invoices#custom-templates)
You can use the [invoice
template](https://dashboard.stripe.com/account/billing/invoice) to customize
​​the content of your invoices. Set a default memo, footer, and numbering
scheme. Determine your default payment terms. Because you know more about your
customers and your business than Stripe does, make sure your invoices include
all of the required information. See the full invoice customization guide at
[Customize invoices](https://docs.stripe.com/invoicing/customize).

![Configure the Invoice
template](https://b.stripecdn.com/docs-statics-srv/assets/invoice-template.d50c4ba2210f06442b6adbb7279fe7a4.png)

Configure the Invoice template

![Manage tax
information](https://b.stripecdn.com/docs-statics-srv/assets/manage-tax-information.3bbd3b8425726dc4ac243bb5bfd707a3.png)

Manage tax information

[Track an invoice](https://docs.stripe.com/no-code/invoices#track-invoice)
Invoices move through different statuses from the time they’re created to when
they’re paid. Track the status of an invoice on the [invoices
page](https://dashboard.stripe.com/test/invoices) in the Dashboard. To let your
customer know that the due date for an invoice is approaching, [send them an
email reminder](https://docs.stripe.com/invoicing/send-email). Learn more in our
[invoice management
docs](https://docs.stripe.com/invoicing/dashboard/manage-invoices).

![Track and manage your
invoices](https://b.stripecdn.com/docs-statics-srv/assets/track-invoices.647ee840cc77e53c4d8537ec43ba9289.png)

Track and manage your invoices

[Automate Invoice Reconciliation and
Collection](https://docs.stripe.com/no-code/invoices#invoicing-plus)
To automate Stripe Invoicing and get paid faster, choose to [automatically
charge](https://docs.stripe.com/invoicing/automatic-charging) your customer’s
payment method on file. You can also let Stripe handle [invoice
recovery](https://docs.stripe.com/invoicing/automatic-collection) issues.

![Automate
invoicing](https://b.stripecdn.com/docs-statics-srv/assets/advanced-invoicing-features.70dfe42ac952e7924876201c06e5902d.png)

Automate invoicing

### Close your books and account for revenue

Using [automatic
reconciliation](https://docs.stripe.com/invoicing/automatic-reconciliation)
means that you don’t need to expose your sensitive bank account details to users
or manually reconcile open invoices with your bank. With auto-reconciliation for
invoices, Stripe can:

- Match incoming payments with invoice amounts.
- Manage overpayment or underpayment, when the amount paid doesn’t match the
invoice.
- Reduce the number of API calls required to transfer funds into Stripe.
- Manage payment retries on open invoices.

![Close your
books](https://b.stripecdn.com/docs-statics-srv/assets/invoicing-auto-reconciliation.2d4b2648e4b67e8b2a2c7225a22bec69.png)

Close your books

## Links

- [Pay-as-you-go](https://stripe.com/pricing)
- [Stripe Billing pricing](https://stripe.com/billing/pricing)
- [invoice](https://docs.stripe.com/api/invoices)
- [Subscriptions](https://docs.stripe.com/billing)
- [adding your business
details](https://dashboard.stripe.com/settings/account?support_details)
- [customizing how your brand
appears](https://dashboard.stripe.com/settings/branding)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [customer portal](https://docs.stripe.com/no-code/customer-portal)
- [invoice template](https://dashboard.stripe.com/settings/billing/invoice)
- [Link](https://docs.stripe.com/payments/link)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [supported payment
methods](https://docs.stripe.com/invoicing/payment-methods#supported)
- [create and send](https://dashboard.stripe.com/invoices/create)
- [Learn more](https://docs.stripe.com/invoicing/dashboard)
- [invoice template](https://dashboard.stripe.com/account/billing/invoice)
- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [invoices page](https://dashboard.stripe.com/test/invoices)
- [send them an email reminder](https://docs.stripe.com/invoicing/send-email)
- [invoice management
docs](https://docs.stripe.com/invoicing/dashboard/manage-invoices)
- [automatically charge](https://docs.stripe.com/invoicing/automatic-charging)
- [invoice recovery](https://docs.stripe.com/invoicing/automatic-collection)
- [automatic
reconciliation](https://docs.stripe.com/invoicing/automatic-reconciliation)