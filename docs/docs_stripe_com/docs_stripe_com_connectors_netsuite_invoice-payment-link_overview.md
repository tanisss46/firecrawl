# NetSuite invoice payment link

## Learn how to create an invoice payment link that customers can use to pay NetSuite invoices.

The Stripe Connector for NetSuite creates a payment link for each of your
invoices. Your customers can pay their invoices using [Stripe
Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works), and
with any of the [payment
methods](https://docs.stripe.com/payments/payment-methods/overview) that you
enable.

This free, self-serve version of the connector allows you to process payments
with Stripe from NetSuite, without syncing payments or other data to NetSuite.

NetSuite

Business

Customer

Stripe

NetSuite creates an invoice and automatically generates a payment page link

You send the payment link to your customer (automatically or manually)

The customer submits payment through Stripe Checkout

Stripe sends the payout to your bank account

A diagram providing a high level overview of the invoice payment link flow
## Customize the payment link

You can customize the look and feel of the payment link to match the design of
your site. Modify the payment link color and design on the [Branding
settings](https://dashboard.stripe.com/settings/branding) page in the Stripe
Dashboard. Modify your name and statement descriptor on the [Public
details](https://dashboard.stripe.com/settings/public) page.

## Add the payment link to your communications

You can integrate the payment link into your customer communications in
NetSuite. For example, you might choose to map the payment link to a [Pay Now
button](https://support.stripe.com/questions/stripe-connector-for-netsuite-pay-now-button)
in your NetSuite email templates, invoice PDF templates, or manual outreach.

## Send email receipts for payments

You have two options for sending email receipts to your customers:

- Use Stripe to automatically send email receipts. The connector provides the
invoice ID and NetSuite customer email. To use this option, enable **Successful
payments** on the [Customer emails
settings](https://dashboard.stripe.com/settings/emails) page in the Stripe
Dashboard. You can also [customize your
receipts](https://docs.stripe.com/receipts?payment-ui=payment-links#customizing-receipts).
- Use NetSuite to send email receipts for payments. You must disable email
receipts in the Stripe Dashboard and then set up a workflow to send customized
email receipts from NetSuite.

## Support multiple currencies and payment methods

Accept payments in the [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies) in your
region. The payment link displays the currency that’s specified on the NetSuite
invoice. Stripe then creates a payment based on that currency.

You can enable the payment methods you want to accept on the [Payment
methods](https://dashboard.stripe.com/settings/payment_methods) page. Stripe
supports many categories of [payment
methods](https://docs.stripe.com/payments/payment-methods/overview) based on
your region and business needs.

## Full version

The free version of the connector with the payment page link doesn’t include
syncing payments or other data to NetSuite.

With the paid, full version of the connector you can:

- Sync all Stripe activity, including payments, invoices, and refunds
- Automate syncing Stripe payouts as NetSuite deposits
- Calculate fees and currency conversion

If you’re interested in learning more about the full [Stripe Connector for
NetSuite](https://docs.stripe.com/connectors/netsuite/overview), [install the
app](https://marketplace.stripe.com/apps/netsuite-connector) and request a demo.
You can also [contact us](mailto:connector-netsuite-sales@stripe.com) to discuss
how you use Stripe and NetSuite.

## See also

- [Install the Stripe Connector for NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
-
[Troubleshooting](https://docs.stripe.com/connectors/netsuite/error-resolution)

## Links

- [Stripe
Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works)
- [payment methods](https://docs.stripe.com/payments/payment-methods/overview)
- [Branding settings](https://dashboard.stripe.com/settings/branding)
- [Public details](https://dashboard.stripe.com/settings/public)
- [Pay Now
button](https://support.stripe.com/questions/stripe-connector-for-netsuite-pay-now-button)
- [Customer emails settings](https://dashboard.stripe.com/settings/emails)
- [customize your
receipts](https://docs.stripe.com/receipts?payment-ui=payment-links#customizing-receipts)
- [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [Payment methods](https://dashboard.stripe.com/settings/payment_methods)
- [Stripe Connector for
NetSuite](https://docs.stripe.com/connectors/netsuite/overview)
- [install the app](https://marketplace.stripe.com/apps/netsuite-connector)
- [Install the Stripe Connector for NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
-
[Troubleshooting](https://docs.stripe.com/connectors/netsuite/error-resolution)