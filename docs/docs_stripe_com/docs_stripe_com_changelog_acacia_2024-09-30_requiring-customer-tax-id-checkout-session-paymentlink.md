# Adds support for requiring a customer tax ID on Checkout and Payment Links

## What’s new

Adds support for requiring a customer tax ID on `Checkout.Session` and
`PaymentLink` using the new `tax_id_collection[required]` parameter. When this
parameter is set to `if_supported`, customers paying from a country where tax ID
[collection is
supported](https://docs.stripe.com/tax/checkout/tax-ids#supported-types) will be
required to provide their tax ID information as part of the payment.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsrequiredAdded[Checkout.Session#create.tax_id_collection](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-tax_id_collection)[Checkout.Session.tax_id_collection](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-tax_id_collection)[PaymentLink#create.tax_id_collection](https://docs.stripe.com/api/payment-link/create#create_payment_link-tax_id_collection)
+ 2 more
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

- [Adds Switzerland UID as a supported customer tax
ID](https://docs.stripe.com/changelog/acacia/2024-09-30/switzerland-tax-uid)
- [Adds Croatian Personal Identification Number to supported Tax
IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number)

## Links

- [collection is
supported](https://docs.stripe.com/tax/checkout/tax-ids#supported-types)
-
[Checkout.Session#create.tax_id_collection](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-tax_id_collection)
-
[Checkout.Session.tax_id_collection](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-tax_id_collection)
-
[PaymentLink#create.tax_id_collection](https://docs.stripe.com/api/payment-link/create#create_payment_link-tax_id_collection)
-
[PaymentLink#update.tax_id_collection](https://docs.stripe.com/api/payment-link/update#update_payment_link-tax_id_collection)
-
[PaymentLink.tax_id_collection](https://docs.stripe.com/api/payment-link/object#payment_link_object-tax_id_collection)
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
- [Adds Switzerland UID as a supported customer tax
ID](https://docs.stripe.com/changelog/acacia/2024-09-30/switzerland-tax-uid)
- [Adds Croatian Personal Identification Number to supported Tax
IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number)