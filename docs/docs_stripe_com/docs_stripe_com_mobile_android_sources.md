# Getting started with Sources in the Android SDKDeprecated

## Learn how to use Sources in your Android application.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently handle any local payment methods using the Sources
API, you must [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

While we don’t plan to remove support for card payments, we recommend replacing
any use of the Sources API with the [PaymentMethods
API](https://docs.stripe.com/api/payment_methods), which provides access to our
latest features and payment method types.

Creating a payment using [Sources](https://docs.stripe.com/sources) with the
Android SDK is a multi-step process:

- [Create a Source
object](https://docs.stripe.com/mobile/android/sources#create-source-object)
that represents your customer’s payment method.
- [Check if further action is
required](https://docs.stripe.com/mobile/android/sources#check-if-further-action-is-required)
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
[Create a Source
object](https://docs.stripe.com/mobile/android/sources#create-source-object)
To create a `Source` object, use the appropriate creation method for your Source
type.

-
[SourceParams#createBancontactParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-bancontact-params.html)
-
[SourceParams#createCardParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-card-params.html)
-
[SourceParams#createGiropayParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-giropay-params.html)
-
[SourceParams#createIdealParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-ideal-params.html)
-
[SourceParams#createP24Params()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-p24-params.html)
-
[SourceParams#createSepaDebitParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sepa-debit-params.html)
-
[SourceParams#createSofortParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sofort-params.html)
-
[SourceParams#createThreeDSecureParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-three-d-secure-params.html)

```
final Stripe stripe = new Stripe(getContext(),
 "pk_test_TYooMQauvdEDq54NiTphI7jx");
Card card = cardInputWidget.getCard();
SourceParams cardSourceParams = SourceParams.createCardParams(card);
// The asynchronous way to do it. Call this method on the main thread.
stripe.createSource(
 cardSourceParams,
 new ApiResultCallback<Source>() {
 @Override
 public void onSuccess(@NonNull Source source) {
 // Store the source somewhere, use it, etc
 }
 @Override
 public void onError(@NonNull Exception error) {
 // Tell the user that something went wrong
 }
 });

// The synchronous way to do it (DON'T DO BOTH)
Source source = stripe.createSourceSynchronous(cardSourceParams);
```

Each method requires parameters unique to the payment type. Refer to the
appropriate [payment
methods](https://docs.stripe.com/sources#supported-payment-methods)
documentation to find out what these are.

Once you have a
[SourceParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/index.html)
object, create a source with either the
[Stripe#createSource()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-source.html)
or
[Stripe#createSourceSynchronous()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-source-synchronous.html),
depending on whether you prefer to manage threading yourself.

#### Warning

Do not call `Stripe#createSourceSynchronous()` on the UI thread as this will
crash. All methods labeled “Synchronous” are blocking and meant to be performed
on a separate thread. Similarly, you must call `createSource` on the UI thread,
as Android’s `AsyncTask` must be launched from the main thread.

[Check if further action is required from your
customer](https://docs.stripe.com/mobile/android/sources#check-if-further-action-is-required)
Some payment methods require your customer to complete a certain action before
the source can be used in a charge request. For instance, customers using
[giropay](https://docs.stripe.com/sources/giropay) must be
[redirected](https://docs.stripe.com/mobile/android/sources#redirecting-your-customer)
to their online banking service to authorize the payment.

```
SourceParams giropayParams = SourceParams.createGiropayParams(
 100,
 "Customer Name",
 "yourapp://post-authentication-return-url",
 "a purchase description");
// Note: this is a synchronous method -- you should not run it on the UI thread
Source giropaySource = stripe.createSourceSynchronous(giropayParams);
if (Source.REDIRECT.equals(giropaySource.getFlow())) {
 String redirectUrl = giropaySource.getRedirect().getUrl();
 // then go to this URL, as shown below.
}
```

For sources that require redirecting your customer, you must specify a return
URL when creating the source. This redirect URL should be unique and used
consistently for your application. Do not use the same redirect URL in other
applications, as it can result in a payment attempt that opens the wrong
application after the redirect.

#### Note

If you would like to accept card payments that are verified with [3D
Secure](https://docs.stripe.com/payments/3d-secure), your integration should use
the [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
instead of sources. Refer to the [Payment Methods API
documentation](https://docs.stripe.com/payments/payment-methods) to determine if
the specific payment methods you wish to use are supported.

## Redirect your customer to authorize a source

For sources that require your customer to complete an action (for example,
verify using 3D Secure), redirect the customer out of your application to
complete this step.

```
String externalUrl = mThreeDSource.getRedirect().getUrl();
// We suggest popping up a dialog asking the user
// to tap to go to their browser so they're not
// surprised when they leave your application.
Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(externalUrl));
startActivity(browserIntent);
```

After the customer has completed the required action, they’re redirected to the
URL that was provided when creating the source.

When declaring your activity that creates redirect-based sources, list an
`intent-filter` item in your `AndroidManifest.xml` file. This allows you to
accept links into your application. Your activity must include
`android:launchMode="singleTask"` or else a new copy of it is opened when your
customer comes back from the browser.

```
<activity
 android:name=".activity.PollingActivity"
 android:launchMode="singleTask"
 android:theme="@style/SampleTheme">
 <intent-filter>
 <action android:name="android.intent.action.VIEW"/>
 <category android:name="android.intent.category.DEFAULT"/>
 <category android:name="android.intent.category.BROWSABLE"/>
 <data
 android:scheme="yourapp"
 android:host="post-authentication-return-url"/>
 </intent-filter>
</activity>
```

To receive information from this event, listen for your activity getting started
back up with a new Intent using the `onNewIntent` lifecycle method.

```
@Override
protected void onNewIntent(Intent intent) {
 super.onNewIntent(intent);
 if (intent.getData() != null && intent.getData().getQuery() != null) {
 // The client secret and source ID found here is identical to
 // that of the source used to get the redirect URL.

 String host = intent.getData().getHost();
 // Note: you don't have to get the client secret
 // and source ID here. they're the same as the
 // values already in your source.
String clientSecret = intent.getData().getQueryParameter(QUERY_CLIENT_SECRET);
 String sourceId = intent.getData().getQueryParameter(QUERY_SOURCE_ID);
 if (clientSecret != null
 && sourceId != null
 && clientSecret.equals(redirectSource.getClientSecret())
 && sourceId.equals(redirectSource.getId())) {
 // Then this is a redirect back for the original source.
 // You should poll your own backend to update based on
// source status change webhook events it may receive, and display the results
 // of that here.
 }
// If you had a dialog open when your user went elsewhere, remember to close it
here.
 mRedirectDialogController.dismissDialog();
 }
}
```

If you’d like more help, check out the [example
app](https://github.com/stripe/stripe-android/tree/master/example) on Github
that demonstrates creating a payment using several different payment methods.

## See also

- [Using Payment Intents on
Android](https://docs.stripe.com/payments/accept-a-payment?integration=elements)
- [Supported payment methods](https://docs.stripe.com/sources)

## Links

- [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [PaymentMethods API](https://docs.stripe.com/api/payment_methods)
- [installed and
configured](https://docs.stripe.com/payments/accept-a-payment-charges?platform=android)
- [Sources](https://docs.stripe.com/sources)
- [webhooks](https://docs.stripe.com/webhooks)
- [Android SDK reference](https://stripe.dev/stripe-android)
-
[SourceParams#createBancontactParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-bancontact-params.html)
-
[SourceParams#createCardParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-card-params.html)
-
[SourceParams#createGiropayParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-giropay-params.html)
-
[SourceParams#createIdealParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-ideal-params.html)
-
[SourceParams#createP24Params()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-p24-params.html)
-
[SourceParams#createSepaDebitParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sepa-debit-params.html)
-
[SourceParams#createSofortParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sofort-params.html)
-
[SourceParams#createThreeDSecureParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-three-d-secure-params.html)
- [payment methods](https://docs.stripe.com/sources#supported-payment-methods)
-
[SourceParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/index.html)
-
[Stripe#createSource()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-source.html)
-
[Stripe#createSourceSynchronous()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-source-synchronous.html)
- [giropay](https://docs.stripe.com/sources/giropay)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Payment Methods API
documentation](https://docs.stripe.com/payments/payment-methods)
- [example app](https://github.com/stripe/stripe-android/tree/master/example)
- [Using Payment Intents on
Android](https://docs.stripe.com/payments/accept-a-payment?integration=elements)