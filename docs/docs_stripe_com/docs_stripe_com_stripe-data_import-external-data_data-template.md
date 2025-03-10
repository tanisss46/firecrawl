# Transform external data using Data TemplatesPrivate preview

## Define rules in templates to map external data files to Stripe objects.

You can use Data Templates to upload and transform external data into
Destination records to make it compatible with Stripe products. Data Templates
are a set of data processing instructions that you can use to transform external
data into Destination records.

Data template settings include:

- Specifying the row in the file where the header is present
- Data types that the uploaded fields convert to
- Conditions to error out certain rows
- How the columns of an uploaded file map to the fields of the Destination
Records
[Create a Data
template](https://docs.stripe.com/stripe-data/import-external-data/data-template#create-data-template)
To create your Data Template:

- Go to the Stripe Dashboard > [Data
Management](https://dashboard.stripe.com/data-management) page.
- Select **Data Template**.
- Click **Add Data Template** and follow the steps in the details drawer to
create the Data template.
- In the **Data template details** step, enter a name for your template and
upload a CSV file with sample data.

#### Note

The header names and rows in your sample file must be the same as the CSV files
you plan to transform using the Data template.

[Configure your CSV
data](https://docs.stripe.com/stripe-data/import-external-data/data-template#configure-csv-data)
Configure how Stripe processes your external data using Stripe data types.

- In the **Header location** field, select your file’s header row number.
- Next, in the **Data types** section, verify or choose a data type for each
column.
- Click **CSV settings** to verify or adjust how your file is parsed.
[Select the destination Record
Type](https://docs.stripe.com/stripe-data/import-external-data/data-template#select-destination-record-type)
Configure how Stripe processes your external data using Stripe data types. You
can map user-uploaded data to Stripe using predefined destination record types.
Choose the appropriate record type and verify the columns in the uploaded sample
file to generate the selected destination record type.

In the **Select destination record type** step, choose how your data uploads and
maps to Stripe by selecting a Destination record type.

[Clean up and
validation](https://docs.stripe.com/stripe-data/import-external-data/data-template#cleanup-and-validation)
In the **Clean up and validate** step, you can use conditions to ignore or
validate records. There are two types of conditions:

- **Clean up conditions**: Add a clean up condition to ignore any records that
meet the condition.
- **Validation checks**: Add a validation check to identify errors or issues
with records and prevent those records from creating Stripe objects.
[Map
columns](https://docs.stripe.com/stripe-data/import-external-data/data-template#map-columns)
Associate the columns in your file to Stripe object attributes.

Mapping options include:

- Mapping a column from the file directly to the attribute
- Manually entering a string value in a text box to assign a hardcoded value to
a specific Stripe object attribute
- Using custom formulas, such as SUM, CONCAT, and FIND, for data transformation

To add data mappings:

- In the **Mandatory columns** section, add data mappings for each attribute.
- (Optional) In the **Optional columns** section, add a mapping for each data
column that maps to an optional Stripe object attribute.
- (Optional) In the **Custom columns** section, add any data columns that don’t
map directly to a Stripe object attribute.
- Click **Save and Activate** and view your Data template in the [Data
Template](https://dashboard.stripe.com/test/data-management/data-templates) List
page.
- Go to the [Import Set](https://dashboard.stripe.com/test/data-management)
page, and upload data using your template.

## Access to this feature is restricted but available by request

To sign up, please submit your email address.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Data Management](https://dashboard.stripe.com/data-management)
- [Data
Template](https://dashboard.stripe.com/test/data-management/data-templates)
- [Import Set](https://dashboard.stripe.com/test/data-management)
- [privacy policy](https://stripe.com/privacy)