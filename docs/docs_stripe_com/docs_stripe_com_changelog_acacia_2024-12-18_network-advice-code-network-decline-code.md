# Adds network advice and decline codes

## What’s new

When a charge is declined, two new error codes are now part of the response. The
`network_decline_code` provides more information from the card network about why
the charge was declined. The `network_advice_code` provides more information
about how to handle the decline.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsnetwork_advice_codenetwork_decline_codeAdded[Charge.outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome)[Invoice.last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)[PaymentIntent.last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
+ 3 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-12-18.acacia`
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