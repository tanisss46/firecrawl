# Migrate to the latest flexible payment scenarios

## Adapt your beta advanced payment scenarios to the general release.

Stripe now supports several flexible payment scenarios for non-card-present
transactions. If you’ve already integrated the private beta version of any of
these features, this guide provides details to upgrade to the general release.
For new integrations, use the following guides for the features that interest
you:

- [Increment an
Authorization](https://docs.stripe.com/payments/incremental-authorization)
- [Capture more than the Authorized
Amount](https://docs.stripe.com/payments/overcapture)
- [Place an Extended Hold on an Online Card
Payment](https://docs.stripe.com/payments/extended-authorization)
- [Capture a Payment Multiple
Times](https://docs.stripe.com/payments/multicapture)

We’ve incorporated the following feedback-driven improvements to these features:

- Detailed control over the features at the
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) level.
- Clearer expectations regarding feature availability and usage after a
[confirmation](https://docs.stripe.com/api/payment_intents/confirm) phase.

Each of the flexible payment features has different requirements from its
private beta integration. Choose the feature you need to upgrade and refer to
the note at the top for changes and requirements specific to that feature.

Incremental authorizationOvercaptureExtended authorizationMulticapture
#### Changes from beta

The first step of this integration is now mandatory.

[Request incremental
authorization](https://docs.stripe.com/payments/flexible-features-migration#request-incremental-auth)
Your [PaymentIntent](https://docs.stripe.com/payments/payment-intents) must
include a request for incremental authorization before confirmation.

#### Warning

This formerly optional step is now mandatory.

BeforeAfter
```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d payment_method=pm_card_debit_incrementalAuthAuthorized \
 -d confirm=true \
 -d capture_method=manual \
 -d "expand[]"=latest_charge \
-d
"payment_method_options[card][request_incremental_authorization_support]"=true
```

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d payment_method=pm_card_debit_incrementalAuthAuthorized \
 -d confirm=true \
 -d capture_method=manual \
 -d "expand[]"=latest_charge \
-d
"payment_method_options[card][request_incremental_authorization]"=if_available
```

The response now returns the status of the incremental authorization request in
the `payment_method_details.card.incremental_authorization.status` property of
the [latest_charge](https://docs.stripe.com/api/charges/object). The status
values is `available` or `unavailable` depending on the customer’s payment
method.

BeforeAfter
```
// PaymentIntent Response
{
 "id": "pi_ANipwO3zNfjeWODtRPIg",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 1000,
 "amount_received": 0,
 ...
 // if latest_charge is expanded
 {
 "latest_charge": {
 "amount": 1000,
 "payment_method_details": {
 "card": {
 "incremental_authorization_supported": true // or false
 }
 }
 ...
 }
 }
}
```

```
// PaymentIntent Response
{
 "id": "pi_ANipwO3zNfjeWODtRPIg",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 1000,
 "amount_received": 0,
 ...
 // if latest_charge is expanded
 {
 "latest_charge": {
 "amount": 1000,
 "payment_method_details": {
 "card": {
 "incremental_authorization": {
 "status": "available" // or "unavailable"
 }
 }
 }
 ...
 }
 }
}
```

[Incrementally modify the authorized
amount](https://docs.stripe.com/payments/flexible-features-migration#use-incremental-auth)
**No changes have been made to this step in comparison to the beta version.**

```
curl
https://api.stripe.com/v1/payment_intents/pi_ANipwO3zNfjeWODtRPIg/increment_authorization
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1500
```

## Choose how to capture more than initially authorized amount

Two of the flexible payment features allow you to capture an amount larger than
initially authorized:

- Over capture up to a certain limit ([Capture more than the authorized amount
on a payment](https://docs.stripe.com/payments/overcapture))
- Increment the existing authorization and then capture the newly authorized
amount ([Increment an
authorization](https://docs.stripe.com/payments/incremental-authorization))

The example below showcases how these features can complement each other in the
generally available version.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d payment_method=pm_card_visa \
 -d confirm=true \
 -d capture_method=manual \
 -d "expand[]"=latest_charge \
-d
"payment_method_options[card][request_incremental_authorization]"=if_available \
 -d "payment_method_options[card][request_overcapture]"=if_available
```

```
// PaymentIntent Response
{
 "object": "payment_intent",
 "amount": 1000,
 ...
 // if latest_charge is expanded
 {
 "latest_charge": {
 "payment_method_details": {
 "card": {
 "incremental_authorization": {
 "status": "available" // or "unavailable"
 },
 "overcapture": {
 "status": "available", // or "unavailable"
 "maximum_capturable_amount": 1200
 }
 }
 }
 ...
 }
 }
}
```

Upon [confirmation](https://docs.stripe.com/api/payment_intents/confirm) of the
PaymentIntent, if both features are available, you have options on the next
steps to capture a larger amount than initially authorized:

- Overcapture if the desired amount is equal or below the
`maximum_capturable_amount`.
- Perform an incremental authorization to the desired amount, then capture.

## Links

- [Increment an
Authorization](https://docs.stripe.com/payments/incremental-authorization)
- [Capture more than the Authorized
Amount](https://docs.stripe.com/payments/overcapture)
- [Place an Extended Hold on an Online Card
Payment](https://docs.stripe.com/payments/extended-authorization)
- [Capture a Payment Multiple
Times](https://docs.stripe.com/payments/multicapture)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [confirmation](https://docs.stripe.com/api/payment_intents/confirm)
- [latest_charge](https://docs.stripe.com/api/charges/object)