# Plans now link to individual products, with several fields moving to the product resourceBreaking changes

## What’s new

Each `Plan` object is now linked to a `Product` object with `type=service`. This
change moves the `Plan` object `statement_descriptor` and `name` attributes to
[Product](https://docs.stripe.com/api#product_object-statement_descriptor)
objects. Additionally, `Plan` objects now have a `nickname` attribute. Creating
a plan now requires passing a
[product](https://docs.stripe.com/api#create_plan-product) attribute to `POST
/v1/plans`. This can be either an existing product ID or a dictionary of product
fields, so that you can continue to create plans without separately creating
products.

## Impact

This change introduces a new relationship between `Plan` and `Product` objects,
moving certain attributes to the `Product` object and adding a `nickname` to
plans. You now need to specify a product when creating plans, either by
referencing an existing product or providing product details. This modification
enhances the flexibility and organization of subscription-related data, but
requires updates to plan creation processes.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2018-02-05`
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

- [Product](https://docs.stripe.com/api#product_object-statement_descriptor)
- [product](https://docs.stripe.com/api#create_plan-product)
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