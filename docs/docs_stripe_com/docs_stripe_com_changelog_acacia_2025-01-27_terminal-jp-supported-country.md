# Adds support for collecting tips in JPY currency to Terminal

## What’s new

We added the Japanese JPY as a [supported
currency](https://docs.stripe.com/currencies) to the Terminal [tipping
configuration](https://docs.stripe.com/terminal/features/collecting-tips/overview).
You can set this attrubute when you
[create](https://docs.stripe.com/api/terminal/configuration/create) or
[update](https://docs.stripe.com/api/terminal/configuration/update) the Terminal
[Configuration](https://docs.stripe.com/api/terminal/configuration).

## Impact

Users in Japan can now [collect on-reader
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-reader) in
the JPY currency.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsjpyAdded[Terminal.Configuration#create.tipping](https://docs.stripe.com/api/terminal/configuration/create#create_configuration-tipping)[Terminal.Configuration#update.tipping](https://docs.stripe.com/api/terminal/configuration/update#update_configuration-tipping)[Terminal.Configuration.tipping](https://docs.stripe.com/api/terminal/configuration/object#terminal_configuration_object-tipping)
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

- [supported currency](https://docs.stripe.com/currencies)
- [tipping
configuration](https://docs.stripe.com/terminal/features/collecting-tips/overview)
- [create](https://docs.stripe.com/api/terminal/configuration/create)
- [update](https://docs.stripe.com/api/terminal/configuration/update)
- [Configuration](https://docs.stripe.com/api/terminal/configuration)
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