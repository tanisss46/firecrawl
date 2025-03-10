# Prepare for app review

## Learn how to prepare your app for Stripe's review process.

Stripe reviews all apps built for Terminal devices before approving them for
deployment. The review process helps prevent putting payment information at risk
or violating industry-standard best practices for payment devices.

## App review at a glance

Stripe reviews the [device asset
version](https://docs.stripe.com/terminal/features/apps-on-devices/submit#create-device-asset-version)
of your app. This process doesn’t require any action from you.

- A reviewer downloads your app and installs it on a Terminal smart reader.
- Using the instructions you provided, the reviewer interacts with your app and
identifies potential problems, focusing on your app’s payment collection user
interface.
- After the reviewer determines there are no present issues, they approve your
app for deployment. Stripe [notifies you of app
approval](https://docs.stripe.com/terminal/features/apps-on-devices/submit#monitor-status).
The reviewer might reject your app if they’re unable to follow instructions, or
if the app contains features that might put payment information at risk.

The exact amount of time and effort required to review each app varies because
no two apps are alike.

## App review guidelines

Use the guidelines below to help with a timely and successful app review.

### Build multi-tenant apps

If you’re a platform building apps for Terminal devices on behalf of individual
businesses, we encourage you to build a multi-tenant app that serves all of your
users. You can build business-specific workflows, such as different image or
graphics assets per business, into your app’s configuration and settings. This
approach also removes the need for you to submit individual apps per business.

### Prevent collecting keyed payment card numbers or PINs

Use the Terminal reader running the app to request payment from a customer and
collect sensitive card and PIN information. The [Terminal
SDK](https://docs.stripe.com/terminal/features/apps-on-devices/build#discover-and-connect-a-reader)
allows you to display an appropriate prompt on the device screen.

Make sure that your app doesn’t display user interface elements (for example, an
input field) that allow the manual entry of PINs, authentication values, or
payment information.

### Support test mode payments

During development and testing, use a DevKit device to [accept test mode
payments](https://docs.stripe.com/terminal/features/apps-on-devices/build). This
allows Stripe to use a [physical Terminal test
card](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
when we review your app.

If you must accept live payments, make sure the app accepts a minimal charge
amount, such as 1 USD (or equivalent in another currency).

### Address technical defects

[Use your
DevKit](https://docs.stripe.com/terminal/features/apps-on-devices/build) to
identify defects before submitting your app for review.

Examples of common defects include:

- The app fails to install because of an error during its build process.
- The app crashes before we can interact with the app’s payment UI.
- The app can’t detect or connect to the reader.

Make sure to address the technical defects that can prevent us from successfully
interacting with or using your app. We reject apps that can’t be fully reviewed
due to technical defects.

### Write clear and complete instructions

When you submit your app for review, assume that Stripe hasn’t seen it before.
Make sure your instructions are self-contained and don’t assume any special
knowledge to complete the review. We must be able to follow your instructions
exactly as submitted.

Include the following with your app’s instructions:

- Login information, such as a username or password (if applicable)
- Fixed authentication code that remains valid indefinitely (if applicable)
- How to reach your payment collection UI
- How to exercise the app fully to highlight any problems

Don’t provide credentials that permit access to sensitive information or to
functionality that can cause any side effects. For example, an app that accepts
orders for food must not cause any actual food preparation to occur as a result
of orders placed during app review.

## Submit your app for review

Follow the steps to [submit your app for
review](https://docs.stripe.com/terminal/features/apps-on-devices/submit).

## Skip app review

You can skip app review and move directly to deployment in these cases:

- To use the API or test your app, you can limit the
[compatible_device_types](https://docs.stripe.com/api/terminal/device_asset_versions/object#terminal_device_asset_version_object-compatible_device_types)
to only DevKit device types (`stripe_s700_devkit`).
- If you previously uploaded a device asset version in test mode and Stripe
reviewed and approved that version’s APK, you can upload it again for live mode.

## Next steps

- [Submit your app for
review](https://docs.stripe.com/terminal/features/apps-on-devices/submit)
- [Deploy your
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)

## Links

- [device asset
version](https://docs.stripe.com/terminal/features/apps-on-devices/submit#create-device-asset-version)
- [notifies you of app
approval](https://docs.stripe.com/terminal/features/apps-on-devices/submit#monitor-status)
- [Terminal
SDK](https://docs.stripe.com/terminal/features/apps-on-devices/build#discover-and-connect-a-reader)
- [accept test mode
payments](https://docs.stripe.com/terminal/features/apps-on-devices/build)
- [physical Terminal test
card](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
- [submit your app for
review](https://docs.stripe.com/terminal/features/apps-on-devices/submit)
-
[compatible_device_types](https://docs.stripe.com/api/terminal/device_asset_versions/object#terminal_device_asset_version_object-compatible_device_types)
- [Deploy your
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)