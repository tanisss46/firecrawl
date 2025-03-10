# Adds new method to retrieve a Tax Calculation

## What’s new

Adds a method to retrieve [Tax
Calculations](https://docs.stripe.com/api/tax/calculations). You can retrieve
Tax Calculations by using the Tax Calculation’s
[ID](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-id).
Tax calculations expire after 90 days and you can’t access them after that.
Learn more about [calculating
taxes](https://docs.stripe.com/tax/custom#calculate-tax).

## Impact

Provides access to and management of tax-related data, ensuring that you can
reference and verify previously created calculations.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NET
 Endpoint

ChangeResourceretrieveAdded[Tax.Calculation](https://docs.stripe.com/api/tax/calculations/object)
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
- [Adds support for tax settings and registrations for Embedded
Components](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-registrations-settings-embedded-components)
- [Adds support for specifying US state sales tax elections while creating tax
registrations](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)

## Links

- [Tax Calculations](https://docs.stripe.com/api/tax/calculations)
-
[ID](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-id)
- [calculating taxes](https://docs.stripe.com/tax/custom#calculate-tax)
- [Tax.Calculation](https://docs.stripe.com/api/tax/calculations/object)
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
- [Adds support for tax settings and registrations for Embedded
Components](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-registrations-settings-embedded-components)
- [Adds support for specifying US state sales tax elections while creating tax
registrations](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)