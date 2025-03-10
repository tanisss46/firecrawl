# Troubleshoot apps on devices

## Learn how to resolve known issues with apps on devices.

- **Why won’t my app upload to Stripe?**

If your APK is too big or your upload internet speeds are too slow, you might
receive a timeout error when you upload your APK with the
[Files](https://docs.stripe.com/api/files) API. Stripe enforces a 45 second
timeout on its servers, and produces an error if an app isn’t uploaded within
that time. To resolve this issue, upload your APK to a server with better
internet (for example, an AWS EC2 instance or another VPS), and then upload to
Stripe from there. The network connection between your server and Stripe servers
is generally much faster than home or office connections to Stripe through an
ISP.
- **Do I have to resubmit my test-mode-approved app for approval in live mode?**

If you obtained approval for your app in test mode and want to use the app in
live mode, you must submit it again for approval. The [app review
process](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
is the same for both test mode and live mode. Make sure to upload the exact same
APK for automatic approval.
- **Why can’t I access the device admin settings screen from my app?**

By default, the device user can access admin settings by swiping from the left
edge of the screen and tapping **Settings**. This method doesn’t work when a
third-party app is the default launch app. You can use the `stripe://settings/`
URI to deep-link into admin settings and then launch the URI from your app using
the following code in your **Activity** or **Fragment**:

```
startActivity(
 Intent(Intent.ACTION_VIEW)
 .setData(Uri.parse("stripe://settings/"))
)
```
- **Why can’t I update the device language on my DevKit?**

The reader app on the DevKit can’t currently update the device language. You can
change the device language through the Android Settings app. Use `adb` to launch
the Android Settings app:

```
$ adb shell am start -a android.settings.SETTINGS

```
- **Why can’t I launch or deep-link into Android Settings on Stripe devices?**

For security and reliability reasons, Stripe blocks the Android Settings app on
production Stripe devices.
- **Can I run multiple apps on my Stripe Reader S700?**

The Stripe Reader S700 supports running multiple apps, but we don’t provide an
app launcher. You must build the functionality within your apps to allow
switching between apps. When you deploy your apps, you can specify the
`default_kiosk_application`, which is the app that launches when the device
checks for updates and after payments. You can’t use the Dashboard to configure
multiple apps on a device.
- **Can I deploy a web app on my Stripe devices?**

You can package your web app to run on your Stripe devices. Use a framework,
such as [Cordova](https://cordova.apache.org/), to modify your web app for
compatibility with Android and generate an Android application package (APK).
You can then [upload the
APK](https://docs.stripe.com/terminal/features/apps-on-devices/submit) in your
Stripe Dashboard.

Frameworks aren’t aware of Stripe or the [Android Terminal
SDK](https://docs.stripe.com/terminal/references/api), so you must create a
JavaScript bridge between your web app and the SDK to send commands from
JavaScript.

Alternatively, you can use the [server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration) to
collect payments, which doesn’t require using the Terminal handoff client
library or a JavaScript bridge. This allows Stripe to handle all payment
collection commands and communication with the device.
- **Why is my app constantly restarting?**

The Stripe Terminal card readers restart the default app in the event of a
crash. This manifests differently for production and DevKit devices:

- Production – If you configure your app as the default app on production
devices, the app automatically restarts when there’s a crash. If the app crashes
during initialization (for example, a missing or broken database migration), the
device can enter a crash loop.
- DevKit – If you configure the Stripe payment app as the default app on DevKit
devices, your app queues on the device and then becomes the primary app. If the
app crashes, the Stripe payment app restarts instead.
- **Why does my app crash when processing payments with a large amount of line
items?**

If your app crashes while attempting to process a payment with a large amount of
line items, the issue might be memory. The Android OS limits data sent per
inter-process (IPC) to 500 KB, when saving state for your activity. To help
prevent your app from crashing, you can store your data out of memory, such as
in a database.
- **What if I find a bug in a deployed app?**

If you discover a bug in an app that’s already deployed, you can fix the issue
in the app, upload a new version, and then [deploy your
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API).
- **How do I view the logs for my app on production readers?**

Stripe doesn’t expose logs on production readers. We rely on Sentry integrations
for observability.
- **I sideloaded my point-of-sale app onto a DevKit and successfully completed a
payment transaction. Why won’t my point-of-sale app start after the transaction
completes?**

On Stripe readers configured for Apps on Devices, the [preferred kiosk
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)
starts after a transaction completes. On a DevKit, the device’s preferred kiosk
app is only set when you include the device in a deploy group.

To set the preferred kiosk app on a DevKit device:

- Submit your app to a DevKit-only deploy group. This allows you to [skip app
review](https://docs.stripe.com/terminal/features/apps-on-devices/app-review#skip-app-review).
- [Deploy the app
version](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)
to a deploy group that targets your DevKit.

## Links

- [Files](https://docs.stripe.com/api/files)
- [app review
process](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
- [Cordova](https://cordova.apache.org/)
- [upload the
APK](https://docs.stripe.com/terminal/features/apps-on-devices/submit)
- [Android Terminal SDK](https://docs.stripe.com/terminal/references/api)
- [server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration)
- [deploy your
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)
- [skip app
review](https://docs.stripe.com/terminal/features/apps-on-devices/app-review#skip-app-review)