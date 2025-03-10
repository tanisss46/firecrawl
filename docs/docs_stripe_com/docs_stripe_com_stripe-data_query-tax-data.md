# Query tax data

## Use Sigma or Data Pipeline to retrieve tax information.

Stripe Tax data includes various components that work together to provide a
comprehensive view of your tax liability through automated calculations with
[Payment Links](https://docs.stripe.com/tax/payment-links),
[Checkout](https://docs.stripe.com/tax/checkout),
[Subscriptions](https://docs.stripe.com/tax/subscriptions),
[Invoices](https://docs.stripe.com/tax/invoicing), [Custom
integrations](https://docs.stripe.com/tax/custom) and [as a
platform](https://docs.stripe.com/tax/connect). All tax-specific data is
available in the **Tax** section of the schema, and the primary table is
`tax_transactions`.

To explore tax data further, you can use additional tables that represent the
components of a `tax_transaction`, such as `tax_transaction_line_items`,
`tax_transaction_shipping_costs`, and `tax_transaction_jurisdiction_details`.

This diagram represents all components created during an automated tax
calculation and how it relates to the original object that triggered
calculation. Amounts in the examples below appear in minor
[currency](https://docs.stripe.com/currencies) units (for example, cents instead
of dollars).

hide sample argumentsid in_02ae51766c844635 hide sample argumentsid
tax_6ac9561b8d634d41 source_idin_02ae51766c844635 source_type`invoice`hide
sample argumentsid tax_li_f47e3fd32b384914
tax_transaction_idtax_6ac9561b8d634d41 hide sample argumentsid
tax_li_8d87a750a4d340dc tax_transaction_idtax_6ac9561b8d634d41 hide sample
argumentstax_transaction_idtax_6ac9561b8d634d41 tax_transaction_item_id
tax_li_f47e3fd32b384914 tax_transaction_item_type`tax_transaction_line_item`hide
sample argumentstax_transaction_idtax_6ac9561b8d634d41
tax_transaction_item_idtax_li_8d87a750a4d340dc
tax_transaction_item_type`tax_transaction_shipping_cost`
## Tax transactions

Each row in the `tax_transactions` table represents a single
[tax_transaction](https://docs.stripe.com/api/tax/transactions/object) object.
Tax transactions record the assumed or reduced tax liability for a transaction
or reversal. You can report on every tax transaction created with automated tax
calculations.

This table is our recommended starting point for creating reports on your tax
liability. You need to join on the other tax tables below for your tax liability
amounts, but this table joins your data to other products like invoices and
checkout sessions. Joining to non-tax tables by `source_id` and `source_type`
provides the object that triggers the creation of the tax transaction.

Tax transactions have a one-to-one relationship with their original source
object. The following example retrieves a list of reportable tax transactions
with their original source of invoices, which you can then expand on with [query
billing data](https://docs.stripe.com/stripe-data/query-billing-data).

```
select
 tx.id as tax_transaction_id,
 tx.posted_at as tax_transaction_posted_at,
 inv.id as invoice_id,
 inv.total as invoice_total
from
 tax_transactions tx
 inner join invoices inv on inv.id = tx.source_id
limit
 5
```

tax_transaction_idtax_transaction_posted_atinvoice_idinvoice_totaltax_f4X7iVeuZxh2aos2024-06-18
16:40:16 +0000in_oXCl9MLgDjbMiL520,000tax_r7yjOkhUupQgfei2021-06-28 00:01:21
+0000in_0ByyEJJVFdLRu1L189tax_hw7JNLccDoXELs92024-06-23 23:35:40
+0000in_PmSAYKFlMPnrjOq219tax_ita7SUjbHDJnDdq2024-06-23 23:35:40
+0000in_QcpXQ8WomRlbCRz10,475tax_pxd81rnNtqninUe2023-07-23 04:03:06
+0000in_7EBeKqBBSj6NAJk200
### Tax transactions metadata

Tax transactions might have metadata set with your [custom
integrations](https://docs.stripe.com/tax/custom). Each row in
`tax_transactions_metadata` returns one key-value pair.

tax_transactions

tax_transactions_metadata[0]

tax_transactions_metadata[1]

tax_transactions_metadata[2]

Tax Transactions Metadata overview
## Tax transaction items

Tax line items and tax shipping costs make up the total amounts and tax
liability for tax transactions. Tax line items and tax shipping costs are in
their own tables, but they both contribute to amounts and total tax liability.

### Tax line items

Tax line items represent line items that contribute to the sale of goods for the
transaction. Each row in `tax_transaction_line_items` represents a single tax
line item associated to the `tax_transaction`.

### Tax shipping costs

Tax shipping costs represent shipping items that contribute to the shipment of
goods for the transaction. Each row in `tax_transaction_shipping_costs`
represents a single shipping cost associated to the `tax_transaction`.

#### Note

These tables provide high level information based on each item. A single tax
transaction can have multiple line items and one shipping cost which make up the
amounts for a tax transaction.

**amount**: This is the gross amount of the line item. When `tax_behavior` is
`inclusive`, it includes tax liability amounts. When `tax_behavior` is
`exclusive` (the default), it excludes tax liability amounts.

**amount_tax**: This is the amount of tax liability for the line item.

**currency**: This is the [presentment
currency](https://docs.stripe.com/currencies) that defines `amount` and
`amount_tax`. Summing across different currencies yields unexpected results.

tax_transactions

tax_transaction_line_items[0]

tax_transaction_line_items[1]

tax_transaction_line_items[2]

tax_transaction_line_items[3]

tax_transaction_shipping_costs[0]

Tax Transaction Items Overview
The following example retrieves a list of all amounts and tax liability for a
given `tax_transaction`.

```
with tax_amounts as (
 select
 li.tax_transaction_id,
 li.id,
 li.amount,
 li.amount_tax,
 li.tax_behavior,
 li.currency,
 'line_item' as item_type
 from
 tax_transaction_line_items li
 union all
 select
 sc.tax_transaction_id,
 sc.id,
 sc.amount,
 sc.amount_tax,
 sc.tax_behavior,
 sc.currency,
 'shipping_cost' as item_type
 from
 tax_transaction_shipping_costs sc
)
select
 id,
 amount,
 amount_tax,
 tax_behavior,
 currency,
 item_type
from
 tax_amounts
where
 tax_transaction_id = 'tax_d2e5470dC63u'
```

idamountamount_taxtax_behaviorcurrencyitem_typetax_li_NCgbmTtmU3aIHH93,1000exclusiveusdline_itemtax_li_T09OHN6pMa66j3k1,999190exclusiveusdline_itemtax_li_FYgUdAppdbgV38X3,500304inclusiveusdline_itemtax_li_BzbrFuAGd4OxQNI4,242242exclusiveusdline_itemtax_li_zDGi30Kox0fGOTW7990exclusiveusdshipping_cost
### Tax transaction line items metadata

Tax transaction line items might have metadata set with your [custom
integrations](https://docs.stripe.com/tax/custom). Each row in
`tax_transaction_line_items_metadata` returns one key-value pair.

tax_transaction_line_items

tax_transaction_line_items_metadata[0]

tax_transaction_line_items_metadata[1]

tax_transaction_line_items_metadata[2]

Tax Transactions Metadata
## Tax transaction jurisdiction details

Each row in the `tax_transaction_jurisdiction_details` table represents a
jurisdiction which makes up the liability for the tax transaction item
(`tax_transaction_line_item` or `tax_transaction_shipping_cost`).

### Understanding jurisdiction details

This table provides more in-depth information based on each jurisdiction. A
single tax transaction item can have multiple jurisdictions which make up the
amounts for a tax transaction item.

Summing `amount_taxable` or `amount_non_taxable` across all jurisdiction details
doesn’t always equal the tax transaction item’s `amount`.

**amount_taxable**: This is the amount up to the tax transaction item’s `amount`
that is taxable. Multiple jurisdictions can have the same taxable amount.

**amount_non_taxable**: This is the amount up to the tax transaction item
`amount` that is non-taxable. Multiple jurisdictions can have the same
non-taxable amount.

**amount_tax**: This is part of the tax transaction item `amount_tax`. Summing
this across all jurisdiction details equals the transaction item’s `amount_tax`.

**currency**: This is the [presentment
currency](https://docs.stripe.com/currencies) that defines `amount_taxable`,
`amount_non_taxable` and `amount_tax`. Summing across different currencies
yields unexpected results.

**filing_currency**: This is the [filing
currency](https://docs.stripe.com/currencies) used by the applicable tax
authority which defines `filing_amount_taxable`, `filing_amount_non_taxable` and
`filing_amount_tax`. Summing across different filing currencies yields
unexpected results.

hide sample argumentsidtax_li_6836762dd869439famount`100`amount_tax`15`hide
sample arguments tax_transaction_item_id
tax_li_6836762dd869439fjurisdiction_level`state`amount_taxable`100`amount_non_taxable`0`amount_tax`10`hide
sample arguments tax_transaction_item_id
tax_li_6836762dd869439fjurisdiction_level`country`amount_taxable`0`amount_non_taxable`100`amount_tax`0`hide
sample arguments tax_transaction_item_id
tax_li_6836762dd869439fjurisdiction_level`district`amount_taxable`50`amount_non_taxable`50`amount_tax`5`
The following example retrieves all jurisdiction details for a given tax
transaction item.

```
select
 jd.amount_taxable,
 jd.amount_non_taxable,
 jd.amount_tax,
 jd.taxability_reason,
 jd.jurisdiction_level,
 jd.jurisdiction_name,
concat(jd.jurisdiction_country, '-', jd.jurisdiction_state) as
jurisdiction_location
from
 tax_transaction_jurisdiction_details jd
where
 li.id = 'tax_li_52d37cdd6f7'
```

amount_taxableamount_non_taxableamount_taxtaxability_reasonjurisdiction_leveljurisdiction_namejurisdiction_location01,2990not_subject_to_taxcountryUnited
States1,299077standard_ratedstateCaliforniaUS-CA1,299016standard_ratedcountySan
DiegoUS-CA1,29907standard_rateddistrictTransactions and Use Tax
(CLVT)US-CA1,29907standard_rateddistrictTransactions and Use Tax
(CVGT)US-CA1,29907standard_rateddistrictRegional Transportation Commission
(SDCT)US-CA
## Example queries

For additional examples, please reference the [Tax section of query template
library in Sigma sidebar](https://dashboard.stripe.com/sigma/queries).

### Tax liability by month

This example summarizes the tax liability imposed on line items and shipping
costs grouped by month and [currency](https://docs.stripe.com/currencies).

```
with tax_amounts as (
 select
 li.tax_transaction_id,
 li.amount,
 li.amount_tax,
 li.tax_behavior,
 li.currency
 from
 tax_transaction_line_items li
 union all
 select
 sc.tax_transaction_id,
 sc.amount,
 sc.amount_tax,
 sc.tax_behavior,
 sc.currency
 from
 tax_transaction_shipping_costs sc
),
tax_liability as (
 select
 date_format(date_trunc('month', posted_at), '%Y-%m-%d') as month,
 currency as presentment_currency,
 sum(
 (
```

See all 49
linesmonthpresentment_currencytotal_sales_excluding_taxtotal_tax2025-03-01usd286,60043,5222025-03-01eur30,898562025-02-01usd79,7762,5652025-02-01eur55,4343,954
### Tax itemized jurisdiction details

This template itemizes tax transaction jurisdiction details for the previous
month to produce a customizable version of the [Tax itemized
export](https://docs.stripe.com/tax/reports#itemized-exports). Review the
comments throughout the template to learn more about how it is customizable for
your needs.

```
with tax_amounts as (
 select
 li.id,
 li.source_line_item_id,
 li.amount,
 li.amount_tax,
 li.tax_behavior,
 li.tax_code,
 li.currency,
 li.quantity_decimal
 from
 tax_transaction_line_items li
 union all
 select
 sc.id,
 -- Shipping costs do not have source line item IDs
 '' as source_line_item_id,
 sc.amount,
 sc.amount_tax,
 sc.tax_behavior,
 sc.tax_code,
 sc.currency,
 -- Shipping costs do not have a quantity
 '' as quantity_decimal
 from
```

See all 85
linessource_idsource_typepresentment_currencyposted_attax_date,transaction_source_item_idtransaction_item_idamountamount_taxtax_behaviortax_codejurisdiction_namejurisdiction_level…in_FmrxdLcUBDvzRWJinvoiceeur2025-02-152025-02-15il_7Mp6RmTqO7ZwLmWtax_il_Upjn1v8h2plDTHh-199-20exclusivetxcd_99999999Irelandcountry…in_mnDZm2m8Ec64qpNinvoiceusd2025-02-152025-02-15il_dTuKeHjncroFiyLtax_il_NZc5R4aaerHsopS10,0001,000exclusivetxcd_99999999Rhode
Islandstate…in_rkXBn1odpDKcLGPinvoiceusd2025-02-092025-02-09il_vlooRsmcYhdFgp7tax_il_Nx5GA7lVrqDfBJO2,999371exclusivetxcd_99999999Fire
District 17district…

## Links

- [Payment Links](https://docs.stripe.com/tax/payment-links)
- [Checkout](https://docs.stripe.com/tax/checkout)
- [Subscriptions](https://docs.stripe.com/tax/subscriptions)
- [Invoices](https://docs.stripe.com/tax/invoicing)
- [Custom integrations](https://docs.stripe.com/tax/custom)
- [as a platform](https://docs.stripe.com/tax/connect)
- [currency](https://docs.stripe.com/currencies)
- [Invoice](https://docs.stripe.com/api/invoices/object)
- [tax_transactions](https://docs.stripe.com/api/tax/transactions/object)
- [query billing data](https://docs.stripe.com/stripe-data/query-billing-data)
- [Tax section of query template library in Sigma
sidebar](https://dashboard.stripe.com/sigma/queries)
- [Tax itemized export](https://docs.stripe.com/tax/reports#itemized-exports)