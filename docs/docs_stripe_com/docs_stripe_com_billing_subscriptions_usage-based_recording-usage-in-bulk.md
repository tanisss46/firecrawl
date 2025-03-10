# Record usage for billing using Amazon S3

## Learn how to record usage events in bulk using an Amazon S3 storage bucket.

You must record usage in Stripe to bill your customers the correct amounts each
billing period. To record usage, you can send meter usage events to Stripe from
your Amazon S3 storage bucket. Stripe parses, validates, and transforms the
usage data into meter events.

After the events upload successfully, you can see them on your subscription
invoice.

## Before you begin

Make sure you have the following:

- Admin account access to the [Stripe
Dashboard](https://dashboard.stripe.com/dashboard)
- AWS account access to the [AWS Management
Console](https://console.aws.amazon.com/) and your S3 bucket
[Upload meter usage
events](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk#upload-meter-usage-events)
You can upload your meter usage events as a CSV, JSON, or JSON Lines file.

#### Need support for a different file format?

If you want to upload files with a different structure or in a custom format,
[contact us](mailto:user-data-acquisition-platform@stripe.com).

### File format and fields

Make sure your file follows the sample file format:

CSVJSONJSON Lines

![Example of the CSV file
format](https://b.stripecdn.com/docs-statics-srv/assets/udap_ubb_csv_format.e5c12ef6a48b407ae9c0cf6c3b873aeb.png)

CSV file format

Follow the [Meter Event](https://docs.stripe.com/api/billing/meter-event/object)
schema when including the following fields in your file:

FieldDescription`identifier`A unique identifier for the event. If you don’t
provide one, Stripe can generate the unique identifier. We recommend using a
globally unique identifier.`timestamp`The time that the event occurred, measured
in seconds since the Unix epoch.`event_name`The name of the meter event.
`payload_columns`

The set of columns that contain key names for customer and numerical usage
values:

- `payload_stripe_customer_id`: The [Customer
ID](https://docs.stripe.com/api/customers/object#customer_object-id) that the
event gets created against.
- `payload_value`: The numerical usage value of the meter event. By default, the
column name is `payload_value`. If you specified a different field name when
creating the meter event, you must update the column name to match the key
value. For example, if you specify tokens in the `value_settings`, update the
column name to `payload_tokens`.
[Prepare your files in Amazon
S3](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk#prepare-files)
You can validate your connection configuration using well-formatted data in your
S3 bucket. The configuration process shows the available files, and runs an
initial sync when configuring the connection.

- Navigate to your [Amazon S3 console](https://s3.console.aws.amazon.com/).
- Make sure to store your files in a designated S3 bucket that’s organized
according to your import preferences. If needed, follow the [AWS
guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
to create an S3 bucket.

For successful retrieval, Stripe requires that file names adhere to [S3 object
naming
conventions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html)
and files are 1 GB maximum.
- Remember the bucket name and region because you need them for future steps.
- Keep your [AWS Management Console](https://console.aws.amazon.com/) open to
configure an IAM role later.
[Configure the Amazon S3 Connector to import
files](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk#dashboard-ui)
First, use the Stripe Dashboard to add the Amazon S3 Connector.

- In the Stripe Dashboard, on the **Data management** >
[Connectors](https://dashboard.stripe.com/data-management/connectors) tab, click
**Add connector**.
- In the **Choose connector** dialog, select **Amazon S3**.
- In the **Requirements** dialog, enter a unique name for **Connector name**,
then click **Next**.
- Complete the steps in the **Permissions** dialog.

Next, configure the appropriate permissions for the Amazon S3 Connector.

- In the AWS Management Console, navigate to the [IAM
console](https://console.aws.amazon.com/iam/).
- Create a custom trust policy:- In the navigation pane, click **Policies** >
**Create policy**.
- Select **JSON**, and replace the existing policy text by copying and pasting
the code block provided in the Stripe Dashboard.
- In the `Resource` section of the **Policy editor** code block, replace
`USER_TARGET_BUCKET` with your intended bucket name.
- Click **Next**.
- Under **Policy details**, add a policy name. Optionally add any tags.
- Click **Create policy**.
- Create a role:- In the navigation pane, click **Roles** > **Create role**.
- Select **Custom trust policy**, and copy and paste the code block provided in
the Stripe Dashboard.
- Click **Next**.
- Locate and select the newly created permission policy to enable it, then click
**Next**.
- and paste the provided role name, then click **Create role** to create a
role name.

Then, make sure to establish a connection between Stripe and your Amazon S3
bucket.

- In the AWS Management Console, do the following:- Provide your [AWS account
ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId).
- Provide the Bucket Name and Region.
- If you use folders to organize your files in your Amazon S3 bucket, specify a
folder within the above bucket. We only fetch data from the specified folder,
not the entire bucket.
- After you set up a new connector, the file preview validates that your
credentials connect Stripe with the expected Amazon S3 bucket and folder. Stripe
fetches all data modified in the last 90 days. This occurs every 5 minutes for
objects with a `LastModified` date later than the last sync.
- Preview the files available in the connected Amazon S3 bucket:- File names
must be under 255 characters and include the appropriate extension, such as
`.csv`, `.json`, or `.jsonl`.
- Initial and recurring imports have an expected file format:- JSON files have
**Billing Meter Event Transaction Template - JSON**.
- JSON Lines files have **Billing Meter Event Transaction Template - JSONLINE**.
- CSV files have **Billing Meter Event Transaction Template - CSV**.
- To create an active data connection and initiate the data import, click
**Done**.

After you upload a file to the Amazon S3 Connector, the usage events update
within 5 minutes. This might take longer if your bucket contains a lot of
unprocessed files.

You can check the status and details of processed files on the [Import
set](https://dashboard.stripe.com/data-management/import-set) tab in the Stripe
Dashboard.

## Rate limits

You can upload any number of files and records to your Amazon S3 bucket. Upload
a file every 10 seconds or when the current file reaches one million records,
whichever comes first. After upload, you can add events in a new file.

Avoid creating empty files, such as:

- CSV files that contain only the header row
- JSON files that contain only [] (empty square brackets)
- JSON Lines files that contain only {} (empty curly brackets)

Although Amazon S3 accepts non-zero byte files, they increase the object and
file count, which might cause delays in the polling of files.

Amazon S3 polls a maximum of 50 files or up to 10 GB of data, and processes your
uploaded data at a rate of 10,000 events per second. If you upload large files
or a high volume of files, Stripe polls and processes the data to maintain this
throughput rate.

For example, if you upload 100 files that each contain 100,000 records daily, it
can take approximately 17 minutes to process the entire dataset (10 million
events).

## Report and handle errors

Stripe polls the files that you upload to the Amazon S3 bucket and then
processes these files asynchronously. If we detect errors during processing,
Stripe notifies you using [events](https://dashboard.stripe.com/events).

### Format issues

Invalid file or record format errors occur when the contents in the uploaded
file contain formatting or data issues.

You can subscribe to these events using a [webhook
endpoint](https://dashboard.stripe.com/webhooks). Based on the event type, you
can implement your own logic to handle these errors.

EventDescriptionPayload type`data_management.import_set.failed`Stripe creates a
[data_management.import_set.failed](https://docs.stripe.com/api/events/types#event_types-data_management.import_set.failed)
event when processing fails for an entire file. For example, if you omit a
mandatory column, such as `event_name`. You can find the reason for failure in
the `failed_reason` parameter of the event, and fix it before
re-uploading.`Snapshot`
`data_management.import_set.succeeded`

Stripe creates a
[data_management.import_set.succeeded](https://docs.stripe.com/api/events/types#event_types-data_management.import_set.succeeded)
event when individual records fail in a partially processed file. For example,
if you omit a value for a mandatory field, such as `stripe_customer_id` or
`event_name`.

You can find details of the failed records in the `status` parameter of the
event. A `succeeded_with_errors` status indicates that at least one record
failed because of invalid formatting. The `result.errors` gives the number of
records that failed and the `file_id` of the file containing the failed records.

Use the [Files](https://docs.stripe.com/file-upload#download-file-contents) API
to download a complete list of the failed records and detailed error
descriptions.

`Snapshot`

### Data issues

Files with correct formatting can fail processing because of invalid data within
the file, such as incorrect values for the `event_name` or `stripe_customer_id`.

For detailed information about these failures, you can subscribe to the
following events using a [webhook
endpoint](https://dashboard.stripe.com/webhooks).

EventDescriptionPayload type`v1.billing.meter.error_report_triggered`This event
occurs when a meter has invalid usage
events.`thin``v1.billing.meter.no_meter_found`This event occurs when usage
events have missing or invalid meter IDs.`thin`
#### Warning

To create an event destination that subscribes to thin events, enable Workbench
in your [Developer settings](https://dashboard.stripe.com/settings/developers).

### Example payloads

Example error report eventExample error event for an incorrect meter
The following is an example payload for a
`v1.billing.meter.error_report_triggered` event.

```
{
 "id": "evt_test_65R2GpwDsnmpzihMjdT16R2GDhI4SQdXJGRbvn7JA8mPEm",
 "object": "v2.core.event",
 "created": "2024-08-28T20:54:12.051Z",
 "data": {
 "developer_message_summary": "There is 1 invalid event",
 "reason": {
 "error_count": 1,
 "error_types": [
 {
```

See all 35 lines
### Error codes

The `reason.error_types.code` provides the error categorization that triggered
the error. Possible error codes include:

- `meter_event_customer_not_found`
- `meter_event_no_customer_defined`
- `meter_event_dimension_count_too_high`
- `archived_meter`
- `timestamp_too_far_in_past`
- `timestamp_in_future`
- `meter_event_value_not_found`
- `meter_event_invalid_value`
- `no_meter` (supported only for the `v1.billing.meter.no_meter_found` event
type)

### Listen to events

You can listen to events by setting up an [event
destination](https://docs.stripe.com/event-destinations).

- On the [Event destinations](https://dashboard.stripe.com/webhooks) tab in
Workbench, click **Create new destination**. Alternatively, use this
[template](https://dashboard.stripe.com/webhooks/create?payload_style=thin&events=v1.billing.meter.error_report_triggered%2Cv1.billing.meter.no_meter_found)
to configure a new destination in Workbench with the two event types
pre-selected.
- Click **Show advanced options**, then select the **Thin** payload style.
- Select `v1.billing.meter.error_report_triggered` and
`v1.billing.meter.no_meter_found` from the list of events.
- Create a handler to process the event.

```
import os
from stripe import StripeClient
from stripe.events import V1BillingMeterErrorReportTriggeredEvent

from flask import Flask, request, jsonify

app = Flask(__name__)
api_key = os.environ.get('STRIPE_API_KEY')
webhook_secret = os.environ.get('WEBHOOK_SECRET')

```

See all 35 lines
- Test your handler by configuring a [local
listener](https://docs.stripe.com/cli/listen) with the [Stripe
CLI](https://docs.stripe.com/stripe-cli) to send events to your local machine
for testing before deploying the handler to production. Use the
`--forward-thin-to` flag to specify which URL to forward the `thin` events to
and the `--thin-events` flag to specify which thin events to forward to your
application. You can forward all thin events with an asterisk (`*`), or a subset
of thin events.

```
$ stripe listen --forward-thin-to localhost:4242/webhooks --thin-events "*"

```
- Trigger test events to your handler. Use the [trigger
function](https://docs.stripe.com/cli/trigger) to run the following commands,
which simulates the respective events in your account for testing.

```
$ stripe trigger v1.billing.meter.error_report_triggered --api-key
<your-secret-key>
$ stripe trigger v1.billing.meter.no_meter_found --api-key <your-secret-key>

```
- If you process events with a webhook endpoint, [verify the webhook
signatures](https://docs.stripe.com/webhooks#verify-official-libraries) to
secure your endpoint and validate all requests are from Stripe.
- Correct the invalid events and save them to a new file. Then, upload the file
to your Amazon S3 bucket for processing.

## Links

- [Stripe Dashboard](https://dashboard.stripe.com/dashboard)
- [AWS Management Console](https://console.aws.amazon.com/)
- [Meter Event](https://docs.stripe.com/api/billing/meter-event/object)
- [Customer ID](https://docs.stripe.com/api/customers/object#customer_object-id)
- [Amazon S3 console](https://s3.console.aws.amazon.com/)
- [AWS
guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
- [S3 object naming
conventions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html)
- [AWS Management Console](https://console.aws.amazon.com)
- [Connectors](https://dashboard.stripe.com/data-management/connectors)
- [IAM console](https://console.aws.amazon.com/iam/)
- [AWS account
ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId)
- [Import set](https://dashboard.stripe.com/data-management/import-set)
- [Contact sales](https://stripe.com/contact/sales)
- [events](https://dashboard.stripe.com/events)
- [webhook endpoint](https://dashboard.stripe.com/webhooks)
-
[data_management.import_set.failed](https://docs.stripe.com/api/events/types#event_types-data_management.import_set.failed)
-
[data_management.import_set.succeeded](https://docs.stripe.com/api/events/types#event_types-data_management.import_set.succeeded)
- [Files](https://docs.stripe.com/file-upload#download-file-contents)
- [Developer settings](https://dashboard.stripe.com/settings/developers)
- [event destination](https://docs.stripe.com/event-destinations)
-
[template](https://dashboard.stripe.com/webhooks/create?payload_style=thin&events=v1.billing.meter.error_report_triggered%2Cv1.billing.meter.no_meter_found)
- [local listener](https://docs.stripe.com/cli/listen)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [trigger function](https://docs.stripe.com/cli/trigger)
- [verify the webhook
signatures](https://docs.stripe.com/webhooks#verify-official-libraries)