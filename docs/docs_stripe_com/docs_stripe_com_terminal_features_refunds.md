# Refund transactions

## Cancel or refund Stripe Terminal payments.

Stripe Terminal supports both automatic and manual capture.

When the SDK returns a confirmed PaymentIntent to your app, the payment is
authorized but not
[captured](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment).
You can
[cancel](https://docs.stripe.com/terminal/features/refunds#canceling-payments)
payments that are authorized and not captured. If the PaymentIntent has already
been captured, you must
[refund](https://docs.stripe.com/terminal/features/refunds#refunds) the
underlying charge created by the PaymentIntent, using the [refunds
API](https://docs.stripe.com/api#create_refund) or
[Dashboard](https://docs.stripe.com/refunds?dashboard-or-api=dashboard).

We recommend [reconciling
payments](https://docs.stripe.com/terminal/payments/collect-card-payment#reconciling)
on your backend after a day’s activity to prevent unintended authorizations and
uncollected funds.

## Availability

**Canceling payments** is available on Visa, Mastercard, American Express,
Discover, and girocard. For single-message payment methods like
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)
and
[eftpos](https://docs.stripe.com/terminal/payments/regional?integration-country=AU#eftpos-payments),
PaymentIntents are automatically captured. In lieu of canceling PaymentIntents,
make sure your application can allow initiating a refund at the end of the
checkout flow.

**Online refunds** are available on all card networks except for Interac.

[In-person
refunds](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#refund-an-interac-payment)
are only available on Interac.

## Cancel payments Client-sideServer-side

You can [cancel](https://docs.stripe.com/api#cancel_payment_intent) a
`card_present` PaymentIntent at any time before it has been captured. Canceling
a PaymentIntent releases all uncaptured funds, and a canceled PaymentIntent can
no longer be used to perform charges.

Use this when, for example, your customer decides to use a different payment
method or pay with cash after the payment has been processed. In your
application’s UI, consider allowing the user to cancel after they [confirm the
payment](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment),
and before you finalize it and notify your backend to
[capture](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment).

#### Client-side

Cancel a `PaymentIntent` from your client using the iOS, Android, or React
Native SDK:

Server-drivenJavaScriptiOSAndroidReact Native
#### Note

Client-side `PaymentIntent` cancellation is possible with the iOS, Android, and
React Native SDKs. If you’re using a server-driven integration, cancel the
`PaymentIntent` server-side.

#### Server-side

The JavaScript SDK and server-driven integration require you to cancel the
`PaymentIntent` on your server. For the other client SDKs, you can cancel the
`PaymentIntent` on your server if the information required to start a payment
isn’t readily available in your app.

```
curl -X POST
https://api.stripe.com/v1/payment_intents/pi_ANipwO3zNfjeWODtRPIg/cancel \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Perform refunds Server-side

When you use a PaymentIntent to collect payment from a customer, Stripe creates
a [charge](https://docs.stripe.com/api/charges/object) behind the scenes. To
refund the customer’s payment after the PaymentIntent has succeeded, [create a
refund](https://docs.stripe.com/api#create_refund) by passing in the
PaymentIntent ID or the charge ID. You can also optionally refund part of a
payment by specifying an amount.

You can perform refunds [with the
API](https://docs.stripe.com/refunds?dashboard-or-api=api) or [through the
Dashboard](https://docs.stripe.com/refunds?dashboard-or-api=dashboard). For
Interac transactions in Canada, the BBPOS WisePOS E reader and Stripe Reader
S700 support [in-person
refunds](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#refund-an-interac-payment)
instead.

Online refunds don’t require a cardholder to present their card again at the
point of sale. The following example shows how to create a full refund by
passing in the PaymentIntent ID.

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent=pi_Aabcxyz01aDfoo
```

To refund part of a PaymentIntent, provide an `amount` parameter, as an integer
in cents (or the charge currency’s smallest currency unit):

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent=pi_Aabcxyz01aDfoo \
 -d amount=1000
```

## See also

- [Cart display](https://docs.stripe.com/terminal/features/display)
- [Receipts](https://docs.stripe.com/terminal/features/receipts)

## Links

-
[captured](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment)
- [refunds API](https://docs.stripe.com/api#create_refund)
- [Dashboard](https://docs.stripe.com/refunds?dashboard-or-api=dashboard)
- [reconciling
payments](https://docs.stripe.com/terminal/payments/collect-card-payment#reconciling)
-
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)
-
[eftpos](https://docs.stripe.com/terminal/payments/regional?integration-country=AU#eftpos-payments)
- [In-person
refunds](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#refund-an-interac-payment)
- [cancelPaymentIntent
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)cancelPaymentIntent:completion:)
- [cancelPaymentIntent
(Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/cancel-payment-intent.html)
- [cancelPaymentIntent (React
Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelPaymentIntent)
- [cancelPaymentIntent
(Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/cancel-payment-intent.html)
- [cancel](https://docs.stripe.com/api#cancel_payment_intent)
- [confirm the
payment](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment)
- [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel)
- [charge](https://docs.stripe.com/api/charges/object)
- [with the API](https://docs.stripe.com/refunds?dashboard-or-api=api)
- [Cart display](https://docs.stripe.com/terminal/features/display)
- [Receipts](https://docs.stripe.com/terminal/features/receipts)