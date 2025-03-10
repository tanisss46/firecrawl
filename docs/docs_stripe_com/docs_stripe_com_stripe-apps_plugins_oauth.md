# Migrate a plugin to an OAuth 2.0 app

## Learn how to migrate your plugin to OAuth authentication through Stripe Apps.

Use this guide to migrate your plugin to a Stripe app that uses OAuth 2.0 for
authentication, also known as an OAuth 2.0 app.

Previously, Stripe allowed plugins to request the standard API keys of a user to
integrate with their products. As of September 30, 2024, Stripe requires all
plugin developers to adopt secure authentication methods (restricted API Key,
OAuth 2.0, or Stripe Connect) to protect users against fraud. All existing and
new plugin developers must use one of these secure authorization methods.
Migrating your plugin to an OAuth 2.0 app meets this requirement.

For more information about OAuth 2.0, see [OAuth 2.0 for Stripe
Apps](https://docs.stripe.com/stripe-apps/api-authentication/oauth).

## Before you begin

- Review [Migrate a plugin to Stripe Apps or Stripe
Connect](https://docs.stripe.com/stripe-apps/plugins/decide-migration).
- If you use Stripe Connect and want to migrate an existing plugin through
Stripe Apps, you must create a new Stripe account. Currently, a Stripe account
with Connect enabled can’t publish an app.
- You can only create one public app per account. If your account already has a
public app and you want to publish another one, you must create a new Stripe
account. You can still create multiple private apps in tandem with the public
app on the same account.
[Install the Stripe CLI
plugin](https://docs.stripe.com/stripe-apps/plugins/oauth#install-stripe-cli)-
Sign in to the [Stripe Dashboard](https://dashboard.stripe.com/).
- If you haven’t already, install the Stripe CLI and log in using the same
account.
```
# Install Homebrew to run this command: https://brew.sh/
brew install stripe/stripe-cli/stripe

# Connect the CLI to your dashboard
stripe login
```

For additional install options, see [Get started with the Stripe
CLI](https://docs.stripe.com/stripe-cli).
- Verify that you’re using CLI version `1.12.4` or newer. You can check by
running:
```
stripe version
```

If your Stripe CLI version is older than `1.12.4`, [update to the latest Stripe
CLI version](https://docs.stripe.com/stripe-cli/upgrade).
- Verify that the node is installed and up to date.
```
node -v
```

You can manage your app’s dependencies with NPM or Yarn. Make sure that you use
the latest stable version. If you plan to [publish your app to the App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app), there are
additional restrictions:- Your must have an [activated
account](https://docs.stripe.com/get-started/account/activate).
- You can’t publish an app on a Connect enabled Stripe account.
[Develop your
app](https://docs.stripe.com/stripe-apps/plugins/oauth#develop-app)- Install the
Stripe Apps CLI plugin: To start building a Stripe app, install the Stripe Apps
CLI plugin:

```
stripe plugin install apps
```

If you already have the `apps` plugin installed, verify that you’re on version
`1.5.12` or later.

```
stripe apps -v
# apps version 1.5.12
```

If you need to upgrade the `apps` plugin, you can run:

```
stripe plugin upgrade apps
```
- [Create your Stripe
app](https://docs.stripe.com/stripe-apps/create-app#create-app) by running
`stripe apps create <app-name> in the CLI:

- When naming your app, Stripe prohibits the following terms: Authenticator,
RAK, Generator, RAK Auth, App, Generator App, Stripe.
- Here are some examples of acceptable names: Analytics Pro by DataWiz, Invoice
Manager by PayFlow.
- If you’re developing an app for a third-party service, use this naming
convention: [App Functionality] by [Developer Name]. For example, Hubspot Sync
by Boomi.
- Edit the following fields in the app manifest:

- Set `stripe_api_access_type` to `oauth`.
- Set `distribution_type` to `public`.
- Set your `allowed_redirect_uris`. These are the URLs you redirect users to
after installing your app using OAuth. The first one in the list is the default
redirect.

For example:

```
{
 "id": "<YOUR_APP_ID>",
 "version": "0.0.1",
 "name": "Your Stripe App",
 "icon": "./[YOUR_APP]_icon_32.png",
 "permissions": [
 // Your app permissions here
 ],
 "stripe_api_access_type": "oauth",
 "distribution_type": "public",
 "allowed_redirect_uris": [
 // Your redirect URIs here
 ]
}
```
- Add all the permissions that your app requires using the `stripe apps grant
permission "PERMISSION_NAME" "EXPLANATION"` command.
- (Optional) [Add UI extensions](https://docs.stripe.com/stripe-apps/build-ui)
to your app. We recommend adding a settings view to allow your users to
configure settings or to link to your app’s documentation. If your app’s only
purpose is for authentication, make sure to remove any unnecessary UI or UX
code. This helps keep your app focused on its primary function.
- [Upload your app](https://docs.stripe.com/stripe-apps/upload-install-app) to
Stripe using the `stripe apps upload` command. After you upload your OAuth 2.0
app, you can’t change the [API authentication
method](https://docs.stripe.com/stripe-apps/api-authentication).
- [Configure OAuth
2.0](https://docs.stripe.com/stripe-apps/api-authentication/oauth) to work with
your app and your OAuth provider.

- Make sure you use the correct [OAuth install
link](https://docs.stripe.com/stripe-apps/api-authentication/oauth#create-install-link)
to begin the OAuth flow for your users.
- You must provide a callback URL in your app manifest which can receive the
OAuth authorization code.
- You must use your secret key to [exchange the authorization code for the OAuth
access and refresh
tokens](https://docs.stripe.com/stripe-apps/api-authentication/oauth#obtain-access-token)
applicable with the user’s account.
- You must periodically use the [refresh token to obtain a new access
token](https://docs.stripe.com/stripe-apps/api-authentication/oauth#refresh-access-token)
to avoid requiring your users to authenticate each time their access token
expires.
[Test your app](https://docs.stripe.com/stripe-apps/plugins/oauth#test-app)
You can test your OAuth App on your own account or with other accounts:

- From the [Developer’s Dashboard](https://dashboard.stripe.com/developers) >
[Apps](https://dashboard.stripe.com/apps), select the app you want to test
externally.
- On the app’s details page, click the **External test** tab, then click **Get
Started**.- If you don’t see the **External test** tab, verify if you’ve
selected public distribution from **Create a release**.
- Complete the following fields to configure external testing (which you can
edit at any time):- **Link access**: Choose whether anyone can install the app
using the link or to restrict to invited users only.
- **Version**: Select a version for users to install. Changing the version
updates all current users to the new version.
- the authorize link in the **Test OAuth** section. Send this link to users
to install the app on their account. These users must have administrator rights
to install the app. After a user installs the test version of your app, all
members of the account can use it.

For more information about external testing, see [Test your app
externally](https://docs.stripe.com/stripe-apps/test-app).

[Publish and distribute your
app](https://docs.stripe.com/stripe-apps/plugins/oauth#publish-distribute-app)
To publish your app to the Stripe App Marketplace:

- [Submit your app for
review](https://docs.stripe.com/stripe-apps/publish-app#submit-app-for-review).
- After Stripe approves your app, [publish your app to Stripe App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app#publish-app).

To distribute your app:

- View your [installed apps](https://dashboard.stripe.com/settings/apps), and
click the app you want to distribute. On the app’s detail page, click the
**Settings** tab.
- Identify the [OAuth install
link](https://docs.stripe.com/stripe-apps/api-authentication/oauth#create-install-link)
from when you [developed your
app](https://docs.stripe.com/stripe-apps/plugins/oauth#develop-app). This link
is mode-specific. You must specify live or test mode depending on your use case.
- Consistently use the same OAuth install link across your product and in user
communications. Some examples to consider include:- Update your documentation to
instruct users to install the Stripe OAuth 2.0 app, and remove any steps that
refer to copying and pasting API keys.
- Add the OAuth install link to your plugin onboarding to help users install the
app.
- Use the OAuth install link in email communications with users to help them
update their existing installations.
[Migrate your exisiting
users](https://docs.stripe.com/stripe-apps/plugins/oauth#migrate-existing-users)
After you migrate your plugin to a Stripe App, you must migrate your existing
users. The approach might vary depending on how you usually interact with your
users, but here are some general key steps for all plugins:

- Notify your existing users to update their connection to Stripe using your
OAuth Install Link. This can be through email, in your plugin’s UI, through
in-product notifications, in your release notes, or many other ways.
- After a user installs your app and completes the OAuth flow, delete the
previous secret API key.
- Track user migration progress. If possible, track the progress of user
migrations. Follow up with users who haven’t migrated to ensure a smooth
transition over time.
[OptionalMonitor and improve the health of your
app](https://docs.stripe.com/stripe-apps/plugins/oauth#improve-app-health)
You can explore and implement the following actions to proactively improve the
health of your app:

- To promote your app, consider joining the [Stripe Partner
Ecosystem](https://docs.stripe.com/partners) as part of the [Apps
Track](https://docs.stripe.com/partners#apps-track). All app developers are
eligible for to join the partner program, and apps that achieve certain
milestones can unlock additional partner benefits as they grow.
- To extend the Stripe Dashboard and provide customized functionality for your
users, [Build a UI
Extension](https://docs.stripe.com/stripe-apps/how-ui-extensions-work).
- Track your [App Analytics](https://docs.stripe.com/stripe-apps/analytics) to
gain insights into the performance of your App Marketplace listing, such as user
installation metrics.
[OptionalConfigure
payments](https://docs.stripe.com/stripe-apps/plugins/oauth#configure%20payments)
If you’re building an app that helps users process payments, review these
guidelines:

### Securely collect payment details

Stripe users are subject to [PCI
compliance](https://stripe.com/guides/pci-compliance), which specifies how to
securely store, process, and transmit credit card data. Businesses face
penalties for non-compliance or potential breaches.

Because you’re making API calls on behalf of a Stripe user, you must transmit
credit card data securely using client-side tokenization.
[Customers](https://docs.stripe.com/api/customers) submit their personal
information through their web browser or mobile app directly to Stripe, and in
return, Stripe sends a simple token to you. This allows your users to securely
collect card details without sensitive data ever touching their server.

If your plugin includes a client-side payment form in the browser, we recommend
that you use either:

- [Stripe Elements](https://docs.stripe.com/payments/elements): A set of
prebuilt UI components for building your web checkout flow. It’s available as a
feature of [Stripe.js](https://docs.stripe.com/js), our foundational JavaScript
library for building payment flows.
- [Stripe Checkout](https://docs.stripe.com/payments/checkout): A low-code
payment integration that creates a customizable form for collecting payments.
You can embed Checkout directly in your website or redirect customers to a
Stripe-hosted payment page.

Both of these options provide client-side tokenization.

If your plugin only operates in a back-end environment, include a note in your
documentation asking users to tokenize payment details using Elements or
Checkout. Tokenization helps Stripe users process as safely as possible on our
platform.

### Add the Express Checkout Element

The [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element) provides a
single integration for accepting payments through one-click payment buttons,
including Apple Pay, Google Pay, Link, or PayPal. This integration allows you to
display multiple buttons at the same time. Customers see different payment
buttons depending on what their device and browser combination supports.

### Enable multiple payment methods

Stripe supports multiple payment methods, aside from credit cards. To learn more
about payment methods, see [Payment
methods](https://docs.stripe.com/payments/payment-methods/overview).

The [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
enables your users to collect payments using additional payment methods (for
example, Alipay, iDEAL, Sofort). You can add these [payment
methods](https://docs.stripe.com/payments/payment-methods#supported-payment-methods)
using one integration path.

### Verify that HTTPS is enabled

If your plugin presents a payment form in a web browser, it must check that the
form is being served over HTTPS. We require our users to enable HTTPS. Present a
clear error to your user if they’re not properly secured.

The following example shows how to verify whether your users have HTTPS enabled:

```
// This example uses Express
const express = require('express');
const app = express();

app.get('/', function(request, response) {
 if (!request.secure) {
 // Present an error to the user
 }
});

app.listen(3000);
```

If your plugin has a front-end component, check whether HTTPS is being used from
the browser. For example, using JavaScript:

```
// This example checks for HTTPS from the browser
if (window.location.protocol !== "https:") {
 // Present an error to the user
}
```

## See also

- [Migrate a plugin to Stripe Apps or Stripe
Connect](https://docs.stripe.com/stripe-apps/plugins/decide-migration).
- [Migrate a plugin to an RAK
app](https://docs.stripe.com/stripe-apps/plugins/rak)

## Links

- [OAuth 2.0 for Stripe
Apps](https://docs.stripe.com/stripe-apps/api-authentication/oauth)
- [Migrate a plugin to Stripe Apps or Stripe
Connect](https://docs.stripe.com/stripe-apps/plugins/decide-migration)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [https://brew.sh/](https://brew.sh/)
- [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [update to the latest Stripe CLI
version](https://docs.stripe.com/stripe-cli/upgrade)
- [publish your app to the App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app)
- [activated account](https://docs.stripe.com/get-started/account/activate)
- [Create your Stripe
app](https://docs.stripe.com/stripe-apps/create-app#create-app)
- [Add UI extensions](https://docs.stripe.com/stripe-apps/build-ui)
- [Upload your app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [API authentication
method](https://docs.stripe.com/stripe-apps/api-authentication)
- [OAuth install
link](https://docs.stripe.com/stripe-apps/api-authentication/oauth#create-install-link)
- [exchange the authorization code for the OAuth access and refresh
tokens](https://docs.stripe.com/stripe-apps/api-authentication/oauth#obtain-access-token)
- [refresh token to obtain a new access
token](https://docs.stripe.com/stripe-apps/api-authentication/oauth#refresh-access-token)
- [Developer’s Dashboard](https://dashboard.stripe.com/developers)
- [Apps](https://dashboard.stripe.com/apps)
- [Test your app externally](https://docs.stripe.com/stripe-apps/test-app)
- [Submit your app for
review](https://docs.stripe.com/stripe-apps/publish-app#submit-app-for-review)
- [publish your app to Stripe App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app#publish-app)
- [installed apps](https://dashboard.stripe.com/settings/apps)
- [developed your
app](https://docs.stripe.com/stripe-apps/plugins/oauth#develop-app)
- [Stripe Partner Ecosystem](https://docs.stripe.com/partners)
- [Apps Track](https://docs.stripe.com/partners#apps-track)
- [Build a UI
Extension](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [App Analytics](https://docs.stripe.com/stripe-apps/analytics)
- [PCI compliance](https://stripe.com/guides/pci-compliance)
- [Customers](https://docs.stripe.com/api/customers)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Stripe.js](https://docs.stripe.com/js)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Payment methods](https://docs.stripe.com/payments/payment-methods/overview)
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
- [payment
methods](https://docs.stripe.com/payments/payment-methods#supported-payment-methods)
- [Migrate a plugin to an RAK
app](https://docs.stripe.com/stripe-apps/plugins/rak)