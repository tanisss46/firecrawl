# Adds funding details to Amazon Pay and Revolut Pay charges

## What’s new

Adds underlying funding details to `charge.payment_method_details` for [Amazon
Pay](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-amazon_pay)
and [Revolut
Pay](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-revolut_pay).

## Impact

You can now see underlying card details when an Amazon Pay or Revolut Pay user
pays with a card. You can see these details in the Dashboard (in the **Events
and logs** section) or in the
[latest_charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
field (when it’s [expanded](https://docs.stripe.com/expand)) of a
[PaymentIntent](https://docs.stripe.com/api/payment_intents) response.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsfundingAdded[Charge.payment_method_details.amazon_pay](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-amazon_pay)[Charge.payment_method_details.revolut_pay](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-revolut_pay)
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
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefix](https://docs.stripe.com/changelog/acacia/2024-12-18/mandate-reference-prefix)

## Links

- [Amazon
Pay](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-amazon_pay)
- [Revolut
Pay](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-revolut_pay)
-
[latest_charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
- [expanded](https://docs.stripe.com/expand)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
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
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefix](https://docs.stripe.com/changelog/acacia/2024-12-18/mandate-reference-prefix)