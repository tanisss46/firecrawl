# Older payment APIs

## Information about our older APIs and the newer APIs that replace them.

We’ve replaced some of our older APIs and no longer update their documentation.

## Migrate to current APIs

The older APIs are limited. To get the latest Stripe features, migrate to the
[Payment Intents](https://docs.stripe.com/payments/payment-intents), [Setup
Intents](https://docs.stripe.com/payments/setup-intents), and [Payment
Methods](https://docs.stripe.com/payments/payment-methods) APIs. See each
individual API’s docs for specifics on migrating.

## Deprecation of the Sources API

We’ve deprecated support for local payment methods in the [Sources
API](https://docs.stripe.com/sources) and plan to turn it off. If you currently
handle any local payment methods using the Sources API, you must [migrate them
to the current
APIs](https://docs.stripe.com/payments/payment-methods/transitioning). We’ll
communicate more information about this end of support via email.

We’ve also deprecated support for card payments in the Sources API, but don’t
currently plan to turn it off.

## Older APIs that remain available

Although unsupported, these APIs aren’t going away. Until you upgrade your
integration, you can still use these APIs:

- [Charges](https://docs.stripe.com/payments/charges-api)
- [ACH](https://docs.stripe.com/ach-deprecated)

## Comparing the APIs

Feature Payment Intents, Setup Intents, & Payment MethodsCharges, Tokens, &
SourcesSupported payment methods[Cards, digital wallets, bank transfers, and so
on](https://docs.stripe.com/payments/payment-methods/overview)Cards,
ACH[SCA-ready](https://docs.stripe.com/strong-customer-authentication)Works with
[Terminal](https://docs.stripe.com/terminal) (in-person payments)Future
development

## Links

- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [Setup Intents](https://docs.stripe.com/payments/setup-intents)
- [Payment Methods](https://docs.stripe.com/payments/payment-methods)
- [Sources API](https://docs.stripe.com/sources)
- [migrate them to the current
APIs](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Charges](https://docs.stripe.com/payments/charges-api)
- [ACH](https://docs.stripe.com/ach-deprecated)
- [Cards, digital wallets, bank transfers, and so
on](https://docs.stripe.com/payments/payment-methods/overview)
- [SCA-ready](https://docs.stripe.com/strong-customer-authentication)
- [Terminal](https://docs.stripe.com/terminal)