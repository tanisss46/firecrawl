# Set a Stripe API version

## Follow these guidelines to make sure that API versions match throughout your Stripe integration.

Your account has a **default API version**, which defines how you call the API,
what functionality you have access to and what you’re guaranteed to get back as
part of the response. Webhook event objects are based on your default API
version, which might be different from the API version used by the SDK. To make
sure these versions match, we recommend [registering a webhook
endpoint](https://docs.stripe.com/webhooks#register-webhook) with the same [API
version](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-api_version)
used as the SDK. To find your version, see [View the API versions used by API
requests](https://docs.stripe.com/workbench/guides#view-api-versions).

## Versioning basics

Choose your SDK language to get started.

RubyPythonPHPJavaNodeGo.NET
### Setting the API version

The stripe-ruby library allows you to set the API version globally or on a
per-request basis. If you don’t set an API version, recent versions of
stripe-ruby use the API version that was latest at the time your version of
stripe-ruby was released. Versions of stripe-ruby before
[v9](https://github.com/stripe/stripe-ruby/blob/master/CHANGELOG.md#900---2023-08-16)
use your account’s default API version.

To set the API version **globally** with the SDK, assign the version to the
`Stripe.api_version` property:

```
require 'stripe'
Stripe.api_key = sk_test_BQokikJOvBiI2HlWgH4olfQ2
Stripe.api_version = '2025-02-24.acacia'
```

Or set the version per-request:

```
require 'stripe'
intent = Stripe::PaymentIntent.retrieve(
 'pi_1DlIVK2eZvKYlo2CW4yj5l2C',
 {
 stripe_version: '2025-02-24.acacia',
 }
)
intent.capture
```

#### Note

When you override the version globally or per-request, the API response objects
are also returned in that version.

### Upgrading your API version

Before upgrading [your API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api), carefully
review the following resources:

- [Stripe API changelog](https://docs.stripe.com/upgrades#api-versions)
- [View the API versions used by API
requests](https://docs.stripe.com/workbench/guides#view-api-versions)

You can upgrade your account’s default API version in
[Workbench](https://dashboard.stripe.com/workbench/overview). Update your code
to use the latest version of the Ruby SDK and set the new API version when
making your calls.

## See also

Stripe SDKs follow their own versioning policy. See the link below to learn
more.

- [Stripe versioning and support
policies](https://docs.stripe.com/sdks/versioning)

## Links

- [registering a webhook
endpoint](https://docs.stripe.com/webhooks#register-webhook)
- [API
version](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-api_version)
- [View the API versions used by API
requests](https://docs.stripe.com/workbench/guides#view-api-versions)
-
[v9](https://github.com/stripe/stripe-ruby/blob/master/CHANGELOG.md#900---2023-08-16)
- [your API version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api)
- [Stripe API changelog](https://docs.stripe.com/upgrades#api-versions)
- [Workbench](https://dashboard.stripe.com/workbench/overview)
- [Stripe versioning and support
policies](https://docs.stripe.com/sdks/versioning)