# Adds advice code to Charges

## What’s new

Adds the
[advice_code](https://docs.stripe.com/api/charges/object#charge_object-outcome-advice_code)
property to the [Charge](https://docs.stripe.com/api/charges/object) object. The
`advice_code` is an enumerated value that provides more details about
unsuccessful transactions.

## Impact

You can use the `advice_code` to understand [how to proceed with an
error](https://docs.stripe.com/declines#issuer-declines) if a transaction is
unsuccessful.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsadvice_codeAdded[Charge.outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome)advice_codeAdded[Invoice.last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)[PaymentIntent.last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)[SetupAttempt.setup_error](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-setup_error)
+ 2 more
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

-
[advice_code](https://docs.stripe.com/api/charges/object#charge_object-outcome-advice_code)
- [Charge](https://docs.stripe.com/api/charges/object)
- [how to proceed with an
error](https://docs.stripe.com/declines#issuer-declines)
-
[Charge.outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome)
-
[Invoice.last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
-
[PaymentIntent.last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
-
[SetupAttempt.setup_error](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-setup_error)
-
[SetupIntent.last_setup_error](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-last_setup_error)
- [StripeError](https://docs.stripe.com/api/errors)
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