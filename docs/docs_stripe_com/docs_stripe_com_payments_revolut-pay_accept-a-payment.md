# Accept a payment with Revolut Pay

## Add support for Revolut Pay to your integration.

WebMobileStripe-hosted pageAdvanced integrationDirect API
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

Revolut Pay is a
[reusable](https://docs.stripe.com/payments/payment-methods#usage) payment
method where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. Customers pay by being redirected from your website or app,
authorizing the payment with Revolut Pay, then returning to your website or app.
You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
of whether the payment succeeded or failed.

[Determine
compatibility](https://docs.stripe.com/payments/revolut-pay/accept-a-payment#compatibility)
To support Revolut Pay payments, a Checkout Session must satisfy all of the
following conditions:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency.- If you have line items in different currencies, create separate
Checkout Sessions for each currency.

Recurring [subscription](https://docs.stripe.com/billing/subscriptions/creating)
plans are supported.

[Accept a
payment](https://docs.stripe.com/payments/revolut-pay/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

This guide describes how to enable Revolut Pay and shows the differences between
accepting a card payment and using Revolut Pay.

### Enable Revolut Pay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `revolut_pay` to the list of `payment_method_types`.
- Make sure all `line_items` use the same currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'revolut_pay'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `revolut_pay`, all line items must have currency: eur, gbp
 currency: 'gbp',
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

[Test your
integration](https://docs.stripe.com/payments/revolut-pay/accept-a-payment#test-integration)
When testing your Checkout integration, select Revolut Pay as the payment method
and click the **Pay** button.

!

## See also

- [More about Revolut Pay](https://docs.stripe.com/payments/revolut-pay)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [reusable](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [More about Revolut Pay](https://docs.stripe.com/payments/revolut-pay)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)