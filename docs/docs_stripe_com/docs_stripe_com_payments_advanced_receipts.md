# Email receipts

## Automatically send receipts and paid invoices.

With payments using [Elements](https://docs.stripe.com/payments/elements) and
the [Payment Intents API](https://docs.stripe.com/api/payment_intents), you can
manually or automatically send customized email receipts. Learn more about
[receipts for payments](https://docs.stripe.com/receipts).

## Automatically send receipts

To enable automated receipts, toggle **Successful payments** on in your
[Customer emails settings](https://dashboard.stripe.com/settings/emails).
Receipts are only sent when a successful payment has been made. No receipt is
sent if the payment fails or is declined.

You don’t have to specify any receipt parameters when you create a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents). However, if
you specify a
[receipt_email](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-receipt_email)
and the payment succeeds, Stripe sends a receipt to that address regardless of
your Customer emails settings.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 --data-urlencode description="Thanks for your purchase!" \
--data-urlencode
receipt_email="I.override.your.customer.email.settings@example.com"
```

The receipt displays the amount, your [public business
information](https://dashboard.stripe.com/settings/public), and any value in the
`description` parameter of the request. Receipts for one-time payments include
only this information. You can’t add additional line items.

To trigger an automatic receipt after the payment is complete, update the
PaymentIntent’s
[receipt_email](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-receipt_email).

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
[description](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-description)
attribute on the
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object). Some
examples include:

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

The [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
can’t generate invoices. Use Stripe Billing to directly [create the
invoice](https://docs.stripe.com/invoicing/integration/quickstart).

## Localization

When using the Payment Intents API, the language of the receipt is determined by
several factors:

- If a Customer is set, their [preferred
locale](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)
is used if available.
- If a Customer is set without any preferred locale, or if no Customer is set,
the [language setting](https://dashboard.stripe.com/settings/emails) from the
Stripe Dashboard is applied.

## Links

- [Elements](https://docs.stripe.com/payments/elements)
- [Payment Intents API](https://docs.stripe.com/api/payment_intents)
- [receipts for payments](https://docs.stripe.com/receipts)
- [Customer emails settings](https://dashboard.stripe.com/settings/emails)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
-
[receipt_email](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-receipt_email)
- [public business information](https://dashboard.stripe.com/settings/public)
-
[receipt_email](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-receipt_email)
- [Branding settings](https://dashboard.stripe.com/settings/branding)
-
[description](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-description)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [update the Charge](https://docs.stripe.com/api/charges/update)
- [create the invoice](https://docs.stripe.com/invoicing/integration/quickstart)
- [preferred
locale](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)