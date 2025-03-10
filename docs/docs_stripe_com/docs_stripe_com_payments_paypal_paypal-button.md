# PayPal Button

## Learn how the PayPal button simplifies payments for your customers.

Your customers can make PayPal payments through a redirect or by using the
PayPal button. Stripe determines whether to present the redirect or the button,
but you can configure your pages to increase availability of the button. The
PayPal button is available in the [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element) and [Stripe
Checkout](https://docs.stripe.com/payments/checkout).

This demo shows the PayPal button in the Express Checkout Element:

Background ColorLightButton ThemeGoldButton TypePayPalSizeDesktop
Before you start, we recommend you create a [PayPal Sandbox
account](https://developer.paypal.com/tools/sandbox/accounts/) to test your
integration.

Express Checkout ElementStripe Checkout
The PayPal button works in Stripe’s Express Checkout Element only for one-off
payments, not for recurring payments. To learn how to integrate PayPal with the
Express Checkout Element, see [the Express Checkout Element
guide](https://docs.stripe.com/elements/express-checkout-element).

**Recommended options**

In certain scenarios, the Express Checkout Element doesn’t support the PayPal
button, and presents PayPal only as a redirect. These scenarios include:

- Billing address collection is enabled
- Phone number collection is enabled

To maximize the chance of presenting the PayPal button, we recommend using the
following options when
[creating](https://docs.stripe.com/js/elements_object/create_express_checkout_element)
the Express Checkout Element.

HTML + JSReact
```
elements.create('expressCheckout', {
 phoneNumberRequired: false,
 billingAddressRequired: false,
});
```

## Links

- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [PayPal Sandbox account](https://developer.paypal.com/tools/sandbox/accounts/)
-
[creating](https://docs.stripe.com/js/elements_object/create_express_checkout_element)