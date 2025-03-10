# Adds support for Affirm transaction IDs

## What’s new

Displays the Affirm transaction ID associated with a payment in the Payment
details page of the Stripe Dashboard or using the API.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointstransaction_idAdded[Charge.payment_method_details.affirm](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-affirm)
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

-
[Charge.payment_method_details.affirm](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-affirm)
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