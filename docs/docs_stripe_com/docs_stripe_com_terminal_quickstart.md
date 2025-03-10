partners](https://stripe.partners/).1 Set up the server
### Install the Stripe Ruby library

Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a ConnectionToken endpoint

To connect to a reader, your backend needs to give the SDK permission to use the
reader with your Stripe account by providing it with the secret from a
[ConnectionToken](https://docs.stripe.com/api/terminal/connection_tokens). Your
backend should only create connection tokens for clients that it trusts. ​​If
you’re using Stripe Connect, you should also [scope the connection
token](https://docs.stripe.com/terminal/features/connect) to the relevant
connected accounts. ​​If using locations, you should [pass a location
ID](https://docs.stripe.com/terminal/fleet/locations-and-zones#connection-tokens)
when creating the connection token to control access to readers.

Server2 Set up the SDK
### Organize your readers

[Create locations](https://docs.stripe.com/terminal/fleet/locations-and-zones)
to organize your readers. Locations group readers and allows them to
automatically download the reader configuration needed for their region of use.

Server
### Install the SDK

To install the SDK, add stripeterminal to the dependencies block of your
build.gradle file.

GradleGitHub
Add the dependencies to your build.gradle file:

```
dependencies {
 // ...

 // Stripe Terminal SDK
 implementation 'com.stripe:stripeterminal:4.2.0'
}
```

Client
### Verify ACCESS_FINE_LOCATION permission

Add a check to make sure that the `ACCESS_FINE_LOCATION` permission is enabled
in your app.

Client
### Verify user location permission

Override the `onRequestPermissionsResult` method in your app and check the
permission result to verify that the app user grants location permission.

Client
### Fetch ConnectionToken

Implement the ConnectionTokenProvider interface in your app, which defines a
single function that requests a connection token from your backend.

Client
### Configure TerminalApplicationDelegate

To prevent memory leaks and ensure proper cleanup of long-running Terminal SDK
processes, your application must subclass `Application` and call out to the
`TerminalApplicationDelegate` from the `onCreate` method.

Client
### Initialize the SDK

To get started, provide the current application context, the
ConnectionTokenProvider, and a TerminalListener object.

Client3 Connect to the simulated reader
### Discover readers

The Stripe Terminal SDK comes with a built-in simulated card reader, so you can
develop and test your app without connecting to physical hardware. To use the
simulated reader, call <code>discoverReaders</code> to search for readers, with
the simulated option set to true.

Client
### Connect to the simulated reader

When `discoverReaders` returns a result, call `connectBluetoothReader` to
connect to the simulated reader.

Client4 Collecting Payments
### Create a PaymentIntent

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents) object
using the SDK. A PaymentIntent tracks the customer’s payment lifecycle, keeping
track of any failed payment attempts and ensuring the customer is only charged
once.

Client
### Collect payment method details

Call `collectPaymentMethod` with the PaymentIntent’s client secret to collect a
payment method. When connected to the simulated reader calling this method
immediately updates the PaymentIntent object with a [simulated test
card](https://docs.stripe.com/terminal/references/testing#simulated-test-cards).
When connected to a physical reader the connected reader waits for a card to be
presented.

Client
### Confirm the payment

After successfully collecting payment method data, call `confirmPaymentIntent`
with the updated PaymentIntent to confirm the payment. A successful call results
in a PaymentIntent with a status of `requires_capture` for manual capture or
`succeeded` for automatic capture.

Client
### Create an endpoint to capture the PaymentIntent

Create an endpoint on your backend that accepts a PaymentIntent ID and sends a
request to the Stripe API to capture it.

Server
### Capture the PaymentIntent

If you defined `capture_method` as `manual` during PaymentIntent creation, the
SDK returns an authorized but not captured PaymentIntent to your application.
When the PaymentIntent status is `requires_capture`, notify your backend to
capture the PaymentIntent. In your request send the PaymentIntent ID. To ensure
the application fee captured is correct for connected accounts, inspect each
`PaymentIntent` and modify the application fee, if needed, prior to manually
capturing the payment.

Client5 Test the integration
### Run the application

Run your server and go to [localhost:4242](http://localhost:4242/).

`ruby server.rb`Server
### Make a test payment

Use
[amounts](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
ending in the following special values to test your integration.

Payment succeeds00Payment is declined01Client
## Next steps

#### [Connecting to a reader](https://docs.stripe.com/terminal/payments/connect-reader)

Learn what it means to connect your app to a reader.

#### [Fleet management](https://docs.stripe.com/terminal/fleet/locations-and-zones)

Group and manage a fleet of readers by physical location.

#### [Connect](https://docs.stripe.com/terminal/features/connect)

Integrate Stripe Terminal with your Connect platform.

Was this page
helpful?server.rbMainActivity.ktTokenProvider.ktStripeTerminalApplication.ktReaderAdapter.ktApiClient.ktBackendService.ktTerminalEventListener.ktTerminalBluetoothReaderListener.ktConnectionToken.ktServerPaymentIntent.ktbuild.gradleDownload
```
require 'sinatra'require 'stripe'
# This is a public sample test API key.# Don’t submit any personally identifiable information in requests made with this key.# Sign in to see your own test API key embedded in code samples.Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
set :root, File.dirname(__FILE__)set :public_folder, -> { File.join(root,
'public') }set :static, trueset :port, 4242
def create_location Stripe::Terminal::Location.create({ display_name: 'HQ',
address: { line1: '1272 Valencia Street', city: 'San Francisco', state: 'CA',
country: 'US', postal_code: '94110', } })end
get '/' do redirect '/index.html'end

# The ConnectionToken's secret lets you connect to any Stripe Terminal reader# and take payments with your Stripe account.# Be sure to authenticate the endpoint for creating connection tokens.post '/connection_token' do content_type 'application/json'
connection_token = Stripe::Terminal::ConnectionToken.create {secret:
connection_token.secret}.to_jsonend
post '/create_payment_intent' do content_type 'application/json' data =
JSON.parse(request.body.read)
# For Terminal payments, the 'payment_method_types' parameter must include #
'card_present'. # To automatically capture funds when a charge is authorized, #
set `capture_method` to `automatic`. intent = Stripe::PaymentIntent.create(
amount: data['amount'], currency: 'usd', payment_method_types: [ 'card_present',
], capture_method: 'manual', )
 intent.to_jsonend

post '/capture_payment_intent' do data = JSON.parse(request.body.read)
 intent = Stripe::PaymentIntent.capture(data['payment_intent_id'])
 intent.to_jsonend

```

## Links

- [text version of this
guide](https://docs.stripe.com/terminal/payments/setup-sdk)
- [View the text-based
guide](https://docs.stripe.com/terminal/payments/setup-integration)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [ConnectionToken](https://docs.stripe.com/api/terminal/connection_tokens)
- [scope the connection
token](https://docs.stripe.com/terminal/features/connect)
- [pass a location
ID](https://docs.stripe.com/terminal/fleet/locations-and-zones#connection-tokens)
- [Create locations](https://docs.stripe.com/terminal/fleet/locations-and-zones)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [simulated test
card](https://docs.stripe.com/terminal/references/testing#simulated-test-cards)
- [localhost:4242](http://localhost:4242)
-
[amounts](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
- [Connecting to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)