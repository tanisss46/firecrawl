# Adds additional beneficiary information for bank transfer payments

## What’s new

Adds additional information about the beneficiary (receiver) for customers
making bank transfer payments.

## Impact

Stripe provides funding instructions for customers making [bank transfer
payments](https://docs.stripe.com/payments/bank-transfers) to merchants using a
Stripe-provided bank account, including details such as the destination account
number and bank code. Some banks (and bank transfer interfaces) also ask
customers to provide additional information about the receiver, such as their
name, address, and the address of the bank. For convenience, Stripe now includes
this information in the funding instructions presented for each bank transfer
payment.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsaccount_holder_addressaccount_holder_nameaccount_typebank_addressAdded[FundingInstructions.bank_transfer.financial_addresses[].aba](https://docs.stripe.com/api/issuing/funding_instructions/object#issuing_funding_instructions_object-bank_transfer-financial_addresses-aba)`FundingInstructions.bank_transfer.financial_addresses[].swift`[PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].aba](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-aba)
+ 1 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-11-20.acacia`
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

- [Adds support for enabling Adaptive Pricing per Checkout
Session](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param)
- [Customize the submit button recurring Payment Links and Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)

## Links

- [bank transfer payments](https://docs.stripe.com/payments/bank-transfers)
-
[FundingInstructions.bank_transfer.financial_addresses[].aba](https://docs.stripe.com/api/issuing/funding_instructions/object#issuing_funding_instructions_object-bank_transfer-financial_addresses-aba)
-
[PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].aba](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-aba)
-
[PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].swift](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-swift)
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
- [Adds support for enabling Adaptive Pricing per Checkout
Session](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param)
- [Customize the submit button recurring Payment Links and Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)