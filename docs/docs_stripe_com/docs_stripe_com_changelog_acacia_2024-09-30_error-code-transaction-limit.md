# Adds error code for exceeded transaction limits

## What’s new

Adds the `charge_exceeds_transaction_limit` [error
code](https://docs.stripe.com/error-codes#charge-exceeds-source-limit) as an
enum value to the following resources:
[Invoices](https://docs.stripe.com/api/invoices), [Payment
Intents](https://docs.stripe.com/api/payment_intents), [Setup
Attempts](https://docs.stripe.com/api/setup_attempts), [Setup
Intents](https://docs.stripe.com/api/setup_intents), and
[Errors](https://docs.stripe.com/api/errors).

This error occurs when the amount of a transaction that uses a [bank
debit](https://docs.stripe.com/payments/bank-debits) payment method causes the
merchant to exceed their transaction volume limit.

## Impact

This allows you to [test your integration](https://docs.stripe.com/testing) and
more easily discover any issues with transaction or weekly volume limits.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumscharge_exceeds_transaction_limitAdded[Invoice.last_finalization_error.code](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error-code)[PaymentIntent.last_payment_error.code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-code)[SetupAttempt.setup_error.code](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-setup_error-code)
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

- [Adds new error code for invalid mandate prefixes to Bacs Direct Debit and
SEPA Direct Debit
payments](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-invalid-mandate-reference-prefix)

## Links

- [error code](https://docs.stripe.com/error-codes#charge-exceeds-source-limit)
- [Invoices](https://docs.stripe.com/api/invoices)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Setup Attempts](https://docs.stripe.com/api/setup_attempts)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
- [Errors](https://docs.stripe.com/api/errors)
- [bank debit](https://docs.stripe.com/payments/bank-debits)
- [test your integration](https://docs.stripe.com/testing)
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
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)
- [Adds new error code for invalid mandate prefixes to Bacs Direct Debit and
SEPA Direct Debit
payments](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-invalid-mandate-reference-prefix)