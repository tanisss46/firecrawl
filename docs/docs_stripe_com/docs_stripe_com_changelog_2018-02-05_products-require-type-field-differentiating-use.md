# Products now require a type field, differentiating their use with order SKUs or subscriptions and plansBreaking changes

## What’s new

Products now have a required `type`: `good` for products used with orders SKUs,
or `service` for products used with subscriptions and plans. On API versions
older than 2018-02-05, `type` is set to `good` by default, and `GET
/v1/products` omits products with `type=service` from the list. If you want to
see products with `type=service` on API versions older than 2018-02-05, you can
specify
[type=service](https://docs.stripe.com/api/products/list#list_products-type)
when listing products.

## Impact

This change introduces a required `type` attribute for products, distinguishing
between physical goods and subscription services. You can now categorize your
products more accurately.

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

- [type=service](https://docs.stripe.com/api/products/list#list_products-type)
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