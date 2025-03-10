# Migrate a plugin to Stripe Apps or Stripe Connect

## Learn about your migration options and decide how to migrate your plugin.

Use this guide to migrate your third-party integration that requires Stripe
users to authenticate with their secret API key (also known as a plugin) to
Stripe Apps or Stripe Connect.

Previously, Stripe allowed plugins to request the standard API keys of a user to
integrate with their products. Starting September 30, 2024, all plugin
developers must use secure authentication methods (OAuth 2.0, restricted API
keys, Stripe Connect) to protect users against fraud. All new and existing
plugin developers must switch to one of these secure authorization methods
supported by Stripe.

If your integration already uses [Stripe
Apps](https://docs.stripe.com/stripe-apps) or [Stripe
Connect](https://docs.stripe.com/connect/oauth-reference), this doesn’t apply to
you or your users.

## Choose your migration path

Stripe offers multiple solutions for developers migrating plugins. Explore each
solution:

Integration typeSuitable forDesigned for[Stripe
Connect](https://docs.stripe.com/stripe-apps/plugins/decide-migration#migrate-to-connect)Best
for integrations that are centralized platforms or marketplacesDesigned for
integrations onboarding new merchants, embedding payments, and managing money
movement[Stripe
Apps](https://docs.stripe.com/stripe-apps/plugins/decide-migration#migrate-to-apps)Best
for integrations that want to integrate Stripe in third-party tools and
servicesDesigned for adding enhanced functionality for existing Stripe
merchants[Manual set up of restricted API keys and
webhooks](https://docs.stripe.com/stripe-apps/plugins/decide-migration#migrate-manual-api-keys)Only
available if your integration requires custom functionality that isn’t supported
by Stripe Connect or Stripe AppsDesigned for users who each must manually create
restricted API keys and webhooks
## Pre-migration decision checklist

Review the following checklist to help you decide on the best migration path for
your integration and users:

- If you need to onboard new businesses
Onboarding new users who might not have existing Stripe accounts often requires
creating a Stripe account for the first time just to use your service. If yes,
consider Stripe Connect, as the onboarding flow allows users to create Stripe
accounts directly during onboarding.
- If you want to make your integration available to users of other platforms 
If you make your integration available for other platforms, consider Stripe
Apps. You can install Stripe Apps on most Stripe accounts, regardless of their
connection to other platforms. This allows you to make your integration
available to a larger base.
- If you have a centralized service for your plugin
If you have a centralized service where your users have their own accounts,
consider Stripe Connect or Stripe Apps, and use platform or OAuth 2.0
authentication. Using Stripe Connect or Stripe Apps ensures that your users
don’t need to copy and paste API keys, which significantly enhances overall
security and streamlines user onboarding.
- If your users self-host their back ends for your integration
If customers self-host your integration, Stripe Apps using the restricted API
key authentication method is likely the best fit. It doesn’t require you to
store your secret key on untrusted servers, which is required for Stripe Connect
or Stripe Apps with platform authentication.

OAuth 2.0 is an option but requires significant additional work, including
hosting a central back-end server where your users create accounts, store the
URLs of their self-hosted back ends, and proxy OAuth tokens to those back ends.
- If you want to receive webhook events on your own endpoints
If you receive webhook events on your own endpoints, consider Stripe Connect or
Stripe Apps, using the platform or OAuth 2.0 authentication methods to set up a
central webhook configuration. Doing so allows you to receive webhook events for
all of your connected account users.
- If your users receive webhook endpoints at their own unique endpoints
If users receive webhook endpoints at their own unique endpoints, instruct them
on how to configure these endpoints manually, which is common with self-hosted
back ends. If you have a special use case that requires managing custom webhook
endpoints for your users through the `webhook_write` API permission, contact
[Stripe Support](https://support.stripe.com/contact/email).
- If your service uses the connected accounts of other platforms
Using the connected accounts of other platforms is uncommon—but in some cases,
plugins are designed to use the transitive access of a platform’s secret API key
to make API calls on behalf of the platform’s connected accounts. Currently, the
only supported option is to have your users manually create restricted API keys.
When creating the key, the user must check the appropriate boxes to grant
permissions on their connected accounts.
- If your app requires access to any gated Stripe APIs or features

## Migrating to Stripe Connect

Stripe Connect is a solution for centralized platforms. To use Connect, you need
to host a web service to securely store your API key and manage connected
accounts.

Using your platform API key requires that all API requests to Stripe originate
from your servers, use your API key for authentication, and use the
`Stripe-Account` header to indicate the connected account you’re acting on
behalf of. Instead of OAuth 2.0, use the `/v1/accounts`
API](/connect/oauth-standard-accounts) to securely retrieve access tokens for
each connected account. Your servers or your customers’ servers can then make
API requests to Stripe using those tokens.

Stripe businesses can only be connected to one Connect platform at a time.
Connect allows you to onboard new businesses directly to your platform, but
businesses with existing Stripe accounts who want to use your platform need to
create new accounts, which might cause extra work your users.

To learn more about migrating from a plugin to Connect, see [Build a multi-party
integration with Connect](https://docs.stripe.com/connect/how-connect-works).

## Migrating to Stripe Apps

Stripe Apps is a platform for developers to create integrations that extend or
enhance Stripe’s functionality for businesses and their users. These
integrations can directly customize Stripe’s behaviors or connect third-party
tools and services to Stripe.

Stripe Apps also offers an authorization framework for securely accessing Stripe
on behalf of businesses. Additionally, Stripe Apps includes features such as [UI
extensions](https://docs.stripe.com/stripe-apps/build-ui), which can improve the
functionality and value of your plugin.

Stripe Apps offers three authentication methods to fit different use cases:

- **Platform**: Designed for Stripe-native integrations that operate as a
centralized service, such as a SaaS platform. API requests require the
developer’s API key and the Stripe Account header.
- **OAuth 2.0**: Uses the industry-standard OAuth 2.0 protocol for
service-to-service user authentication. This method is ideal for integrations
already using OAuth (previously known as [Connect
Extensions](https://docs.stripe.com/stripe-apps/migrate-extension)), and
provides added benefits such as enhanced management, increased visibility,
analytics, and so on through the Stripe Apps platform.
- **Restricted API keys (RAK)**: Automatically generates restricted API keys for
each app a user installs. Each app gets a unique API key with only the
permissions it needs. Users must still manually copy and paste this key into
your integration. While this method boosts security, it adds extra steps for
user onboarding.

### Compare authentication types for Stripe Apps

Before you migrate your plugin to Stripe Apps, compare the three authentication
methods:

AuthenticationBenefits Tradeoffs Platform default- Click to install for
businesses.
- Enhanced security versus collecting secret API keys for businesses.
- Ability to centrally manage the configuration of webhooks to receive events
from connected accounts. Minimal data storage requirements. Doesn’t require
merchants to have an account with your service (optional).
- Only need to keep track of one API key.
- Access to gated features needs to be granted only once for your account.
- Must have a centralized back end to store your API key and make API calls.
- Not suitable for self-hosted plugins.
- Requires code changes if your plugin uses secret API keys or OAuth 2.0 today.
OAuth 2.0 recommended- Industry standard.
- Enhanced security versus collecting the secret API keys from businesses.
- Streamlined installation and onboarding flow for businesses.
- Centrally managed configuration of webhooks to receive events from connected
accounts.
- Few or no code changes if using OAuth today.
- Support for self-hosted plugins with additional developer effort.
- Access to gated features needs to be granted only once for your account.
- Requires a centralized back end to begin the OAuth flow and receive OAuth
tokens at the end.
- You must keep track of accounts as part of your service.
- You must store OAuth access and refresh tokens for each account.
- Requires code changes if your plugin uses secret API keys today.
RAK- Replacement for existing secret API keys.
- Enhanced security versus collecting the secret API keys from businesses.
- Use with self-hosted back ends.
- Doesn’t require businesses to have an account with your service (optional).
- You must manually onboard businesses to use your integration (copy and paste
keys).
- No support for centrally managing webhook endpoints to receive events from
accounts that installed your app.
- Users must configure their own webhooks, if needed.
- Access to gated features requires each account that installs your app to be
granted access separately.

We recommend platform or OAuth 2.0 authentication because they offer better
security and a streamlined onboarding process for your users.

For step-by-step instructions on migrating plugins to Stripe Apps, see:

- [Migrate a plugin to an OAuth
app](https://docs.stripe.com/stripe-apps/plugins/oauth)
- [Migrate a plugin to a RAK
app](https://docs.stripe.com/stripe-apps/plugins/rak)

## Migrating to manual setup of restricted API keys and webhooks

If neither Stripe Connect nor Stripe Apps meets your needs, users can manually
set up their integration with your service.

To migrate and comply with Stripe’s security requirements, you must:

- **Document the setup**: Provide instructions for businesses to configure a
restricted API key that only has the needed permissions.
- **Validate API Keys**: Make sure businesses give you restricted API keys that
start with the prefix with `rk_`, not `sk_`.
- (Optional) **Document the webhook setup**: Guide businesses on setting up
webhook endpoints to send data to the correct address.

#### Note

This authentication method introduces manual onboarding steps for businesses and
lacks the benefits of Stripe Connect and Stripe Apps.

## See also

- [Migrate a plugin to an OAuth
app](https://docs.stripe.com/stripe-apps/plugins/oauth)
- [Migrate a plugin to a RAK
app](https://docs.stripe.com/stripe-apps/plugins/rak)
- [Sample apps](https://docs.stripe.com/stripe-apps/sample-apps)

## Links

- [Stripe Apps](https://docs.stripe.com/stripe-apps)
- [Stripe Connect](https://docs.stripe.com/connect/oauth-reference)
- [Stripe
Connect](https://docs.stripe.com/stripe-apps/plugins/decide-migration#migrate-to-connect)
- [Stripe
Apps](https://docs.stripe.com/stripe-apps/plugins/decide-migration#migrate-to-apps)
- [Manual set up of restricted API keys and
webhooks](https://docs.stripe.com/stripe-apps/plugins/decide-migration#migrate-manual-api-keys)
- [Stripe Support](https://support.stripe.com/contact/email)
- [Build a multi-party integration with
Connect](https://docs.stripe.com/connect/how-connect-works)
- [UI extensions](https://docs.stripe.com/stripe-apps/build-ui)
- [Connect Extensions](https://docs.stripe.com/stripe-apps/migrate-extension)
- [Migrate a plugin to an OAuth
app](https://docs.stripe.com/stripe-apps/plugins/oauth)
- [Migrate a plugin to a RAK
app](https://docs.stripe.com/stripe-apps/plugins/rak)
- [Sample apps](https://docs.stripe.com/stripe-apps/sample-apps)