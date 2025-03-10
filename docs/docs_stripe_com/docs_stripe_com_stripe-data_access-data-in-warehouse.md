# Access data within a data warehouse

## Use Data Pipeline to sync Stripe data to a data warehouse.

[Data Pipeline](https://dashboard.stripe.com/settings/stripe-data-pipeline) is a
no-code product that sends all your Stripe data to a variety of data storage
destinations. This lets you centralize your Stripe data with other business data
to help close your books and get more detailed business insights. If you have
questions regarding support for your data destination, [contact
us](mailto:data-pipeline@stripe.com).

With Data Pipeline, you can:

- Automatically export your complete Stripe data in a fast and reliable manner.
- Stop relying on third-party extract, transform, and load (ETL) pipelines or
home-built API integrations.
- Combine data from all your Stripe accounts into one data warehouse.
- Integrate Stripe data with your other business data for more complete business
insights.

#### Caution

Because of data localization requirements, Stripe doesn’t offer Data Pipeline
services to customers, businesses, or users in India.

## Destination support

Stripe Data Pipeline supports two variations of destinations:

- [Data
warehouses](https://docs.stripe.com/stripe-data/access-data-in-warehouse/data-warehouses)
(Snowflake, Amazon Redshift)

- For data warehouse destinations, Stripe sends a data share to your data
warehouse.
- After you accept the data share, you can access your core Stripe data in
Snowflake or Amazon Redshift within 12 hours.
- After the initial load, your Stripe data [refreshes
regularly](https://docs.stripe.com/stripe-data/available-data), delivering an
incremental or full load of data every 3 hours.
- [Cloud
storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage)
(Google Cloud Storage, Azure Blob Storage, Amazon S3)

- For our cloud storage destinations, Stripe sends
[Parquet](https://parquet.apache.org/) files directly to a cloud storage
location you own.
- After the initial load, your Stripe data [refreshes
regularly](https://docs.stripe.com/stripe-data/available-data), delivering a new
full load of your data every 6 hours.

## Database schemas

Your warehouse data is split into two database schemas based on the API mode you
used to create the data.

Schema nameDescription`STRIPE`Data populated from live mode`STRIPE_TESTMODE`Data
populated from [test mode](https://docs.stripe.com/test-mode)
If you share data from multiple Stripe accounts with the same data warehouse,
you can identify these separately. Every table has a `merchant_id` column, which
allows you to filter the data by account.

## Combine proprietary and Stripe data

In some cases, you might want to combine information from your proprietary data
with Stripe data. The following schema shows an `orders` table that lists data
about an order for a company. This table doesn’t contain data regarding
transaction fees or [payouts](https://docs.stripe.com/payouts) because that data
exists solely within Stripe.

dateorder_nostripe_txn_nocustomer_namepriceitems3/9/20251bt_xcVXgHcBfi83m94John
Smith51 book
In Stripe, the `balance_transactions` table contains the following information,
but lacks proprietary data regarding customer names and items purchased:

idamountavailable_onfeenetautomatic_transfer_idbt_xcVXgHcBfi83m945003/9/202550450po_rC4ocAkjGy8zl3j
To access your proprietary data alongside your Stripe data, combine the `orders`
table with Stripe’s `balance_transactions` table:

```
select
 orders.date,
 orders.order_no,
 orders.stripe_txn_no,
 bts.amount,
 bts.fee,
 bts.automatic_transfer_id
from mycompany.orders join stripe.balance_transactions bts
on orders.stripe_txn_no = bts.id;
```

After it completes, the following information is available:

dateorder_noStripe_txn_noamountfeeautomatic_transfer_id3/9/20251bt_xcVXgHcBfi83m9450050po_rC4ocAkjGy8zl3j
## Datasets

You can see a list of available datasets under **Datasets** in the [schema
documentation](https://dashboard.stripe.com/stripe-schema) page in the
Dashboard. Available datasets might vary by region, subject to local product
availability and regulations. Data Pipeline separately shares each dataset,
which contains one or more warehouse tables, as data becomes available. Data
Pipeline updates some tables on different schedules based on the availability of
new data. See [data
freshness](https://docs.stripe.com/stripe-data/available-data) for more
information on available datasets and refresh schedules.

## Turn off Data Pipeline

You can turn off Data Pipeline in the Dashboard by clicking **Turn off**. After
you disconnect, you lose access to your data share immediately. If you want to
upload files with a different structure or in a custom format, [contact
us](mailto:data-pipeline@stripe.com).

## See also

- [Export data to a data
warehouse](https://docs.stripe.com/stripe-data/access-data-in-warehouse/data-warehouses)
- [Export data to cloud
storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage)
- [Data freshness](https://docs.stripe.com/stripe-data/available-data)

## Links

- [Data Pipeline](https://dashboard.stripe.com/settings/stripe-data-pipeline)
- [Data
warehouses](https://docs.stripe.com/stripe-data/access-data-in-warehouse/data-warehouses)
- [refreshes regularly](https://docs.stripe.com/stripe-data/available-data)
- [Cloud
storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage)
- [Parquet](https://parquet.apache.org/)
- [test mode](https://docs.stripe.com/test-mode)
- [payouts](https://docs.stripe.com/payouts)
- [schema documentation](https://dashboard.stripe.com/stripe-schema)