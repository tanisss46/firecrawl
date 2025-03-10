# Accept a GrabPay payment

## Learn how to accept GrabPay, a common payment method in Southeast Asia.

#### Note

[Subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
using GrabPay for future payments aren’t currently supported. Reach out to
[Stripe support](https://support.stripe.com/contact) for any support queries on
these features.

WebMobileStripe-hosted pageDirect API
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

GrabPay is a
[single-use](https://docs.stripe.com/payments/payment-methods#usage) payment
method. Customers pay with GrabPay by redirecting from your website to GrabPay
to authorize the payment. After that, they will automatically be redirected back
to your website. You will get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

Assets such as logos and payment buttons are provided in the [branding
guidelines](https://docs.stripe.com/payments/grabpay#branding-guidelines)
section.

[Determine
compatibility](https://docs.stripe.com/payments/grabpay/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
GrabPay payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
- The `sgd` currency is supported for businesses based in Singapore.
- The `myr` currency is supported for businesses based in Malaysia.
[Accept a
payment](https://docs.stripe.com/payments/grabpay/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
Checkout integration.

This guides you through enabling GrabPay and shows the differences between
accepting a card payment and using GrabPay.

### Enable GrabPay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `grabpay` to the list of `payment_method_types`
- Make sure all your `line_items` use the same currency

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'grabpay'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `grabpay`, all line items must have currency: sgd, myr
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

When testing your Checkout integration, select GrabPay as the payment method and
click the **Pay** button.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Stripe support](https://support.stripe.com/contact)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [branding
guidelines](https://docs.stripe.com/payments/grabpay#branding-guidelines)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)