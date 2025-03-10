# Revenue Recognition data importPublic preview

## Import data from other sources to manage all of your revenue recognition in Stripe.

Perform revenue recognition on non-Stripe transactions and adjust the
recognition schedules of existing Stripe transactions, or exclude the existing
Stripe transactions from the revenue.

Data import is categorized by general import or exclusion import.

**General import** allows you to upload revenue data with CSV files. You can
import transactions processed completely outside of Stripe and customize the
recognition terms of existing Stripe transactions to fit your business model.
For example, you can import data to:

- **Add** a service period to a Stripe payment.
- **Override** the service period of a line item in a Stripe
[invoice](https://docs.stripe.com/api/invoices).
- **Split** a payment into multiple different revenue schedules.
- **Import** an external payment processor’s data with a service period, amount,
and currency.

**Exclusion import** allows you to exclude transactions from your revenue by
uploading the IDs of the transactions to exclude. You can exclude the following
types of transactions: invoice, invoice item, invoice line item, standalone
payment.

#### Caution

When you import data related to India, make sure you’re in compliance with India
data locality requirements.

## General import

You can import data into Revenue Recognition reports and view all the data
you’ve imported from the [Data import
page](https://dashboard.stripe.com/revenue-recognition/data-import). Click
**Download CSV template** and select **General import CSV** to see the required
format for the data import feature. You can then click **Import CSV** and select
**General import** to upload your completed template. See the following
descriptions of the CSV format:

**Source**

The provider of the original transaction. Examples:

- `Stripe` (case-insensitive) for transactions processed by Stripe
- Any value such as `Checks` or `App Store`, an arbitrary identifier that helps
you group the source of a set of transactions

**Transaction ID**

The ID of a transaction. Examples:

- An ID such as `ch_123456` or `py_1234` for Stripe payments
- An ID such as `in_12345` for Stripe invoices
- Any value such as `my_internal_id` or `Check Number 1234`, an arbitrary
identifier that helps you track a single transaction

**Split transaction ID**

If you’re not overriding an invoice line item service period or splitting a
transaction, you can leave this blank.

When overriding an invoice line item service period, this is the invoice line
item ID. Examples:

- An ID such as `il_1234`, that you can find from your Revenue Recognition
reports at the invoice line item level

If you’re splitting a transaction, this is an arbitrary identifier that
differentiates between different parts of the same transaction. Examples:

- `bike`
- `my_internal_id`

**Booked date**

This is the date that you recorded the transaction in `YYYY-MM-DD` format in the
UTC timezone.

**Recognition start date**

This is the date that you want to start recognizing revenue in `YYYY-MM-DD`
format in the UTC timezone.

**Recognition end date**

This is the date that you want to stop recognizing revenue in `YYYY-MM-DD`
format in the UTC timezone.

**Amount**

This is the numeric amount of the transaction without any currency symbols. For
example, for 10.95 USD, you would specify `10.95`.

**Currency**

This is the three-letter [ISO 4217 currency
code](https://en.wikipedia.org/wiki/ISO_4217) for the currency of the recognized
revenue of the transaction. For example, for 10.95 USD, you would specify `usd`.
Your Stripe account must be set up to support the specified currency.

**Description**

This can be any arbitrary description. You can use these in combination with
[Revenue Recognition rules](https://docs.stripe.com/revenue-recognition/rules)
to further customize your recognized revenue.

### Additional verifications

- All rows must have a transaction ID.
- All of the split parts of a transaction must have an amount that adds up to
the original transaction.
- External transactions must provide a booked date, revenue recognition start
and end date, amount, and currency.
- We ignore overrides on payments attached to Stripe invoices, so if you want to
override such a payment, use the invoice itself as the transaction.

## Exclusion import

You can exclude transactions from revenue and view the excluded transactions
that you imported from the [Data import
page](https://dashboard.stripe.com/revenue-recognition/data-import). Click
**Download CSV template** and select **Exclusion import CSV** to see the
required format for the exclusion data import feature. You can then click
**Import CSV** and select **Exclusion import** to upload your completed
template.

**Transaction ID**

Transaction ID examples include:

- `ch_123456` or `py_1234` – An ID for a standalone Stripe payment. If a payment
or charge is linked with an invoice, don’t use the charge or payment ID. Use the
invoice ID for exclusion instead.
- `in_12345` – An ID for Stripe invoices.
- `ii_12345` – An ID for Stripe invoice items.
- `il_12345` – An ID for Stripe invoice line items.

## Opening accounting periods

Applying a transaction to a closed accounting period generates corrections. If
you want to apply past transactions directly to a past accounting period, make
sure that the past accounting period is open. If you forgot to do this, you
don’t need to re-import data. Instead, you can [open the relevant accounting
period](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)
and wait for the reports to be recalculated.

## See also

- [Manage imported
data](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data)
- [Examples](https://docs.stripe.com/revenue-recognition/data-import/examples)

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [Data import
page](https://dashboard.stripe.com/revenue-recognition/data-import)
- [ISO 4217 currency code](https://en.wikipedia.org/wiki/ISO_4217)
- [Revenue Recognition rules](https://docs.stripe.com/revenue-recognition/rules)
- [open the relevant accounting
period](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)
- [Manage imported
data](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data)
- [Examples](https://docs.stripe.com/revenue-recognition/data-import/examples)