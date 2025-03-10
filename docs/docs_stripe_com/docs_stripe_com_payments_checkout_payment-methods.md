# Manage payment methods

## Use dynamic payment methods or manually define the payment methods to allow per checkout session.

Stripe dynamically displays the most relevant payment methods to your customers
based on the payment method preferences you set in the Dashboard and eligibility
factors such as transaction amount, currency, and payment flow. To enable and
manage your payment method preferences, go to the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
enables certain payment methods for you by default and might enable additional
payment methods after notifying you.

## Manually specify payment methods

You can override Dashboard settings by manually specifying
[payment_method_types](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)
when creating the Checkout Session. Unless your integration requires that you
list payment methods manually, we recommend that you manage payment methods from
the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

If multiple payment methods are passed, Stripe dynamically reorders them to
prioritize the most relevant payment methods based on the customer’s location
and other characteristics.

[Learn about payment methodsExplore the available options for global payment
methods.](https://docs.stripe.com/payments/payment-methods/overview)[Add
one-click payment buttonsUse one-click payment options, such as Apple Pay or
Google Pay.](https://docs.stripe.com/checkout/one-click-payment-buttons)

## Links

- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
-
[payment_method_types](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)
- [Learn about payment methodsExplore the available options for global payment
methods.](https://docs.stripe.com/payments/payment-methods/overview)
- [Add one-click payment buttonsUse one-click payment options, such as Apple Pay
or Google Pay.](https://docs.stripe.com/checkout/one-click-payment-buttons)