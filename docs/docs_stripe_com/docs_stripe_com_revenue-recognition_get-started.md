# Recognize revenue with Stripe

## Learn how to use Stripe for your revenue recognition.

You can import your transaction data, set up rules to automate your revenue
recognition, generate and customize revenue reports, and test your transaction
model before going live.

All Stripe Revenue Recognition features are available from the
[Dashboard](https://dashboard.stripe.com/revenue-recognition).

#### Try for free

Stripe offers a 30-day free trial for Revenue Recognition if you want to preview
it. When you [sign up](https://dashboard.stripe.com/), use a
[sandbox](https://docs.stripe.com/sandboxes) to explore all the features for
free.

#### Private preview

If you’re a Connect platform with destination charges, and want to use Stripe
Revenue Recognition, [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports) on our
support page to join our destination charges beta.

[Set up Revenue
Recognition](https://docs.stripe.com/revenue-recognition/get-started#set-up)
Revenue Recognition is already automated for some business use cases but
requires additional setup for others. Below is a list of some common billing
models. Click them to learn more:

### Simple subscriptions

### Metered billing subscriptions

### Third-party recurring billing

### Product bundles

[Generate reports and
charts](https://docs.stripe.com/revenue-recognition/get-started#generate-reports)
By default, the Dashboard displays all [Revenue Recognition reports and
charts](https://docs.stripe.com/revenue-recognition/reports#dashboard) by
accounting periods (which is defined as the start and end dates of a given
month). It takes up to 24 hours for reports to generate and become available for
download.

#### Note

If you’d like to recognize revenue based on custom accounting periods such as
the 4-5-4 retail calendar, please [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports) on our
support page to join our beta.

Below is a short summary of the reports and charts you can view, download, or
both.

Reports and chartsDescriptionRevenue overviewHigh-level bar graphs that show
your revenue activity (that is, your net recognized revenue and your ending
balance per month) over time.Monthly summaryDetails of the accounting activities
for the last month or a specified previous month. See [Monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
for more information.Revenue waterfallDisplays expected recognizable revenue
over time. This is also referred to as a revenue schedule chart. See [Revenue
waterfall](https://docs.stripe.com/revenue-recognition/reports/waterfall) for
more information.Income statementDetails of the revenue and contra revenue by
month.Balance sheetDetails of the balance sheet account by month.Debits and
creditsDetails of the monthly debit-credit journal entries for accounts with
activity.Accounts receivable agingDetails of the monthly and MTD outstanding
invoice amounts that affect the accounts receivable ledger
account.CorrectionsDetails of the monthly debit-credit correction journal
entries for accounts.Trial balanceShows the account balances for each general
ledger account during each accounting period. See [Trial
balance](https://docs.stripe.com/revenue-recognition/reports/trial-balance) for
more information.
Sometimes you’ll see mismatches between your accounting reports after you import
the data and set up Stripe.

[Test your transaction
model](https://docs.stripe.com/revenue-recognition/get-started#test)
Use a sandbox in the Dashboard to generate test revenue reports based on your
transactions.

Before going live, you can test the transaction model without your test
transactions. Create rules to exclude transactions from specific customers,
products, invoices, or payments.

For example, you can exclude all revenues produced by a test customer, named
`test@example.com`. [Create a
rule](https://dashboard.stripe.com/revenue-recognition/rules/create) that
applies to this customer and choose **Exclude revenue 100%** as the revenue
treatment.

## Other considerations

You might need to handle other considerations like [tax
revenue](https://docs.stripe.com/revenue-recognition/get-started#third-party-tax),
[passthrough
fees](https://docs.stripe.com/revenue-recognition/get-started#passthrough-fees),
[amortization
granularity](https://docs.stripe.com/revenue-recognition/revenue-settings#amortization-granularity),
and [catch-up
revenue](https://docs.stripe.com/revenue-recognition/revenue-settings#catch-up-revenue).
You can further set up Revenue Recognition so Stripe can handle it for you.

### Recognize tax revenue from third-party solutions

You can set up rules for Revenue Recognition to automatically calculate your tax
revenue if you’re not using Stripe Tax.

First, set the tax amount to the
[tax](https://docs.stripe.com/billing/taxes/tax-rates) parameter of an invoice
or an invoice line item. Then, set up a rule to recognize the amount as tax. You
can track the revenue from tax in the reports under **Tax liability**.

As an example, say you’re using Avalara AvaTax to calculate sales tax for your
products. You want to treat the invoice line item for `AvaTax` as tax so you
create this rule:

NameApply toTreatment`Recognize tax revenue from AvaTax`Invoices- **Line item
description contains all of the following:** `AvaTax`
Treat as tax- **Allocation** `100%`

### Calculate passthrough fees

You can set up [rules](https://docs.stripe.com/revenue-recognition/rules) so
Stripe can automatically calculate the passthrough fees and, separately, your
revenue on [invoice line items](https://docs.stripe.com/api/invoices/line_item)
or a portion of an invoice line item.

For example, say you have an invoice line item `Service A` that costs 100 USD.
You want to recognize 10 USD as passthrough fees and recognize 90 USD as
revenue, so you [create this
rule](https://dashboard.stripe.com/revenue-recognition/rules/create):

NameApply toTreatment
`Service A includes passthrough fees`

**Invoices**

- **Line item description contains all of the following:** `Service A`

**Defer upon event & amortize over line item service period**

- **Allocation** `90%`
- **Defer from finalized time and amortize over line item service period**

**Treatment as passthrough fees**

- **Allocation** `10%`

### Adjust Revenue Recognition controls

While Stripe Revenue Recognition is designed to work out-of-the-box for many
business types, we understand that each business might have unique needs. We
offer advanced configurations on your revenue recognition reporting through our
[Controls](https://docs.stripe.com/revenue-recognition/revenue-settings) page,
where you can easily adjust for settings like revenue amortization granularity
and catch-up revenue treatment.

## See also

- [Subscriptions and Tax](https://docs.stripe.com/billing/taxes)

## Links

- [Dashboard](https://dashboard.stripe.com/revenue-recognition)
- [sign up](https://dashboard.stripe.com/)
- [sandbox](https://docs.stripe.com/sandboxes)
- [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports)
- [Revenue Recognition reports and
charts](https://docs.stripe.com/revenue-recognition/reports#dashboard)
- [Monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
- [Revenue
waterfall](https://docs.stripe.com/revenue-recognition/reports/waterfall)
- [Trial
balance](https://docs.stripe.com/revenue-recognition/reports/trial-balance)
- [Create a rule](https://dashboard.stripe.com/revenue-recognition/rules/create)
- [amortization
granularity](https://docs.stripe.com/revenue-recognition/revenue-settings#amortization-granularity)
- [catch-up
revenue](https://docs.stripe.com/revenue-recognition/revenue-settings#catch-up-revenue)
- [tax](https://docs.stripe.com/billing/taxes/tax-rates)
- [rules](https://docs.stripe.com/revenue-recognition/rules)
- [invoice line items](https://docs.stripe.com/api/invoices/line_item)
- [Controls](https://docs.stripe.com/revenue-recognition/revenue-settings)
- [Subscriptions and Tax](https://docs.stripe.com/billing/taxes)