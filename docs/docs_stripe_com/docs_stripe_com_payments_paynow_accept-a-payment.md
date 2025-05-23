# Accept a PayNow payment

## Accept payments with PayNow, a funds transfer service popular in Singapore.

Stripe-hosted pageDirect API
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, update your integration
to [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

PayNow is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method. Customers pay with PayNow by scanning the QR code that they see
during Checkout. Completing the payment redirects customers back to your
website.

[Determine
compatibility](https://docs.stripe.com/payments/paynow/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
PayNow payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency, and must be in `sgd`.
- You can only use one-time line items (PayNow Checkout Sessions don’t support
recurring [subscription](https://docs.stripe.com/billing/subscriptions/creating)
plans).
[Accept a
payment](https://docs.stripe.com/payments/paynow/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
Checkout integration.

This guides you through enabling PayNow and shows the differences between
accepting a card payment and using PayNow.

### Enable PayNow as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `paynow` to the list of `payment_method_types`
- Make sure all your `line_items` use the same currency

```
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['paynow'],
 # or you can take multiple payment methods with
 # payment_method_types: ['card', 'paynow', ...]
 line_items: [{
 price_data: {
 currency: 'sgd',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill
orders](https://docs.stripe.com/checkout/fulfillment).

## Test your integration

When testing your Checkout integration, select PayNow as the payment method and
click the **Generate QR code** button, which creates and renders a QR code.

While testing, you can scan the QR code with a QR code scanning application on
your mobile device. The QR code payload contains a URL which brings you to a
Stripe-hosted PayNow test payment page where you can either authorize or fail
the test payment.

In live mode, you will be able to scan the QR code using a preferred banking app
or payment app that supports PayNow.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)