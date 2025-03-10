# MobilePay payments

## Learn how to accept MobilePay, a popular payment method in Denmark and Finland.

WebMobileStripe-hosted pageAdvanced integrationDirect API
MobilePay is a
[single-use](https://docs.stripe.com/payments/payment-methods#usage) card wallet
payment method used in Denmark and Finland. It allows your customer to
[authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using
the card data we receive from MobilePay. The processing of the card transaction
is invisible to your integration, and Stripe [immediately notifies
you](https://docs.stripe.com/payments/payment-methods#payment-notification)
whether the payment succeeded or failed.

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

Use this guide to enable MobilePay on
[Checkout](https://docs.stripe.com/payments/checkout), our hosted checkout form,
and learn the differences between accepting a card payment and a MobilePay
payment.

[Determine
compatibility](https://docs.stripe.com/payments/mobilepay/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
MobilePay payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Euro, Danish Krona, Swedish Krona or Norwegian Krona (currency
codes `eur`, `dkk`, `sek` or `nok`).
[Set up
StripeServer-side](https://docs.stripe.com/payments/mobilepay/accept-a-payment#set-up-stripe)
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
payment](https://docs.stripe.com/payments/mobilepay/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
Checkout integration.

### Enable MobilePay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `mobilepay` to the list of `payment_method_types`
- Make sure all your `line_items` use the `eur`, `dkk`, `sek` or `nok` currency

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'mobilepay'],
 line_items: [{
 price_data: {
 currency: 'usd',
# To accept `mobilepay`, all line items must have currency: eur, dkk, sek, nok
 currency: 'dkk',
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

[Handle post-payment
events](https://docs.stripe.com/payments/mobilepay/accept-a-payment#post-payment-events)
Stripe sends a
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
event when the payment completes. Use the Dashboard, a custom
[webhook](https://docs.stripe.com/webhooks), or a partner solution to receive
these events and run actions, like sending an order confirmation email to your
customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On
the client, the customer could close the browser window or quit the app before
the callback executes, and malicious clients could manipulate the response.
Setting up your integration to listen for asynchronous events also helps you
accept more payment methods in the future. Learn about the [differences between
all supported payment
methods](https://stripe.com/payments/payment-methods-guide).

### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts,
handle payouts, or retry failed payments.

- [View your test payments in the
Dashboard](https://dashboard.stripe.com/test/payments)

### Custom code

Build a webhook handler to listen for events and build custom asynchronous
payment flows. Test and debug your webhook integration locally with the Stripe
CLI.

- [Build a custom
webhook](https://docs.stripe.com/payments/handling-payment-events#build-your-own-webhook)

### Prebuilt apps

Handle common business events, like
[automation](https://stripe.partners/?f_category=automation) or [marketing and
sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating
a partner application.

[Test the
integration](https://docs.stripe.com/payments/mobilepay/accept-a-payment#testing)Mobile
web app testingDesktop web app testing
To test your integration, choose MobilePay as the payment method and tap
**Pay**. In test mode, this redirects you to a test payment page where you can
approve or decline the payment.

In live mode, tapping **Pay** redirects you to the MobilePay mobile application,
where you can approve or decline the payment.

[OptionalAuthorize a payment and then capture
later](https://docs.stripe.com/payments/mobilepay/accept-a-payment#manual-capture)[OptionalCancellation](https://docs.stripe.com/payments/mobilepay/accept-a-payment#cancellation)
## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined.
Learn more about [card declines](https://docs.stripe.com/declines/card). In this
case, the PaymentMethod is detached and the PaymentIntent’s status automatically
transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must
authenticate the payment within 5 minutes. If no action is taken after 5
minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically
transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a
MobilePay transaction. [Refunds](https://docs.stripe.com/refunds) and
[disputes](https://docs.stripe.com/disputes/how-disputes-work) are subject to
the Visa and Mastercard network rules.

## See also

- [More about MobilePay](https://docs.stripe.com/payments/mobilepay)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customize Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediately notifies
you](https://docs.stripe.com/payments/payment-methods#payment-notification)
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
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
- [webhook](https://docs.stripe.com/webhooks)
- [differences between all supported payment
methods](https://stripe.com/payments/payment-methods-guide)
- [View your test payments in the
Dashboard](https://dashboard.stripe.com/test/payments)
- [Build a custom
webhook](https://docs.stripe.com/payments/handling-payment-events#build-your-own-webhook)
- [automation](https://stripe.partners/?f_category=automation)
- [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales)
- [card declines](https://docs.stripe.com/declines/card)
- [Refunds](https://docs.stripe.com/refunds)
- [disputes](https://docs.stripe.com/disputes/how-disputes-work)
- [More about MobilePay](https://docs.stripe.com/payments/mobilepay)
- [Customize Checkout](https://docs.stripe.com/payments/checkout/customization)