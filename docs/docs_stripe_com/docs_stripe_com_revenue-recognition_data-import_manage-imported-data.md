# Manage imported data

## Search for and manage existing imported data.

After you import data, you can manage it through the
[Dashboard](https://dashboard.stripe.com/revenue-recognition/data-import).

## CSV imports

After you upload a CSV, you can refresh this tab to see the status of the
import. To help you identify the import type, a **Transaction** (for general
import) or **Exclusion** (for exclusion import) tag appears before each import.

Successful imports show the number of lines imported. Click **View
transactions** or **View exclusions** to navigate to the list of imported
transactions or exclusions. Unsuccessful imports show the errors that occurred
and each line that the error occurred on.

![Data import CSV import
list](https://b.stripecdn.com/docs-statics-srv/assets/data-import-csv-import-list.897afffbbe75c6ae284aab92deb87eb3.png)

## Transactions

From the list view, you can see a paginated view of all transactions that you’ve
imported. For Stripe transactions, we provide a link to the main transaction
page in the Dashboard.

![Data import transaction
list](https://b.stripecdn.com/docs-statics-srv/assets/data-import-transaction-list.c1a3c2b2e2e9238500d5836767260cf7.png)

The column format follows the CSV format, with the addition of a status column.
An **Active** status indicates that the Revenue Recognition reports include the
imported data. A **Processing** status indicates that our system has recorded
the imported data, but revenue recognition reports don’t yet include this data.

Transactions that have been split into multiple components have a caret icon
that you can click to reveal the applicable split transactions.

![Data import transaction list with split transactions
expanded](https://b.stripecdn.com/docs-statics-srv/assets/data-import-transaction-list-expanded-split-transactions.44a4f3a52c496de09d7b90e27dee887b.png)

### Filtering

The transaction list supports filtering on all of the dates associated with the
imported data. Additionally, you can filter on **Source**, **Transaction ID**
and **Split transaction ID**, but these values must be exact matches.

### Deletion

To delete a transaction, select its checkbox and click **Delete**. It can take
up to 24 hours for Revenue Recognition reports to reflect deletions.

## Exclusions

From the list view, you can see a paginated view of all excluded transactions
that you imported. For transactions other than invoice items, we provide a link
to the main transaction page in the Dashboard.

![Data import exclusion
list](https://b.stripecdn.com/docs-statics-srv/assets/data-import-exclusion-list.601b3ad27aae399df66edfcfc36dfe94.png)

The column follows the exclusion CSV format, with the addition of a status
column. An **Active** status indicates that the transaction is excluded from
your Revenue Recognition reports. A **Processing** status indicates that our
system has recorded the transaction to be excluded, but Revenue Recognition
reports don’t yet exclude this data.

### Filtering

The exclusion list supports filtering on the ID of the excluded transactions on
exactly matched values.

### Deletion

To reverse the exclusions, select the transaction checkbox and click **Delete**.
It can take up to 24 hours for Revenue Recognition reports to reflect reversals.

## Links

- [Dashboard](https://dashboard.stripe.com/revenue-recognition/data-import)