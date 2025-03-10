# View all accounts

## Learn how to view all of your connected accounts, and filter them by verification status, balance, volume, and other attributes.

The [accounts overview](https://dashboard.stripe.com/connect/accounts/overview)
page provides multiple ways to view your connected accounts. By default, the
**All accounts** tab is selected. However, the other tabs organize accounts
according to their status. Each tab includes the number of accounts with that
status. When you select a tab, the results in your accounts list update
automatically. You can then narrow these results further by using the filter
feature on each tab.

## Status tabs and workflows

Selecting different status tabs on the account overview page automatically
updates the filters and columns displayed. The interactive table below provides
an overview and description of the columns associated with each tab. You can
sort many of the columns listed below can also by clicking on the column heading
in the Dashboard.

All accountsRestrictedRestricted soonPendingEnabledComplete
This tab is displayed by default, and is commonly used to see a high-level view
of all your connected accounts.

Column DescriptionAccountsThe name of the account.StatusThe [account
status](https://docs.stripe.com/connect/dashboard#status-badges).BalanceThe
total of pending and available balances, converted to your platform’s default
currency.VolumeThe total gross volume on the account, converted to your
platform’s default currency. This is only displayed for connected accounts that
don’t have access to the full Stripe Dashboard (including Custom and Express
accounts) and connected accounts with [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts).TypeAccount
type (Standard, Express, Custom, or
[None](https://docs.stripe.com/connect/migrate-to-controller-properties)).Country
(icon)An icon representing the account’s country.ConnectedThe date the account
connected to your platform.
## Filters

Each tab provides a list of accounts based on a shared status, but you can use
filters to narrow the results further. When you apply a new filter, the account
list updates automatically.

![screenshot of sample
filter](https://b.stripecdn.com/docs-statics-srv/assets/filters.09676e78aad7739ba40cc52c335c523e.png)

Filter accounts by country

## Links

- [accounts overview](https://dashboard.stripe.com/connect/accounts/overview)
- [account status](https://docs.stripe.com/connect/dashboard#status-badges)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [None](https://docs.stripe.com/connect/migrate-to-controller-properties)