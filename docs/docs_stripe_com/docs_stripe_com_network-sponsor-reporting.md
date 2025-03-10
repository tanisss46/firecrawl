# Network Sponsor Reporting

## Learn about the available reports for our network sponsors.

## Stripe Reports

All reports are provided as CSV files over SFTP. The available reports are:

- **Daily Settlement Report**: a same-day summary report of transaction volume
- **Clearing Transaction Detail Report**: a daily transaction-level report of
cleared transactions
- **Dispute Event Report**: a daily transaction-level report of events related
to disputes
- **Transaction Summary Report**: a periodic per-merchant summary of processed
volume
- **Merchant Report**: a list of events related to merchant metadata

Filenames are customizable.

### CSV

CSV files are as described in [RFC 4180](https://tools.ietf.org/html/rfc4180):

- Fields are optionally delimited by `"` quotes.- When they’re, `""` inside is
used to represent a single quote and fields can contain commas
- In the example below, the first value is `"quoted, field"`
- Dates will always be in `YYYY-MM-DD` format and in UTC time.
- Headers will always be present
- Blank fields will either be an empty delimited field (`""`) or just nothing
between commas. Both the `example_header` and `a_date_field` values in the
second row of the below sample are empty.

#### Sample

```
example_header,a_date_field,an_amount,a_currency
"""quoted, field""",2016-06-03,12345,usd
"",,12345,jpy

```

### Amounts

Amounts are always:

- provided as an integer
- accompanied by a three-letter currency code
- in the smallest unit for the currency (cents, pence, centavos, etc)

For example `12345,usd` is USD $123.45 and `12345,jpy` is JPY ¥12345

### Backward compatibility

In the same vein as our [API Backward-Compatibility
Guidelines](https://docs.stripe.com/upgrades#what-changes-does-stripe-consider-to-be-backward-compatible),
we consider the following changes to be backward compatible:

- Adding new rightmost columns to the CSV reports
- Adding new values to `type` fields

## Daily Settlement Report

Each line of this report is a summary of transactions for one reconciliation
window for Visa and Mastercard.

### Fields

- `brand`: either `visa` or `mastercard`
- `network_numeric`: for Visa, the BIN; for Mastercard, the ICA.
- `settlement_service`: an identifier for the settlement service used for the
transactions- For Visa, see the full list of possible values below
- For Mastercard, the identifier from the *Settlement Manual* is used
- `reconciliation_date`: the processing date in `YYYY-MM-DD` format.
- `reconciliation_cycle`: which cycle is summarized
- `type`: which transactions are included in the aggregation. Valid values are:-
`first_presentment`
- `first_chargeback`
- `second_presentment`
- `second_chargeback`(includes prearbitration withdrawals for Visa)
- `interchange` (interchange reimbursement fees)
- `scheme_fee`
- `miscellaneous`
- `amount`: the amount as an integer number of minor units, possibly with a
leading `-` to denote a negative amount. Amounts in this report are relative to
Stripe, so a positive amount means money flowing to Stripe.
- `currency`: the three-letter currency code

### Sample

```

brand,network_numeric,settlement_service,reconciliation_date,reconciliation_cycle,type,amount,currency
mastercard,010100,US00000001,2017-03-24,1,first_presentment,3800,usd
mastercard,010100,US00000001,2017-03-24,1,interchange,-21,usd
mastercard,010100,US00000001,2017-03-24,2,scheme_fee,-1000,usd
visa,444000,international,2017-03-24,1,first_presentment,247400,usd
visa,444000,international,2017-03-24,1,interchange,-784,usd

```

## Clearing Transaction Detail Report

This report contains records for cleared charges and refunds. It has a number of
limitations:

- Some of the listed transactions may later fail in clearing. This means that
this report cannot be reconciled against other reports counting successfully
settled transactions.
- The clearing date in this report reflects the date the clearing attempt was
created internally within Stripe, and may not be the same as the date the
transaction is eventually processed.
- The amount is in the presentment currency of the transaction, so cannot be
used to reconcile to cash.

### Fields

- `date`: the date this transaction was submitted for clearing
- `brand`: either `visa` or `mastercard`
- `merchant`: the unique identifier assigned by Stripe
- `card_number`: the first six and last four digits of the card number,
separated with an asterisk `*`
- `acquirer_reference_number`: the acquirer reference number sent with clearing
- `type`: the type of transaction. One of:- `charge`
- `refund`
- `amount`: the transaction amount
- `currency`: the three-letter transaction currency code
- `raw__visa_moto`: the raw Visa MOTO/ECI value. Only populated for Visa
transactions
- `raw__mastercard_sli`: the raw Mastercard Security Level Indicator value. Only
populated for Mastercard transactions

### Sample

```

date,brand,merchant,card_number,acquirer_reference_number,type,amount,currency,raw__visa_moto,raw__mastercard_sli

2017-03-22,visa,400009*1234,ZX2DSEDKGX7WDYZMWFAQEPG,74242429888000000000011,charge,1800,usd,07,

2017-03-23,visa,456721*0017,ZX2DSEDKGX7WDYZMWFAQEPG,74242429888000000000029,charge,1000,usd,01,

2017-03-24,mastercard,510789*2010,ZX2DSEDKGX7WDYZMWFAQEPG,85242429888000000000055,refund,523,gbp,,210,

2017-03-24,visa,400009*1234,XZPWCHXWVG9ZRK6JFPFSZC4,74242429888000000000034,charge,6400,eur,05,

```

## Dispute Events Report

This report contains records of events related to transaction Disputes.

### Fields

- `date`: the date of the incoming record
- `brand`: either `visa` or `mastercard`
- `merchant`: the unique identifier assigned by Stripe
- `card_number`: the first six and last four digits of the card number,
separated with an asterisk `*`
- `acquirer_reference_number`: the acquirer reference number sent with clearing
- `type`: the type of event. One of:- `retrieval`
- `first_chargeback`
- `first_chargeback_reversal`
- `representment`
- `representment_reversal`
- `second_chargeback`
- `second_chargeback_reversal`
- `prearbitration`
- `amount`: the chargeback amount
- `currency`: the three-letter currency code
- `reason_code`: the raw Visa or Mastercard reason code

### Sample

```

date,brand,merchant,card_number,acquirer_reference_number,type,amount,currency,reason_code

2017-03-24,visa,400009*1234,ZX2DSEDKGX7WDYZMWFAQEPG,74242429888000000000011,first_chargeback,1800,usd,78

2017-03-24,mastercard,510789*2010,ZX2DSEDKGX7WDYZMWFAQEPG,85242429888000000000055,second_chargeback,900,gbp,3001

```

## Transaction Summary Report

This report breaks down transactions by merchant for a given period of time. It
is available on a daily, weekly, or monthly basis. Rows are aggregated by:

- Merchant
- Transaction Type
- Presentment Currency

Chargebacks and refunds are counted in the time period that they themselves
occur, not the one in which the original transaction did.

### Fields

- `merchant`: the unique identifier assigned by Stripe
- `range_start`: the first date included in this aggregation, in `YYYY-MM-DD`
format
- `range_end`: the last date included in this aggregation, in `YYYY-MM-DD`
format
- `brand`: either `visa` or `mastercard`
- `type`: what type of transaction is being aggregated- `charge`
- `full_refund`
- `partial_refund`
- `chargeback`
- `count`: the number of transactions
- `amount`: the sum of the transaction amounts
- `currency`: the three-letter currency code of the transaction

### Sample

```
merchant,range_start,range_end,brand,type,count,amount,currency
ZX2DSEDKGX7WDYZMWFAQEPG,2017-03-01,2017-03-31,visa,charge,3,1500,usd
ZX2DSEDKGX7WDYZMWFAQEPG,2017-03-01,2017-03-31,mastercard,charge,2,1000,usd
ZX2DSEDKGX7WDYZMWFAQEPG,2017-03-01,2017-03-31,visa,charge,1,600,gbp
ZX2DSEDKGX7WDYZMWFAQEPG,2017-03-01,2017-03-31,mastercard,full_refund,1,500,usd
ZX2DSEDKGX7WDYZMWFAQEPG,2017-03-01,2017-03-31,visa,partial_refund,1,200,gbp
ZX2DSEDKGX7WDYZMWFAQEPG,2017-03-01,2017-03-31,visa,chargeback,1,500,usd
XZPWCHXWVG9ZRK6JFPFSZC4,2017-03-01,2017-03-31,mastercard,charge,2,66998,usd
XZPWCHXWVG9ZRK6JFPFSZC4,2017-03-01,2017-03-31,visa,charge,1,333333,jpy

```

## Merchant Report

This report provides information about the merchants transacting on Stripe.

- It can be provided daily, weekly, monthly, or quarterly. Monthly or quarterly
reports will be a full copy of the portfolio each time, whereas weekly or daily
ones will be just changes.
- The exact selection and ordering of fields in this report can be configured
depending on the details of the Network Sponsor’s requirements and the country
of operation.
- Merchants are included in this report when they have settled three live
transactions.

### Available Fields

- `report_date`: the date of the report and event, in `YYYY-MM-DD` format
- `event`: what happened to this merchant?- `onboarded`: this is a new merchant
- `updated`: the merchant has updated information. When a merchant is updated,
the row for them in this report will still include all of their information.
- `offboarded`: the merchant is no longer processing with Stripe
- `merchant`: the unique identifier assigned by Stripe
- `business_dba`: the merchant’s business name
- `business_type`: the merchant’s business type
- `tax_id`: a tax identification number for this merchant. It will be blank if
it does not apply
- `address_line1`: merchant’s address line 1
- `address_line2`: merchant’s address line 2
- `city`: merchant city
- `region`: merchant region, meaning depends on country
- `postal_code`: merchant postal code, meaning depends on country, might be
blank
- `country`: merchant country
- `representative_first_name`: the first name of the merchant’s legal
representative
- `representative_last_name`: the first name of the merchant’s legal
representative
- `representative_dob`: the Date of Birth for a representative, in `YYYY-MM-DD`
format.
- `merchant_url`: the merchant’s website
- `mcc`: the MCC the merchant will be using
- `email`: the MCC the merchant will be using
- `bank_account_last4`: the last four digits of the merchant’s attached bank
account. Will be blank if the merchant hasn’t yet attached a bank account.

### Sample

```
report_date,merchant,event,tax_id,business_dba
2017-03-31,ZX2DSEDKGX7WDYZMWFAQEPG,updated,123-45-6789,"Computers, and More"
2017-03-31,XZPWCHXWVG9ZRK6JFPFSZC4,onboarded,987-65-4321,"Delivery Cupcakes"
2017-03-31,8MPJSJC3OVHR0VCM4Z0OJOV,offboarded,111-111-1111,"Prohibited Business
Llc."

```

## Links

- [RFC 4180](https://tools.ietf.org/html/rfc4180)
- [API Backward-Compatibility
Guidelines](https://docs.stripe.com/upgrades#what-changes-does-stripe-consider-to-be-backward-compatible)