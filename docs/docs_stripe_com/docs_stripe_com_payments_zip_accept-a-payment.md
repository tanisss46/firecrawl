# Accept a Zip payment

## Learn how to accept Zip, the popular buy now, pay later payment method in Australia.

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

Zip is an Australia-based BNPL payment method that allows customers to split
purchases over a series of payments.

Customers authenticate a payment on Zip website and there is immediate
notification about the success or failure of a payment.

[Determine
compatibility](https://docs.stripe.com/payments/zip/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support Zip
payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Australian Dollar (currency code `aud`).
[Accept a Zip
payment](https://docs.stripe.com/payments/zip/accept-a-payment#accept-a-Zip-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Make the following updates to your card payment integration to enable Zip.

### Enable Zip as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `zip` to the list of `payment_method_types`
- Make sure all your `line_items` use the `aud` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'zip'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `zip`, all line items must have currency: aud
 currency: 'aud',
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
integration](https://docs.stripe.com/payments/zip/accept-a-payment#test-integration)
When testing your Checkout integration, select Zip as the payment method and
click **Pay**.

[Handle refunds and
disputes](https://docs.stripe.com/payments/zip/accept-a-payment#refunds-and-disputes)
Learn more about Zip
[disputes](https://docs.stripe.com/payments/zip#disputes-and-fraud) and
[refunds](https://docs.stripe.com/payments/zip#refunds).

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [disputes](https://docs.stripe.com/payments/zip#disputes-and-fraud)
- [refunds](https://docs.stripe.com/payments/zip#refunds)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)