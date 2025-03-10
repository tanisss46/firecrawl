# Revenue Recognition reports

## Generate and export revenue reports using Revenue Recognition.

Revenue Recognition automatically generates reports that you can view in the
Stripe Dashboard and export as CSV files. These reports include key information
like revenue and deferred revenue. They’re available in both aggregate views for
high-level analysis, and detailed views so you can validate data.

## Integration requirements

Revenue Recognition assumes that you’ve properly modeled your business. This
includes:

- Modeling subscriptions using [products and
prices](https://docs.stripe.com/products-prices/overview), and
[customers](https://docs.stripe.com/billing/customer).
- Setting taxes using the
[default_tax_rates](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_tax_rates)
attribute, not as line items.
- Setting discounts using the
[discount](https://docs.stripe.com/api/subscriptions/object#subscription_object-discount)
object, not as [invoice](https://docs.stripe.com/api/invoices) items.

#### Caution

Revenue recognition requirements vary based on a number of factors, including
the location of your business and the goods and services that you sell. You need
to make sure that you understand and comply with the requirements applicable to
your business, and that you model your business accordingly.

## Dashboard

The Revenue Recognition section of your Dashboard provides high-level
information regarding the operations and financial health of your business. It
includes [graphs for recognized revenue and deferred
revenue](https://dashboard.stripe.com/revenue-recognition), a [monthly
summary](https://dashboard.stripe.com/revenue-recognition), and a [revenue
waterfall
report](https://dashboard.stripe.com/revenue-recognition/accounting-reports).

The Revenue Recognition section is also where you can manage your Stripe
integration, such as [uploading your revenue
data](https://dashboard.stripe.com/revenue-recognition/data-import), [defining
custom rules](https://dashboard.stripe.com/revenue-recognition/rules) on how to
treat your revenue, and [mapping to the chart of
accounts](https://docs.stripe.com/revenue-recognition/chart-of-accounts) that
you use in your general ledger.

You can download any accounting report or statement you’re viewing by clicking
**Download**. Below is a list of the different report formats available to you
for download as a CSV file:

Report formatDescriptionSummaryThis report provides a summary of revenue
recognition on your account for the selected period.ProductThis report provides
a detailed view of revenue recognition on your account over the selected period,
organized by product.PriceThis report provides a detailed view of revenue
recognition on your account over the selected period, organized by price. It can
include information such as pricing metadata and pricing intervals.CustomerThis
report provides a detailed view of revenue recognition on your account over the
selected period, organized by customer. It can include information such as
customer name, email, and address.InvoiceThis report provides a detailed view of
revenue recognition on your account over the selected period, organized by
invoice. It can include information such as charges, refunds, and dispute
IDs.Line itemThis report provides a detailed view of revenue recognition on your
account over the selected period, organized by line item. It can include
information at the granularity of a line item (such as charges, refunds, and
dispute IDs).MetadataThis report provides a customized summary of revenue
recognition on your account for the selected period, grouped by the user
selected metadata object type and key. This report supports grouping by charge,
customer, invoice, invoice item, product, or subscription metadata. Learn more
about metadata [here](https://docs.stripe.com/api/metadata).Event typeThis
report is available in the debits and credits reports. It provides a detailed
view of revenue recognition on your account over the selected period, organized
by event type. The event type provides a brief description of the recorded
event, which can help you understand the nature of each journal entry.Invoice
event typeThis report is available in the debits and credits reports. It
provides a detailed view of revenue recognition on your account over the
selected period, organized by invoice and event type. It can include information
such as charges, refunds, and dispute IDs.Line item event typeThis report is
available in the debits and credits reports. It provides a detailed view of
revenue recognition on your account over the selected period, organized by line
item and event type. It can include information at the granularity of a line
item (such as charges, refunds, and dispute IDs).
#### Caution

Revenue Recognition generates reports from transactions processed by Stripe.
Expect a 72 hour delay before the data displays in the Dashboard.

Also, all report information is accessible only after you [import the
data](https://docs.stripe.com/revenue-recognition/data-import).

### Revenue graphs

The revenue graphs in the Dashboard provide a high-level view of your business
by displaying revenue activity over time. The recognized revenue graph shows
your net recognized revenue and the deferred revenue graph shows your ending
balance per month.

The monthly and daily charts differentiate between open and closed accounting
periods using colors. The figures continue to change until the accounting period
closes. Toggling to the daily view provides a day-by-day snapshot of recognized
and deferred revenue for the selected month. Revenue from metered billing is
recognized in full when invoices finalize, or when the accounting period closes.

### AR aging graphs

The accounts receivable (AR) aging graphs in the Dashboard provide a high-level
view of your accounts receivable activity over time. Use this information to
understand the financial health of your customers. The balance graph shows the
outstanding invoice amounts for the specified periods. The summary table shows
unpaid invoice amounts and categorizes them by how long the invoices have been
outstanding for the specified period.

### Monthly summary

The [monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
provides a detailed breakdown of activity for the last complete month. Use this
information to understand how your activity affected revenue and to book journal
entries. You can also see activity that contributed to your net revenue. For
example, you can see the portions of new billings that you recognized, and
contra revenue items. This section also lists changes to deferred revenue based
on your activity, like portions of new billings that you haven’t recognized and
contra revenue items.

The monthly summary only shows details if you had activity. For example, if you
don’t have any contra revenue, the monthly summary doesn’t include it.

### Revenue waterfall

The [revenue
waterfall](https://docs.stripe.com/revenue-recognition/reports/waterfall),
sometimes called a revenue schedule chart, displays expected recognizable
revenue over time. Use this to understand how activity from each period affects
revenue in future periods.

This report shows expected revenue amounts based on historical billings. It
doesn’t model future billings and it doesn’t predict future revenue from those
potential billings. The expected future revenue amounts change as you add future
billings.

### CSV reports

You can download reports as a CSV file at any time. To do this:

- Click **Download** next to the report.
- If applicable, select the report format.
- Choose the columns you want to include in the report.
- Click **Download**.

The reports you can download include:

ReportDescription[Income
statement](https://docs.stripe.com/revenue-recognition/reports/income-statement)Detailed
revenue and contra revenue breakdown by monthBalance sheetDetailed balance sheet
account breakdown by monthDebits and creditsMonthly debit and credit journal
entries shown at these levels: summary, product, price, customer, invoice, line
item, metadata, event type, invoice event type, and line item event typeAccounts
receivable agingOutstanding invoice amounts grouped into age buckets shown at
these levels: summary, product, price, customer, invoice, line item, and
metadataCorrectionsMonthly correction entries shown at these levels: summary,
product, price, customer, invoice, line item, and metadata[Trial
balance](https://docs.stripe.com/revenue-recognition/reports/trial-balance)Shows
the account balances for each general ledger account during each accounting
period
The [income
statement](https://docs.stripe.com/revenue-recognition/reports/income-statement)
report shows revenue, contra revenue, expenses, gains, and losses. Contra
revenue adjustments are deductions from gross revenue. Applying the contra
revenue to your gross revenue results in your net income. Use this report to
better understand your net revenue and determine how you want to track contra
revenue items.

The balance sheet report shows the beginning and ending balances for accounts
like deferred revenue, accounts receivable, cash, and so on. You can use this
report to understand overall inflows and outflows to these accounts, as well as
how revenue activity ties to cash.

The accounts receivable aging report consolidates outstanding invoice amounts
and groups them into age ranges: not yet due, 1-30 days, 31-60 days, 61-90 days,
91-120 days, and over 120 days. The report rounds up the ranges (for example, an
invoice overdue by 30.5 days falls into the 31-60 days range). You can use this
report to understand your collections performance and identify customers with
outstanding invoices that are potentially collectible.

The corrections report displays corrected ledger entries, ensuring the accuracy
and transparency of your accounting data. Corrections occur when changes are
made to ledger entries in closed accounting periods. These changes are due to:

- [Data import](https://docs.stripe.com/revenue-recognition/data-import) for
past transactions
- Adding, updating, and deleting [chart of accounts
mappings](https://docs.stripe.com/revenue-recognition/chart-of-accounts) or
[rules](https://docs.stripe.com/revenue-recognition/rules)
- Modifying [revenue
settings](https://docs.stripe.com/revenue-recognition/revenue-settings)
- Bug fixes introduced by Revenue Recognition system upgrades

To allow corrections to backdate to their original periods, reopen the closed
accounting periods with [accounting period
control](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control).

The [trial
balance](https://docs.stripe.com/revenue-recognition/reports/trial-balance)
report lists the balances of the accounts at a specific point in time (as of a
specific date) and ensures the total of the debit accounts equals the total of
the credit accounts. You can use this report to get a snapshot of all the
account balances and to reconcile account balances in Stripe with your general
ledger.

## See also

- [Revenue Recognition
Methodology](https://docs.stripe.com/revenue-recognition/methodology)
- [Revenue Recognition
Examples](https://docs.stripe.com/revenue-recognition/examples)

## Links

- [products and prices](https://docs.stripe.com/products-prices/overview)
- [customers](https://docs.stripe.com/billing/customer)
-
[default_tax_rates](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_tax_rates)
-
[discount](https://docs.stripe.com/api/subscriptions/object#subscription_object-discount)
- [invoice](https://docs.stripe.com/api/invoices)
- [graphs for recognized revenue and deferred
revenue](https://dashboard.stripe.com/revenue-recognition)
- [revenue waterfall
report](https://dashboard.stripe.com/revenue-recognition/accounting-reports)
- [uploading your revenue
data](https://dashboard.stripe.com/revenue-recognition/data-import)
- [defining custom
rules](https://dashboard.stripe.com/revenue-recognition/rules)
- [mapping to the chart of
accounts](https://docs.stripe.com/revenue-recognition/chart-of-accounts)
- [here](https://docs.stripe.com/api/metadata)
- [import the data](https://docs.stripe.com/revenue-recognition/data-import)
- [monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
- [revenue
waterfall](https://docs.stripe.com/revenue-recognition/reports/waterfall)
- [Income
statement](https://docs.stripe.com/revenue-recognition/reports/income-statement)
- [Trial
balance](https://docs.stripe.com/revenue-recognition/reports/trial-balance)
- [rules](https://docs.stripe.com/revenue-recognition/rules)
- [revenue
settings](https://docs.stripe.com/revenue-recognition/revenue-settings)
- [accounting period
control](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)
- [Revenue Recognition
Methodology](https://docs.stripe.com/revenue-recognition/methodology)
- [Revenue Recognition
Examples](https://docs.stripe.com/revenue-recognition/examples)