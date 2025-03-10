# Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference prefix

## What’s new

We added the `reference_prefix` parameter to payment method options for SEPA
Direct Debit and Bacs Direct Debit. The parameter is available in [Payment
Intents](https://docs.stripe.com/api/payment_intents), [Setup
Intents](https://docs.stripe.com/api/setup_intents), and [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions) in Payment and Setup
modes.

## Impact

This change lets you specify a reference prefix when creating a mandate with
[SEPA Direct
Debit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-sepa_debit-mandate_options-reference_prefix)
or [Bacs Direct
Debit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-bacs_debit-mandate_options-reference_prefix).

You can specify a prefix in the `mandate_options.reference_prefix` parameter to
customize either the [SEPA Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-sepa_debit-reference)
or [Bacs Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsreference_prefixAdded[Checkout.Session#create.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-bacs_debit-mandate_options)[Checkout.Session#create.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-sepa_debit-mandate_options)[Checkout.Session.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-bacs_debit-mandate_options)
+ 17 more
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

## Related changes

- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-12-18/new-bank-transfer-beneficiary-information)
- [Adds funding details to Amazon Pay and Revolut Pay
charges](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-pm-details)

## Links

- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [SEPA Direct
Debit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-sepa_debit-mandate_options-reference_prefix)
- [Bacs Direct
Debit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-bacs_debit-mandate_options-reference_prefix)
- [SEPA Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-sepa_debit-reference)
- [Bacs Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference)
-
[Checkout.Session#create.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-bacs_debit-mandate_options)
-
[Checkout.Session#create.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-sepa_debit-mandate_options)
-
[Checkout.Session.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-bacs_debit-mandate_options)
-
[Checkout.Session.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-sepa_debit-mandate_options)
-
[PaymentIntent#confirm.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-bacs_debit-mandate_options)
-
[PaymentIntent#confirm.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-sepa_debit-mandate_options)
-
[PaymentIntent#create.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-bacs_debit-mandate_options)
-
[PaymentIntent#create.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-sepa_debit-mandate_options)
-
[PaymentIntent#update.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-bacs_debit-mandate_options)
-
[PaymentIntent#update.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-sepa_debit-mandate_options)
-
[PaymentIntent.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-bacs_debit-mandate_options)
-
[PaymentIntent.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-sepa_debit-mandate_options)
-
[SetupIntent#confirm.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-bacs_debit-mandate_options)
-
[SetupIntent#confirm.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-sepa_debit-mandate_options)
-
[SetupIntent#create.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-bacs_debit-mandate_options)
-
[SetupIntent#create.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-sepa_debit-mandate_options)
-
[SetupIntent#update.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_options-bacs_debit-mandate_options)
-
[SetupIntent#update.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_options-sepa_debit-mandate_options)
-
[SetupIntent.payment_method_options.bacs_debit.mandate_options](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options-bacs_debit-mandate_options)
-
[SetupIntent.payment_method_options.sepa_debit.mandate_options](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options-sepa_debit-mandate_options)
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
- [Adds additional beneficiary information for bank transfer
payments](https://docs.stripe.com/changelog/acacia/2024-12-18/new-bank-transfer-beneficiary-information)
- [Adds funding details to Amazon Pay and Revolut Pay
charges](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-pm-details)