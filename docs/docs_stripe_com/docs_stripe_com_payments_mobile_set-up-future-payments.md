# Set up future payments

## Learn how to save payment details in your mobile app and charge your customers later.

iOSAndroidReact Native
The [Setup Intents API](https://docs.stripe.com/api/setup_intents) lets you save
a customer’s payment details without an initial payment. This is helpful if you
want to onboard customers now, set them up for payments, and charge them in the
future—when they’re offline.

Use this integration to set up recurring payments or to create one-time payments
with a final amount determined later, often after the customer receives your
service.

#### Card-present transactions

Card-present transactions, such as collecting card details through Stripe
Terminal, use a different process for saving the payment method. For details,
see [the Terminal
documentation](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. These requirements
generally apply if you want to save your customer’s payment method for future
use, such as displaying a customer’s payment method to them in the checkout flow
for a future purchase or charging them when they’re not actively using your
website or app. Add terms to your website or app that state how you plan to save
payment method details and allow customers to opt in.

When you save a payment method, you can only use it for the specific usage you
have included in your terms. To charge a payment method when a customer is
offline and save it as an option for future purchases, make sure that you
explicitly collect consent from the customer for this specific use. For example,
include a “Save my payment method for future use” checkbox to collect consent.

To charge them when they’re offline, make sure your terms include the following:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges
are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

#### Note

If you need to use manual server-side confirmation or your integration requires
presenting payment methods separately, see our [alternative
guide](https://docs.stripe.com/payments/save-and-reuse-cards-only).

!

Integrate Stripe’s prebuilt payment UI into the checkout of your iOS app with
the
[PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html)
class. See our sample integration [on
GitHub](https://github.com/stripe/stripe-ios/tree/master/Example/PaymentSheet%20Example).

[Set up
StripeServer-sideClient-side](https://docs.stripe.com/payments/mobile/set-up-future-payments#setup)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API.
Use our official libraries for access to the Stripe API from your server:

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
- Add the **StripePaymentSheet** product to the [target of your
app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### Note

For details on the latest SDK release and past versions, see the
[Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To
receive notifications when a new release is published, [watch
releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository)
for the repository.

[Add an
endpointServer-side](https://docs.stripe.com/payments/mobile/set-up-future-payments#add-server-endpoint)
#### Note

The mobile Payment Element only supports SetupIntents with cards, Bancontact,
iDEAL, Link, SEPA Direct Debit, Sofort, and US bank accounts.

This integration uses three Stripe API objects:

- A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent to set up a customer’s payment method for future
payments. The payment methods shown to customers during the checkout process are
also included on the SetupIntent. You can let Stripe automatically pull payment
methods from your Dashboard settings or you can list them manually.
- A [Customer](https://docs.stripe.com/api/customers). To set up a payment
method for future payments, it must be attached to a Customer. Create a Customer
object when your customer creates an account with your business. If your
customer is making a payment as a guest, you can create a Customer object before
payment and associate it with your own internal representation of the customer’s
account later.
- A Customer Ephemeral Key (optional). Information on the Customer object is
sensitive, and can’t be retrieved directly from an app. An Ephemeral Key grants
the SDK temporary access to the Customer.

For security reasons, your app can’t create these objects. Instead, add an
endpoint on your server that:

- Retrieves the Customer, or creates a new one.
- Creates an Ephemeral Key for the Customer.
- Creates a SetupIntent with the Customer ID.
- Returns the SetupIntent’s [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret),
the Ephemeral Key’s `secret`, the Customer’s
[ID](https://docs.stripe.com/api/customers/object#customer_object-id), and your
[publishable key](https://dashboard.stripe.com/apikeys) to your app.

The payment methods shown to customers during the checkout process are also
included on the SetupIntent. You can let Stripe automatically pull payment
methods from your Dashboard settings or you can list them manually.

Manage payment methods from the DashboardListing payment methods manually
You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow.

```
# Create a Customer (use an existing Customer ID if this is a returning customer)
curl https://api.stripe.com/v1/customers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST"

# Create an Ephemeral Key for the Customer
curl https://api.stripe.com/v1/ephemeral_keys \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia" \
 -X "POST" \
 -d "customer"="{{CUSTOMER_ID}}" \

# Create a SetupIntent
curl https://api.stripe.com/v1/setup_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
# In the latest version of the API, specifying the `automatic_payment_methods`
parameter
 # is optional because Stripe enables its functionality by default.
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "automatic_payment_methods[enabled]"=true \
```

[Collect payment
detailsClient-side](https://docs.stripe.com/payments/mobile/set-up-future-payments#collect-payment-details)
#### Note

To display the mobile Payment Element before you create a SetupIntent, see
[Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?type=setup).

To display the mobile Payment Element on your checkout screen, you must add a
checkout button that displays Stripe’s UI components.

UIKitSwiftUI
In your app’s checkout screen, fetch the SetupIntent client secret, Ephemeral
Key secret, Customer ID, and publishable key from the endpoint you created in
the previous step. Set your publishable key using `StripeAPI.shared` and
initialize
[PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html).

```
import UIKit
import StripePaymentSheet

class CheckoutViewController: UIViewController {
 @IBOutlet weak var checkoutButton: UIButton!
 var paymentSheet: PaymentSheet?
let backendCheckoutUrl = URL(string: "Your backend endpoint/payment-sheet")! //
Your backend endpoint

 override func viewDidLoad() {
 super.viewDidLoad()

checkoutButton.addTarget(self, action: #selector(didTapCheckoutButton), for:
.touchUpInside)
 checkoutButton.isEnabled = false

// MARK: Fetch the SetupIntent client secret, Ephemeral Key secret, Customer ID,
and publishable key
 var request = URLRequest(url: backendCheckoutUrl)
 request.httpMethod = "POST"
let task = URLSession.shared.dataTask(with: request, completionHandler: { [weak
self] (data, response, error) in
 guard let data = data,
let json = try? JSONSerialization.jsonObject(with: data, options: []) as?
[String : Any],
 let customerId = json["customer"] as? String,
 let customerEphemeralKeySecret = json["ephemeralKey"] as? String,
 let setupIntentClientSecret = json["setupIntent"] as? String,
 let publishableKey = json["publishableKey"] as? String,
 let self = self else {
 // Handle error
 return
 }

 STPAPIClient.shared.publishableKey = publishableKey
 // MARK: Create a PaymentSheet instance
 var configuration = PaymentSheet.Configuration()
 configuration.merchantDisplayName = "Example, Inc."
configuration.customer = .init(id: customerId, ephemeralKeySecret:
customerEphemeralKeySecret)
 // Set `allowsDelayedPaymentMethods` to true if your business handles
 // delayed notification payment methods like US bank accounts.
 configuration.allowsDelayedPaymentMethods = true
self.paymentSheet = PaymentSheet(setupIntentClientSecret:
setupIntentClientSecret, configuration: configuration)

 DispatchQueue.main.async {
 self.checkoutButton.isEnabled = true
 }
 })
 task.resume()
 }

}
```

When the customer taps the **Checkout** button, call `present` to present the
PaymentSheet. After the customer completes the payment, Stripe dismisses the
PaymentSheet and calls the completion block with
[PaymentSheetResult](https://stripe.dev/stripe-ios/stripe-paymentsheet/Enums/PaymentSheetResult.html).

```
@objc
func didTapCheckoutButton() {
 // MARK: Start the checkout process
 paymentSheet?.present(from: self) { paymentResult in
 // MARK: Handle the payment result
 switch paymentResult {
 case .completed:
 print("Your order is confirmed")
 case .canceled:
 print("Canceled!")
 case .failed(let error):
 print("Payment failed: \(error)")
 }
 }
}
```

If `PaymentSheetResult` is `.completed`, inform the user (for example, by
displaying an order confirmation screen).

Setting `allowsDelayedPaymentMethods` to true allows [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment methods like US bank accounts. For these payment methods, the final
payment status isn’t known when the `PaymentSheet` completes, and instead
succeeds or fails later. If you support these types of payment methods, inform
the customer their order is confirmed and only fulfill their order (for example,
ship their product) when the payment is successful.

[Set up a return
URLServer-side](https://docs.stripe.com/payments/mobile/set-up-future-payments#set-up-return-url)
The customer might navigate away from your app to authenticate (for example, in
Safari or their banking app). To allow them to automatically return to your app
after authenticating, [configure a custom URL
scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)
and set up your app delegate to forward the URL to the SDK. Stripe doesn’t
support [universal
links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

SceneDelegateAppDelegateSwiftUI
```
// This method handles opening custom URL schemes (for example,
"your-app://stripe-redirect")
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>)
{
 guard let url = URLContexts.first?.url else {
 return
 }
 let stripeHandled = StripeAPI.handleURLCallback(with: url)
 if (!stripeHandled) {
 // This was not a Stripe url – handle the URL normally as you would
 }
}
```

Additionally, set the
[returnURL](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV9returnURLSSSgvp)
on your
[PaymentSheet.Configuration](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html)
object to the URL for your app.

```
var configuration = PaymentSheet.Configuration()
configuration.returnURL = "your-app://stripe-redirect"
```

[Charge the saved payment method
laterServer-side](https://docs.stripe.com/payments/mobile/set-up-future-payments#charge-saved-payment-method)
#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. When rendering past
payment methods to your end customer for future purchases, make sure you’re
listing payment methods where you’ve collected consent from the customer to save
the payment method details for this specific future use. To differentiate
between payment methods attached to customers that can and can’t be presented to
your end customer as a saved payment method for future purchases, use the
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
parameter.

When you’re ready to charge your customer off-session, use the Customer and
PaymentMethod IDs to create a PaymentIntent. To find a payment method to charge,
list the payment methods associated with your customer. This example lists cards
but you can list any supported
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).

```
curl -G https://api.stripe.com/v1/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d type=card
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with
the amount and currency of the payment. Set a few other parameters to make the
off-session payment:

- Set
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
to `true` to indicate that the customer isn’t in your checkout flow during a
payment attempt and can’t fulfill an authentication request made by a partner,
such as a card issuer, bank, or other payment institution. If, during your
checkout flow, a partner requests authentication, Stripe requests exemptions
using customer information from a previous on-session transaction. If the
conditions for exemption aren’t met, the PaymentIntent might throw an error.
- Set the value of the PaymentIntent’s
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
property to `true`, which causes confirmation to occur immediately when the
PaymentIntent is created.
- Set
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
to the ID of the PaymentMethod and
[customer](https://docs.stripe.com/api#create_payment_intent-customer) to the ID
of the Customer.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1099 \
 -d currency=usd \
# In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 -d "automatic_payment_methods[enabled]"=true \
 -d customer="{{CUSTOMER_ID}}" \
 -d payment_method="{{PAYMENT_METHOD_ID}}" \
 -d return_url="https://example.com/order/123/complete" \
 -d off_session=true \
 -d confirm=true
```

[Test the
integration](https://docs.stripe.com/payments/mobile/set-up-future-payments#test-the-integration)Payment
methodScenarioHow to testCredit cardThe card setup succeeds and doesn’t require
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number `4242 4242 4242 4242` with
any expiration, CVC, and postal code.Credit cardThe card requires authentication
for the initial setup, then succeeds for subsequent payments.Fill out the credit
card form using the credit card number `4000 0025 0000 3155` with any
expiration, CVC, and postal code.Credit cardThe card requires authentication for
the initial setup and also requires authentication for subsequent payments.Fill
out the credit card form using the credit card number `4000 0027 6000 3184` with
any expiration, CVC, and postal code.Credit cardThe card is declined during
setup.Fill out the credit card form using the credit card number `4000 0000 0000
9995` with any expiration, CVC, and postal code.[OptionalEnable Apple
Pay](https://docs.stripe.com/payments/mobile/set-up-future-payments#apple-pay)[OptionalEnable
card
scanning](https://docs.stripe.com/payments/mobile/set-up-future-payments#card-scanning)[OptionalCustomize
the
sheet](https://docs.stripe.com/payments/mobile/set-up-future-payments#customization)[OptionalComplete
payment in your
UI](https://docs.stripe.com/payments/mobile/set-up-future-payments#flowcontroller)

## Links

- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [the Terminal
documentation](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly)
- [alternative
guide](https://docs.stripe.com/payments/save-and-reuse-cards-only)
-
[PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html)
- [on
GitHub](https://github.com/stripe/stripe-ios/tree/master/Example/PaymentSheet%20Example)
- [Register now](https://dashboard.stripe.com/register)
- [Stripe iOS SDK](https://github.com/stripe/stripe-ios)
- [fully documented](https://stripe.dev/stripe-ios/index.html)
- [releases page](https://github.com/stripe/stripe-ios/releases)
- [target of your
app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)
- [watch
releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository)
- [Customer](https://docs.stripe.com/api/customers)
- [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
- [ID](https://docs.stripe.com/api/customers/object#customer_object-id)
- [publishable key](https://dashboard.stripe.com/apikeys)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?type=setup)
-
[PaymentSheetResult](https://stripe.dev/stripe-ios/stripe-paymentsheet/Enums/PaymentSheetResult.html)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [configure a custom URL
scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)
- [universal
links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content)
-
[returnURL](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV9returnURLSSSgvp)
-
[PaymentSheet.Configuration](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html)
-
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
-
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
-
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
-
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
-
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
- [customer](https://docs.stripe.com/api#create_payment_intent-customer)
- [authentication](https://docs.stripe.com/strong-customer-authentication)