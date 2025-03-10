# Accept a payment via local bank transfers in NigeriaPrivate preview

Stripe-hosted pageDirect API
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

Integrating with Naira bank transfer enables Nigerian customers to pay using a
local bank transfer.

Stripe’s merchant of record service provider offers a redirect-based payment
flow for local bank transfers (also known locally as “Transfers”). When a
customer makes a payment, Stripe redirects them to the local merchant of record
service provider’s checkout flow to authenticate and authorize the payment.
After the customer authorizes the payment, Stripe redirects them back to your
site.

[Determine
compatibility](https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment#compatibility)
[A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works#session)
must satisfy all of the following conditions to support Nigerian payment
methods:

- Express [prices](https://docs.stripe.com/api/prices) for all line items in
Nigerian naira (currency code `ngn`).
- The transaction amount must be between 500 NGN and 100,000,000 NGN.
[Accept a Naira bank transfer
payment](https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment#accept-a-ng-bank-transfer-payment)
To enable Naira bank transfer, update your integration to:

- Add `ng_bank_transfer` to the list of `payment_method_types` when you create a
[Checkout Session](https://docs.stripe.com/api/checkout/sessions).
- Make sure all `line_items` use the `ngn` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'ng_bank_transfer'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `ng_bank_transfer`, all line items must have currency: ngn
 currency: 'ngn',
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

[Test your
integration](https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment#test-integration)
When testing your Checkout integration, select **Nigerian payment methods** as
the payment method and click **Pay**.

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [A Checkout
Session](https://docs.stripe.com/payments/checkout/how-checkout-works#session)
- [prices](https://docs.stripe.com/api/prices)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)