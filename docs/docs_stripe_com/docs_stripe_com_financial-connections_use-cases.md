# Financial Connections use cases

## View options for integrating Financial Connections and common use cases.

Financial Connections allows your users to link their financial accounts to
collect ACH payments, facilitate Connect
[payouts](https://docs.stripe.com/payouts), and build financial data products.
It also enables your users to connect their accounts in fewer steps with
[Link](https://docs.stripe.com/payments/link), allowing them to save and quickly
reuse their bank account details across Stripe merchants. View the following
integration paths based on your requirements, and some common use cases for
Financial Connections data below.

How you integrate Financial Connections depends on your desired use cases.

Use caseExampleRecommended integration[ACH Direct Debit
payments](https://docs.stripe.com/financial-connections/use-cases#ach-direct-debit)-
Bank-based payments
- Wallet transfers and top-ups
- Bill payments
An ACH payments integration:- [Setup
Intents](https://docs.stripe.com/api/setup_intents)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Invoices](https://docs.stripe.com/invoicing)
[Connect
payouts](https://docs.stripe.com/financial-connections/use-cases#custom-connect-payouts)-
Pay out funds to Connected Accounts
A Connect onboarding integration:- [Hosted
onboarding](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=prebuilt-web-form)
- [Setup
Intents](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=direct-api#create-a-setup-intent)
[Building financial
products](https://docs.stripe.com/financial-connections/use-cases#building-other-products)-
Financial management application
- Wealth management application
- Loan underwriting
[Financial Connections
Sessions](https://docs.stripe.com/api/financial_connections/sessions/object)
To process ACH payments or facilitate Connect payouts, use a recommended
payments integration in the table above, such as Setup Intents. This makes sure
that the collected accounts are compatible with [ACH
transfers](https://docs.stripe.com/payments/ach-direct-debit).

The Financial Connections Sessions API provides more flexibility for use cases
that won’t use the collected accounts for ACH payments or Connect payouts. It
has configuration options that let your users link additional [account
types](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-category)
that aren’t compatible with ACH, and you can collect multiple accounts in a
single session.

Regardless of which API you choose to integrate with, you can request access to
additional data on your users’ financial accounts. You can then use this data to
optimize your integration or create more complex products. The following
sections provide more context on the above use cases, including recommendations
on which data to access.

## ACH Direct Debit payments

In accordance with [Nacha
regulations](https://support.stripe.com/questions/nacha-bank-account-validation-rule),
you must verify a user’s account to accept an ACH Direct Debit payment or
transfer. With Financial Connections, your customer authenticates their bank
account and provides permission to share the details you need to charge their
account, such as a tokenized account and routing number.

Collecting bank account details from a customer with Financial Connections can
help you:

- Improve payment reliability by verifying that a user’s bank account is open
and able to accept ACH direct debits.
- Increase checkout conversion by eliminating the need for your customers to
leave your website or application to locate their account and routing numbers.
- Save development time by eliminating the need for you to build bank account
form validation when your customer enters account details.

To verify a bank account to accept an ACH Direct Debit payment with Financial
Connections, use Stripe’s Payment Intent or Setup Intent APIs. Alternatively,
you can use a hosted Stripe payments integration such as
[Checkout](https://docs.stripe.com/payments/checkout) or the [Payment
Element](https://docs.stripe.com/payments/payment-element).

Learn how to [collect a bank account to accept an ACH Direct Debit
payment](https://docs.stripe.com/financial-connections/ach-direct-debit-payments).

Optionally, you can request permission from your customers to retrieve
additional data on their [Financial Connections
account](https://docs.stripe.com/api/financial_connections/accounts/object). We
recommend that you access
[balances](https://docs.stripe.com/financial-connections/balances) data to
perform balance checks prior to processing the payment.

Manual account entry and microdeposit verification are available as a fallback
method for this use case. However, accounts that you add through microdeposits
won’t have access to additional account data.

## Custom Connect payouts

Use Financial Connections with Connect to verify bank accounts for Custom
connected accounts, thereby facilitating payouts. This allows your connected
account to authenticate its own bank account and provide permission to share
details you need for payouts, like tokenized account and routing numbers.

Collecting account details from your connected account with Financial
Connections can help you:

- Increase onboarding conversion by eliminating the need for your connected
account to leave your website or application to locate their account and routing
numbers.
- Reduce first payout failure rates by eliminating errors that result from
manual entry of account and routing numbers.
- Make sure you don’t need to store sensitive data such as account and routing
numbers on your server.
- Save development time by eliminating the need for you to build bank account
form validation when your connected account enters their bank account details.

Optionally, you can request permission from your connected account to retrieve
additional data on their Financial Connections account. Consider accessing
[ownership](https://docs.stripe.com/financial-connections/ownership) details to
optimize your onboarding process. Retrieving ownership data on an account can
help you mitigate fraud by verifying an account’s ownership details, such as the
name and address of the account holder.

Learn how to [collect a bank account to initiate payouts to a US Custom Connect
account](https://docs.stripe.com/financial-connections/connect-payouts).

Manual account entry and microdeposit verification are available as a fallback
method for this use case (for example, if your connected account can’t find
their institution or otherwise authenticate). However, accounts that you add
through microdeposits won’t have access to additional account data.

## Build financial products

Use Financial Connections to access external bank account data that you can use
to build financial products.

After your user has consented to share data from their financial accounts, you
can retrieve data for various use cases, such as:

- Help your user track expenses, handle bills, manage their finances and take
control of their financial well-being with
[transactions](https://docs.stripe.com/financial-connections/transactions) data.
- Speed up underwriting and improve access to credit and other financial
services with transactions and balances data.

Learn how to [collect an account to access
data](https://docs.stripe.com/financial-connections/other-data-powered-products)
using Financial Connections’ Sessions API.

Manual account entry and microdeposit verification aren’t available in the
authentication flow for this use case because the primary goal of collecting an
account is data accessibility.

You can [convert most previously linked Financial Connections accounts to
Payment
Methods](https://docs.stripe.com/financial-connections/other-data-powered-products?platform=web#accept-ach-direct-debit).
However, if your integration uses the Sessions API, the linked account might not
be compatible with ACH.

## Links

- [payouts](https://docs.stripe.com/payouts)
- [Link](https://docs.stripe.com/payments/link)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Invoices](https://docs.stripe.com/invoicing)
- [Hosted
onboarding](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=prebuilt-web-form)
- [Setup
Intents](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=direct-api#create-a-setup-intent)
- [Financial Connections
Sessions](https://docs.stripe.com/api/financial_connections/sessions/object)
- [ACH transfers](https://docs.stripe.com/payments/ach-direct-debit)
- [account
types](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-category)
- [Balances](https://docs.stripe.com/financial-connections/balances)
- [Nacha
regulations](https://support.stripe.com/questions/nacha-bank-account-validation-rule)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [collect a bank account to accept an ACH Direct Debit
payment](https://docs.stripe.com/financial-connections/ach-direct-debit-payments)
- [Financial Connections
account](https://docs.stripe.com/api/financial_connections/accounts/object)
- [Ownership](https://docs.stripe.com/financial-connections/ownership)
- [collect a bank account to initiate payouts to a US Custom Connect
account](https://docs.stripe.com/financial-connections/connect-payouts)
- [Transactions](https://docs.stripe.com/financial-connections/transactions)
- [collect an account to access
data](https://docs.stripe.com/financial-connections/other-data-powered-products)
- [convert most previously linked Financial Connections accounts to Payment
Methods](https://docs.stripe.com/financial-connections/other-data-powered-products?platform=web#accept-ach-direct-debit)