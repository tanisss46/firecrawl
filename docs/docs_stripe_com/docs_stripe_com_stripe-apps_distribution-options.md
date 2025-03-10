# Distribution options

## Learn what you need to know to share your Stripe Apps with users.

#### Caution

Publicly distributed apps have new [naming
restrictions](https://docs.stripe.com/stripe-apps/distribution-options#app-name-restrictions).

Stripe Apps gives you two ways to distribute your apps. You can make them
publicly available or share them only with your [team
members](https://docs.stripe.com/dashboard/teams).

## Publish your app on the Stripe App Marketplace

The [Stripe App Marketplace](https://marketplace.stripe.com/) is how you share
your application with the Stripe user community.

When you publish an app on the App Marketplace, make sure the app complies with
all [app review
requirements](https://docs.stripe.com/stripe-apps/review-requirements#app-review-requirements).
We also recommend reviewing our [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines) for best
practices and recommended coding patterns. Stripe reviews all apps to make sure
they comply with the published requirements before listing them in the
marketplace.

Stripe can only support language listings at this time. To support
additional languages, reach out to Stripe.

The publishing process consists of these steps:

- Select the version of the app that you want to publish.
- Create an app listing that provides prospective users with information about
your app and defines how your app appears in the App Marketplace.
- Submit the application for review.
- Publish the app to the App Marketplace.

For more information, learn how to [publish your
app](https://docs.stripe.com/stripe-apps/publish-app).

## Share your app with team members

With Stripe Apps, you have the option of sharing your app only with [team
members](https://docs.stripe.com/dashboard/teams). For example, you might
develop an app that sends sale data into your own custom accounting system. Or
you might build an app that connects paid orders with your fulfillment system.
For these and other situations, you can make the application only available to
team members of your Stripe account.

Unlike apps on the App Marketplace, apps shared with team members don’t go
through a review process. However, we recommend reviewing our [app review
requirements](https://docs.stripe.com/stripe-apps/review-requirements#app-review-requirements)
and [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines) when you
build your app.

Sharing your app with team members consists of these steps:

- Specify that you want to share your app only with members of your Stripe
account.
- Select the version of the app that you want to [upload and make
available](https://docs.stripe.com/stripe-apps/upload-install-app).

If you later decide you want to publish your app on the Stripe App Marketplace,
you must uninstall your app in [live
mode](https://docs.stripe.com/stripe-apps/upload-install-app#install-in-live-mode)
first.

## Setting the distribution type for your app

To set the distribution type for your app, run the following command:

```
stripe apps set distribution public
```

```
stripe apps set distribution private
```

This updates the app manifest to reflect the distribution type. The new
distribution takes effect after you [upload your
app](https://docs.stripe.com/stripe-apps/upload-install-app). The private
distribution type is the default type, which you don’t need to explicitly set.

#### Caution

You can continue to change the distribution type until you upload an app. After
you upload an app with a public distribution, you can’t set a public
distribution for another app within the same Stripe account. You can change the
distribution type from private to public if there are no other public apps
within the same Stripe account.

### Updated app manifest:

## App name restrictions

Beginning in September 2024, Stripe apps with a `public` distribution type can’t
contain the words “Stripe”, “app”, “free” or “paid” in their names.

This update won’t impact your previously uploaded or published
[versions](https://docs.stripe.com/stripe-apps/versions-and-releases). However,
the [Stripe CLI](https://docs.stripe.com/stripe-apps/reference/cli) and Stripe
Dashboard will prompt you to change your app’s name in the
[manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest) if:

- You [upload a new app
version](https://docs.stripe.com/stripe-apps/upload-install-app) with a
restricted name and `distribution_type` set to `public`.
- You select a previous app version that contains a restricted name to
distribute with [external
testing](https://docs.stripe.com/stripe-apps/test-app).
- You [submit](https://docs.stripe.com/stripe-apps/publish-app) to the [Stripe
App Marketplace](https://marketplace.stripe.com/) an app version with a
restricted name.

In all these cases, you can proceed by removing the banned words from your app
name in the
[manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest) and
[uploading](https://docs.stripe.com/stripe-apps/upload-install-app) a new
version.

For external testing or the App Marketplace, select that version (or any other
version without the restricted name) for distribution.

## See also

- [Publish your app](https://docs.stripe.com/stripe-apps/publish-app)
- [Upload your app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [Invite team members or developers to access your Stripe
account](https://support.stripe.com/questions/invite-team-members-or-developers-to-access-your-stripe-account)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)

## Links

- [naming
restrictions](https://docs.stripe.com/stripe-apps/distribution-options#app-name-restrictions)
- [team members](https://docs.stripe.com/dashboard/teams)
- [Stripe App Marketplace](https://marketplace.stripe.com)
- [app review
requirements](https://docs.stripe.com/stripe-apps/review-requirements#app-review-requirements)
- [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines)
- [publish your app](https://docs.stripe.com/stripe-apps/publish-app)
- [upload and make
available](https://docs.stripe.com/stripe-apps/upload-install-app)
- [live
mode](https://docs.stripe.com/stripe-apps/upload-install-app#install-in-live-mode)
- [versions](https://docs.stripe.com/stripe-apps/versions-and-releases)
- [Stripe CLI](https://docs.stripe.com/stripe-apps/reference/cli)
- [manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [external testing](https://docs.stripe.com/stripe-apps/test-app)
- [Invite team members or developers to access your Stripe
account](https://support.stripe.com/questions/invite-team-members-or-developers-to-access-your-stripe-account)