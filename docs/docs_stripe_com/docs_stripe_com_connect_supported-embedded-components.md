# Supported Connect embedded components

## Learn about current and upcoming embedded components.

Add Connect embedded components to your page as HTML elements or as [React
components](https://github.com/stripe/react-connect-js).

## Available components

[Account
management](https://docs.stripe.com/connect/supported-embedded-components/account-management)Show
account details and allow them to be edited.[Account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)Show
a localized onboarding form that validates
data.[Balances](https://docs.stripe.com/connect/supported-embedded-components/balances)Show
balance information and allow your connected accounts to perform
payouts.[Documents](https://docs.stripe.com/connect/supported-embedded-components/documents)Show
a list of documents available for download.[Financial
account](https://docs.stripe.com/connect/supported-embedded-components/financial-account)Show
details of a financial account.[Financial account
transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions)Show
a table of all transactions for a financial account.[Issuing
card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card)Show
an individual issued card.[Issuing cards
list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list)Show
a table of all issued cards.[Notification
banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)Show
a banner that lists required actions for risk interventions and onboarding
requirements.[Payments](https://docs.stripe.com/connect/supported-embedded-components/payments)Show
a list of payments with export, refund, and dispute capabilities.[Payment
details](https://docs.stripe.com/connect/supported-embedded-components/payment-details)Show
details of a given payment and allow users to manage disputes and perform
refunds.[Payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts)Show
payout information and allow your users to perform payouts.[Payouts
list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list)Show
a filterable list of payouts.[Tax
registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)Show
and manage tax registrations from connected accounts.[Tax
settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings)Allow
connected accounts to set up Stripe Tax.
## Preview components

When using private preview components, use beta versions of the Stripe SDK, as
well as beta versions of the
[@stripe/connect-js](https://github.com/stripe/connect-js) and
[@stripe/react-connect-js](https://github.com/stripe/react-connect-js) SDKs.

To create an account session with private preview components, use the Stripe
beta SDKs:

- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks) `>=13.4.0-beta.4`
- [Python](https://github.com/stripe/stripe-python/#beta-sdks) `>=11.5.0b3`
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks) `>=16.5.0-beta.3`
- [Node](https://github.com/stripe/stripe-node/#beta-sdks) `>=17.6.0-beta.3`
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks) `>=47.3.0-beta.3`
- [Java](https://github.com/stripe/stripe-java#beta-sdks) `>=28.3.0-beta.3`
- [Go](https://github.com/stripe/stripe-go#beta-sdks) `>=81.3.0-beta.3`

Use the client-side libraries for rendering the private preview components:

npmGitHub
Install the library:

`npm install --save @stripe/connect-js@preview`
If you’re using React in your application:

`npm install --save @stripe/react-connect-js@preview`
### Available preview components

[App
install](https://docs.stripe.com/connect/supported-embedded-components/app-install)Show
a button to install an App.[App
viewport](https://docs.stripe.com/connect/supported-embedded-components/app-viewport)Show
a view from an installed App.[Capital financing
application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)Show
an end-to-end application flow for Capital financing.[Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)Show
promotional content about a connected account's Capital financing offer and
launch a Capital application.[Capital
financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing)Allow
a connected account to view and manage their active Capital financing.[Payment
method
settings](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings)Show
a list of payment methods that connected accounts can manage and
accept.[Reporting
chart](https://docs.stripe.com/connect/supported-embedded-components/reporting-chart)Show
charts to your connected accounts.
## Integration guides

[Accounting integrations](https://docs.stripe.com/stripe-apps/embedded-apps)Show
third-party accounting software integrations.[Fully embedded Connect platform
integration](https://docs.stripe.com/connect/build-full-embedded-integration)Allow
your connected accounts to access Stripe Connect features from your own website,
without a Stripe hosted dashboard.[Embedded
finance](https://docs.stripe.com/baas/start-integration/integration-guides/embedded-finance?integration=embedded)Use
prebuilt UI components to embed Issuing and Treasury into your website.
## Migrate from the v1 to v2 beta

- Update your client library.-
[Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks) `>=13.4.0-beta.4`
- [Python](https://github.com/stripe/stripe-python/#beta-sdks) `>=11.5.0b3`
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks) `>=16.5.0-beta.3`
- [Node](https://github.com/stripe/stripe-node/#beta-sdks) `>=17.6.0-beta.3`
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks) `>=47.3.0-beta.3`
- [Java](https://github.com/stripe/stripe-java#beta-sdks) `>=28.3.0-beta.3`
- [Go](https://github.com/stripe/stripe-go#beta-sdks) `>=81.3.0-beta.3`
- Update the beta header used from `embedded_connect_beta=v1` to
`embedded_connect_beta=v2`.
- Specify the list of `components` to enable as a parameter when creating an
[Account Session](https://docs.stripe.com/api/account_sessions/create).

## Migrate from v2 beta to GA

If you’re using a beta component that’s now generally available, follow these
steps:

- Update your client library.- [Ruby](https://github.com/stripe/stripe-ruby)
`>=13.4.1`
- [Python](https://github.com/stripe/stripe-python) `>=11.5.0`
- [PHP](https://github.com/stripe/stripe-php) `>=16.5.0`
- [Node](https://github.com/stripe/stripe-node) `>=17.6.0`
- [.NET](https://github.com/stripe/stripe-dotnet) `>=47.3.0`
- [Java](https://github.com/stripe/stripe-java) `>=28.3.0`
- [Go](https://github.com/stripe/stripe-go) `>=81.3.0`
- Remove the `embedded_connect_beta` header.
- Use the GA releases of the `@stripe/connect-js` and `@stripe/react-connect-js`
npm packages.

## Links

- [React components](https://github.com/stripe/react-connect-js)
- [Account
management](https://docs.stripe.com/connect/supported-embedded-components/account-management)
- [Account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
-
[Balances](https://docs.stripe.com/connect/supported-embedded-components/balances)
-
[Documents](https://docs.stripe.com/connect/supported-embedded-components/documents)
- [Financial
account](https://docs.stripe.com/connect/supported-embedded-components/financial-account)
- [Financial account
transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions)
- [Issuing
card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card)
- [Issuing cards
list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list)
- [Notification
banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
-
[Payments](https://docs.stripe.com/connect/supported-embedded-components/payments)
- [Payment
details](https://docs.stripe.com/connect/supported-embedded-components/payment-details)
-
[Payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts)
- [Payouts
list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list)
- [Tax
registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)
- [Tax
settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings)
- [@stripe/connect-js](https://github.com/stripe/connect-js)
- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks)
- [Python](https://github.com/stripe/stripe-python/#beta-sdks)
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks)
- [Node](https://github.com/stripe/stripe-node/#beta-sdks)
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks)
- [Java](https://github.com/stripe/stripe-java#beta-sdks)
- [Go](https://github.com/stripe/stripe-go#beta-sdks)
- [App
install](https://docs.stripe.com/connect/supported-embedded-components/app-install)
- [App
viewport](https://docs.stripe.com/connect/supported-embedded-components/app-viewport)
- [Capital financing
application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)
- [Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
- [Capital
financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing)
- [Payment method
settings](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings)
- [Reporting
chart](https://docs.stripe.com/connect/supported-embedded-components/reporting-chart)
- [Accounting integrations](https://docs.stripe.com/stripe-apps/embedded-apps)
- [Fully embedded Connect platform
integration](https://docs.stripe.com/connect/build-full-embedded-integration)
- [Embedded
finance](https://docs.stripe.com/baas/start-integration/integration-guides/embedded-finance?integration=embedded)
- [Account Session](https://docs.stripe.com/api/account_sessions/create)
- [Ruby](https://github.com/stripe/stripe-ruby)
- [Python](https://github.com/stripe/stripe-python)
- [PHP](https://github.com/stripe/stripe-php)
- [Node](https://github.com/stripe/stripe-node)
- [.NET](https://github.com/stripe/stripe-dotnet)
- [Java](https://github.com/stripe/stripe-java)
- [Go](https://github.com/stripe/stripe-go)