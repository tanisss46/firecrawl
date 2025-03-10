# Stripe connector for Amazon S3Public preview

## Automate recurring file imports from your Amazon S3 bucket to Stripe.

This guide explains how to import files from Amazon S3 into the Stripe Data
Management Platform. By following these steps, you set up an automated job for
importing data to keep your Stripe products up-to-date.

## Prerequisites

Before starting the integration, make sure you have the following:

- An active AWS account and S3 bucket with access to the relevant files.
- Admin account access to the Stripe Dashboard.
[Log in to your AWS
account](https://docs.stripe.com/stripe-data/import-external-data/connectors/s3#section-1)
You need access to your AWS Access Console during the configuration process.

- Sign in to the [AWS Management Console](https://console.aws.amazon.com/)
[Prepare your Files in Amazon
S3](https://docs.stripe.com/stripe-data/import-external-data/connectors/s3#section-2)
To validate your connection configuration, use well-formatted data in your S3
bucket. The configuration process shows you available files, and runs an initial
sync when the connection is configured.

- Visit your [Amazon S3 console](https://s3.console.aws.amazon.com/)
- Make sure that your files are stored in a designated S3 bucket and organized
according to your import preferences.- If you don’t currently have an S3 bucket,
you can follow the [AWS guidelines for creating your first
bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
- Stripe has the following file requirements for successful retrieval:- File
names must adhere to [S3 Object naming
conventions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html).
- The maximum file size is 1 GB.
- Remember the bucket name and region because you need them for future steps.
- Keep your AWS Console open to configure an IAM role in future steps.

### Supported file formats

- CSV
- TSV
- JSON
- JSONLINE
- For more formats, please [contact support](https://support.stripe.com/)
[Configure the Stripe Amazon S3 Connector to import files from your S3
Bucket](https://docs.stripe.com/stripe-data/import-external-data/connectors/s3#section-3)-
Sign in to the [Stripe Data Management Connector
Dashboard](https://dashboard.stripe.com/data-management/connectors)
- Click **+ Set up connector** > **Amazon S3**.
- Provide a unique connector name for this Connection. Consider using details
about the data source, objects in the file, and product destination to create a
strong unique name.
- In your Amazon console, navigate to the [IAM
console](https://console.aws.amazon.com/iam/).
- The next step of the Stripe Amazon S3 Connector setup provides details to
Create an IAM Role using a Custom trust policy.- In the navigation pane of the
console, click **Policies** > **Create policy**.
- To create your permission policy, select **JSON** and replace the existing
policy text by copying and pasting the provided code block. In the Resource
section of the **Policy editor** code block, replace `USER_TARGET_BUCKET` with
your intended bucket name. Click **Next**. Under **Policy details**, add a
policy name, along with any tags (optional), then click **Create policy**.
- Return to the navigation pane of the console, then click **Roles** > **Create
role**.
- Choose the **Custom trust policy** role type, copy and paste the provided code
block, then click **Next**.
- To select your permission policy, locate the newly created permission policy
in the list. Enable the checkbox to select the policy, scroll down, then click
**Next**.
- To create a role name, copy and paste the provided role name, then click
**Create role**.
- The following step of the Stripe Amazon S3 Connector setup establishes the
connection between your Amazon S3 bucket and Stripe.- From the AWS Console,
[find and provide your AWS Account
ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId).
- Provide the Bucket Name and Region saved from your AWS Console during Step
2.3.
- If you use folders to organize your files in your Amazon S3 bucket, specify a
folder within the above bucket.- If you specify a folder within the above
bucket, we only fetch data from this folder, not the entire bucket.
- After successfully setting up a new connector, Stripe fetches all data from
the Amazon S3 bucket that was modified in the last 90 days.- We fetch data after
every five minutes.
- Only objects with a LastModified date later than the last sync are imported
for recurring imports.
- Step 4 previews the files available in the connected Amazon S3 bucket and
allows you to associate them with a data template.- The file preview validates
that your credentials connect Stripe with the expected Amazon S3 bucket and
folder.
- The data template associates this connection with an expected file format for
initial and recurring imports.
- Click **Done** to create an Active Data Connection and initiate the initial
Data Import.
[Maintaining your Amazon S3
connection](https://docs.stripe.com/stripe-data/import-external-data/connectors/s3#section-4)
After your connection is established, we fetch your data every 5 minutes. To
monitor the health of your connection, you can perform the following actions:

- Visit the [Stripe Data Management Connector
dashboard](https://dashboard.stripe.com/data-management/connectors) for the
status and last sync details of your established connections.
- Manage a single Connection by clicking on a connector.- You can edit the
connector name or data template, re-authenticate a broken connection, and delete
a connection.
- We recommend setting up an automated job to regularly deliver new files to
your S3 bucket.
- The Amazon List Object API doesn’t allow for filtering objects by
LastModified. As a result, you must list all the contents of your bucket for
each import. Make sure that you only allow the associated IAM role access to
data that you intend to import to Stripe. We recommend limiting the number of
files in your bucket below 50000. To achieve this, make sure that you set the
expiry time for your objects accordingly.

## Interested in the Stripe Connector for S3?

Please provide your email address below and our team will be in touch.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [AWS Management Console](https://console.aws.amazon.com/)
- [Amazon S3 console](https://s3.console.aws.amazon.com/)
- [AWS guidelines for creating your first
bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
- [S3 Object naming
conventions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html)
- [contact support](https://support.stripe.com/)
- [Stripe Data Management Connector
Dashboard](https://dashboard.stripe.com/data-management/connectors)
- [IAM console](https://console.aws.amazon.com/iam/)
- [find and provide your AWS Account
ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId)
- [privacy policy](https://stripe.com/privacy)