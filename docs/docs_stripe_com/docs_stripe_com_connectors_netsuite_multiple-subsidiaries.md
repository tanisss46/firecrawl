# Multiple NetSuite subsidiaries

## Learn how the Stripe Connector for NetSuite supports multiple NetSuite subsidiaries with multiple Stripe accounts.

If your business has multiple subsidiaries or charges customers in multiple
currencies, the Stripe Connector for NetSuite can handle currency conversion and
bank reconciliation for you. For example, the connector supports the following
configurations:

- One Stripe account with one settlement currency
- One Stripe account with multiple settlement currencies
- Multiple Stripe accounts with multiple NetSuite subsidiaries
- Multiple Stripe accounts with one subsidiary

You can’t use one Stripe account with multiple NetSuite subsidiaries.

## When to use multiple Stripe accounts

The connector supports syncing multiple Stripe accounts to one NetSuite
subsidiary. Whether or not you use multiple Stripe accounts depends on your
integration and other considerations. Review the guidelines below and consult
with your implementation partner to understand all accounting and technical
implications.

#### Note

How you structure Stripe accounts and NetSuite subsidiaries can have tax or
legal implications. The information below isn’t official legal or tax advice.
Consult legal counsel for advice about your particular situation.

### Reporting to government authorities

Stripe reports all transactions for each account to the relevant government
authority. If you have one Stripe account that you use for transactions across
multiple subsidiaries, Stripe reports all of the transactions in that account as
if they came from a single entity. You can’t split transactions from one Stripe
account to multiple legal entities.

### Multiple NetSuite subsidiaries

We recommend associating each Stripe account with a different NetSuite
subsidiary. If you use multiple subsidiaries in NetSuite and transact on each
subsidiary, you must have a separate Stripe account for each subsidiary.

### Separate configurations

You can decide how you want to grant access to certain Stripe data by creating
multiple Stripe accounts and separating the data as needed. Customer support and
finance teams won’t have access to multiple accounts.

The connector configuration for each account is different. For example, each
account might belong to a different department or use a different workflow.

You must deposit revenue in different bank accounts, depending on the site or
app where the user made the purchase.

## When not to use multiple Stripe accounts

You might not need to use multiple Stripe accounts in the following cases:

- Your connector configuration is mostly similar for your accounts. For example,
they’re e-commerce accounts and post to the same department, class, or
subsidiary.
- You don’t need to restrict access to certain Stripe data.
- You want separate API keys for multiple sites or components of an application.
- You want to share saved payment methods between the sites and applications
that use Stripe.

## Configure the connector to use multiple Stripe accounts

The connector supports using one Stripe account per NetSuite subsidiary, by
default. If necessary, you can configure the connector to use multiple Stripe
accounts. To do so, you can implement business logic that switches the Stripe
account used in your various systems. In addition to your e-commerce application
(if applicable), you must also update these key connector workflows to specify
which Stripe account to use:

- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)

## Test multiple subsidiaries

The connector supports testing multiple Stripe accounts with multiple NetSuite
subsidiaries. Consult with your implementation partner to get started.

## Links

- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)