# Migrate an extension to Stripe Apps

## Learn why and how to migrate your extensions to Stripe Apps.

[Extensions](https://docs.stripe.com/building-extensions) are legacy apps built
on Stripe, available to Stripe users in the [Partner
Directory](https://stripe.partners/). Through OAuth and API requests, they bring
payments data into other business tools, like analytics dashboards or data
warehouses.

[Stripe Apps](https://stripe.com/apps) replaces extensions as the preferred way
to integrate Stripe with other tools. Stripe will redirect users from the
[Partner Directory](https://stripe.partners/) to discover apps on the [Stripe
App Marketplace](https://marketplace.stripe.com/).

After May 24, 2022, you can no longer create new extensions. On August 31, 2022,
Stripe will remove all mentions of extensions on the Partner Directory. If you
own an extension, migrate to Stripe Apps now to ensure continued
discoverability.

## Reasons to migrate

Stripe Apps is an upgrade from the current extensions. By migrating, you get the
following:

- Better discoverability, with broad visibility in the Stripe Dashboard and the
Stripe App Marketplace
- More granular permissions, so you can set (and your users can understand) what
data and APIs an app can access
- Interactive functionality, with embedded UI components in the Stripe Dashboard
(so users can interact directly with your app without leaving Stripe)
- No interruption to your existing extension users if they choose to migrate

### What happens if you don’t migrate

If you choose not to migrate your extension to a Stripe App, your extension will
continue to work as it does today, without impact to users until 2024. We’ll
continue to support extensions on our backend until the end of 2024. However,
new users won’t be able to find any mention of extensions in the [Partner
Directory](https://stripe.partners/) starting August 31, 2022.

## Stripe Apps vs. extensions

An app can do everything an extension does, with two key additions:

- Interactive functionality, using embedded UI components in the Stripe
Dashboard
- More granular permissions to help users understand what an app can access

The other difference is that any user can discover apps from the Stripe App
Marketplace instead of the Partner Directory.

ExtensionsStripe AppsAny Stripe user can use.Any Stripe user can use.After
August 31, 2022, Stripe will remove all mentions of extensions from the [Partner
Directory](https://stripe.partners/).Discoverable in the [Stripe App
Marketplace](https://marketplace.stripe.com/), with better visibility to all
Stripe users.You can find your existing extensions in the Dashboard, under
Developers > Extensions.You can find your apps in the Dashboard, under
Developers > [Apps](https://dashboard.stripe.com/apps).Extensions are limited to
either all read or all write permissions. No support for granular
permissions.You can request a granular set of permissions from users as part of
app installation.You can’t create new extensions after May 24, 2022.Any
developer can build on Stripe’s platform.After users link their Stripe accounts
to your extension with OAuth, you can make API requests on their behalf.After
users authorize and install your app, you can make API requests on their
behalf.Users interact with your extension by installing additional tools and
leaving Stripe.Users can interact with your app within the Stripe UI without
leaving Stripe.No ability to extend the Stripe UI.You can build directly on top
of the Stripe UI, starting with the Stripe Dashboard.
## Impact on your extension’s users

After migrating your extension, your existing users will see a badge in their
[extension settings](https://dashboard.stripe.com/test/extensions) page
prompting them to re-authenticate. Your users must accept permissions to begin
using your migrated app. If they choose not to accept permissions, they can
continue to use their extension uninterrupted until 2024.

Migrating lets you keep your existing extension code on the Stripe account
you’re already using. You can’t have both an existing extension and a Stripe app
on the same Stripe account—you can only have either an extension or an app. If
you choose to migrate, you must migrate using the Stripe account linked to your
extension. Using the same Stripe account also ensures continuity in the user
experience, and users only need to accept a prompt in the Stripe Dashboard to
switch from an extension to your new app.

If you don’t want to migrate your extension, and you still want to create an
app, you will encounter several restrictions:

- You must create another Stripe account to publish the app.
- The app must have a unique and different purpose than your existing
extension’s service.

## Migrate to Stripe Apps

Follow the steps below to migrate your extension to a Stripe App.

![Steps to migrate an extension to a Stripe
App](https://b.stripecdn.com/docs-statics-srv/assets/migrate_to_stripe_app_diagram.a741f6bfbd91e5840e123d581733bca9.png)

Migrating an extension to a Stripe App

## Before you begin

- To protect your extension’s users while you develop your Stripe App,
[test](https://docs.stripe.com/stripe-apps/test-app) and upload your app with a
separate or new Stripe account to fully separate the app’s users from your
extension’s users.
- To add an extra layer of safety, create a separate testing instance of your
backend. While testing your Stripe app, avoid making changes to the backend code
powering your live extension.
- After you have fully tested your Stripe app, upload the app to the same Stripe
account that links to your extension to submit for App Review.
[Create an app
manifest](https://docs.stripe.com/stripe-apps/migrate-extension#create-app-manifest)
[Create an app manifest by creating a Stripe
App](https://docs.stripe.com/stripe-apps/create-app).

[Add interactive
functionality](https://docs.stripe.com/stripe-apps/migrate-extension#add-additional-functionality)
Optionally, you can add interactive functionality in the Stripe Dashboard with
UI components:

- [Build UI components on your Stripe
App](https://docs.stripe.com/stripe-apps/build-ui).
- [Build a self-hosted backend and authenticate users to your
backend](https://docs.stripe.com/stripe-apps/build-backend).
[Add a webhook
listener](https://docs.stripe.com/stripe-apps/migrate-extension#add-a-webhook-listener)
Make sure your extension can make authenticated requests to Stripe. [Add a
webhook
listener](https://docs.stripe.com/stripe-apps/build-backend#receiving-events-webhooks)
for the `account.application.authorized` event.

Each event for a connected account contains the documented response properties
in the [event object reference](https://docs.stripe.com/api#events) and a
top-level `account` property. The `account` property identifies the unique user
the webhook is for:

```
{
 "id": "evt_",
 "livemode": true,
 "object": "event",
 "type": "account.application.authorized",
 "account": "acct_",
 "pending_webhooks": 2,
 "created": 1349654313,
 "data": {...}
}
```

The user is now connected to your platform. Store the `account` in your
database—this is the Stripe ID for the new account. You’ll use this value to
[authenticate](https://docs.stripe.com/connect/authentication) as the connected
account by passing it into requests in the `Stripe-Account` header.

For more information, see [Connect
webhooks](https://docs.stripe.com/connect/webhooks).

[Add permissions and upload your
app](https://docs.stripe.com/stripe-apps/migrate-extension#add-permissions-and-upload)
[Add permissions to your app manifest and upload your
app](https://docs.stripe.com/stripe-apps/publish-app). After uploading the app,
you can use the permission migration tool on the App Details page to view
recommended missing permissions. Administrators of your connected accounts must
accept these permissions to migrate to your app.

#### Warning

The permissions model for Stripe Apps will overwrite the global permissions
previously accepted by a user that authorized an extension. To ensure your
existing users don’t experience permissions related interruptions, you must
identify which objects your extension (not your app) calls on the Stripe API to
know which permissions to add to your app.

The migration process between your connected account administrator, Stripe, and
your extension looks like:

![migrated app permissions
diagram](https://b.stripecdn.com/docs-statics-srv/assets/migrated-app-permissions-diagram.8ed2661a5c4c75477ccd9aa77f02cd13.png)

You can find the migration tool by navigating to your app on the App Details
page in the [Dashboard](https://dashboard.stripe.com/apps). The tool exists in
multiple locations highlighted below.

![Entry point for permission migration tool for unpublished
apps](https://b.stripecdn.com/docs-statics-srv/assets/permission_tool_entry_point_unpublished.400af30ac4fb84772931a492e8b7edbe.png)

Callout and button for unpublished apps

![Entry point for permission migration tool for published
apps](https://b.stripecdn.com/docs-statics-srv/assets/permission_tool_entry_point_published.1c4da81be36b34728ab23812763573ab.png)

Pushed to overflow menu option when app is published

After your app passes review and you publish your app, your extension’s users
must accept permissions in their Dashboard settings to see and use the migrated
app. If you [add UI
extensions](https://docs.stripe.com/stripe-apps/migrate-extension#add-additional-functionality),
users get redirected to the Stripe App Marketplace to accept changes instead of
in the Dashboard.

[Publish your
app](https://docs.stripe.com/stripe-apps/migrate-extension#publish-app)
[Submit your app for review and publish it on the Stripe App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app).

To increase your chances of passing app review, adhere to Stripe’s:

- [App review
requirements](https://docs.stripe.com/stripe-apps/review-requirements)
- [App listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines)

#### Caution

When you provide test credentials, make sure the account has access to the new
app installation flow.

Your app **must pass** app review to list it in the Stripe App Marketplace. When
you’re ready to publish your app, use the primary Stripe account you use for
live mode traffic so that your extension’s users can migrate to your app.

[Onboard
users](https://docs.stripe.com/stripe-apps/migrate-extension#onboard-users)
After migration, your existing users must re-authenticate in the Dashboard to
use your Stripe app. If they don’t accept the permissions prompt, they can
continue to use your extension uninterrupted until 2024.

You can onboard *new* users to your Stripe App in two ways:

- You can list your migrated app in the Stripe App Marketplace after migrating
your app and passing the app listing requirements. Any Stripe App on the Stripe
App Marketplace will be available to install to Stripe account users starting
late June 2022.
- New users can continue to onboard to your extension with OAuth from your
website. After users accept OAuth authorization and return to the Stripe
Dashboard, Stripe prompts them to use your migrated Stripe App instead. If they
decline, users can continue using the extension uninterrupted until 2024.

#### Note

To avoid onboarding new users with OAuth after you complete the migration, you
can remove your OAuth callbacks and redirect new users to your app listing on
the Stripe App Marketplace by changing your website’s **Connect with Stripe**
button. If you remove OAuth callbacks, you can’t onboard new users until late
June 2022, using the Stripe App Marketplace. If you don’t remove OAuth
callbacks, you’re responsible for managing the separate listings and users for
both your extension and Stripe App.

## See also

- [Stripe Apps](https://docs.stripe.com/stripe-apps)
- [Sample apps](https://docs.stripe.com/stripe-apps/sample-apps)

## Links

- [Extensions](https://docs.stripe.com/building-extensions)
- [Partner Directory](https://stripe.partners)
- [Stripe Apps](https://stripe.com/apps)
- [Stripe App Marketplace](https://marketplace.stripe.com)
- [Apps](https://dashboard.stripe.com/apps)
- [extension settings](https://dashboard.stripe.com/test/extensions)
- [test](https://docs.stripe.com/stripe-apps/test-app)
- [Create an app manifest by creating a Stripe
App](https://docs.stripe.com/stripe-apps/create-app)
- [Build UI components on your Stripe
App](https://docs.stripe.com/stripe-apps/build-ui)
- [Build a self-hosted backend and authenticate users to your
backend](https://docs.stripe.com/stripe-apps/build-backend)
- [Add a webhook
listener](https://docs.stripe.com/stripe-apps/build-backend#receiving-events-webhooks)
- [event object reference](https://docs.stripe.com/api#events)
- [authenticate](https://docs.stripe.com/connect/authentication)
- [Connect webhooks](https://docs.stripe.com/connect/webhooks)
- [Add permissions to your app manifest and upload your
app](https://docs.stripe.com/stripe-apps/publish-app)
- [App review
requirements](https://docs.stripe.com/stripe-apps/review-requirements)
- [App listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines)
- [Stripe Apps](https://docs.stripe.com/stripe-apps)
- [Sample apps](https://docs.stripe.com/stripe-apps/sample-apps)