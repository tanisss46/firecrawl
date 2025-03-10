# Collect card payments while offlinePublic preview

## Collect card payments with intermittent, limited, or no internet connectivity.

Bluetooth readersInternet readersiOSAndroidReact Native
The Terminal SDK allows your application to continue collecting payments using a
mobile reader without a network connection.

#### Warning

When operating offline, payment information is collected at the time of sale,
and authorization is only attempted after connectivity is restored and the
payment is forwarded. You, as the user, assume all decline risk of the
transaction. If the issuer declines the offline transaction, there’s no way to
recover the funds, and you might not receive payment from the customer for goods
or services already provided.

To reduce the chances of an issuer decline, you’re encouraged to:

- Reestablish internet connectivity as soon as possible to record the payments
to Stripe.
- Restrict transactions if they exceed a certain amount.
- [Fail all offline
payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#managing-risk-while-offline)
if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect,
process, and capture the payment. Your device can transition from online to
offline at any step in the process.

- [Enable offline
mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#enable-offline-mode)
- [Connect to a reader while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#connect-while-offline)
- [Handle offline
events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#handle-offline-events)
- [Create a PaymentIntent while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#create-payment-intent)
- [Collect a payment
method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#collect-payment-method)
- [Confirm the
payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#confirm-payment)
- [Wait for payments to
forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#wait-for-forward)
- [Capture the
payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#capture-payment)
- [Examine offline
payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#examine-offline)
[Enable offline
mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#enable-offline-mode)
To use offline mode, your application needs to consume version `3.3.0` or later
of the Terminal iOS SDK.

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration) object
to enable offline mode for the [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt), [Stripe Reader
M2](https://docs.stripe.com/terminal/readers/stripe-m2) or [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)
devices at your `Location`.

```
curl https://api.stripe.com/v1/terminal/configurations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "offline[enabled]"=true
```

After you enable offline mode on a `Configuration` object, you can [assign
it](https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api#create-a-configuration-for-an-individual-location)
to a `Location`. You can also enable offline mode by default for all `Locations`
by updating the
[default](https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api#retrieve-the-account-default-configuration)
`Configuration` object for your account. Configuration API changes can take
several minutes to propagate to your SDK and reader, and require you to
disconnect from and reconnect to your reader to take effect.

[Connect to a reader while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#connect-while-offline)
The SDK stores necessary `Location` information locally after connecting online.
On subsequent offline connections, it uses the stored configuration information
from that `Location`.

To connect to a reader while offline, you must have previously connected to any
mobile reader of the same type at the same `Location` while online within the
last 30 days, and have updated your reader’s software within that time. If you
attempt to connect to a reader while offline without meeting these requirements,
the request fails with an error.

ErrorResolutionThe SDK isn’t connected to the internetMake sure the `Location`
you’re using is
[configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#enable-offline-mode)
for offline mode. Otherwise, if your `Location` is properly configured, your POS
hasn’t previously connected to any readers while online. You should first
connect to any reader while online, and then connect to a reader of the same
type while offline.The selected reader requires a software update before it can
be used to collect payments offline.The reader’s software hasn’t been updated in
30 days or more. Connect to the reader while online to update it.The selected
reader must be paired online at this location before it can be used to collect
payments offline.You’re attempting to connect to a reader type that your POS
hasn’t previously connected to while online. You must first connect to this
reader or any reader of the same type while online. Or, if you want to connect
while offline, you can connect to a reader type that your POS previously
connected to while online.
If you reinstall the application or perform any operation that clears the disk
storage for the SDK, you lose any payments that the SDK has stored and not yet
forwarded. Make sure there are no stored payments before you perform any
destructive action.

[Handle offline
eventsClient-side](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#handle-offline-events)
Implement the `OfflineDelegate` protocol and pass it to Terminal to notify your
application of offline-related events. You must set `OfflineDelegate` before
collecting payments offline.

You can also query `Terminal.offlineStatus.sdk.networkStatus` to check the
current network status of the SDK.

The SDK attempts to forward payments even if the network status is offline. This
means your connection token provider might receive a request to provide a
connection token, even if the SDK’s network status is offline. During payment
collection, the network status determines if the SDK processes the payment
online or immediately stores the payment.

```
import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {

func terminal(_ terminal: Terminal, didChangeOfflineStatus offlineStatus:
OfflineStatus) {
// Check the value of `offlineStatus` and update your UI accordingly. For
instance,
// you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
 //
 // You can also check the SDK's current offline status using
 // `Terminal.shared.offlineStatus.sdk.networkStatus`.
 }

func terminal(_ terminal: Terminal, didForwardPaymentIntent intent:
PaymentIntent, error: Error?) {
 // The PaymentIntent was successfully forwarded, or an error occurred.
// Reconcile any local state using the backend-generated
`PaymentIntent.stripeId`
 // and the metadata you supplied when creating the PaymentIntent.
 //
// Note that the `PaymentIntent.stripeId` may still be nil if creating the
 // PaymentIntent in the backend failed.
 }

 func terminal(_ terminal: Terminal, didReportForwardingError error: Error) {
 // A non-specific error occurred while forwarding a PaymentIntent.
 // Check the error message and your integration implementation to
 // troubleshoot.
 }
}
```

```
import UIKit
import StripeTerminal

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

func application(_ application: UIApplication, didFinishLaunchingWithOptions
launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
 Terminal.setTokenProvider(APIClient.shared)
 Terminal.shared.offlineDelegate = CustomOfflineDelegate()
 // ...
 return true
 }

 // ...

}
```

[Create a PaymentIntent while
offlineClient-side](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#create-payment-intent)
To support operating offline, you must use the SDK’s `createPaymentIntent` to
create PaymentIntent objects.

While operating offline, `PaymentIntent` objects have a null `stripeId`. We
recommend adding a custom identifier to the PaymentIntent’s
[metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata)
to help reconcile `PaymentIntent` objects created offline.

Within your `OfflineDelegate.didForwardPaymentIntent` callback, you can use your
identifier to correlate offline payments with payments that are successfully
forwarded to Stripe.

```
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

 // Action for a "Checkout" button
 func checkoutAction() throws {
 // Populate the correct transaction amount from your application.
 let amount = UInt(10_00)

 // Build up parameters for creating a `PaymentIntent`
 let params = try PaymentIntentParametersBuilder(
 amount: amount,
 currency: "usd"
 )
 .setMetadata(["offlineId": UUID().uuidString])
 .build()

// Your app might want to prevent offline payments for too large an amount.
 // Here, we block the payment if the amount is over 1000 usd.
// Otherwise, we allow collecting offline if the network connection is
unavailable.
 let offlineBehavior: SCPOfflineBehavior = {
 if amount > UInt(1_000_00) {
 return .requireOnline
 } else {
 return .preferOnline
 }
 }()

let createConfiguration = try
CreateConfigurationBuilder().setOfflineBehavior(offlineBehavior).build()
Terminal.shared.createPaymentIntent(params, createConfig: createConfiguration) {
createResult, createError in
 if let error = createError {
// Handle offline-specific errors in your application (for example,
// `offlineBehavior` was set to `.requireOnline` and the SDK is offline).
 print("createPaymentIntent failed: \(error)")
 } else if let paymentIntent = createResult {
 print("createPaymentIntent succeeded")
// If the `PaymentIntent` was created offline, its `stripeId` field will be nil.
 if let onlineCreatedId = paymentIntent.stripeId {
 print("created online");
 } else {
 print("created offline")
 }
 }
 }
 }
}
```

#### Managing risk while offline

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By
default, if you’re operating offline, the Terminal SDK stores all offline
payments, then forwards them to Stripe’s backend when connectivity is restored.
You can pass a `CreateConfiguration` object with `offlineBehavior` set to
`REQUIRE_ONLINE` to fail the current transaction if you’re operating offline.
You might want to disallow transactions above a certain amount or disallow all
offline transactions if the SDK has stored a set of transactions whose sum
exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

- `Terminal.offlineStatus.sdk.offlinePaymentsCount`
- `Terminal.offlineStatus.sdk.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

By default, the Terminal SDK automatically determines whether to collect
payments online or offline based on your network connectivity. However, you
might want to operate offline despite having an active network connection – for
example, if you need to collect transactions quickly and your network connection
is slow. You can pass a `CreateConfiguration` object with `offlineBehavior` set
to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.
Payments collected offline while the Terminal SDK has an active network
connection are forwarded in the background.

[Collect a payment
methodClient-side](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#collect-payment-method)
Swiping cards isn’t supported while offline. Tapping cards is also not supported
in markets where [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) is
required.

Use the `didRequestReaderInput` method to display the valid card presentment
options to the customer.

Using the `initWithUpdatePaymentIntent` parameter in `CollectConfiguration` is
disabled when offline mode is enabled unless the `offlineBehavior` is set to
`REQUIRE_ONLINE`.

#### Note

Payment liability is your responsibility when operating your reader offline.
Because magnetic stripe data is easy to spoof, Stripe disallows this option
while operating offline.

```
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

 // Action for a "Checkout" button
 func checkoutAction() {
Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult,
collectError in
 if let error = collectError {
// Handle offline-specific errors in your application (for example,
 // unsupported payment method).
 print("collectPaymentMethod failed: \(error)")
 }
 else if let paymentIntent = collectResult {
 print("collectPaymentMethod succeeded")
 // ... Confirm the payment
 }
 }
 }
}
```

[Confirm
paymentClient-side](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#confirm-payment)
This step is similar to [confirming payments while
online](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment).
The primary difference is that your integration must handle offline-specific
error cases, such as when the transaction exceeds the Stripe-enforced offline
maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it
while offline. When this happens, the `PaymentIntent` might have a non-null
`stripeId`. You can check if `offlineDetails` is defined to determine if it was
confirmed offline.

```
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

 // Action for a "Checkout" button
 func checkoutAction() {

Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult,
confirmError in
 if let error = confirmError {
// Handle offline-specific errors in your application (for example,
 // unsupported payment method).
 print("confirmPaymentIntent failed: \(error)")
 } else if let confirmedPaymentIntent= confirmResult {
 print("confirmPaymentIntent succeeded")
 if let offlineDetails = paymentIntent.offlineDetails {
 print("confirmed offline");
 } else {
 print("confirmed online")
 }
 }
 }
 }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while
offline. For example, you might need to generate a receipt for customers who
require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its
[OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineCardPresentDetails.html)
from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a
[ReceiptDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html)
property you can use to generate a receipt, as well as other card details like
the cardholder name and card brand.

Not all receipt details are available while operating offline. [Prebuilt email
receipts](https://docs.stripe.com/terminal/features/receipts#prebuilt) are only
sent after connectivity is restored and the payment is successfully captured.

[Wait for payments to
forwardClient-side](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#wait-for-forward)
When Internet access is restored, the SDK automatically begins forwarding the
stored offline payments.

If you power off your POS device too soon, your payments might not be forwarded.
You can query `Terminal.offlineStatus.sdk.networkStatus` to make sure your POS
is online and can forward payments, and
`Terminal.offlineStatus.sdk.offlinePaymentsCount` to check how many payments the
Terminal SDK has to be forwarded.

[Capture
payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#capture-payment)
#### Note

While offline, you can create PaymentIntents with `captureMethod` set to
`automatic`. Once you confirm these PaymentIntents, they have a `Succeeded`
status instead of `RequiresCapture`. Stripe automatically captures the payments
after you forward them.

Payments that are successfully forwarded and authorized require capture from
your backend or application:

- To capture payments from your backend, use
[webhooks](https://docs.stripe.com/webhooks) to listen for PaymentIntents with a
`requires_capture` status.
- To capture payments from your application, wait for your application to
receive calls to `OfflineDelegate.didForwardPayment` for each PaymentIntent as
the SDK forwards it. A PaymentIntent is ready to capture if its status is
`RequiresCapture`.

If your application determines when to capture a PaymentIntent after
`confirmPaymentIntent`, they’re ready to capture when the status is
`RequiresCapture` , and the `offlineDetails` is null or has a `requiresUpload`
value of `NO` .

Capture a payment after `confirmPaymentIntent`, if it’s confirmed online:

```
Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult,
confirmError in
 if let error = confirmError {
 // Handle offline-specific errors in your application (for example,
 // unsupported payment method).
 print("confirmPaymentIntent failed: \(error)")
 } else if let confirmedPaymentIntent = confirmResult {
 if intent.status == .requiresCapture {
 if let offlineDetails = confirmedPaymentIntent.offlineDetails(),
 offlineDetails.requiresUpload {
// Offline payment, wait for `didForwardPaymentIntent` (see snippet below)
 } else {
 // Online payment, can be captured now
 }
 }
 // else, handle other intent.status results here
 }
}
```

Capture an offline payment after the SDK forwards it in your OfflineDelegate’s
`didForwardPaymentIntent`:

```
import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {
 // ...
func terminal(_ terminal: Terminal, didForwardPaymentIntent intent:
PaymentIntent, error: Error?) {
 if let error = error {
 // Handle the error appropriate for your application
 return
 }

 if intent.status == .requiresCapture {
 // The intent is ready to be captured.
 } else {
 // Handle the intent.status as appropriate.
 }
 }
 // ...
}
```

[Examine payments collected
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#examine-offline)
After authorization, you can use the
[PaymentIntents](https://docs.stripe.com/payments/payment-intents) API to
examine offline details on a payment. Access the [payment method
details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-offline)
on the [latest
Charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
object on a `PaymentIntent` to determine if it was collected offline.

## Links

- [Fail all offline
payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#managing-risk-while-offline)
- [Configuration](https://docs.stripe.com/api/terminal/configuration)
- [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)
- [Stripe Reader M2](https://docs.stripe.com/terminal/readers/stripe-m2)
- [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)
- [assign
it](https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api#create-a-configuration-for-an-individual-location)
-
[default](https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api#retrieve-the-account-default-configuration)
-
[configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments#enable-offline-mode)
- [OfflineDelegate
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPOfflineDelegate.html)
- [NetworkStatus
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPNetworkStatus.html)
- [createPaymentIntent
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)createPaymentIntent:completion:)
- [CreateConfiguration
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCreateConfiguration.html)
- [OfflineDetails
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineDetails.html)
-
[metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata)
- [didRequestReaderInput
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDisplayDelegate.html#/c:objc(pl)SCPReaderDisplayDelegate(im)terminal:didRequestReaderInput:)
- [CollectConfiguration
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectConfiguration.html)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [confirming payments while
online](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment)
-
[OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineCardPresentDetails.html)
-
[ReceiptDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html)
- [Prebuilt email
receipts](https://docs.stripe.com/terminal/features/receipts#prebuilt)
- [webhooks](https://docs.stripe.com/webhooks)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [payment method
details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-offline)
- [latest
Charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)