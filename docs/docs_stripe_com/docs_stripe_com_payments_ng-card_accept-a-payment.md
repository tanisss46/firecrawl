# Accept a payment using local cards in NigeriaPrivate preview

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

Integrating with Naira card enables Nigerian customers to pay using
Nigerian-issued cards.

Local cards offer a redirect-based payment flow. When a customer makes a
payment, Stripe redirects them to the local merchant of record service
provider’s checkout page to authenticate and authorize the payment. After the
customer authorizes the payment, Stripe redirects them back to your site.

[Determine
compatibility](https://docs.stripe.com/payments/ng-card/accept-a-payment#compatibility)
[A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works#session)
must satisfy all of the following conditions to support Nigerian payment
methods:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Nigerian naira (currency code `ngn`).
- The minimum amount accepted is 500 NGN, and the maximum amount accepted is
100,000,000 NGN.
[Accept a Naira card
payment](https://docs.stripe.com/payments/ng-card/accept-a-payment#accept-a-ng-card-payment)
Enable Naira card by making the following updates to your integration.

When creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you must do the
following:

- Add `ng_card` to the list of `payment_method_types`.
- Make sure all `line_items` use the `ngn` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'ng_card'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `ng_card`, all line items must have currency: ngn
 currency: 'ngn',
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
integration](https://docs.stripe.com/payments/ng-card/accept-a-payment#test-integration)
When testing your Checkout integration, select **Naira payment methods** as the
payment method and click **Pay**.

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works#session)
- [Prices](https://docs.stripe.com/api/prices)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)