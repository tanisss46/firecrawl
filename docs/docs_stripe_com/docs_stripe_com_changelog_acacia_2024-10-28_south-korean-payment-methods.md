# Adds support for new South Korean payment methods

## What’s new

Adds support for several new South Korean payment methods:

- [South Korean
cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment)
- [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment)

You can use these payment methods with any of the following integration paths:

- [Checkout](https://docs.stripe.com/payments/checkout)
- [Elements](https://docs.stripe.com/payments/elements)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Billing](https://docs.stripe.com/billing)
- [Invoicing](https://docs.stripe.com/invoicing/overview)

## Impact

Wallets and cards are popular payment methods in South Korea, with a variety of
local card issuers but no single predominant brand. To provide familiar payment
options and increase conversion rates, you can now offer the majority of payment
methods available in South Korea to your customers.

You can now use these South Korean payments with:

-
[capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method):
This lets you [place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage):
This lets you [save payment details during
payment](https://docs.stripe.com/payments/save-during-payment) and charge the
payment method later.

This makes it easier to use the South Korean payment methods with [Stripe
connectors](https://docs.stripe.com/connectors).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointskakao_paykr_cardAdded[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)[ConfirmationToken.testHelpers#create.payment_method_data](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data)
+ 14
morenaver_payAdded[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)[ConfirmationToken.testHelpers#create.payment_method_data](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data)
+ 13
morepaycosamsung_payAdded[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)[ConfirmationToken.testHelpers#create.payment_method_data](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data)
+ 12
morekakao_pay_paymentskr_card_paymentsnaver_pay_paymentspayco_paymentssamsung_pay_paymentsAdded[Account#create.capabilities](https://docs.stripe.com/api/accounts/create#create_account-capabilities)[Account#update.capabilities](https://docs.stripe.com/api/accounts/update#update_account-capabilities)[Account.capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)kakao_paykr_cardnaver_paypaycosamsung_payAdded[Checkout.Session#create.payment_method_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options)[Checkout.Session.payment_method_options](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options)ValuesChangeEnumskakao_paykr_cardnaver_paypaycosamsung_payAdded[Checkout.Session#create.payment_method_types[]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_types)[Customer#list_payment_methods.type](https://docs.stripe.com/api/payment_methods/customer_list#list_customer_payment_methods-type)[PaymentMethod#create.type](https://docs.stripe.com/api/payment_methods/create#create_payment_method-type)
+ 1
morekakao_paykr_cardnaver_paypaycosamsung_payAdded[ConfirmationToken.testHelpers#create.payment_method_data.type](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data-type)[PaymentIntent#confirm.payment_method_data.type](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-type)[PaymentIntent#create.payment_method_data.type](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_data-type)
+ 4
morekakao_paykr_cardnaver_paypaycoAdded[Invoice#create.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_types)[Invoice#update.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/update#update_invoice-payment_settings-payment_method_types)[Invoice.payment_settings.payment_method_types[]](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
+ 3
morekakao_paykr_cardnaver_paypaycosamsung_payAdded[ConfirmationToken.payment_method_preview.type](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-type)[PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
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

- [Adds support for Alma in
France](https://docs.stripe.com/changelog/acacia/2024-10-28/alma)

## Links

- [South Korean
cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment)
- [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Elements](https://docs.stripe.com/payments/elements)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Billing](https://docs.stripe.com/billing)
- [Invoicing](https://docs.stripe.com/invoicing/overview)
-
[capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method)
- [place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage)
- [save payment details during
payment](https://docs.stripe.com/payments/save-during-payment)
- [Stripe connectors](https://docs.stripe.com/connectors)
-
[Charge.payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
-
[ConfirmationToken.payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)
-
[ConfirmationToken.testHelpers#create.payment_method_data](https://docs.stripe.com/api/confirmation_tokens/test_create#test_create-payment_method_data)
-
[Mandate.payment_method_details](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details)
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
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
-
[SetupAttempt.payment_method_details](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details)
-
[SetupIntent#confirm.payment_method_data](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_data)
-
[SetupIntent#create.payment_method_data](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_data)
-
[SetupIntent#update.payment_method_data](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_data)
- [PaymentMethod#update](https://docs.stripe.com/api/payment_methods/update)
-
[Account#create.capabilities](https://docs.stripe.com/api/accounts/create#create_account-capabilities)
-
[Account#update.capabilities](https://docs.stripe.com/api/accounts/update#update_account-capabilities)
-
[Account.capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
-
[Checkout.Session#create.payment_method_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options)
-
[Checkout.Session.payment_method_options](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options)
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
-
[ConfirmationToken.payment_method_preview.type](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview-type)
-
[PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
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
- [Adds support for Alma in
France](https://docs.stripe.com/changelog/acacia/2024-10-28/alma)