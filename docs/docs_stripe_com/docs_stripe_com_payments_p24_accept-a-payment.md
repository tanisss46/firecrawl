# Accept a Przelewy24 payment

## Learn how to accept Przelewy24 (P24), the most popular payment method in Poland.

WebMobileStripe-hosted pageAdvanced integration
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

[Przelewy24](https://www.przelewy24.pl/) is a [single
use](https://docs.stripe.com/payments/payment-methods#usage) payment method
where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. [Customers](https://docs.stripe.com/api/customers) pay with
Przelewy24 by redirecting from your website, authorizing the payment, then
returning to your website where you get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

[Determine
compatibility](https://docs.stripe.com/payments/p24/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Przelewy24 payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
[Accept a
payment](https://docs.stripe.com/payments/p24/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
Checkout integration.

Use this guide to learn how to enable Przelewy24—it shows the differences
between accepting a card payment and using Przelewy24.

### Enable Przelewy24 as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `p24` to the list of `payment_method_types`.
- Make sure all your `line_items` use the same currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'p24'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `p24`, all line items must have currency: eur, pln
 currency: 'eur',
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
integration](https://docs.stripe.com/payments/p24/accept-a-payment#test-integration)
When testing your Checkout integration, select Przelewy24 as the payment method
and click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/p24/accept-a-payment#refunds-and-disputes)
The refund period for Przelewy24 is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Przelewy24](https://www.przelewy24.pl)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)