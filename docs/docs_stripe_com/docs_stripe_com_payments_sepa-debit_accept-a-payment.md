# Accept a SEPA Direct Debit payment

## Learn to accept SEPA Direct Debit payments.

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

Accepting SEPA Direct Debit payments on your website consists of creating an
object to track a payment, collecting payment method information and mandate
acknowledgement, and submitting the payment to Stripe for processing. Stripe
uses this payment object, the PaymentIntent, to track and handle all the states
of the payment until the payment completes.

#### Note

SEPA Direct Debit is a **delayed notification payment method**, which means that
funds are not immediately available after payment. A payment typically takes **5
business days** to arrive in your account.

[Determine
compatibility](https://docs.stripe.com/payments/sepa-debit/accept-a-payment#compatibility)
To support SEPA Direct Debit payments in Checkout,
[Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Euro (currency code `eur`).

[Accept a
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
Checkout integration.

Use this guide to learn how to enable SEPA Direct Debit—it shows the differences
between accepting a card payment and using SEPA Direct Debit.

### Enable SEPA Direct Debit as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `sepa_debit` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `eur` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'sepa_debit'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `sepa_debit`, all line items must have currency: eur
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
integration](https://docs.stripe.com/payments/sepa-debit/accept-a-payment#test-integration)
Stripe provides several test numbers you can use to make sure your integration
is ready for production.

Use the [SEPA Direct Debit test
numbers](https://docs.stripe.com/payments/sepa-debit/accept-a-payment#test-integration)
when testing your Checkout integration with SEPA Direct Debit.

##### Test IBANs

AustriaBelgiumCroatiaEstoniaFinlandFranceGermanyGibraltarIrelandLiechtensteinLithuaniaLuxembourgNetherlandsNorwayPortugalSpainSwedenSwitzerlandUnited
KingdomAccount NumberDescription`AT611904300234573201`The PaymentIntent status
transitions from `processing` to `succeeded`.`AT321904300235473204`The
PaymentIntent status transitions from `processing` to `succeeded` after at least
three minutes.`AT861904300235473202`The PaymentIntent status transitions from
`processing` to `requires_payment_method`.`AT051904300235473205`The
PaymentIntent status transitions from `processing` to `requires_payment_method`
after at least three minutes.`AT591904300235473203`The PaymentIntent status
transitions from `processing` to `succeeded`, but a dispute is immediately
created.`AT981904300000343434`The payment fails with a
`charge_exceeds_source_limit` failure code due to payment amount causing account
to exceed its weekly payment volume limit.`AT601904300000121212`The payment
fails with a `charge_exceeds_weekly_limit` failure code due to payment amount
exceeding account's transaction volume limit.[Handle refunds and
disputes](https://docs.stripe.com/payments/sepa-debit/accept-a-payment#refunds-and-disputes)
The refund period for SEPA Direct Debit is up to 180 days after the original
payment.

[Customers](https://docs.stripe.com/api/customers) can dispute a payment through
their bank up to 13 months after the original payment and there’s no appeal
process.

Learn more about [SEPA Direct Debit
disputes](https://docs.stripe.com/payments/sepa-debit#disputed-payments).

[OptionalCustomize mandate references with a
prefix](https://docs.stripe.com/payments/sepa-debit/accept-a-payment#mandate-reference-prefix)
## See also

- [Save SEPA Direct Debit details for future
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Customers](https://docs.stripe.com/api/customers)
- [SEPA Direct Debit
disputes](https://docs.stripe.com/payments/sepa-debit#disputed-payments)
- [Save SEPA Direct Debit details for future
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)