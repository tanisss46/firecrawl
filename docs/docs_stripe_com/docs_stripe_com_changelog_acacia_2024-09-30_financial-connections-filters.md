# Adds support for filtering by account subcategories on Financial Connections

## What’s new

Adds support for filtering Financial Connections Accounts by subcategory across
several Payment APIs: Checkout, Invoice, PaymentIntent, SetupIntent, and
Subscription. The supported values are `checking` and `savings`.

## Impact

This is net new opt-in functionality for advanced users who want to limit
allowed Financial Connections Accounts to either checking or savings accounts.
There is no impact unless you adopt the functionality.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsfiltersAdded[Checkout.Session.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-us_bank_account-financial_connections)[Invoice#create.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_options-us_bank_account-financial_connections)[Invoice#update.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/invoices/update#update_invoice-payment_settings-payment_method_options-us_bank_account-financial_connections)
+ 12 more
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

- [Expands filtering support for Financial Connections
Sessions](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-additional-filters)

## Links

-
[Checkout.Session.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-us_bank_account-financial_connections)
-
[Invoice#create.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_options-us_bank_account-financial_connections)
-
[Invoice#update.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/invoices/update#update_invoice-payment_settings-payment_method_options-us_bank_account-financial_connections)
-
[Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_options-us_bank_account-financial_connections)
-
[PaymentIntent#confirm.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-us_bank_account-financial_connections)
-
[PaymentIntent#create.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-us_bank_account-financial_connections)
-
[PaymentIntent#update.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-payment_method_options-us_bank_account-financial_connections)
-
[PaymentIntent.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-us_bank_account-financial_connections)
-
[SetupIntent#confirm.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-us_bank_account-financial_connections)
-
[SetupIntent#create.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-financial_connections)
-
[SetupIntent#update.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/setup_intents/update#update_setup_intent-payment_method_options-us_bank_account-financial_connections)
-
[SetupIntent.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options-us_bank_account-financial_connections)
-
[Subscription#create.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-us_bank_account-financial_connections)
-
[Subscription#update.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/subscriptions/update#update_subscription-payment_settings-payment_method_options-us_bank_account-financial_connections)
-
[Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-payment_method_options-us_bank_account-financial_connections)
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
- [Expands filtering support for Financial Connections
Sessions](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-additional-filters)