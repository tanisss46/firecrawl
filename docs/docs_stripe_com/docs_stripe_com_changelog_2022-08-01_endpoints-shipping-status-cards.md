# New endpoints for managing a physical card's shipping status in test modeBreaking changes

## What’s new

When creating a physical card in testmode, its shipping
[status](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-status)
no longer automatically changes from `pending` to `delivered`. This
functionality is now accessible through the following new endpoints:

- `/v1/test_helpers/issuing/cards/:card/shipping/ship`
- `/v1/test_helpers/issuing/cards/:card/shipping/deliver`
- `/v1/test_helpers/issuing/cards/:card/shipping/return`
- `/v1/test_helpers/issuing/cards/:card/shipping/fail`

## Impact

You now have more control over simulating different shipping scenarios using new
dedicated endpoints. This change allows for more comprehensive testing of
shipping-related workflows in card issuance processes

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2022-08-01`
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
[status](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-status)
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