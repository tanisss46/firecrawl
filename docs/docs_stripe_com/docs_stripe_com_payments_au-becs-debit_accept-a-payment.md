# Accept an Australia BECS Direct Debit payment

## Learn to accept Australia BECS Direct Debit payments.

WebMobileStripe-hosted pageAdvanced integration
Stripe users in Australia can use the Payment Element and a Payment Intent to
initiate BECS Direct Debit payments from customers with an AU bank account.

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

[Determine
compatibility](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment#compatibility)
To support BECS Direct Debit payments in Checkout,
[Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Australian dollars (currency code `aud`).

[Accept a
payment](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable BECS Direct Debit—it shows the differences
between accepting a card payment and using BECS Direct Debit.

### Enable BECS Direct Debit as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `au_becs_debit` to the list of `payment_method_types`
- Make sure all your `line_items` use the `aud` currency

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'au_becs_debit'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `au_becs_debit`, all line items must have currency: aud
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
integration](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment#test-integration)
#### Note

You’ll want to use the [BECS Direct Debit test
numbers](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment#test-integration)
when testing your Checkout integration with BECS Direct Debit.

There are several test numbers you can use to make sure your integration is
ready for production.

BSB NumberAccount NumberDescription`000-000``000123456`The PaymentIntent status
transitions from `processing` to `succeeded`. The mandate status remains
`active`.`000-000``900123456`The PaymentIntent status transitions from
`processing` to `succeeded` (with a three-minute delay). The mandate status
remains `active`.`000-000``111111113`The PaymentIntent status transitions from
`processing` to `requires_payment_method` with an `account_closed` failure code.
The mandate status becomes `inactive`.`000-000``111111116`The PaymentIntent
status transitions from `processing` to `requires_payment_method` with a
`no_account` failure code. The mandate status becomes
`inactive`.`000-000``222222227`The PaymentIntent status transitions from
`processing` to `requires_payment_method` with a `refer_to_customer` failure
code. The mandate status remains `active`.`000-000``922222227`The PaymentIntent
status transitions from `processing` to `requires_payment_method` with a
`refer_to_customer` failure code (with a three-minute delay). The mandate status
remains `active`.`000-000``333333335`The PaymentIntent status transitions from
`processing` to `requires_payment_method` with a `debit_not_authorized` failure
code. The mandate status becomes `inactive`.`000-000``666666660`The
PaymentIntent status transitions from `processing` to `succeeded`, but a dispute
is immediately created.`000-000``343434343`The PaymentIntent fails with a
`charge_exceeds_source_limit` error due to the payment amount causing the
account to exceed its weekly payment volume limit.`000-000``121212121`The
PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the
payment amount exceeding the account’s transaction volume limit.[Handle refunds
and
disputes](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment#refunds-and-disputes)
The refund period for BECS Direct Debit is up to 90 days after the original
payment.

Customers can dispute a payment through their bank up to 7 years after the
original payment and there is no appeals process.

Learn more about [BECS Direct Debit
disputes](https://docs.stripe.com/payments/au-becs-debit).

## See also

- [More about BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit)
- [Managing mandates](https://docs.stripe.com/payments/au-becs-debit#mandates)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)
- [Save BECS Direct Debit details for future
payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)

## Links

- [BECS Direct Debit overview](https://docs.stripe.com/payments/au-becs-debit)
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
- [Managing mandates](https://docs.stripe.com/payments/au-becs-debit#mandates)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)
- [Save BECS Direct Debit details for future
payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)