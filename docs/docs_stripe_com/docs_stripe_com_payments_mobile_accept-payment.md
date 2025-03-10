# Accept in-app payments

## Build a customized payments integration and checkout flows for your iOS, Android, and React Native apps.

Add a payments form to your app.

iOSAndroidReact NativeAccept a paymentSet up a payment method
The Payment Element allows you to accept multiple payment methods using a single
integration. In this integration, you build a custom payment flow where you
render the Payment Element, create the
[PaymentIntent](https://docs.stripe.com/payments/payment-intents), and confirm
the payment in your app. To confirm the payment on the server instead, see
[Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server).

[Set up
StripeServer-sideClient-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#setup)
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

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open
source and fully documented. Internally, it uses the [native
iOS](https://github.com/stripe/stripe-ios) and
[Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s
React Native SDK, run one of the following commands in your project’s directory
(depending on which package manager you use):

yarnnpm
```
yarn add @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, navigate to the **ios** directory and run `pod install` to ensure
that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen
with the `StripeProvider` component, or use the `initStripe` initialization
method. Only the API [publishable
key](https://docs.stripe.com/keys#obtain-api-keys) in `publishableKey` is
required. The following example shows how to initialize Stripe using the
`StripeProvider` component.

```
import { StripeProvider } from '@stripe/stripe-react-native';

function App() {
 const [publishableKey, setPublishableKey] = useState('');

 const fetchPublishableKey = async () => {
 const key = await fetchKey(); // fetch key from your server here
 setPublishableKey(key);
 };

 useEffect(() => {
 fetchPublishableKey();
 }, []);

 return (
 <StripeProvider
 publishableKey={publishableKey}
 merchantIdentifier="merchant.identifier" // required for Apple Pay
 urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
 >
 // Your app code here
 </StripeProvider>
 );
}
```

#### Note

Use your API keys for [test mode](https://docs.stripe.com/keys#obtain-api-keys)
while you test and develop, and your [live
mode](https://docs.stripe.com/keys#test-live-modes) keys when you publish your
app.

[Enable payment
methods](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#enable-payment-methods)
View your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) and enable the
payment methods you want to support. You need at least one payment method
enabled to create a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents).

By default, Stripe enables cards and other prevalent payment methods that can
help you reach more customers, but we recommend turning on additional payment
methods that are relevant for your business and customers. See [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
for product and payment method support, and our [pricing
page](https://stripe.com/pricing/local-payment-methods) for fees.

[Set up a return
URLClient-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#set-up-return-url)
When a customer exits your app, for example to authenticate in Safari or their
banking app, provide a way for them to automatically return to your app
afterward. Many payment method types **require** a return URL, so if you fail to
provide it, we can’t present those payment methods to your user, even if you’ve
enabled them.

To provide a return URL:

-
[Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme)
a custom URL. Universal links aren’t supported.
- [Configure](https://reactnative.dev/docs/linking) your custom URL.
- Set up your root component to forward the URL to the Stripe SDK as shown
below.

#### Note

If you’re using Expo, [set your
scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the
`app.json` file.

```
import React, { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
 const { handleURLCallback } = useStripe();

 const handleDeepLink = useCallback(
 async (url: string | null) => {
 if (url) {
 const stripeHandled = await handleURLCallback(url);
 if (stripeHandled) {
// This was a Stripe URL - you can return or add extra handling here as you see
fit
 } else {
 // This was NOT a Stripe URL – handle as you normally would
 }
 }
 },
 [handleURLCallback]
 );

 useEffect(() => {
 const getUrlAsync = async () => {
 const initialUrl = await Linking.getInitialURL();
 handleDeepLink(initialUrl);
 };

 getUrlAsync();

 const deepLinkListener = Linking.addEventListener(
 'url',
 (event: { url: string }) => {
 handleDeepLink(event.url);
 }
 );

 return () => deepLinkListener.remove();
 }, [handleDeepLink]);

 return (
 <View>
 <AwesomeAppComponent />
 </View>
 );
}
```

Additionally, set the `returnURL` when you call the `initPaymentSheet` method:

```
await initPaymentSheet({
 ...
 returnURL: 'your-app://stripe-redirect',
 ...
});
```

For more information on native URL schemes, refer to the
[Android](https://developer.android.com/training/app-links/deep-linking) and
[iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app)
docs.

[Collect payment
detailsClient-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#collect-payment-details)
The integration can use the default payment flow or a custom flow.

Default Custom flow 

![PaymentSheet](https://b.stripecdn.com/docs-statics-srv/assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)

 

![Custom
flow](https://b.stripecdn.com/docs-statics-srv/assets/ios-multi-step.cd631ea4f1cd8cf3f39b6b9e1e92b6c5.png)

Displays a sheet to collect payment details and complete the payment. The button
in the sheet says Pay $X and completes the payment. Displays a sheet to collect
payment details only. The button in the sheet says Continue and returns the
customer to your app, where your own button completes payment. DefaultCustom
flow
### Initialize PaymentSheet

When you’re ready to take a payment, for example, when a customer checks out,
initialize the PaymentSheet with an `intentConfiguration`. The
`intentConfiguration` object contains details about the specific payment, such
as the amount and currency, and a `confirmHandler` callback.

```
import { useStripe } from '@stripe/stripe-react-native';
import {View, Button} from 'react-native';

export default function CheckoutScreen() {
 const { initPaymentSheet, presentPaymentSheet } = useStripe();

 const initializePaymentSheet = async () => {
 const { error } = await initPaymentSheet({
 merchantDisplayName: "Example, Inc.",
 intentConfiguration: {
 mode: {
 amount: 1099,
 currencyCode: 'USD',
 },
 confirmHandler: confirmHandler
 }
 });
 if (error) {
 // handle error
 }
 };

 useEffect(() => {
 initializePaymentSheet();
 }, []);

const confirmHandler = async (paymentMethod, shouldSavePaymentMethod,
intentCreationCallback) => {
 // explained later
 }

 const didTapCheckoutButton = async () => {
 // implement later
 }
 return (
 <View>
 <Button
 title="Checkout"
 onPress={didTapCheckoutButton}
 />
 </View>
 );
}
```

### Present PaymentSheet

Next, present the PaymentSheet. The `presentPaymentSheet` method resolves with a
promise when the customer finishes paying, and then the sheet is dismissed.

```
export default function CheckoutScreen() {
 // ...
 const didTapCheckoutButton = async () => {
 const { error } = await presentPaymentSheet();

 if (error) {
 if (error.code === PaymentSheetError.Canceled) {
 // Customer canceled - you should probably do nothing.
 } else {
// PaymentSheet encountered an unrecoverable error. You can display the error to
the user, log it, etc.
 }
 } else {
 // Payment completed - show a confirmation screen.
 }
 }
 // ...
}
```

### Confirm the payment

When the customer taps **Pay** in the PaymentSheet, it calls the callback you
passed to `initPaymentSheet` with a
[PaymentMethod.Result](https://stripe.dev/stripe-react-native/api-reference/interfaces/PaymentMethod.Result.html)
object representing the customer’s payment details.

Implement this method to send a request to your server. Your server creates a
PaymentIntent and returns its client secret (explained in the next step).

When the request returns, call the `intentCreationCallback` with your server
response’s client secret or an error. The PaymentSheet confirms the
PaymentIntent using the client secret.

```
export default function CheckoutScreen() {
 // ...

const confirmHandler = async (paymentMethod, shouldSavePaymentMethod,
intentCreationCallback) => {
 // Make a request to your own server.
 const response = await fetch(`${API_URL}/create-intent`, {
 method: 'POST',
 headers: {
 'Content-Type': 'application/json',
 }});
// Call the `intentCreationCallback` with your server response's client secret
or error
 const { client_secret, error } = await response.json();
 if (client_secret) {
 intentCreationCallback({clientSecret: client_secret});
 } else {
 intentCreationCallback({error});
 }
 }
 // ...
}
```

[Create a
PaymentIntentServer-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-submit-payment)
On your server, create a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) with an amount
and currency. You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow. To prevent malicious customers
from choosing their own prices, always decide how much to charge on the
server-side (a trusted environment) and not the client.

If the call succeeds, return the PaymentIntent [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret).
If the call fails, [handle the error](https://docs.stripe.com/error-handling)
and return an error message with a brief explanation for your customer.

#### Note

Verify that all IntentConfiguration properties match your PaymentIntent (for
example, `setup_future_usage`, `amount`, and `currency`).

```
require 'stripe'
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/create-intent' do
 data = JSON.parse request.body.read
 params = {
 amount: 1099,
 currency: 'usd',
# In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 automatic_payment_methods: {enabled: true},
 }
 begin
 intent = Stripe::PaymentIntent.create(params)
 {client_secret: intent.client_secret}.to_json
 rescue Stripe::StripeError => e
 {error: e.error.message}.to_json
 end
end
```

[Handle post-payment
eventsServer-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-post-payment)
Stripe sends a
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
event when the payment completes. Use the [Dashboard webhook
tool](https://dashboard.stripe.com/webhooks) or follow the [webhook
guide](https://docs.stripe.com/webhooks/quickstart) to receive these events and
run actions, such as sending an order confirmation email to your customer,
logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On
the client, the customer could close the browser window or quit the app before
the callback executes, and malicious clients could manipulate the response.
Setting up your integration to listen for asynchronous events is what enables
you to accept [different types of payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

In addition to handling the `payment_intent.succeeded` event, we recommend
handling these other events when collecting payments with the Payment Element:

EventDescriptionAction[payment_intent.succeeded](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.succeeded)Sent
when a customer successfully completes a payment.Send the customer an order
confirmation and fulfill their
order.[payment_intent.processing](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.processing)Sent
when a customer successfully initiates a payment, but the payment has yet to
complete. This event is most commonly sent when the customer initiates a bank
debit. It’s followed by either a `payment_intent.succeeded` or
`payment_intent.payment_failed` event in the future.Send the customer an order
confirmation that indicates their payment is pending. For digital goods, you
might want to fulfill the order before waiting for payment to
complete.[payment_intent.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent
when a customer attempts a payment, but the payment fails.If a payment
transitions from `processing` to `payment_failed`, offer the customer another
attempt to pay.[Test the
integration](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-test-the-integration)CardsBank
redirectsBank debitsCard numberScenarioHow to test4242424242424242The card
payment succeeds and doesn’t require authentication.Fill out the credit card
form using the credit card number with any expiration, CVC, and postal
code.4000002500003155The card payment requires
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number with any expiration, CVC,
and postal code.4000000000009995The card is declined with a decline code like
`insufficient_funds`.Fill out the credit card form using the credit card number
with any expiration, CVC, and postal code.6205500000000000004The UnionPay card
has a variable length of 13-19 digits.Fill out the credit card form using the
credit card number with any expiration, CVC, and postal code.
See [Testing](https://docs.stripe.com/testing) for additional information to
test your integration.

[OptionalEnable saved
cardsServer-sideClient-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-enable-saved-cards)[OptionalAllow
delayed payment
methodsClient-side](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-allow-delayed-payment-methods)[OptionalEnable
Apple
Pay](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-apple-pay)[OptionalEnable
card
scanning](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-card-scanning)[OptionalCustomize
the
sheet](https://docs.stripe.com/payments/mobile/accept-payment?platform=react-native#ios-customization)

## Links

- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)
- [React Native SDK](https://github.com/stripe/stripe-react-native)
- [native iOS](https://github.com/stripe/stripe-ios)
- [Android](https://github.com/stripe/stripe-android)
- [publishable key](https://docs.stripe.com/keys#obtain-api-keys)
- [live mode](https://docs.stripe.com/keys#test-live-modes)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing page](https://stripe.com/pricing/local-payment-methods)
-
[Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme)
- [Configure](https://reactnative.dev/docs/linking)
- [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app)
- [Android](https://developer.android.com/training/app-links/deep-linking)
-
[iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app)
-
[PaymentMethod.Result](https://stripe.dev/stripe-react-native/api-reference/interfaces/PaymentMethod.Result.html)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [handle the error](https://docs.stripe.com/error-handling)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
- [Dashboard webhook tool](https://dashboard.stripe.com/webhooks)
- [webhook guide](https://docs.stripe.com/webhooks/quickstart)
- [different types of payment
methods](https://stripe.com/payments/payment-methods-guide)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.succeeded)
-
[payment_intent.processing](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.processing)
-
[payment_intent.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Testing](https://docs.stripe.com/testing)