# Adds support for configuring the reboot time setting

## What’s new

The `reboot_window` parameter lets you set a custom time window for your
Terminal reader to reboot and update software.

Addedreboot_windowparameter
Reboot time settings for readers that support customized reboot time
configuration.

[POST /v1/terminal/configurationsCreate a new configuration for a Terminal
reader. You can optionally add a
reboot_window.](https://docs.stripe.com/api/terminal/configuration/create)
## Impact

This is useful for ensuring that reader reboots don’t interfere with business
operations.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsreboot_windowAdded[Terminal.Configuration#create](https://docs.stripe.com/api/terminal/configuration/create)[Terminal.Configuration#update](https://docs.stripe.com/api/terminal/configuration/update)[Terminal.Configuration](https://docs.stripe.com/api/terminal/configuration/object)
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

- [Updates consent modeling for saving cards with
Terminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay)
- [Adds the Stripe S700 reader as a valid device
type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)
- [Adds details about offline collection on card_present PaymentMethod
objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)

## Links

- [POST /v1/terminal/configurationsCreate a new configuration for a Terminal
reader. You can optionally add a
reboot_window.](https://docs.stripe.com/api/terminal/configuration/create)
-
[Terminal.Configuration#update](https://docs.stripe.com/api/terminal/configuration/update)
-
[Terminal.Configuration](https://docs.stripe.com/api/terminal/configuration/object)
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
- [Updates consent modeling for saving cards with
Terminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay)
- [Adds the Stripe S700 reader as a valid device
type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)
- [Adds details about offline collection on card_present PaymentMethod
objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)