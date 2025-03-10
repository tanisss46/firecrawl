# Collect a bank account to optimize ACH Direct Debit payments with account data

## Use account data such as balances to optimize your payments integration.

Stripe offers a number of ways to accept ACH Direct Debit payments from your
users. All of these methods require that you
[verify](https://docs.stripe.com/payments/ach-direct-debit#verification) the
user’s account before you can debit their account. Financial Connections is the
secure method offered by Stripe to perform instant bank account verification,
that’s also extensible to more powerful features such as balance or ownership
checks. When using Financial Connections to power your ACH flows, you can:

- Reduce payment failure rate from closed or inactive accounts
- Improve payments conversion by keeping users on session, instead of forcing
them to leave your payments flow to locate their account and routing numbers
- Save development time by eliminating the need to create a custom bank account
collection form
- Enable the collection of additional bank account data, such as balances and
ownership information, to further optimize your integration

## Before you begin

Financial Connections is the default verification method for all hosted ACH
payment flows, such as Checkout or the Payment Element. If you use a hosted
flow, skip directly to [accessing additional account
data](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#access).
If you’re not already set up to collect ACH payments, [set that
up](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?platform=web&ui=stripe-hosted)
first.

[Enable Financial
Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#enable)
The `verification_method` parameter on various API resources controls whether
Financial Connections is enabled for bank account verification. Financial
Connections with microdeposit fallback is the default.

#### Common mistake

Bank accounts that your customers link through manual entry and microdeposits
won’t have access to additional bank account data like balances, ownership, and
transactions.

Verification methodDescription`automatic` (default)Financial Connections with
the option to manually enter bank account information and use
microdeposits`instant`Financial Connections only, with no manual entry +
microdeposit fallback`microdeposits`Manual entry and microdeposits only
This option is available on the following APIs:

-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-us_bank_account-verification_method)
-
[SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-verification_method)
-
[CheckoutSession](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-us_bank_account-verification_method)
-
[Invoice](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_options-us_bank_account-verification_method)
-
[Subscription](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-us_bank_account-verification_method)
- [Payment
Element](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method)
[Create a
customerRecommended](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#customer)
We recommend that you create a [Customer](https://docs.stripe.com/api/customers)
with an email address to represent your user, that you then attach to your
payment. Attaching a Customer object allows you to [list previously linked
accounts](https://docs.stripe.com/api/financial_connections/accounts/list)
later. By providing an email address on the Customer object, Financial
Connections can improve the authentication flow by streamlining sign-in or
sign-up for your user, depending on whether they’re a returning
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)
user.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d email={{CUSTOMER_EMAIL}}
```

[Request access to additional account
data](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#access)
To access additional account data on Financial Connections Accounts, first make
sure you’ve submitted your Financial Connections application by checking
[Financial Connections settings in the
Dashboard](https://dashboard.stripe.com/settings/financial-connections). To view
this page, activate your account. How you configure which types of account data
you have access to depends on your integration.

Dynamic payment methodsPayment method types
If you use Stripe’s [dynamic payment method
feature](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
to collect ACH payments for non-Connect use cases, you can configure requested
Financial Connections data directly from the [ACH Dashboard settings
page](https://dashboard.stripe.com/test/settings/payment_methods). Account and
routing number is always required for ACH debits; other data types are optional.

#### Note

We recommend configuring permissions in the Dashboard because it allows you to
change which data you collect without any code changes.

To override the Dashboard configuration, specify Financial Connections
permissions directly in the API. To do this for PaymentIntents:

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2000 \
 -d currency=usd \
 -d customer={{CUSTOMER_ID}} \
 -d "automatic_payment_methods[enabled]"=true \
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method
\
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=balances
\
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership
\
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=transactions
```

[Use data to optimize ACH
integration](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#optimize)
After you have been approved for additional bank account data access like
balances or ownership, you can use this data to optimize ACH payments
performance. For example, you can use balance data to reduce the risk of
insufficient funds failures. See related data guides for examples:

- [Balances](https://docs.stripe.com/financial-connections/balances): check
account balance prior to payment initiation to reduce NSFs.
- [Ownership](https://docs.stripe.com/financial-connections/ownership): pull
account owners and compare against your internal data models to catch potential
fraud.
- [Transactions](https://docs.stripe.com/financial-connections/transactions):
pull an account’s transaction history to check when the customer’s paycheck
might land.

### Finding the Financial Connections Account ID

To initiate data refreshes and retrieve data on a Financial Connections Account,
you first need to get the account’s ID from the linked Payment Method by
expanding the Payment Intent’s `payment_method` property:

```
curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=payment_method
```

The Financial Connections Account ID is on the expanded Payment Method’s
[us_bank_account
hash](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account).
If you allow [manual entry
fallback](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#enable)
and the user manually entered their account information, this field is `null`.

```
{
 "id": "pi_3OK3g4FitzZY8Nvm11121Lhb",
 "object": "payment_intent",
 "payment_method": {
 "us_bank_account": {
 "financial_connections_account": "fca_1OK123bitUAA8SvmruWkck76"
 }
 // ... other fields on the Payment Method
 }
 // ... other fields on the Payment Intent
}
```

## Links

- [overview of integration
options](https://docs.stripe.com/financial-connections/use-cases)
- [verify](https://docs.stripe.com/payments/ach-direct-debit#verification)
- [set that
up](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?platform=web&ui=stripe-hosted)
- [this section of the ACH
guide](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?platform=web&ui=direct-api#web-collect-details)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-us_bank_account-verification_method)
-
[SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-verification_method)
-
[CheckoutSession](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-us_bank_account-verification_method)
-
[Invoice](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_options-us_bank_account-verification_method)
-
[Subscription](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-us_bank_account-verification_method)
- [Payment
Element](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method)
- [Customer](https://docs.stripe.com/api/customers)
- [list previously linked
accounts](https://docs.stripe.com/api/financial_connections/accounts/list)
-
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)
- [Financial Connections settings in the
Dashboard](https://dashboard.stripe.com/settings/financial-connections)
- [dynamic payment method
feature](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [ACH Dashboard settings
page](https://dashboard.stripe.com/test/settings/payment_methods)
- [Balances](https://docs.stripe.com/financial-connections/balances)
- [Ownership](https://docs.stripe.com/financial-connections/ownership)
- [Transactions](https://docs.stripe.com/financial-connections/transactions)
- [us_bank_account
hash](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account)
- [manual entry
fallback](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#enable)