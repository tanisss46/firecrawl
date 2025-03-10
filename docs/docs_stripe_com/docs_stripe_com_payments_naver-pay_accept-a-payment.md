# Accept a payment using Naver Pay in South Korea

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

Integrating with [Naver Pay](https://pay.naver.com/) enables South Korea-based
customers to pay using this popular local payment method.

When a customer makes a payment, we redirect them to our local processor partner
to authenticate and authorize the payment. After the customer authorizes the
payment, we redirect them back to your site.

Customers can optionally use their Naver Pay points to pay for their purchase.

[Determine
compatibility](https://docs.stripe.com/payments/naver-pay/accept-a-payment#compatibility)
[A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works) must
satisfy all of the following conditions to support South Korean payment methods:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Korean won (currency code `krw`).
- The minimum amount accepted is 100 KRW, and the maximum amount accepted is
2,000,000 KRW.
[Accept a Naver Pay
payment](https://docs.stripe.com/payments/naver-pay/accept-a-payment#accept-a-naver-pay-payment)
Enable Naver Pay by making the following updates to your integration.

When creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you must do the
following:

- Add `naver_pay` to the list of `payment_method_types`.
- Make sure all `line_items` use the `krw` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'naver_pay'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `naver_pay`, all line items must have currency: krw
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

[Test your
integration](https://docs.stripe.com/payments/naver-pay/accept-a-payment#test-integration)
While testing your Checkout integration, select **Naver Pay** and click **Pay**.
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
- [Naver Pay](https://pay.naver.com/)
- [A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works)
- [Prices](https://docs.stripe.com/api/prices)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [test](https://docs.stripe.com/testing#redirects)