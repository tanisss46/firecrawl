# Makes Issuing and Treasury embedded components generally available

## What’s new

The following embedded components are now generally available:

- [Issuing
card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card)
- [Issuing cards
list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list)
- [Financial
account](https://docs.stripe.com/connect/supported-embedded-components/financial-account)
- [Financial account
transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account)

These components allow you to deploy [embedded
finance](https://docs.stripe.com/baas/start-integration/integration-guides/embedded-finance)
services for your connected accounts, with minimal coding and configuration. You
can create and manage Issuing cards, manage your financial accounts, view
transactions, and more.

## Impact

To get started, follow our guide on [how to get started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components),
and then use the [Account Session
API](https://docs.stripe.com/api/account_sessions) to enable the components.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsfinancial_account_transactionsfinancial_accountissuing_cardissuing_cards_listAdded[AccountSession#create.components](https://docs.stripe.com/api/account_sessions/create#create_account_session-components)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2025-01-27.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Links

- [Issuing
card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card)
- [Issuing cards
list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list)
- [Financial
account](https://docs.stripe.com/connect/supported-embedded-components/financial-account)
- [embedded
finance](https://docs.stripe.com/baas/start-integration/integration-guides/embedded-finance)
- [how to get started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Account Session API](https://docs.stripe.com/api/account_sessions)
-
[AccountSession#create.components](https://docs.stripe.com/api/account_sessions/create#create_account_session-components)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)