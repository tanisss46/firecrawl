# Manage your app's versions and releases

## Learn about app versioning and releases to ship new versions of your app and manage changes over time.

In Stripe Apps, a *version* is a framework to help you manage changes to your
app over time. A *release* is a version of your app that you decide to
publish—either to your own account or on the [Stripe App
Marketplace](https://marketplace.stripe.com/) after passing app review.

## Versions overview

The `version` property in the [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest) lets you
specify the version of your app. Stripe doesn’t enforce a specific versioning
schema for apps, but we recommend following an established pattern, like
[semantic versioning](https://semver.org/).

Stripe users who install your app don’t have to think about the version number.
Stripe automatically upgrades them to the latest release of an app. The app
functions in a similar manner to apps updating automatically on your phone. The
only exception is cases where the permissions scope changes. If you change the
permissions, users of your app are prompted to re-authorize your app and its new
permissions.

## How to upload a new app version

- Change the `version` property in the [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest).
- Upload the new app version to Stripe. Follow the same [upload
process](https://docs.stripe.com/stripe-apps/upload-install-app) that you used
when creating an app.

## Changing between app versions in test mode

You can change between different app versions in test mode before creating a
release.

- In the Stripe Dashboard, go to [Apps](https://dashboard.stripe.com/apps).
- Select the app you want to create a new version for, and view **App Details**.
- In the version history table, click the overflow menu () of the new version.
- Select **Install in test mode** and complete the installation.

## Releases overview

To distribute your app in live mode for users, create a new release. You can
publish it to your own account or to the [App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app). To be listed in
the App Marketplace, releases must go through [App
Review](https://docs.stripe.com/stripe-apps/review-requirements).

## How to create a new release

- In the Stripe Dashboard, go to [Apps](https://dashboard.stripe.com/apps).
- Select the app you want to create a new version for, and view **App Details**.
- Click **Create new release**.
- Follow the steps to create a new release.

When your release passes app review, all users are automatically upgraded to the
latest released version.

## How to remove an app listing or change a release

App releases can only be fixed forward. To remove an app listing or change an
app release that had accidental changes, bump the app version and make a new
release of the app.

Since we don’t enforce a versioning structure, an incremental release is any
release created after the current live version. For example, if version 2.0.0
was uploaded before version 1.0.0, version 2.0.0 won’t be available to create a
release.

To remove an app or an app release from Stripe, [contact Stripe
Support](https://support.stripe.com/).

## See also

- [Upload your app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [Publish your app](https://docs.stripe.com/stripe-apps/publish-app)
- [App review
requirements](https://docs.stripe.com/stripe-apps/review-requirements)

## Links

- [Stripe App Marketplace](https://marketplace.stripe.com)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [semantic versioning](https://semver.org/)
- [upload process](https://docs.stripe.com/stripe-apps/upload-install-app)
- [Apps](https://dashboard.stripe.com/apps)
- [App Marketplace](https://docs.stripe.com/stripe-apps/publish-app)
- [App Review](https://docs.stripe.com/stripe-apps/review-requirements)
- [contact Stripe Support](https://support.stripe.com/)