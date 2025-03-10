# Data import examples

## Learn how to apply data import to common use cases.

## Adding a service period to a Stripe payment

In this example, you use Stripe as a payment processor, but have your own
recurring payment solution. You have payments in Stripe, but your separate
system keeps the service period for these payments.

Suppose you have a payment in Stripe with the ID `py_1234` of 120 USD on January
1, 2020 that represents a yearly
[subscription](https://docs.stripe.com/billing/subscriptions/creating) from
February 1, 2020 to January 31, 2021. To add this data to Stripe, you can import
a CSV with the following fields:

sourcetransaction_idsplit_transaction_idbooked_daterecognition_start_daterecognition_end_dateamountcurrencydescriptionStripepy_12342020-02-012021-01-31
Stripe already has data on the booked date, amount, and currency, so you can
leave these fields blank.

## Adding or overriding a service period on an invoice line item

In this example, you use [Stripe Invoicing](https://docs.stripe.com/invoicing),
but you have your own recurring payment solution. You may have missing or
incorrect service periods on your
[invoice](https://docs.stripe.com/api/invoices) line items.

Suppose you manually generated an invoice for a large enterprise customer and
finalized this invoice on April 1, 2020. The invoice has the ID `in_1234` and
has several line items, some of which are physical goods, and some of which are
subscriptions for other products. In your [Revenue Recognition report by line
item](https://docs.stripe.com/revenue-recognition/reports#csv-reports), you
notice:

- An unexpected increase in April revenue in your report. The line item for one
subscription (`il_5678`) has no service period, and so all of the revenue for
that line item books into April.
- Another line item for another subscription (`il_7890`) has an incorrect
service period of April 1, 2020 to April 15, 2020, resulting in revenue
recognized in April.

You want to recognize revenue for `il_5678` from May 1, 2020 to June 1, 2020,
and recognize the revenue for `il_7890` from June 1, 2020 to September 1, 2020.

sourcetransaction_idsplit_transaction_idbooked_daterecognition_start_daterecognition_end_dateamountcurrencydescriptionStripein_1234il_56782020-05-012021-06-01Stripein_1234il_78902020-06-012021-09-01
Stripe already has data on the booked date from the invoice finalization date,
amount, and currency, so you can leave these fields blank.

## Splitting Stripe payments with additional data

In this example, you use Stripe as your payment processor. You have payments in
Stripe, but these payments may represent multiple different goods and services
that you want to have custom revenue recognition schedules for.

Suppose you have a payment in Stripe of 100 USD with the ID `py_1234` that
represents two separate goods and services:

- A 74.99 USD subscription recognized from February 1, 2020 to May 31, 2020.
- A 25.01 USD shipment of materials recognized immediately on a shipment date of
January 1, 2020.

To split this Stripe payment, you could provide the following data:

sourcetransaction_idsplit_transaction_idbooked_daterecognition_start_daterecognition_end_dateamountcurrencydescriptionStripepy_1234subscription2020-02-012021-05-3174.99USDThe
subscription part of the
paymentStripepy_1234shipment2020-01-012021-01-0125.01USDThe material shipment
part of the payment
You must specify a unique **Split transaction ID** for each part of the
transactions. This helps us differentiate different parts of a payment with the
same ID. The only requirement is that each **Split transaction ID** is unique.

Stripe already has data on the booked date and currency, so you can leave these
fields blank, or fill them in with the correct values. We’ll check that the
amounts of each component of the payment add up to the original payment amount,
and that the currencies (if specified) stay the same. The descriptions are
optional.

## Importing external transactions

In this example, you’re migrating to Stripe from a different payment processor
or have a multiple payment processor solution.

Suppose you’re migrating your subscriptions to Stripe, and all of them have
already been paid for. One of these subscriptions is a yearly subscription from
January 1, 2020 to December 31, 2020 paid for in advance on December 15, 2019
for a price of 100 USD. To import this data into Stripe for revenue recognition
purposes, you can provide the following data:

sourcetransaction_idsplit_transaction_idbooked_daterecognition_start_daterecognition_end_dateamountcurrencydescriptionMy
previous systemTransaction 12342019-12-152020-01-012020-12-31100USDA yearly
subscription
Because Stripe doesn’t have any data on this transaction, you must provide every
field except **Split transaction ID** and the always optional **Description**.
You can also provide a **Split transaction ID** if that best represents your
data.

The currency must be a [currency supported on your
account](https://docs.stripe.com/currencies) in Stripe, but otherwise the data
in any of the other fields has no restrictions.

## Correcting imported data

If you make a mistake when importing data, you can [delete the transaction in
the
Dashboard](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data#transactions-deletion),
and re-import the correct data to correct the errors. Alternatively, you can
upload a new CSV, and any rows with the corresponding **Source**, **Transaction
ID**, and **Split transaction ID** to replace the old imported data.

Suppose you have an import like the one below, but want to remove the
recognition start and end dates and change the booked date to March 1, 2022.

sourcetransaction_idsplit_transaction_idbooked_daterecognition_start_daterecognition_end_dateamountcurrencydescriptionStripepy_12342020-02-012021-01-31
You can import another CSV with the following format, and it completely replaces
the previous row:

sourcetransaction_idsplit_transaction_idbooked_daterecognition_start_daterecognition_end_dateamountcurrencydescriptionStripepy_12342022-03-01
The blank fields for **Recognition start date** and **Recognition end date**
signal that we use the recognition start and end dates for the existing payment,
`py_1234`. The previous incorrect recognition start and end date for the import
are no longer used.

## Excluding transactions from revenue

You might want to exclude certain transactions from your revenue recognition
process because they were erroneously generated due to incorrect settings or are
test transactions.

For example, you have five transactions to exclude from your revenue:

- in_1234 – test invoice
- ii_1234 – invoice item incorrectly generated from a subscription update
- in_5678 – invoice that includes multiple line items, of which il_1234 was
mistakenly added
- py_1234 – standalone payment created by a problematic integration
- ch_1234 – test standalone charge

To exclude these transactions, [download the CSV template for Exclusion
Import](https://dashboard.stripe.com/revenue-recognition/data-import) and fill
in the IDs as follows:

transaction_idin_1234ii_1234il_1234py_1234ch_1234

## Links

- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Stripe Invoicing](https://docs.stripe.com/invoicing)
- [invoice](https://docs.stripe.com/api/invoices)
- [Revenue Recognition report by line
item](https://docs.stripe.com/revenue-recognition/reports#csv-reports)
- [currency supported on your account](https://docs.stripe.com/currencies)
- [delete the transaction in the
Dashboard](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data#transactions-deletion)
- [download the CSV template for Exclusion
Import](https://dashboard.stripe.com/revenue-recognition/data-import)