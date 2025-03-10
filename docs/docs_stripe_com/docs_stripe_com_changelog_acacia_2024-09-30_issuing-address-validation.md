# Adds address validation for physical cards

## What’s new

Lets you specify the address validation mode for shipping addresses on physical
cards when you [Create a
card](https://docs.stripe.com/api/issuing/cards/create). You can also update the
shipping addresses on physical cards when you [Update a
card](https://docs.stripe.com/api/issuing/cards/update).

Addedshipping.address_validationobject
Address validation settings.

## Impact

This change increases the accurancy of the shipping address provided by the user
by validating and normailzing the address provided by the user

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsaddress_validationAdded[Issuing.Card#create.shipping](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-shipping)[Issuing.Card.shipping](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping)shippingAdded[Issuing.Card#update](https://docs.stripe.com/api/issuing/cards/update)
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

- [Updates the default value for shipping address
validation](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation)
- [Adds a new webhook event for when funds are deducted as part of a
dispute](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction)

## Links

- [Create a card](https://docs.stripe.com/api/issuing/cards/create)
- [Update a card](https://docs.stripe.com/api/issuing/cards/update)
-
[Issuing.Card#create.shipping](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-shipping)
-
[Issuing.Card.shipping](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping)
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
- [Updates the default value for shipping address
validation](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation)
- [Adds a new webhook event for when funds are deducted as part of a
dispute](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction)