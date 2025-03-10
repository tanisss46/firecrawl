# Save a card without bank authentication

## Collect card details in your mobile app and charge your customer at a later time.

iOSAndroidReact Native
​​Stripe allows you to collect card details and charge your customer at a later
time. ​​In some regions, banks require a second form of authentication such as
entering a code sent to a phone. ​​The extra step decreases conversion if your
customer isn’t actively using your website or application because they aren’t
available to authenticate the purchase.

​​If you primarily do business in the US and Canada, banks don’t require
authentication, so you can follow this simpler integration. This integration
will be non-compliant in countries that require authentication for saving cards
(for example, India) so building this integration means that expanding to other
countries or adding other payment methods will require significant changes.
Learn how to [save cards that require
authentication](https://docs.stripe.com/payments/save-and-reuse).

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. For instance, if you
want to save their payment method for future use, such as charging them when
they’re not actively using your website or app. Add terms to your website or app
that state how you plan to save payment method details and allow customers to
opt in. If you want to charge them when they’re offline, make sure your terms
include the following:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges
are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

[Set up
StripeServer-sideClient-side](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-setup)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Set up the iOS and server Stripe SDKs before starting your integration.

### Server-side

This integration requires endpoints on your server that talk to the Stripe API.
Use our official libraries:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source,
[fully documented](https://stripe.dev/stripe-ios/index.html), and compatible
with apps supporting iOS 13 or above.

Swift Package ManagerCocoaPodsCarthageManual Framework
To install the SDK, follow these steps:

- In Xcode, select **File** > **Add Package Dependencies…** and enter
`https://github.com/stripe/stripe-ios-spm` as the repository URL.
- Select the latest version number from our [releases
page](https://github.com/stripe/stripe-ios/releases).
- Add the **StripePaymentsUI** product to the [target of your
app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### Note

For details on the latest SDK release and past versions, see the
[Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To
receive notifications when a new release is published, [watch
releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository)
for the repository.

Configure the SDK with your Stripe [publishable
key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your
app to make requests to the Stripe API.

```
import UIKit
import StripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

func application(_ application: UIApplication, didFinishLaunchingWithOptions
launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
 StripeAPI.defaultPublishableKey = "pk_test_TYooMQauvdEDq54NiTphI7jx"
 // do any other necessary launch configuration
 return true
 }
}
```

#### Note

Use your [test mode](https://docs.stripe.com/keys#obtain-api-keys) keys while
you test and develop, and your [live
mode](https://docs.stripe.com/keys#test-live-modes) keys when you publish your
app.

[Collect card
detailsClient-side](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-collect-card-details)
Start by displaying a payment form to your customer. Collect card details from
the customer using
[STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html),
a drop-in UI component provided by the SDK that collects the card number,
expiration date, CVC, and postal code.

[STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html)
performs on-the-fly validation and formatting.

Pass the card details to
[createPaymentMethod](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createPaymentMethodWithPayment:completion:)
to create a [PaymentMethod](https://docs.stripe.com/api/payment_methods).

```
class CheckoutViewController: UIViewController {
 lazy var cardTextField: STPPaymentCardTextField = {
 let cardTextField = STPPaymentCardTextField()
 return cardTextField
 }()

 @objc
 func pay() {
 // Collect card details on the client
STPAPIClient.shared.createPaymentMethod(with: cardTextField.paymentMethodParams)
{ [weak self] paymentMethod, error in
 guard let paymentMethod = paymentMethod else {
 // Display the error to the user
 return
 }
 let paymentMethodId = paymentMethod.stripeId
 // Send paymentMethodId to your server for the next steps
 }
 }
}
```

Send the resulting PaymentMethod ID to your server and follow the remaining
steps to save the card to a customer and charge the card in the future.

[Save the
cardServer-side](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-save-card)
Save the card by attaching the PaymentMethod to a
[Customer](https://docs.stripe.com/api/customers). You can use the Customer
object to store other information about your customer, such as shipping details
and email address.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_method={{PAYMENT_METHOD_ID}}
```

If you have an existing Customer, you can attach the PaymentMethod to that
object instead.

```
curl https://api.stripe.com/v1/payment_methods/{{PAYMENT_METHOD_ID}}/attach \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}}
```

At this point, associate the ID of the Customer object and the ID of the
PaymentMethod with your own internal representation of a customer, if you have
one.

[Charge the saved
cardServer-side](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-charge-card)
When you are ready to charge the Customer, look up the PaymentMethod ID to
charge. You can do this by either storing the IDs of both in your database, or
by using the Customer ID to look up all the Customer’s available PaymentMethods.

```
curl -G https://api.stripe.com/v1/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d type=card
```

Use the PaymentMethod ID and the Customer ID to create a new PaymentIntent. Set
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
to true to decline payments that require any actions from your customer, such as
two-factor authentication.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d error_on_requires_action=true \
 -d confirm=true
```

When a payment attempt fails, the request also fails with a 402 HTTP status code
and Stripe throws an error. You need to notify your customer to return to your
application (for example, by sending an in-app notification) to complete the
payment. Check the code of the
[Error](https://docs.stripe.com/api/errors/handling) raised by the Stripe API
library or check the
[last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
on the PaymentIntent to inspect why the card issuer declined the payment.

[Handle any card
errors](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-handle-errors)
Notify your customer that the payment failed and direct them to the payment form
you made in Step 1 where they can enter new card details. Send that new
PaymentMethod ID to your server to
[attach](https://docs.stripe.com/api/payment_methods/attach) to the Customer
object and make the payment again.

Alternatively, you can create a PaymentIntent and save a card all in one API
call if you have already created a Customer.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d error_on_requires_action=true \
 -d confirm=true \
 -d setup_future_usage=on_session
```

Setting
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
to `on_session` indicates to Stripe that you wish to save the card for later,
without triggering unnecessary authentication.

[Test the
integration](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-test-integration)
Stripe provides [test cards](https://docs.stripe.com/testing) you can use in a
sandbox to simulate different cards’ behavior. Use these cards with any CVC,
postal code, and expiry date in the future.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000000000009995Always fails with a decline code of
`insufficient_funds`.4000002500003155Requires authentication, which in this
integration will decline with a code of
`authentication_required`.[OptionalRe-collect a
CVC](https://docs.stripe.com/payments/mobile/save-card-without-authentication#ios-recollect-cvc)
## Upgrade your integration to handle card authentication

This integration **declines cards that require authentication during payment**.
If you start seeing many payments in the Dashboard listed as `Failed`, then it’s
time to [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions).
Stripe’s global integration handles these payments instead of automatically
declining.

## Links

- [save cards that require
authentication](https://docs.stripe.com/payments/save-and-reuse)
- [Register now](https://dashboard.stripe.com/register)
- [Stripe iOS SDK](https://github.com/stripe/stripe-ios)
- [fully documented](https://stripe.dev/stripe-ios/index.html)
- [releases page](https://github.com/stripe/stripe-ios/releases)
- [target of your
app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)
- [watch
releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository)
- [publishable key](https://dashboard.stripe.com/test/apikeys)
- [test mode](https://docs.stripe.com/keys#obtain-api-keys)
- [live mode](https://docs.stripe.com/keys#test-live-modes)
-
[STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html)
-
[createPaymentMethod](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createPaymentMethodWithPayment:completion:)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Customer](https://docs.stripe.com/api/customers)
-
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
- [Error](https://docs.stripe.com/api/errors/handling)
-
[last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
- [attach](https://docs.stripe.com/api/payment_methods/attach)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [test cards](https://docs.stripe.com/testing)
- [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions)