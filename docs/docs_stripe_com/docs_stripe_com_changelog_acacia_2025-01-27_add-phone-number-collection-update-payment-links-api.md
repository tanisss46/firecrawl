# Modify phone number collection on Payment Links

## What’s new

Adds the
[phone_number_collection](https://docs.stripe.com/api/payment-link/object#payment_link_object-phone_number_collection)
parameter to the [update Payment Link
method](https://docs.stripe.com/api/payment-link/update). You can use this new
parameter to enable or disable phone number collection in the payment form of an
existing Payment Link.

## Impact

You can now update existing Payment Links to configure whether the payment form
requires the customer to provide a phone number. Previously, you had to set this
configuration when creating a Payment Link, with no way to change it.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsphone_number_collectionAdded[PaymentLink#update](https://docs.stripe.com/api/payment-link/update)
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

## Links

-
[phone_number_collection](https://docs.stripe.com/api/payment-link/object#payment_link_object-phone_number_collection)
- [update Payment Link method](https://docs.stripe.com/api/payment-link/update)
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