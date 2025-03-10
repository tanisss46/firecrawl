# Adds new error code for invalid mandate prefixes to Bacs Direct Debit and SEPA Direct Debit payments

## What’s new

Adds the `invalid_mandate_reference_prefix_format` [error
code](https://docs.stripe.com/error-codes) as an enum value to the following
resources: [Payment Intents](https://docs.stripe.com/api/payment_intents),
[Setup Attempts](https://docs.stripe.com/api/setup_attempts), [Setup
Intents](https://docs.stripe.com/api/setup_intents), and
[Errors](https://docs.stripe.com/api/errors). This allows you to test your
integration and more easily discover any issues with the format of reference
prefixes in [Mandates](https://docs.stripe.com/api/mandates) related to [Bacs
Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit) and
[SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit) payments.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsmandate_optionsAdded[PaymentIntent#confirm.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-bacs_debit)[PaymentIntent#create.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-bacs_debit)[PaymentIntent#update.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-bacs_debit)
+ 1
morebacs_debitAdded[SetupIntent#confirm.payment_method_options](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options)[SetupIntent#create.payment_method_options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options)[SetupIntent#update.payment_method_options](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_options)
+ 1
moreValueChangeEnumsinvalid_mandate_reference_prefix_formatAdded[Invoice.last_finalization_error.code](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error-code)[PaymentIntent.last_payment_error.code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-code)[SetupAttempt.setup_error.code](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-setup_error-code)
+ 2 more
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

- [Adds error code for exceeded transaction
limits](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-transaction-limit)

## Links

- [error code](https://docs.stripe.com/error-codes)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Setup Attempts](https://docs.stripe.com/api/setup_attempts)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
- [Errors](https://docs.stripe.com/api/errors)
- [Mandates](https://docs.stripe.com/api/mandates)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
-
[PaymentIntent#confirm.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-bacs_debit)
-
[PaymentIntent#create.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-bacs_debit)
-
[PaymentIntent#update.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-bacs_debit)
-
[PaymentIntent.payment_method_options.bacs_debit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-bacs_debit)
-
[SetupIntent#confirm.payment_method_options](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options)
-
[SetupIntent#create.payment_method_options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options)
-
[SetupIntent#update.payment_method_options](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_options)
-
[SetupIntent.payment_method_options](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options)
-
[Invoice.last_finalization_error.code](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error-code)
-
[PaymentIntent.last_payment_error.code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-code)
-
[SetupAttempt.setup_error.code](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-setup_error-code)
-
[SetupIntent.last_setup_error.code](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-last_setup_error-code)
- [StripeError.code](https://docs.stripe.com/api/errors#errors-code)
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
- [Adds error code for exceeded transaction
limits](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-transaction-limit)