# Financial Connections fundamentals

## Learn how Financial Connections works.

The Stripe Financial Connections product has two main components: end user bank
account collection through the authentication flow, and data retrieval on the
collected accounts. There are a [number of
ways](https://docs.stripe.com/financial-connections/use-cases) to integrate
Financial Connections. In the following example, we assume you’re using a
[Financial Connections
Session](https://docs.stripe.com/api/financial_connections/sessions). However,
the overall concepts and flow diagrams function similarly with payments
integrations such as Setup or Payment Intents.

To initialize and complete the Financial Connections authentication flow:

- Your user initiates the bank account linking process on your client.
- Create a Financial Connections Session on your server to drive the
authentication flow.
- Return the session’s `client_secret` to your client.
- Initiate the authentication flow using
[collectFinancialConnectionsAccounts](https://docs.stripe.com/js/financial_connections/collect_financial_connections_accounts).
- Your user completes the flow, which attaches
[accounts](https://docs.stripe.com/api/financial_connections/accounts) to the
session.

Client

Server

Stripe

Initiate account linking

Create session

Session

Session `client_secret`

User completes account linking

Retrieve accounts from session

Accounts

An overview of the Financial Connections authentication flow
After you have your user’s authenticated accounts, you can initiate data
refreshes from your server. When the refreshes are complete, you can retrieve
the account data.

## Authentication flow

The authentication flow is the client-side UI that allows your user to consent
to data sharing and link their financial accounts to you and Stripe.

Embed the UI in your client-side user flow. It works across all major browsers
and platforms, including web, iOS, Android, and mobile web views.

![Authentication
Flow](https://b.stripecdn.com/docs-statics-srv/assets/canonical-flow-v3.e0b5244b9d16ed2e03e6ed656e5ab1df.png)

Your user follows these steps during the authentication flow:

StepDescriptionGive consentUsers consent to share requested data.Select
institutionUsers select their bank either from frequently chosen banks or by
searching over more than 5,000 other supported banks.Log into bankUsers
authenticate access to their accounts by logging into their bank.Select
accountsUsers select which specific accounts to link.SuccessUsers see a success
screen after authentication completes successfully.
For payments integrations such as Setup Intents, you can configure the
authentication flow to use microdeposits as a fallback using the
[verification_method](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-verification_method)
parameter.

### Return user optimization

Financial Connections enables your users to connect their accounts in fewer
steps with
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses),
allowing them to save and quickly reuse their bank account details across Stripe
businesses.

![Authentication
Flow](https://b.stripecdn.com/docs-statics-srv/assets/return-user-flow-v3.5a17b62098a2cfb95d42bfe37f641d1e.png)

For return users, launch the Financial Connections authentication flow with a
[Customer](https://docs.stripe.com/api/customers) that has an email address. See
our [use case guide](https://docs.stripe.com/financial-connections/use-cases)
for examples of how to do this for your specific use case.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d email={{CUSTOMER_EMAIL}}
```

## How Stripe links financial accounts

During the authentication flow, your user logs into their bank through either an
OAuth (bank-hosted) or non-OAuth flow to authenticate access to their accounts.
Stripe typically defaults the authentication flow to OAuth if it’s available at
the financial institution. Your integration doesn’t need to treat OAuth accounts
differently than non-OAuth accounts.

OAuth is a standardized protocol that allows users to grant applications (for
example, Stripe) access to their information within other applications (for
example, bank apps). This protocol eliminates the need for users to share their
login credentials.

Here’s how OAuth and Financial Connections function together:

- When your user selects their bank in the Financial Connections authentication
flow, they’re sent to their bank’s website or mobile app.
- Your user logs into their bank and grants the bank permission to share account
data (such as balances or transactions) with Stripe.
- The bank redirects your user back to the authentication flow, passing a token
that allows Stripe access to approved bank account information.
- Your user never shares their login credentials with Stripe.

In non-OAuth flows, end users provide credentials directly to Stripe or one of
our [trusted
partners](https://support.stripe.com/questions/what-is-the-relationship-between-stripe-and-stripe-s-service-providers).

## Financial Connections Account

Successful completion of the authentication flow creates one [Financial
Connections
Account](https://docs.stripe.com/api/financial_connections/accounts/object) for
each account authorized by your user. The Financial Connections Account is the
API object you use to access additional account data, such as balances and
transactions. They represent external financial accounts such as checking,
savings, loan, or credit card accounts. See the
[account_subcategory](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-subcategory)
field on the account for a list of all account types we support. Only cash-based
accounts, such as checking and savings accounts, allow ACH (Automated Clearing
House) transfers.

## Data permissions

After collecting an account, you immediately receive access to the following
information:

- Last four digits of the account number
- Account category such as checking or savings
- Account nickname, if available

To access additional account data such as balances or transactions, you must
request access with data permissions. You configure data permissions on
server-side objects such as the Financial Connections Session using the
[permissions](https://docs.stripe.com/api/financial_connections/sessions/create#financial_connections_create_session-permissions)
parameter.

Data AvailablePermissionsDescriptionAccount details`payment_method`Tokenized
account and routing number (required for money movement)Account
owners`ownership`Account owner names and mailing
addressesBalances`balances`Current and available
balancesTransactions`transactions`Pending and posted transactions
Consider the data required to fulfill your use case and request permission to
access only the data you need. Requesting permissions that go well beyond your
application’s scope may erode your users’ trust in how you use their data. For
example, if you’re building a personal financial management application or a
lending product, you might request `transactions` data. If you’re mitigating
fraud such as account takeovers, you might want to request `ownership` details.

During the authentication flow, your users can see the data types that you’ve
requested access to. They must provide their consent to share this data. To
expand the data types you have access to, your user needs to complete the
authentication flow again with the new data permissions.

Consult the [balances
integration](https://docs.stripe.com/financial-connections/balances) guide for
an example of how to access financial account data, or learn more about [use
cases](https://docs.stripe.com/financial-connections/use-cases) for the
different data types.

## Links

- [number of ways](https://docs.stripe.com/financial-connections/use-cases)
- [Financial Connections
Session](https://docs.stripe.com/api/financial_connections/sessions)
-
[collectFinancialConnectionsAccounts](https://docs.stripe.com/js/financial_connections/collect_financial_connections_accounts)
- [accounts](https://docs.stripe.com/api/financial_connections/accounts)
-
[verification_method](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-verification_method)
-
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)
- [Customer](https://docs.stripe.com/api/customers)
- [trusted
partners](https://support.stripe.com/questions/what-is-the-relationship-between-stripe-and-stripe-s-service-providers)
- [Financial Connections
Account](https://docs.stripe.com/api/financial_connections/accounts/object)
-
[account_subcategory](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-subcategory)
-
[permissions](https://docs.stripe.com/api/financial_connections/sessions/create#financial_connections_create_session-permissions)
- [balances integration](https://docs.stripe.com/financial-connections/balances)