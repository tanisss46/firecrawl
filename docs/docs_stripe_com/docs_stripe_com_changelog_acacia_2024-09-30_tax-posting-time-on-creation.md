# Adds support for posting time on tax transaction creation

## What’s new

Lets you specify and retrieve the posting time when creating a tax transaction.

Addedposted_atnullable object
The Unix timestamp representing when the tax liability is assumed or reduced.

## Impact

This improves your ability to accurately record liability for tax reporting
within correct periods.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsposted_atAdded[Tax.Transaction#create_from_calculation](https://docs.stripe.com/api/tax/transactions/create_from_calculation)[Tax.Transaction](https://docs.stripe.com/api/tax/transactions/object)
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

- [Adds support for tax settings and registrations for Embedded
Components](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-registrations-settings-embedded-components)
- [Adds new method to retrieve a Tax
Calculation](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)
- [Adds support for specifying US state sales tax elections while creating tax
registrations](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)

## Links

-
[Tax.Transaction#create_from_calculation](https://docs.stripe.com/api/tax/transactions/create_from_calculation)
- [Tax.Transaction](https://docs.stripe.com/api/tax/transactions/object)
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
- [Adds support for tax settings and registrations for Embedded
Components](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-registrations-settings-embedded-components)
- [Adds new method to retrieve a Tax
Calculation](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)
- [Adds support for specifying US state sales tax elections while creating tax
registrations](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)