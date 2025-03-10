# Upload and install your Stripe App

## Make your app available to team members on your Stripe account.

To share your app with your [team
members](https://docs.stripe.com/dashboard/teams), install it on your Stripe
account with two steps:

- [Upload in test
mode](https://docs.stripe.com/stripe-apps/upload-install-app#upload-your-app-in-test-mode)
- [Install in live
mode](https://docs.stripe.com/stripe-apps/upload-install-app#install-in-live-mode)

Any team member with access to your Stripe account can run your installed apps.
To give other Stripe accounts access, you can [publish your
app](https://docs.stripe.com/stripe-apps/publish-app) on the Stripe App
Marketplace. Your [app
ID](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema) must be
globally unique.

[Upload in test
mode](https://docs.stripe.com/stripe-apps/upload-install-app#install-your-app-in-test-mode)
To upload your app, run the following command from your project root directory:

```
stripe apps upload
```

Stripe validates your [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest), then
uploads your app to your Stripe test account. After validation is a complete, a
banner is shown with a prompt and button to install the new version into test
mode.

You can install previous versions though the Version History list.

- In the version history table, click the overflow menu () of the version you
want to install.
- Select **Install in test mode** and complete the installation.

After this step:

- Any team member can access your app in [test
mode](https://docs.stripe.com/test-mode) at
[https://dashboard.stripe.com/test/](https://dashboard.stripe.com/test/).
- Your app can [store
secrets](https://docs.stripe.com/stripe-apps/store-secrets) in test mode.
- You can access your app’s signing secret to connect it to a
[backend](https://docs.stripe.com/stripe-apps/build-backend).
[Install in live
mode](https://docs.stripe.com/stripe-apps/upload-install-app#install-in-live-mode)
To access real customer data, install your app in live mode.

- Select your app from the [Apps page in the Developers
Dashboard](https://dashboard.stripe.com/apps).
- Select the **Private to your account** option when choosing how to distribute.
- Choose a version for your app and click **Continue**.
- Click **Continue** to open your app in the Dashboard, then click **Install**.
- Click **Done**, refresh your browser, and see your app in live mode across the
Dashboard in the right-hand side drawer.

After this step:

- Any team member can access your app in live mode in the Dashboard.
- Your app can [store
secrets](https://docs.stripe.com/stripe-apps/store-secrets) in live mode.
- Your app’s signing secret remains available.

### Uninstall your app in live mode

To switch between installing your app in live mode to publishing it on the
[Stripe App Marketplace](https://marketplace.stripe.com/), uninstall the app in
live mode:

- Go to the [Installed Apps page in the
Dashboard](https://dashboard.stripe.com/settings/apps/), and find the app you
want to uninstall.
- Click the overflow menu at the right side of your app, and click **View app
details**.
- Click **Uninstall app**, and click **Uninstall**.

After this step, you can [publish your app to the Stripe App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app).

## See also

- [Add deep links](https://docs.stripe.com/stripe-apps/deep-links)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)

## Links

- [Store secrets](https://docs.stripe.com/stripe-apps/store-secrets)
- [Add server-side
functionality](https://docs.stripe.com/stripe-apps/build-backend)
- [team members](https://docs.stripe.com/dashboard/teams)
- [publish your app](https://docs.stripe.com/stripe-apps/publish-app)
- [app ID](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [test mode](https://docs.stripe.com/test-mode)
- [https://dashboard.stripe.com/test/](https://dashboard.stripe.com/test/)
- [Apps page in the Developers Dashboard](https://dashboard.stripe.com/apps)
- [Stripe App Marketplace](https://marketplace.stripe.com)
- [Installed Apps page in the
Dashboard](https://dashboard.stripe.com/settings/apps/)
- [Add deep links](https://docs.stripe.com/stripe-apps/deep-links)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)