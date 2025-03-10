# Access data in cloud storage

## Use Data Pipeline to sync your Stripe account with your cloud storage destination.

When you set up Data Pipeline, Stripe sends
[Parquet](https://parquet.apache.org/) files to your owned cloud storage
location, such as Google Cloud Storage or Azure Blob Storage. After the initial
load, your Stripe data [refreshes
regularly](https://docs.stripe.com/stripe-data/available-data), delivering a new
full load of your data on a regular basis.

We support the following destinations:

- [Google Cloud
Storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage)
- [Azure Blob
Storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage)
Private preview
- [Amazon S3
Storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage)

See how we organize files in the destination:

```
rundate (for example, YYYYMMDDHH)/
├─ mode (for example, livemode)/
│ ├─ tablename (for example, accounts)/

```

For each run date and mode, we create a SUCCESS file that confirms the
successful transfer and validation of all files for a specific set of tables.
Learn more about [the file organization for the most commonly used tables in our
schema](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/file-organization).

## Links

- [Parquet](https://parquet.apache.org/)
- [refreshes regularly](https://docs.stripe.com/stripe-data/available-data)
- [Google Cloud
Storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage)
- [Azure Blob
Storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage)
- [Amazon S3
Storage](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage)
- [the file organization for the most commonly used tables in our
schema](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/file-organization)