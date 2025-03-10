# Collect tips

## Learn about the different ways you can collect tips from customers.

Use Terminal to collect tips from your customer before or after authorizing a
payment. You can collect voluntary tips in two ways:

- [On-receipt
tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt):
Tips are collected when the payment is captured. This method is most commonly
used when collecting tips on printed paper receipts.
- [On-reader
tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-reader):
The card reader suggests tips to customers before collecting payment.

For mandatory tips, you must include the tip amount in the original
`PaymentIntent`
[amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount).
You can’t use on-receipt or on-reader tipping.

## On-receipt versus on-reader tipping

The table below outlines some differences between on-receipt tipping and
on-reader tipping.

On-reader tippingOn-receipt tipping
Country

BBPOS WisePad 3:

Available in: 
Stripe Reader S700 and BBPOS WisePOS E:

Available in: 
Reader

[BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)

[BBPOS WisePOS
E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e)

[Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)

Any

Integrations/SDKs

BBPOS WisePad 3:

- Android SDK
- iOS SDK
- React Native SDK

BBPOS WisePOS E and Stripe Reader S700:

- [All SDKs,
server-driven](https://docs.stripe.com/terminal/payments/setup-reader#feature-table)

[All SDKs,
server-driven](https://docs.stripe.com/terminal/payments/setup-reader#feature-table)

Merchant categoryAnyRestrictedCard brandAnyVisa, Mastercard, American Express,
DiscoverTipping limit[Maximum charge
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
for the total amount inclusive of the tip, which is eight or nine digits
depending on the currency[Maximum charge
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
for the total amount inclusive of the tipCustomer experienceTips suggested on
the readerTips set with custom integration on the point of sale or on a paper
receiptCustomer credit card statementShows the payment amount inclusive of the
tip, without waiting for settlementShows an initial pending authorization that’s
later updated to reflect the initial amount inclusive of the tip
## How tips are displayed on-receipt or on-reader

On-receipt and on-reader tipping use the
[PaymentIntents](https://docs.stripe.com/api/payment_intents) API, work with all
[Terminal SDKs](https://docs.stripe.com/terminal/payments/setup-integration),
and require [manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).

#### Caution

Choose only one tipping method per `PaymentIntent`. If you use on-reader
tipping, you can’t use the same `PaymentIntent` for on-receipt tipping.

The table below summarizes the specific API behavior.

On-reader tippingOn-receipt tippingTips in the API requestThe reader
automatically adds the customer-selected tip when processing a payment.You add
the tip amount and pass the total
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
when [capturing a
PaymentIntent](https://docs.stripe.com/api/payment_intents/capture). The
`amount_to_capture` field is inclusive of the tip.Tips and API response
amountThe
[amount_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_details)
object appears in the API response when processing a payment. The tip amount is
returned in the `amount_details` object.Tips aren’t directly represented but can
be derived from the [Charge](https://docs.stripe.com/api/charges/object) object.
The `amount` in the `PaymentIntent` capture response is inclusive of the tip.
Tips in the underlying `Charge` object

Tips aren’t directly represented in the `Charge` object.

After capture, the fields below all show the same value inclusive of the tip.

-
[amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
-
[amount_authorized](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-amount_authorized)
-
[amount_captured](https://docs.stripe.com/api/charges/object#charge_object-amount_captured)

Tips can be derived from the `Charge` object. You can derive the tip by
subtracting `amount_authorized` from `amount`.

- `amount_authorized` is the original authorized amount exclusive of the tip.
- `amount_captured` and `amount` are the same and both are inclusive of the tip.

## Links

- [On-receipt
tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt)
- [On-reader
tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-reader)
-
[amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount)
- [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)
- [BBPOS WisePOS
E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [All SDKs,
server-driven](https://docs.stripe.com/terminal/payments/setup-reader#feature-table)
- [Maximum charge
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [Terminal SDKs](https://docs.stripe.com/terminal/payments/setup-integration)
- [manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
-
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
- [capturing a
PaymentIntent](https://docs.stripe.com/api/payment_intents/capture)
-
[amount_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_details)
- [Charge](https://docs.stripe.com/api/charges/object)
-
[amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
-
[amount_authorized](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-amount_authorized)
-
[amount_captured](https://docs.stripe.com/api/charges/object#charge_object-amount_captured)