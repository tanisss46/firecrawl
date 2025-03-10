# Link in the Mobile Payment Element

## Add Link to your native iOS, Android, and React Native apps.

Let your customer check out faster by using
[Link](https://docs.stripe.com/payments/link) in the [Mobile Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element).
You can autofill information for any customer already using Link, regardless of
whether they initially saved their information in Link with another business.
The default Mobile Payment Element integration includes a Link prompt in the
card form.

![Link in
iOS](https://b.stripecdn.com/docs-statics-srv/assets/link-in-ios.de526c6199ff89fbaa7b1beb5e8bc3da.png)

Add Link to your iOS integration

## Enable Link

To offer Link in your mobile app:

- [Integrate the Mobile Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)
using the latest version of the Stripe Mobile SDK.
- Enable Link in your [Payment Method
settings](https://dashboard.stripe.com/settings/payment_methods).
- Enable [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
by using the [latest version of the API](https://docs.stripe.com/upgrades) or by
adding the
[automatic_payment_methods](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-automatic_payment_methods)
parameter when creating your PaymentIntent.
- (Optional) [Pass in your customer’s email
address](https://docs.stripe.com/payments/link/mobile-payment-element-link#pass-email).

For information about how your payment integration affects Link, see [Link in
different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations).

## Pass in a customer’s email address

Link authenticates a customer using their email address. We recommend prefilling
as much information as possible to streamline the checkout process.

iOSAndroidReact Native
To prefill the customer’s name, email address, and phone number, supply
`defaultBillingDetails` with your customer information after initializing
`PaymentSheet.Configuration`.

```
var configuration = PaymentSheet.Configuration()
configuration.defaultBillingDetails.name = "Jenny Rosen"
configuration.defaultBillingDetails.email = "jenny.rosen@example.com"
configuration.defaultBillingDetails.phone = "888-888-8888"
```

## Test your integration

You can create sandbox accounts for Link using any valid email address. When
prompted for a one-time passcode, enter `000000`.

## See also

- [Stripe Mobile SDKs](https://docs.stripe.com/sdks#stripe-mobile-sdks)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Mobile Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)
- [Payment Method
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [latest version of the API](https://docs.stripe.com/upgrades)
-
[automatic_payment_methods](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-automatic_payment_methods)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)
- [Stripe Mobile SDKs](https://docs.stripe.com/sdks#stripe-mobile-sdks)