# Cash App Pay payments

## Add support for Cash App Pay to your integration.

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

This guides you through enabling Cash App Pay on
[Checkout](https://docs.stripe.com/payments/checkout), our hosted checkout form,
and shows the differences between accepting a card payment and a Cash App Pay
payment.

[Determine
compatibility](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support Cash
App Pay payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in USD.
[Set up
StripeServer-side](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment#web-set-up-stripe)
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
payment](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
Checkout integration.

### Enable Cash App Pay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `cashapp` to the list of `payment_method_types`
- Make sure all your `line_items` use the `usd` currency

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'cashapp'],
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
integration](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment#web-test-integration)Mobile
web app testingDesktop web app testing
To test your integration, choose Cash App Pay as the payment method and tap
**Pay**. While testing, this redirects you to a test payment page where you can
approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile
application—you don’t have the option to approve or decline the payment within
Cash App. The payment is automatically approved after the redirect.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

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
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)