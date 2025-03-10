# Incremental authorizations

## Increase the authorized amount before capturing a payment.

Incremental authorizations allow you to increase the authorized
[amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount)
on a confirmed [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
before you capture it. This is helpful if the total price changes or the
customer adds goods or services and you need to update the amount on the
payment.

Depending on the issuing bank, cardholders might see the amount of the original
pending authorization increase in place, or they might see each increment as an
additional pending authorization. After capture, the total captured amount
appears as one entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- They’re only available with Visa, Mastercard, or Discover.
- Certain card brands have merchant category restrictions (see below).
- You can only increment a transaction made with the POS and reader fully
online.
- You have a maximum of 10 attempts per payment.

#### Availability by card network and merchant category

Use incremental authorizations on payments that fulfill the criteria below. You
can find your user category in the
[Dashboard](https://dashboard.stripe.com/settings/update/company/update).

Attempting to perform an incremental authorization on a payment that doesn’t
fulfill the below criteria results in an error.

Card brandMerchant categoryVisaAll user categoriesMastercardAll user
categoriesDiscoverCar rental, hotels, local/suburban commuter, passenger
transportation, including ferries, passenger railways, bus lines-charter, tour,
steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets,
electric vehicle charging, eating places and restaurants, drinking places
(alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds,
equip/tool/furn/appl rental & leasing, automobile rental agency, truck and
utility trailer rentals, motor home and rec vehicle rentals, parking lots,
parking meters, and garages, amusement parks, circuses, fortune tell, recreation
services (not classified)[Request incremental authorization
supportServer-sideClient-side](https://docs.stripe.com/terminal/features/incremental-authorizations#request-incremental-authorization-support)
When you create a `PaymentIntent`, you can request the ability to capture
increments of the payment. Set the
[request_incremental_authorization_support](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support)
field to `true` and the
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
to `manual`. This updates the text from `Total` to `Pre-authorization` in the
payment collection screen.

Server-sideiOSAndroidReact Native
```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card_present \
 -d capture_method=manual \
-d
"payment_method_options[card_present][request_incremental_authorization_support]"=true
```

[Confirm the
PaymentIntentClient-side](https://docs.stripe.com/terminal/features/incremental-authorizations#confirm-payment-intent)
Check the
[incremental_authorization_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)
field in the confirm response to determine if the `PaymentIntent` is eligible
for incremental authorization.

You can only perform incremental authorizations on uncaptured payments after
confirmation. To adjust the amount of a payment before confirmation, use the
[update](https://docs.stripe.com/api/payment_intents/update) method instead.

JavaScriptiOSAndroidReact Native
```
async () => {
 const result = await terminal.processPayment(paymentIntent);
 if (result.error) {
 // Placeholder for handling result.error
 } else if (result.paymentIntent) {
 // Now you're ready to increment the authorization using your backend
 }
}
```

[Perform an incremental
authorizationServer-side](https://docs.stripe.com/terminal/features/incremental-authorizations#increment-authorization)
To increase the authorized amount on a payment, use the
[increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization)
endpoint and provide the updated total
[amount](https://docs.stripe.com/api/payment_intents/increment_authorization#increment_authorization-amount)
to increment to, which must be greater than the original authorized amount. This
attempts to authorize for the difference between the previous amount and the
incremented amount. Each `PaymentIntent` can have a maximum of 10 incremental
authorization attempts, including declines.

A single `PaymentIntent` can call this endpoint multiple times to further
increase the authorized amount.

```
curl
https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/increment_authorization
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1500
```

An authorization can either:

- Succeed – Returns the `PaymentIntent` with the updated amount.
- Fail – Returns a
[card_declined](https://docs.stripe.com/error-codes#card-declined) error, and
the `PaymentIntent` remains authorized to capture the original amount. Updates
to other `PaymentIntent` fields (for example,
[application_fee_amount](https://docs.stripe.com/api/payment_intents/increment_authorization#increment_authorization-application_fee_amount))
aren’t saved.
[Capture the
PaymentIntentServer-side](https://docs.stripe.com/terminal/features/incremental-authorizations#capture-payment-intent)
To capture the authorized amount on a `PaymentIntent` that has prior incremental
authorizations, use the
[capture](https://docs.stripe.com/api/payment_intents/capture) endpoint. To
increase the authorized amount and simultaneously capture that updated amount,
provide an updated
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture).

Providing an `amount_to_capture` that’s higher than the currently authorized
amount results in an automatic incremental authorization attempt.

#### Note

If you’re eligible to [collect on-receipt
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt),
using an `amount_to_capture` that’s higher than the currently authorized amount
won’t result in an automatic incremental authorization attempt. Capture requests
always succeed.

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount_to_capture=2000
```

The possible outcomes of an incremental authorization attempt are:

- Succeed – Returns the `captured` `PaymentIntent` with the updated amount.
- Fail – Returns a
[card_declined](https://docs.stripe.com/error-codes#card-declined) error, and
the `PaymentIntent` remains authorized to capture the original amount. Updates
to other `PaymentIntent` fields (for example,
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount))
aren’t saved.

Regardless, when using `amount_to_capture` we recommend that you always check
for potential failures.

## Links

-
[amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Dashboard](https://dashboard.stripe.com/settings/update/company/update)
-
[request_incremental_authorization_support](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support)
-
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
-
[incremental_authorization_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)
- [update](https://docs.stripe.com/api/payment_intents/update)
-
[increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization)
-
[amount](https://docs.stripe.com/api/payment_intents/increment_authorization#increment_authorization-amount)
- [card_declined](https://docs.stripe.com/error-codes#card-declined)
-
[application_fee_amount](https://docs.stripe.com/api/payment_intents/increment_authorization#increment_authorization-application_fee_amount)
- [capture](https://docs.stripe.com/api/payment_intents/capture)
-
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
- [collect on-receipt
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt)
-
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount)