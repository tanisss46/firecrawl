# Query connected account data

## Use Sigma and Data Pipeline to retrieve connected account information.

[Connect](https://docs.stripe.com/connect) platforms can report on their
connected accounts using Sigma or Data Pipeline. You can write queries that run
across your entire platform in much the same way as your own Stripe account.

Additional groups of Connect-specific tables within the schema are located in
the **Connect** sections of the schema. If you don’t operate a Connect platform,
these tables are not displayed.

## Connected account information

The `connected_accounts` table provides a list of
[Account](https://docs.stripe.com/api#account_object) objects with information
about connected accounts. This table is used for account-level information
across all accounts on your platform, such as [business
name](https://docs.stripe.com/api#account_object-business_name),
[country](https://docs.stripe.com/api#account_object-country), or the user’s
[email address](https://docs.stripe.com/api#account_object-email).

The following example uses the `connected_accounts` table to retrieve a list of
five accounts for individuals located in the US that have
[payouts](https://docs.stripe.com/payouts) disabled because Stripe does not have
the [required verification
information](https://docs.stripe.com/connect/required-verification-information)
to [verify their
account](https://docs.stripe.com/connect/identity-verification).

```
select
 id,
 email,
 legal_entity_address_city as city,
 legal_entity_address_line1 as line1,
 legal_entity_address_postal_code as zip,
 legal_entity_address_state as state,
 legal_entity_dob_day as dob_day,
 legal_entity_dob_month as dob_month,
 legal_entity_dob_year as dob_year,
```

See all 22 lines
All the required fields for individual accounts in the US are retrieved as
columns. This allows you to see what information has been provided, and what is
needed, for each account. This can be seen in the example report below (some
columns have been omitted for brevity).

idemailcity…id_provideddocument_idacct_jMqdyEw…jenny.rosen@example.comSan
Francisco…truefile_TJYhXYr…acct_heBfRXR…sophia.garcia@example.com…falsefile_fGziLJb…acct_dx84KB7…natalie.davis@example.comSeattle…truefile_2x61pZo…acct_V2xUyzd…ella.thompson@example.comAustin…falsefile_WPtYIRT…acct_SU5NhuU…james.smith@example.com…falsefile_KYXhOHu…
## Accounts with requirements

The `connected_accounts` table also contains information about the
`requirements` and `future_requirements` for connected accounts. Use the table
to retrieve lists of accounts that have requirements currently due and will be
disabled soon. Use the `future_requirements` columns to [handle verification
updates](https://docs.stripe.com/connect/handle-verification-updates).

The following example uses the `connected_accounts` table to retrieve a list of
accounts that have upcoming verification updates.

```
select
 id,
 business_name,
 requirements_currently_due,
 future_requirements_currently_due
from
 connected_accounts
where
 future_requirements_currently_due != ''
```

The `requirements_past_due`, `requirements_currently_due`,
`requirements_eventually_due`, `future_requirements_past_due`,
`future_requirements_currently_due`, and `future_requirements_eventually_due`
are comma-separated lists of requirements on the account.

idbusiness_namerequirements_currently_duefuture_requirements_currently_dueacct_1JLOXTr65xL6wmw6RocketRidesbusiness_profile.urlacct_1hxFexyxvT84ZvdCKavholmindividual.email,settings.payments.statement_descriptoracct_1zEjBGteqUk5H1fgFurEverexternal_accountsettings.payments.statement_descriptoracct_14MlH11Khlv6x67MPashabusiness_profile.urlcompany.tax_id
## Transactional data for connected accounts

[Transactional](https://docs.stripe.com/stripe-data/query-transactions) and
[subscription](https://docs.stripe.com/stripe-data/query-billing-data) data for
connected accounts is contained within the `connected_account_` tables. The
available data for connected accounts is organized and structured in the same
way as data for your own account.

For instance, the `balance_transactions` table, located in the **Payments**
section, contains balance transaction data for your Stripe account. The
`connected_account_balance_transactions` table, located in the **Connect -
Payments** section, contains balance transaction data for your connected
accounts. Each Connect-specific table has an additional `account` column
containing the identifier of a connected account. This can be used when joining
tables to build advanced queries.

The following example is based upon the default query that’s loaded into the
editor. Instead of retrieving the ten most recent balance transactions on your
account, it does so across all of your platform’s connected accounts.

```
select
 date_format(created, '%m-%d-%Y') as day,
 account, -- Added to include corresponding account identifier
 id,
 amount,
 currency,
 source_id,
 type
from connected_account_balance_transactions -- Changed to use Connect-specific
table
 order by day desc
 limit 5
```

dayaccountidamountcurrencysource_idtype3/9/2025acct_Vw3EDvu…txn_ScuEGOM…-1,000usdre_GdqbgRN…refund3/9/2025acct_Yq2BSIO…txn_fDzCh4D…1,000usdch_YVvJgfj…charge3/9/2025acct_ybODP21…txn_c6V3Udj…1,000usdch_IkhpbTv…charge3/9/2025acct_nBu71YE…txn_v1ck5Wc…1,000eurch_K2o0BPL…charge3/9/2025acct_Twta3HX…txn_hpGyffj…-1,000usdre_O4PoWkI…refund
Refer to our
[transactions](https://docs.stripe.com/stripe-data/query-transactions) and
[subscriptions](https://docs.stripe.com/stripe-data/query-billing-data)
documentation to learn more about querying transactional and subscription data.
You can then supplement or adapt your queries with Connect-specific information
to report on connected accounts.

### Query charges on connected accounts

Use Sigma or Data Pipeline to report on the flow of funds to your connected
accounts. How you do this depends on your platform’s approach to creating
charges.

## Direct charges

If your platform creates [direct
charges](https://docs.stripe.com/connect/direct-charges) on a connected account,
they appear on the connected account, not on your platform. This is analogous to
a connected account making a charge request itself. Platforms can use the
Connect-specific tables (for example, `connected_account_charges` or
`connected_account_balance_transactions`) to report on direct charges.

Access the [direct charges query
template](https://dashboard.stripe.com/sigma/queries/templates/Direct%20charges)
to retrieve itemized information about application fees earned through direct
charges, and reports on the connected account, transfer, and payment that is
created.

## Destination charges

If your platform creates [destination
charges](https://docs.stripe.com/connect/destination-charges) on behalf of
connected accounts, charge information is available within your own account’s
data. A separate transfer of the funds to the connected account is automatically
created, which creates a payment on that account. For example, the [destination
charges query
template](https://dashboard.stripe.com/sigma/queries/templates/Destination%20charges)
reports on transfers related to destination charges made by your platform. One
way to analyze the flow of funds from a destination charge to a connected
account is by joining the `transfer_id` column of the `charges` table to the
`id` column of the `transfers` table. This example includes the original charge
identifier and amount, the amount transferred to the connected account, and the
connected account’s identifiers and resulting payment.

```
select
 date_format(date_trunc('day', charges.created), '%y-%m-%d') as day,
 charges.id,
 charges.amount as charge_amount,
 transfers.amount as transferred_amount,
 transfers.destination_id
from charges
inner join transfers
 on transfers.id=charges.transfer_id
order by day desc
limit 5
```

dayidcharge_amounttransferred_amountdestination_id3/9/2025ch_acct_bwKf2jd…1,0001,000acct_Ia0jwSN…3/9/2025ch_acct_F284nt4…800800acct_UqQtSr8…3/9/2025ch_acct_jz6C5D3…1,000800acct_TRdjkdU…3/9/2025ch_acct_ObTBQkd…1,100950acct_uustuMj…3/9/2025ch_acct_XAxnpCR…1,1001,100acct_vub3PlU…
Payment and transfer information for Connected accounts is also available within
Connect-specific tables (for example, `connected_account_charges`).

### Separate charges and transfers

Report on [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) using
a similar approach to destination charges. All charges are created on your
platform’s account, with funds separately transferred to connected accounts
using [transfer
groups](https://docs.stripe.com/connect/separate-charges-and-transfers). A
payment is created on the connected account that references the transfer and
transfer group.

Both the `charges` and `transfers` table include a `transfer_group` column.
Payment, transfer, and transfer group information is available within the
Connect-specific `connected_account_charges` table.

## Links

- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-standard-accounts)
- [Connect](https://docs.stripe.com/connect)
- [Account](https://docs.stripe.com/api#account_object)
- [business name](https://docs.stripe.com/api#account_object-business_name)
- [country](https://docs.stripe.com/api#account_object-country)
- [email address](https://docs.stripe.com/api#account_object-email)
- [payouts](https://docs.stripe.com/payouts)
- [required verification
information](https://docs.stripe.com/connect/required-verification-information)
- [verify their account](https://docs.stripe.com/connect/identity-verification)
- [handle verification
updates](https://docs.stripe.com/connect/handle-verification-updates)
- [query templates](https://dashboard.stripe.com/sigma/queries/templates)
- [Transactional](https://docs.stripe.com/stripe-data/query-transactions)
- [subscription](https://docs.stripe.com/stripe-data/query-billing-data)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [direct charges query
template](https://dashboard.stripe.com/sigma/queries/templates/Direct%20charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [destination charges query
template](https://dashboard.stripe.com/sigma/queries/templates/Destination%20charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)