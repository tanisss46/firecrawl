# Export data to Azure Blob Storage

## Automate recurring data exports from Stripe to your Azure Blob Storage container.

# Azure Blob Storage destination

The Azure Blob Storage destination delivers copies of all your Stripe data as
Parquet files into your Azure Blob Storage account. It contains a directory of
files for each table, delivered and updated every 6 hours.

[Prerequisites](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#prerequisites)
Before starting the integration, make sure you have access to:

- Create a new Azure App Registration.
- Create a new Azure Storage account.
- Create a new Azure Storage container.
- Access the Stripe Dashboard as an admin.
[Create a new Azure App
Registration](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#create-app-registration)-
On the [App
registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
page, click **+ New Registration**.
- Enter a name for this application and click **Register**.
#### Note

Don’t make any changes to either the **Supported account types** field or the
**Redirect URI** field.
- Make a note of the Application (client) ID and Directory (tenant) ID values
from the Overview page of created app registration.
- Click **Add a certificate or secret link** in the same section or click
**Manage** > **Certificates & secrets**.
- Click **+ New Client Secret** and enter a description and set `Expires` to 730
days (24 months).
- Click the ** to clipboard** icon to copy the Value field (client secret
value) and make a note of it.
[Create a new Azure Storage
account](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#storage-account)-
On the [Storage
accounts](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts)
page, click **+ Create**.
- Choose a Subscription and Resource group.
- Enter a Storage account name that’s unique across all Storage accounts in
Azure (for example, “stripeuniquename” or “stripeasd5dwju8awkwe”).
- Choose a Region. 
#### Caution

We don’t support data regions in India. Let us know if you have questions about
support for your desired region.
- Choose a **Performance** level and **Redundancy** option.
- Click **Review + create**.
- Review your settings and click **Create**.
- After creating the account, click **Go to resource**. Resource creation
typically completes within 15 seconds.
- Make a note of Resource group value and Subscription ID values as shown in the
Overview section.
[Create a new Azure Storage
container](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#create-storage-container)-
Click **Data storage** > **Containers** in the left pane.
- Click **+ Container**.
- Choose a name for your container (for example, “stripe-data”).
- Set anonymous access level to **Private (no anonymous access)**.
- Click **Create**.
- Click the created container and go to **Settings** > **Properties** in the
left pane.
- Make a note of the container URL field.
[Grant permissions on Storage
account](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#grant-permissions)-
Navigate to your created Storage account page.
- Click **Access Control (IAM)** in the left menu.
- Click **Add** then **Add role assignment**
- Search for the **Storage Blob Data Contributor** role and select it, then
click next.
- Click **+ Select members** and search with the application name created in
step 2.2
- Select the corresponding application shown in the dropdown and click select.
- Click **Review + assign**.
- Verify if the role and application name display correctly, and Click **Review
+ assign**. The role assignment completes after it processes.
- Follow the same steps from 1-7 and search for and select the **Reader and Data
Access** role in step 4 instead.
- By following these instructions, you grant both the `Storage Blob Data
Contributor` and `Reader and Data Access` roles to your registered application
for the storage account.
[OptionalGenerate encryption
keys](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#generate-encryption-key)[Establishing
Your Azure Blob Storage
Connection](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/azure-blob-storage#establishing-connection)-
Visit the [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline).
- Click **Get started**.
- Select the Microsoft Azure warehouse.
- Enter the Client ID, tenant ID and Client secret generated in step 2.
- Enter the Subscription ID and Resource group values generated in step 3.
- Enter the Container URL generated in step 4.
- Select your data encryption option. If you chose to use a customer managed
key, upload your public key.
- Click **Next**. Clicking **Next** sends test data to the container on the
storage account you provided, but not production data.
- When you confirm test data delivery, go to your container on the Azure Storage
account.
- Open the container, navigate to the penny_test directory, and open the acct_
prefixed sub-directory to locate the delivered account_validation.csv test file.
- Click the **account_validation.csv** file
- Click **DOWNLOAD**.
- Click **Upload file** in the Stripe Dashboard and upload the downloaded
account_validation.csv file.
- When the file shows as verified, click **Subscribe**. This subscribes you to
the product and schedules the initial full load of data for delivery to your
container on the Azure Storage account, a process that can take 6-12 hours.

## Links

- [App
registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
- [Storage
accounts](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts)
- [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline)