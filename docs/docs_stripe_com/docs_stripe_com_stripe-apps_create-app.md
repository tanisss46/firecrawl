# Getting started with Stripe Apps

## Learn the basics of app development by building, previewing, and updating a Stripe app.

In this guide, build a “Hello, world!” sample app with a UI extension on the
Customer details page in the Stripe Dashboard.

## Before you begin

- If you have an existing [Connect](https://docs.stripe.com/connect) extension,
see [Migrate to Stripe
Apps](https://docs.stripe.com/stripe-apps/migrate-extension).
- Sign in to the [Stripe Dashboard](https://dashboard.stripe.com/).
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
- Verify that you’re using CLI version 1.12.4 or newer. You can check by
running:
```
stripe version
```

If your Stripe CLI version is older than 1.12.4, [update your Stripe CLI version
to the latest version](https://docs.stripe.com/stripe-cli/upgrade).
- Verify that node is installed and up to date.
```
node -v
```

You can manage your app’s dependencies with NPM or Yarn. Use the latest stable
version for the best development experience. If you plan to [publish your app to
the App Marketplace](https://docs.stripe.com/stripe-apps/publish-app), there are
additional restrictions:
- Your account must be
[activated](https://docs.stripe.com/get-started/account/activate).
- Currently to publish an app on the Stripe Marketplace, you can’t be a Platform
account.
[Install the Stripe Apps CLI
plugin](https://docs.stripe.com/stripe-apps/create-app#install-stripe-apps-cli)
To start building a Stripe app, install the Stripe Apps CLI plugin:

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

[Create an app](https://docs.stripe.com/stripe-apps/create-app#create-app)-
Build the basic structure of your “Hello, world!” app:

```
stripe apps create helloworld
```
- Follow the prompts by entering the following information:

- **ID**: You can accept the auto-generated app ID or customize one. This is how
Stripe identifies your app. Your [app
ID](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema) must be
globally unique.
- **Display name**: Enter a display name. This is the name your Dashboard
displays for your app. You can always change the name later.

### Your directory file structure is now:

Stripe Apps only supports React 17. Make sure any dependency you install is
compatible with this version. For more information see [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#apps-cant-control-the-react-version).

[Preview your app](https://docs.stripe.com/stripe-apps/create-app#preview-app)
You can run your app locally, update it, and preview your changes in the
Dashboard:

- Go into the `helloworld` directory:

```
cd helloworld
```
- To preview your app, start your local development server:

```
stripe apps start
```
- Press **Enter** to open your browser.

#### Note

Use a [browser that supports the Stripe
Dashboard](https://docs.stripe.com/dashboard/basics). Safari doesn’t support the
Dashboard. For more updates, see the [GitHub issue tracking browser
support](https://github.com/stripe/stripe-apps/issues/146).
- Click **Continue** to preview your app in your Stripe account:

![Screenshot of enabling preview
mode](https://b.stripecdn.com/docs-statics-srv/assets/enable_app_preview.7d71712d107d581e0a25a4ebaf71484e.png)

Enable app preview

![Hello World
app](https://b.stripecdn.com/docs-statics-srv/assets/helloworld_app.7b1588ce22f93f72ab2ecd07c44dd041.png)

Your app in the Dashboard

The `App` view only renders on the Customer details page in the Dashboard. If
you don’t see your app, make sure you [create a customer in the
Dashboard](https://docs.stripe.com/invoicing/customer).

[Build your app](https://docs.stripe.com/stripe-apps/create-app#build-app)
While you’re previewing your app in the Dashboard, the local development server
enables real-time updates on your app:

- In your `App.tsx` file, change the title while you keep the Stripe Dashboard
page open and your development server running. Save the file to see your changes
in your app.
- In the same file, remove `>` from the `</ContextView>` closing tag, and save
the file to see an error:

![Hello World
error](https://b.stripecdn.com/docs-statics-srv/assets/helloworld_error.ee7aeea9d33b54f1e17b108f61741e97.png)

You can resolve the error in the Stripe Dashboard, your browser developer tools,
or the Stripe CLI.
- To stop the development server, **Ctrl+C** from your command line.

Your sample app is complete. Next, start adding more features to your Stripe
app.

## See also

- [Build a UI extension](https://docs.stripe.com/stripe-apps/build-ui)
- [Add server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [Distribution
options](https://docs.stripe.com/stripe-apps/distribution-options)

## Links

- [Connect](https://docs.stripe.com/connect)
- [Migrate to Stripe
Apps](https://docs.stripe.com/stripe-apps/migrate-extension)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [https://brew.sh/](https://brew.sh/)
- [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [update your Stripe CLI version to the latest
version](https://docs.stripe.com/stripe-cli/upgrade)
- [publish your app to the App
Marketplace](https://docs.stripe.com/stripe-apps/publish-app)
- [activated](https://docs.stripe.com/get-started/account/activate)
- [app ID](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#apps-cant-control-the-react-version)
- [browser that supports the Stripe
Dashboard](https://docs.stripe.com/dashboard/basics)
- [GitHub issue tracking browser
support](https://github.com/stripe/stripe-apps/issues/146)
- [create a customer in the
Dashboard](https://docs.stripe.com/invoicing/customer)
- [Build a UI extension](https://docs.stripe.com/stripe-apps/build-ui)
- [Add server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [Distribution
options](https://docs.stripe.com/stripe-apps/distribution-options)