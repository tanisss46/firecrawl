# Adds support for in-person payment methods, including Interac cards

## What’s new

Allows for better handling and differentiation of in-person transactions made
with `card_present` or `interac_present` payment methods.

Addedcard_present.descriptionnullable string
A high-level description of the type of cards issued in this range. (For
internal use only and not typically available in standard API requests.)

Addedcard_present.issuernullable string
The name of the card’s issuing bank. (For internal use only and not typically
available in standard API requests.)

Addedcard_present.brand_productnullable string
The product code that identifies the specific program or product associated with
a card.

Addedcard_present.network_transaction_idnullable string
This is used by the financial networks to identify a transaction. Visa calls
this the Transaction ID, Mastercard calls this the Trace ID, and American
Express calls this the Acquirer Reference Data. The first three digits of the
Trace ID is the Financial Network Code, the next 6 digits is the Banknet
Reference Number, and the last 4 digits represent the date (MM/DD). This field
will be available for successful Visa, Mastercard, or American Express
transactions and always null for other card brands.

## Impact

This change allows you to access specific details related to these transaction
types.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsissuerdescriptionbrand_productnetwork_transaction_idAdded[Charge.payment_method_details.card_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present)issuerdescriptionnetwork_transaction_idAdded[Charge.payment_method_details.interac_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-interac_present)issuerdescriptionbrand_productAdded[PaymentMethod.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present)issuerdescriptionAdded[PaymentMethod.interac_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-interac_present)network_transaction_idbrand_productAdded[ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present)[PaymentMethod.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-generated_from-payment_method_details-card_present)
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
- [Displays authorization_code for
Charges](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges)
- [Adds wallet details for card_present Charges and Payment
Methods](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods)
- [Adds country field for Charges that use
Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
Disputes](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)

## Links

-
[Charge.payment_method_details.card_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present)
-
[Charge.payment_method_details.interac_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-interac_present)
-
[PaymentMethod.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present)
-
[PaymentMethod.interac_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-interac_present)
-
[ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present)
-
[PaymentMethod.card.generated_from.payment_method_details.card_present](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-generated_from-payment_method_details-card_present)
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
- [Displays authorization_code for
Charges](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges)
- [Adds wallet details for card_present Charges and Payment
Methods](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods)
- [Adds country field for Charges that use
Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
Disputes](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)