# Adds support for three new payment methods: Multibanco, Twint, and Zip

## What’s new

Expands the suite of supported payment methods on Payment Links by adding
support for [Multibanco](https://docs.stripe.com/payments/multibanco),
[Twint](https://docs.stripe.com/payments/twint), and
[Zip](https://docs.stripe.com/payments/zip).

## Impact

This allows you to use
[Multibanco](https://docs.stripe.com/payments/multibanco),
[Twint](https://docs.stripe.com/payments/twint), and
[Zip](https://docs.stripe.com/payments/zip) with Payment Links.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValuesChangeEnumsmultibancotwintzipAdded[PaymentLink#create.payment_method_types[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-payment_method_types)[PaymentLink#update.payment_method_types[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-payment_method_types)[PaymentLink.payment_method_types[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-payment_method_types)
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

- [Adds support for using the Multibanco payment method with
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-mutlibanco-support)
- [Adds Twint to the PaymentMethodConfiguration
API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration)
- [Adds Girocard as a PaymentMethod brand and
network](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network)

## Links

- [Multibanco](https://docs.stripe.com/payments/multibanco)
- [Twint](https://docs.stripe.com/payments/twint)
- [Zip](https://docs.stripe.com/payments/zip)
-
[PaymentLink#create.payment_method_types[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-payment_method_types)
-
[PaymentLink#update.payment_method_types[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-payment_method_types)
-
[PaymentLink.payment_method_types[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-payment_method_types)
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
- [Adds support for using the Multibanco payment method with
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-mutlibanco-support)
- [Adds Twint to the PaymentMethodConfiguration
API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration)
- [Adds Girocard as a PaymentMethod brand and
network](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network)