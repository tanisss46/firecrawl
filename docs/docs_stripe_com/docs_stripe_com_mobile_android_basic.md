# Android basic integrationDeprecated

## Accept cards with the Android SDK's prebuilt UI.

#### Note

We created an improved [payments
UI](https://docs.stripe.com/payments/accept-a-payment?platform=android) for
mobile apps with support for additional payment methods. We recommend using it
for your integration instead of this one.

If you want to migrate but are unable to, please [let us
know](https://github.com/stripe/stripe-android/issues).

Use this integration if you want a prebuilt UI that:

- Accepts credit cards and other payment methods
- Saves and displays cards for reuse
- Can be [customized to fit your app’s look and
feel](https://docs.stripe.com/mobile/android/basic#customize-ui) using an
Android theme
- Launches full-screen activities to collect payment details, shipping address,
and shipping method
- Allows your customer to choose Google Pay as a payment method

![PaymentMethodsActivity](https://b.stripecdn.com/docs-statics-srv/assets/android-payment-methods.1058cf4a3dcf9186e73a8ed12f31f070.png)

[PaymentMethodsActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-methods-activity/index.html)

![AddPaymentMethodActivity](https://b.stripecdn.com/docs-statics-srv/assets/android-add-card.cb06f4cf8f5f8e012a21ec6a26ca7c20.png)

[AddPaymentMethodActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-add-payment-method-activity/index.html)

![PaymentFlowActivity](https://b.stripecdn.com/docs-statics-srv/assets/android-shipping-address.3e2b1fc09358f86bfb401fa7e0128c8d.png)

[PaymentFlowActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-flow-activity/index.html)

These activities [can also be used
individually](https://docs.stripe.com/mobile/android/basic#use-individual-activities).
This integration requires both server and client-side steps to implement.

#### Note

Check out the example [Basic Integration
app](https://github.com/stripe-samples/sample-store-android) and
[backend](https://github.com/stripe/example-mobile-backend/blob/master/web.rb)
for a full implementation of this guide.

[Set up
StripeClient-sideServer-side](https://docs.stripe.com/mobile/android/basic#setup)
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

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open
source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your
[app/build.gradle](https://developer.android.com/studio/build/dependencies)
file:

```
plugins {
 id("com.android.application")
}

android { ... }

dependencies {
 // ...

 // Stripe Android SDK
 implementation("com.stripe:stripe-android:21.6.0")
}
```

#### Note

For details on the latest SDK release and past versions, see the
[Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To
receive notifications when a new release is published, [watch releases for the
repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable
key](https://dashboard.stripe.com/apikeys) so that it can make requests to the
Stripe API, such as in your `Application` subclass:

```
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
 override fun onCreate() {
 super.onCreate()
 PaymentConfiguration.init(
 applicationContext,
 "pk_test_TYooMQauvdEDq54NiTphI7jx"
 )
 }
}
```

#### Note

Use your [test mode](https://docs.stripe.com/keys#obtain-api-keys) keys while
you test and develop, and your [live
mode](https://docs.stripe.com/keys#test-live-modes) keys when you publish your
app.

[Set up an ephemeral
keyClient-sideServer-side](https://docs.stripe.com/mobile/android/basic#set-up-ephemeral-key)
In order for the SDK to save and retrieve credit cards for later use, create a
single Stripe [Customer](https://docs.stripe.com/api/customers) object for each
of your users. When you create a new user or account on your server, create a
corresponding Customer object at the same time, even if you don’t collect
payment information from your users when they sign up. This ensures that your
application has a matching Customer for each user.

For security, the Customer API is not directly accessible from the client.
Instead, your server provides the SDK with an ephemeral key—a short-lived API
key with restricted access to the Customer API. You can think of an ephemeral
key as a session, authorizing the SDK to retrieve and update a specific Customer
object s for the duration of the session.

### Server-side

To provide an ephemeral key to the SDK, expose a new API endpoint on your
backend. This endpoint should create an ephemeral key for the current Stripe
customer, and return the key’s unmodified response as JSON. When the SDK
requests an ephemeral key, it will specify the version of the Stripe API that it
expects the response to come from. Your endpoint must accept an `api_version`
parameter, and use the specified API version when creating the ephemeral key.
This ensures that the SDK always receives the correct ephemeral key response
from your backend. Consult our [Example
Backend](https://github.com/stripe/example-mobile-backend/blob/9ac448f8b5d49175d26c7b77fd6bd3c88703e838/web.rb#L25-L40)
to see this in practice.

```
curl https://api.stripe.com/v1/ephemeral_keys \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer"="{{CUSTOMER_ID}}" \
 -H "Stripe-Version: {{API_VERSION}}"
```

### Client-side

After you’ve added an ephemeral key endpoint to your backend, you’ll need a way
for your Android app to communicate with this endpoint. In your app, make your
API client class implement the
[EphemeralKeyProvider](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-ephemeral-key-provider/index.html)
interface, which defines a single method,
[createEphemeralKey()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-ephemeral-key-provider/create-ephemeral-key.html).
When implementing this method, pass the `apiVersion` parameter along to your
ephemeral keys endpoint. Refer to our [example
app](https://github.com/stripe/stripe-android/blob/72eb77b0e5a4c785131c7b04e3d64a6b79dc6b33/example/src/main/java/com/stripe/example/service/ExampleEphemeralKeyProvider.kt)
to see this in practice.

```
public class ExampleEphemeralKeyProvider implements EphemeralKeyProvider {
 private final BackendApi backendApi =
 RetrofitFactory.instance.create(BackendApi.class);
 private final CompositeDisposable compositeDisposable =
 new CompositeDisposable();

 @Override
 public void createEphemeralKey(
 @NonNull @Size(min = 4) String apiVersion,
 @NonNull final EphemeralKeyUpdateListener keyUpdateListener) {
 final Map<String, String> apiParamMap = new HashMap<>();
 apiParamMap.put("api_version", apiVersion);

 // Using RxJava2 for handling asynchronous responses
 compositeDisposable.add(backendApi.createEphemeralKey(apiParamMap)
 .subscribeOn(Schedulers.io())
 .observeOn(AndroidSchedulers.mainThread())
 .subscribe(
 response -> {
 try {
 final String rawKey = response.string();
 keyUpdateListener.onKeyUpdate(rawKey);
 } catch (IOException ignored) {
 }
 }));
 }
}
```

[Set up a
CustomerSessionClient-side](https://docs.stripe.com/mobile/android/basic#set-up-customer-session)
After creating an `EphemeralKeyProvider`, initialize a
[CustomerSession](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/index.html).
A `CustomerSession` talks to your backend to retrieve an ephemeral key for your
Customer with its `EphemeralKeyProvider`, and uses that key to manage retrieving
and updating the Customer’s payment methods on your behalf.

You can also use `CustomerSession` with your own custom UI to
[retrieve](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/retrieve-current-customer.html)
or
[refresh](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/update-current-customer.html)
the Customer, and
[list](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/get-payment-methods.html)
their payment methods,
[attach](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/attach-payment-method.html)
a payment method, or
[detach](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/detach-payment-method.html)
a payment method.

```
public class StoreActivity extends Activity {
 @Override
 protected void onCreate(@Nullable Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 CustomerSession.initCustomerSession(
 this,
 new ExampleEphemeralKeyProvider()
 );
 }
}
```

To reduce load times, preload your customer’s information by initializing
`CustomerSession` before they enter your payment flow.

If your current user logs out of the app, clear the current `CustomerSession`
singleton by calling `CustomerSession.endCustomerSession()`. When a new user
logs in, re-initialize the instance. On your backend, create and return a new
ephemeral key for the Customer object associated with the new user.

[Set up a
PaymentSessionClient-side](https://docs.stripe.com/mobile/android/basic#set-up-payment-session)
The core of this integration is the
[PaymentSession](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/index.html)
class. It uses `CustomerSession` to launch full-screen activities to collect and
store payment information, and can also be used to collect shipping info. Think
of it as the data source for your checkout activity—it handles asynchronously
retrieving the data you need, and notifies its `PaymentSessionListener` when
your UI should change.

To work with `PaymentSession`, you’ll need to:

- Create a `PaymentSessionConfig` object
- Implement a `PaymentSessionListener`

### PaymentSessionConfig

The `PaymentSessionConfig` object is created using a
[Builder](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session-config/-builder/index.html).
All of the `Builder`’s fields are optional. See the [API
reference](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session-config/-builder/index.html)
for details on each method.

```
public StoreActivity extends AppCompatActivity {

 @NonNull
 private PaymentSessionConfig createPaymentSessionConfig() {
 return PaymentSessionConfig.Builder()

 // hide the phone field on the shipping information form
 .setHiddenShippingInfoFields(
 ShippingInfoWidget.CustomizableShippingField.PHONE_FIELD
 )

 // make the address line 2 field optional
 .setOptionalShippingInfoFields(
ShippingInfoWidget.CustomizableShippingField.ADDRESS_LINE_TWO_FIELD
 )

 // specify an address to pre-populate the shipping information form
 .setPrepopulatedShippingInfo(ShippingInformation(
 new Address.Builder()
 .setLine1("123 Market St")
 .setCity("San Francisco")
 .setState("CA")
 .setPostalCode("94107")
 .setCountry("US")
 .build(),
 "Jenny Rosen",
 "4158675309"
 ))

 // collect shipping information
 .setShippingInfoRequired(true)

 // collect shipping method
 .setShippingMethodsRequired(true)

 // specify the payment method types that the customer can use;
 // defaults to PaymentMethod.Type.Card
 .setPaymentMethodTypes(
 Arrays.asList(PaymentMethod.Type.Card)
 )

 // only allow US and Canada shipping addresses
 .setAllowedShippingCountryCodes(new HashSet<>(
 Arrays.asList("US", "CA")
 ))

 // specify a layout to display under the payment collection form
 .setAddPaymentMethodFooter(R.layout.add_payment_method_footer)

 // specify the shipping information validation delegate
.setShippingInformationValidator(new AppShippingInformationValidator())

 // specify the shipping methods factory delegate
 .setShippingMethodsFactory(new AppShippingMethodsFactory())

 // if `true`, will show "Google Pay" as an option on the
 // Payment Methods selection screen
 .setShouldShowGooglePay(true)

 .build();
 }

 private static class AppShippingInformationValidator
 extends PaymentSessionConfig.ShippingInformationValidator {

 @Override
 public boolean isValid(
 @NonNull ShippingInformation shippingInformation
 ) {
 final Address address = shippingInformation.getAddress();
 return address != null && Locale.US.country == address.getCountry();
 }

 @NonNull
 public String getErrorMessage(
 @NonNull ShippingInformation shippingInformation
 ) {
 return "A US address is required";
 }
 }

 private static class AppShippingMethodsFactory
 extends PaymentSessionConfig.ShippingMethodsFactory {

 @Override
 public List<ShippingMethod> create(
 @NonNull ShippingInformation shippingInformation
 ) {
 returns Arrays.asList(
 new ShippingMethod(
 "UPS Ground",
 "ups-ground",
 0,
 "USD",
 "Arrives in 3-5 days"
 ),
 new ShippingMethod(
 "FedEx",
 "fedex",
 599,
 "USD",
 "Arrives tomorrow"
 )
 );
 }
 }
}
```

### PaymentSessionListener

After creating the `PaymentSessionConfig`, you’ll need to implement
`PaymentSessionListener`.

```
public class MyPaymentSessionListener
 implements PaymentSession.PaymentSessionListener {
 // Called whenever the PaymentSession's data changes,
// For example, when the user selects a new `PaymentMethod` or enters shipping
info.
 @Override
 public void onPaymentSessionDataChanged(@NonNull PaymentSessionData data) {
 if (data.getUseGooglePay()) {
 // customer intends to pay with Google Pay
 } else {
 final PaymentMethod paymentMethod = data.getPaymentMethod();
 if (paymentMethod != null) {
 // Display information about the selected payment method
 }
 }

 // Update your UI here with other data
 if (data.isPaymentReadyToCharge()) {
 // Use the data to complete your charge - see below.
 }
 }

 @Override
 public void onCommunicatingStateChanged(boolean isCommunicating) {
 }

 @Override
 public void onError(int errorCode, @NotNull String errorMessage) {
 }
}
```

This method should also check for whether or not the payment data is complete,
according to the `PaymentSessionConfig` specified. If you receive an update for
which `PaymentSessionData#isPaymentReadyToCharge()` returns true, you can
immediately send a message to your server to complete the charge.

#### `void onCommunicatingStateChanged(boolean isCommunicating)`

This method is called whenever the network communication state has changed. We
recommend showing a spinner or infinite progress bar when it is set to `true`

```
public class MyPaymentSessionListener
 implements PaymentSession.PaymentSessionListener {
 @Override
 public void onCommunicatingStateChanged(boolean isCommunicating) {
 if (isCommunicating) {
 // update UI to indicate that network communication is in progress
 } else {
 // update UI to indicate that network communication has completed
 }
 }
}
```

#### `void onError(int errorCode, @Nullable String errorMessage)`

This method is called whenever an error occurs when connecting to the Stripe
API. Make sure users can see the error messages, so display them in an alert
dialog.

### Initialize a PaymentSession

Having created your `PaymentSessionConfig` and `PaymentSessionListener`, you can
now
[initialize](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/init.html)
the `PaymentSession`. In the below example, we use anonymous classes to create
our listener and config for simplicity.

```
public class HostActivity extends Activity {
 private PaymentSession paymentSession;
 private Button startPaymentFlowButton;

 @Override
 protected void onCreate(@Nullable Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 paymentSession = new PaymentSession(
 this,
 new PaymentSessionConfig.Builder()
 .setPrepopulatedShippingInfo(getDefaultShippingInfo())
 .build()
 );
 setupPaymentSession();
 }

 private void setupPaymentSession() {
 paymentSession.init(
 new PaymentSession.PaymentSessionListener() {
 @Override
 public void onCommunicatingStateChanged(
 boolean isCommunicating
 ) {
 // update UI, such as hiding or showing a progress bar
 }

 @Override
 public void onError(
 int errorCode,
 @Nullable String errorMessage
 ) {
 // handle error
 }

 @Override
 public void onPaymentSessionDataChanged(
 @NonNull PaymentSessionData data
 ) {
 final PaymentMethod paymentMethod = data.getPaymentMethod();
 // use paymentMethod
 }
 }
 );
 startPaymentFlowButton.setEnabled(true);
 }

 @Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable
Intent data) {
 super.onActivityResult(requestCode, resultCode, data);
 if (data != null) {
 paymentSession.handlePaymentData(requestCode, resultCode, data);
 }
 }

 @NonNull
 private ShippingInformation getDefaultShippingInfo() {
 // optionally specify default shipping address
 return new ShippingInformation();
 }
}
```

[Collect the customer's payment and shipping
detailsClient-side](https://docs.stripe.com/mobile/android/basic#collect-details)
Once the `PaymentSession` has been initialized, you can use it to make the
following calls.

#### `void presentPaymentMethodSelection()`

![PaymentMethodsActivity](https://b.stripecdn.com/docs-statics-srv/assets/android-payment-methods.1058cf4a3dcf9186e73a8ed12f31f070.png)

[PaymentMethodsActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-methods-activity/index.html)

![AddPaymentMethodActivity](https://b.stripecdn.com/docs-statics-srv/assets/android-add-card.cb06f4cf8f5f8e012a21ec6a26ca7c20.png)

[AddPaymentMethodActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-add-payment-method-activity/index.html)

This method starts the `PaymentMethodsActivity` to allow the customer to choose
a saved payment method, using `CustomerSession` as its data source. If the **Add
new card** button is tapped, or there are no existing payment methods,
`AddPaymentMethodActivity` is launched to add a credit card.

#### `void presentShippingFlow()`

![PaymentFlowActivity](https://b.stripecdn.com/docs-statics-srv/assets/android-shipping-address.3e2b1fc09358f86bfb401fa7e0128c8d.png)

[PaymentFlowActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-flow-activity/index.html)

This method presents the PaymentFlowActivity to allow the user to enter shipping
information, if such information is required according to your
`PaymentSessionConfig`.

[Complete the
paymentClient-sideServer-side](https://docs.stripe.com/mobile/android/basic#complete-the-payment)
Once `PaymentSession#isPaymentReadyToCharge()` returns `true`, submit the
payment to Stripe using a [Payment
Intent](https://docs.stripe.com/payments/payment-intents). Stripe uses this
payment object to track and handle all the states of the payment—even when the
bank requires customer intervention, like additional card authentication—until
the payment completes.

### Server-side

On your server, make an endpoint that creates a `PaymentIntent` with an amount
and currency and returns its [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
to your client.

Always decide how much to charge on the server side, a trusted environment, as
opposed to the client. This prevents malicious customers from being able to
choose their own prices.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=1099 \
 -d "currency"="usd"
```

### Client-side

- Request a `PaymentIntent` from your server
- Assemble a
[ConfirmPaymentIntentParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-payment-intent-params/index.html)
object with the `PaymentIntent` client secret from your server and the id of
`PaymentSessionData#paymentMethod` obtained from
`PaymentSessionListenerImpl#onPaymentSessionDataChanged()`.
- Call the [Stripe
confirmPayment](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html)
method to confirm the payment.

```
public class CheckoutActivity extends Activity {
 private void confirmPayment(
 @NonNull String clientSecret,
 @NonNull String paymentMethodId
 ) {
 stripe.confirmPayment(
 this,
 ConfirmPaymentIntentParams.createWithPaymentMethodId(
 paymentMethodId,
 clientSecret
 )
 );
 }
}
```

When the payment completes, `onSuccess` is called and the value of the returned
PaymentIntent’s `status` is `Succeeded`. Any other value indicates the payment
was not successful. Inspect
[lastPaymentError](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-intent/index.html#com.stripe.android.model/PaymentIntent/lastPaymentError/#/PointingToDeclaration/)
to determine the cause. End the payment session by calling
`PaymentSession#onCompleted()`.

[Manage PaymentSession in a host
ActivityClient-side](https://docs.stripe.com/mobile/android/basic#manage)
In order to get updates for the `PaymentSessionData` object and to handle state
during Activity lifecycle, you’ll need to hook up your `PaymentSession` instance
to a few key parts of your host Activity lifecycle. The first is in
`onActivityResult()`

```
public class HostActivity extends Activity {
 @Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable
Intent data) {
 super.onActivityResult(requestCode, resultCode, data);
 paymentSession.handlePaymentData(requestCode, resultCode, data);
 }
}
```

This is all you need to do to get updates from the various activities launched
by `PaymentSession`. Any updates to the data are reported to the
[PaymentSessionListener](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/-payment-session-listener/index.html)
argument to
[PaymentSession#init()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/init.html).

```
public class HostActivity extends Activity {
 private PaymentSession paymentSession;

 // Can also be re-initialized in onRestoreInstanceState
 @Override
 public void onCreate(@Nullable Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);

 // other onCreate logic

 // Create the PaymentSession
 paymentSession = new PaymentSession(
 this,
 createPaymentSessionConfig()
 );

 // Attach your listener
 paymentSession.init(createPaymentSessionListener());
 }

 @NonNull
private PaymentSession.PaymentSessionListener createPaymentSessionListener() {
 return new PaymentSession.PaymentSessionListener() {
 @Override
 public void onCommunicatingStateChanged(
 boolean isCommunicating
 ) {
 // update UI, such as hiding or showing a progress bar
 }

 @Override
 public void onError(
 int errorCode,
 @NotNull String errorMessage
 ) {
 // handle error
 }

 @Override
 public void onPaymentSessionDataChanged(
 @NotNull PaymentSessionData data
 ) {
 data.getPaymentMethod();
 }
 };
 }

 @NonNull
 private PaymentSessionConfig createPaymentSessionConfig() {
 return new PaymentSessionConfig.Builder()
 .build();
 }
}
```

[Test the integration](https://docs.stripe.com/mobile/android/basic#test)
​​Several test cards are available for you to use in a sandbox to make sure this
integration is ready. Use them with any CVC and an expiration date in the
future.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000002500003155Requires authentication. Stripe triggers a modal asking
for the customer to authenticate.4000000000009995Always fails with a decline
code of `insufficient_funds`.
For the full list of test cards see our guide on
[testing](https://docs.stripe.com/testing).

[OptionalHandle post-payment
events](https://docs.stripe.com/mobile/android/basic#fulfillment)[OptionalUse
individual
activitiesClient-side](https://docs.stripe.com/mobile/android/basic#use-individual-activities)[OptionalCustomize
the UIClient-side](https://docs.stripe.com/mobile/android/basic#customize-ui)
## See also

- [About Stripe payments](https://docs.stripe.com/payments/about)
- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Stripe Android SDK Reference](https://stripe.dev/stripe-android)

## Links

- [payments
UI](https://docs.stripe.com/payments/accept-a-payment?platform=android)
- [let us know](https://github.com/stripe/stripe-android/issues)
-
[PaymentMethodsActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-methods-activity/index.html)
-
[AddPaymentMethodActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-add-payment-method-activity/index.html)
-
[PaymentFlowActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-flow-activity/index.html)
- [Basic Integration
app](https://github.com/stripe-samples/sample-store-android)
- [backend](https://github.com/stripe/example-mobile-backend/blob/master/web.rb)
- [Register now](https://dashboard.stripe.com/register)
- [Stripe Android SDK](https://github.com/stripe/stripe-android)
- [fully documented](https://stripe.dev/stripe-android/)
- [app/build.gradle](https://developer.android.com/studio/build/dependencies)
- [Releases](https://github.com/stripe/stripe-android/releases)
- [watch releases for the
repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository)
- [publishable key](https://dashboard.stripe.com/apikeys)
- [test mode](https://docs.stripe.com/keys#obtain-api-keys)
- [live mode](https://docs.stripe.com/keys#test-live-modes)
- [Customer](https://docs.stripe.com/api/customers)
- [Example
Backend](https://github.com/stripe/example-mobile-backend/blob/9ac448f8b5d49175d26c7b77fd6bd3c88703e838/web.rb#L25-L40)
-
[EphemeralKeyProvider](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-ephemeral-key-provider/index.html)
-
[createEphemeralKey()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-ephemeral-key-provider/create-ephemeral-key.html)
- [example
app](https://github.com/stripe/stripe-android/blob/72eb77b0e5a4c785131c7b04e3d64a6b79dc6b33/example/src/main/java/com/stripe/example/service/ExampleEphemeralKeyProvider.kt)
-
[CustomerSession](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/index.html)
-
[retrieve](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/retrieve-current-customer.html)
-
[refresh](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/update-current-customer.html)
-
[list](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/get-payment-methods.html)
-
[attach](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/attach-payment-method.html)
-
[detach](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/detach-payment-method.html)
-
[PaymentSession](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/index.html)
-
[Builder](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session-config/-builder/index.html)
-
[initialize](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/init.html)
- [Payment Intent](https://docs.stripe.com/payments/payment-intents)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
-
[ConfirmPaymentIntentParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-payment-intent-params/index.html)
- [Stripe
confirmPayment](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html)
-
[lastPaymentError](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-intent/index.html#com.stripe.android.model/PaymentIntent/lastPaymentError/#/PointingToDeclaration/)
-
[PaymentSessionListener](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/-payment-session-listener/index.html)
- [testing](https://docs.stripe.com/testing)
- [About Stripe payments](https://docs.stripe.com/payments/about)
- [Stripe Android SDK Reference](https://stripe.dev/stripe-android)