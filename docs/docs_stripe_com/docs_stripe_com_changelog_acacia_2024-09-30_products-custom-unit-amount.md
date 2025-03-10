# Add support for custom_unit_amount during product creation

## What’s new

Adds the `custom_unit_amount` parameter to a
[Product](https://docs.stripe.com/api/products)’s `default_price_data`
[parameter](https://docs.stripe.com/api/products/create#create_product-default_price_data).

Addedcustom_unit_amountobject
When set, provides configuration for the amount to be adjusted by the customer
during Checkout Sessions and Payment Links. Required unless `unit_amount` is
provided.

## Impact

This allows you to specify custom unit amounts when creating a product’s default
price data. This change also benefits businesses that need specific price
configurations tailored to their unique offerings.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointscustom_unit_amountAdded[Product#create.default_price_data](https://docs.stripe.com/api/products/create#create_product-default_price_data)
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

## Links

- [Product](https://docs.stripe.com/api/products)
-
[parameter](https://docs.stripe.com/api/products/create#create_product-default_price_data)
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