# Terminal SDK migration guide

## Learn how to migrate to the latest version of the Stripe Terminal SDK.

The Stripe Terminal iOS and Android SDKs have been updated with a number of
breaking changes in APIs and behavior, some of which require you to update your
integration with the Stripe Terminal SDK. To improve consistency between our
SDKs and to simplify your application logic and integration, we regularly make
changes in major version updates that might affect the way your integration
works or behaves. This guide explains the latest changes to help you upgrade
your integration.

#### Note

Building a new Stripe Terminal integration? Visit our [Design an
integration](https://docs.stripe.com/terminal/designing-integration) page to
learn how to get started.

## Migrate to version 4.0.0

Here are some things you need to know about the 4.0.0 Stripe Terminal iOS and
Android SDKs:

- [Save cards after payment
globally](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment)-
Users can now save cards after payment outside of the US by updating the
customer consent collection process for saving card details on point-of-sale
devices.
- Support for [Mail order and telephone
order](https://docs.stripe.com/terminal/features/mail-telephone-orders/overview)
(MOTO) payments on smart readers Preview- This feature is in preview. To request
access, email
[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).
- Updates to minimum supported iOS platform version
- Enables [reader auto-reconnect on unexpected
disconnects](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=tap-to-pay#automatically-attempt-reconnection)
by default for mobile and Tap to Pay readers, enhancing reader resiliency
- Consolidates reader connection functionality and disconnect callbacks for all
reader types
iOSAndroid
If your application currently uses an Terminal iOS SDK version prior to 4.0.0,
there are a few changes you need to make to upgrade and accept card present
payments globally. For a detailed list of the changes from version 3.9.1 to
4.0.0, please reference the [SDK
changelog](https://github.com/stripe/stripe-terminal-ios/blob/master/CHANGELOG.md).

## Update your minimum supported version to iOS 14 or higher

We regularly update the minimum supported version of our SDKs to streamline our
developer support efforts.

Existing 3.X versions of the Terminal iOS SDK will continue to support devices
running **iOS 13** and higher.

## Update saving cards after PaymentIntents integration

If you [save a payment method after a successful in-person
PaymentIntent](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment),
you need to make the following updates to your integration:

- When creating Terminal PaymentIntents, pass the
[setup_future_usage](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Classes/SCPPaymentIntent.html#/c:objc(cs)SCPPaymentIntent(py)setupFutureUsage)
parameter, which informs Stripe that you want to make future payments with the
same card.
- You also need to pass
[allow_redisplay](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectConfiguration.html#/c:objc(cs)SCPCollectConfiguration(py)allowRedisplay)
as `always` or `limited` in `SCPCollectConfiguration`. Pass `always` if you want
the customer’s saved card to be presented to them in all future checkout flows,
and `limited` if it can only be used in the context of the initially scoped use,
such as a subscription.

Learn more about [saving cards after a
payment](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment).

## Update saving cards without payment with SetupIntents integration

To ensure a consistent integration shape between SetupIntents and
PaymentIntents, as well as in-person and online transactions, in `SCPTerminal`’s
`collectSetupIntentPaymentMethod`, we removed the `customerConsentCollected`
parameter that was previously required on all SetupIntent transactions, and
replaced it with the `allowRedisplay` parameter.

Learn more about [saving directly without
charging](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly).

## Update your discoverReaders usage

- We added a new enum value, `discovering`, to
[SCPConnectionStatus](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPConnectionStatus.html)
to represent when reader discovery is running. Make sure your integration can
handle this new state and provide relevant information to your customers.
- We improved the handling of multiple simultaneous reader discover operations.
Previously, calling
[discoverReaders](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:)
multiple times would queue the operations. Now, when a new
[discoverReaders](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:)
is called while an existing one is already in progress, the SDK cancels the
ongoing operation and returns a
[SCPErrorCanceledDueToIntegrationError](https://stripe.dev/stripe-terminal-ios/docs/Errors.html#/c:@SCPErrorNewDiscoveryRequested)
error. The new discoverReaders operation then starts immediately.
- Discovering smart and Tap to Pay readers now calls the `discoverReaders`
completion block when the operation ends. This change reflects the reality that
reader discovery for these reader types isn’t a long-running operation.
- We fixed a bug that strongly held a reference to the
[SCPDiscoveryDelegate](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPDiscoveryDelegate.html)
in the SDK. Make sure your application is holding a strong reference to your
delegate to receive the discovery events.

## Update your reader connection usage

- To ensure a consistent integration pattern across reader discovery and
connection, we consolidated all previous reader connection methods
(`connectBluetoothReader`, `connectInternetReader`, `connectLocalMobileReader`)
into
[connectReader](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:delegate:connectionConfig:completion:).
The exact connection type is still determined by the passed in connection
configuration.
- For mobile readers and Tap to Pay readers, the `ReaderDelegate` parameter has
been removed from the `connectReader` method and instead moved into the
`connectionConfig`, replacing `SCPReconnectionDelegate`. Consistent with other
reader types, smart readers `InternetConnectionConfiguration` now also expects
an `InternetReaderDelegate` to be passed in, which will alert your integration
of events, including when a reader disconnects.
Reader TypeConnection ConfigurationReader DelegateMobile
ReaderSCPBluetoothConnectionConfiguration[SCPMobileReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPMobileReaderDelegate.html)Smart
ReaderSCPInternetConnectionConfiguration[SCPInternetReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Reader.html#/c:objc(pl)SCPInternetReaderDelegate)Tap
to
PaySCPTapToPayConnectionConfiguration[SCPTapToPayReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPTapToPayReaderDelegate.html)
### Before

```
// Call `connectBluetoothReader` with the selected reader and a connection
config
// to register to a location as set by your app.
let connectionConfig: BluetoothConnectionConfiguration
do {
connectionConfig = try BluetoothConnectionConfigurationBuilder(locationId:
"{{LOCATION_ID}}").build()
} catch {
 // Handle the error building the connection configuration
 return
}
Terminal.shared.connectBluetoothReader(selectedReader, delegate: readerDelegate,
connectionConfig: connectionConfig) { reader, error in
 if let reader = reader {
 print("Successfully connected to reader: \(reader)")
 } else if let error = error {
 print("connectBluetoothReader failed: \(error)")
 }
}
```

### After

```
// Call `connectReader` with the selected reader and a connection config
// to register to a location as set by your app.
let connectionConfig: BluetoothConnectionConfiguration
do {
connectionConfig = try BluetoothConnectionConfigurationBuilder(delegate:
yourMobileReaderDelegate, locationId: "{{LOCATION_ID}}")
 .build()
} catch {
 // Handle the error building the connection configuration
 return
}
Terminal.shared.connectReader(selectedReader, connectionConfig:
connectionConfig) { reader, error in
 if let reader = reader {
 print("Successfully connected to reader: \(reader)")
 } else if let error = error {
 print("connectReader failed: \(error)")
 }
}
```

For more details, refer our documentation about [connecting to a
reader](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#connect-reader).

## Auto reconnection is now enabled by default for mobile and Tap to Pay readers

- To increase the resiliency of your Terminal integration with mobile and Tap to
Pay readers, we enabled [auto
reconnection](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#handle-disconnects)
by default when a reader unexpectedly disconnects.
- We recommend displaying notifications in your app to inform the users about
the reader status throughout the reconnection process. To handle reader
reconnection methods, we removed the `SCPReconnectionDelegate`. Its
responsibilities have been integrated into the respective ReaderDelegates. Use
`MobileReaderDelegate` for mobile readers, and `TapToPayReaderDelegate` for Tap
to Pay readers to handle reconnection events.
- If you implemented your own reader reconnection logic and want to maintain
this behavior, you can turn off auto reconnection by setting
[setAutoReconnectOnUnexpectedDisconnect](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothConnectionConfigurationBuilder.html#/c:objc(cs)SCPBluetoothConnectionConfigurationBuilder(im)setAutoReconnectOnUnexpectedDisconnect:)
to `false`.

### Before

```
import StripeTerminal

extension ReaderViewController: ReconnectionDelegate {
 // MARK: ReconnectionDelegate
func terminal(_ terminal: Terminal, didStartReaderReconnect cancelable:
Cancelable) {
 // 1. Notified at the start of a reconnection attempt
 // Use cancelable to stop reconnection at any time
 }

 func terminalDidSucceedReaderReconnect(_ terminal: Terminal) {
 // 2. Notified when reader reconnection succeeds
 // App is now connected
 }
 func terminalDidFailReaderReconnect(_ terminal: Terminal) {
 // 3. Notified when reader reconnection fails
 // App is now disconnected
 }
}
```

### After

```
import StripeTerminal

extension ReaderViewController: MobileReaderDelegate {
 // MARK: MobileReaderDelegate

func reader(_ reader: Reader, didStartReconnect cancelable: Cancelable,
disconnectReason: DisconnectReason) {
 // 1. Notified at the start of a reconnection attempt
 // Use cancelable to stop reconnection at any time
 }

 func readerDidSucceedReconnect(_ reader: Reader) {
 // 2. Notified when reader reconnection succeeds
 // App is now connected
 }
 func readerDidFailReconnect(_ reader: Reader) {
 // 3. Notified when reader reconnection fails
 // App is now disconnected
 }
}
```

For more details and code snippets, refer to our documentation about
[automatically attempting to
reconnect](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=tap-to-pay#automatically-attempt-reconnection).

## Update your reader disconnect handling

- To be informed when a reader disconnects, we consolidated the reader
disconnect callbacks for all reader types by removing
`terminal:didReportUnexpectedReaderDisconnect:` from the `SCPTerminalDelegate`.
Use `reader:didDisconnect:` as part of the ReaderDelegates to be notified when a
reader disconnects. For mobile readers, the
[SCPDisconnectReason](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPDisconnectReason.html)
can help identify the reason for the disconnection.

With auto-reconnection enabled, both
[-readerDidFailReconnect:](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)readerDidFailReconnect:)
and
[reader:didDisconnect:](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)reader:didDisconnect:)
methods are called if the SDK fails to reconnect to the reader and it becomes
disconnected.

### Before

```
import StripeTerminal

class ReaderViewController: UIViewController, TerminalDelegate {
 override func viewDidLoad() {
 super.viewDidLoad()
 Terminal.shared.delegate = self
 }

 // ...
 // MARK: TerminalDelegate
func terminal(_ terminal: Terminal, didReportUnexpectedReaderDisconnect reader:
Reader) {
// Consider displaying a UI to notify the user and start rediscovering readers
 }
}
```

### After

```
import StripeTerminal

class ReaderViewController: UIViewController, MobileReaderDelegate {
 override func viewDidLoad() {
 super.viewDidLoad()
 // Set the reader delegate when connecting to a reader
 }

 // ...

 func reader(_ reader: Reader, didDisconnect reason: DisconnectReason) {
// Consider displaying a UI to notify the user and start rediscovering readers
 }
}
```

For more details, refer to our documentation about [handling disconnects
manually](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=tap-to-pay#handle-the-disconnect-manually).

## Update your payment acceptance integration

- You can now cancel `confirmPaymentIntent` using the returned `Cancelable`
object. This is useful for QR code payments, which have an asynchronous
confirmation process. Similarly, `confirmSetupIntent` and `confirmRefund` are
now cancelable as well.
- We improved type safety and consistency between the mobile SDKs by updating
the way `paymentMethodTypes` are specified in `SCPPaymentIntentParameters` and
`SCPSetupIntentParameters`. Previously, this parameter was represented as an
array of strings (for example, [“card_present”]). It now uses enum values from
`SCPPaymentMethodType`.
- To improve the cancelation flow for PaymentIntents and SetupIntents, calling
`Terminal::cancelPaymentIntent` or `Terminal::cancelSetupIntent` now also
cancels any ongoing payment processing, you no longer need to cancel payment
operations such as `.collectPaymentMethod` separately before canceling the
PaymentIntent.
- `SCPSetupIntent.stripeId` is now nullable to be consistent with
`SCPPaymentIntent.stripeId`. Although the `stripeId` value will continue to
exist, make sure your code safely handles the case where
`SCPSetupIntent.stripeId` might be `null` to avoid compiler errors.

## Update usage for renaming and deprecation

-
[BluetoothReaderDelegate](https://stripe.dev/stripe-terminal-ios/3.9.0/Protocols/SCPBluetoothReaderDelegate.html)
has been renamed to
[MobileReaderDelegate](https://stripe.dev/stripe-terminal-ios/Protocols/SCPMobileReaderDelegate.html).
- In `SCPReaderSoftwareUpdate,` we renamed `SCPUpdateTimeEstimate` to
`SCPUpdateDurationEstimate` and `estimatedUpdateTime` to `durationEstimate` to
better represent their intent.
- In `SCPOfflineDetails`, which represents payment details available when a
payment is created or confirmed while offline, we renamed the time that the
offline payment happened from `collectedAt` to `storedAt`, aligning with the
naming conventions in the Terminal Android SDK.
- We renamed “local mobile” and “apple built in” to “Tap To Pay” in all SDK
function names and error codes.

## Links

- [Design an
integration](https://docs.stripe.com/terminal/designing-integration)
- [Save cards after payment
globally](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment)
- [Mail order and telephone
order](https://docs.stripe.com/terminal/features/mail-telephone-orders/overview)
- [reader auto-reconnect on unexpected
disconnects](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=tap-to-pay#automatically-attempt-reconnection)
- [SDK
changelog](https://github.com/stripe/stripe-terminal-ios/blob/master/CHANGELOG.md)
-
[setup_future_usage](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Classes/SCPPaymentIntent.html#/c:objc(cs)SCPPaymentIntent(py)setupFutureUsage)
-
[allow_redisplay](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectConfiguration.html#/c:objc(cs)SCPCollectConfiguration(py)allowRedisplay)
- [saving directly without
charging](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly)
-
[SCPConnectionStatus](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPConnectionStatus.html)
-
[discoverReaders](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:)
-
[SCPErrorCanceledDueToIntegrationError](https://stripe.dev/stripe-terminal-ios/docs/Errors.html#/c:@SCPErrorNewDiscoveryRequested)
-
[SCPDiscoveryDelegate](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPDiscoveryDelegate.html)
-
[connectReader](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:delegate:connectionConfig:completion:)
-
[SCPMobileReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPMobileReaderDelegate.html)
-
[SCPInternetReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Reader.html#/c:objc(pl)SCPInternetReaderDelegate)
-
[SCPTapToPayReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPTapToPayReaderDelegate.html)
- [connecting to a
reader](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#connect-reader)
- [auto
reconnection](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#handle-disconnects)
-
[setAutoReconnectOnUnexpectedDisconnect](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothConnectionConfigurationBuilder.html#/c:objc(cs)SCPBluetoothConnectionConfigurationBuilder(im)setAutoReconnectOnUnexpectedDisconnect:)
-
[SCPDisconnectReason](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPDisconnectReason.html)
-
[-readerDidFailReconnect:](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)readerDidFailReconnect:)
-
[reader:didDisconnect:](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)reader:didDisconnect:)
- [handling disconnects
manually](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=tap-to-pay#handle-the-disconnect-manually)
-
[BluetoothReaderDelegate](https://stripe.dev/stripe-terminal-ios/3.9.0/Protocols/SCPBluetoothReaderDelegate.html)
-
[MobileReaderDelegate](https://stripe.dev/stripe-terminal-ios/Protocols/SCPMobileReaderDelegate.html)