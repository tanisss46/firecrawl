# Stripe Connector for Commercetools Connect

## Learn how to enable Stripe payments through Commercetools Connect.

You can integrate payments with the [Commercetools
Connect](https://commercetools.com/commerce-platform/connect) integration
framework. Because of the composability of Commercetools, you can choose between
two integration paths to address your specific needs and technical requirements.
These paths are also SAQ-A eligible for PCI compliance.

## Use Commercetools Checkout

The Commercetools pre-built checkout supports the Stripe [Payment
Element](https://docs.stripe.com/payments/payment-element) natively. You can
access this integration through the [Stripe Payment for
Checkout](https://docs.stripe.com/connectors/commercetools-connect/install-and-configure-checkout).

!

Commercetools Checkout

## Build a custom checkout

If you want to build a custom checkout for Commercetools, you can use the
[Stripe Payment for Composable
Commerce](https://docs.stripe.com/connectors/commercetools-connect/install-and-configure)
to maintain communication between both systems. The connector translates webhook
events between both systems, and supports integration with the [Payment
Element](https://docs.stripe.com/payments/payment-element) and [Express
Checkout](https://docs.stripe.com/elements/express-checkout-element).

!

Custom checkout composable commerce

## Manage payment methods

You can enable or disable payment methods from your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) in the Stripe
Dashboard. This applies to both the Express Checkout Element and the Payment
Element.

To customize the look and feel of these Elements from the Stripe Payment
Connector configuration, add code similar to the following:

```
{
 "theme":"stripe","variables":
 {
 "colorPrimary":"#0570DE",
 "colorBackground":"#FFFFFF",
 "colorText":"#30313D",
 "colorDanger":"#DF1B41",
 "fontFamily":"Ideal Sans,
 system-ui,sansserif","
 spacingUnit":"2px",
 "borderRadius":"4px"
 }
 }

```

## See also

- [Install and configure the Stripe Payment Connector for Commercetools
Checkout](https://docs.stripe.com/connectors/commercetools-connect/install-and-configure-checkout)
- [Install and configure the Stripe Payment Composable
Connector](https://docs.stripe.com/connectors/commercetools-connect/install-and-configure)

## Links

- [Commercetools Connect](https://commercetools.com/commerce-platform/connect)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Stripe Payment for
Checkout](https://docs.stripe.com/connectors/commercetools-connect/install-and-configure-checkout)
- [Stripe Payment for Composable
Commerce](https://docs.stripe.com/connectors/commercetools-connect/install-and-configure)
- [Express Checkout](https://docs.stripe.com/elements/express-checkout-element)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)