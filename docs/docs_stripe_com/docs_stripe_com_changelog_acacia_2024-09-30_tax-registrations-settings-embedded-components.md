# Adds support for tax settings and registrations for Embedded Components

## What’s new

Adds `tax_settings` and `tax_registrations` parameters to the list of supported
[embedded
components](https://docs.stripe.com/connect/supported-embedded-components) in
[Account Sessions](https://docs.stripe.com/api/account_sessions).

Addedcomponents.tax_settingsobject
Configuration for the tax settings embedded component.

Addedcomponents.tax_registrationsobject
Configuration for the tax registrations embedded component.

## Impact

With this change, Connect platforms can use the [Tax
Settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings)
and [Tax
Registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)
[embedded
components](https://docs.stripe.com/connect/supported-embedded-components). You
can use these to whitelabel [Stripe Tax](https://docs.stripe.com/tax)
integrations for your connected accounts without building custom UIs or
redirecting them to the Stripe Dashboard.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointstax_registrationstax_settingsAdded[AccountSession#create.components](https://docs.stripe.com/api/account_sessions/create#create_account_session-components)[AccountSession.components](https://docs.stripe.com/api/account_sessions/object#account_session_object-components)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
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

## Related changes

- [Adds support for posting time on tax transaction
creation](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-posting-time-on-creation)
- [Adds new method to retrieve a Tax
Calculation](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)
- [Adds support for specifying US state sales tax elections while creating tax
registrations](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)

## Links

- [embedded
components](https://docs.stripe.com/connect/supported-embedded-components)
- [Account Sessions](https://docs.stripe.com/api/account_sessions)
- [Tax
Settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings)
- [Tax
Registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)
- [Stripe Tax](https://docs.stripe.com/tax)
-
[AccountSession#create.components](https://docs.stripe.com/api/account_sessions/create#create_account_session-components)
-
[AccountSession.components](https://docs.stripe.com/api/account_sessions/object#account_session_object-components)
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
- [Adds support for posting time on tax transaction
creation](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-posting-time-on-creation)
- [Adds new method to retrieve a Tax
Calculation](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)
- [Adds support for specifying US state sales tax elections while creating tax
registrations](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)