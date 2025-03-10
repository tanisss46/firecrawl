# Build and test your app

## Learn how to build and test your app using a DevKit.

Use your SmartPOS DevKit device to test and iterate your application without
going through the deployment, app review, or signing process.

If you need a DevKit device, you can [order up to five per
user](https://docs.stripe.com/terminal/fleet/order-and-return-readers) from the
[Readers](https://dashboard.stripe.com/terminal) section in your Dashboard.

## Set up the DevKit

Before you can use your DevKit for app development, you must do the following:

- Follow the on-screen prompts to connect to a network.
-
[Register](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=internet#register-reader)
the device to your Stripe account.
- Install all available updates.

After the initial setup, you can register your DevKit to another account or
location at any time. To do so, connect the DevKit to the internet and follow
the steps to [register a
reader](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=internet#register-reader).

While similar to production devices, DevKit devices:

- Can only operate in [test mode](https://docs.stripe.com/keys#test-live-modes).
- Ship with [developer
options](https://developer.android.com/studio/debug/dev-options) and [Android
Debug Bridge](https://developer.android.com/studio/command-line/adb) (`adb`)
enabled by default.
- Display an on-screen watermark to indicate that the device is only used for
testing. The watermark moves around the screen while the device is in use so
that you can see all parts of the screen.

The Terminal API supports targeting registered DevKit devices.

## Develop your app for Stripe devices

Use the following steps to develop your app for Stripe Android devices,
including setting up the app and handing it off to the Stripe Reader app.

[Set up the
appClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#setup-app)AndroidReact
Native
First, [set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=android)
for in-person payments. Then, follow the guidance below for Apps on Devices
integrations.

### Add dependencies

Add the following dependencies to your project’s Gradle build script. Apps on
Devices integrations require [Terminal Android
SDK](https://github.com/stripe/stripe-terminal-android) version `2.22.0` or
later. We recommend that you integrate with the [latest
version](https://github.com/stripe/stripe-terminal-android/releases).

```
dependencies {
 implementation("com.stripe:stripeterminal-core:4.2.0")
 implementation("com.stripe:stripeterminal-handoffclient:4.2.0")
}
```

Make sure that you aren’t using any other Stripe Terminal SDK dependencies. For
example, if you previously integrated the Terminal Android SDK, don’t use the
top-level `com.stripe:stripeterminal` dependency (for example,
`com.stripe:stripeterminal:4.2.0`).

See an example of [including dependencies in your app’s build
script](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/build.gradle.kts#L66).

### Configure your application

To inform the Stripe SDK of lifecycle events, add a
[TerminalApplicationDelegate.onCreate()](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal-application-delegate/on-create.html)
call to the
[onCreate()](https://developer.android.com/reference/android/app/Application#onCreate())
method for your application subclass.

```
class MyApplication : Application() {
 override fun onCreate() {
 super.onCreate()

 TerminalApplicationDelegate.onCreate(this)
 }
}
```

In your [app
manifest](https://developer.android.com/guide/topics/manifest/manifest-intro),
specify the name of your `Application` subclass with the `android:name`
attribute.

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
 <application android:name=".MyApp">
 <!-- App manifest contents -->
 </application>
</manifest>
```

Learn more about [setting up your
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=android)
or see the Apps on Devices sample app GitHub repository for an example of
[configuring the Application
subclass](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/MyApp.kt#L10).

[Build the
appClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#build-app)
Follow the guidance below for Apps on Devices integrations.

### Discover and connect a reader

AndroidReact Native
You must register a new Stripe device to your account as a new [Reader
object](https://docs.stripe.com/api/terminal/readers/object). Use the pairing
code provided in the device’s admin settings to [create the Reader
object](https://docs.stripe.com/api/terminal/readers/create). Your app uses the
Stripe Terminal Android SDK to discover and connect to your device:

- Your app runs on your registered device.
- Your app discovers the reader by calling
[discoverReaders](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
with
[HandoffDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-handoff-discovery-configuration/index.html).
- Your app connects to the reader by using
[connectReader](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html).

The following example shows how to discover and connect to a Stripe reader using
handoff mode in an Android app:

```
private fun discoverReaders() {
 Terminal.getInstance().discoverReaders(
 config = HandoffDiscoveryConfiguration(),
 discoveryListener = object : DiscoveryListener {
 override fun onUpdateDiscoveredReaders(readers: List<Reader>) {
 // In handoff discovery, the list will
 // contain a single reader. Connect to
 // the reader after it is discovered.
 readers.firstOrNull()?.let { reader ->
 connectReader(reader)
 }
 }
 },
 callback = object : Callback {
 override fun onSuccess() {
 // Handle successfully discovering readers
 }

 override fun onFailure(e: TerminalException) {
 // Handle exception while discovering readers
 }
 }
 )
}

private fun connectReader(reader: Reader) {
 Terminal.getInstance().connectReader(
 reader,
 HandoffConnectionConfiguration(
 object : HandoffReaderListener {
 override fun onDisconnect(reason: DisconnectReason) {
// Optionally get notified about reader disconnects (for example, reader was
rebooted)
 }

 override fun onReportReaderEvent(event: ReaderEvent) {
// Optionally get notified about reader events (for example, a card was
inserted)
 }
 }
 ),
 object : ReaderCallback {
 override fun onSuccess(reader: Reader) {
 // Handle successfully connecting to the reader
 }

 override fun onFailure(e: TerminalException) {
 // Handle exception when connecting to the reader
 }
 }
 )
}
```

### Collect payments

After you connect to the reader using handoff mode, you can start [collecting
payments](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=android#create-payment).

The Stripe Reader app handles payment collection and other payment operations,
such as [saving a
card](https://docs.stripe.com/terminal/features/saving-cards/overview). When
initiating a payment operation, the Stripe Reader app becomes the primary and
launches in full screen. Then, the Stripe Reader app guides the customer through
the flow and returns control to your app after completion (success or failure)
or customer cancellation. When control returns to your app, the Stripe Reader
app continues to run in the background.

See an example of [collecting payment in an Apps on Devices
app](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/model/CheckoutViewModel.kt#L82).

#### Collect payments while offline Preview

Apps on Devices supports [offline payment
collection](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-sdk-platform=android&reader-type=internet).

[Device
managementClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#device-management)
You can access the device’s admin settings by launching the `stripe://settings/`
deep-link URI from your app.

See an example of [launching the admin settings deep-link
URI](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/fragment/HomeFragment.kt#L30).

```
startActivity(
 Intent(Intent.ACTION_VIEW)
 .setData(Uri.parse("stripe://settings/"))
)
```

[Instrument the
appClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#instrument-app)
Stripe doesn’t provide an application-level instrumentation solution. To keep
track of crashes and other logs from your application, you can use a third-party
library such as Sentry or Crashlytics.

[Set the device
localeClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#device-locale)
The device user’s language selection (not country) informs the value returned by
[Locale.getDefault()](https://developer.android.com/reference/java/util/Locale#getDefault()).
You can change the device language in the admin settings.

[Screen
orientationClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#screen-orientation)
Stripe Android devices have the *Auto-rotate screen* setting enabled by default.
Your app can override this setting by locking the UI to a specific screen
orientation.

This can be achieved by setting the
[screenOrientation](https://developer.android.com/guide/topics/manifest/activity-element#screen)
attribute on the relevant `<activity>` tags in the manifest.

```
<activity
 android:name=".MainActivity"
 android:screenOrientation="portrait">
</activity>
```

Alternatively, this can be set programatically using
[Activity::setRequestedOrientation](https://developer.android.com/reference/android/app/Activity#setRequestedOrientation(int))
in your `Activity` class.

```
class MainActivity : Activity() {
 override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)

 // Lock to portrait orientation
 requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_PORTRAIT

 // Or, lock to landscape orientation
 // requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE
 }
}
```

[LimitationsClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#limitations)
Stripe Android devices don’t render a system UI, including a back button or
status bar.

If your app needs to communicate battery level, charging state, and connectivity
status to the user, refer to the following Android API docs for guidance:

- [Monitor the Battery Level and Charging
State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)
- [Monitor connectivity status and connection
metering](https://developer.android.com/training/monitoring-device-state/connectivity-status-type)
[Working with device
accessoriesClient-side](https://docs.stripe.com/terminal/features/apps-on-devices/build#device-accessories)
When the Stripe reader connects or disconnects from a dock, the Android
operation system triggers a [configuration
change](https://developer.android.com/guide/topics/resources/runtime-changes).

By default, your app’s activity is automatically recreated on a configuration
change.

To disable automatic activity recreation when connecting to or disconnecting
from a dock, add `android:configChanges="uiMode"` in the `<activity>` entry in
your `AndroidManifest.xml` file.

```
<activity
 android:name=".MyActivity"
 android:configChanges="uiMode" />
```

Your activity can be notified of configuration changes by implementing
[Activity::onConfigurationChanged](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)).
This method is only called if you’ve specified configurations you want to handle
with the `android:configChanges` attribute in your manifest.

```
class MainActivity : Activity() {
 override fun onConfigurationChanged(newConfig: Configuration) {
 super.onConfigurationChanged(newConfig)
 // implement custom configuration change handling logic
 }
}
```

## Test your app

Use your S700 DevKit device to test your app in the Stripe Dashboard or using
the Android Debug Bridge (`adb`).

Android Debug Bridge (adb)Dashboard
You can connect your DevKit device to your computer using a USB-A to USB-C
cable. Then, use `adb` to directly install your app’s assembled APK onto the
DevKit device.

The following examples assume your application’s [package
name](https://developer.android.com/studio/build/configure-app-module) is
`com.example.myapp` and the [main
activity](https://developer.android.com/reference/android/content/Intent.html#ACTION_MAIN)
is `MainActivity`.

```
$ adb install myapp.apk

```

After installation completes, launch your app:

```
$ adb shell am start com.example.myapp/.MainActivity

```

Start admin settings:

```
$ adb shell am start -d "stripe://settings/"

```

If needed, uninstall your app:

```
$ adb uninstall com.example.myapp

```

Google’s [Android Debug Bridge
documentation](https://developer.android.com/studio/command-line/adb) provides a
comprehensive guide to using `adb`.

## Test payments

DevKit devices can process test payments using a Stripe physical test card,
which you can order in the
[Dashboard](https://dashboard.stripe.com/terminal/shop/thsku_FmpZaTqwezTFvS).
When [testing
payments](https://docs.stripe.com/terminal/references/testing#physical-test-cards),
you can use decimal amounts to produce specific outcomes.

#### Warning

Don’t use real cards for test payments on DevKit devices.

## Next steps

- [Prepare for app
review](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
- [Submit your
app](https://docs.stripe.com/terminal/features/apps-on-devices/submit)

## Links

- [GitHub](https://github.com/stripe-samples/terminal-apps-on-devices)
- [order up to five per
user](https://docs.stripe.com/terminal/fleet/order-and-return-readers)
- [Readers](https://dashboard.stripe.com/terminal)
-
[Register](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=internet#register-reader)
- [test mode](https://docs.stripe.com/keys#test-live-modes)
- [developer options](https://developer.android.com/studio/debug/dev-options)
- [Android Debug Bridge](https://developer.android.com/studio/command-line/adb)
- [set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=android)
- [Terminal Android SDK](https://github.com/stripe/stripe-terminal-android)
- [latest version](https://github.com/stripe/stripe-terminal-android/releases)
- [including dependencies in your app’s build
script](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/build.gradle.kts#L66)
-
[TerminalApplicationDelegate.onCreate()](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal-application-delegate/on-create.html)
-
[onCreate()](https://developer.android.com/reference/android/app/Application#onCreate())
- [app
manifest](https://developer.android.com/guide/topics/manifest/manifest-intro)
-
[http://schemas.android.com/apk/res/android](http://schemas.android.com/apk/res/android)
- [configuring the Application
subclass](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/MyApp.kt#L10)
- [Reader object](https://docs.stripe.com/api/terminal/readers/object)
- [create the Reader
object](https://docs.stripe.com/api/terminal/readers/create)
-
[discover](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/model/MainViewModel.kt#L90)
-
[connect](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/model/MainViewModel.kt#L106)
-
[discoverReaders](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
-
[HandoffDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-handoff-discovery-configuration/index.html)
-
[connectReader](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html)
- [collecting
payments](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=android#create-payment)
- [saving a
card](https://docs.stripe.com/terminal/features/saving-cards/overview)
- [collecting payment in an Apps on Devices
app](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/model/CheckoutViewModel.kt#L82)
- [offline payment
collection](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-sdk-platform=android&reader-type=internet)
- [launching the admin settings deep-link
URI](https://github.com/stripe-samples/terminal-apps-on-devices/blob/718c2de38c7b8003fcf58c536c266bb990ad43a7/app/src/main/java/com/stripe/aod/sampleapp/fragment/HomeFragment.kt#L30)
-
[Locale.getDefault()](https://developer.android.com/reference/java/util/Locale#getDefault())
-
[screenOrientation](https://developer.android.com/guide/topics/manifest/activity-element#screen)
-
[Activity::setRequestedOrientation](https://developer.android.com/reference/android/app/Activity#setRequestedOrientation(int))
- [Monitor the Battery Level and Charging
State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)
- [Monitor connectivity status and connection
metering](https://developer.android.com/training/monitoring-device-state/connectivity-status-type)
- [configuration
change](https://developer.android.com/guide/topics/resources/runtime-changes)
-
[Activity::onConfigurationChanged](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration))
- [package
name](https://developer.android.com/studio/build/configure-app-module)
- [main
activity](https://developer.android.com/reference/android/content/Intent.html#ACTION_MAIN)
- [Dashboard](https://dashboard.stripe.com/terminal/shop/thsku_FmpZaTqwezTFvS)
- [testing
payments](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
- [Prepare for app
review](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
- [Submit your
app](https://docs.stripe.com/terminal/features/apps-on-devices/submit)