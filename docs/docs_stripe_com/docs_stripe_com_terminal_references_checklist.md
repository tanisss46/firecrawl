# Deployment checklist

## Use this checklist to help ensure a smooth deployment of Stripe Terminal.

Stripe Terminal requires integrating hardware and software to bring Stripe to
the physical world. As you develop your integration, refer to this checklist to
make sure you cover all the critical steps.

It’s fine to go out of order, but understanding the full scope of a Terminal
integration helps you connect all the pieces.

After following the integration guides for Stripe Terminal, check that your
application is set up correctly.

- Set up the ConnectionToken endpoint correctly
To handle the ConnectionToken lifecycle, set up an endpoint on your backend that
creates a ConnectionToken for your client application. Authenticate this
endpoint to control who can access your readers. Don’t hard-code the
ConnectionToken in your application—it prevents you from reconnecting to a
reader. To further control access to smart readers like the [Verifone
P400](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=smart)
and [BBPOS WisePOS
E](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=smart),
use [Locations](https://docs.stripe.com/terminal/fleet/locations-and-zones).
- Capture PaymentIntents
If you defined the PaymentIntent
[capture_method](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-capture_method)
as `manual`, the payment is authorized but not captured when the SDK returns a
processed PaymentIntent to your application. To complete collection of funds,
you must [capture the
PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment).

When your application receives a processed PaymentIntent from the SDK, make sure
it notifies your backend to capture the PaymentIntent.
- Make sure you can provide receipts to customers
Provide your customer with the option to receive a paper or email receipt. You
can use Stripe’s prebuilt receipts, or use receipt data from the Stripe API to
build custom receipts that are on-brand for your business. Test that you receive
a receipt when you create a live mode payment using your application.

If you provide your customers with [custom
receipts](https://docs.stripe.com/terminal/features/receipts#custom), save a
copy of each receipt as dispute evidence. If you use Stripe’s prebuilt receipts,
a copy of the receipt is saved automatically and available in the Dashboard.
- Set up a process to reconcile payments with your internal orders system
[Reconcile
payments](https://docs.stripe.com/terminal/payments/collect-card-payment#reconciling)
with your internal orders system on your server at the end of a day’s activity
to avoid unintended authorizations or un-captured funds:

- A user abandoning your application’s checkout flow early can result in an
un-captured PaymentIntent, which may appear to the cardholder as an unintended
authorization.
- Similarly, the request from your application notifying your backend to capture
the PaymentIntent may fail, resulting in incomplete collection of funds.
- Support updates for the BBPOS Chipper 2X BT
The [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt) does not
auto-update, so it’s important for your application to support updates. Although
they’re rare, updates usually contain important features or critical fixes. Make
sure your app supports the following:

- First, check for whether an update is available.
- If an update is available, display in the UI the estimated time to complete
the update, along with options to continue or cancel.
- While the update is in progress, have the UI tell the user to leave the reader
powered on and nearby. Block the user from navigating away from the page.
- Display a visual indicator of the update progress (for example, the percentage
or a progress bar).

Refer to our example applications
([iOS](https://github.com/stripe/stripe-terminal-ios),
[Android](https://github.com/stripe/stripe-terminal-android)) for a reference
UI.
- Support registering readers in the field
For smart readers like the [Verifone
P400](https://docs.stripe.com/terminal/readers/verifone-p400) and [BBPOS WisePOS
E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e), you must [register
the reader](https://docs.stripe.com/terminal/fleet/register-readers) to your
account before you can connect your application to the reader.

How you handle reader registration depends on your use case:

- **Deployment size**: For smaller deployments, [register each
reader](https://docs.stripe.com/terminal/fleet/register-readers) in the Stripe
Dashboard. For larger deployments that require shipping readers to various
locations, make sure site managers can add new readers to your company’s Stripe
account. Build a workflow into your application to let others register readers
to your Stripe account. The endpoint for [registering a
reader](https://docs.stripe.com/api/terminal/readers/create) must be called
server side. If you support registering readers from your client application,
the app must communicate with your backend to register the reader.
- **Using Connect**: If you use Connect [direct
charges](https://docs.stripe.com/connect/direct-charges), use the
`Stripe-Account` header to register the reader to the connected account. With
[destination charges](https://docs.stripe.com/connect/destination-charges),
register new readers [to the platform
account](https://docs.stripe.com/terminal/features/connect).
- Use Locations to group your readers
Create a Terminal
[Location](https://docs.stripe.com/api/terminal/locations/create) object for
each physical operating site at which your business accepts in-person payments.
You must register each reader to a location to ensure that it downloads the
proper regional configuration.

For smart readers, support specifying a location while [registering the
reader](https://docs.stripe.com/terminal/fleet/register-readers#smart-readers).
For Bluetooth readers, support specifying a location while [connecting to the
reader](https://docs.stripe.com/terminal/fleet/register-readers#bluetooth-readers).
- Support discovering multiple readers and provide helpful UI
Make sure your application can display an updating list of discovered readers,
with the label and/or serial number of each. Refer to our [example
applications](https://docs.stripe.com/terminal/example-applications) for a
sample UI.

If you expect your mobile app to be used with multiple Bluetooth readers, use
the [Bluetooth
Proximity](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#bluetooth-proximity)
discovery method. Include in your app instructions to hold the reader close to
the app device, and wait for it to begin flashing multiple colors. Make sure
your app’s UI allows canceling the reader discovery process.

If you use the [Verifone
P400](https://docs.stripe.com/terminal/readers/verifone-p400) or [BBPOS WisePOS
E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e), check that the
reader and the device running your application are both on the correct LAN.
Include in your application instructions for verifying the correct LAN.
- Make sure you’re on the latest release of the SDK
Stripe periodically releases updates which can include new functionality, bug
fixes, and security updates. Update your SDK as soon as a new version is
available. The currently available SDKs are:

- [Stripe Terminal Android
SDK](https://github.com/stripe/stripe-terminal-android/releases)
- [Stripe Terminal iOS
SDK](https://github.com/stripe/stripe-terminal-ios/releases)
- [Stripe Terminal JavaScript
SDK](https://docs.stripe.com/terminal/references/api/js-sdk#changelog)
- [Stripe Terminal React Native
SDK](https://github.com/stripe/stripe-terminal-react-native)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of
BBPOS Limited in the United States and/or other countries. The Verifone® name
and logo are either trademarks or registered trademarks of Verifone in the
United States and/or other countries. Use of the trademarks does not imply any
endorsement by BBPOS or Verifone.

## Links

- [Verifone
P400](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=smart)
- [Locations](https://docs.stripe.com/terminal/fleet/locations-and-zones)
-
[capture_method](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-capture_method)
- [capture the
PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment)
- [custom receipts](https://docs.stripe.com/terminal/features/receipts#custom)
- [Reconcile
payments](https://docs.stripe.com/terminal/payments/collect-card-payment#reconciling)
- [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)
- [iOS](https://github.com/stripe/stripe-terminal-ios)
- [Android](https://github.com/stripe/stripe-terminal-android)
- [Verifone P400](https://docs.stripe.com/terminal/readers/verifone-p400)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [register the reader](https://docs.stripe.com/terminal/fleet/register-readers)
- [registering a reader](https://docs.stripe.com/api/terminal/readers/create)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [to the platform account](https://docs.stripe.com/terminal/features/connect)
- [Location](https://docs.stripe.com/api/terminal/locations/create)
- [registering the
reader](https://docs.stripe.com/terminal/fleet/register-readers#smart-readers)
- [connecting to the
reader](https://docs.stripe.com/terminal/fleet/register-readers#bluetooth-readers)
- [example applications](https://docs.stripe.com/terminal/example-applications)
- [Bluetooth
Proximity](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#bluetooth-proximity)
- [Stripe Terminal Android
SDK](https://github.com/stripe/stripe-terminal-android/releases)
- [Stripe Terminal iOS
SDK](https://github.com/stripe/stripe-terminal-ios/releases)
- [Stripe Terminal JavaScript
SDK](https://docs.stripe.com/terminal/references/api/js-sdk#changelog)
- [Stripe Terminal React Native
SDK](https://github.com/stripe/stripe-terminal-react-native)