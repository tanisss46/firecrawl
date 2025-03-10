# Use iDEAL to set up future SEPA Direct Debit payments

## Learn how to save bank details from an iDEAL payment and charge your customers later with SEPA Direct Debit.

#### Caution

We recommend that you follow the [Set up future
payments](https://docs.stripe.com/payments/save-and-reuse) guide. If you’ve
already integrated with Elements, see the [Payment Element migration
guide](https://docs.stripe.com/payments/payment-element/migration).

iDEAL is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
each payment. With this integration, Stripe charges your customer 0.01 EUR
through iDEAL to collect their bank details. After your customer authenticates
the payment, Stripe refunds the payment and stores your customer’s
[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) in a
[SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit) payment method.
You can then use the SEPA Direct Debit
[PaymentMethod](https://docs.stripe.com/api/payment_methods) to [accept
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment) or [set
up a subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit).

#### Caution

To use iDEAL to set up SEPA Direct Debit payments, you must activate SEPA Direct
Debit in the
[Dashboard](https://dashboard.stripe.com/account/payments/settings). You must
also comply with the [iDEAL Terms of Service](https://stripe.com/ideal/legal)
and [SEPA Direct Debit Terms of
Service](https://stripe.com/sepa-direct-debit/legal).

Stripe-hosted pageAdvanced integrationiOSAndroidReact Native
You can use [Checkout in setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout) to
collect payment details and set up future SEPA Direct Debit payments using
iDEAL.

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/ideal/set-up-payment#create-retrieve-customer)
To set up future SEPA Direct Debit payments using iDEAL, you must attach the
SEPA Direct Debit payment method to a
[Customer](https://docs.stripe.com/api/customers).

Create a `Customer` object when your customer creates an account with your
business. You can retrieve and use a customer’s stored payment method details
later, if you associate the ID of the `Customer` object with your own internal
representation of the customer.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Set up future
payments](https://docs.stripe.com/payments/ideal/set-up-payment#setup-a-payment)
This guide builds on the foundational [set up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
Checkout integration and describes how to enable iDEAL—it shows the differences
between setting up future payments for cards and using iDEAL.

### Enable iDEAL as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to add `ideal`
to the list of `payment_method_types`.

```
Stripe::Checkout::Session.create({
 mode: 'setup',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'ideal'],
 customer: customer.id,
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

[Charge the SEPA Direct Debit PaymentMethod
laterServer-side](https://docs.stripe.com/payments/ideal/set-up-payment#charge-sepa-pm)
When you need to charge your customer again, create a new PaymentIntent. Find
the ID of the SEPA Direct Debit payment method by
[retrieving](https://docs.stripe.com/api/setup_intents/retrieve) the SetupIntent
and [expanding](https://docs.stripe.com/api/expanding_objects) the
`latest_attempt` field where you will find the `generated_sepa_debit` ID inside
of `payment_method_details`.

```
curl -G https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=latest_attempt
```

Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=sepa_debit \
 -d amount=1099 \
 -d currency=eur \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{SEPA_DEBIT_PAYMENT_METHOD_ID}} \
 -d confirm=true
```

[Test your
integration](https://docs.stripe.com/payments/ideal/set-up-payment#testing)
Using your [test API keys](https://docs.stripe.com/keys#test-live-modes), select
any bank from the list. After confirming, you’re redirected to a test page with
options to authorize or fail the payment method setup.

- Click **Authorize test payment** to test the case when the setup is
successful.
- Click **Fail test payment** to test the case when the customer fails to
authenticate.

## See also

- [Accept a SEPA Direct Debit
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Set up a subscription with SEPA Direct Debit in the
EU](https://docs.stripe.com/billing/subscriptions/sepa-debit)

## Links

- [Save bank details during
payment](https://docs.stripe.com/payments/ideal/save-during-payment)
- [Set up future payments](https://docs.stripe.com/payments/save-and-reuse)
- [Payment Element migration
guide](https://docs.stripe.com/payments/payment-element/migration)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [accept
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [set up a
subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [iDEAL Terms of Service](https://stripe.com/ideal/legal)
- [SEPA Direct Debit Terms of
Service](https://stripe.com/sepa-direct-debit/legal)
- [Checkout in setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [retrieving](https://docs.stripe.com/api/setup_intents/retrieve)
- [expanding](https://docs.stripe.com/api/expanding_objects)
- [test API keys](https://docs.stripe.com/keys#test-live-modes)