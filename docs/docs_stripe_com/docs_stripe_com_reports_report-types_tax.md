# Tax report type

## Review the Tax report schema and parameters.

The Tax report returns data related to the tax calculated and charged for your
transactions, including information about the tax codes used.

The following tables define the required and optional parameters to run the
report, as well as the schema of the CSV output.

Report typeRequired run parametersOptional run
parameters`tax.transactions.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/tax#schema-tax-transactions-itemized-2)-
`interval_start`
- `interval_end`
- `timezone`
- `decimal_separator`
- `columns`

### Itemized tax transactions

API report type: `tax.transactions.itemized.2`

Column nameDefaultDescriptioncountry_code
Two-letter ISO code representing the situs country.

credit_note_metadata[key]
Metadata associated with a Credit Note object

currency
Transaction currency presented to the buyer.

customer_tax_id
List of tax ID type-value pairs for the customer.

destination_resolved_address_country
Two-letter ISO code representing the customer country.

destination_resolved_address_state
Two-letter ISO code representing the customer country subdivision.

filing_currency
Filing currency for applicable registration jurisdiction.

filing_exchange_rate
Filing exchange rate used.

filing_non_taxable_amount
Non-taxable amount in filing currency.

filing_tax_amount
Tax amount in filing currency.

filing_taxable_amount
Taxable amount in filing currency.

filing_total
Taxable amount plus tax or non-taxable amount in filing currency.

id
Unique ID for the tax transaction. A transaction is identified by reference to
an invoice, checkout session, credit note, subscription, or order.

invoice_metadata[key]
Metadata associated with an Invoice object

jurisdiction_level
Jurisdiction level imposing the tax.

jurisdiction_name
Imposing tax jurisdiction name.

line_item_id
Unique ID for the line item associated with the tax transaction. Multiple sales
taxes rates may be applied to a single line item, so you may see several rows
with the same line item ID.

non_taxable_amount
Non-taxable amount in the transaction currency.

origin_resolved_address_country
Two-letter ISO code representing the merchant country.

origin_resolved_address_state
Two-letter ISO code representing the merchant country subdivision.

quantity
Units sold as per the invoice.

quantity_decimal
Units sold as per the invoice expressed in decimal.

refund_metadata[key]
Metadata associated with a Refund object

state_code
Two-letter ISO code representing the situs country subdivision.

subtotal
Taxable or non-taxable amount.

tax_amount
Tax amount in the transaction currency.

tax_code
Unique ID for the product tax code assigned to the line item.

tax_date
Date used to determine the tax rate. It is usually the same date as the
transaction date; however, it can be different in the context of refunds. When a
credit note is issued, the `transaction_date` is the date on which the credit
note is issued, but the `tax_date` is the date when tax was calculated on the
original transaction.

tax_name
Local name of the applicable tax.

tax_rate
Tax rate applied to the line item.

tax_transaction_metadata[key]
Metadata associated with a Tax Transaction object

taxability
Indicates whether a line item is `taxable` or `non_taxable`.

taxability_reason
Reason for tax collection or non-collection.

taxable_amount
Taxable amount in the transaction currency.

total
Taxable amount plus tax or the non-taxable amount.

transaction_date
Date when the transaction is committed in the requested timezone.

type
This refers to how a transaction is processed by Stripe. Possible values are:
`invoice`, `checkout`, `payment_link`, `payment_intent`, `order`, `refund`,
`credit_note.`

## See also

- [Tax reporting overview](https://docs.stripe.com/tax/reports)

## Links

- [Tax reporting overview](https://docs.stripe.com/tax/reports)