# Stripe Treasury accounts structure

## Learn how the account components of Treasury fit together and interact.

Understanding the technical components of Stripe Treasury is important for you
to develop an optimized financial service for the sellers and service providers
on your platform. A crucial first step in that understanding is to learn the
different account types involved with a Treasury integration.

## Account types

Your platform must have Stripe [Connect](https://docs.stripe.com/connect) to use
Treasury. In its most basic form, a Connect integration includes a platform
account with many connected accounts, each owned by a seller or service provider
that uses the platform. Both the platform account and its connected accounts are
[Account](https://docs.stripe.com/api/accounts) objects in the Stripe API.

Treasury only supports connected accounts that don’t use a Stripe-hosted
dashboard and where your platform is responsible for requirements collection and
loss liability, including Custom connected accounts. Learn how to [create
connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
that work with Treasury.

#### Private preview

Enabling Treasury on non-custom connected accounts is a new feature. Email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com) to request
access.

As a platform with connected accounts, you’re responsible for maintaining a
minimum API version, communicating terms of service updates to your connected
accounts, handling information requests from them, and providing them with
support. Because your platform is ultimately responsible for the losses your
connected accounts incur, you’re also responsible for vetting them for fraud. To
learn more, read the [Treasury fraud
guide](https://docs.stripe.com/treasury/examples/fraud-guide).

![Flow chart with lines connecting a platform with three different connected
accounts.](https://b.stripecdn.com/docs-statics-srv/assets/connected-accounts.7443ee88f52a49904439afc21ded676e.png)

A Connect platform with connected accounts

Stripe Treasury introduces another type of account to the Stripe ecosystem:
financial accounts. When you onboard your platform to Treasury, Stripe
automatically creates and assigns a `FinancialAccount` object to your platform
account. As the platform, you request the `treasury` capability when requesting
the capabilities you need for your connected accounts. After you request it,
Stripe updates the connected account’s `Account` object to include additional
requirements in its [requirements
hash](https://docs.stripe.com/api/accounts/object#account_object-requirements).
You can create financial accounts for your connected accounts, but until you
gather the requirements from your connected account owners, the financial
accounts aren’t accessible. For more information on using Treasury financial
accounts, see the [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
guide.

## Account balances

Each account in Stripe Connect (both platform and connected accounts) has an
[account balance](https://docs.stripe.com/connect/account-balances) that tracks
pending and available funds for that account. With Stripe Treasury, each of
these accounts can also have a financial account, which has a balance of its
own. Treasury provides you the tools to transfer funds between the platform
account and financial account, but their respective balances always remain
separate. However, funds can’t be transferred from a platform end-user’s
financial account to their connected account. For more information on platform
and connected account balances, see the [Understanding Connect account
balances](https://docs.stripe.com/connect/account-balances) guide. For more
information on financial account balances, see the [Working with balances and
transactions](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions)
guide.

![Flow chart with a line connecting a platform account with a connected account.
For each account, two lines connect both a payments account balance and a
financial account balance. A double arrow with a dollar sign shows funds flow
between each accounts balances and a one direction arrow with a dollar sign flow
from the platform financial account balance to the connected account financial
account
balance.](https://b.stripecdn.com/docs-statics-srv/assets/fund-flow.6fb714d66e6c95a45f14066001c290bc.png)

Flow of funds between accounts

## Flow of funds between accounts

Although the payments balance and financial account balances are separate,
Treasury supports the flow of funds between the two. Treasury also enables you
to transfer funds from your platform financial account to the financial accounts
attached to your platform’s connected accounts. You can use
[Payouts](https://docs.stripe.com/api/payouts) to send funds from your payment
balance to your financial account or to the financial accounts attached to your
platform’s connected accounts. To move money between two financial accounts,
Treasury introduces
[OutboundPayment](https://docs.stripe.com/api/treasury/outbound_payments)
objects to facilitate this movement.

Transfers affect funds on the Stripe Account Balance, so if you want to move
funds between two financial accounts, you must use OutboundPayments.

## Links

- [Connect](https://docs.stripe.com/connect)
- [Account](https://docs.stripe.com/api/accounts)
- [create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
- [Treasury fraud guide](https://docs.stripe.com/treasury/examples/fraud-guide)
- [requirements
hash](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [account balance](https://docs.stripe.com/connect/account-balances)
- [Working with balances and
transactions](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions)
- [Payouts](https://docs.stripe.com/api/payouts)
- [OutboundPayment](https://docs.stripe.com/api/treasury/outbound_payments)