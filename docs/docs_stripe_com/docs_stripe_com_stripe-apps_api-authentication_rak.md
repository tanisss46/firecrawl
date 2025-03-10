# Restricted API key authentication

## Generate a permissioned restricted API key (RAK) when a user installs your app.

A user authenticating with the RAK follows these steps.

- On your site, the user clicks a link that redirects them to Stripe.
- On Stripe, the user selects the appropriate account and accepts permissions
for installing the app.
- After the app is installed, it generates a restricted API key provisioned with
the proper permissions.
- The user copies the generated keys and provides them to your site.

![Installing an app to generate a
RAK](https://b.stripecdn.com/docs-statics-srv/assets/rak-user-journey.14fda11d13eaeb5cdbebbea71f277126.png)

[Develop your
app](https://docs.stripe.com/stripe-apps/api-authentication/rak#develop-app)-
Create your app using our template.

```
stripe apps create <app-name> --template restricted-api-key-app
```

If you have an existing app, run this command in Stripe CLI:

```
stripe apps set api-access-type restricted_api_key
```
- Add all the
[permissions](https://docs.stripe.com/stripe-apps/reference/permissions) that
your app requires.
- Edit your [app settings
page](https://docs.stripe.com/stripe-apps/app-settings). If you use the template
above, a settings view is automatically created. We recommend adding
instructions or links to your own documentation on this page for users to
reference when setting up your app.

![The install link page showing app
permissions](https://b.stripecdn.com/docs-statics-srv/assets/settingsview.ca0e43bcc311ea9819da61b2949e6ed1.png)

Example app settings page
- [Upload](https://docs.stripe.com/stripe-apps/upload-install-app) your app to
Stripe.

#### Note

After you upload your RAK app, you can’t change the [API authentication
method](https://docs.stripe.com/stripe-apps/api-authentication).

```
stripe apps upload
```
[Test your
app](https://docs.stripe.com/stripe-apps/api-authentication/rak#test-app)
You can test the RAK authentication on your own account.

- [Install your app in test
mode](https://docs.stripe.com/stripe-apps/versions-and-releases#changing-between-versions)
on your account.
- Go to your [installed apps page](https://dashboard.stripe.com/settings/apps)
in settings and click your recently installed app.
- From the app settings page, click **View API keys**. this secret key to
test your integration.

To test your app on a different Stripe account than the one used to develop your
app, use [external testing](https://docs.stripe.com/stripe-apps/test-app).

## Links

- [permissions](https://docs.stripe.com/stripe-apps/reference/permissions)
- [app settings page](https://docs.stripe.com/stripe-apps/app-settings)
- [Upload](https://docs.stripe.com/stripe-apps/upload-install-app)
- [API authentication
method](https://docs.stripe.com/stripe-apps/api-authentication)
- [Install your app in test
mode](https://docs.stripe.com/stripe-apps/versions-and-releases#changing-between-versions)
- [installed apps page](https://dashboard.stripe.com/settings/apps)
- [external testing](https://docs.stripe.com/stripe-apps/test-app)