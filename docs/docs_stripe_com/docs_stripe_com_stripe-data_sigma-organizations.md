# Query data across accounts belonging to an organizationPublic preview

## Use Sigma with Organizations to query multiple accounts.

If you use [Stripe
Organizations](https://docs.stripe.com/get-started/account/orgs) to unify your
business across multiple Stripe accounts, you can run Sigma queries across
multiple accounts with Sigma for Organizations. Using Sigma queries allows you
to gain insights about your customers and payments across your entire business
in the Dashboard.

## Getting started

Before you begin, complete the following steps:

- [Create an
organization](https://docs.stripe.com/get-started/account/orgs/build) and add
all the accounts you want to include in your queries.
- Enable Sigma in each account you want to include in your queries.
- Make sure that you’re assigned a role at the organization-level with
permissions to view reports (such as
[Analyst](https://docs.stripe.com/get-started/account/teams/roles)) to run and
execute Sigma queries.

## Run Sigma queries across multiple accounts

To run Sigma queries that span multiple accounts in your organization, follow
these steps:

- From the Dashboard, switch into your organization from the account picker,
then click [Sigma](https://dashboard.stripe.com/org/sigma/queries).
- Write a new query, choose from saved queries, or select from the list of
templates.
- To specify the accounts in scope of your query, click the **Run on accounts**
dropdown in the top right corner, then click **Edit business accounts**.
- Run the query across the accounts you selected.

### Return results for each account

By default, queries return results that include data across all selected
accounts. To return results for each account, you can group results by
`merchant_id`. For example, the following query returns the sum of payment
intents in the last 14 days for each account and currency:

```
select
 merchant_id,
 currency,
 sum(amount) as total_payment_volume_last_14d
from payment_intents
where created >= date_add('day', -14, current_date)
group by 1, 2
```

`merchant_id``currency``total_payment_volume_last_14d`acct_ffGTVwu5ZNBuFgkUSD4934823acct_mRW2Pj50Di0G5BFCAD2235991acct_7bpzAYf5YCFf9b6GBP1870021acct_VVDFrkS41Xkd8IMEU9008212
### Filter accounts within a query

To use the `merchant_id` field to filter results to specific accounts directly
in your query, add a `WHERE merchant_id = 'acct_id'` clause. For example, the
following query returns the total volume of payments in a specific account:

```
select
 currency,
 sum(amount) as total_payment_volume_last_14d
from payment_intents
where created >= date_add('day', -14, current_date)
AND merchant_id in (
 'acct_d8upQPPBbFtSIe1',
 'acct_1fCSEPk3waoDZox'
)
group by 1
```

`currency``total_payment_volume_last_14d`USD8833809CAD9008212

## Links

- [Stripe Organizations](https://docs.stripe.com/get-started/account/orgs)
- [Create an
organization](https://docs.stripe.com/get-started/account/orgs/build)
- [Analyst](https://docs.stripe.com/get-started/account/teams/roles)
- [Sigma](https://dashboard.stripe.com/org/sigma/queries)