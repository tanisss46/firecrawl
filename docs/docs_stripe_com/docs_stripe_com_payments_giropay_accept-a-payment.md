# Accept a giropay paymentDeprecated

## Learn how to accept giropay, a common payment method in Germany.

#### Warning

Our financial partners are deprecating Giropay. No new business onboarding or
transactions will be possible after June 30, 2024. Read our [support
page](https://support.stripe.com/questions/june-2024-update-to-giropays-availability)
for more details.

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

giropay is a [single
use](https://docs.stripe.com/payments/payment-methods#usage) payment method
where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. [Customers](https://docs.stripe.com/api/customers) pay with
giropay by redirecting from your website, authorizing the payment, then
returning to your website where you get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed. Because giropay is a single use
payment method, it isn’t compatible with
[SetupIntents](https://docs.stripe.com/api/setup_intents).

#### Note

Your use of giropay must be in accordance with the [giropay Terms of
Service](https://stripe.com/giropay/legal).

[Determine
compatibility](https://docs.stripe.com/payments/giropay/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
giropay payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
[Accept a
payment](https://docs.stripe.com/payments/giropay/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable giropay—it shows the differences between
accepting a card payment and using giropay.

### Enable giropay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `giropay` to the list of `payment_method_types`
- Make sure all your `line_items` use the `eur` currency

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'giropay'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `giropay`, all line items must have currency: eur
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
integration](https://docs.stripe.com/payments/giropay/accept-a-payment#test-integration)
When testing your Checkout integration, select giropay as the payment method and
click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/giropay/accept-a-payment#refunds-and-disputes)
The refund period for giropay is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [support
page](https://support.stripe.com/questions/june-2024-update-to-giropays-availability)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [SetupIntents](https://docs.stripe.com/api/setup_intents)
- [giropay Terms of Service](https://stripe.com/giropay/legal)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)