# Adds wallet details for card_present Charges and Payment Methods

## What’s new

Adds a `wallet.type` field to `card_present`
[Charges](https://docs.stripe.com/api/charges) and [Payment
Methods](https://docs.stripe.com/api/payment_methods).

Addedcard_present.walletnullable object
If a mobile wallet was presented in the transaction, this contains the details
of the mobile wallet.

## Impact

Lets you see the type of wallet used for `card_present`
[Charges](https://docs.stripe.com/api/charges) and [Payment
Methods](https://docs.stripe.com/api/payment_methods).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointswalletAdded[Charge.payment_method_details.card_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present)[ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present)[ConfirmationToken.payment_method_preview.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card_present)
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

- [Adds option to retrieve CVC tokens on Confirmation
Tokens](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-method-options-confirmation)
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
- [Adds country field for Charges that use
Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
Disputes](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)

## Links

- [Charges](https://docs.stripe.com/api/charges)
- [Payment Methods](https://docs.stripe.com/api/payment_methods)
-
[Charge.payment_method_details.card_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present)
-
[ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present)
-
[ConfirmationToken.payment_method_preview.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card_present)
-
[PaymentMethod.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-generated_from-payment_method_details-card_present)
-
[PaymentMethod.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present)
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
- [Adds option to retrieve CVC tokens on Confirmation
Tokens](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-method-options-confirmation)
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
- [Adds country field for Charges that use
Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
Disputes](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)