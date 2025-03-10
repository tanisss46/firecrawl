# Payout reconciliation report

## Reconcile each payout with the batch of transactions it settles.

The [Payout reconciliation](https://dashboard.stripe.com/reports/reconciliation)
report helps you match the payouts you receive in your bank account with the
batches of payments and other transactions that they relate to.

The payout reconciliation report is only available for users with **automatic
payouts** enabled, and is optimized for users who prefer to reconcile the
transactions included in each payout as a settlement batch. If you use manual
payouts or prefer to track and reconcile your Stripe balance like a bank
account, see the [Balance](https://docs.stripe.com/reports/balance) report
instead. To help you decide which report is right for you, see the [guide for
selecting
reports](https://docs.stripe.com/reports/select-a-report#reconciliation).

To get started, use the [controls](https://docs.stripe.com/reports/options) at
the top of the screen to select a date range.

The **Balance summary** section shows your starting and ending Stripe balance
for the selected date range, along with a high level summary of your activity
during the period.

The **Payout reconciliation** section provides a breakdown of the automatic
payouts that were received in your bank account during the selected date range.
The transactions included in those settlement batches are grouped by [reporting
category](https://docs.stripe.com/reports/reporting-categories).

The **Ending balance reconciliation** section provides a similar breakdown of
the transactions that hadn’t been settled as of the report’s end date.

## Downloading data

You can download the data displayed in each section of the report as a CSV file
by clicking the **Download** button in the upper right corner of that section.
The **Payout reconciliation** and **Ending balance reconciliation** sections
allow you to download multiple types of reports:

- **Summary**: This downloads data in CSV format exactly as you see it in the
dashboard.
- **Itemized**: This downloads the full list of individual transactions that are
summarized in the dashboard. You can include custom metadata associated with
those transactions to speed up the reconciliation process.

In addition, you can quickly download itemized data for a single category of
transactions by hovering over that category and clicking the **Download** button
that appears.

## Available columns

You can customize the columns that appear in the reports when downloading them
in the dashboard or via the [Reporting
API](https://docs.stripe.com/reports/api). The available columns in each type of
report are described below.

- [Balance
summary](https://docs.stripe.com/reports/payout-reconciliation#schema-balance-summary-1)
- [Payouts reconciliation
summary](https://docs.stripe.com/reports/payout-reconciliation#schema-payout-reconciliation-summary-1)
- [Itemized payout
reconciliation](https://docs.stripe.com/reports/payout-reconciliation#schema-payout-reconciliation-itemized-5)
- [Ending balance reconciliation
summary](https://docs.stripe.com/reports/payout-reconciliation#schema-ending-balance-reconciliation-summary-1)
- [Itemized ending balance
reconciliation](https://docs.stripe.com/reports/payout-reconciliation#schema-ending-balance-reconciliation-itemized-4)

### Balance summary

API report type: `balance.summary.1`

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

## Links

- [payout reconciliation through the
API](https://docs.stripe.com/payouts/reconciliation)
- [Payout reconciliation](https://dashboard.stripe.com/reports/reconciliation)
- [Balance](https://docs.stripe.com/reports/balance)
- [guide for selecting
reports](https://docs.stripe.com/reports/select-a-report#reconciliation)
- [controls](https://docs.stripe.com/reports/options)
- [reporting category](https://docs.stripe.com/reports/reporting-categories)
- [Reporting API](https://docs.stripe.com/reports/api)
- [ISO code for the currency](https://stripe.com/docs/currencies)
- [Reporting Category](https://stripe.com/docs/reporting/reporting-categories)
- [automatic payout](https://stripe.com/docs/payouts#payout-schedule)
- [Card brand](https://stripe.com/docs/api#card_object-brand)
- [funding type](https://stripe.com/docs/api#account_card_object-funding)
- [dispute reasons](https://stripe.com/docs/disputes/categories)
- [Trace ID](https://stripe.com/docs/payouts/trace-id)