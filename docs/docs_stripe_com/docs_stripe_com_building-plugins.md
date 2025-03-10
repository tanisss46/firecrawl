# Legacy pluginsDeprecated

## Ensure your legacy plugin meets Stripe's requirements.

#### Deprecated

The plugin integration pattern is deprecated. This means you can no longer
request secret API keys from users.

Stripe Apps is the new method for authenticating users and includes support for
both restricted API keys and OAuth 2.0. For more information, see the [migration
docs](https://docs.stripe.com/stripe-apps/plugins/decide-migration).

## What is a plugin?

Plugins are any integration between a third-party solution and Stripe that
requires a user to authenticate with their secret API keys. A plugin typically
interacts with Stripe APIs either by making API calls or responding to Stripe
API events on behalf of its users. Plugins often run code that allows Stripe to
interact with other software, such as accepting payments on WordPress. They can
also take other forms, like open-source libraries or website builders.

## Best practices for legacy plugins

#### Note

Join the [Stripe Insiders](https://insiders.stripe.dev/c/stripe-plugins/15)
community to stay updated on the latest product changes affecting your
integration.

Follow these best practices to help your users safely process on Stripe’s
platform without disruption if our API upgrades or changes. If you have
questions, contact us at [plugins@stripe.com](mailto:plugins@stripe.com).

- Register your plugin by creating a Stripe account or using an existing one
- [Identify your
plugin](https://docs.stripe.com/building-plugins#identify-plugin) using
`setAppInfo` and `registerAppInfo` so we can alert you to any potential issues
we notice
- Set [Stripe’s API
version](https://docs.stripe.com/building-plugins#set-api-version) in your
plugin to avoid potentially breaking changes for your users
- Use [client-side
tokenization](https://docs.stripe.com/building-plugins#tokenization) to securely
collect payment details in the browser

You can also take a few steps to improve the quality of your connector:

- Add the [Express Checkout
Element](https://docs.stripe.com/building-plugins#express-checkout-element) to
offer multiple one-click payment buttons to your customers, including [Apple
Pay](https://docs.stripe.com/apple-pay), [Google
Pay](https://docs.stripe.com/google-pay),
[Link](https://docs.stripe.com/payments/link), and
[PayPal](https://docs.stripe.com/payments/paypal)
- Enable [multiple payment
methods](https://docs.stripe.com/building-plugins#apms) beyond credit cards to
support international users
- Verify your users [have HTTPS
enabled](https://docs.stripe.com/building-plugins#https) to improve their
security
- Subscribe to our [mailing
list](https://docs.stripe.com/building-plugins#subscribe) to keep up to speed
with changes to Stripe’s API

#### Note

[Become a Stripe Partner](https://stripe.com/partner-program) to reach
businesses on Stripe who are looking to add capabilities to their platforms.

## Identifying your plugin

Provide identifying information so that we can contact you if there’s an issue
with your connector or critical update to the API.

### Backend API calls

If you use the APIs to create server-side requests, use `setAppInfo` with a hash
containing the following options:

- `name` (required): your plugin’s name
- `partner_id` (required for [Stripe Verified
Partners](https://stripe.com/partner-program), optional otherwise): your Partner
ID from the [Partners](https://dashboard.stripe.com/partners/settings) section
of the Dashboard
- `version` (optional): your plugin’s version
- `url` (optional): the URL for your plugin’s website with your contact details

```
Stripe.set_app_info(
 'MyStripePlugin',
 partner_id: '{{PARTNER_ID}}', # Used by Stripe to identify your connector
 version: '1.2.34',
 url: 'https://example.com'
)
```

#### Caution

If your connector is designed for a particular platform, include that platform
in the `name` field (for example, **WordPress MyStripePlugin** or **WooCommerce
MyStripePlugin**).

If you’re building a connector and not using one of our official libraries, set
the value of the User-Agent header on requests made to the Stripe API as
`name/version (url)`.

The following is an example:

```
User-Agent: WordPress MyStripePlugin/1.2.34 (https://example.com)

```

### Client side / Stripe.js

For frontend libraries that use Stripe.js, use `registerAppInfo` with the same
options as `setAppInfo` above. For example, using JavaScript:

```
stripe.registerAppInfo({
 name: "MyOSSLibrary",
 partner_id: '{{PARTNER_ID}}', // Used by Stripe to identify your connector
 version: "1.2.34",
 url: "https://example.com",
});
```

## Setting the API version

Your plugin should use the `setApiVersion` function, which will set the
`Stripe-Version` HTTP header on all requests. Your users will use their own API
keys to access Stripe, but this header will be included with every request. We
recommend that you use the most recently published version of the API. The
current API version and details on our [versioning
policy](https://docs.stripe.com/api#versioning) can be found in the API
reference.

```
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
Stripe.api_version = '2022-08-01'
```

New Stripe users automatically default to the latest version of the API. This
header ensures that your connector is pinned to a specific API version, which
keeps the occasional [backward-incompatible
change](https://docs.stripe.com/upgrades#what-changes-does-stripe-consider-to-be-backward-compatible)
from breaking your connector’s functionality.

Users can upgrade their own API version through the [Stripe
Dashboard](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api). If your
connector relies on [webhook](https://docs.stripe.com/webhooks) events, their
data format and structure depend on the user’s account API version. You should
instruct your users to set the version in their Dashboard to match your plugin.

#### Caution

**API versions can’t be downgraded.** You should regularly release new versions
of your connector to correctly handle any changes to JSON responses.

## Subscribing to our mailing list for updates

We regularly release new versions of the Stripe API that bring new features and
bug fixes. You can subscribe to the
[api-announce](https://groups.google.com/a/lists.stripe.com/forum/#!forum/api-announce)
mailing list to be notified of updates that might affect users of your
connector.

## Securely collecting payment details

Stripe users are subject to [PCI
compliance](https://stripe.com/guides/pci-compliance), which specifies how
credit card data should be securely stored, processed, and transmitted. Their
businesses could face stiff penalties for noncompliance or potential breaches,
so it’s important to help them safely process on Stripe.

Since your connector will make API calls on behalf of a Stripe user, you must
transmit credit card data securely using *client-side tokenization*.
[Customers](https://docs.stripe.com/api/customers) submit their personal
information through their web browser or mobile app directly to Stripe, and in
exchange a simple token will be sent to the Stripe user. This allows your users
to securely collect card details without sensitive data ever touching their
server.

If your connector includes a client-side payment form in the browser, we
recommend that you use either [Stripe.js and
Elements](https://docs.stripe.com/payments/elements) or
[Checkout](https://docs.stripe.com/payments/checkout):

- Elements provides prebuilt UI components and complete control over the look
and feel of payment forms
- Checkout provides a complete checkout experience and can be quickly added to a
Stripe user’s website

Both of these options provide client-side tokenization.

If your plugin only operates in a backend environment, please include a note in
your connector’s documentation asking users to tokenize payment details using
Elements or Checkout. Tokenization helps Stripe users process as safely as
possible on our platform.

## Add the Express Checkout Element

The [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element) gives you a
single integration for accepting payments through one-click payment buttons,
including [Apple Pay](https://docs.stripe.com/apple-pay), [Google
Pay](https://docs.stripe.com/google-pay),
[Link](https://docs.stripe.com/payments/link), or
[PayPal](https://docs.stripe.com/payments/paypal).

The Express Checkout Element allows you to display multiple buttons at the same
time. Customers see different payment buttons depending on what their device and
browser combination supports.

## Enabling multiple payment methods

Stripe supports multiple payment methods, aside from credit cards. We’ve
published a [guide to payment
methods](https://stripe.com/payments/payment-methods-guide) that introduces
terminology, key considerations, and how we support each method on our platform.

The [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
enables your users to collect payments using additional payment methods (for
example, Alipay, iDEAL, Sofort). You can add these [payment
methods](https://docs.stripe.com/payments/payment-methods#supported-payment-methods)
using one integration path.

## Verifying that HTTPS is enabled

If your plugin presents a payment form in a web browser, it should check if the
form is being served over HTTPS. We require our users to enable HTTPS: you
should present a clear error to your user if they’re not properly secured.

Here are a few examples to verify whether your users have HTTPS enabled:

```
# This example uses Sinatra, but the `request` object is provided by Rack
require 'sinatra'

get '/' do
 if !request.https?
 # Present an error to the user
 end
 # ...
end
```

If your connector has a front-end component, check whether HTTPS is being used
from the browser. For example, using JavaScript:

```
// This example checks for HTTPS from the browser
if (window.location.protocol !== "https:") {
 // Present an error to the user
}
```

## Links

- [migration docs](https://docs.stripe.com/stripe-apps/plugins/decide-migration)
- [Stripe Insiders](https://insiders.stripe.dev/c/stripe-plugins/15)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [Link](https://docs.stripe.com/payments/link)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Become a Stripe Partner](https://stripe.com/partner-program)
- [Partners](https://dashboard.stripe.com/partners/settings)
- [https://example.com](https://example.com)
- [versioning policy](https://docs.stripe.com/api#versioning)
- [backward-incompatible
change](https://docs.stripe.com/upgrades#what-changes-does-stripe-consider-to-be-backward-compatible)
- [Stripe Dashboard](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api)
- [webhook](https://docs.stripe.com/webhooks)
-
[api-announce](https://groups.google.com/a/lists.stripe.com/forum/#!forum/api-announce)
- [PCI compliance](https://stripe.com/guides/pci-compliance)
- [Customers](https://docs.stripe.com/api/customers)
- [Stripe.js and Elements](https://docs.stripe.com/payments/elements)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
- [payment
methods](https://docs.stripe.com/payments/payment-methods#supported-payment-methods)