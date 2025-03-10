# Accept an Alipay payment

## Learn how to accept Alipay payments, a digital wallet popular with customers from China.

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

Alipay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. Customers pay by redirecting from your website or app, authorize
the payment through Alipay, then return to your website or app where you get
[immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

[Determine
Compatibility](https://docs.stripe.com/payments/alipay/accept-a-payment#compatibility)
To support Alipay payments, a Checkout Session must satisfy all of the following
conditions:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency.- If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items.

Recurring [subscription](https://docs.stripe.com/billing/subscriptions/creating)
plans aren’t supported.

[Accept a
payment](https://docs.stripe.com/payments/alipay/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

This guide describes how to enable Alipay and shows the differences between
accepting a card payment and using Alipay.

### Enable Alipay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `Alipay` to the list of `payment_method_types`.
- Make sure all `line_items` use the same currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'alipay'],
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

[Test your
integration](https://docs.stripe.com/payments/alipay/accept-a-payment#test-integration)
When testing your Checkout integration, select Alipay as the payment method and
click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/alipay/accept-a-payment#refunds-and-disputes)
The refund period for Alipay is up to 90 days after the original payment.

Alipay has no dispute process—customers authenticate with their Alipay account.

## See also

- [More about Alipay](https://docs.stripe.com/payments/alipay)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
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
- [More about Alipay](https://docs.stripe.com/payments/alipay)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)