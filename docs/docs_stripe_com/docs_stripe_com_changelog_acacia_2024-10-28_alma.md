# Adds support for Alma in France

## What’s new

[Alma](https://docs.stripe.com/payments/alma) is a [buy now, pay
later](https://docs.stripe.com/payments/buy-now-pay-later) payment method that’s
now available in France.

## Impact

You can offer French customers the ability to pay in 2, 3, or 4 installments
while getting paid instantly. Learn how to get [started with
Alma](https://docs.stripe.com/payments/alma#get-started).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsalmaAdded[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)[ConfirmationToken.testHelpers#create.payment_method_data](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data)
+ 16
morealma_paymentsAdded[Account#create.capabilities](https://docs.stripe.com/api/accounts/create#create_account-capabilities)[Account#update.capabilities](https://docs.stripe.com/api/accounts/update#update_account-capabilities)[Account.capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)ValuesChangeEnumsalmaAdded[PaymentLink#create.payment_method_types[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-payment_method_types)[PaymentLink#update.payment_method_types[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-payment_method_types)[PaymentLink.payment_method_types[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-payment_method_types)almaAdded[ConfirmationToken.payment_method_preview.type](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-type)[PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)almaAdded[Checkout.Session#create.payment_method_types[]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)[Customer#list_payment_methods.type](https://docs.stripe.com/api/payment_methods/customer_list#list_customer_payment_methods-type)[PaymentMethod#create.type](https://docs.stripe.com/api/payment_methods/create#create_payment_method-type)
+ 1
morealmaAdded[ConfirmationToken.testHelpers#create.payment_method_data.type](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data-type)[PaymentIntent#confirm.payment_method_data.type](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-type)[PaymentIntent#create.payment_method_data.type](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_data-type)
+ 4 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
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

- [Adds support for new South Korean payment
methods](https://docs.stripe.com/changelog/acacia/2024-10-28/south-korean-payment-methods)

## Links

- [Alma](https://docs.stripe.com/payments/alma)
- [buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later)
- [started with Alma](https://docs.stripe.com/payments/alma#get-started)
-
[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
-
[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)
-
[ConfirmationToken.testHelpers#create.payment_method_data](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data)
-
[PaymentIntent#confirm.payment_method_data](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data)
-
[PaymentIntent#confirm.payment_method_options](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options)
-
[PaymentIntent#create.payment_method_data](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_data)
-
[PaymentIntent#create.payment_method_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options)
-
[PaymentIntent#update.payment_method_data](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_data)
-
[PaymentIntent#update.payment_method_options](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options)
-
[PaymentIntent.payment_method_options](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options)
- [PaymentMethod#create](https://docs.stripe.com/api/payment_methods/create)
-
[PaymentMethodConfiguration#create](https://docs.stripe.com/api/payment_method_configurations/create)
-
[PaymentMethodConfiguration#update](https://docs.stripe.com/api/payment_method_configurations/update)
-
[PaymentMethodConfiguration](https://docs.stripe.com/api/payment_method_configurations/object)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
-
[Refund.destination_details](https://docs.stripe.com/api/refunds/object#refund_object-destination_details)
-
[SetupIntent#confirm.payment_method_data](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_data)
-
[SetupIntent#create.payment_method_data](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_data)
-
[SetupIntent#update.payment_method_data](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_data)
-
[Account#create.capabilities](https://docs.stripe.com/api/accounts/create#create_account-capabilities)
-
[Account#update.capabilities](https://docs.stripe.com/api/accounts/update#update_account-capabilities)
-
[Account.capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
-
[PaymentLink#create.payment_method_types[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-payment_method_types)
-
[PaymentLink#update.payment_method_types[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-payment_method_types)
-
[PaymentLink.payment_method_types[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-payment_method_types)
-
[ConfirmationToken.payment_method_preview.type](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-type)
-
[PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
-
[Checkout.Session#create.payment_method_types[]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)
-
[Customer#list_payment_methods.type](https://docs.stripe.com/api/payment_methods/customer_list#list_customer_payment_methods-type)
-
[PaymentMethod#create.type](https://docs.stripe.com/api/payment_methods/create#create_payment_method-type)
-
[PaymentMethod#list.type](https://docs.stripe.com/api/payment_methods/list#list_payment_methods-type)
-
[ConfirmationToken.testHelpers#create.payment_method_data.type](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data-type)
-
[PaymentIntent#confirm.payment_method_data.type](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-type)
-
[PaymentIntent#create.payment_method_data.type](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_data-type)
-
[PaymentIntent#update.payment_method_data.type](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_data-type)
-
[SetupIntent#confirm.payment_method_data.type](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_data-type)
-
[SetupIntent#create.payment_method_data.type](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_data-type)
-
[SetupIntent#update.payment_method_data.type](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_data-type)
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
- [Adds support for new South Korean payment
methods](https://docs.stripe.com/changelog/acacia/2024-10-28/south-korean-payment-methods)