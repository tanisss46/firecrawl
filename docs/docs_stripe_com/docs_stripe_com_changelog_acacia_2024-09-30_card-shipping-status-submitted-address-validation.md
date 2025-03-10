# Updates the default value for shipping address validationBreaking changes

## What’s new

Lets you more accurately track the status of physical card shipments, ensuring
you know when a card has been submitted for shipping. Additionally, the updated
default for shipping address
validation—`validation_and_normalization`—automatically validates and normalizes
addresses, reducing the likelihood of shipment errors and improving delivery
success rates.

## Why is this a breaking change?

This change introduces a new default value.

## Impact

Increase the address validation process by generating an error for physical card
shipping addresses that are likely undeliverable.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsubmittedAdded[Issuing.Card.shipping.status](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-status)
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

- [Adds address validation for physical
cards](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-address-validation)
- [Adds a new webhook event for when funds are deducted as part of a
dispute](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction)

## Links

-
[Issuing.Card.shipping.status](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-status)
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
- [Adds address validation for physical
cards](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-address-validation)
- [Adds a new webhook event for when funds are deducted as part of a
dispute](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction)