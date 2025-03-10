# Adds support for merchant amount and currency for test mode authorizations

## What’s new

When you [create a test mode
authorization](https://docs.stripe.com/api/issuing/authorizations/test_mode_create),
you can now optionally specify a
[merchant_amount](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-merchant_amount)
and
[merchant_currency](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-merchant_currency).

## Impact

You can use
[merchant_amount](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-merchant_amount)
and
[merchant_currency](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-merchant_currency)
to create valid
[Authorizations](https://docs.stripe.com/api/issuing/authorizations) that have
currencies that differ from the merchant’s card currency.

With the addition of `merchant_amount`, the
[amount](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-amount)
parameter becomes optional. You can specify either `amount` or `merchant_amount`
when you create test mode authorizations.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NET
 Endpoint

ChangeResourcerespondAdded[Issuing.Authorization](https://docs.stripe.com/api/issuing/authorizations/object)ParametersChangeResources
or
endpointsmerchant_amountmerchant_currencyAdded[Issuing.Authorization.testHelpers#create](https://docs.stripe.com/api/issuing/authorizations/test_mode_create)FieldChangeFrom
→ toIssuing.Authorization.testHelpers#create.amountChanged`required → optional`
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

- [Adds support for issuing fraud
challenges](https://docs.stripe.com/changelog/acacia/2024-11-20/issuing-fraud-challenges)

## Links

- [create a test mode
authorization](https://docs.stripe.com/api/issuing/authorizations/test_mode_create)
-
[merchant_amount](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-merchant_amount)
-
[merchant_currency](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-merchant_currency)
- [Authorizations](https://docs.stripe.com/api/issuing/authorizations)
-
[amount](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-amount)
-
[Issuing.Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
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
- [Adds support for issuing fraud
challenges](https://docs.stripe.com/changelog/acacia/2024-11-20/issuing-fraud-challenges)