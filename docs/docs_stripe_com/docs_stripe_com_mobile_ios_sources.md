# Getting started with Sources in the iOS SDKDeprecated

## Learn how to use Sources in your iOS application.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently handle any local payment methods using the Sources
API, you must [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

While we don’t plan to remove support for card payments, we recommend replacing
any use of the Sources API with the [PaymentMethods
API](https://docs.stripe.com/api/payment_methods), which provides access to our
latest features and payment method types.

Creating a payment using [Sources](https://docs.stripe.com/sources) with the iOS
SDK is a multi-step process:

- [Create an STPSource
object](https://docs.stripe.com/mobile/ios/sources#create-an-stpsource-object)
that represents your customer’s payment method.
- [Check if further action is
required](https://docs.stripe.com/mobile/ios/sources#check-if-further-action-is-required)
from your customer.

If no further action is required:

- Confirm the source is ready to use.
- Create a charge request on your backend using the source.

If further action is required:

- Present the user with any information they may need to authorize the charge.
- On your backend, listen to Stripe [webhooks](https://docs.stripe.com/webhooks)
to create a charge with the source.
- In your app, display the appropriate confirmation to your customer based on
the source’s status.
[Create an STPSource
object](https://docs.stripe.com/mobile/ios/sources#create-an-stpsource-object)
Once you’ve collected your customer’s payment details, you can use the
`STPAPIClient` class to create a source. First, assemble an `STPSourceParams`
object with the payment information you’ve collected. Then, pass this object to
`STPAPIClient`’s `createSourceWithParams:` method.

To create an `STPSourceParams` object, use one of the helper constructors we
provide, which specify the information needed for each [payment
method](https://docs.stripe.com/sources).

[Check if further action is required from your
customer](https://docs.stripe.com/mobile/ios/sources#check-if-further-action-is-required)
To determine whether further action is required from your customer, check the
`flow` property on the newly created `STPSource` object. If `flow` is
`STPSourceFlowNone`, no further action is required. For example, if you create a
source for a card payment, its status is immediately set to
`STPSourceStatusChargeable`. No additional customer action is needed, so you can
tell your backend to create a charge with the source right away.

```
let cardParams = STPCardParams()
cardParams.name = "Jenny Rosen"
cardParams.number = "4242424242424242"
cardParams.expMonth = 12
cardParams.expYear = 18
cardParams.cvc = "424"

let sourceParams = STPSourceParams.cardParams(withCard: cardParams)
STPAPIClient.shared.createSource(with: sourceParams) { (source, error) in
 if let s = source, s.flow == .none && s.status == .chargeable {
 self.createBackendChargeWithSourceID(s.stripeID)
 }
}
```

If the source’s flow is not `STPSourceFlowNone`, then your customer needs to
complete an action before the source can be used in a charge request.

FlowDescription`STPSourceFlowRedirect`Your customer must be redirected to the
[payment method](https://docs.stripe.com/sources)’s website or app to confirm
the charge. See the section below for more
information.`STPSourceFlowReceiver`Your customer must push funds to the account
information provided in the Source object. See the documentation for the
specific [payment method](https://docs.stripe.com/sources) you are using for
more information.`STPSourceFlowVerification`Your customer must verify ownership
of their account by providing a code that you post to the Stripe API for
authentication. See the documentation for the specific [payment
method](https://docs.stripe.com/sources) you are using for more information.
If the source requires further action from your customer, your iOS app should
*not* tell your backend to create a charge request. Instead, your backend should
listen for the `source.chargeable` webhook event to charge the source. This
ensures that the source is charged even if the user never returns to your app
after taking the required action. See [best
practices](https://docs.stripe.com/sources/best-practices) for more information
on supporting different payment methods using webhooks.

## Redirect your customer to authorize a source

For sources that require redirecting your customer to authorize the payment, you
need to specify a return URL when you create the source. This allows your
customer to be redirected back to your app after they authorize the payment. For
this return URL, you can either use a custom URL scheme or a universal link
supported by your app. For more information on registering and handling URLs in
your app, refer to the Apple documentation:

- [Implementing custom URL
schemes](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6-SW10)
- [Supporting universal
links](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html)

To handle redirecting your customer to the URL in the source object’s
`redirect.url` parameter, we recommend using `STPRedirectContext`, which you can
use to open the URL in `SFSafariViewController`, if available, or mobile Safari
otherwise. To use `STPRedirectContext`, you’ll need to first set up your app
delegate to forward URLs to the Stripe SDK.

```
// This method handles opening native URLs (for example,
"your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options:
[UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
 let stripeHandled = StripeAPI.handleURLCallback(with: url)
 if (stripeHandled) {
 return true
 } else {
 // This was not a stripe url – do whatever url handling your app
 // normally does, if any.
 }
 return false
}

// This method handles opening universal link URLs (for example,
"https://example.com/stripe_ios_callback")
func application(_ application: UIApplication, continue userActivity:
NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) ->
Void) -> Bool {
 if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
 if let url = userActivity.webpageURL {
 let stripeHandled = StripeAPI.handleURLCallback(with: url)
 if (stripeHandled) {
 return true
 } else {
 // This was not a stripe url – do whatever url handling your app
 // normally does, if any.
 }
 }
 }
 return false
}
```

`STPRedirectContext`’s completion block is called after your customer returns to
your app. At this point, the user may or may not have completed the
authorization process. You can use webhooks on your own server to receive
notification of a change in status of the source’s chargeable state. See [best
practices](https://docs.stripe.com/sources/best-practices) for more information
on how to build a confirmation screen when using sources.

If you’d like more help, check out the [example
app](https://github.com/stripe/stripe-ios/tree/master/Example/Non-Card%20Payment%20Examples)
that demonstrates creating a payment using several different payment methods.

## See also

- [Using Payment Intents on
iOS](https://docs.stripe.com/payments/accept-a-payment?integration=elements)
- [Transitioning to Payment
Methods](https://docs.stripe.com/payments/payment-methods)

## Links

- [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [PaymentMethods API](https://docs.stripe.com/api/payment_methods)
- [installed and
configured](https://docs.stripe.com/payments/accept-a-payment-charges)
- [Sources](https://docs.stripe.com/sources)
- [webhooks](https://docs.stripe.com/webhooks)
- [iOS SDK reference](http://stripe.github.io/stripe-ios)
- [best practices](https://docs.stripe.com/sources/best-practices)
- [Implementing custom URL
schemes](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6-SW10)
- [Supporting universal
links](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html)
-
[https://example.com/stripe_ios_callback](https://example.com/stripe_ios_callback)
- [example
app](https://github.com/stripe/stripe-ios/tree/master/Example/Non-Card%20Payment%20Examples)
- [Using Payment Intents on
iOS](https://docs.stripe.com/payments/accept-a-payment?integration=elements)
- [Transitioning to Payment
Methods](https://docs.stripe.com/payments/payment-methods)