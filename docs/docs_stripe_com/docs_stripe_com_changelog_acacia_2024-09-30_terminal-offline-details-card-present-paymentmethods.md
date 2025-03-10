# Adds details about offline collection on card_present PaymentMethod objects

## What’s new

This change provides visibility into `card_present` [Payment
Methods](https://docs.stripe.com/api/payment_methods) collected offline,
allowing you to track and manage offline transactions processed through the
Terminal mobile SDKs. By including a `type` field set to `deferred`, you can
accurately report and reconcile offline `card_present` transactions.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsofflineAdded[ConfirmationToken.payment_method_preview.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card_present)[PaymentMethod.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present)typeAdded[Charge.payment_method_details.card_present.offline](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-offline)[ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present.offline](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present-offline)[ConfirmationToken.payment_method_preview.card_present.offline](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card_present-offline)
+ 3 more
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
- [Adds the Stripe S700 reader as a valid device
type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)

## Links

- [Payment Methods](https://docs.stripe.com/api/payment_methods)
-
[ConfirmationToken.payment_method_preview.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card_present)
-
[PaymentMethod.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present)
-
[Charge.payment_method_details.card_present.offline](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-offline)
-
[ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present.offline](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present-offline)
-
[ConfirmationToken.payment_method_preview.card_present.offline](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card_present-offline)
-
[PaymentMethod.card.generated_from.payment_method_details.card_present.offline](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-generated_from-payment_method_details-card_present-offline)
-
[PaymentMethod.card_present.offline](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present-offline)
-
[SetupAttempt.payment_method_details.card_present.offline](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-setup_error-code)
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
- [Adds the Stripe S700 reader as a valid device
type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)