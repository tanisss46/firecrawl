# TWINT payments

## Learn how to accept TWINT, a popular payment method in Switzerland.

WebStripe-hosted pageDirect API
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

TWINT is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method used in Switzerland. It allows customers to [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
payments using an approved TWINT mobile app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

[Determine
compatibility](https://docs.stripe.com/payments/twint/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
TWINT:

- You must express [Prices](https://docs.stripe.com/api/prices) for all line
items in Swiss Franc (currency code `chf`).
[Accept a TWINT
payment](https://docs.stripe.com/payments/twint/accept-a-payment#accept-a-twint-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Enable TWINT by making the following updates to your card payment integration.

When creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you must:

- Add `twint` to the list of `payment_method_types`.
- Make sure all `line_items` use the `chf` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'twint'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `twint`, all line items must have currency: chf
 currency: 'chf',
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
integration](https://docs.stripe.com/payments/twint/accept-a-payment#test-integration)
When testing your Checkout integration, select ‘TWINT’ as the payment method and
click **Pay**.

[Handle
refunds](https://docs.stripe.com/payments/twint/accept-a-payment#refunds-and-disputes)
Learn more about [TWINT
refunds](https://docs.stripe.com/payments/twint#refunds).

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [TWINT refunds](https://docs.stripe.com/payments/twint#refunds)
- [Customizing
checkout](https://docs.stripe.com/payments/checkout/customization)