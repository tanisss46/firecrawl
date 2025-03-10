# Google Pay

## Learn how to accept payments using Google Pay.

Google Pay allows customers to make payments in your app or website using any
credit or debit card saved to their Google Account, including those from Google
Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request
any credit or debit card stored in your customer’s Google account.

Google Pay is fully compatible with Stripe’s products and features (for example,
recurring payments), allowing you to use it in place of a traditional payment
form whenever possible. Use it to accept payments for physical goods, donations,
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating), and so
on.

#### Google Pay terms

By integrating Google Pay, you agree to Google’s [terms of
service](https://payments.developers.google.com/terms/sellertos).

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Worldwide except India
- **Presentment currency**

See [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Wallet
- **Recurring payments**

Yes
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[Yes](https://docs.stripe.com/google-pay#disputed-payments)
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/google-pay#refunds)

## Using Stripe and Google Pay versus the Google Play billing system

For sales of physical goods and services, your app can accept Google Pay or any
other Stripe-supported payment method. Those payments are processed through
Stripe, and you only need to pay Stripe’s [processing
fees](https://stripe.com/pricing). However, in-app purchases of digital products
and content must use the [Google Play billing
system](https://developer.android.com/google/play/billing). Those payments are
processed by Google and are subject to their transaction fees.

For more information about which purchases must use the Google Play billing
system, see Google Play’s [developer
terms](https://support.google.com/googleplay/android-developer/answer/10281818).

AndroidReact NativeWeb
## Accept a payment using Google Pay in your Android app

`GooglePayLauncher`, part of the Stripe Android SDK, is the fastest and easiest
way to start accepting Google Pay in your Android apps.

## Prerequisites

To support Google Pay in Android, you need the following:

- A `minSdkVersion` of `19` or higher.
- A `compileSdkVersion` of `28` or higher.

Additionally, if you wish to test with your own device, you need to [add a
payment method to your Google
Account](https://support.google.com/wallet/answer/12058983?visit_id=637947092743186187-653786796&rd=1).

[Set up your integration](https://docs.stripe.com/google-pay#setup)
To use Google Pay, first enable the Google Pay API by adding the following to
the `<application>` tag of your **AndroidManifest.xml**:

```
<application>
 ...
 <meta-data
 android:name="com.google.android.gms.wallet.api.enabled"
 android:value="true" />
</application>
```

This guide assumes you’re using the latest version of the Stripe Android SDK.

```
dependencies {
 implementation 'com.stripe:stripe-android:21.6.0'
}
```

For more details, see Google Pay’s [Set up Google Pay
API](https://developers.google.com/pay/api/android/guides/setup) for Android.

[Add the Google Pay button](https://docs.stripe.com/google-pay#button)
Add the Google Pay button to your app by following [Google’s
tutorial](https://developers.google.com/pay/api/android/guides/tutorial#add-button).
This ensures you’re using the correct assets.

[Instantiate GooglePayLauncher](https://docs.stripe.com/google-pay#instantiate)
Next, create an instance of
[GooglePayLauncher](https://github.com/stripe/stripe-android/blob/master/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt)
in your `Activity` or `Fragment`. This must be done in `Activity#onCreate()`.

`GooglePayLauncher.Config` exposes both required and optional properties that
configure `GooglePayLauncher`. See `GooglePayLauncher.Config` for more details
on the configuration options.

```
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
 // fetch client_secret from backend
 private lateinit var clientSecret: String

 private lateinit var googlePayButton: PayButton

 override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)
 setContentView(R.layout.checkout_activity)

 PaymentConfiguration.init(this, PUBLISHABLE_KEY)

googlePayButton = /* TODO: Initialize button by following Google's guide. */

 val googlePayLauncher = GooglePayLauncher(
 activity = this,
 config = GooglePayLauncher.Config(
 environment = GooglePayEnvironment.Test,
 merchantCountryCode = "US",
 merchantName = "Widget Store"
 ),
 readyCallback = ::onGooglePayReady,
 resultCallback = ::onGooglePayResult
 )

 googlePayButton.setOnClickListener {
 // launch `GooglePayLauncher` to confirm a Payment Intent
 googlePayLauncher.presentForPaymentIntent(clientSecret)
 }
 }

 private fun onGooglePayReady(isReady: Boolean) {
 // implemented below
 }

 private fun onGooglePayResult(result: GooglePayLauncher.Result) {
 // implemented below
 }
}
```

After instantiating `GooglePayLauncher`, the `GooglePayLauncher.ReadyCallback`
instance is called with a flag indicating whether Google Pay is available and
ready to use. This flag can be used to update your UI to indicate to your
customer that Google Pay is ready to be used.

```
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
 // continued from above

 private lateinit var googlePayButton: PayButton

 private fun onGooglePayReady(isReady: Boolean) {
 googlePayButton.isEnabled = isReady
 }
}
```

[Launch GooglePayLauncher](https://docs.stripe.com/google-pay#launch-google-pay)
After Google Pay is available and your app has obtained a `PaymentIntent` or
`SetupIntent` client secret, launch `GooglePayLauncher` using the appropriate
method. When confirming a `PaymentIntent`, use
`GooglePayLauncher#presentForPaymentIntent(clientSecret)`. When confirming a
`SetupIntent`, use `GooglePayLauncher#presentForSetupIntent(clientSecret)`.

```
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
 // fetch client_secret from backend
 private lateinit var clientSecret: String

 private lateinit var googlePayButton: PayButton

 override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)

 // instantiate `googlePayLauncher`

 googlePayButton.setOnClickListener {
 // launch `GooglePayLauncher` to confirm a Payment Intent
 googlePayLauncher.presentForPaymentIntent(clientSecret)
 }
 }
}
```

[Handle the result](https://docs.stripe.com/google-pay#handle-result)
Finally, implement `GooglePayLauncher.ResultCallback` to handle the result of
the `GooglePayLauncher` operation.

The result can be `GooglePayLauncher.Result.Completed`,
`GooglePayLauncher.Result.Canceled`, or `GooglePayLauncher.Result.Failed`.

```
class CheckoutActivity : AppCompatActivity() {
 // continued from above

 private fun onGooglePayResult(result: GooglePayLauncher.Result) {
 when (result) {
 GooglePayLauncher.Result.Completed -> {
 // Payment succeeded, show a receipt view
 }
 GooglePayLauncher.Result.Canceled -> {
 // User canceled the operation
 }
 is GooglePayLauncher.Result.Failed -> {
 // Operation failed; inspect `result.error` for the exception
 }
 }
 }
}
```

[Going live with Google Pay](https://docs.stripe.com/google-pay#going-live)
Follow [Google’s
instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access)
to request production access for your app. Choose the integration type
**Gateway** when prompted, and provide screenshots of your app for review.

After your app has been approved, test your integration in production by setting
the environment to `GooglePayEnvironment.Production`, and launching Google Pay
from a signed, release build of your app. Remember to use your live mode [API
keys](https://docs.stripe.com/keys). You can use a `PaymentIntent` with
[capture_method =
manual](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
to process a transaction without capturing the payment.

## Creating a PaymentMethod

If you confirm your payment on your server, you can use
`GooglePayPaymentMethodLauncher` to only collect a `PaymentMethod` instead of
confirm payment.

```
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
 private lateinit var googlePayButton: PayButton

 override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)
 setContentView(R.layout.checkout_activity)

 PaymentConfiguration.init(this, PUBLISHABLE_KEY)

googlePayButton = /* TODO: Initialize button by following Google's guide. */

 val googlePayLauncher = GooglePayPaymentMethodLauncher(
 activity = this,
 config = GooglePayPaymentMethodLauncher.Config(
 environment = GooglePayEnvironment.Test,
 merchantCountryCode = "FR",
 merchantName = "Widget Store"
 ),
 readyCallback = ::onGooglePayReady,
 resultCallback = ::onGooglePayResult
 )

 googlePayButton.setOnClickListener {
 googlePayLauncher.present(
 currencyCode = "EUR",
 amount = 2500
 )
 }
 }

 private fun onGooglePayReady(isReady: Boolean) {
 googlePayButton.isEnabled = isReady
 }

 private fun onGooglePayResult(
 result: GooglePayPaymentMethodLauncher.Result
 ) {
 when (result) {
 is GooglePayPaymentMethodLauncher.Result.Completed -> {
 // Payment details successfully captured.
 // Send the paymentMethodId to your server to finalize payment.
 val paymentMethodId = result.paymentMethod.id
 }
 GooglePayPaymentMethodLauncher.Result.Canceled -> {
 // User canceled the operation
 }
 is GooglePayPaymentMethodLauncher.Result.Failed -> {
 // Operation failed; inspect `result.error` for the exception
 }
 }
 }
}
```

## Disputes

Users must authenticate payments with their Google Pay accounts, which reduces
the risk of fraud or unrecognized payments. However, users can still dispute
transactions after they complete payment. You can submit evidence to contest a
dispute directly. The dispute process is the same as that for card payments.
Learn how to [manage disputes](https://docs.stripe.com/disputes/responding).

### Liability shift for Google Pay charges

Google Pay supports [liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
globally. This is true automatically for users on Stripe-hosted products and
using Stripe.js. For Visa transactions outside of a Stripe-hosted product, you
must enable liability shift in the Google Pay & Wallet Console. To do so,
navigate to your *Google Pay & Wallet Console*, select *Google Pay API* in the
navigation bar on the left, and then enable *Fraud Liability Protection for Visa
Device Tokens* for liability shift protection.

There are three use cases of Google Pay transactions:

- If the user adds a card to the Google Pay app using their mobile device, this
card is saved as a Device Primary Account Number (DPAN), and it supports
liability shift by default.
- If the user adds a card to Chrome or a Google property (for example, YouTube,
or Play), it’s saved as a Funding Primary Account Number (FPAN). When you use
[3D Secure](https://docs.stripe.com/payments/3d-secure), we globally support
liability shift for all major networks, including Visa. You can customize
[Stripe Radar rules](https://docs.stripe.com/radar/rules#request-3d-secure) to
request activation of 3D Secure.
- If the user selects Google Pay as the payment method on an e-commerce site or
in an app that pays with Google Pay, the cards are saved as e-commerce tokens
that represent the cards on file. Neither liability shift nor 3D Secure are
supported for e-commerce tokens at this time.

For Sigma users, the `charges` table contains a `card_token_type` field that
indicates the Google Pay transaction type. An FPAN transaction sets the
`card_token_type` to `fpan`. DPAN and ecommerce token transactions set the
`card_token_type` to `dpan_or_ecommerce_token`.

## Refunds

You can partially or fully refund any successful Google Pay payment. The refund
process is the same as that for card payments. See [Refund and cancel
payments](https://docs.stripe.com/refunds) for instructions on initiating or
managing refunds.

## Test Google Pay

You can’t save Stripe test card information to Google Pay wallets. Instead,
Stripe recognizes when you’re using your test [API
keys](https://docs.stripe.com/keys), returning a successful test card token for
you to use. This allows you to make test payments using a live card without it
being charged.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [terms of service](https://payments.developers.google.com/terms/sellertos)
- [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [Yes](https://docs.stripe.com/google-pay#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/google-pay#refunds)
- [processing fees](https://stripe.com/pricing)
- [Google Play billing
system](https://developer.android.com/google/play/billing)
- [developer
terms](https://support.google.com/googleplay/android-developer/answer/10281818)
- [add a payment method to your Google
Account](https://support.google.com/wallet/answer/12058983?visit_id=637947092743186187-653786796&rd=1)
- [Set up Google Pay
API](https://developers.google.com/pay/api/android/guides/setup)
- [Google’s
tutorial](https://developers.google.com/pay/api/android/guides/tutorial#add-button)
-
[GooglePayLauncher](https://github.com/stripe/stripe-android/blob/master/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt)
- [Google’s
instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access)
- [API keys](https://docs.stripe.com/keys)
- [capture_method =
manual](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
- [manage disputes](https://docs.stripe.com/disputes/responding)
- [liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Stripe Radar rules](https://docs.stripe.com/radar/rules#request-3d-secure)
- [Refund and cancel payments](https://docs.stripe.com/refunds)