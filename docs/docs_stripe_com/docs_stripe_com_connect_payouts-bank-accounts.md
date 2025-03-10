# Manage payout accounts for connected accounts

## Learn how to manage external bank accounts and debit cards for connected accounts

[Payout](https://docs.stripe.com/payouts) accounts can be bank accounts or debit
cards. Stripe recommends collecting external account details with the Connect
Onboarding web form, which helps you:

- Save design and development time.
- Eliminate the need to store sensitive data such as account and routing numbers
on your server.
- Eliminate the need to build form validations when users enter account details.

In the US, we also recommend using [Stripe Financial
Connections](https://docs.stripe.com/financial-connections), which lets your
users securely link their financial accounts to your business. It helps you:

- Increase onboarding conversion by preventing your accounts from having to
interrupt the process to locate their account and routing numbers.
- Reduce first payout failure rates by eliminating errors that result from
manual entry of account and routing numbers.
- Eliminate the need to store sensitive data such as account and routing numbers
on your server.
- Eliminate the need to build form validations when accounts enter account
details in custom onboarding forms.
- Enable your accounts to authenticate in fewer steps by reusing bank account
details they’ve saved to
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses).
Accounts that save their account information at any of the Stripe businesses
using Link can share their account details with your platform the next time they
use Financial Connections.
- Access additional information on an account’s external bank account, such as
[balances](https://docs.stripe.com/financial-connections/balances), [ownership
details](https://docs.stripe.com/financial-connections/ownership), and
[transactions](https://docs.stripe.com/financial-connections/transactions). You
can mitigate fraud during onboarding by verifying that information, such as the
name and address of the external bank account holder.

Financial Connections is free when you include Link. Otherwise, using it [incurs
fees](https://stripe.com/financial-connections#pricing).

Alternatively, if you use API onboarding for your connected accounts, you can
collect payout account details with a custom form in your account onboarding
flow.

### Opting out of external account collection

For accounts where the platform is responsible for collecting requirements, such
as Custom accounts, you may opt not to collect external account information in
onboarding. You may do this if, for instance, you build your own onboarding flow
where you want to collect external account information.

In embedded onboarding, you can [disable external account
collection](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding?#external-account-collection)
by setting the `external_account_collection` feature on the Account Session to
false. Alternatively, in hosted onboarding you can navigate to your [Connect
external accounts
settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts)
and then under **Accounts where the platform is responsible for collecting
requirements** enable or disable collecting external account information. Note
that this is off by default.

## Collecting external accounts

Stripe-hosted onboardingDirect API calls from a custom form
[Stripe-hosted onboarding for connected
accounts](https://docs.stripe.com/connect/custom/hosted-onboarding) uses a web
form hosted by Stripe to collect the information required to onboard connected
accounts. Stripe-hosted onboarding can collect both bank accounts and debit
cards. You can use Financial Connections with Stripe-hosted onboarding to
collect bank account details. However, you can’t use Financial Connections to
collect debit card details.

If you’re responsible for connected accounts that can’t cover negative balances,
including Custom and Express accounts, you can customize the collection flow of
external accounts in your [External
account](https://dashboard.stripe.com/settings/connect/payouts/external_accounts)
settings. These settings aren’t applicable if you’re using direct API calls from
your own form.

In your **External account** settings, you can:

- Enable or disable the collection of debit cards, by making a selection under
**Allow debit cards?**.
- Require that connected accounts must add at least one bank account before
being able to add any other type of external account, such as a debit card. You
can access this setting under **Require at least one bank account?**. This is
useful for ensuring [auto
debit](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts)
support.
- Control whether or not connected accounts to add more than one external
account in a given currency. There is a limit of five external accounts per
currency. You can access this setting under **Collect multiple external accounts
per currency**.
Use Stripe Financial ConnectionsEnable manual entry of bank account details
## Available in

United States
Stripe platforms in the US can enable [Stripe Financial
Connections](https://docs.stripe.com/financial-connections) within the
Stripe-hosted onboarding form by following these steps:

- Navigate to your [External Account
settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts),
where you manage optional Connect onboarding features.
- For connected accounts where your platform collects account information when
requirements change, including for Custom accounts, you must allow Stripe-hosted
onboarding to collect external account details. Under **Stripe-hosted onboarding
for Custom accounts**, allow Stripe to collect external account information by
turning on the toggle.
- Under **How will bank account details be collected?**, select **Financial
Connections**.
- *(Optional)* Request permission to access additional data on the accounts
instantly verified with Financial Connections, such as balances, ownership
details, and transactions. If you opt to request this additional information,
you’ll be prompted to sign up for Stripe Financial Connections.

When external account detail collection is enabled, all connected accounts are
prompted to authenticate their bank account using the Stripe-hosted modal UI
embedded within the onboarding form.

![Image showing a Connect onboarding flow using Stripe Financial Connections to
collect a payout
account.](https://b.stripecdn.com/docs-statics-srv/assets/connect-custom-onboarding-financial-connections-onboarding.8937a023f6682c90bab8c0b39873909a.png)

A Connect onboarding flow using Stripe Financial Connections to collect a payout
account.

If a connected account can’t instantly verify their bank account using Financial
Connections, the verification process automatically falls back to manual entry:

![Image showing a Connect onboarding flow using the Stripe Financial Connections
modal to collect a payout account using manual
entry.](https://b.stripecdn.com/docs-statics-srv/assets/connect-custom-onboarding-financial-connections-manual-entry.930da1e01c9026b9014008d75958bc8c.png)

A Connect onboarding flow using the Stripe Financial Connections modal to
collect a payout account using manual entry.

After onboarding, the specified bank account automatically attaches to the
connected account.

## Retrieve data on a Financial Connections account Server-side

You can determine if your user linked a Financial Connections Account by
retrieving any linked Financial Connections Accounts using their connected
account ID. Be sure to specify their account ID in the `Stripe-Account` header.

```
curl -G https://api.stripe.com/v1/financial_connections/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "account_holder[account]"={{CONNECTED_ACCOUNT_ID}}
```

This returns an API response similar to the following:

```
{
 "object": "list",
 "data": [
 {
 "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
 "object": "financial_connections.account",
 "account_holder": {
 "account": '{{CONNECTED_ACCOUNT_ID}}',
 "type": "account"
 },
 ...
 "supported_payment_method_types": [
 "us_bank_account"
 ]
 }
 ...
 ]
}
```

If any Financial Connections accounts are listed, it indicates that the
connected account linked them during the onboarding process. You can use the
`id` value to access or refresh the data you specified in your [External Account
settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts).
To protect the privacy of your connected account’s data, you can only access the
data you specified.

To start retrieving account data, follow the guides for
[balances](https://docs.stripe.com/financial-connections/balances),
[ownership](https://docs.stripe.com/financial-connections/ownership), and
[transactions](https://docs.stripe.com/financial-connections/transactions). On
all subsequent account retrieval and refresh requests, be sure to include the
`Stripe-Account` header with the connected account ID:

```
curl
https://api.stripe.com/v1/financial_connections/accounts/fca_zbyrdjTrwcYZJZc6WBs6GPid/refresh
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "features[]"=balance
```

## Links

- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [Payout](https://docs.stripe.com/payouts)
- [Stripe Financial Connections](https://docs.stripe.com/financial-connections)
-
[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)
- [balances](https://docs.stripe.com/financial-connections/balances)
- [ownership details](https://docs.stripe.com/financial-connections/ownership)
- [transactions](https://docs.stripe.com/financial-connections/transactions)
- [incurs fees](https://stripe.com/financial-connections#pricing)
- [disable external account
collection](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding?#external-account-collection)
- [Connect external accounts
settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts)
- [Stripe-hosted onboarding for connected
accounts](https://docs.stripe.com/connect/custom/hosted-onboarding)
- [auto
debit](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts)