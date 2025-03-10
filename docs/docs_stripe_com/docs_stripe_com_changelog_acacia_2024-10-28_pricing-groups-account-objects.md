# Adds pricing groups to the Accounts API

## What’s new

Adds `groups` to `Account` objects, allowing you to place connected accounts in
[pricing
groups](https://docs.stripe.com/connect/platform-pricing-tools/pricing-groups)
and read their current pricing group membership.

## Impact

You can now assign connected accounts to specific pricing groups and retrieve
information about their current group memberships through the API. This change
provides more programmatic flexibility in managing pricing structures for
connected accounts after setting up the pricing groups using Connect’s [platform
pricing tools](https://docs.stripe.com/connect/platform-pricing-tools). Adding
accounts to a pricing groups allows for more tailored pricing strategies and
improved reporting on account categorizations.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsgroupsAdded[Account#create](https://docs.stripe.com/api/accounts/create)[Account#update](https://docs.stripe.com/api/accounts/update)[Account](https://docs.stripe.com/api/accounts/object)
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

## Links

- [pricing
groups](https://docs.stripe.com/connect/platform-pricing-tools/pricing-groups)
- [platform pricing
tools](https://docs.stripe.com/connect/platform-pricing-tools)
- [Account#create](https://docs.stripe.com/api/accounts/create)
- [Account#update](https://docs.stripe.com/api/accounts/update)
- [Account](https://docs.stripe.com/api/accounts/object)
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