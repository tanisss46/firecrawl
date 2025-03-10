# Receipts and paid invoices

## Send payment or refund receipts automatically.

Each receipt contains a link to view it in a browser and a unique [receipt
number](https://docs.stripe.com/api#charge_object-receipt_number) that’s useful
when looking up payment information.

You can also access the link to view the receipt in a browser through the API in
the [PaymentIntent’s](https://docs.stripe.com/payments/payment-intents) related
[Charge](https://docs.stripe.com/api/charges/object#charge_object-receipt_url)
object. When you visit the link, the receipt always shows the latest status of
that charge—if it has been refunded, the receipt accurately reflects it.

As a security measure, receipt links expire within 30 days. Expired receipt
links require the customer to provide the original email address to resend the
receipt to that address.

## Automatically send receipts

You can enable automated receipts with:

- [Payment
Links](https://docs.stripe.com/payment-links/post-payment#send-email-receipts)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)-
[Stripe-hosted
page](https://docs.stripe.com/payments/checkout/receipts?payment-ui=stripe-hosted#automatically-send-receipts)
- [Embedded
form](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-form#automatically-send-receipts-embedded-form)
- [Embedded
components](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-components#automatically-send-receipts-embedded-components)
- [Advanced
integrations](https://docs.stripe.com/payments/advanced/receipts#automatically-send-receipts)

## Manually send receipts

To send receipts in the [Dashboard](https://dashboard.stripe.com/payments),
click **Send receipt** within the **Receipt history** section of a Payment
details page. You can also hover over a payment within the **Payments** section
of a customer’s page and click the **Send receipt** icon. To resend an email
receipt, input a different email address, or specify a comma-separated list of
addresses to send it to several recipients. A record of the last 10 receipts is
visible on the payment’s page.

To give your customer direct access to a receipt through your application, use
the
[receipt_url](https://docs.stripe.com/api/charges/object#charge_object-receipt_url).

## Customize receipts

Learn how to customize receipts with:

- [Payment
Links](https://docs.stripe.com/payment-links/post-payment#send-email-receipts)
- [Checkout Sessions
API](https://docs.stripe.com/payments/checkout/receipts#customizing-receipts)-
[Stripe-hosted
page](https://docs.stripe.com/payments/checkout/receipts?payment-ui=stripe-hosted#customizing-receipts)
- [Embedded
form](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-form#customizing-receipts-embedded-form)
- [Embedded
components](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-components#customizing-receipts-embedded-components)
- [Advanced
integrations](https://docs.stripe.com/payments/advanced/receipts#automatically-send-receipts)

## Refund receipts

When a payment is refunded, Stripe can automatically send a receipt to the same
email address provided in the original charge. You can also use the Dashboard to
manually send a copy of the refund receipt. To enable automated refund receipts,
toggle **Refunds** on in your [Customer emails
settings](https://dashboard.stripe.com/settings/emails).

## Invoice and subscription payment receipts

Stripe creates a receipt when a customer pays an
[invoice](https://docs.stripe.com/api/invoices) or makes any
[subscription](https://docs.stripe.com/billing/subscriptions/creating) payment.
Receipts for subscription and invoice payments are itemized to include line
items, discounts, and taxes. After payment, the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page) includes a link to
a receipt that the customer can download for their own records.

## Stripe Connect receipts

Receipt settings depend on the charge and account type:

- [Destination charges](https://docs.stripe.com/connect/destination-charges) and
[separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers):
Receipts use the platform account’s **Customer emails**, **Branding**, and
**Public details** settings.
- [Direct charges](https://docs.stripe.com/connect/direct-charges): Receipts use
the connected account’s **Customer emails**, **Branding**, and **Public
details** settings.

Platform accounts can send a receipt for a connected account by passing
`receipt_email` when making a charge request.

For connected accounts that use the Stripe Dashboard (which includes Standard
connected accounts), you can configure receipt settings under
[Branding](https://dashboard.stripe.com/settings/branding). For connected
accounts that don’t use the Dashboard (which includes Express and Custom
connected accounts), the platform configures receipt settings through
[settings.branding](https://docs.stripe.com/api/accounts/update#update_account-settings-branding).

## See also

- [Send customer emails](https://docs.stripe.com/invoicing/send-email)
- [Automate customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails)

## Links

- [test API keys](https://docs.stripe.com/keys#test-live-modes)
- [Dashboard](https://dashboard.stripe.com/test/payments)
- [receipt number](https://docs.stripe.com/api#charge_object-receipt_number)
- [PaymentIntent’s](https://docs.stripe.com/payments/payment-intents)
- [Charge](https://docs.stripe.com/api/charges/object#charge_object-receipt_url)
- [Payment
Links](https://docs.stripe.com/payment-links/post-payment#send-email-receipts)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)
- [Stripe-hosted
page](https://docs.stripe.com/payments/checkout/receipts?payment-ui=stripe-hosted#automatically-send-receipts)
- [Embedded
form](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-form#automatically-send-receipts-embedded-form)
- [Embedded
components](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-components#automatically-send-receipts-embedded-components)
- [Advanced
integrations](https://docs.stripe.com/payments/advanced/receipts#automatically-send-receipts)
- [Dashboard](https://dashboard.stripe.com/payments)
- [Checkout Sessions
API](https://docs.stripe.com/payments/checkout/receipts#customizing-receipts)
- [Stripe-hosted
page](https://docs.stripe.com/payments/checkout/receipts?payment-ui=stripe-hosted#customizing-receipts)
- [Embedded
form](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-form#customizing-receipts-embedded-form)
- [Embedded
components](https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-components#customizing-receipts-embedded-components)
- [Customer emails settings](https://dashboard.stripe.com/settings/emails)
- [invoice](https://docs.stripe.com/api/invoices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)
- [Branding](https://dashboard.stripe.com/settings/branding)
-
[settings.branding](https://docs.stripe.com/api/accounts/update#update_account-settings-branding)
- [Send customer emails](https://docs.stripe.com/invoicing/send-email)
- [Automate customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails)