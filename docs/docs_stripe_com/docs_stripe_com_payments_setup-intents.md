# The Setup Intents API

## Learn more about the Setup Intents API for saving payment methods.

Use the [Setup Intents API](https://docs.stripe.com/api/setup_intents) to set up
a payment method for future payments. It’s similar to a payment, but no charge
is created. [Set up a payment method for future payments
now](https://docs.stripe.com/payments/save-and-reuse).

The goal is to have payment credentials saved and optimized for future payments,
meaning the payment method is configured correctly for any scenario. When
setting up a card, for example, it may be necessary to authenticate the customer
or check the card’s validity with the customer’s bank. Stripe updates the
`SetupIntent` object throughout that process.

![UI that collects card details but does not charge the
card](https://b.stripecdn.com/docs-statics-srv/assets/reuse-si.2499c9ffdcfc8bd5d430e9a1809890bf.svg)

## Saving and reusing payment methods

The Setup Intents API is useful for businesses that onboard customers but don’t
charge them right away:

- A car rental company that collects payment method details before the customer
rents the car and charges the card after the rental period ends
- A crowdfunding website that collects card details to be charged later, only if
the campaign reaches a certain amount
- A utility company that charges a different amount each month based on usage
but collects SEPA payment details before the first month’s payment

#### Note

You can set up payment methods for future use with
[Checkout](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
too.

#### Get started

- [Save cards without making an initial
payment](https://docs.stripe.com/payments/save-and-reuse)
- [Save bank details for SEPA Direct Debit
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment)
- [Save bank details for BECS Direct Debit
payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment)

## Getting permission to save a payment method

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. If you set up a
payment method for future on-session payments, such as displaying the payment
method on a future checkout page, make sure that you explicitly collect consent
from the customer for this specific use. For example, include a “Save my payment
method for future use” checkbox to collect consent. If you need to differentiate
between payment methods saved only for offline usages and payment methods you
can present to your customer for future on-session purchases, you can utilize
the
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
parameter on the PaymentMethod object.

If you set up a payment method for future off-session payments, you need
permission. Creating an agreement (sometimes called a *mandate*) up front allows
you to charge the customer when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to process payments,
and let customers opt in. At a minimum, ensure that your terms cover the
following:

- The customer’s permission to your initiating a payment or a series of payments
on their behalf
- The anticipated frequency of payments (that is, one-time or recurring)
- How the payment amount will be determined

See recommended mandate text for [saving
cards](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#collect-payment-details)
or [saving SEPA bank
details](https://docs.stripe.com/payments/sepa-debit/set-up-payment).

For users impacted by
[SCA](https://docs.stripe.com/strong-customer-authentication), this agreement
helps payments succeed without interruption. When you set up your integration to
properly save a card, Stripe marks any subsequent off-session payment as a
[merchant-initiated
transaction](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)
(MIT) so that your customers don’t have to come back online and authenticate.
Merchant-initiated transactions require an agreement between you and your
customer.

## Increasing success rate by specifying usage

The
[usage](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage)
parameter tells Stripe how you plan to use payment method details later. For
some payment methods, Stripe can use your `usage` setting to pick the most
frictionless flow for the customer. This optimization is designed to increase
the number of successful payments.

For example, credit and debit cards under European
[SCA](https://docs.stripe.com/strong-customer-authentication) regulation may
require the customer to authenticate the card during the saving process. Setting
`usage` to `off_session` properly authenticates a credit or debit card for
off-session payments so that your customer doesn’t have to come back online and
re-authenticate. So although it creates initial friction in the setup flow,
setting `usage` to `off_session` can reduce customer intervention in later
off-session payments.

However, if you only plan to use the card when the customer is checking out, set
`usage` to `on_session`. This lets the bank know you plan to use the card when
the customer is available to authenticate, so you can postpone authenticating
the card details until then and avoid upfront friction.

How you intend to use the cardusage enum value to useOn-session payments
only`on_session`Off-session payments only`off_session` (default)Both on and
off-session payments`off_session` (default)
`Usage` is an optimization. You can still use a card that’s set up for
on-session payments to make off-session payments, but banks are more likely to
reject the off-session payment and require authentication from the customer.
Either case might still require later authentication, so [build a recovery
process](https://docs.stripe.com/billing/revenue-recovery) in your app. When an
off-session card payment requires authentication, bring your customer back
online to complete the payment.

If not specified, `usage` defaults to `off_session`. See how to create a
SetupIntent on your server and specify the `usage`:

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d usage=on_session
```

#### Note

Follow the guidance on this page to ensure your integration handles cards that
require [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication).
Correctly flagging transactions allows Stripe to claim correct SCA exemptions on
your behalf to minimize the need for authentication with each payment.

## Links

- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [Set up a payment method for future payments
now](https://docs.stripe.com/payments/save-and-reuse)
- [Checkout](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [Save bank details for SEPA Direct Debit
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment)
- [Save bank details for BECS Direct Debit
payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment)
-
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
- [saving
cards](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#collect-payment-details)
- [SCA](https://docs.stripe.com/strong-customer-authentication)
- [merchant-initiated
transaction](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)
-
[usage](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage)
- [build a recovery process](https://docs.stripe.com/billing/revenue-recovery)