# Map to your chart of accounts

## Map transactions from the Stripe default accounts to the chart of accounts in your general ledger.

You can customize Stripe Revenue Recognition reporting to use your General
Ledger (GL) chart of accounts instead of using the default [Stripe
accounts](https://docs.stripe.com/revenue-recognition/methodology). You can
configure a rule to map transactions by product, shipping region, or invoice
metadata to your GL account. Stripe applies your custom mappings to the [CSV
reports](https://docs.stripe.com/revenue-recognition/reports#csv-reports) you
download and also when you [audit your revenue
numbers](https://docs.stripe.com/revenue-recognition/reports/audit-numbers). A
mapping rule consists of the following:

Mapping rule attribute DescriptionStripe accountThe [Stripe default
account](https://docs.stripe.com/revenue-recognition/methodology#chart-of-accounts)
that you want to override.GL accountThe name of the GL account you want to
override the Stripe account with.GL account numberThe number corresponding to
the GL account.
Effective period

The time period the mapping applies to.

An [invoice line item](https://docs.stripe.com/api/invoices/line_item) fulfills
the effective period requirement if the finalization time of the invoice is
within the specified effective period.

A [charge](https://docs.stripe.com/api/charges) fulfills the effective period
requirement if the balance transaction it corresponds to has a creation time
that’s within the specified effective period.

ConditionAn optional criteria to map transactions by product, shipping region,
or invoice metadata. If not specified, all transactions involving the configured
Stripe account are mapped to the GL account.
Status

**Active**: The mapping rule is active and all transactions are mapped as per
the rule.

**Processing**: The rule is processing. On completion, the rule is active and
transactions are mapped accordingly.

## Configuring a mapping rule

Mapping rule configuration is a 4-step process—click the add mapping button on
the accounts mapping page to begin.

- **Select Stripe account**: Select the default Stripe account from the dropdown
for which you want to create the rule.
- **Select GL account**: You can select your GL account from the dropdown or add
one if you can’t find it in the dropdown. When setting up the rules for the
first time, you have to add these accounts by specifying the GL account name and
number. You have to specify at least a name or a number to add the account.
- **Specify effective period**: The effective period is the time frame in which
the mapping rule is applicable. Select a start and end date from the dropdown to
configure the effective period. If you specify an effective period that overlaps
with closed accounting periods, you’ll see corrections in your report in the
current open accounting period. You can reopen the past accounting periods
corresponding to the effective period to avoid corrections.
- **Specify mapping condition (optional)***: You can optionally specify a
mapping condition on any of the following attributes:- **Product**: If you have
product specific accounts in your GL, you can classify your transactions based
on the products that you have configured in the Stripe Dashboard.
- **Shipping region**: Similar to products, you can specify the shipping region
to map transactions to the relevant GL account. Only ISO-compliant country and
state codes are supported.
- **Invoice metadata**: You can configure a custom rule using invoice metadata
if your GL accounts don’t track transactions by product or shipping region.
Create a rule by selecting a key and adding a value. The keys are from metadata
you created in past invoices.**

Click **Map accounts** to create the mapping rule and for Stripe to [process the
data](https://docs.stripe.com/revenue-recognition/methodology#data-availability).
The rule’s status changes to active when the data processing is complete, and
you can then download reports with the mapped GL accounts.

## Mapping rule configuration example

The following example involves 3 different products:

- Product A: Annual subscription cost of 1,200 USD
- Product B: Annual subscription cost of 2,400 USD
- Product C: Annual subscription cost of 3,600 USD

If you sell 1 subscription each for A, B, and C in January, your journal entry
at the end of the month appears as follows without account mapping:

AccountJanuaryRevenue+600 USDDeferred Revenue+6600 USD
However, the user has 3 separate revenue accounts in its GL, say revenue_A,
revenue_B, and revenue_C for tracking revenue corresponding to these 3 products.
The user has to do manual work to identify revenue in these accounts before
posting to its GL.

If you have product-specific accounts in your General Ledger that you want to
map to, you can create 3 mapping rules:

Stripe accountGL account numberGL accountConditionEffective
periodRevenue10001revenue_AProduct AJan 2023 -
IndefiniteRevenue10002revenue_BProduct BJan 2023 -
IndefiniteRevenue10003revenue_CProduct CJan 2023 - Indefinite
After you set up these rules, your journal entries will contain three line items
reflecting the revenue distribution for each product. This can help you
streamline the process of posting to your GL.

GL account numberAccountJanuary1001revenue_A+100 USD1002revenue_B+200
USD1003revenue_C+300 USD-Deferred Revenue+6600 USD
* For a default Stripe account, you can only pick one attribute to create a
rule. Please [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports) on our
support page if you have any questions.** Don’t import any personally
identifiable information and/or protected health information.

## Links

- [Stripe accounts](https://docs.stripe.com/revenue-recognition/methodology)
- [CSV reports](https://docs.stripe.com/revenue-recognition/reports#csv-reports)
- [audit your revenue
numbers](https://docs.stripe.com/revenue-recognition/reports/audit-numbers)
- [Stripe default
account](https://docs.stripe.com/revenue-recognition/methodology#chart-of-accounts)
- [invoice line item](https://docs.stripe.com/api/invoices/line_item)
- [charge](https://docs.stripe.com/api/charges)
- [process the
data](https://docs.stripe.com/revenue-recognition/methodology#data-availability)
- [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports)