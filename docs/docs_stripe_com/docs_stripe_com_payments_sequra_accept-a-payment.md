# Accept a payment with SeQuraPrivate preview

## Learn how to set up your integration with SeQura.

## Interested in getting early access to SeQura?

To learn more or get early access, enter your email address below. We'll work
with you to determine your eligibility, and from there, add you to the waitlist.

Collect EmailSign upRead our [privacy
policy](https://stripe.com/privacy).WebStripe-hosted pageAdvanced
integrationDirect API
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

SeQura is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method that offers customers payment terms ranging from 7-120 days.
Customers are redirected from your website or app, authorize the payment with
SeQura, then return to your website or app. You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
of whether the payment succeeded or failed.

[Determine
compatibility](https://docs.stripe.com/payments/sequra/accept-a-payment#compatibility)
To support SeQura payments, a Checkout Session must satisfy all of the following
conditions:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency.- If you have line items in different currencies, create separate
Checkout Sessions for each currency.
[Accept a
payment](https://docs.stripe.com/payments/sequra/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

This guide describes how to enable SeQura and shows the differences between
accepting a card payment and using SeQura.

### Enable SeQura as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add ` sequra ` to the list of `payment_method_types`.
- Make sure all `line_items` use the same currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'sequra'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `sequra`, all line items must have currency: eur
 currency: 'eur',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 1000,
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
integration](https://docs.stripe.com/payments/sequra/accept-a-payment#test-integration)
When testing your Checkout integration, select SeQura as the payment method and
click the **Pay** button.

!

## See also

- [More about SeQura](https://docs.stripe.com/payments/sequra)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [privacy policy](https://stripe.com/privacy)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [More about SeQura](https://docs.stripe.com/payments/sequra)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)