# Previous authorization agreements

## Learn which payments previous authorization agreements can be used for (sometimes referred to as grandfathering).

#### Warning

If you’re affected by SCA, [update your Stripe
integration](https://docs.stripe.com/strong-customer-authentication#preparing)
now, even if some of your payments can use previous authorization agreements.

## Eligibility

[Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) requires
an additional step of customer authentication, but sometimes you collect
payments when your customer isn’t actively using your application. Even if they
authenticated in the past, SCA may require your customer to come back online and
re-authenticate. To reduce friction in these off-session payments, Stripe APIs
enable upfront authentication—so you can authenticate your customer on-session
once and reuse the card off-session repeatedly. As of September 14, 2019, you
need to use these APIs to reduce the chance of failed payments when [reusing
cards](https://docs.stripe.com/payments/save-and-reuse) or [creating
subscriptions and
invoices](https://docs.stripe.com/billing/migration/strong-customer-authentication).

However, you can use previous authorization agreements for off-session payments
that meet the following criteria:

- Cards from EU customers saved before December 31, 2020
- Cards from UK customers saved before September 14, 2021

This means you don’t have to use Stripe’s new APIs to set up saved cards again,
and your off-session payments can proceed normally—without re-authentication
from customers.

## How it works

You can use previous authorization agreements for all off-session payments that
meet both of these conditions, regardless of payment amount and frequency:

- You saved the card details before the
[eligibility](https://docs.stripe.com/strong-customer-authentication/previous-authorization-agreements#eligibility)
cutoff
- You explicitly tell Stripe the transaction is off-session

Stripe automatically looks for a transaction made with the card prior to the
eligibility cutoff. If found, Stripe uses the previous authorization agreement
for the current transaction. If the bank accepts the previous authorization
agreement, the transaction is categorized as out of scope for SCA and can
proceed without additional authentication.

If the bank declines the previous authorization agreement, it’s like any other
PaymentIntent failing the confirmation step. The PaymentIntent’s [status
changes](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)
to [requires_payment_method](https://docs.stripe.com/upgrades#2019-02-11), and
you have to [notify your customer to complete the
payment](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method).

## Saving cards after the eligibility period

Now that SCA has taken effect, [save and reuse
cards](https://docs.stripe.com/payments/save-and-reuse) with the Payment Intents
and [Setup Intents APIs](https://docs.stripe.com/api/setup_intents) to qualify
for off-session exemptions. You can also save cards using [Stripe
Checkout](https://docs.stripe.com/payments/save-and-reuse?platform=checkout).

## Preparing your saved cards for SCA

For Stripe to reuse authorization agreements, you need to use PaymentIntents and
tell Stripe the payment is off-session.

How you saved the card before the eligibility cutoffWhat to do after the
eligibility periodBy passing a [token](https://docs.stripe.com/saving-cards),
[source](https://docs.stripe.com/sources/cards), or [payment
method](https://docs.stripe.com/payments/save-during-payment) to the
`Customer`Create a PaymentIntent with [off-session
flag](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)By
creating a [SetupIntent](https://docs.stripe.com/payments/save-and-reuse) or
using
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
in a PaymentIntentCreate a PaymentIntent with [off-session
flag](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)
For [subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
[invoices](https://docs.stripe.com/api/invoices) managed with Stripe Billing,
refer to the [Billing SCA
guide](https://docs.stripe.com/billing/migration/strong-customer-authentication#previous-agreements).

## See also

- [Payment Intents Overview](https://docs.stripe.com/payments/payment-intents)
- [Payment Intents Migration
Guide](https://docs.stripe.com/payments/payment-intents/migration)

## Links

- [update your Stripe
integration](https://docs.stripe.com/strong-customer-authentication#preparing)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [reusing cards](https://docs.stripe.com/payments/save-and-reuse)
- [creating subscriptions and
invoices](https://docs.stripe.com/billing/migration/strong-customer-authentication)
- [status
changes](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)
- [requires_payment_method](https://docs.stripe.com/upgrades#2019-02-11)
- [Setup Intents APIs](https://docs.stripe.com/api/setup_intents)
- [Stripe
Checkout](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [token](https://docs.stripe.com/saving-cards)
- [source](https://docs.stripe.com/sources/cards)
- [payment method](https://docs.stripe.com/payments/save-during-payment)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoices](https://docs.stripe.com/api/invoices)
- [Billing SCA
guide](https://docs.stripe.com/billing/migration/strong-customer-authentication#previous-agreements)
- [Payment Intents Overview](https://docs.stripe.com/payments/payment-intents)
- [Payment Intents Migration
Guide](https://docs.stripe.com/payments/payment-intents/migration)