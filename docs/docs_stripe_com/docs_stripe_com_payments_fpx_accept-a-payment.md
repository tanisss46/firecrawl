# Accept an FPX payment

## Learn how to accept FPX, a common payment method in Malaysia.

WebMobileStripe-hosted pageAdvanced integration
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

FPX is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method. Customers pay with FPX by redirecting from your website, sending
you payment, then returning to your website where you get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

[Determine
compatibility](https://docs.stripe.com/payments/fpx/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support FPX
payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
[Accept a
payment](https://docs.stripe.com/payments/fpx/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable FPX—it shows the differences between
accepting a card payment and using FPX.

### Enable FPX as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `fpx` to the list of `payment_method_types`
- Make sure all your `line_items` use the `myr` currency

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'fpx'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `fpx`, all line items must have currency: myr
 currency: 'myr',
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

### Confirmation page

FPX requires showing your customer their transaction information after they’ve
completed their payment. Follow the [custom success
page](https://docs.stripe.com/payments/checkout/custom-success-page) guide to
learn how to customize your success page.

When customizing, you’ll need to retrieve the Charge object directly from the
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
object using the PaymentIntent ID from your Checkout Session and display the
following information on your `success_url` page.

InformationSource of informationTransaction Date & Time`created` from the
`Charge` object.Amount`amount` from the `Charge` object.Seller Order
No.`statement_descriptor` from the `Charge` object.FPX Transaction
ID`payment_method_details[fpx][transaction_id]` from the `Charge` object.Buyer
Bank Name`payment_method_details[fpx][bank]` from the `Charge` objectTransaction
Status`status` from the `Charge` object[Test your
integration](https://docs.stripe.com/payments/fpx/accept-a-payment#test-integration)
When testing your Checkout integration, select FPX as the payment method and
click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/fpx/accept-a-payment#refunds-and-disputes)
The refund period for FPX is up to 60 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [More about FPX](https://docs.stripe.com/payments/fpx)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [custom success
page](https://docs.stripe.com/payments/checkout/custom-success-page)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
- [More about FPX](https://docs.stripe.com/payments/fpx)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)