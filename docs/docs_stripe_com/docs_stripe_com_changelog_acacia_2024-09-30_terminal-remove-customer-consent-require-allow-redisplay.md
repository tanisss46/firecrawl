# Updates consent modeling for saving cards with TerminalBreaking changes

## What’s new

Removes the `customer_consent_collected` parameter and replaces it with
[allow_redisplay](https://docs.stripe.com/api/terminal/readers/process_setup_intent#process_setup_intent-allow_redisplay).

Requires `allow_redisplay` when using `setup_future_usage`.

Removedcustomer_consent_collectedboolean
Indicates whether customer consent has been collected to redisplay the payment
method.

Addedallow_redisplayenum
This field indicates whether this payment method can be shown again to its
customer in a checkout flow. Stripe products such as Checkout and Elements use
this field to determine whether a payment method can be shown as a saved payment
method in a checkout flow. The field defaults to `unspecified`.

## Why is this a breaking change?

This is a breaking change because it requires `allow_redisplay` when saving card
details with Terminal. For SetupIntents, `customer_consent_collected` has been
removed and replaced with `allow_redisplay`. For PaymentIntents that specify
`setup_future_usage`, then `allow_redisplay` must also be passed before
collecting card details. With the new version, you must use `allow_redisplay` to
control whether a payment can be shown to a customer again.

## Impact

Lets you save cards in more regions using Terminal, expanding your service
coverage. Additionally, the improved alignment with industry requirements for
customer consent collection ensures regulatory compliance.

You must add the new parameter to your integration before March 31, 2025 and
ensure that it’s set to `always` or `limited` on all Setup Intents transactions
and Payment Intents that specify `setup_future_usage`.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsallow_redisplayAdded[Terminal.Reader#process_payment_intent.process_config](https://docs.stripe.com/api/terminal/readers/process_payment_intent#process_payment_intent-process_config)[Terminal.Reader#process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)customer_consent_collectedRemoved[Terminal.Reader#process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
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

- [Adds support for configuring the reboot time
setting](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window)
- [Adds the Stripe S700 reader as a valid device
type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)
- [Adds details about offline collection on card_present PaymentMethod
objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)

## Links

-
[allow_redisplay](https://docs.stripe.com/api/terminal/readers/process_setup_intent#process_setup_intent-allow_redisplay)
-
[Terminal.Reader#process_payment_intent.process_config](https://docs.stripe.com/api/terminal/readers/process_payment_intent#process_payment_intent-process_config)
-
[Terminal.Reader#process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
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
- [Adds support for configuring the reboot time
setting](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window)
- [Adds the Stripe S700 reader as a valid device
type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)
- [Adds details about offline collection on card_present PaymentMethod
objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)