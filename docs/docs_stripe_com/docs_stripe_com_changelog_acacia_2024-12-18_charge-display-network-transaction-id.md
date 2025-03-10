# Adds network transaction ID to charges

## What’s new

Adds
[network_transaction_id](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-interac_present-network_transaction_id)
as a property of the [Charge](https://docs.stripe.com/api/charges) object.

## Impact

Successful Visa, Mastercard, Amex, Discover, and Cartes Bancaires transactions
include the
[network_transaction_id](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-interac_present-network_transaction_id)
property in the associated [Charge](https://docs.stripe.com/api/charges) to
accurately map a Stripe transaction with the card network identifier. Declined
transactions and card validations don’t include the property. Successful
transactions for other card brands include the property as a null value.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsnetwork_transaction_idAdded[Charge](https://docs.stripe.com/api/charges/object)
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
[network_transaction_id](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-interac_present-network_transaction_id)
- [Charge](https://docs.stripe.com/api/charges)
- [Charge](https://docs.stripe.com/api/charges/object)
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