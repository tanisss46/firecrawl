# Adds PayPal country property to the PaymentMethods and Charge objects

## What’s new

Adds the `country` property for PayPal to the [Payment
Methods](https://docs.stripe.com/api/payment_methods) and
[Charge](https://docs.stripe.com/api/charges) resources:

- For Payment Methods, in the
[paypal](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal-country)
hash.
- For Charges, in the
[payment_method_details.paypal](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal)
hash.

## Impact

The `country` property represents the buyer’s country, which PayPal provides (if
supported) at the time of authorization or settlement. You can’t set or mutate
it. With this change, you can now retrieve the `country` value from either:

- A customer’s [PayPal
PaymentMethod](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal-country)
- A [transaction paid using
PayPal](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal)

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointscountryAdded[Charge.payment_method_details.paypal](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal)[ConfirmationToken.payment_method_preview.paypal](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-paypal)[PaymentMethod.paypal](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal)
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

- [Adds support for the Pay by Bank local payment
method](https://docs.stripe.com/changelog/acacia/2025-01-27/pay-by-bank-lpm)

## Links

- [Payment Methods](https://docs.stripe.com/api/payment_methods)
- [Charge](https://docs.stripe.com/api/charges)
-
[paypal](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal-country)
-
[payment_method_details.paypal](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal)
-
[ConfirmationToken.payment_method_preview.paypal](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-paypal)
-
[PaymentMethod.paypal](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal)
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
- [Adds support for the Pay by Bank local payment
method](https://docs.stripe.com/changelog/acacia/2025-01-27/pay-by-bank-lpm)