# Adds Polish PLN currency support to Terminal tipping configuration

## What’s new

We’ve added the Polish PLN as a [supported
currency](https://docs.stripe.com/currencies) for Terminal’s [tipping
configuration](https://docs.stripe.com/terminal/features/collecting-tips/overview).

## Impact

Users in Poland can now [collect on-reader
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-reader) in
PLN.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsplnAdded[Terminal.Configuration#create.tipping](https://docs.stripe.com/api/terminal/configuration/create#create_configuration-tipping)[Terminal.Configuration#update.tipping](https://docs.stripe.com/api/terminal/configuration/update#update_configuration-tipping)[Terminal.Configuration.tipping](https://docs.stripe.com/api/terminal/configuration/object#terminal_configuration_object-tipping)
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

- [Adds a metadata field to the Vault and Forward
API](https://docs.stripe.com/changelog/acacia/2024-10-28/forwarding-api-metadata-field)
- [Supports domain registration for Amazon
Pay](https://docs.stripe.com/changelog/acacia/2024-10-28/amazon-pay-domain-registration)

## Links

- [supported currency](https://docs.stripe.com/currencies)
- [tipping
configuration](https://docs.stripe.com/terminal/features/collecting-tips/overview)
- [collect on-reader
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-reader)
-
[Terminal.Configuration#create.tipping](https://docs.stripe.com/api/terminal/configuration/create#create_configuration-tipping)
-
[Terminal.Configuration#update.tipping](https://docs.stripe.com/api/terminal/configuration/update#update_configuration-tipping)
-
[Terminal.Configuration.tipping](https://docs.stripe.com/api/terminal/configuration/object#terminal_configuration_object-tipping)
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
- [Adds a metadata field to the Vault and Forward
API](https://docs.stripe.com/changelog/acacia/2024-10-28/forwarding-api-metadata-field)
- [Supports domain registration for Amazon
Pay](https://docs.stripe.com/changelog/acacia/2024-10-28/amazon-pay-domain-registration)