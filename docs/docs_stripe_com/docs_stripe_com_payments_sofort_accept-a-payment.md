# Accept a Sofort payment

## Learn how to accept Sofort, a common payment method in Europe.

#### Warning

New businesses can’t accept SOFORT payments and our financial partners are in
the process of discontinuing SOFORT. For more information, read our [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method).

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

#### Note

SOFORT is a **delayed notification payment method**, which means that funds are
not immediately available after payment. A payment typically takes **2 to 14
business days** to arrive in your account.

Customers pay with SOFORT by redirecting away from the Checkout Session to their
bank, sending you payment, and then returning to Checkout. they’re then
redirected back to your site.

[Determine
compatibility](https://docs.stripe.com/payments/sofort/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
SOFORT payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Euro (currency code `eur`).
[Accept a
payment](https://docs.stripe.com/payments/sofort/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable SOFORT—it shows the differences between
accepting a card payment and using SOFORT.

### Enable SOFORT as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `sofort` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `eur` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'sofort'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `sofort`, all line items must have currency: eur
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
integration](https://docs.stripe.com/payments/sofort/accept-a-payment#test-integration)
When testing your Checkout integration, select SOFORT as the payment method and
click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/sofort/accept-a-payment#refunds-and-disputes)
The refund period for SOFORT is up to 180 days after the original payment.

There is no dispute process–customers authenticate with their bank.

## Links

- [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)
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