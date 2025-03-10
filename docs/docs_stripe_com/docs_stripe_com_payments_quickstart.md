[subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements),
and other Stripe products, [compare payment
integrations](https://docs.stripe.com/payments/online-payments#compare-features-and-availability).

#### Interested in using Stripe Tax, discounts, shipping, or currency conversion?

We’re developing a Payment Element integration that manages tax, discounts,
shipping, and currency conversion. Read the [Build a checkout
page](https://docs.stripe.com/checkout/custom/quickstart) guide to learn more.

Download full appDon't code? Use Stripe’s [no-code
options](https://docs.stripe.com/no-code) or get help from [our
partners](https://stripe.partners/).1Set up the server
### Install the Stripe Ruby library

Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a PaymentIntent

Add an endpoint on your server that creates a
[PaymentIntent](https://docs.stripe.com/api/payment_intents). A PaymentIntent
tracks the customer’s payment lifecycle, keeping track of any failed payment
attempts and ensuring the customer is only charged once. Return the
PaymentIntent’s [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
in the response to finish the payment on the client.

Server
### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic
payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods).
You can update and configure payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code
required. Stripe filters payment methods based on eligibility and payment method
preferences, then orders and displays them by probability based on factors
including amount, currency, and buyer location.

Server2Build a checkout screen on the client
### Install the SDK

The Stripe Android SDK is [open
source](https://github.com/stripe/stripe-android) and [fully
documented](https://stripe.dev/stripe-android/) and compatible with devices
running Android 5.0 (API level 21) and above.

To install the SDK, add `stripe-android` to the dependencies block of your
`build.gradle` file:

```
implementation 'com.stripe:stripe-android:21.6.0'
```

#### Note

For details on the latest SDK release and past versions, see the [Releases
page](https://github.com/stripe/stripe-android/releases) on GitHub.

Client
### Setup the SDK

Configure the Stripe SDK with your Stripe [publishable API
key](https://docs.stripe.com/keys#obtain-api-keys). Hardcoding the publishable
API key in the SDK is for demonstration only. In a production app, you must
retrieve the API key from your server.

Client
### Fetch a PaymentIntent

Make a request to your server for a PaymentIntent as soon as the view loads.
Store a reference to the PaymentIntent’s [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
returned by the server; the Payment Sheet uses this secret to complete the
payment later.

Client3Complete the payment on the client
### Configure and present the Payment Sheet

Create a `PaymentSheet` instance using the client secret retrieved earlier, and
present it from your view controller.

Use the `PaymentSheet.Configuration` struct for
[customizing](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html)
the Payment Sheet.

Client
### Handle the payment result

Use the completion block for handling the payment result.

If payment fails with an [error](https://docs.stripe.com/error-codes), display
the appropriate message to your customer so they can take action and try again.
If no error has occurred, tell your customer that the payment was successful.

Client4Test the integration
### Make a test payment

To verify that your integration works, make a test payment using [test payment
details](https://docs.stripe.com/payments/accept-a-payment?platform=android#android-test-the-integration).

### See your payment in the Dashboard

Navigate to the [Stripe Dashboard](https://dashboard.stripe.com/test/payments)
to see your test payment.

## Accept payments and enhance your integration

You’re ready to accept payments with Stripe. Continue with the steps below to
add more features.

### Automate tax collection

Calculate and collect the right amount of tax on your Stripe transactions.
Before using Stripe Tax, you need to activate it in the
[Dashboard](https://dashboard.stripe.com/settings/tax/activate). Learn more
about [Stripe Tax](https://docs.stripe.com/tax) and [how to add it to your
Payments integration](https://docs.stripe.com/tax/custom).

### Allow delayed payment methods

Some payment methods can’t guarantee that you’ll receive funds from your
customer at the end of the check out because they take time to settle (for
example, most bank debits, such as SEPA or ACH) or require customer action to
complete (for example, OXXO, Konbini, Boleto). Use this flag to enable delayed
payment methods.

If you enable this feature, make sure your server integration listens to
[webhooks](https://docs.stripe.com/payments/payment-methods#payment-notification)
for notifications on whether payment has succeeded or not.

### Add Google Pay support

### Customize the primary button color

Consider using a custom color for the primary button that better matches your
brand or app’s visual identity.

### Enable card scanning

Card scanning can help increase your conversion rate by removing the friction of
manual card entry. To enable card scanning, add `stripecardscan` to the
`dependencies` block of your
[app/build.gradle](https://developer.android.com/studio/build/dependencies)
file:

```
implementation 'com.stripe:stripecardscan:21.6.0'
```

### Save payment details after payment

Often used by SaaS or e-commerce businesses with recurring customers.

### Collect addresses using the Address Element

Collect local and international shipping or billing addresses from your
customers.

If you use the Address Element, you can optionally use the [Google Places
SDK](https://developers.google.com/maps/documentation/places/android-sdk/overview)
to fetch address autocomplete suggestions. To enable autocomplete suggestions,
add `places` to the dependency block of your
[app/build.gradle](https://developer.android.com/studio/build/dependencies)
file:

```
implementation 'com.google.android.libraries.places:places:2.6.0'
```

## Next steps

#### [Payouts](https://docs.stripe.com/payouts)

Learn how to move funds out of your Stripe account into your bank account.

#### [Refunds](https://docs.stripe.com/refunds)

Handle requests for refunds by using the Stripe API or Dashboard.

#### [Fulfillment](https://docs.stripe.com/webhooks/quickstart)

Create an event destination to send events to your webhook endpoint to fulfill
orders after a payment succeeds, and to handle other critical events.

server.rbMyApp.ktCheckoutActivity.ktDownload
```
require 'sinatra'require 'stripe'# This is a public sample test API key.# Don’t
submit any personally identifiable information in requests made with this key.#
Sign in to see your own test API key embedded in code samples.Stripe.api_key =
'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
set :static, trueset :port, 4242
# Securely calculate the order amountdef calculate_order_amount(_items) # Calculate the order total on the server to prevent # people from directly manipulating the amount on the client _items.sum {|h| h['amount']}end
# An endpoint to start the payment processpost '/create-payment-intent' do content_type 'application/json' data = JSON.parse(request.body.read)
# Create a PaymentIntent with amount and currency payment_intent =
Stripe::PaymentIntent.create( amount: calculate_order_amount(data['items']),
currency: 'usd', # In the latest version of the API, specifying the
`automatic_payment_methods` parameter is optional because Stripe enables its
functionality by default. automatic_payment_methods: { enabled: true, }, )
 { clientSecret: payment_intent.client_secret, }.to_jsonend

```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)
- [Web](https://docs.stripe.com/payments/elements)
- [Mobile](https://docs.stripe.com/payments/mobile)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?&ui=elements)
-
[subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements)
- [compare payment
integrations](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
- [Build a checkout page](https://docs.stripe.com/checkout/custom/quickstart)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [open source](https://github.com/stripe/stripe-android)
- [fully documented](https://stripe.dev/stripe-android/)
- [Releases page](https://github.com/stripe/stripe-android/releases)
- [publishable API key](https://docs.stripe.com/keys#obtain-api-keys)
-
[customizing](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html)
- [error](https://docs.stripe.com/error-codes)
- [test payment
details](https://docs.stripe.com/payments/accept-a-payment?platform=android#android-test-the-integration)
- [Stripe Dashboard](https://dashboard.stripe.com/test/payments)
- [Dashboard](https://dashboard.stripe.com/settings/tax/activate)
- [Stripe Tax](https://docs.stripe.com/tax)
- [how to add it to your Payments
integration](https://docs.stripe.com/tax/custom)
-
[webhooks](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [app/build.gradle](https://developer.android.com/studio/build/dependencies)
- [Google Places
SDK](https://developers.google.com/maps/documentation/places/android-sdk/overview)
- [Payouts](https://docs.stripe.com/payouts)
- [Refunds](https://docs.stripe.com/refunds)
- [Fulfillment](https://docs.stripe.com/webhooks/quickstart)