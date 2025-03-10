# Connect report type

## Retrieve financial reports for your connected accounts using the API.

[Connect](https://docs.stripe.com/connect) platforms can use most financial
reports to view the activity in their platform account, or in one or more of
their connected accounts. In the Dashboard, the [report
setting](https://docs.stripe.com/reports/options) controls which account’s data
the report displays. By default, the API returns report data for your platform
account activity. To view data for your connected accounts, use the
Connect-specific report types listed below.

The following tables define the required and optional parameters to run the
report, as well as the schema of the CSV output.

Report typeRequired run parametersOptional run
parameters`connected_account_balance_change_from_activity.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-balance-change-from-activity-itemized-1)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_balance_change_from_activity.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-balance-change-from-activity-itemized-2)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_balance_change_from_activity.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-balance-change-from-activity-itemized-3)-
`interval_start`
- `interval_end`
- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_balance_change_from_activity.summary.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-balance-change-from-activity-summary-1)-
`interval_start`
- `interval_end`
- `currency`
- `connected_account`
- `timezone`
- `columns`

`connected_account_payouts.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payouts-itemized-1)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payouts.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payouts-itemized-2)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payouts.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payouts-itemized-3)-
`interval_start`
- `interval_end`
- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payouts.summary.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payouts-summary-1)-
`interval_start`
- `interval_end`
- `currency`
- `connected_account`
- `timezone`
- `columns`

`connected_account_balance.summary.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-balance-summary-1)-
`interval_start`
- `interval_end`
- `timezone`
- `currency`
- `connected_account`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-ending-balance-reconciliation-itemized-1)-
`interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-ending-balance-reconciliation-itemized-2)-
`interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-ending-balance-reconciliation-itemized-3)-
`interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `timezone`
- `decimal_separator`
- `columns`

`connected_account_ending_balance_reconciliation.summary.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-ending-balance-reconciliation-summary-1)-
`interval_end`
- `connected_account`
- `currency`
- `timezone`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-by-id-itemized-1)-
`connected_account`
- `payout`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-by-id-itemized-2)-
`connected_account`
- `payout`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-by-id-itemized-3)-
`connected_account`
- `payout`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.4`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-by-id-itemized-4)-
`connected_account`
- `payout`
- `timezone`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.summary.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-by-id-summary-1)-
`connected_account`
- `payout`
- `columns`

`connected_account_payout_reconciliation.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-itemized-1)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-itemized-2)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-itemized-3)-
`interval_start`
- `interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.4`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-itemized-4)-
`interval_start`
- `interval_end`
- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.summary.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-summary-1)-
`interval_start`
- `interval_end`
- `currency`
- `connected_account`
- `timezone`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.4`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-ending-balance-reconciliation-itemized-4)-
`interval_end`
- `connected_account`
- `currency`
- `reporting_category`
- `timezone`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.5`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-payout-reconciliation-itemized-5)-
`interval_start`
- `interval_end`
- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connect.negative_balance_refunds_disputes_overview.1`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connect-negative-balance-refunds-disputes-overview-1)-
`interval_end`

`connected_account_tax.transactions.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/connect#schema-connected-account-tax-transactions-itemized-2)-
`interval_start`
- `interval_end`
- `connected_account`
- `timezone`
- `decimal_separator`
- `columns`

### Connected account itemized balance change from activity

API report type: `connected_account_balance_change_from_activity.itemized.1`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_method_type
The type of payment method used in the related payment.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized balance change from activity

API report type: `connected_account_balance_change_from_activity.itemized.2`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_address_city
City of the card address associated with this charge, if any

card_address_country
Country of the card address associated with this charge, if any

card_address_line1
First line of the card address associated with this charge, if any

card_address_line2
Second line of the card address associated with this charge, if any

card_address_postal_code
Postal code of the card address associated with this charge, if any

card_address_state
State of the card address associated with this charge, if any

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_address_city
City of the customer address associated with this charge, if any

customer_address_country
Country of the customer address associated with this charge, if any

customer_address_line1
First line of the customer address associated with this charge, if any

customer_address_line2
Second line of the customer address associated with this charge, if any

customer_address_postal_code
Postal code of the customer address associated with this charge, if any

customer_address_state
State of the customer address associated with this charge, if any

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

customer_shipping_address_city
City of the customer shipping address associated with this charge, if any

customer_shipping_address_country
Country of the customer shipping address associated with this charge, if any

customer_shipping_address_line1
First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2
Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_code
Postal code of the customer shipping address associated with this charge, if any

customer_shipping_address_state
State of the customer shipping address associated with this charge, if any

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

invoice_number
Unique Number for the invoice associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized balance change from activity

API report type: `connected_account_balance_change_from_activity.itemized.3`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested timezone, or UTC if not provided. This is also when
the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_at_utc
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in the requested timezone, or UTC if not provided.

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_address_city
City of the card address associated with this charge, if any

card_address_country
Country of the card address associated with this charge, if any

card_address_line1
First line of the card address associated with this charge, if any

card_address_line2
Second line of the card address associated with this charge, if any

card_address_postal_code
Postal code of the card address associated with this charge, if any

card_address_state
State of the card address associated with this charge, if any

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in the requested
timezone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created
Time at which the balance transaction was created. Dates in the requested
timezone, or UTC if not provided.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_address_city
City of the customer address associated with this charge, if any

customer_address_country
Country of the customer address associated with this charge, if any

customer_address_line1
First line of the customer address associated with this charge, if any

customer_address_line2
Second line of the customer address associated with this charge, if any

customer_address_postal_code
Postal code of the customer address associated with this charge, if any

customer_address_state
State of the customer address associated with this charge, if any

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

customer_shipping_address_city
City of the customer shipping address associated with this charge, if any

customer_shipping_address_country
Country of the customer shipping address associated with this charge, if any

customer_shipping_address_line1
First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2
Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_code
Postal code of the customer shipping address associated with this charge, if any

customer_shipping_address_state
State of the customer shipping address associated with this charge, if any

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

invoice_number
Number for the invoice associated with this balance transaction. Available for
charges, refunds, and disputes made in connection with a Stripe Billing invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected account balance change from activity summary

API report type: `connected_account_balance_change_from_activity.summary.1`

Column nameDefaultDescriptioncount
The number of transactions associated with the `reporting_category`.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

fee
Sum of the fees paid for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

gross
Sum of the gross amounts of the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

net
Sum of the net amounts for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

### Connected account itemized payouts

API report type: `connected_account_payouts.itemized.1`

Column nameDefaultDescriptionbalance_transaction_id
Unique identifier for the balance transaction.

connected_account
Unique identifier for the Stripe account associated with this line.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

effective_at_utc
For [automatic payouts](https://stripe.com/docs/payouts#payout-schedule), this
is the date we expect funds to arrive in your bank account. For [manual
payouts](https://stripe.com/docs/payouts#manual-payouts), this is the date the
payout was initiated. In both cases, it’s the date the paid-out funds are
deducted from your Stripe balance. All dates in UTC.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payout_description
An arbitrary string attached to the payout. Often useful for displaying to
users.

payout_destination_id
ID of the bank account or card the payout was sent to.

payout_expected_arrival_date
Date the payout is scheduled to arrive in the bank. This factors in delays like
weekends or bank holidays. Dates in UTC.

payout_id
The Stripe object to which this transaction is related.

payout_reversed_at
Typically this field will be empty. However, if the payout’s status is
`canceled` or `failed`, this field will reflect the time at which it entered
that status.

payout_status
Current status of the payout (`paid`, `pending`, `in_transit`, `canceled` or
`failed`). A payout will be `pending` until it is submitted to the bank, at
which point it becomes `in_transit`. It will then change to `paid` if the
transaction goes through. If it does not go through successfully, its status
will change to `failed` or `canceled`.

payout_type
Can be `bank_account` or `card`.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized payouts

API report type: `connected_account_payouts.itemized.2`

Column nameDefaultDescriptionbalance_transaction_id
Unique identifier for the balance transaction.

connected_account
Unique identifier for the Stripe account associated with this line.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

effective_at_utc
For [automatic payouts](https://stripe.com/docs/payouts#payout-schedule), this
is the date we expect funds to arrive in your bank account. For [manual
payouts](https://stripe.com/docs/payouts#manual-payouts), this is the date the
payout was initiated. In both cases, it’s the date the paid-out funds are
deducted from your Stripe balance. All dates in UTC.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payout_description
An arbitrary string attached to the payout. Often useful for displaying to
users.

payout_destination_id
ID of the bank account or card the payout was sent to.

payout_expected_arrival_date
Date the payout is scheduled to arrive in the bank. This factors in delays like
weekends or bank holidays. Dates in UTC.

payout_id
The Stripe object to which this transaction is related.

payout_reversed_at
Typically this field will be empty. However, if the payout’s status is
`canceled` or `failed`, this field will reflect the time at which it entered
that status.

payout_status
Current status of the payout (`paid`, `pending`, `in_transit`, `canceled` or
`failed`). A payout will be `pending` until it is submitted to the bank, at
which point it becomes `in_transit`. It will then change to `paid` if the
transaction goes through. If it does not go through successfully, its status
will change to `failed` or `canceled`.

payout_type
Can be `bank_account` or `card`.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized payouts

API report type: `connected_account_payouts.itemized.3`

Column nameDefaultDescriptionbalance_transaction_id
Unique identifier for the balance transaction.

connected_account
Unique identifier for the Stripe account associated with this line.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

effective_at
For [automatic payouts](https://stripe.com/docs/payouts#payout-schedule), this
is the date we expect funds to arrive in your bank account. For [manual
payouts](https://stripe.com/docs/payouts#manual-payouts), this is the date the
payout was initiated. In both cases, it’s the date the paid-out funds are
deducted from your Stripe balance. All dates in the requested timezone, or UTC
if not provided.

effective_at_utc
For [automatic payouts](https://stripe.com/docs/payouts#payout-schedule), this
is the date we expect funds to arrive in your bank account. For [manual
payouts](https://stripe.com/docs/payouts#manual-payouts), this is the date the
payout was initiated. In both cases, it’s the date the paid-out funds are
deducted from your Stripe balance. All dates in UTC.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payout_description
An arbitrary string attached to the payout. Often useful for displaying to
users.

payout_destination_id
ID of the bank account or card the payout was sent to.

payout_expected_arrival_date
Date the payout is scheduled to arrive in the bank. This factors in delays like
weekends or bank holidays.

payout_id
The Stripe object to which this transaction is related.

payout_reversed_at
Typically this field will be empty. However, if the payout’s status is
`canceled` or `failed`, this field will reflect the time at which it entered
that status. Times in the requested timezone, or UTC if not provided.

payout_reversed_at_utc
Typically this field will be empty. However, if the payout’s status is
`canceled` or `failed`, this field will reflect the time at which it entered
that status. Times in UTC.

payout_status
Current status of the payout (`paid`, `pending`, `in_transit`, `canceled` or
`failed`). A payout will be `pending` until it is submitted to the bank, at
which point it becomes `in_transit`. It will then change to `paid` if the
transaction goes through. If it does not go through successfully, its status
will change to `failed` or `canceled`.

payout_type
Can be `bank_account` or `card`.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account payouts summary

API report type: `connected_account_payouts.summary.1`

Column nameDefaultDescriptioncount
The number of transactions associated with the `reporting_category`.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

fee
Sum of the fees paid for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

gross
Sum of the gross amounts of the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

net
Sum of the net amounts for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

### Connected account balance summary

API report type: `connected_account_balance.summary.1`

Column nameDefaultDescriptioncategory
One of `starting_balance`, `ending_balance`, `activity` or `payouts`.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `net_amount` is defined.

description
One of `Starting balance (YYYY-MM-DD)` - the balance at the start of the period,
`Activity` - the net amount of all transactions that affected your balance
except for payouts, `Total payouts` - the amount of payouts to your bank
account, or `Ending balance (YYYY-MM-DD)` - the balance left over at the end of
the period after subtracting payouts from the `Starting balance` and `Activity`.

net_amount
Net amount for the transactions associated with `category`. Expressed in major
units of the currency (e.g. dollars for USD, yen for JPY).

### Connected account itemized ending balance reconciliation

API report type: `connected_account_ending_balance_reconciliation.itemized.1`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_method_type
The type of payment method used in the related payment.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized ending balance reconciliation

API report type: `connected_account_ending_balance_reconciliation.itemized.2`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_address_city
City of the card address associated with this charge, if any

card_address_country
Country of the card address associated with this charge, if any

card_address_line1
First line of the card address associated with this charge, if any

card_address_line2
Second line of the card address associated with this charge, if any

card_address_postal_code
Postal code of the card address associated with this charge, if any

card_address_state
State of the card address associated with this charge, if any

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_address_city
City of the customer address associated with this charge, if any

customer_address_country
Country of the customer address associated with this charge, if any

customer_address_line1
First line of the customer address associated with this charge, if any

customer_address_line2
Second line of the customer address associated with this charge, if any

customer_address_postal_code
Postal code of the customer address associated with this charge, if any

customer_address_state
State of the customer address associated with this charge, if any

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

customer_shipping_address_city
City of the customer shipping address associated with this charge, if any

customer_shipping_address_country
Country of the customer shipping address associated with this charge, if any

customer_shipping_address_line1
First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2
Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_code
Postal code of the customer shipping address associated with this charge, if any

customer_shipping_address_state
State of the customer shipping address associated with this charge, if any

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

invoice_number
Unique Number for the invoice associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized ending balance reconciliation

API report type: `connected_account_ending_balance_reconciliation.itemized.3`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested timezone, or UTC if not provided. This is also when
the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_at_utc
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in the requested timezone, or UTC if not provided.

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in the requested
timezone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created
Time at which the balance transaction was created. Dates in the requested
timezone, or UTC if not provided.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_method_type
The type of payment method used in the related payment.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account ending balance reconciliation summary

API report type: `connected_account_ending_balance_reconciliation.summary.1`

Column nameDefaultDescriptioncount
The number of transactions associated with the `reporting_category`.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

fee
Sum of the fees paid for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

gross
Sum of the gross amounts of the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

net
Sum of the net amounts for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

### Connected account itemized single payout reconciliation

API report type: `connected_account_payout_reconciliation.by_id.itemized.1`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized single payout reconciliation

API report type: `connected_account_payout_reconciliation.by_id.itemized.2`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized single payout reconciliation

API report type: `connected_account_payout_reconciliation.by_id.itemized.3`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_method_type
The type of payment method used in the related payment.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized single payout reconciliation

API report type: `connected_account_payout_reconciliation.by_id.itemized.4`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested timezone, or UTC if not provided. This is also when
the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_at_utc
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in the requested timezone, or UTC if not provided.

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in the requested
timezone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created
Time at which the balance transaction was created. Dates in the requested
timezone, or UTC if not provided.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected account single payout reconciliation summary

API report type: `connected_account_payout_reconciliation.by_id.summary.1`

Column nameDefaultDescriptioncount
The number of transactions associated with the `reporting_category`.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

fee
Sum of the fees paid for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

gross
Sum of the gross amounts of the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

net
Sum of the net amounts for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

### Connected account itemized date-ranged payout reconciliation

API report type: `connected_account_payout_reconciliation.itemized.1`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized date-ranged payout reconciliation

API report type: `connected_account_payout_reconciliation.itemized.2`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account itemized date-ranged payout reconciliation

API report type: `connected_account_payout_reconciliation.itemized.3`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_address_city
City of the card address associated with this charge, if any

card_address_country
Country of the card address associated with this charge, if any

card_address_line1
First line of the card address associated with this charge, if any

card_address_line2
Second line of the card address associated with this charge, if any

card_address_postal_code
Postal code of the card address associated with this charge, if any

card_address_state
State of the card address associated with this charge, if any

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_address_city
City of the customer address associated with this charge, if any

customer_address_country
Country of the customer address associated with this charge, if any

customer_address_line1
First line of the customer address associated with this charge, if any

customer_address_line2
Second line of the customer address associated with this charge, if any

customer_address_postal_code
Postal code of the customer address associated with this charge, if any

customer_address_state
State of the customer address associated with this charge, if any

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

customer_shipping_address_city
City of the customer shipping address associated with this charge, if any

customer_shipping_address_country
Country of the customer shipping address associated with this charge, if any

customer_shipping_address_line1
First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2
Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_code
Postal code of the customer shipping address associated with this charge, if any

customer_shipping_address_state
State of the customer shipping address associated with this charge, if any

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

invoice_number
Unique Number for the invoice associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized date-ranged payout reconciliation

API report type: `connected_account_payout_reconciliation.itemized.4`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested timezone, or UTC if not provided. This is also when
the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_at_utc
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in the requested timezone, or UTC if not provided.

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in the requested
timezone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created
Time at which the balance transaction was created. Dates in the requested
timezone, or UTC if not provided.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_method_type
The type of payment method used in the related payment.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

### Connected account date-ranged payouts reconciliation summary

API report type: `connected_account_payout_reconciliation.summary.1`

Column nameDefaultDescriptioncount
The number of transactions associated with the `reporting_category`.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

fee
Sum of the fees paid for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

gross
Sum of the gross amounts of the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

net
Sum of the net amounts for the transactions associated with the
`reporting_category`. Expressed in major units of the currency (e.g. dollars for
USD, yen for JPY).

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

### Connected account itemized ending balance reconciliation

API report type: `connected_account_ending_balance_reconciliation.itemized.4`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested timezone, or UTC if not provided. This is also when
the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_at_utc
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in the requested timezone, or UTC if not provided.

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_address_city
City of the card address associated with this charge, if any

card_address_country
Country of the card address associated with this charge, if any

card_address_line1
First line of the card address associated with this charge, if any

card_address_line2
Second line of the card address associated with this charge, if any

card_address_postal_code
Postal code of the card address associated with this charge, if any

card_address_state
State of the card address associated with this charge, if any

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in the requested
timezone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created
Time at which the balance transaction was created. Dates in the requested
timezone, or UTC if not provided.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_address_city
City of the customer address associated with this charge, if any

customer_address_country
Country of the customer address associated with this charge, if any

customer_address_line1
First line of the customer address associated with this charge, if any

customer_address_line2
Second line of the customer address associated with this charge, if any

customer_address_postal_code
Postal code of the customer address associated with this charge, if any

customer_address_state
State of the customer address associated with this charge, if any

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

customer_shipping_address_city
City of the customer shipping address associated with this charge, if any

customer_shipping_address_country
Country of the customer shipping address associated with this charge, if any

customer_shipping_address_line1
First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2
Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_code
Postal code of the customer shipping address associated with this charge, if any

customer_shipping_address_state
State of the customer shipping address associated with this charge, if any

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

invoice_number
Number for the invoice associated with this balance transaction. Available for
charges, refunds, and disputes made in connection with a Stripe Billing invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized date-ranged payout reconciliation

API report type: `connected_account_payout_reconciliation.itemized.5`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested timezone, or UTC if not provided. This is also when
the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_at_utc
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in UTC. This is also when the paid-out funds are deducted from your
Stripe balance.

automatic_payout_id
ID of the automatically created payout associated with this balance transaction
(only set if your account is on an [automatic payout
schedule](https://stripe.com/docs/payouts#payout-schedule)).

available_on
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in the requested timezone, or UTC if not provided.

available_on_utc
The date the balance transaction’s net funds will become available in the Stripe
balance. Dates in UTC.

balance_transaction_id
Unique identifier for the balance transaction.

card_address_city
City of the card address associated with this charge, if any

card_address_country
Country of the card address associated with this charge, if any

card_address_line1
First line of the card address associated with this charge, if any

card_address_line2
Second line of the card address associated with this charge, if any

card_address_postal_code
Postal code of the card address associated with this charge, if any

card_address_state
State of the card address associated with this charge, if any

card_brand
[Card brand](https://stripe.com/docs/api#card_object-brand), if applicable.

card_country
Two-letter ISO code representing the country of the card.

card_funding
Card [funding type](https://stripe.com/docs/api#account_card_object-funding), if
applicable.

charge_created
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in the requested
timezone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account
Unique identifier for the Stripe account associated with this line.

created
Time at which the balance transaction was created. Dates in the requested
timezone, or UTC if not provided.

created_utc
Time at which the balance transaction was created. Dates in UTC.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which `gross`, `fee` and `net` are defined.

customer_address_city
City of the customer address associated with this charge, if any

customer_address_country
Country of the customer address associated with this charge, if any

customer_address_line1
First line of the customer address associated with this charge, if any

customer_address_line2
Second line of the customer address associated with this charge, if any

customer_address_postal_code
Postal code of the customer address associated with this charge, if any

customer_address_state
State of the customer address associated with this charge, if any

customer_description
Description provided when creating the customer, often used to store the
customer name.

customer_email
Email address of the customer, if any, associated with this balance transaction.

customer_facing_amount
For transactions associated with charges, refunds, or disputes, the amount of
the original charge, refund, or dispute. If the customer was charged in a
different currency than your account’s default, this field will reflect the
amount as seen by the customer.

customer_facing_currency
For transactions associated with charges, refunds, or disputes, the three-letter
[ISO currency code](https://stripe.com/docs/currencies) for
`customer_facing_amount`.

customer_id
The unique ID of the related customer, if any.

customer_name
Name of the customer, if any, associated with this balance transaction.

customer_shipping_address_city
City of the customer shipping address associated with this charge, if any

customer_shipping_address_country
Country of the customer shipping address associated with this charge, if any

customer_shipping_address_line1
First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2
Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_code
Postal code of the customer shipping address associated with this charge, if any

customer_shipping_address_state
State of the customer shipping address associated with this charge, if any

description
An arbitrary string attached to the balance transaction. Often useful for
displaying to users.

dispute_reason
Reason given by cardholder for dispute. Read more about [dispute
reasons](https://stripe.com/docs/disputes/categories).

fee
Fees paid for this transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

gross
Gross amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

invoice_id
Unique ID for the invoice associated with this balance transaction. Available
for charges, refunds, and disputes made in connection with a Stripe Billing
invoice.

invoice_number
Unique Number for the invoice associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing invoice.

is_link
Whether or not the payment was made using Link.

net
Net amount of the transaction. Expressed in major units of the currency (e.g.
dollars for USD, yen for JPY).

payment_intent_id
The unique ID of the related Payment Intent, if any.

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

payment_method_type
The type of payment method used in the related payment.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

regulatory_tag
​​An identifier reflecting the classification of this transaction according to
local regulations, if applicable. Accounts with automatic payouts enabled
receive a separate payout for each regulatory tag. ​​This column is only
populated for Brazilian accounts.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

shipping_address_city
City of the shipping address associated with this charge, if any

shipping_address_country
Country of the shipping address associated with this charge, if any

shipping_address_line1
First line of the shipping address associated with this charge, if any

shipping_address_line2
Second line of the shipping address associated with this charge, if any

shipping_address_postal_code
Postal code of the shipping address associated with this charge, if any

shipping_address_state
State of the shipping address associated with this charge, if any

source_id
The Stripe object to which this transaction is related.

source_transaction_id
The source transaction id in case of Separate Charges & Transfers and
destination charges

statement_descriptor
The dynamic statement descriptor or suffix specified when the related charge was
created.

subscription_id
Unique ID for the subscription associated with this balance transaction.
Available for charges, refunds, and disputes made in connection with a Stripe
Billing subscription.

trace_id
[Trace ID](https://stripe.com/docs/payouts/trace-id) is a unique identifier
generated by bank for the Stripe payouts. Used by banks to locate specific
transfers, sometimes referred to as a Reference number.

trace_id_status
The status of the trace ID. Either `pending`, `unsupported` or `supported`.

transfer_metadata[key]
Metadata associated with the related transfer object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

### Connected accounts with negative balances disputes and refunds

API report type: `connect.negative_balance_refunds_disputes_overview.1`

Column nameDefaultDescriptionaccount_id
The ID of the connected account.

balance
The balance of the connected account, including both available and pending
funds.

balance_24hr_net_change
The 24 hour net change in balance for the connected account.

balance_excluding_pending_debits
The balance, excluding [pending
debits](https://stripe.com/docs/connect/account-balances#accounting-for-negative-balances).

business_name
The business name of the connected account.

country
Two-letter ISO code representing the account’s country.

currency
Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) in
which the balance, refunded amount, and disputed amount are defined.

dispute_pct_change
The percent change in disputes in the past 7 days compared to the preceding
period.

disputed_amount_7d
The total amount disputed in the past 7 days related to the connected account.

disputed_amount_7d_prev
The total amount disputed in the past 7 days prior to the most recent 7 days
related to the connected account.

has_24hr_negative_balance_change
Whether the account has had their balance go negative in the past 24 hours.

has_high_disputes
Whether the account has been tagged as having high disputes.

has_high_refunds
Whether the account has been tagged as having high refunds.

pending_debits
The sum of
[debits](https://stripe.com/docs/connect/account-balances#accounting-for-negative-balances)
that are currently pending or in transit on the connected account.

refund_pct_change
The percent change in refunds in the past 7 days compared to the preceding
period.

refunded_amount_7d
The total amount refunded in the past 7 days related to the connected account.

refunded_amount_7d_prev
The total amount refunded in the past 7 days prior to the most recent 7 days
related to the connected account.

### Connected account itemized tax transactions

API report type: `connected_account_tax.transactions.itemized.2`

Column nameDefaultDescriptionconnected_account
Unique ID for the Connected account associated with this line.

country_code
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
Date used to determine the tax rate. It’s usually the same date as the
transaction date, but can vary for refunds. When a credit note is issued, the
`transaction_date` is when the credit note was issued. The `tax_date` is when
tax was calculated on the original transaction.

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
How a transaction is processed by Stripe. Possible values are: `invoice`,
`checkout`, `payment_link`, `payment_intent`, `order`, `refund`, `credit_note.`

## Links

- [Connect](https://docs.stripe.com/connect)
- [report setting](https://docs.stripe.com/reports/options)
- [automatic payout](https://stripe.com/docs/payouts#payout-schedule)
- [Card brand](https://stripe.com/docs/api#card_object-brand)
- [funding type](https://stripe.com/docs/api#account_card_object-funding)
- [ISO code for the currency](https://stripe.com/docs/currencies)
- [Reporting Category](https://stripe.com/docs/reporting/reporting-categories)
- [Trace ID](https://stripe.com/docs/payouts/trace-id)
- [dispute reasons](https://stripe.com/docs/disputes/categories)
- [manual payouts](https://stripe.com/docs/payouts#manual-payouts)
- [pending
debits](https://stripe.com/docs/connect/account-balances#accounting-for-negative-balances)