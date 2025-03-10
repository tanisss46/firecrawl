# Payment method settingsPrivate preview

## Display a configurable list of payment methods that connected accounts can offer during checkout.

Render a connected account’s [Payment Method
Configuration](https://docs.stripe.com/api/payment_method_configurations) to
enable customization of payment methods displayed at checkout. Connected
accounts can customize their checkout payment methods and provide the necessary
compliance details for their usage.

#### Private preview

This Connect embedded component is in private preview. [Request
access](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#request-access)
below.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
#### Note

We support the following payment methods in the embedded component:

Affirm, Afterpay Clearpay, Amazon Pay, Apple Pay, Bancontact, BLIK, Cards, EPS,
Google Pay, iDEAL, Klarna, Link, P24, Sofort, and Zip.

The embedded payment method settings uses the [Payment Method
Configurations](https://docs.stripe.com/connect/payment-method-configurations)
and [Account Capabilities](https://docs.stripe.com/connect/account-capabilities)
APIs to display a list of customizable payment methods to your connected
accounts. If a connected account requires additional compliance data prior to
requesting the payment method
[capability](https://docs.stripe.com/api/capabilities/object), the component
indicates this and collects the necessary information in advance.

## Requirements

Your integration must use [dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods) to
automatically apply the connected account’s preferences during checkout. In
prebuilt payment UIs such as [Payment
Element](https://stripe.com/payments/elements) and
[Checkout](https://stripe.com/payments/checkout), Stripe handles the logic for
displaying eligible payment methods for each transaction.

Install a beta version of the Stripe SDKs to create account sessions for private
preview components:

- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks) `>=13.4.0-beta.4`
- [Python](https://github.com/stripe/stripe-python/#beta-sdks) `>=11.5.0b3`
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks) `>=16.5.0-beta.3`
- [Node](https://github.com/stripe/stripe-node/#beta-sdks) `>=17.6.0-beta.3`
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks) `>=47.3.0-beta.3`
- [Java](https://github.com/stripe/stripe-java#beta-sdks) `>=28.3.0-beta.3`
- [Go](https://github.com/stripe/stripe-go#beta-sdks) `>=81.3.0-beta.3`

Use the beta version of the Stripe’s client-side libraries to render private
preview components:

npmGitHub
Install the library:

`npm install --save @stripe/connect-js@preview`
If you’re using React in your application:

`npm install --save @stripe/react-connect-js@preview`
## Integrate the component

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable payment
method settings by specifying `payment_method_settings` in the `components`
parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payment_method_settings][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payment method settings component in the frontend:

```
// Include this element in your HTML
const paymentMethodSettings =
stripeConnectInstance.create('payment-method-settings');
container.appendChild(paymentMethodSettings);
```

### Platform-level controls

The embedded payment method settings component respects the platform-level
defaults that you configure in the
[Dashboard](https://docs.stripe.com/connect/payment-methods) or the [Payment
Method Configurations
API](https://docs.stripe.com/connect/payment-method-configurations).

For payment methods that you configure as **On by default** or **Off by
default**, the connected account can override that preference in the component.
If you have set a payment method to **Blocked**, it’s completely hidden in the
component.

### Multiple payment method configurations

With default settings, the embedded payment method settings component shows the
connected account’s default payment method configuration. During the preview,
the component supports [multiple
configurations](https://docs.stripe.com/connect/multiple-payment-method-configurations)
with the `payment-method-configuration` attribute.

### Supported parameters

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setPaymentMethodConfiguration``string`Set
the payment method configuration ID to appear in the component. You can pass any
payment method configuration that the connected account owns. If you don’t set
this parameter, the embedded component shows the connected account’s default
payment method configuration that inherits from your platform’s settings. For
more information, see [Payment method
configurations](https://docs.stripe.com/payments/payment-method-configurations)
or [List payment method
configurations](https://docs.stripe.com/api/payment_method_configurations/list).optional
## Request early access Private preview

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-method-settings)
to request access to this Connect embedded component in preview.

If you don’t have a Stripe account, you can [register
here](https://dashboard.stripe.com/register).

## See also

- [Connect integration guide](https://docs.stripe.com/connect/charges)
- [Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)
- [Payment Method Configurations
API](https://docs.stripe.com/connect/payment-method-configurations)
- [Account Capabilities
API](https://docs.stripe.com/connect/account-capabilities)

## Links

- [Payment Method
Configuration](https://docs.stripe.com/api/payment_method_configurations)
- [Request
access](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#request-access)
- [furever.dev](https://furever.dev)
- [Payment Method
Configurations](https://docs.stripe.com/connect/payment-method-configurations)
- [Account Capabilities](https://docs.stripe.com/connect/account-capabilities)
- [capability](https://docs.stripe.com/api/capabilities/object)
- [dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)
- [Payment Element](https://stripe.com/payments/elements)
- [Checkout](https://stripe.com/payments/checkout)
- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks)
- [Python](https://github.com/stripe/stripe-python/#beta-sdks)
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks)
- [Node](https://github.com/stripe/stripe-node/#beta-sdks)
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks)
- [Java](https://github.com/stripe/stripe-java#beta-sdks)
- [Go](https://github.com/stripe/stripe-go#beta-sdks)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [Dashboard](https://docs.stripe.com/connect/payment-methods)
- [multiple
configurations](https://docs.stripe.com/connect/multiple-payment-method-configurations)
- [Payment method
configurations](https://docs.stripe.com/payments/payment-method-configurations)
- [List payment method
configurations](https://docs.stripe.com/api/payment_method_configurations/list)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-method-settings)
- [register here](https://dashboard.stripe.com/register)
- [Connect integration guide](https://docs.stripe.com/connect/charges)