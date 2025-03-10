# Issuing authorizations now include merchant tax ID number

## What’s new

Adds a new `tax_id` field under `issuing_authorization.merchant_data` that
contains the seller’s tax ID number. This field is currently populated for
French sellers only.

## Impact

This field allows you to identify the business associated with an authorization
by the tax ID number.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointstax_idAdded[Issuing.Authorization.merchant_data](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data)[Issuing.Transaction.merchant_data](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-merchant_data)
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

- [Creates Issuing authorizations when Stripe is
unavailable](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-auths-when-stripe-unavailable)

## Links

-
[Issuing.Authorization.merchant_data](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data)
-
[Issuing.Transaction.merchant_data](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-merchant_data)
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
- [Creates Issuing authorizations when Stripe is
unavailable](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-auths-when-stripe-unavailable)