# Export data to Amazon S3

## Automate recurring data exports from Stripe to your AWS S3 Storage bucket.

Data pipeline can deliver copies of all your Stripe data as Parquet files into
your Amazon S3 storage bucket. It includes a directory of files for each table
that’s delivered and updated every 6 hours.

[Prerequisites](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#prerequisites)
Before starting the integration, make sure you have an active AWS account and
permission to:

- Create an Amazon S3 bucket.
- Create an IAM role enabling Stripe to create objects in the provisioned
bucket.
- Access the Stripe Dashboard with an admin or developer role.
[Create a
bucket](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#create-bucket)-
Navigate to your [Amazon S3 console](https://s3.console.aws.amazon.com/) in your
chosen account region.
- If needed, create a new storage bucket.- If you don’t currently have an S3
bucket, follow the [AWS guidelines for creating your first
bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
We recommend including “stripe” in the name, such as “<name>-stripe-data.”
- Take note of this bucket name and the region because you’ll need them for
future steps.
[Start the onboarding
process](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#start-onboarding)-
Visit the [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline).
- Click **Get started**.
- Select the Amazon S3 logo and click **Next**.
- On this permissions step, you see code blocks that you can use to create the
IAM role and trust policy.
[Create a new permission
policy](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#create-permission-polcy)
To create a new permission policy:

- In your [AWS IAM console](https://console.aws.amazon.com/iam/), click
**Policies** > **Create policy** > **JSON**.
- Paste in the supplied JSON snippet from the Stripe onboarding step.
- In the Resource section of the JSON snippet, replace `BUCKET_RESOURCE` with
the bucket name you set.
- Provide a name for the new policy (for example,
`stripe-data-pipeline-policy`).
[Create a new trust role using a custom
policy](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#create-trust-role)
To create a new role using a custom policy:

- In your [AWS IAM console](https://console.aws.amazon.com/iam/), click
**Roles** > **Create role** > **Custom Trust Policy**.
- Paste in the supplied JSON snippet from the Stripe onboarding step.
- Click **Next** on the permissions page, then add the new role to your new
policy.
- Select the newly created policy name (for example,
`stripe-data-pipeline-policy`).
- Save the role with the following name: **stripe-data-pipeline-s3-role**. You
must use this exact name.
[Establishing your AWS S3
connection](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#establish-connection)-
Return to the Stripe Data Pipeline onboarding process.
- Enter the AWS Account ID, bucket name and region generated in the previous
step.
- Select your data encryption option. If you chose to use a customer managed
key, upload your public key. Check the step to [generate encryptions
keys](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#generate-encryption-keys)
to see how to create one.
- Click **Next**. Clicking **Next** sends test data to the bucket you provided,
but not production data.
- When you confirm test data delivery, go to your [S3
bucket](https://s3.console.aws.amazon.com/).
- Open the bucket, navigate to the `penny_test` directory, and open the acct_
prefixed sub-directory to locate the delivered `account_validation.csv` test
file.
- Download the `account_validation.csv` file.
- Upload this test file in your data pipeline onboarding step.
- Click **Confirm value**.
- When you confirm the test value, click **Subscribe**. This subscribes you to
the product and schedules the initial full load of data for delivery to your
Amazon S3 bucket, a process that can take 6-12 hours.
[OptionalGenerate encryption
keys](https://docs.stripe.com/stripe-data/access-data-in-warehouse/cloud-storage/aws-s3-storage#generate-encryption-keys)

## Links

- [Amazon S3 console](https://s3.console.aws.amazon.com/)
- [AWS guidelines for creating your first
bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
- [Data Pipeline
Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline)
- [AWS IAM console](https://console.aws.amazon.com/iam/)