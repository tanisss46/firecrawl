# BLIK payments

## Learn how to accept BLIK, a common payment method in Poland.

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

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payments. When customers want to pay online using BLIK, they request a
six-digit code from their banking application and enter it into the payment
collection form.

The bank sends a push notification to your customer’s mobile phone asking to
authorize the payment inside their banking application. The BLIK code is valid
for 2 minutes; customers have 60 seconds to authorize the payment after starting
a payment. After 60 seconds, it times out and they must request a new BLIK code.
Customers typically approve BLIK payments in less than 10 seconds.

[Determine
compatibility](https://docs.stripe.com/payments/blik/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support BLIK
payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Złoty (currency code `pln`).
[Accept a
payment](https://docs.stripe.com/payments/blik/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
Checkout integration.

Use this guide to learn how to enable BLIK—it shows the differences between
accepting a card payment and using BLIK.

### Enable BLIK as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `blik` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `pln` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'blik'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `blik`, all line items must have currency: pln
 currency: 'pln',
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

### What customers see

Inside their Banking app, customers see four lines related to each BLIK
transaction:

- If you provided a value for `description` when creating the PaymentIntent, the
first two lines display it (max 70 characters).
- If you provided a value for `statement_descriptor` (typically, an order ID),
line 3 displays it (max 22 characters).
- The fourth line automatically populates with the URL of your website.

### Fulfill your orders

After accepting a payment, learn how to [fulfill
orders](https://docs.stripe.com/checkout/fulfillment).

[Test your
integration](https://docs.stripe.com/payments/blik/accept-a-payment#test-integration)
When testing your Checkout integration, select BLIK as the payment method and
click the **Pay** button.

Use a [sandbox](https://docs.stripe.com/sandboxes) to test a successful payment
by entering any 6-digit code (such as `123456`) in the payment form.

[Handle refunds and
disputes](https://docs.stripe.com/payments/blik/accept-a-payment#refunds-and-disputes)
The refund period for BLIK is up to 13 months after the original payment.

[Customers](https://docs.stripe.com/api/customers) can dispute a payment through
their bank up to 13 months after the original payment and there’s no appeal
process.

Learn more about [BLIK
disputes](https://docs.stripe.com/payments/blik#disputed-payments).

[OptionalSimulate failures in a
sandbox](https://docs.stripe.com/payments/blik/accept-a-payment#simulate-failures)
## See also

- [More about BLIK](https://docs.stripe.com/payments/blik)
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
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [sandbox](https://docs.stripe.com/sandboxes)
- [Customers](https://docs.stripe.com/api/customers)
- [BLIK disputes](https://docs.stripe.com/payments/blik#disputed-payments)
- [More about BLIK](https://docs.stripe.com/payments/blik)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)