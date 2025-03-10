# Swish paymentsInvite only

## Learn how to accept Swish, a popular payment method in Sweden.

WebMobileStripe-hosted pageAdvanced integrationDirect API
Swish is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method used in Sweden. It allows customers to [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
payments using the Swish mobile app and the Swedish BankID mobile app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

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

Use this guide to enable Swish on
[Checkout](https://docs.stripe.com/payments/checkout), our hosted checkout form,
and learn the differences between accepting a card payment and a Swish payment.

[Determine
compatibility](https://docs.stripe.com/payments/swish/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support Swish
payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in SEK.
[Set up
StripeServer-side](https://docs.stripe.com/payments/swish/accept-a-payment#web-set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Accept a
payment](https://docs.stripe.com/payments/swish/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
Checkout integration.

### Enable Swish as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `swish` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `sek` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'swish'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `swish`, all line items must have currency: sek
 currency: 'sek',
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

[OptionalHandle post-payment
events](https://docs.stripe.com/payments/swish/accept-a-payment#post-payment-events)[OptionalTest
the
integration](https://docs.stripe.com/payments/swish/accept-a-payment#direct-api-test-integration)
## Failed payments

Swish uses multiple data points to decide when to decline a transaction (for
example, there aren’t enough funds in the customer’s bank account, or the
customer has clicked **Cancel** in the app).

In these cases, the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) is detached
and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for a Swish
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) with a
status of `requires_action`, customers must complete the payment within 3
minutes. If no action is taken after 3 minutes, the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) is detached
and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
object’s status automatically transitions to `requires_payment_method`.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Prices](https://docs.stripe.com/api/prices)
- [Register now](https://dashboard.stripe.com/register)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)