# Accept a WeChat Pay payment

## Use the Payment Intents and Payment Methods APIs to accept WeChat Pay, a digital wallet popular with customers from China.

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

WeChat Pay is a
[single-use](https://docs.stripe.com/payments/payment-methods#usage) payment
method. Customers pay with WeChat Pay by scanning the QR code that they see
during Checkout. Completing the payment redirects customers back to your
website.

[Determine
compatibility](https://docs.stripe.com/payments/wechat-pay/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
WeChat Pay payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (WeChat Pay Checkout Sessions don’t
support recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans).
[Accept a
payment](https://docs.stripe.com/payments/wechat-pay/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
Checkout integration.

This guides you through enabling WeChat Pay and shows the differences between
accepting a card payment and using WeChat Pay.

### Enable WeChat Pay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `wechat_pay` to the list of `payment_method_types`
- Pass the `client` as `'web'` in the `payment_method_options.wechat_pay` hash
- Make sure all your `line_items` use the same currency

```
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['wechat_pay'],

 # or you can take multiple payment methods with
 # payment_method_types: ['card', 'wechat_pay', ...]

# Specify the client (currently, Checkout only supports a client value of "web")
 payment_method_options: {
 wechat_pay: {
 client: 'web',
 },
 },
 line_items: [{
 price_data: {
 currency: 'usd',
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

When testing your Checkout integration, select WeChat Pay as the payment method
and click the **Pay** button, which renders a QR code.

Scanning the QR code while testing routes you to a Stripe hosted page, which
allows you to simulate authorizing the test payment.

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