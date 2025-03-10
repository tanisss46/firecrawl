# Adds support for new countries to the Tax Registration API

## What’s new

Adds support for Belarus, Costa Rica, Ecuador, Moldova, Morocco, Russia, Serbia,
Tanzania, Uzbekistan in Tax Registration API.

## Impact

This change expands the geographic coverage of the [Tax
Registration](https://docs.stripe.com/api/tax/registrations) resource to include
nine additional countries. It allows businesses operating in or selling to these
countries to register and manage their tax information through Stripe.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsbycrecmamdrsrutzuzAdded[Tax.Registration#create.country_options](https://docs.stripe.com/api/tax/registrations/create#tax_registration_create-country_options)[Tax.Registration.country_options](https://docs.stripe.com/api/tax/registrations/object#tax_registration_object-country_options)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
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

- [Adds support for tax ID types in several new
countries](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-ids)
- [Adds support for collecting retail delivery
fees](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee)
- [Adds option to automatically validate customer tax location during an
update](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto)

## Links

- [Tax Registration](https://docs.stripe.com/api/tax/registrations)
-
[Tax.Registration#create.country_options](https://docs.stripe.com/api/tax/registrations/create#tax_registration_create-country_options)
-
[Tax.Registration.country_options](https://docs.stripe.com/api/tax/registrations/object#tax_registration_object-country_options)
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
- [Adds support for tax ID types in several new
countries](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-ids)
- [Adds support for collecting retail delivery
fees](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee)
- [Adds option to automatically validate customer tax location during an
update](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto)