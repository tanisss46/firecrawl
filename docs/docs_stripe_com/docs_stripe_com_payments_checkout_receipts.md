# Email receipts and paid invoices

## Send receipts for payments and refunds automatically.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can manually or automatically send customized email receipts or [paid
invoices](https://docs.stripe.com/payments/checkout/receipts#paid-invoices).
Learn more about [receipts for payments](https://docs.stripe.com/receipts).

## Automatically send receipts

To enable automated receipts, toggle **Successful payments** on in your
[Customer emails settings](https://dashboard.stripe.com/settings/emails).
Receipts are only sent when a successful payment has been made—no receipt is
sent if the payment fails or is declined.

## Customize receipts

Alter the appearance and functionality of your receipts with the following
customization options:

- **Branding**: Modify the logo and colors in your [Branding
settings](https://dashboard.stripe.com/settings/branding). The upper limit for a
custom logo image file size is 512KB. Ideally, the logo should be a square image
exceeding 128 x 128 pixels. JPG, PNG, and GIF file types are supported.
- **Public information**: Specify the public information you want to include,
such as your contact number or website address, in your [Public details
settings](https://dashboard.stripe.com/settings/public).

To display custom text, use the
[payment_intent_data.description](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-description)
attribute on the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/object). Some examples
include:

- Description of goods or services provided
- Authorization code
- Subscription information
- Cancellation policies

You can see a real-time preview of your email receipt on your Dashboard Branding
settings page. To send a test receipt, hover over the preview image and click
**Send test receipt**, then enter your email address.

#### Caution

Receipts pull data from the `Charge` object generated when the PaymentIntent is
confirmed. To update receipt data such as the `description` after the charge is
generated, you must [update the
Charge](https://docs.stripe.com/api/charges/update). Changes to a confirmed
PaymentIntent don’t appear on receipts.

## Automatically send paid invoices

In addition to ordinary receipts, Checkout can generate paid invoices as proof
of payment. Invoices have more information than receipts. For subscriptions,
Stripe generates invoices automatically, but for one-time payments, you need to
enable them.

#### Note

Invoice creation for one-time payments through the [Checkout Sessions
API](https://docs.stripe.com/api/checkout/sessions) is not an
[Invoicing](https://stripe.com/invoicing) feature, and is priced separately.
Review [this support
article](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links)
to learn more.

To generate invoices, first, in your [Customer emails
settings](https://dashboard.stripe.com/settings/emails), under **Email customers
about**, select **Successful payments**. Then, when creating a Checkout session,
set
[invoice_creation[enabled]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-invoice_creation-enabled)
to `true`.

#### Note

Enabling `invoice_creation` isn’t supported if you set
`payment_intent_data[capture_method]` to `manual`.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 -d "invoice_creation[enabled]"=true \
 -d "line_items[0][price]"={{ONE_TIME_PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 --data-urlencode success_url="https://example.com" \
 --data-urlencode cancel_url="https://example.com"
```

After the payment completes, Stripe sends an invoice summary with links to
download the invoice PDF and invoice receipt to the email address your customer
provides during checkout.

#### Caution

Invoices for delayed notification payment methods might take longer to send
because we send the invoice after successful payment, not upon checkout session
completion. These methods include: [Bacs Direct
Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment), [Bank
transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment),
[Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment), [Canadian
pre-authorized
debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment),
[Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment),
[OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment), [Pay by
Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment), [SEPA
Direct Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment),
[SOFORT](https://docs.stripe.com/payments/sofort/accept-a-payment), and [ACH
Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment).

![Screenshot of the invoice PDF that customers can download from the invoice
summary
email](https://b.stripecdn.com/docs-statics-srv/assets/invoice.9e44668032383601eeec362f38293b7a.png)

The downloadable invoice PDF

![Screenshot of the invoice receipt that customers can download from the invoice
summary
email](https://b.stripecdn.com/docs-statics-srv/assets/invoice_receipt.4f120ee7363f8e7728fa553a8a24aae3.png)

The downloadable invoice receipt

![Screenshot of the invoice summary email Stripe
sends](https://b.stripecdn.com/docs-statics-srv/assets/email.560c2666905531b907f7fcd4f1a0a6dd.png)

The customer email with links to the invoice PDF and receipt

You can also view the invoice in the
[Dashboard](https://dashboard.stripe.com/invoices) or access it programmatically
by listening to the
[invoice.paid](https://docs.stripe.com/api/events/types#event_types-invoice.paid)
event through an [event
destination](https://docs.stripe.com/event-destinations).

You can use the `invoice_data` hash inside `invoice_creation` to further
customize the invoice generated by the Checkout Session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 -d "invoice_creation[enabled]"=true \
 -d "invoice_creation[invoice_data][description]"="Invoice for Product X" \
 -d "invoice_creation[invoice_data][metadata][order]"=order-xyz \
 -d "invoice_creation[invoice_data][account_tax_ids][0]"=DE123456789 \
 -d "invoice_creation[invoice_data][custom_fields][0][name]"="Purchase Order" \
 -d "invoice_creation[invoice_data][custom_fields][0][value]"=PO-XYZ \
-d
"invoice_creation[invoice_data][rendering_options][amount_tax_display]"=include_inclusive_tax
\
 -d "invoice_creation[invoice_data][footer]"="B2B Inc." \
 -d "line_items[0][price]"={{ONE_TIME_PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 --data-urlencode success_url="https://example.com" \
 --data-urlencode cancel_url="https://example.com"
```

Review [invoice best practices](https://docs.stripe.com/invoicing/customize) for
your region to make sure you’re collecting the right information from your
customers. Information like the customer’s billing and shipping addresses, phone
number and tax ID appear on the resulting invoice.

## Localization

When using Checkout Sessions, the language of the receipt and invoice is
determined by several factors:

- If a Customer is set, their [preferred
locale](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)
are used if available.
- If a Customer is set without any preferred locales, the [language
setting](https://dashboard.stripe.com/settings/emails) from the Stripe Dashboard
is applied.
- If no Customer is set, the language defaults to the browser locale of the user
opening the Checkout Session URL.

## See also

- [Send customer emails](https://docs.stripe.com/invoicing/send-email)
- [Automate customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails)

## Links

- [receipts for payments](https://docs.stripe.com/receipts)
- [Customer emails settings](https://dashboard.stripe.com/settings/emails)
- [Branding settings](https://dashboard.stripe.com/settings/branding)
- [Public details settings](https://dashboard.stripe.com/settings/public)
-
[payment_intent_data.description](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-description)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object)
- [update the Charge](https://docs.stripe.com/api/charges/update)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)
- [Invoicing](https://stripe.com/invoicing)
- [this support
article](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links)
-
[invoice_creation[enabled]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-invoice_creation-enabled)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment)
- [Bank
transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment)
- [Canadian pre-authorized
debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment)
- [Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment)
- [OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment)
- [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment)
- [SEPA Direct
Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [SOFORT](https://docs.stripe.com/payments/sofort/accept-a-payment)
- [ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
- [Dashboard](https://dashboard.stripe.com/invoices)
-
[invoice.paid](https://docs.stripe.com/api/events/types#event_types-invoice.paid)
- [event destination](https://docs.stripe.com/event-destinations)
- [invoice best practices](https://docs.stripe.com/invoicing/customize)
- [preferred
locale](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)
- [Send customer emails](https://docs.stripe.com/invoicing/send-email)
- [Automate customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails)