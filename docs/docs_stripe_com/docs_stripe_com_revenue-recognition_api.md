# Revenue Recognition APIPublic preview

## Access Stripe Revenue Recognition reports programmatically to automate your accrual accounting.

For accrual accounting, Stripe Revenue Recognition provides [downloadable
reports](https://docs.stripe.com/revenue-recognition/reports), such as a
[monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
and a [revenue
waterfall](https://docs.stripe.com/revenue-recognition/reports/waterfall). You
can download these reports in CSV format through the
[Dashboard](https://dashboard.stripe.com/revenue-recognition) or you can
programmatically access them through the API.

Revenue Recognition has six supported report types:

- `revenue_recognition.debit_credit_summary.1`
- `revenue_recognition.debit_credit_by_price.1`
- `revenue_recognition.debit_credit_by_product.1`
- `revenue_recognition.debit_credit_by_customer.1`
- `revenue_recognition.debit_credit_by_invoice.1`
- `revenue_recognition.debit_credit_by_invoice_line_item.1`

#### Caution

Because this feature is in beta, the data fields might change.

## Download a report

The following example downloads the debits and credits by summary for May 2021.

First, create a report run using [Create a Report
Run](https://docs.stripe.com/api/reporting/report_run/create).

To get a report for May 2023, set `parameters[interval_start]` to 1 May 2023 and
`parameters[interval_end]` to 1 Jun 2023.

```
curl https://api.stripe.com/v1/reporting/report_runs \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d report_type="revenue_recognition.debit_credit_summary.1" \
 -d "parameters[interval_start]"=1682899200 \
 -d "parameters[interval_end]"=1685577600
```

Next, check whether the [Report
Run](https://docs.stripe.com/api/reporting/report_run/object) object succeeds by
fetching the report run object:

The report run object ID starts with `frr_`.

```
curl https://api.stripe.com/v1/reporting/report_runs/{{REPORT_RUN_OBJECT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

When the object’s `status` is `succeeded`, you can download the CSV using its
`result.id` value, as in the following example:

The report run result ID starts with `file_`.

```
curl https://files.stripe.com/v1/files/{{REPORT_RUN_RESULT_ID}}/contents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

## Report Run Parameters

Report TypeRequired Run ParametersOptional Run
Parametersrevenue_recognition.debit_credit_summary.1- `interval_start`
- `interval_end`
- `decimal_format`
revenue_recognition.debit_credit_by_price.1- `interval_start`
- `interval_end`
- `customer`
- `decimal_format`
revenue_recognition.debit_credit_by_product.1- `interval_start`
- `interval_end`
- `customer`
- `decimal_format`
revenue_recognition.debit_credit_by_customer.1- `interval_start`
- `interval_end`
- `decimal_format`
revenue_recognition.debit_credit_by_invoice.1- `interval_start`
- `interval_end`
- `customer`
- `invoice`
- `invoice_line_item`
- `decimal_format`
revenue_recognition.debit_credit_by_invoice_line_item.1- `interval_start`
- `interval_end`
- `customer`
- `invoice`
- `invoice_line_item`
- `decimal_format`

## Report Run Columns

By default, reports are run with the default set of columns. You can customize
the selection and ordering of columns in the output by including the optional
columns parameter with a [list of column
names](https://docs.stripe.com/reports/api#report-runs). You can find the
supported columns for each report type below.

### Summary

API report type: `revenue_recognition.debit_credit_summary.1`

Column NameDefaultDescriptionaccounting_periodThe accounting
periodopen_accounting_periodThe open accounting period; entries in open periods
are subject to changecurrencyThree-letter [ISO code for the
currency](https://docs.stripe.com/currencies) of the amount.debitThe debited
accountcreditThe credited accountamountAmount change, expressed in major units
of the currency (for example, dollars for USD, or pesos for
MXN).credit_gl_codeThe credited general ledger codedebit_gl_codeThe debited
general ledger code
### By Price

API report type: `revenue_recognition.debit_credit_by_price.1`

Column NameDefaultDescriptionaccounting_periodThe accounting
periodopen_accounting_periodThe open accounting period; entries in open periods
are subject to changecurrencyThree-letter [ISO code for the
currency](https://docs.stripe.com/currencies) of the amount.price_idThe price
associated with this change.debitThe debited accountcreditThe credited
accountamountAmount change, expressed in major units of the currency (for
example, dollars for USD, or pesos for MXN).credit_gl_codeThe credited general
ledger codedebit_gl_codeThe debited general ledger code
### By Product

API report type: `revenue_recognition.debit_credit_by_product.1`

Column NameDefaultDescriptionaccounting_periodThe accounting
periodopen_accounting_periodThe open accounting period; entries in open periods
are subject to changecurrencyThree-letter [ISO code for the
currency](https://docs.stripe.com/currencies) of the amount.product_idThe
product associated with this change.debitThe debited accountcreditThe credited
accountamountAmount change, expressed in major units of the currency (for
example, dollars for USD, or pesos for MXN).credit_gl_codeThe credited general
ledger codedebit_gl_codeThe debited general ledger code
### By Customer

API report type: `revenue_recognition.debit_credit_by_customer.1`

Column NameDefaultDescriptionaccounting_periodThe accounting
periodopen_accounting_periodThe open accounting period; entries in open periods
are subject to changecurrencyThree-letter [ISO code for the
currency](https://docs.stripe.com/currencies) of the amount.customer_idThe
customer associated with this change.debitThe debited accountcreditThe credited
accountamountAmount change, expressed in major units of the currency (for
example, dollars for USD, or pesos for MXN).credit_gl_codeThe credited general
ledger codedebit_gl_codeThe debited general ledger code
### By Invoice

API report type: `revenue_recognition.debit_credit_by_invoice.1`

Column NameDefaultDescriptionaccounting_periodThe accounting
periodopen_accounting_periodThe open accounting period; entries in open periods
are subject to changecurrencyThree-letter [ISO code for the
currency](https://docs.stripe.com/currencies) of the
amount.transaction_model_idThe model in Stripe associated with this change -
either an invoice line item, invoice, invoiceitem, charge, or etc.debitThe
debited accountcreditThe credited accountbooked_dateThe date that the ledger
entry is added to the books.amountAmount change, expressed in major units of the
currency (for example, dollars for USD, or pesos for MXN).debit_gl_codeThe
debited general ledger codecredit_gl_codeThe credited general ledger
codeinvoice_idThe invoice associated with this change. Standalone charges or
invoice items not associated with an invoice are `null`.invoice_line_item_idThe
ID of the invoice line_item.invoice_item_idThe ID of the invoice
iteminvoice_numberThe customer unique number associated with the
invoice.subscription_item_idThe ID of the subscription_item.price_idThe price
associated with this change. Standalone charges or invoice items not associated
with a price are `null`.product_idThe product associated with this
price.customer_idThe customer associated with this change.subscription_idThe
subscription associated with this change.charge_idThe charge associated with
this change.refund_idThe refund associated with this change.dispute_idThe
dispute associated with this change.presentment_currencyThe presentment
(customer facing) currency of the transaction.presentment_amountThe presentment
(customer facing) amount.
### By Invoice Line Item

API report type: `revenue_recognition.debit_credit_by_invoice_line_item.1`

Column NameDefaultDescriptionaccounting_periodThe accounting
periodopen_accounting_periodThe open accounting period; entries in open periods
are subject to changecurrencyThree-letter [ISO code for the
currency](https://docs.stripe.com/currencies) of the
amount.transaction_model_idThe model in Stripe associated with this change—an
invoice line item, invoice, invoice item, charge, and so on.debitThe debited
accountcreditThe credited accountbooked_dateThe date that the ledger entry is
added to the books.amountAmount change, expressed in major units of the currency
(for example, dollars for USD, or pesos for MXN).debit_gl_codeThe debited
general ledger codecredit_gl_codeThe credited general ledger codeinvoice_idThe
invoice associated with this change. Standalone charges or invoice items not
associated with an invoice are `null`.invoice_line_item_idThe ID of the invoice
line_item.invoice_item_idThe ID of the invoice itemsubscription_item_idThe ID of
the subscription_item.price_idThe price associated with this change. Standalone
charges or invoice items not associated with a price are `null`.product_idThe
product associated with this price.customer_idThe customer associated with this
change.subscription_idThe subscription associated with this change.charge_idThe
charge associated with this change.refund_idThe refund associated with this
change.dispute_idThe dispute associated with this change.presentment_currencyThe
presentment (customer facing) currency of the transaction.presentment_amountThe
presentment (customer facing) amount.
If you encounter any issues, you can contact
[revenue-recognition-api-beta@stripe.com](mailto:revenue-recognition-api-beta@stripe.com).

## Links

- [downloadable reports](https://docs.stripe.com/revenue-recognition/reports)
- [monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
- [revenue
waterfall](https://docs.stripe.com/revenue-recognition/reports/waterfall)
- [Dashboard](https://dashboard.stripe.com/revenue-recognition)
- [Create a Report Run](https://docs.stripe.com/api/reporting/report_run/create)
- [Report Run](https://docs.stripe.com/api/reporting/report_run/object)
- [list of column names](https://docs.stripe.com/reports/api#report-runs)
- [ISO code for the currency](https://docs.stripe.com/currencies)