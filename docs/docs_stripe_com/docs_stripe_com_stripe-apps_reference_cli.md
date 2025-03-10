# Stripe Apps CLI reference

## Install the Stripe Apps command line interface and use it to manage your app.

The Stripe Apps CLI helps you create, develop, configure, and upload your Stripe
app using the terminal.

## Before you begin

- [Log in to the Stripe Dashboard](https://dashboard.stripe.com/) using your
existing Stripe account, or by creating a new one.
- [Install the Stripe CLI](https://docs.stripe.com/stripe-cli).
- Log in to the CLI using the same account you logged into the Stripe Dashboard
with.
```
stripe login
```
- Verify that you’re using CLI version 1.8.11 or newer.
```
stripe version
# expected output: stripe version 1.8.11
```

## Install the CLI plugin

To install the Stripe Apps CLI plugin, run:

```
stripe plugin install apps
```

## Upgrade the CLI plugin

To get the latest version of the Stripe Apps CLI plugin, run:

```
stripe plugin upgrade apps
```

## Command overview

CommandDescription`create`Create a new Stripe app.`start`Start a development
server for viewing your app in the Stripe Dashboard. Use the `--manifest` flag
to [load an extended manifest
file](https://docs.stripe.com/stripe-apps/reference/app-manifest#extended-manifest).`add`Add
a building block for developing your app.`remove`Remove a building block from
your `stripe-app.json` file.`grant`Grant configuration access to your
app.`revoke`Revoke configuration access to your app.`set`Set a configuration
value within the app manifest.`upload`Upload your app to be submitted for
review.`version`Print the version of Stripe Apps CLI plugin.
## See also

- [App manifest
reference](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [Upload and install your Stripe
App](https://docs.stripe.com/stripe-apps/upload-install-app)

## Links

- [Log in to the Stripe Dashboard](https://dashboard.stripe.com/)
- [Install the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [load an extended manifest
file](https://docs.stripe.com/stripe-apps/reference/app-manifest#extended-manifest)
- [App manifest
reference](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [Upload and install your Stripe
App](https://docs.stripe.com/stripe-apps/upload-install-app)