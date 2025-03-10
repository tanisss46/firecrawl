# Adds Sudan to allowed shipping countries for Checkout

## What’s new

Adds Sudan (`SD`) to the list of possible enum values for
[shipping_address_collection.allowed_countries](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries).

## Impact

The
[allowed_countries](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries)
parameter lets you specify which countries your customers can select as a
shipping location. You can now transact and ship to Sudan.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsSDAdded[Checkout.Session#create.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries)[Checkout.Session.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-shipping_address_collection-allowed_countries)[PaymentLink#create.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-shipping_address_collection-allowed_countries)
+ 2 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2025-01-27.acacia`
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

- [Adds discounts field to Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sessions-discounts-field)

## Links

-
[shipping_address_collection.allowed_countries](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries)
-
[Checkout.Session.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-shipping_address_collection-allowed_countries)
-
[PaymentLink#create.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-shipping_address_collection-allowed_countries)
-
[PaymentLink#update.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-shipping_address_collection-allowed_countries)
-
[PaymentLink.shipping_address_collection.allowed_countries[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-shipping_address_collection-allowed_countries)
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
- [Adds discounts field to Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sessions-discounts-field)