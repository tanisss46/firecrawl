# Diagnose connection issues with cloud storage

## Check common cloud storage configuration points.

If you have issues with your Stripe Data Pipeline connection to your cloud
storage, use this guide to check common configuration points. Select your cloud
storage provider below for specific troubleshooting steps.

## Google Cloud Storage

First, confirm that the bucket and project names match those in the Data
Pipeline Dashboard:

- Navigate to the [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline).
- Save the bucket and project listed for your Google Cloud Storage connection.
- Open the [Cloud Storage
bucket](https://console.cloud.google.com/storage/browser) page under the correct
Google Cloud Project.
- Confirm that the bucket listed in your Dashboard appears in your console.

To confirm that the roles and permissions are correct:

- Navigate to your [Cloud Storage
bucket](https://console.cloud.google.com/storage/browser) details, then click
the Permissions tab.
- Confirm that your [Service
Account](https://console.cloud.google.com/iam-admin/serviceaccounts) includes
the following roles: `Storage Object User`, `Storage Object Creator`, and
`Storage Insights Collector Service`.

Make sure that you continue to confirm the [Google Cloud Status
Dashboard](https://status.cloud.google.com/) for any ongoing issues with Google
Cloud Storage. [Contact us](mailto:data-pipeline@stripe.com) if these steps
don’t resolve your connection issues.

## Azure

First, confirm that the container is correct:

- Navigate to the [Storage
Accounts](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts)
page.
- Click **Storage browser** > **Data storage** > **Containers**.
- Confirm that your container from the [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline) appears
on the Azure Containers page.

To confirm that the access key still exists:

- Navigate to the [Storage
Accounts](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts)
page.
- Click **Security + networking** > **Access keys**.
- Confirm that the shared access key still exists.

To confirm that the Resource group and Subscription ID are correct:

- Navigate to the [Storage
Accounts](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts)
page.
- Click **Overview**.
- Confirm that the Resource group and Subscription ID match those from the
initial onboarding. Make sure that you continue to confirm the [Azure Status
Dashboard](https://azure.status.microsoft/en-us/status) for any ongoing issues
with Azure. [Contact us](mailto:data-pipeline@stripe.com) if these steps don’t
resolve your connection issues.

## Amazon S3

To confirm you attached the policy you created to the new trust role:

- Navigate to the [IAM console](https://console.aws.amazon.com/iam/) and click
**Policies**.
- Select the policy created in [step
4](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#create-permission-polcy)
(for example, `stripe-data-pipeline-policy`).
- Click **Entities attached** and confirm that `stripe-data-pipeline-s3-role`
appears under **Attached as a permissions policy**.
- If not, click **Attach**, then select `stripe-data-pipeline-s3-role` and click
**Attach policy**.

## Links

- [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline)
- [Cloud Storage bucket](https://console.cloud.google.com/storage/browser)
- [Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Google Cloud Status Dashboard](https://status.cloud.google.com/)
- [Storage
Accounts](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts)
- [Azure Status Dashboard](https://azure.status.microsoft/en-us/status)
- [IAM console](https://console.aws.amazon.com/iam/)
- [step
4](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#create-permission-polcy)