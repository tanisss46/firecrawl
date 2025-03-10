# Adds support for specifying US state sales tax elections while creating tax registrations

## What’s new

Adds the `state_sales_tax` field to the
`Tax.Registration#create.country_options.us` and
`Tax.Registration.country_options.us` objects.

## Impact

This update allows you to specify US state sales tax elections using the API
when creating tax registrations. This aligns with the API functionality in the
Stripe Dashboard, providing more flexibility in managing tax registrations for
states such as TX, AL, and PA.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsstate_sales_taxAdded[Tax.Registration#create.country_options.us](https://docs.stripe.com/api/tax/registrations/create#tax_registration_create-country_options-us)[Tax.Registration.country_options.us](https://docs.stripe.com/api/tax/registrations/object#tax_registration_object-country_options-us)
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
- [Adds new method to retrieve a Tax
Calculation](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)

## Links

-
[Tax.Registration#create.country_options.us](https://docs.stripe.com/api/tax/registrations/create#tax_registration_create-country_options-us)
-
[Tax.Registration.country_options.us](https://docs.stripe.com/api/tax/registrations/object#tax_registration_object-country_options-us)
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
- [Adds new method to retrieve a Tax
Calculation](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)