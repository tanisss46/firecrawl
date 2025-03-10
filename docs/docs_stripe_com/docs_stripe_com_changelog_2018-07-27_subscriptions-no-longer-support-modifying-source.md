# Subscriptions no longer support modifying the source parameter directlyBreaking changes

## What’s new

Subscription endpoints no longer support the `source` parameter. If you want to
change the default source for a customer, use the [Source creation
API](https://docs.stripe.com/api#create_source) to add the new source, and then
the [Customer update API](https://docs.stripe.com/api#update_customer) to set it
as the default.

## Impact

This change removes the ability to directly update a subscription’s payment
source through subscription endpoints. You must now use a two-step process:
first adding a new source through the Source Creation API, then updating the
customer’s default source using the Customer Update API. This modification might
require significant updates to existing code that manages subscription payment
sources

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2018-07-27`
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

- [Source creation API](https://docs.stripe.com/api#create_source)
- [Customer update API](https://docs.stripe.com/api#update_customer)
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