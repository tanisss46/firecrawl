# Adds option to retrieve CVC tokens on Confirmation Tokens

## What’s new

Lets you specify the `cvc_update` token collected from the [Payment
Element](https://docs.stripe.com/payments/payment-element) for a [Confirmation
Token](https://docs.stripe.com/api/confirmation_tokens).

Addedpayment_method_options.card.cvc_tokennullable string
The `cvc_update` Token collected from the Payment Element.

## Impact

This change lets you use CVC numbers with Confirmation Tokens.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointspayment_method_optionsAdded[ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens/object)
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

- [Adds customer ID to payment method preview on a confirmation
token](https://docs.stripe.com/changelog/acacia/2024-09-30/support-customer-payment-method-preview)
- [Adds support for identifying the unique payer for the BLIK payment
method](https://docs.stripe.com/changelog/acacia/2024-09-30/buyer-id-blik)
- [Adds support for Affirm transaction
IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/affirm-transaction-id-dashboard)
- [Adds support for in-person payment methods, including Interac
cards](https://docs.stripe.com/changelog/acacia/2024-09-30/card-interac-present-support)
- [Displays authorization_code for
Charges](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges)
- [Adds wallet details for card_present Charges and Payment
Methods](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods)
- [Adds country field for Charges that use
Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
Disputes](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)

## Links

- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)
- [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens/object)
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
- [Adds customer ID to payment method preview on a confirmation
token](https://docs.stripe.com/changelog/acacia/2024-09-30/support-customer-payment-method-preview)
- [Adds support for identifying the unique payer for the BLIK payment
method](https://docs.stripe.com/changelog/acacia/2024-09-30/buyer-id-blik)
- [Adds support for Affirm transaction
IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/affirm-transaction-id-dashboard)
- [Adds support for in-person payment methods, including Interac
cards](https://docs.stripe.com/changelog/acacia/2024-09-30/card-interac-present-support)
- [Displays authorization_code for
Charges](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges)
- [Adds wallet details for card_present Charges and Payment
Methods](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods)
- [Adds country field for Charges that use
Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
Disputes](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)