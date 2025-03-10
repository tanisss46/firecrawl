# Integrate the Customer Sheet

## Offer a prebuilt UI for your customers to manage their saved payment methods.

iOSAndroidReact Native
The Customer Sheet is a prebuilt UI component that lets your customers manage
their saved payment methods. You can use the Customer Sheet UI outside of a
checkout flow, and the appearance and styling is customizable to match the
appearance and aesthetic of your app. Customers can add and remove payment
methods, which get saved to the customer object, and set their default payment
method stored locally on the device. Use both the Mobile Payment Element and the
Customer Sheet to provide customers a consistent end-to-end solution for saved
payment methods.

![Screenshot of Customer Sheet presenting multiple saved payment methods in an
iOS
app.](https://b.stripecdn.com/docs-statics-srv/assets/ios-landing.6c4969968fd6efe3d39fe673628f8284.png)

CustomerAdapter uses Customer Ephemeral Keys and serves as a bridge to help
users of legacy products adopt CustomerSheet more quickly. If you’re starting a
new integration, we recommend adopting CustomerSession over Customer Ephemeral
Keys.

[Set up Stripe](https://docs.stripe.com/elements/customer-sheet#ios-setup)
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
- Add the **StripePaymentSheet** product to the [target of your
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
import StripePaymentSheet

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

[Enable payment
methods](https://docs.stripe.com/elements/customer-sheet#ios-enable-payment-methods)
View your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) and enable the
payment methods you want to support. You need at least one payment method
enabled to create a [SetupIntent](https://docs.stripe.com/api/setup_intents).

By default, Stripe enables cards and other prevalent payment methods that can
help you reach more customers, but we recommend turning on additional payment
methods that are relevant for your business and customers. See [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
for product and payment method support, and our [pricing
page](https://stripe.com/pricing/local-payment-methods) for fees.

#### Note

At this time, CustomerSheet only supports cards and US bank accounts.

[Add Customer
endpointsServer-side](https://docs.stripe.com/elements/customer-sheet#ios-add-endpoints)
Create two endpoints on your server: one for fetching a Customer’s ephemeral
key, and one to create a
[SetupIntent](https://docs.stripe.com/api/setup_intents) for saving a new
payment method to the [Customer](https://docs.stripe.com/api/customers).

- Create an endpoint to return a
[Customer](https://docs.stripe.com/api/customers) ID and an associated ephemeral
key. You can view the API version used by the SDK
[here](https://github.com/stripe/stripe-ios/blob/master/StripeCore/StripeCore/Source/API%20Bindings/STPAPIClient.swift#L233).

```
# Create a Customer (skip this and get the existing Customer ID if this is a returning customer)
curl https://api.stripe.com/v1/customers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST"

curl https://api.stripe.com/v1/ephemeral_keys \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST" \
 -d "customer"="{{CUSTOMER_ID}}" \
```

- Create an endpoint to return a
[SetupIntent](https://docs.stripe.com/api/setup_intents) configured with the
[Customer](https://docs.stripe.com/api/customers) ID.

```
# Create a Customer (skip this and get the existing Customer ID if this is a returning customer)
curl https://api.stripe.com/v1/customers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST"

curl https://api.stripe.com/v1/setup_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer"="{{CUSTOMER_ID}}" \
```

If you only plan to use the payment method for future payments when your
customer is present during the checkout flow, set the
[usage](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage)
parameter to on_session to improve authorization rates.

[Create a Customer
adapterClient-side](https://docs.stripe.com/elements/customer-sheet#ios-customer-adapter)
A `StripeCustomerAdapter` enables a `CustomerSheet` to communicate with Stripe.
On the client, configure a `StripeCustomerAdapter` with providers that make
requests to these endpoints on your server.

```
import StripePaymentSheet

let customerAdapter = StripeCustomerAdapter(customerEphemeralKeyProvider: {
 let json = await myBackend.getCustomerEphemeralKey()
return CustomerEphemeralKey(customerId: json["customerId"]!, ephemeralKeySecret:
json["ephemeralKeySecret"]!)
}, setupIntentClientSecretProvider: {
 let json = await myBackend.getSetupIntentForCustomer()
 return json["setupIntentClientSecret"]!
})
```

[Configure the
sheet](https://docs.stripe.com/elements/customer-sheet#ios-configure-wallet-element)
Next, configure the Customer Sheet with your `StripeCustomerAdapter` and a
[CustomerSheet.Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/configuration/).

```
var configuration = CustomerSheet.Configuration()

// Configure settings for the CustomerSheet here. For example:
configuration.headerTextForSelectionScreen = "Manage your payment method"

let customerSheet = CustomerSheet(configuration: configuration, customer:
customerAdapter)
```

[Present the
sheet](https://docs.stripe.com/elements/customer-sheet#ios-present-wallet-element)UIKitSwiftUI
Present the Customer Sheet. When the customer dismisses the sheet, the Customer
Sheet calls the completion block with a `CustomerSheet.SheetResult`.

```
import StripePaymentSheet

customerSheet.present(from: self, completion: { result in
 switch result {
 case .canceled(let paymentOption), .selected(let paymentOption):
 // Configure your UI based on the payment option
 self.paymentLabel.text = paymentOption?.displayData().label ?? "None"

// Optional: Send the selected payment method ID to your backend for advanced
use cases
 // like charging a customer when not present in your app
 if let paymentOption = paymentOption {
 switch paymentOption {
 case .paymentMethod(let paymentMethod, let paymentOptionDisplayData):
 MyBackend.setDefaultPaymentMethod(paymentMethod.stripeId)
 case .applePay(paymentOptionDisplayData: let paymentOptionDisplayData):
 MyBackend.setDefaultPaymentMethodIsApplePay()
 }
 }
 case .error(let error):
 // Show the error in your UI
 }
})
```

- If the customer selects a payment method, the result is
`.selected(PaymentOptionSelection?)`. The associated value is the selected
[PaymentOptionSelection](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/paymentoptionselection),
or `nil` if the user deleted the previously-selected payment method. You can
find the full payment method details in the PaymentOptionSelection’s
`paymentMethod` associated value.
- If the user cancels the sheet, the result is `.canceled`. The associated value
is the original payment method selected prior to opening the customer sheet, as
long as that payment method is still available.
- If an error occurs, the result is `.error(Error)`.

Learn more about how to [enable Apple
Pay](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element#ios-apple-pay).

[OptionalEnable ACH
payments](https://docs.stripe.com/elements/customer-sheet#ios-ach)[OptionalFetch
the selected payment
method](https://docs.stripe.com/elements/customer-sheet#ios-get-selected-payment-method)[OptionalCustomize
the sheet](https://docs.stripe.com/elements/customer-sheet#ios-custom-behavior)

## Links

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
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing page](https://stripe.com/pricing/local-payment-methods)
- [Customer](https://docs.stripe.com/api/customers)
-
[here](https://github.com/stripe/stripe-ios/blob/master/StripeCore/StripeCore/Source/API%20Bindings/STPAPIClient.swift#L233)
-
[usage](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage)
-
[CustomerSheet.Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/configuration/)
-
[PaymentOptionSelection](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/paymentoptionselection)
- [enable Apple
Pay](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element#ios-apple-pay)