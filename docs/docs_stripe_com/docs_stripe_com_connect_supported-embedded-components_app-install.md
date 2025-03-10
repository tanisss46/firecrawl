# App installPrivate preview

## Show a button to install an app.

App install renders a component that enables your connected account to install
an app.

For full integration details, see the [Embedded Stripe Apps integration
guide](https://docs.stripe.com/stripe-apps/embedded-apps).

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the App
install component by specifying `app_install` in the `components` parameter. You
must enable the app you want to install by specifying the `features` parameter
under `allowed_apps`.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[app_install][enabled]"=true \
 -d "components[app_install][features][allowed_apps][]"=APP_ID
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the App install component in the front end:

```
const appInstall = stripeConnectInstance.create('app-install');
appViewport.setApp('{{APP_ID}}');
container.appInstall(appViewport);
```

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setApp``string`Sets the ID of the App your
connected account can install. See the list of [available
apps](https://docs.stripe.com/stripe-apps/embedded-apps#app-select).
You can configure custom behavior based on the current or updated state of an
install. To do so, set a custom callback function using the following methods:

HTML + JSReactMethodDescriptionVariables`setOnAppInstallStateFetched`Allows
users to specify custom behavior in a callback function on install fetch.-
`response.appId`: The app installed
- `response.state`: The state of the install `INSTALLED | UNINSTALLED`
`setOnAppInstallStateChanged`Allows users to specify custom behavior in a
callback function when the install state has changed.- `response.appId`: The app
installed
- `response.state`: The state of the install `INSTALLED | UNINSTALLED`

You can integrate our sample app (set `APP_ID` to `stripe.app-explorer`), which
we’ve pre-approved for embedding on your platform.

## Request early access Private preview

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-install)
to request access to this Connect embedded component in preview.

If you don’t have a Stripe account, you can [register
now](https://dashboard.stripe.com/register).

## Links

- [Embedded Stripe Apps integration
guide](https://docs.stripe.com/stripe-apps/embedded-apps)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [available apps](https://docs.stripe.com/stripe-apps/embedded-apps#app-select)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-install)
- [register now](https://dashboard.stripe.com/register)