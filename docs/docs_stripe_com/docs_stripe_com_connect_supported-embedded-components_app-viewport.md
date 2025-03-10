# App viewportPrivate preview

## Show a view from an installed App.

App viewport renders a view from an installed app.

For full integration details, see the [Embedded Stripe Apps integration
guide](https://docs.stripe.com/stripe-apps/embedded-apps).

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the App
install component by specifying `app_viewport` in the `components` parameter.
You must enable the app you want to render by specifying the `features`
parameter under `allowed_apps`.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[app_viewport][enabled]"=true \
 -d "components[app_viewport][features][allowed_apps][]"=APP_ID
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the App viewport component in the front end. The view doesn’t
render if the app isn’t installed:

```
const appViewport = stripeConnectInstance.create('app-viewport');
appViewport.setApp('{{APP_ID}}');
appViewport.setAppData({userId: '{{PLATFORM_USER_ID}}'});
container.appendChild(appViewport);
```

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setApp``string`Sets the ID of the App your
connected account can render. See available apps in the [Embedded Stripe Apps
integration
guide](https://docs.stripe.com/stripe-apps/embedded-apps#app-select).`setAppData``Record<String,
String>`Sets data pertaining to your platform consumed by the App.
You can integrate our sample app (set `APP_ID` to `stripe.app-explorer`), which
we’ve pre-approved for embedding on your platform.

Read more about [App
install](https://docs.stripe.com/connect/supported-embedded-components/app-install).

## Request early access Private preview

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-viewport)
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
- [Embedded Stripe Apps integration
guide](https://docs.stripe.com/stripe-apps/embedded-apps#app-select)
- [App
install](https://docs.stripe.com/connect/supported-embedded-components/app-install)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-viewport)
- [register now](https://dashboard.stripe.com/register)