# Export data to Google Cloud Storage

## Automate recurring data exports from Stripe to your Google Cloud Storage.

# Google Cloud Storage destination

Data pipeline can deliver copies of all your Stripe data as Parquet files into
your Google Cloud Storage (GCS) bucket. It includes a directory of files for
each table, delivered, and updated every 6 hours.

[Prerequisites](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage#prerequisites)
Before starting the integration, make sure you have access and permission to:

- Create a Google Cloud Storage bucket.
- Create a service account enabling Stripe to create objects in the provisioned
bucket.
- Access the Stripe Dashboard as an admin.
[Select Your Google Cloud
Project](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage#select-project)-
Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Select the project that you want to send your Stripe data to.
[Create a new Service Account and generate a JSON
key](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage#create-service-account)-
On the [Service
Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page, make
sure you’re in the correct Google Cloud Project.
- Click **+ CREATE SERVICE ACCOUNT**.
- Enter a name for the service account, for example,
“<name>-stripe-data-pipeline.”
- Add a description—for example, “This role gives Stripe access to upload data
files to our bucket.”
- Click **CREATE AND CONTINUE**.
- In the **Select a Role** dropdown, add three roles: `Storage Object User`,
`Storage Object Creator`, and `Storage Insights Collector Service`.
- Click **DONE**.
- For your new [Service
Account](https://console.cloud.google.com/iam-admin/serviceaccounts), click
**Manage keys** in the **Actions** menu.
- Click **ADD KEY ▾** and select **Create new key**.
- Choose **Key type JSON** and click **CREATE**. The JSON file downloads to your
device.
[Create a New
Bucket](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage#create-bucket)-
Make sure you’re in the correct Google Cloud project by navigating to **Cloud
Storage** > **Buckets** in the [Google Cloud
console](https://console.cloud.google.com/storage/browser).
- Click **+ CREATE**.
- In the **Name** field, we recommend a name including “stripe,” such as
“<name>-stripe-data.”
- For the **Location type**, we recommend **Multi-Regional US**.
- For the **Storage class**, we recommend **Set a default class - Standard**.
- For the **Access Control**, choose **Prevent public access** with **Uniform**
access control.
- For **Data protection**, we recommend a logical **Retention Policy**, for
example **7 days**.
- Click **CREATE** button to create the bucket.
- Select the **PERMISSIONS** tab for your newly created bucket.
- Under **Permissions** in the **VIEW BY PRINCIPAL** tab, check the box next to
the Service Account you created in the previous step.
[OptionalGenerate encryption
keys](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage#generate-encryption-key)[Establishing
your Google Cloud Storage
connection](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/google-cloud-storage#establishing-connection)-
Visit the [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline).
- Click **Get started**.
- Select the Google Cloud Storage logo and click **Continue ->**. This step
generates a bucket name.
- Enter the bucket name generated in the previous step.
- Upload your Service Account `.json` file generated earlier.
- Select your data encryption option. If you chose to use a customer managed
key, upload your public key.
- Click the **Next** button. Clicking this button sends test data to the bucket
you provided, but not production data.
- When you confirm test data delivery, go to your [Cloud Storage
bucket](https://console.cloud.google.com/storage/browser).
- Open the bucket, navigate to the **penny_test** directory, and open the
**acct_** prefixed sub-directory to locate the delivered
`account_validation.csv` test file.
- Click the **account_validation.csv** file.
- Click **DOWNLOAD**.
- Click the **Upload the test value file** and upload the downloaded
`account_validation.csv`.
- Click **Confirm value**.
- When you confirm the test value, click **Subscribe**. This subscribes you to
the product and schedules the initial full load of data for delivery to your
Google Cloud Storage bucket, a process that can take 6-12 hours.

*Google Cloud Storage is a trademark of Google LLC.

## Links

- [Google Cloud Console](https://console.cloud.google.com/)
- [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Google Cloud console](https://console.cloud.google.com/storage/browser)
- [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline)