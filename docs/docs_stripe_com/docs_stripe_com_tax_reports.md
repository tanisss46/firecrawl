# Tax reporting

## Learn about different reporting available in Stripe Tax.

#### Note

[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

Stripe Tax provides reports of completed transactions, and it provides three
different kinds of reports:

- Itemized exports show a detailed view of completed transactions for all
locations, or a country or state.
- Summarized exports show an aggregated view of completed transactions by
location.
- Location reports show an aggregated view of completed transactions for your
registrations in the US and Canada.

To access these reports, navigate to the
[Registrations](https://dashboard.stripe.com/tax/registrations) page on the
Dashboard.

In May 2024, we updated jurisdictions in our location reports, itemized exports,
and summarized exports for increased consistency across Stripe Tax. These
changes include:

- Splitting some jurisdictions into multiple sub-jurisdictions
- Changing the names of some jurisdictions

As a result, jurisdiction names in transactions before and after May 2024 might
not be identical.

#### Note

If you work for a platform that pays you via Stripe you’ll need a 1099 form to
file your taxes. Visit the [support
site](https://support.stripe.com/express/topics/1099-tax-forms) to learn more
about how to verify your tax information and receive your forms

## Exports

Exports are CSV files that contain details of completed transactions where you
enabled Stripe Tax. Typically, new transactions become available within a day of
completion.

### Itemized exports

Itemized exports contain a detailed view of the line item level tax breakdown
for every transaction. You might have multiple rows per line item if you have
multiple jurisdictions imposing tax. This amount of detail can help with filing
tax in jurisdictions that require more details in tax reports.

Itemized exports also contain non-taxable transactions. Non-taxable transactions
are transactions in locations where you’re not registered, in locations that
Stripe Tax doesn’t support, or locations where no jurisdiction imposes tax. You
can filter out these transactions by selecting **Exclude non-taxable
transactions** when exporting.

#### Sub-state level reportingUnited States

Use itemized exports for US states that require sub-state level reporting.

#### One Stop Shop (OSS)EU

If you’ve registered for the One Stop Shop (OSS) within the European Union, you
can download an itemized export of all your EU transactions. This export can
assist in preparing your VAT OSS return. Itemized exports include non-taxable
transactions (unless purposely excluded) and domestic transactions, which you
don’t need to report in an OSS return. Make sure to filter out domestic
transactions in your export.

[Download example CSV
file](https://d37ugbyn3rpeym.cloudfront.net/docs/files/tax/itemized-export.csv)

### Summarized exports

Summarized exports contain an aggregated view of transactions per jurisdiction.
In certain cases, such as when currencies or tax rates vary, you might have
multiple rows per jurisdiction.

All columns account for negative line items generated as a result of
subscription prorations or credits for unused time. This helps reconcile your
summarized and itemized exports.

Summarized exports don’t contain non-taxable transactions, unlike itemized
exports.

#### Regional considerations

Use this export for country-level filings and VAT OSS, and for simpler US
states.

### Summarized tax transactions

Column nameDescriptioncountry_code
Two-letter ISO code representing the situs country.

filing_currency
Filing currency for applicable registration jurisdiction

filing_tax_payable
Total amount of tax payable in filing currency

filing_total_nontaxable_sales
Total amount of nontaxable sales in filing currency

filing_total_sales
Total amount of all sales (not including tax) in filing currency

filing_total_sales_refunded
Total amount of taxable refunds in filing currency

filing_total_tax_collected
Total amount of tax collected in filing currency

filing_total_tax_refunded
Total amount of tax refunded in filing currency

filing_total_taxable_refunded
Total amount of taxable refunds in filing currency. Replaces
filing_total_taxable_refunds

filing_total_taxable_sales
Total amount of taxable sales in filing currency

jurisdiction_level
The jurisdiction level imposing the tax

jurisdiction_name
The imposing tax jurisdiction name

state_code
Two-letter ISO code representing the situs country subdivision.

tax_rate
Tax rate

total
Total of transaction amounts (including tax) in presentment currency

total_nontaxable_sales
Non-taxable amount in presentment currency

total_sales
Total amount of all sales (not including tax) in presentment currency

total_sales_refunded
Total amount of all refunds (not including tax) in presentment currency.
Replaces total_refunds

total_tax_collected
Total amount of tax collected in presentment currency

total_tax_refunded
Total amount of tax refunded in presentment currency

total_taxable_sales
Taxable amount in presentment currency

transaction_currency
Transaction currency

transaction_date_end
The transaction date end in the requested timezone

transaction_date_end_utc
The transaction date end in UTC

transaction_date_start
The transaction date start in the requested timezone

transaction_date_start_utc
The transaction date start in UTC

[Download example CSV
file](https://stripe.com/files/docs/tax/summarized-export-v3.csv)

## Imports

We’re building a feature that lets you import transactional data from platforms
such as Amazon, Shopify, and eBay into Stripe Tax. By consolidating your
transactional data, you can:

- Eliminate the need to reconcile and aggregate across different platforms.
- Stay compliant by having the most accurate view of your tax obligations at all
times.

Sign up below if you want to participate in the beta. If selected, we’ll contact
you with more information about the next steps.

## Interested in getting early access to the Stripe Tax third-party import tool?

Share your email address to learn more.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Location reports

Location reports provide a summary of transaction and refund data aggregated for
specific locations. Every location report follows the filing and formatting
requirements of the location it’s generated for, and aligns with the specific
filing periods of its online filing portal. You can select the **frequency** and
**period** within the report, as determined by the location.

Stripe provides location reports for the US and Canada. You can only view
location reports in the Dashboard and can’t download them.

Stripe Tax currently doesn’t support use cases beyond your transaction data,
such as credits, prepayments, discounts, and so on. As a result, the final
numbers for your business’s filing might vary.

#### Caution

Location reports include transactions starting from January 1, 2023, and support
fiscal annual periods from 2024 onward. To access your transaction data from
2022, use [itemized](https://docs.stripe.com/tax/reports#itemized-exports) or
[summarized](https://docs.stripe.com/tax/reports#summarized-exports) exports.

### Refunds

Location reports include refunds associated with an original transaction in the
same period as the original transaction, even if the refund occurred much later.
This can affect the aggregated amounts in a report. Stripe doesn’t allow the
reassigning of refunds to alternate periods.

### Tax types

Location reports support sales or use tax types only.

For more detailed breakdowns including other tax types, use [itemized
exports](https://docs.stripe.com/tax/reports#itemized-exports).

### Location specific considerations

The locations listed below have additional report considerations:

-
[Alaska](https://docs.stripe.com/tax/supported-countries/united-states/alaska#location-reports)
-
[Arizona](https://docs.stripe.com/tax/supported-countries/united-states/arizona#location-reports)
-
[Florida](https://docs.stripe.com/tax/supported-countries/united-states/florida#location-reports)
-
[Hawaii](https://docs.stripe.com/tax/supported-countries/united-states/hawaii#location-reports)
-
[Illinois](https://docs.stripe.com/tax/supported-countries/united-states/illinois#location-reports)
-
[Kentucky](https://docs.stripe.com/tax/supported-countries/united-states/kentucky#location-reports)
-
[Tennessee](https://docs.stripe.com/tax/supported-countries/united-states/tennessee#location-reports)
-
[Washington](https://docs.stripe.com/tax/supported-countries/united-states/washington#location-reports)

## Access data using exports and reports

### Itemized and summarized exports

- Navigate to the **Registrations** page on the Dashboard.
- Click **Export transactions**.
- Specify the date range and time zone.
- Select either **Itemized export** or **Summarized export**. If you selected
**Itemized export**:- Select the **Columns** you want.
- Select whether to **Exclude non-taxable transactions** or not.
- Click **Export**. The export might need time to process.

#### Itemized exports by location

- Navigate to the **Registrations** page on the Dashboard.
- Click the location you want to generate an export for.
- Click **Export transactions**.
- Specify the date range and the time zone.
- Select the **Columns** you want
- Select whether to **Exclude non-taxable transactions** or not.
- Click **Export**. The export might need time to process.

### Location reports

- Navigate to the **Registrations** page on the Dashboard.
- Click the location whose location report you want to access.
- Select the **Frequency**.
- Select the **Period**.

## Scheduled Tax reports

Stripe can generate your Tax reports on a schedule.

### Itemized and summarized exports

- Navigate to the **Registrations** page on the Dashboard.
- Click **Export transactions**.
- Click **Schedule…**
- Select the **Schedule** you want to receive your reports by: **Daily**,
**Weekly**, or **Monthly**. To disable scheduled reports, select **None**.
- Select **Columns** for **Itemized tax transactions**. We recommend exporting
**All** columns for completeness.
- Click **Save**.

### Itemized exports by location

- Navigate to the **Registrations** page on the Dashboard.
- Click the location you want to schedule Tax reports for.
- Click **Export transactions**.
- Click **Schedule…**
- Select the **Schedule** you want to receive your reports by: **Daily**,
**Weekly**, or **Monthly**. To disable scheduled reports, select **None**.
- Select **Columns**. We recommend exporting **All** columns for completeness.
- Click **Save**.

### Location reports

You can’t schedule location reports.

## Giving access to your accountant

If you want to give access to your accountant or other trusted third parties to
access your Tax reports, you can [invite them as a team
member](https://support.stripe.com/questions/invite-team-members-or-developers-to-access-your-stripe-account).

After you invite them, your accountant (or others) can perform the same steps
described above to access location reports, itemized, and summarized exports.

#### Security tip

Give your users the smallest set of permissions possible that they can still
perform their duties with.

For accessing Tax reports, we recommend the **View Only** role. See [user
roles](https://docs.stripe.com/get-started/account/teams/roles) to learn what
this role can and can’t do.

## Tax calculations recorded in reports

Stripe Tax exports include transactions created using [Stripe Tax
API](https://docs.stripe.com/tax/custom) and operations on Stripe objects with
`automatic_tax[enabled]=true`.

#### Note

We consider transactions effective on the date they finalize and we don’t
recalculate taxes afterwards.

The following operations *increase* the balance of total tax reported:

- The customer completes a payment in a Checkout Session. This also applies to
Checkout Sessions created through [Payment
Links](https://docs.stripe.com/api/payment_links/payment_links).
- [Finalizing](https://docs.stripe.com/api/invoices/finalize) an invoice. This
applies to one-off invoices and recurring (subscription) invoices. [Invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)
happens when the state of the invoice transitions from a `draft` to an `open`
state. This transition happens *before* the invoice is paid.
- Transitioning the state of an invoice from `uncollectible` to `paid` through
the [Pay Invoices API](https://docs.stripe.com/api/invoices/pay).
- [Voiding](https://docs.stripe.com/api/credit_notes/void) a credit note.
-
[Creating](https://docs.stripe.com/api/tax/transactions/create_from_calculation)
a tax transaction using the Stripe Tax API.

The following operations *decrease* the balance of total tax reported:

- [Voiding](https://docs.stripe.com/api/invoices/void) an invoice.
- [Marking](https://docs.stripe.com/api/invoices/mark_uncollectible) an invoice
as uncollectible.
- [Creating](https://docs.stripe.com/api/credit_notes/create) a credit note.
- [Creating](https://docs.stripe.com/api/refunds) a refund of a charge
associated with an invoice or a Checkout Session.
- [Creating a
reversal](https://docs.stripe.com/api/tax/transactions/create_reversal) of a tax
transaction using the Stripe Tax API.

The following operations aren’t reflected in Tax reports:

- [Disputes](https://docs.stripe.com/disputes) that are upheld by the
cardholder’s bank. Stripe Tax doesn’t decrease the balance of the collected
total tax.
- Refunds of [uncaptured
amounts](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
of a payment. This can happen when performing a [partial
capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
for payments of Checkout sessions using
[capture_method=manual](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method).
When the capture amount is lower than the original amount, Stripe Tax doesn’t
reduce the total balance of the collected tax.

## Tax data in Sigma and Data Pipeline

If you want to create tailored reports for your specific needs, sign up for
[Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard) or [Data
Pipeline](https://docs.stripe.com/stripe-data/access-data-in-warehouse). For
guidance on querying and creating custom tax data reports, see our guide on
[Querying Tax data](https://docs.stripe.com/stripe-data/query-tax-data).

## See also

- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [Registering for tax](https://docs.stripe.com/tax/registering)
- [Tax filing and remittance](https://docs.stripe.com/tax/filing)

## Links

- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [support site](https://support.stripe.com/express/topics/1099-tax-forms)
- [Download example CSV
file](https://d37ugbyn3rpeym.cloudfront.net/docs/files/tax/itemized-export.csv)
- [Download example CSV
file](https://stripe.com/files/docs/tax/summarized-export-v3.csv)
- [privacy policy](https://stripe.com/privacy)
-
[Alaska](https://docs.stripe.com/tax/supported-countries/united-states/alaska#location-reports)
-
[Arizona](https://docs.stripe.com/tax/supported-countries/united-states/arizona#location-reports)
-
[Florida](https://docs.stripe.com/tax/supported-countries/united-states/florida#location-reports)
-
[Hawaii](https://docs.stripe.com/tax/supported-countries/united-states/hawaii#location-reports)
-
[Illinois](https://docs.stripe.com/tax/supported-countries/united-states/illinois#location-reports)
-
[Kentucky](https://docs.stripe.com/tax/supported-countries/united-states/kentucky#location-reports)
-
[Tennessee](https://docs.stripe.com/tax/supported-countries/united-states/tennessee#location-reports)
-
[Washington](https://docs.stripe.com/tax/supported-countries/united-states/washington#location-reports)
- [invite them as a team
member](https://support.stripe.com/questions/invite-team-members-or-developers-to-access-your-stripe-account)
- [user roles](https://docs.stripe.com/get-started/account/teams/roles)
- [Stripe Tax API](https://docs.stripe.com/tax/custom)
- [Payment Links](https://docs.stripe.com/api/payment_links/payment_links)
- [Finalizing](https://docs.stripe.com/api/invoices/finalize)
- [Invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)
- [Pay Invoices API](https://docs.stripe.com/api/invoices/pay)
- [Voiding](https://docs.stripe.com/api/credit_notes/void)
-
[Creating](https://docs.stripe.com/api/tax/transactions/create_from_calculation)
- [Voiding](https://docs.stripe.com/api/invoices/void)
- [Marking](https://docs.stripe.com/api/invoices/mark_uncollectible)
- [Creating](https://docs.stripe.com/api/credit_notes/create)
- [Creating](https://docs.stripe.com/api/refunds)
- [Creating a
reversal](https://docs.stripe.com/api/tax/transactions/create_reversal)
- [Disputes](https://docs.stripe.com/disputes)
- [uncaptured
amounts](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
-
[capture_method=manual](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
- [Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard)
- [Data Pipeline](https://docs.stripe.com/stripe-data/access-data-in-warehouse)
- [Querying Tax data](https://docs.stripe.com/stripe-data/query-tax-data)
- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [Registering for tax](https://docs.stripe.com/tax/registering)
- [Tax filing and remittance](https://docs.stripe.com/tax/filing)