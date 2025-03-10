# Migrate subscriptions to Stripe Billing using toolkit

## Learn how to migrate your existing subscriptions to Stripe using the toolkit.

Use the [Billing migration
toolkit](https://dashboard.stripe.com/billing/migrations) to migrate your
existing [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
from a third-party system, home-grown system, or an existing Stripe account to
Stripe Billing.

## Before you begin

- If you haven’t already, review the [migration
stages](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions#migration-stages).
- [Set up a Stripe Billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
before you begin migration. This is a one-time setup that you don’t need to
repeat for future migrations.
- [Request a PAN data
import](https://docs.stripe.com/get-started/data-migrations/pan-import) from
your current processor. This step is only required if you’re migrating to Stripe
from another processor. If you’re migrating from Stripe to Stripe, you can skip
this prerequisite.
- If you’re migrating from a third-party or home-grown system, carefully time
the cancellation of your existing subscriptions and the creation of new ones in
Stripe. To avoid missing a billing period, create the new subscriptions in
Stripe first, before canceling the old subscriptions. To avoid double billing,
cancel subscriptions in your old system before the subscriptions are set to
charge. For subscriptions with upcoming billing dates close to migration,
schedule them to start after the cycle so the final bill is in the old system.
[Open the Billing migration
toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#open-billing-toolkit)
Select the test-mode toggle on the top right corner if you want to run a test
migration first.

- Navigate to [Dashboard](https://dashboard.stripe.com/billing) >
[Subscriptions](https://dashboard.stripe.com/test/subscriptions) >
[Migrations](https://dashboard.stripe.com/test/billing/migrations).

Alternatively, you can click the overflow menu () next to **+ Create
subscription**, and select [Migrate
subscriptions](https://dashboard.stripe.com/settings/billing/migrations).
- To start your migration, click **Let’s get started**.
[Download a CSV
file](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#download-csv)
First, export your existing subscriptions by matching the exported data to a
migration-compatible CSV file. You can create your own CSV file, or download any
of the following CSV templates provided by Stripe:

-
[Basic](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#basic)
- [Multi-price
items](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#multi-price)
- [Ad-hoc
pricing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#ad-hoc)

You can also find examples of CSV files for common migration use cases in the
[Toolkit CSV
reference](https://docs.stripe.com/billing/subscriptions/toolkit-reference#migration-use-cases).

- Click **Download CSV template**.
- Choose a CSV template (basic, multi-price items, or ad-hoc pricing) based on
your billing use case.

### Basic CSV

This example shows a migration for common subscription use cases like quantity,
taxes, billing anchor, discounts, trials, and backdating.

### Specify the following fields for a Basic CSV file:

### Multi-price items CSV

This example shows a migration that has multiple products per subscription.

### Specify the following fields for a Multi-price items CSV file:

### Ad-hoc prices CSV

This example shows handling a subscription migration using [ad-hoc
pricing](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data)
for existing products.

### Specify the following fields for an Ad-hoc pricing CSV file:
- In the CSV file, specify the details of the subscriptions you want to export.

#### For Stripe-to-Stripe migrations

If you’re migrating subscriptions within Stripe accounts, refer to the [CSV
example](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)
before you specify and upload a CSV file.
[Upload a CSV
file](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#upload-csv)
Click **Upload CSV**. The CSV file size limit is 120 MB.

Stripe validates the file to verify that the uploaded subscriptions are in the
required CSV format. This process might take up to a few hours, depending on the
size of the file. If the file is valid, you can proceed to the next step in the
migration.

### Resolve validation errors

If you have any errors in your uploaded file, the toolkit displays a failure
summary. To resolve the errors:

- Click **Download file to review errors**.
- Review the `processing_error` column to see the errors.
- Correct all the errors. Common errors include:

ErrorTroubleshootingInvalid datesMake sure all the dates are in epoch or Unix
timestamp format.Incorrect `start_date` rangeMake sure the `start_date` for each
subscription is at least 24 hours in the future.Missing dataMake sure every
record contains the required fields.Incompatible price and taxMake sure prices
for specified tax rates have the same `tax_behavior` (inclusive versus
exclusive).
- Click **Upload revised file** to re-upload the corrected CSV (the CSV file
size limit is 120 mb).
- Wait for re-validation to see the latest validation status.
[Review uploaded
subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#review-subscriptions)
After Stripe validates your CSV file, review the summary of your uploaded
subscriptions for any discrepancies:

- Cross-check the summary for the correct:

- Date of upload
- Uploaded file name
- Number of subscriptions
- Number of customers
- First subscription go-live date
- If everything is valid, click **Start migration**.

If you see errors, click **Cancel migration** and restart the migration from
[Download a CSV
file](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#download-csv).
[Track migration
progress](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#track-migration)
After you review your uploaded subscriptions, track the progress of your
migration:

### Migration in progress

Your subscriptions are queued to schedule on the specified start date. This
process can take a few minutes to a few hours, depending on the size of the
file. For example, the validation and migration for 100,000 subscriptions takes
approximately 30 minutes to complete.

The Billing migration toolkit uses the [Subscription
schedule](https://docs.stripe.com/api/subscription_schedules) to migrate your
subscriptions. This allows your subscriptions to remain in a scheduled state for
24 hours before going live. In test mode, the buffer time is reduced to 1 hour
for faster evaluation and testing.

### Scheduled subscriptions

After migration, your subscriptions remain in a scheduled state for 24 hours
before going live. You have 10 hours to [cancel these scheduled
subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#cancel-migration)
using the toolkit.

Currently, you can’t update scheduled subscriptions using the toolkit. If you
want to update your scheduled subscriptions, you can either call the
[update](https://docs.stripe.com/api/subscription_schedules/update) endpoint, or
update each subscription (one-by-one) in the
[Subscriptions](https://dashboard.stripe.com/subscriptions) Dashboard.

Customers can’t cancel scheduled subscriptions from their customer portal. They
can only cancel live subscriptions.

### Go live with subscriptions

After 24 hours, your scheduled subscriptions go live and charge customers on
their applicable start dates. You can view all your live subscriptions in the
[Subscriptions](https://dashboard.stripe.com/subscriptions) Dashboard.

After the migration goes live, we recommend you monitor your subscriptions
starting from the first payment. Make sure the charge dates and amounts for the
migrated subscriptions match the specified
[start_date](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-start_date).

Customers can cancel live subscriptions from their customer portal.

### Monitor subscriptions

When you monitor your subscriptions after the migration goes live, look out for
problems related to payment methods.

For example, check transactions for unrecoverable issuer [decline
codes](https://docs.stripe.com/declines/codes) such as `incorrect_number` and
[take
action](https://docs.stripe.com/get-started/data-migrations/pan-import#post-import-payment-declines)
to make sure invoices get paid. Consider notifying customers with invalid
payment methods through channels other than email, such as text messages or
in-app notifications.

When using automatic collection, check [open or past due
invoices](https://docs.stripe.com/billing/collection-method#failed-incomplete-subscriptions)
to make sure customers aren’t missing [default payment
methods](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method),
which might cause the invoice to be unable to attempt collection.

[View all
migrations](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#view-migrations)
To view all of your migrations:

- Select the migration you want to review in
[Migrations](https://dashboard.stripe.com/billing/migrations).
- To open a migration, click **View** in the dropdown menu.

You can track the following fields:

- Upload date
- File name
- Stripe billing migration id
- Number of subscriptions
- Migration status
[OptionalCancel a
migration](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#cancel-migration)
If you identify any problems with the scheduled subscriptions, you can roll back
the migration and revert the scheduled subscriptions. The Dashboard displays a
timestamp to indicate if you can still cancel the migration using the toolkit.
You have 10 hours from when you scheduled the subscriptions to cancel them.
After 10 hours, the cancel option is disabled in the toolkit.

- Find the migration you want to cancel in your
[Migrations](https://dashboard.stripe.com/billing/migrations).
- Click **Cancel migration** in the dropdown menu.

### Cancel after 10 hours

To cancel the migration after 10 hours, you can either call the
[cancel](https://docs.stripe.com/api/subscription_schedules/cancel) endpoint, or
individually cancel each subscription (one-by-one) in the
[Subscriptions](https://dashboard.stripe.com/subscriptions) Dashboard.

[OptionalRun multiple
migrations](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#run-multiple-migrations)
You can run as many simultaneous subscription migrations as you want. For large
migrations, divide the subscriptions into batches and start with a small batch.
This can help you quickly identify any validation issues and save validation
time.

To start a new migration:

- Click **Start new migration**.
- Restart the migration process from [Download a CSV
file](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#download-csv).

You can also find examples of CSV files for common migration use cases in the
[Toolkit CSV
reference](https://docs.stripe.com/billing/subscriptions/toolkit-reference#migration-use-cases).

## See also

- [Toolkit CSV
reference](https://docs.stripe.com/billing/subscriptions/toolkit-reference)

## Links

- [Billing migration toolkit](https://dashboard.stripe.com/billing/migrations)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [migration
stages](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions#migration-stages)
- [Set up a Stripe Billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Request a PAN data
import](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [Dashboard](https://dashboard.stripe.com/billing)
- [Subscriptions](https://dashboard.stripe.com/test/subscriptions)
- [Migrations](https://dashboard.stripe.com/test/billing/migrations)
- [Migrate
subscriptions](https://dashboard.stripe.com/settings/billing/migrations)
-
[Basic](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#basic)
- [Multi-price
items](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#multi-price)
- [Ad-hoc
pricing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#ad-hoc)
- [Toolkit CSV
reference](https://docs.stripe.com/billing/subscriptions/toolkit-reference#migration-use-cases)
- [ad-hoc
pricing](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data)
- [CSV
example](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)
- [Download a CSV
file](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#download-csv)
- [Subscription schedule](https://docs.stripe.com/api/subscription_schedules)
- [cancel these scheduled
subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#cancel-migration)
- [update](https://docs.stripe.com/api/subscription_schedules/update)
- [Subscriptions](https://dashboard.stripe.com/subscriptions)
-
[start_date](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-start_date)
- [decline codes](https://docs.stripe.com/declines/codes)
- [take
action](https://docs.stripe.com/get-started/data-migrations/pan-import#post-import-payment-declines)
- [open or past due
invoices](https://docs.stripe.com/billing/collection-method#failed-incomplete-subscriptions)
- [default payment
methods](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method)
- [cancel](https://docs.stripe.com/api/subscription_schedules/cancel)
- [Toolkit CSV
reference](https://docs.stripe.com/billing/subscriptions/toolkit-reference)