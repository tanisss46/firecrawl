# MB WAY paymentsInvite only

## Learn how to accept the MB WAY payment method.

MB WAY is a digital wallet payment method in Portugal. When paying with MB WAY,
customers initiate payments using their phone number, and [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions) them
using their MB WAY app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
of whether the payment succeeded or failed.

#### Note

MB WAY supports international phone numbers, but the majority of customers use a
Portuguese phone number starting with +351. You can test your integration in a
[sandbox](https://docs.stripe.com/sandboxes) using [test phone
numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment#web-test-integration).

Stripe-hosted pageAdvanced integrationDirect API
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

MB WAY is a digital wallet payment method in Portugal. When paying with MB WAY,
customers initiate payments using their phone number, and [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions) them
using their MB WAY app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
of whether the payment succeeded or failed.

#### Note

MB WAY supports international phone numbers, but the majority of customers use a
Portuguese phone number starting with +351. You can test your integration in a
[sandbox](https://docs.stripe.com/sandboxes) using [test phone
numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment#web-test-integration).

[Determine
compatibility](https://docs.stripe.com/payments/mb-way/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support MB
WAY:

- You must express [Prices](https://docs.stripe.com/api/prices) for all line
items in Euros (currency code `eur`).
[Accept a MB WAY
payment](https://docs.stripe.com/payments/mb-way/accept-a-payment#accept-a-mb-way-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Enable MB WAY by making the following updates to your integration.

When creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you must:

- Add `mb_way` to the list of `payment_method_types`.
- Make sure all `line_items` use the `eur` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'mb_way'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `mb_way`, all line items must have currency: eur
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

[Handle
refunds](https://docs.stripe.com/payments/mb-way/accept-a-payment#refunds-and-disputes)
Learn more about [MB WAY
refunds](https://docs.stripe.com/payments/mb-way#refunds).

[Test your
integration](https://docs.stripe.com/payments/mb-way/accept-a-payment#web-test-integration)
Test your MB WAY integration by using the following test phone numbers. Each set
of details reproduces a common live mode scenario.

Phone numberDescription`+351911111112`The PaymentIntent status transitions from
`requires_action` to `succeeded` after 15 seconds.`+351911111113`The
PaymentIntent status transitions from `requires_action` to
`requires_payment_method` immediately. Stripe returns the
`payment_method_not_available` error code.`+351911111114`The PaymentIntent
status transitions from `requires_action` to `requires_payment_method`
immediately. Stripe returns the `payment_method_provider_decline` error
code.`+351911111115`The PaymentIntent status transitions from `requires_action`
to `requires_payment_method` immediately. Stripe returns the
`payment_intent_payment_attempt_expired` error code.`+351911111116`The
PaymentIntent status transitions from `requires_action` to
`requires_payment_method` immediately. Stripe returns the
`payment_method_customer_decline` error code.`<any other number>`The
PaymentIntent status immediately transitions from `requires_action` to
`succeeded`.
## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [sandbox](https://docs.stripe.com/sandboxes)
- [test phone
numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment#web-test-integration)
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
- [MB WAY refunds](https://docs.stripe.com/payments/mb-way#refunds)
- [Customizing
checkout](https://docs.stripe.com/payments/checkout/customization)