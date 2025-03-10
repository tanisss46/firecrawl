# Export data to a data warehouse

## Automate data exports from Stripe to Snowflake or Redshift.

Data Pipeline currently supports
[Snowflake](https://docs.snowflake.com/en/user-guide/intro-regions.html)
(deployed on AWS) and [Amazon
Redshift](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html)
data regions. For additional information on supported instances, view the table
below.

AWS RegionSnowflake Amazon Redshift RA3 (with encryption) us-west-2
(Oregon)us-east-2 (Ohio)us-east-1 (N. Virginia)us-west-1 (N.
California)ca-central-1 (Central Canada)sa-east-1 (São Paulo)eu-central-1
(Frankfurt)eu-west-1 (Ireland)eu-west-2 (London)eu-west-3 (Paris)eu-north-1
(Stockholm)me-south-1 (Bahrain)ap-southeast-1 (Singapore)ap-southeast-2
(Sydney)ap-northeast-1 (Tokyo)ap-northeast-2 (Seoul)ap-east-1 (Hong Kong)
#### Note

If you’re using another data warehouse besides Snowflake or Amazon Redshift, or
if your warehouse region isn’t listed above, let us know at
[data-pipeline@stripe.com](mailto:data-pipeline@stripe.com).

## Get started

When you sign up for Data Pipeline, Stripe sends a data share to your Snowflake
or Amazon Redshift account. After you accept the data share, you can access your
core Stripe data in Snowflake or Amazon Redshift within 12 hours. After the
initial load, your Stripe data [refreshes
regularly](https://docs.stripe.com/stripe-data/available-data).

#### Note

You can only have one warehouse account connected to your Stripe account.

SnowflakeAmazon Redshift RA3
### Link your Snowflake account

First, send all your up-to-date Stripe data and reports through the Dashboard:

- On the [Data Pipeline
settings](https://dashboard.stripe.com/settings/stripe-data-pipeline) page in
the Dashboard, click **Sign up**.
- From the drawer, select **Snowflake**, then click **Continue**.
- Enter your Snowflake [Account
Identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html)
and your AWS region, then click **Next**.
- the SQL from the code block and insert it in a SQL worksheet in Snowflake
warehouse and run the query to retrieve the unique value. Enter the value in the
text box and click **Subscribe**.

### Access your data share in Snowflake

Next, after 48 hours, access your data share from your Snowflake account:

- Navigate to your Snowflake account to accept the Stripe data share.
- In Snowflake, have an `ACCOUNTADMIN` navigate to **Data** > **Shared Data**.
In the **Ready to Get** section, navigate to a share entitled
`SHARE_[ACCOUNT_IDENTIFIER]` from one of three Stripe accounts, depending on
your data warehouse region:- `GSWUDFY_STRIPE_AWS_US_EAST_1`: data warehouses in
`us-east-1`
- `JZA07263`: data warehouses in `us-west-2`
- `VM70738`: data warehouses in `us-east-2`
Then, click **Get shared data** to accept the share.
- In the modal that opens, give the database a name (for example, “Stripe”),
select the roles to grant access to (for example, `SYSADMIN`), then click **Get
Data**.
- Confirm that you can view your Stripe data in **Data From Direct Shares** and
**Databases**. You can now query your Stripe data directly in Snowflake.

### Change the warehouse account

To change the warehouse account your Stripe account is connected to:

- Turn off Data Pipeline from the Dashboard [settings
page](https://dashboard.stripe.com/settings/stripe-data-pipeline).
- Sign up for Data Pipeline again using the steps detailed above for the new
warehouse account you want to connect to.

To add another Stripe account to your warehouse account:

- Follow the [sign
up](https://docs.stripe.com/stripe-data/access-data-in-warehouse/data-warehouses#get-started)
steps above for your new Stripe account.
- Use the same account identifier as above for the respective warehouse. To find
your Account ID, navigate to the Dashboard [settings
page](https://dashboard.stripe.com/settings/stripe-data-pipeline) and locate
**ID** under the **Connected data warehouse** section.

## Query Stripe data in your data warehouse

In Snowflake and Amazon Redshift, your data is available as secure views. To
query your data, follow the steps below.

SnowflakeAmazon Redshift RA3
View your available Stripe data by navigating to **Views** in the database you
created. For each table, you can also see the available columns by clicking on
the table and navigating to **Columns**.

## Financial reports in Data Pipeline

To facilitate your financial close, you can access Stripe’s
[reports](https://docs.stripe.com/stripe-reports) directly in your data
warehouse.

#### Note

At this time, financial reports aren’t available for Amazon Redshift.

Financial report templates have a `FINANCIAL_REPORT` prefix and are available as
views in your data warehouse.

!

### Generating financial reports in Snowflake

Generating financial reports from Data Pipeline requires setting a few custom
variables. These are the same variables you set when generating the report
through the Dashboard or API:

- `START_DATE` (varchar)—The starting date of the report (inclusive).
- `END_DATE` (varchar)—The ending date of the report (exclusive).
- `TIMEZONE` (varchar)—The time zone of non-UTC datetime columns.

To set these variables and run the report query:

- Create a new worksheet.
- Set the database schema and required variables to your desired values.

```
-- set schema based on the name you gave your Stripe database
use schema db_name.stripe;
-- set financial report template variables
set (TIMEZONE, START_DATE, END_DATE) = ('UTC', '2021-09-01', '2021-10-01');
```

#### Caution

Run these lines of code separately before attempting to query tables that
require them. Otherwise, you might receive an error that a session variable
doesn’t exist.

If you’re using the [Snowflake Connector for
Python](https://docs.snowflake.com/en/user-guide/python-connector.html), set the
session parameter `TIMEZONE` with the `ALTER SESSION SET TIMEZONE = 'UTC'`
command.
- After running the code that sets the necessary variables, query the view of
the report you want to generate. For example, running:

```
select * from FINANCIAL_REPORT_BALANCE_CHANGE_FROM_ACTIVITY_ITEMIZED;
```

Returns the same results that the itemized balance change from the activity
report displays in the Dashboard or through the API:

!

#### Need support for a different file format?

If you want to upload files with a different structure or in a custom format,
[contact us](mailto:data-pipeline@stripe.com).

## Links

- [Snowflake](https://docs.snowflake.com/en/user-guide/intro-regions.html)
- [Amazon
Redshift](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html)
- [refreshes regularly](https://docs.stripe.com/stripe-data/available-data)
- [Data Pipeline
settings](https://dashboard.stripe.com/settings/stripe-data-pipeline)
- [Account
Identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html)
- [reports](https://docs.stripe.com/stripe-reports)
- [Snowflake Connector for
Python](https://docs.snowflake.com/en/user-guide/python-connector.html)