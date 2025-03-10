# Access ownership details for a Financial Connections account

## Learn how to access an account's ownership details with your user's permission.

The Financial Connections API allows you to retrieve the ownership details of a
[Financial Connections
account](https://docs.stripe.com/api/financial_connections/accounts/object).
Ownership data is useful for a variety of applications, including reducing the
risk of fraud when onboarding users or underwriting.

## Before you begin

You must have a completed Financial Connections registration to access ownership
in live mode. Check your [Dashboard
settings](https://dashboard.stripe.com/settings/financial-connections) to check
the state of your registration or begin the registration process. Test mode
Financial Connections data is always available.

[Create a
customerRecommendedServer-side](https://docs.stripe.com/financial-connections/ownership#customer)
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

[Request access to an account's ownership
dataServer-side](https://docs.stripe.com/financial-connections/ownership#request-account-ownership)
You must collect an account before you can access its ownership data. To learn
more about how to collect Financial Connections Accounts, read the integration
guide most relevant to your use case (for example, [accept
payments](https://docs.stripe.com/financial-connections/ach-direct-debit-payments),
[facilitate Connect
payouts](https://docs.stripe.com/financial-connections/connect-payouts), or
[build other-data powered
products](https://docs.stripe.com/financial-connections/other-data-powered-products)).

If you use [Connect Onboarding for Custom
Accounts](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=prebuilt-web-form)
to collect Financial Connections Accounts, configure which data you want access
to in the [Dashboard](https://dashboard.stripe.com/settings/connect/custom).

If you use an API integration to collect accounts, specify the data you need
access to with the
[permissions](https://docs.stripe.com/financial-connections/fundamentals#data-permissions)
parameter. The set of requested data permissions are viewable by the user in the
[authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow).
Financial Connections Accounts are collectible through various integration
paths, and how you specify the parameter varies slightly by API.

Setup IntentsPayment IntentsSessionsCheckoutInvoicesSubscriptions
```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=us_bank_account \
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership
\
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method
```

When using dynamic payment methods for certain payments APIs, you can also
configure requested permissions in the Dashboard. Learn how to [access
additional account data on Financial Connections
accounts](https://docs.stripe.com/financial-connections/ach-direct-debit-payments?dashboard-or-api=dashboard#access).

[Initiate an ownership
refreshServer-side](https://docs.stripe.com/financial-connections/ownership#initiate-ownership-refresh)
All Financial Connections data retrievals are asynchronous. You initiate an
ownership refresh and wait for it to complete, then retrieve the results. You
can initiate ownership refreshes with the `prefetch` API parameter or the
[Refresh
API](https://docs.stripe.com/api/financial_connections/accounts/refresh).

### Prefetch ownership data

Specify whether you want to prefetch account ownership details *before* account
collection. This initiates the refresh process as soon as your user connects
their account in the [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow).
Set `prefetch` when you require ownership data for every linked account, to make
sure you receive it with minimal delay. The `prefetch` parameter is available on
all APIs that support Financial Connections.

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=us_bank_account \
-d
"payment_method_options[us_bank_account][financial_connections][prefetch][]"=ownership
\
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method
\
-d
"payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership
```

### Initiate an on-demand refresh

Use the [Refresh
API](https://docs.stripe.com/api/financial_connections/accounts/refresh) to
initiate on-demand ownership refreshes *after* account collection, and fetch
ownership information for a specific account at your convenience, allowing you
to defer the decision until a later time. Although account ownership data can
change, it generally doesn’t change as frequently as
[balance](https://docs.stripe.com/financial-connections/balances) or
[transaction](https://docs.stripe.com/financial-connections/transactions) data.

Use the Financial Connections account ID to initiate a refresh. If you’re
integrating through a payments flow, find the account ID [on the associated
Payment
Method](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#finding-the-financial-connections-account-id).
When using a Financial Connections Session, retrieve it [through the
session](https://docs.stripe.com/financial-connections/other-data-powered-products?platform=web#collect-an-account).

```
curl
https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}/refresh
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "features[]"=ownership
```

#### Note

Refreshes aren’t allowed on inactive accounts.

### Wait for the ownership refresh to complete

The
[ownership_refresh](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-ownership_refresh)
field on a Financial Connections account represents the ownership refresh state.
This field remains `null` until you request the `ownership` permission and
initiate a refresh. After you start an ownership refresh, the state changes to
`pending`, and after completion, it moves to either `succeeded` or `failed`. We
send the
[financial_connections.account.refreshed_ownership](https://docs.stripe.com/api/events/types#event_types-financial_connections.account.refreshed_ownership)
event when the ownership refresh completes. To determine the success of the
ownership refresh, check the `ownership_refresh.status` field while handling the
webhook.

ownership_refresh: `null`

ownership_refresh.status: `pending`

ownership_refresh.status: `succeeded`

ownership_refresh.status: `failed`

financial_connections.account.refreshed_ownership

prefetchRefresh APIsuccessfailureOwnership refresh flow
After an ownership refresh completes, Stripe sets the availability of future
refreshes through the
[ownership_refresh.next_refresh_available_at](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-ownership_refresh-next_refresh_available_at)
field. Check this field before initiating a new ownership refresh to make sure
that refreshes are currently available. If you attempt a refresh while the value
is `null` (as is always the case when the refresh is pending or the account is
inactive) or the current time is less than the `next_refresh_available_at`
timestamp, the refresh won’t be initiated.

#### Private preview

In the unlikely event that a refresh fails, the `error` field on the refresh
hash is a preview feature that provides the cause of the failure and recommended
next steps. If you’d like to use it, [email
us](mailto:financial-connections-beta+refresh-error@stripe.com) for access.

[Retrieve an account's ownership
dataServer-side](https://docs.stripe.com/financial-connections/ownership#retrieve-account-ownership)
After the ownership refresh completes, retrieve the Financial Connections
account from the API and expand the
[ownership](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-ownership)
field to see ownership details.

```
curl -G https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=ownership
```

This returns the Financial Connections account with the ownership field expanded
to list the account’s owners:

```
{
 "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
 "object": "financial_connections.account",
 "ownership": {
 "id": "fcaowns_1MzTG4IG1CZuezXppfPbUpXb",
 "object": "financial_connections.account_ownership",
 "created": 1651784999,
 "owners": {
 "object": "list",
 "data": [
 {
 "name": "Jenny Rosen",
 "email": "jenny.rosen@example.com",
 "phone": "+1 555-555-5555",
 "ownership": "fcaowns_1MzTG4IG1CZuezXppfPbUpXb",
 "raw_address": "510 Townsend San Francisco, CA 94103",
 "refreshed_at": 1651784999
 }
 ],
 "has_more": false,
"url":
"/v1/financial_connections/accounts/fca_zbyrdjTrwcYZJZc6WBs6GPid/owners?ownership=fcaowns_1MzTG4IG1CZuezXppfPbUpXb"
 }
 },
 "ownership_refresh": {
 "status": "succeeded",
 "last_attempted_at": 1651784999,
 "next_refresh_available_at": 1651785000
 },
 // ...
}
```

Stripe returns the ownership information made available by a financial
institution, and the availability of ownership details varies. We return all
available fields and owners provided by the bank. Ownership details can include
account owner name, address, email, and phone number.

## Links

- [Financial Connections
account](https://docs.stripe.com/api/financial_connections/accounts/object)
- [Dashboard
settings](https://dashboard.stripe.com/settings/financial-connections)
- [Customer](https://docs.stripe.com/api/customers)
- [list previously linked
accounts](https://docs.stripe.com/api/financial_connections/accounts/list)
-
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)
- [accept
payments](https://docs.stripe.com/financial-connections/ach-direct-debit-payments)
- [facilitate Connect
payouts](https://docs.stripe.com/financial-connections/connect-payouts)
- [build other-data powered
products](https://docs.stripe.com/financial-connections/other-data-powered-products)
- [Connect Onboarding for Custom
Accounts](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=prebuilt-web-form)
- [Dashboard](https://dashboard.stripe.com/settings/connect/custom)
-
[permissions](https://docs.stripe.com/financial-connections/fundamentals#data-permissions)
- [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow)
- [access additional account data on Financial Connections
accounts](https://docs.stripe.com/financial-connections/ach-direct-debit-payments?dashboard-or-api=dashboard#access)
- [Refresh
API](https://docs.stripe.com/api/financial_connections/accounts/refresh)
- [balance](https://docs.stripe.com/financial-connections/balances)
- [transaction](https://docs.stripe.com/financial-connections/transactions)
- [on the associated Payment
Method](https://docs.stripe.com/financial-connections/ach-direct-debit-payments#finding-the-financial-connections-account-id)
- [through the
session](https://docs.stripe.com/financial-connections/other-data-powered-products?platform=web#collect-an-account)
-
[ownership_refresh](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-ownership_refresh)
-
[financial_connections.account.refreshed_ownership](https://docs.stripe.com/api/events/types#event_types-financial_connections.account.refreshed_ownership)
-
[ownership_refresh.next_refresh_available_at](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-ownership_refresh-next_refresh_available_at)
-
[ownership](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-ownership)