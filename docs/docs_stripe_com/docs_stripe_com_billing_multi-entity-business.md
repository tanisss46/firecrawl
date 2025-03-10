# Billing for a multi-entity business

## Integrate Stripe Billing for a business with more than one legal entity.

Stripe requires you to have a separate account for each legal entity. Businesses
might need to create different legal entities to accommodate international
operations, set up financial isolation for different business units, or handle
acquisitions. Use this guide to learn how to set up multiple Stripe accounts for
a business that has multiple legal entities.

## Multiple entities architecture

To manage multiple legal entities in a scalable way, we recommend using Stripe
Connect with a [Standard
account](https://docs.stripe.com/connect/standard-accounts), where you have a
platform account that serves as a single entry point, and multiple connected
accounts for each line of business.

![Organization with multiple accounts setup using
Connect](https://b.stripecdn.com/docs-statics-srv/assets/structure_4_before.e35e09f6d8127fb01f240a30834b99b7.png)

A platform account and multiple connected accounts, each representing different
business lines.

With this account configuration, each account can maintain its own customers,
subscriptions, and product catalog. The platform account provides a single
integration point and a single, shared API key that you can use to manage
multiple connected Stripe accounts.

Platform
US Account

EUR Account

Connected accountConnected accountCustomerCustomerBankBank
US product catalog

[Product object](https://docs.stripe.com/api/products/object)

EUR customer

[Customer object](https://docs.stripe.com/api/customers/object)

EUR product catalog

[Product object](https://docs.stripe.com/api/products/object)

US customer

[Customer object](https://docs.stripe.com/api/customers/object)

PayoutPayoutDirect chargesDirect chargesStandard account with Connect 
You create a service on your app to route customers to the right account when
they check out. On the backend, your integration passes in the correct account
ID to make a direct charge for the relevant Standard account, which settles
funds to that entity’s bank account.

## Metrics and analytics

To get a consolidated view of metrics for multiple Stripe accounts, use the
Stripe Data Pipeline to [sync your Stripe account with an external
system](https://docs.stripe.com/stripe-data/access-data-in-warehouse). You can
export the data for all your accounts to your data warehouse, where you can
apply analytic tools to get business insights.

## Accounting reports

Use [Revenue Recognition](https://docs.stripe.com/revenue-recognition) to export
and consolidate accounting reports. You can also import data into a single
account and get a comprehensive view that way.

## Product catalog

Your product catalog can be part of the platform account or each connected
Standard account. Where you maintain your catalog depends on your business
needs. For example, a company that operates in the US and in the EU likely wants
to keep the catalog with the connected accounts to help them maintain local
prices. A company with a global website that serves customers in multiple
currencies likely wants to keep the catalog with the platform account and use
multi-currency prices.

### Lookup keys

To efficiently manage product catalogs for connected accounts, use [lookup
keys](https://docs.stripe.com/products-prices/manage-prices?dashboard-or-api=api#lookup-keys).
Product IDs and lookup key names only need to be unique for each account.

## Entitlements

To correctly associate a customer with a Stripe account, store the customer ID
and Stripe account ID in your database so that when you check the statuses of
invoices and subscriptions for entitlements, you know you’re referencing the
correct Stripe account.

## Tax

If you want to report taxes as a single entity for two Stripe accounts, you can
merge the tax reports of those accounts. Export the data then combine the
reports in a spreadsheet or with a partner such as TaxJar or Avalara.

## Revenue recovery

To enable [revenue recovery](https://docs.stripe.com/billing/revenue-recovery),
configure invoice templates, subscription lifecycles, and dunning emails for
each individual Stripe account.

## Payment methods

To correctly associate a customer with a Stripe account, store the customer ID
and Stripe account ID in your database. Doing so means that when you check the
statuses of invoices and subscriptions for entitlements, you know you’re
referencing the correct Stripe account.

To transition to multiple Stripe accounts, we recommend setting up a platform
account and a connected account when you first get started.

### Limitations

Payment method cloning currently has the following limitations:

- You can only clone payment methods that have the
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
set to `card` or `us_bank_account`.
- You can’t clone payment methods from one connected account to another
connected account.
- You can’t clone payment methods from a connected account to a platform
account.

## Links

- [Standard account](https://docs.stripe.com/connect/standard-accounts)
- [Product object](https://docs.stripe.com/api/products/object)
- [Customer object](https://docs.stripe.com/api/customers/object)
- [sync your Stripe account with an external
system](https://docs.stripe.com/stripe-data/access-data-in-warehouse)
- [Revenue Recognition](https://docs.stripe.com/revenue-recognition)
- [lookup
keys](https://docs.stripe.com/products-prices/manage-prices?dashboard-or-api=api#lookup-keys)
- [revenue recovery](https://docs.stripe.com/billing/revenue-recovery)
-
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)