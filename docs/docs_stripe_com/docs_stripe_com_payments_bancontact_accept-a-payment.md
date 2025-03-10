# Accept a Bancontact payment

## Learn how to accept Bancontact, a common payment method in Belgium.

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

Bancontact is a [single
use](https://docs.stripe.com/payments/payment-methods#usage) payment method
where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. [Customers](https://docs.stripe.com/api/customers) pay with
Bancontact by redirecting from your website, authorizing the payment, then
returning to your website where you get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

#### Note

Your use of Bancontact must be in accordance with our [Bancontact Terms of
Service](https://stripe.com/bancontact/legal).

[Determine
compatibility](https://docs.stripe.com/payments/bancontact/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Bancontact payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Euro (currency code `eur`).
[Accept a
payment](https://docs.stripe.com/payments/bancontact/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable Bancontact—shows the differences between
accepting a card payment and using Bancontact.

### Enable Bancontact as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `bancontact` to the list of `payment_method_types`
- Make sure all your `line_items` use the `eur` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'bancontact'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `bancontact`, all line items must have currency: eur
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
integration](https://docs.stripe.com/payments/bancontact/accept-a-payment#test-integration)
There are no special test numbers required for Bancontact.

When testing your Checkout integration, select Bancontact as the payment method
and click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/bancontact/accept-a-payment#refunds-and-disputes)
The refund period for Bancontact is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [More about Bancontact](https://docs.stripe.com/payments/bancontact)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

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
- [Bancontact Terms of Service](https://stripe.com/bancontact/legal)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [More about Bancontact](https://docs.stripe.com/payments/bancontact)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)