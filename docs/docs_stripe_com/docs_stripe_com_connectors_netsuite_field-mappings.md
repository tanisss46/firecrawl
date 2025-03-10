# Field mappings

## Learn how to customize data synced to your NetSuite records using the Stripe Connector for NetSuite.

You use field mappings when you want additional reporting or categorization of
records in NetSuite, or to add values for required fields that the connector
needs to create records.

The Stripe Connector for NetSuite provides two ways for you to add data to your
NetSuite records:

- [Field
defaults](https://docs.stripe.com/connectors/netsuite/field-mappings#field-defaults)
(static)
- [Field
mappings](https://docs.stripe.com/connectors/netsuite/field-mappings#field-mappings-values)
(dynamic)

You can find both mapping methods in the connector app when you navigate to
**Settings** > **Field mappings**. This allows you to customize the data that’s
synced to NetSuite, for example, if you require more data in the NetSuite record
than what’s synced by default.

## Field defaults

You can add field defaults (static values) to any record that the integration
creates, even if it’s not present in Stripe. If one of your NetSuite records has
a required field, the connector must include a value for that field to create
the record. Otherwise, the request to create the record fails with an error.

For example, if your invoice form has a required `Class` field, you must provide
a value for `Class` so the connector can create the record. Because `Class` is a
`recordReference` or dropdown field, the connector needs the internal ID of the
value to use as the field default. To use the value `Corporate` with
`internalID: 5`, you enter the following JSON hash:

```
invoice: {
 "klass_id": 5
}

```

If the invoice line item requires the same field, you enter the following JSON
hash:

```
invoice_item: {
 "klass_id": 5
}

```

In the above examples, we use `klass` instead of `class`, which is specific to
the NetSuite API for this field. The suffix `_id` indicates to NetSuite that the
field value is a `recordReference` (dropdown). Another common suffix is `_date`,
which indicates a NetSuite date field that must be in Unix timestamp format.

#### Common mistake

The same error message displays if the following are missing: required fields,
header level fields for `invoice`, or line level fields for `invoice_item`. If
you add the header level mapping and the record fails to sync, you can try
adding the line level mapping.

## Field mappings

You can pass field mappings (dynamic values) from Stripe to NetSuite. To do so,
the connector retrieves data from the Stripe field and records it in the
NetSuite field.

For example, your system that’s integrated with Stripe passes a `company_id` to
the metadata of each payment. You want that ID passed to a custom field on the
NetSuite customer payment for tracking purposes. To do so, you set up the
following field mapping:

```
customer_payment: {
 "metadata.company_id": "custbody_company_identifier"
}

```

The above example uses the suffix `_identifier` instead of `_id` on the custom
field in NetSuite. Custom fields must use a value other than the suffix `_id`
because NetSuite uses `_id` to indicate a record reference or dropdown field
type.

For example, a field default for setting a revenue recognition rule on service
sales items might look as follows:

```
"service_sale_item": { "revenue_recognition_rule_id": 123 }

```

## Overwrite customizations

When the connector creates a record in NetSuite, it maps a standard set of data
from the Stripe record to the NetSuite record. For example, the Stripe customer
ID and email map to the NetSuite customers created by the connector.

If you want to overwrite the connector’s standard data mappings, you can use
field defaults or field mappings. If you have a default mapping (static) and a
field mapping (dynamic) on the same NetSuite field, the field mapping takes
precedence over the field default.

For example, the connector maps the Stripe customer name to the NetSuite field
`company_name`. NetSuite copies the value for the `company_name` to the entity
ID, by default. The connector overrides this functionality and uses the Stripe
customer ID instead to make sure it meets the NetSuite requirement of using a
unique entity ID. Don’t use the Stripe customer ID—we recommend using a unique
ID instead.

In this case, you can override the standard data mapping by nullifying the
entity ID. This allows NetSuite to copy the customer name as the entity ID, and
use the default NetSuite behavior.

```
"customer": {
 "entity_id": null
 }

```

## See also

- [Stripe and NetSuite fields and
references](https://docs.stripe.com/connectors/netsuite/fields-references)
- [NetSuite schema
browser](https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2018_2/script/record/campaign.html)

## Links

- [Field
defaults](https://docs.stripe.com/connectors/netsuite/field-mappings#field-defaults)
- [Field
mappings](https://docs.stripe.com/connectors/netsuite/field-mappings#field-mappings-values)
- [Stripe and NetSuite fields and
references](https://docs.stripe.com/connectors/netsuite/fields-references)
- [NetSuite schema
browser](https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2018_2/script/record/campaign.html)