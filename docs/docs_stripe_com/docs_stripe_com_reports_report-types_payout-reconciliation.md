# Payout reconciliation report type

## Review the Payout reconciliation report schema and parameters.

The Payout reconciliation report returns data related to the payouts your
receive in your bank account to help you match them to the transactions they
relate to. Run this report to use the returned data in your API calls. You can
also download the CSV from the [Payment fees
report](https://dashboard.stripe.com/reports/reconciliation) in the Dashboard.

The following tables define the required and optional parameters to run the
report, as well as the schema of the CSV output.

Report typeRequired run parametersOptional run
parameters`ending_balance_reconciliation.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-ending-balance-reconciliation-itemized-1)-
`interval_end`
- `currency`
- `reporting_category`
- `columns`

`ending_balance_reconciliation.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-ending-balance-reconciliation-itemized-2)-
`interval_end`
- `currency`
- `reporting_category`
- `columns`

`ending_balance_reconciliation.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-ending-balance-reconciliation-itemized-3)-
`interval_end`
- `currency`
- `reporting_category`
- `timezone`
- `columns`

`ending_balance_reconciliation.itemized.4`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-ending-balance-reconciliation-itemized-4)-
`interval_end`
- `currency`
- `reporting_category`
- `timezone`
- `decimal_separator`
- `columns`

`payout_reconciliation.itemized.5`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-itemized-5)-
`interval_start`
- `interval_end`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.by_id.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-by-id-itemized-1)-
`payout`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.by_id.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-by-id-itemized-2)-
`payout`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.by_id.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-by-id-itemized-3)-
`payout`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.by_id.itemized.4`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-by-id-itemized-4)-
`payout`
- `reporting_category`
- `timezone`
- `decimal_separator`
- `columns`

`payout_reconciliation.by_id.summary.1`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-by-id-summary-1)-
`payout`
- `columns`

`ending_balance_reconciliation.summary.1`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-ending-balance-reconciliation-summary-1)-
`interval_end`
- `currency`
- `timezone`
- `columns`

`payout_reconciliation.itemized.1`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-itemized-1)-
`interval_start`
- `interval_end`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.itemized.2`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-itemized-2)-
`interval_start`
- `interval_end`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.itemized.3`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-itemized-3)-
`interval_start`
- `interval_end`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.itemized.4`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-itemized-4)-
`interval_start`
- `interval_end`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`payout_reconciliation.summary.1`[Columns](https://docs.stripe.com/reports/report-types/payout-reconciliation#schema-payout-reconciliation-summary-1)-
`interval_start`
- `interval_end`
- `currency`
- `timezone`
- `columns`

### Itemized ending balance reconciliation

API report type: `ending_balance_reconciliation.itemized.1`

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

### Itemized ending balance reconciliation

API report type: `ending_balance_reconciliation.itemized.2`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_direct_charge_id
(Beta) For Stripe Connect activity related to a connected account, charge id of
the direct charge that happened on connected account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

### Itemized ending balance reconciliation

API report type: `ending_balance_reconciliation.itemized.3`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

### Itemized ending balance reconciliation

API report type: `ending_balance_reconciliation.itemized.4`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_direct_charge_id
(Beta) For Stripe Connect activity related to a connected account, charge id of
the direct charge that happened on connected account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

### Itemized payout reconciliation

API report type: `payout_reconciliation.itemized.5`

Column nameDefaultDescriptionautomatic_payout_effective_at
The date we expect this [automatic
payout](https://stripe.com/docs/payouts#payout-schedule) to arrive in your bank
account, in the requested time zone, or UTC if not provided. This is also when
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
balance. Dates in the requested time zone, or UTC if not provided.

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
time zone, or UTC if not provided.

charge_created_utc
Creation time of the original charge associated with this balance transaction.
Available for charges, refunds and disputes. For charges that were separately
authorized and captured, this is the authorization time. Dates in UTC.

charge_id
Unique identifier for the original charge associated with this balance
transaction. Available for charges, refunds and disputes.

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_direct_charge_id
(Beta) For Stripe Connect activity related to a connected account, charge id of
the direct charge that happened on connected account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

created
Time at which the balance transaction was created. Dates in the requested time
zone, or UTC if not provided.

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

order_id
Unique ID for the order associated with this balance transaction.

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

### Itemized reconciliation for a single payout

API report type: `payout_reconciliation.by_id.itemized.1`

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

### Itemized reconciliation for a single payout

API report type: `payout_reconciliation.by_id.itemized.2`

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

source_id
The Stripe object to which this transaction is related.

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

### Itemized reconciliation for a single payout

API report type: `payout_reconciliation.by_id.itemized.3`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_direct_charge_id
(Beta) For Stripe Connect activity related to a connected account, charge id of
the direct charge that happened on connected account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

### Itemized reconciliation for a single payout

API report type: `payout_reconciliation.by_id.itemized.4`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_direct_charge_id
(Beta) For Stripe Connect activity related to a connected account, charge id of
the direct charge that happened on connected account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

### Payouts reconciliation summary for a single payout

API report type: `payout_reconciliation.by_id.summary.1`

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

### Ending balance reconciliation summary

API report type: `ending_balance_reconciliation.summary.1`

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

### Itemized payout reconciliation

API report type: `payout_reconciliation.itemized.1`

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

### Itemized payout reconciliation

API report type: `payout_reconciliation.itemized.2`

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

payment_metadata[key]
Metadata associated with the related PaymentIntent, if any. If no PaymentIntent
metadata exists, metadata from any related charge object will be returned. API
requests including this column must specify a metadata key in brackets. This
column can be specified multiple times to retrieve data from additional metadata
keys.

refund_metadata[key]
Metadata associated with the related refund object, if any. API requests
including this column must specify a metadata key in brackets. This column can
be specified multiple times to retrieve data from additional metadata keys.

reporting_category
[Reporting Category](https://stripe.com/docs/reporting/reporting-categories) is
a new categorization of balance transactions, meant to improve on the current
`type` field.

source_id
The Stripe object to which this transaction is related.

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

### Itemized payout reconciliation

API report type: `payout_reconciliation.itemized.3`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_direct_charge_id
(Beta) For Stripe Connect activity related to a connected account, charge id of
the direct charge that happened on connected account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

order_id
Unique ID for the order associated with this balance transaction.

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

### Itemized payout reconciliation

API report type: `payout_reconciliation.itemized.4`

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

connected_account_country
For Stripe Connect activity related to a connected account, the two-letter ISO
code representing the country of the account.

connected_account_id
For Stripe Connect activity related to a connected account, the unique ID for
the account.

connected_account_name
For Stripe Connect activity related to a connected account, the name of the
account.

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

destination_payment_id
Destination payment id in the case of Separate Charges & Transfers and
destination charges

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

### Payouts reconciliation summary

API report type: `payout_reconciliation.summary.1`

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

## See also

- [Payout reconciliation report
overview](https://docs.stripe.com/reports/payout-reconciliation)

## Links

- [Payment fees report](https://dashboard.stripe.com/reports/reconciliation)
- [automatic payout](https://stripe.com/docs/payouts#payout-schedule)
- [Card brand](https://stripe.com/docs/api#card_object-brand)
- [funding type](https://stripe.com/docs/api#account_card_object-funding)
- [ISO code for the currency](https://stripe.com/docs/currencies)
- [Reporting Category](https://stripe.com/docs/reporting/reporting-categories)
- [Trace ID](https://stripe.com/docs/payouts/trace-id)
- [dispute reasons](https://stripe.com/docs/disputes/categories)
- [Payout reconciliation report
overview](https://docs.stripe.com/reports/payout-reconciliation)