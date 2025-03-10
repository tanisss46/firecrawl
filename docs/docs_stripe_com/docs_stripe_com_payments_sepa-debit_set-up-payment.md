# Save SEPA Direct Debit details for future payments

## Learn how to save payment method details for future SEPA Direct Debit payments.

Stripe-hosted pageAdvanced integrationReact Native
You can use [Checkout in setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout) to
collect SEPA Direct Debit payment details in advance, and determine the final
amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- [Starting a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)

#### Note

SEPA Direct Debit is a **delayed notification payment method**, which means that
funds are not immediately available after payment. A payment typically takes **5
business days** to arrive in your account.

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/sepa-debit/set-up-payment#create-retrieve-customer)
To reuse a SEPA Direct Debit payment method for future payments, it must be
attached to a [Customer](https://docs.stripe.com/api/customers).

Create a Customer object when your customer creates an account with your
business. Associating the ID of the Customer object with your own internal
representation of a customer enables you to retrieve and use the stored payment
method details later.

Create a new customer or retrieve an existing customer to associate with this
payment. Include the following code on your server to create a new customer.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Set up future
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment#setup-a-payment)
#### Note

This guide builds on the foundational [set up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
Checkout integration.

Use this guide to learn how to enable SEPA Direct Debit—it shows the differences
between setting up future payments for cards and using SEPA Direct Debit.

### Enable SEPA Direct Debit as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to add
`sepa_debit` to the list of `payment_method_types`.

```
Stripe::Checkout::Session.create({
 mode: 'setup',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'sepa_debit'],
 customer: customer.id,
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

[Test your
integration](https://docs.stripe.com/payments/sepa-debit/set-up-payment#testing)
You can test your integration using the IBANs below. The payment method details
are successfully collected for each IBAN but exhibit different behavior when
charged.

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
exceeding account's transaction volume limit.[OptionalCustomize mandate
references with a
prefix](https://docs.stripe.com/payments/sepa-debit/set-up-payment#mandate-reference-prefix)
## See also

- [Manually configure SEPA Direct Debit as a
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)

## Links

- [Checkout in setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [Start a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [Manually configure SEPA Direct Debit as a
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)