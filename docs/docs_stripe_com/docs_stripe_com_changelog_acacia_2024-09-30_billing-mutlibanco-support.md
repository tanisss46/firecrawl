# Adds support for using the Multibanco payment method with billing

## What’s new

Adds the Multibanco payment method as an available option in invoices and
subscriptions.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsmultibancoAdded[Invoice#create.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_types)[Invoice#update.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/update#update_invoice-payment_settings-payment_method_types)[Invoice.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
+ 3 more
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

- [Adds support for three new payment methods: Multibanco, Twint, and
Zip](https://docs.stripe.com/changelog/acacia/2024-09-30/payment-links-new-payment-methods)
- [Adds Twint to the PaymentMethodConfiguration
API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration)
- [Adds Girocard as a PaymentMethod brand and
network](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network)

## Links

-
[Invoice#create.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_types)
-
[Invoice#update.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/update#update_invoice-payment_settings-payment_method_types)
-
[Invoice.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
-
[Subscription#create.payment_settings.payment_method_types[]](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_settings-payment_method_types)
-
[Subscription#update.payment_settings.payment_method_types[]](https://docs.stripe.com/api/subscriptions/update#update_subscription-payment_settings-payment_method_types)
-
[Subscription.payment_settings.payment_method_types[]](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-payment_method_types)
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
- [Adds support for three new payment methods: Multibanco, Twint, and
Zip](https://docs.stripe.com/changelog/acacia/2024-09-30/payment-links-new-payment-methods)
- [Adds Twint to the PaymentMethodConfiguration
API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration)
- [Adds Girocard as a PaymentMethod brand and
network](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network)