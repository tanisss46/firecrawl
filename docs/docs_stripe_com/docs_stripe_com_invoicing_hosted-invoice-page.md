# Hosted Invoice Page

## Use the Hosted Invoice Page to securely collect payment from your customers.

The Hosted Invoice Page provides a secure, private URL where your customers can:

- View the details, amounts, and status of the invoice.
- Pay the invoice using any of the enabled payment methods.
- Download PDF copies of the invoice and receipt.

!

A sample Hosted Invoice Page

Stripe assigns all invoices a unique URL that you can send to your customer. We
host these invoices, which means you can securely collect payments without any
extra implementation code.

## Invoice URLs

When you create and send an invoice, Stripe generates a unique URL for the
Hosted Invoice Page. The URL includes a secure, long, and random identifier,
resembling the following example:

```

https://invoice.stripe.com/i/acct_abcdefghijklmno/test_YWNjdF8xRGZ3UzJDbENJS2xqV3ZzLF9MNGJvMDBzY0xFQ2c1cG1QZzZ6Wk5jV0RXR2lOS1V6LDM0Mjk3NjEz0200wpYOWgBE?s=em

```

Invoice URLs expire 30 days after the due date. If the invoice doesn’t have a
due date, the invoice expires 30 days after it finalizes. In all cases, the
expiration window is never longer than 120 days.

#### Note

Even after expiration, any URLs that the Dashboard displays or a user retrieves
through the API are guaranteed to be valid for at least 10 days.

DashboardAPI
When a URL expires, it no longer loads the intended resource. Instead, Stripe
redirects invoiced customers to a page that states that the URL has expired and
to contact the merchant. This page also provides the merchant’s contact
information.

#### Note

If you sent an invoice through the Dashboard or API, any email recipients are
automatically associated with that invoice. In this case, Stripe redirects the
user to a recovery page where they can enter their email address to receive a
new copy of the original email with non-expired links.

## Invoice email links

You can configure the invoice email to include a link to the Hosted Invoice
Page. When enabled, the Hosted Invoice Page URL appears in:

- Invoice emails as a payment link.
- The footer of invoice PDFs.
- The Invoice API response as
[hosted_invoice_url](https://docs.stripe.com/api/invoices/object#invoice_object-hosted_invoice_url).

To enable the Hosted Invoice Page for all newly created invoices, select the
checkbox for **Include a Stripe-hosted link to an invoice payment page in the
invoice email** in the [Invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) of the
Dashboard.

When sending an invoice, you can use the **Delivery** section to have Stripe
automatically send an email to your customer with the Hosted Invoice Page or
generate a Hosted Invoice Page that you can send yourself. To send the Hosted
Invoice Page yourself, create the invoice and then copy the link to send to your
customer.

## Page customization

The Hosted Invoice Page is customizable with your:

- Brand color
- Logo
- Icon

You can customize these [branding
settings](https://dashboard.stripe.com/account/branding) in the Dashboard.

## Set allowed payment methods

Using the Hosted Invoice Page, you can configure invoices to allow payment with
one or more of the [supported payment
methods](https://docs.stripe.com/invoicing/payment-methods). You can set
defaults to apply to all of the newly created invoices from the [Invoice default
payment method
configuration](https://dashboard.stripe.com/settings/billing/invoice). You can
also select the payment method on a per-invoice basis when you’re [creating an
invoice](https://dashboard.stripe.com/invoices/create) through the Dashboard.

With the Hosted Invoice Page, you can display the allowed payment method list to
the customer. This gives them the option to choose a payment method that suits
them best. Additionally, enabling the Hosted Invoice Page gives the customer the
benefit of having Stripe handle complex payment and authentication flows
(without any extra implementation effort from you).

#### Note

For example, the [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) (SCA)
regulation in Europe requires customers to confirm their payment with [3D
Secure](https://docs.stripe.com/payments/3d-secure) (3DS). In this case, the
Hosted Invoice Page displays the payment confirmation modal to your customer.

## Payment method persistence

Cards, Bacs Direct Debit and BECS Direct Debit details that you enter on the
Hosted Invoice Page are stored on the customer for use in subsequent payments.
We don’t store single-use payment methods like iDEAL, and Bancontact for reuse.

## Public support information

Invoices include any public information that you specified under [Public
business information](https://dashboard.stripe.com/settings/public), such as
your support email address or business website. Using these settings, you can
also choose to include a support phone number in customer-facing documents—like
invoice PDFs and emails—or default to your business address.

## Links

-
[hosted_invoice_url](https://docs.stripe.com/api/invoices/object#invoice_object-hosted_invoice_url)
- [Invoice settings](https://dashboard.stripe.com/settings/billing/invoice)
- [branding settings](https://dashboard.stripe.com/account/branding)
- [supported payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [creating an invoice](https://dashboard.stripe.com/invoices/create)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Public business information](https://dashboard.stripe.com/settings/public)