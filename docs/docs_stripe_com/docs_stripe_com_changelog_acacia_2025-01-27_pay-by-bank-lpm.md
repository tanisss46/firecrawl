# Adds support for the Pay by Bank local payment method

## What’s new

Adds support for the [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
local payment method (LPM)—a single-use payment method that lets customers pay
directly from their bank account.

## Impact

Pay by Bank is a single-use payment method that lets customers pay directly from
their bank account instead of using a card. It runs on banking infrastructure
and open banking APIs. When a customer chooses Pay by Bank, they select their
bank and approve the payment on their bank’s mobile app or web portal.

You can use Pay by Bank with [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
or integrate it using [Payment
Intents](https://docs.stripe.com/api/payment_intents).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointspay_by_bankAdded[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)[Checkout.Session#create.payment_method_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options)[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)
+ 17
morepay_by_bank_paymentsAdded[Account#create.capabilities](https://docs.stripe.com/api/accounts/create#create_account-capabilities)[Account#update.capabilities](https://docs.stripe.com/api/accounts/update#update_account-capabilities)[Account.capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)ValuesChangeEnumspay_by_bankAdded[Checkout.Session#create.payment_method_types[]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)pay_by_bankAdded[ConfirmationToken.testHelpers#create.payment_method_data.type](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data-type)[PaymentIntent#confirm.payment_method_data.type](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-type)[PaymentIntent#create.payment_method_data.type](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_data-type)
+ 4
morepay_by_bankAdded[ConfirmationToken.payment_method_preview.type](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-type)[PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)pay_by_bankAdded[PaymentLink#create.payment_method_types[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-payment_method_types)[PaymentLink#update.payment_method_types[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-payment_method_types)[PaymentLink.payment_method_types[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-payment_method_types)
+ 3 more
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

- [Adds PayPal country property to the PaymentMethods and Charge
objects](https://docs.stripe.com/changelog/acacia/2025-01-27/paypal-country)

## Links

- [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
- [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
-
[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
-
[Checkout.Session#create.payment_method_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options)
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
- [PaymentMethod#update](https://docs.stripe.com/api/payment_methods/update)
-
[PaymentMethodConfiguration#create](https://docs.stripe.com/api/payment_method_configurations/create)
-
[PaymentMethodConfiguration#update](https://docs.stripe.com/api/payment_method_configurations/update)
-
[PaymentMethodConfiguration](https://docs.stripe.com/api/payment_method_configurations/object)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
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
[Checkout.Session#create.payment_method_types[]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)
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
-
[ConfirmationToken.payment_method_preview.type](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-type)
-
[PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
-
[PaymentLink#create.payment_method_types[]](https://docs.stripe.com/api/payment-link/create#create_payment_link-payment_method_types)
-
[PaymentLink#update.payment_method_types[]](https://docs.stripe.com/api/payment-link/update#update_payment_link-payment_method_types)
-
[PaymentLink.payment_method_types[]](https://docs.stripe.com/api/payment-link/object#payment_link_object-payment_method_types)
-
[Customer#list_payment_methods.type](https://docs.stripe.com/api/payment_methods/customer_list#list_customer_payment_methods-type)
-
[PaymentMethod#create.type](https://docs.stripe.com/api/payment_methods/create#create_payment_method-type)
-
[PaymentMethod#list.type](https://docs.stripe.com/api/payment_methods/list#list_payment_methods-type)
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
- [Adds PayPal country property to the PaymentMethods and Charge
objects](https://docs.stripe.com/changelog/acacia/2025-01-27/paypal-country)