# Accept a payment using Kakao Pay in South Korea

## Learn how to accept payments from Kakao Pay users.

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

Integrating with [Kakao Pay](https://www.kakaopay.com/) enables South
Korea-based customers to pay using this popular local payment method.

When a customer makes a payment, we redirect them to our local processor partner
to authenticate and authorize the payment. After the customer authorizes the
payment, Stripe redirects them back to your site.

[Determine
compatibility](https://docs.stripe.com/payments/kakao-pay/accept-a-payment#compatibility)
[A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works) must
satisfy all of the following conditions to support South Korean payment methods:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Korean won (currency code `krw`).
- The minimum amount accepted is 100 KRW, and the maximum amount accepted is
2,000,000 KRW.
[Accept a Kakao Pay
payment](https://docs.stripe.com/payments/kakao-pay/accept-a-payment#accept-a-kakao-pay-payment)
Enable Kakao Pay by making the following updates to your integration.

When creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you must do the
following:

- Add `kakao_pay` to the list of `payment_method_types`.
- Make sure all `line_items` use the `krw` currency.
- Provide the buyer’s email address.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'kakao_pay'],
 payment_method_data: {
 kakao_pay: {},
 billing_details: {
 email: "jane.diaz@stripe.com"
 }
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `kakao_pay`, all line items must have currency: krw
 currency: 'krw',
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

[Test your integration with Kakao
Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment#test-integration)
While testing your Checkout integration, select **Kakao Pay** and click **Pay**.
This redirects you to a Stripe-hosted page where you have the choice to
authorize or fail the payment. If you authorize the payment, the PaymentIntent
switches from `requires_action` to `succeeded`. Failing the test payment makes
the PaymentIntent switch from `requires_action` to `requires_payment_method`.
Learn more about how to [test](https://docs.stripe.com/testing#redirects)
redirect-based payment methods.

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Kakao Pay](https://www.kakaopay.com/)
- [A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works)
- [Prices](https://docs.stripe.com/api/prices)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [test](https://docs.stripe.com/testing#redirects)