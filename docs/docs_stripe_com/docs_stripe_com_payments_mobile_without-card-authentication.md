# Card payments without bank authentication

## Build a simpler mobile integration with regional limitations.

iOSAndroidReact Native
This integration supports businesses accepting only US and Canadian cards. It’s
simpler up front, but does not scale to support a global customer base.

### How does this integration work?

### How does it compare to the global integration?

Growing or global businesses should use Stripe’s [global
integration](https://docs.stripe.com/payments/accept-a-payment) to support bank
requests for two-factor authentication and allow customers to pay with more
payment methods.

[Install the Stripe iOS
SDKClient-side](https://docs.stripe.com/payments/mobile/without-card-authentication#ios-install-sdk)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

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
detailsClient-side](https://docs.stripe.com/payments/mobile/without-card-authentication#ios-collect-payment-details)
Securely collect card information on the client with
[STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html),
a drop-in UI component provided by the SDK that collects the card number,
expiration date, CVC, and postal code.

[STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html)
performs on-the-fly validation and formatting.

Create an instance of the card component and a **Pay** button with the following
code:

```
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {

 lazy var cardTextField: STPPaymentCardTextField = {
 let cardTextField = STPPaymentCardTextField()
 return cardTextField
 }()
 lazy var payButton: UIButton = {
 let button = UIButton(type: .custom)
 button.layer.cornerRadius = 5
 button.backgroundColor = .systemBlue
 button.titleLabel?.font = UIFont.systemFont(ofSize: 22)
 button.setTitle("Pay", for: .normal)
 button.addTarget(self, action: #selector(pay), for: .touchUpInside)
 return button
 }()

 override func viewDidLoad() {
 super.viewDidLoad()
 view.backgroundColor = .white
let stackView = UIStackView(arrangedSubviews: [cardTextField, payButton])
 stackView.axis = .vertical
 stackView.spacing = 20
 stackView.translatesAutoresizingMaskIntoConstraints = false
 view.addSubview(stackView)
 NSLayoutConstraint.activate([
stackView.leftAnchor.constraint(equalToSystemSpacingAfter: view.leftAnchor,
multiplier: 2),
view.rightAnchor.constraint(equalToSystemSpacingAfter: stackView.rightAnchor,
multiplier: 2),
stackView.topAnchor.constraint(equalToSystemSpacingBelow:
view.safeAreaLayoutGuide.topAnchor, multiplier: 2),
 ])
 }

 @objc
 func pay() {
 // ...
 }
}
```

Run your app and make sure your checkout page shows the card component. When the
customer taps **Pay**, call
[createPaymentMethod](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createPaymentMethodWithPayment:completion:)
to collect the card details and create a
[PaymentMethod](https://docs.stripe.com/api/payment_methods). Send the ID of the
PaymentMethod to your server.

```
func pay() {
 // Create a PaymentMethod with the card text field's card details
STPAPIClient.shared.createPaymentMethod(with: cardTextField.paymentMethodParams)
{ (paymentMethod, error) in
 guard let paymentMethod = paymentMethod else {
 // Display the error to the customer
 return
 }
 let paymentMethodID = paymentMethod.stripeId
 // Send paymentMethodID to your server for the next step
 }
}
```

[Make a
paymentServer-side](https://docs.stripe.com/payments/mobile/without-card-authentication#ios-create-payment-intent)
Set up an endpoint on your server to receive the request from the client. Use
the official libraries for access to the Stripe API from your server:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents)
object to represent your intent to collect payment from a customer, tracking
charge attempts and payment state changes throughout the process.

Create an HTTP endpoint to respond to the request from step 2. In that endpoint,
you should decide how much to charge the customer. To create a payment, create a
PaymentIntent using the PaymentMethod ID from step 2 with the following
parameters:

Always decide how much to charge on the server, a trusted environment, as
opposed to the client. This prevents malicious customers from being able to
choose their own prices.

```
# Check the status of the PaymentIntent to make sure it succeeded

curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1099 \
 -d currency=usd \

# A PaymentIntent can be confirmed some time after creation,
# but here we want to confirm (collect payment) immediately.
 -d confirm=true \
 -d payment_method="{{PAYMENT_METHOD_ID}}" \

# If the payment requires any follow-up actions from the
# customer, like two-factor authentication, Stripe will error
# and you will need to prompt them for a new payment method.
 -d error_on_requires_action=true
```

#### Warning

If you set
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
to `true` when confirming a payment, Stripe automatically fails the payment if
it requires two-factor authentication from the user.

#### Payment Intents API response

When you make a payment with the API, the response includes a status of the
PaymentIntent. If the payment was successful, it will have a status of
`succeeded`.

```
{
 "id": "pi_0FdpcX589O8KAxCGR6tGNyWj",
 "object": "payment_intent",
 "amount": 1099,
 "charges": {
 "object": "list",
 "data": [
 {
 "id": "ch_GA9w4aF29fYajT",
 "object": "charge",
 "amount": 1099,
 "refunded": false,
 "status": "succeeded",
 }
 ]
 },
"client_secret": "pi_0FdpcX589O8KAxCGR6tGNyWj_secret_e00tjcVrSv2tjjufYqPNZBKZc",
 "currency": "usd",
 "last_payment_error": null,
 "status": "succeeded",
}
```

If the payment is declined, the response includes the error code and error
message. Here’s an example of a payment that failed because two-factor
authentication was required for the card.

```
{
 "error": {
 "code": "authentication_required",
 "decline_code": "authentication_not_handled",
 "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
"message": "This payment required an authentication action to complete, but
`error_on_requires_action` was set. When you're ready, you can upgrade your
integration to handle actions at
https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
 "payment_intent": {
 "id": "pi_1G8JtxDpqHItWkFAnB32FhtI",
 "object": "payment_intent",
 "amount": 1099,
 "status": "requires_payment_method",
 "last_payment_error": {
 "code": "authentication_required",
 "decline_code": "authentication_not_handled",
"doc_url": "https://docs.stripe.com/error-codes#authentication-required",
"message": "This payment required an authentication action to complete, but
`error_on_requires_action` was set. When you're ready, you can upgrade your
integration to handle actions at
https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
 "type": "card_error"
 },
 },
 "type": "card_error"
 }
}
```

[Test the
integration](https://docs.stripe.com/payments/mobile/without-card-authentication#ios-test)
There are several test cards you can use in test mode to make sure this
integration is ready. Use them with any CVC, postal code, and future expiration
date.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000000000009995Always fails with a decline code of
`insufficient_funds`.4000002500003155Requires authentication, which in this
integration will fail with a decline code of `authentication_not_handled`.
See the full list of [test cards](https://docs.stripe.com/testing).

[Upgrade your integration to handle card
authentication](https://docs.stripe.com/payments/mobile/without-card-authentication#ios-upgrade-to-handle-card-authentication)
Congratulations! You completed a payments integration for basic card payments.
Note that this integration **declines cards that require authentication during
payment**.

If you start seeing payments in the Dashboard listed as `Failed`, then it’s time
to [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions).
Stripe’s global integration handles these payments instead of automatically
declining them.

## Links

- [global integration](https://docs.stripe.com/payments/accept-a-payment)
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
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
-
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
-
[https://docs.stripe.com/error-codes#authentication-required](https://docs.stripe.com/error-codes#authentication-required)
-
[https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.](https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions)
- [test cards](https://docs.stripe.com/testing)
- [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions)