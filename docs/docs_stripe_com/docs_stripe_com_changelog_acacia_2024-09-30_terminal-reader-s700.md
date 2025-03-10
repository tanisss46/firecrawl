# Adds the Stripe S700 reader as a valid device type

## What’s new

The [Stripe Reader
S700](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700)
is now available as an enum for the `device_type`
[parameter](https://docs.stripe.com/api/terminal/readers/object) for
[Reader](https://docs.stripe.com/api/terminal/readers/object) objects.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsstripe_s700Added[Terminal.Reader#list.device_type](https://docs.stripe.com/api/terminal/readers/list#list_terminal_reader-device_type)[Terminal.Reader.device_type](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-device_type)
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
- [Adds support for configuring the reboot time
setting](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window)
- [Adds details about offline collection on card_present PaymentMethod
objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)

## Links

- [Stripe Reader
S700](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700)
- [parameter](https://docs.stripe.com/api/terminal/readers/object)
-
[Terminal.Reader#list.device_type](https://docs.stripe.com/api/terminal/readers/list#list_terminal_reader-device_type)
-
[Terminal.Reader.device_type](https://docs.stripe.com/api/terminal/readers/object#terminal_reader_object-device_type)
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
- [Adds support for configuring the reboot time
setting](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window)
- [Adds details about offline collection on card_present PaymentMethod
objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)