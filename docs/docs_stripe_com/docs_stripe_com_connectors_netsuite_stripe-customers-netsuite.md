# Stripe customers in NetSuite

## Learn about how the connector automatically represents Stripe customers in NetSuite.

The Stripe Connector for NetSuite automatically syncs your Stripe invoices and
associated customers to NetSuite as invoices and customer records. This applies
to Stripe invoices that you send and payments made by customers with saved
details in Stripe. The connector creates or links the customer during the first
transaction with that customer.

The connector can represent customers in NetSuite in the following ways:

- [Sync a new Stripe customer as a new NetSuite
customer](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#new-customer)
- [Link a new Stripe customer to an existing NetSuite
customer](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#existing-customer)
- [Associate all customers with a single global
customer](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#no-customer-data)

If you don’t want customer data in NetSuite, use the single global customer.

## Sync a new Stripe customer to a new NetSuite customer

The connector syncs each Stripe customer to NetSuite as a customer record. This
allows you to capture and analyze customer data in NetSuite, create detailed
reports on customer spending, and manage receipts in NetSuite.

In some cases, you might not want to create a customer record for every Stripe
customer. For example:

- If product signup in your business flow doesn’t require payment, the connector
still creates a NetSuite customer record for the Stripe customer, without any
accounting impact. This approach might cause additional impacts to your NetSuite
customer database.
- If you have a high volume of customer sign-ups (thousands per day) and
customer data reporting isn’t necessary in NetSuite, we don’t recommend this
approach—it can add more entries in your NetSuite customer database than your
NetSuite environment can handle.
- If you have a high volume of customers created daily in your NetSuite account,
the amount of associated traffic can impact the connector’s sync time.

### Customer sync timing

By default, the connector creates a NetSuite customer record when it syncs a
Stripe customer’s first transaction.

Alternatively, you can do either of the following:

- Configure the connector to create the NetSuite customer record immediately
after Stripe customer creation. To do so, ask your implementation partner to
disable the `Disable customer events` feature. Consult with your implementation
partner to understand all accounting and technical implications.
- Delay syncing customers by [adding
metadata](https://docs.stripe.com/connectors/netsuite/custom-payment-application#override-sync-timing)
that specifies when the connector creates the NetSuite customer record. Ask your
implementation partner for more information.

### Customer details to sync

The connector syncs the following customer details from Stripe to NetSuite. You
can use Stripe metadata to map additional fields, override most of the fields
below, or specify default values for NetSuite fields.

Stripe fieldNetSuite fieldDescriptionStripe IDEntity ID and external IDNetSuite
requires an entity ID. If you don’t specify a name in Stripe (either a company
name or an individual’s first and last name), the connector uses the Stripe ID
as the entity ID in NetSuite. The Stripe customer ID starts with a `cus_` and is
unique across all NetSuite customer records.EmailEmailIf you don’t specify an
email address in Stripe, the connector uses the Stripe customer
ID.DescriptionCompany Name (or first and last name)NetSuite requires a customer
name. If you don’t specify a name in Stripe, the connector uses the customer’s
email address.PhonePhoneThe `Phone` field on the Stripe customer maps to the
header-level `Phone` field on the NetSuite customer record.
Shipping Address

Default Shipping Address

If specified on the Stripe [customer](https://docs.stripe.com/api/customers),
the NetSuite customer record uses this as the default shipping address. The
connector uses the following fields: `Name`, `Phone`, `Address1`, `Address2`,
`City`, `State`, `Zip`, and `Country`.

The country field is optional. If you don’t specify a country in Stripe, the
connector uses the default country in your NetSuite account. Use two character
codes (ISO2) or full names that conform to the [ISO-3166
standard](https://en.wikipedia.org/wiki/ISO_3166-1). If the values don’t
conform, the connector sets it to empty.

Billing Address

Default Billing Address

If specified on the Stripe customer’s [payment
source](https://docs.stripe.com/api/payment_methods), the NetSuite customer
record uses this as the default billing address. The connector uses the
following fields: `Address1`, `City` or `Zip`, and `State`.

The country field is optional. If you don’t specify a country in Stripe, the
connector uses the default country in your NetSuite account. Use two character
codes (ISO2) or full names that conform to the [ISO-3166
standard](https://en.wikipedia.org/wiki/ISO_3166-1). If the values don’t
conform, the connector sets it to empty.

### Create a customer in NetSuite

NetSuite has two types of customers: company and individual. The connector
creates customers as a company, by default.

If you want to create a customer as an individual, NetSuite requires a first and
last name. You can pass the name to NetSuite in one of the following ways:

MethodDescription
Use the `name` field on the Stripe customer

If you pass the full name in the `name` field, the connector uses the first
space in the `name` to split the full name into a first name and a last name.

For example, “Jane Sally Doe” syncs as “Jane” for the first name and “Sally Doe”
for the last name. If you collect name prefixes, such as “Sir” in “Sir Richard
Branson,” use metadata so that “Sir” isn’t used as the first name.

Use the `description` field on the Stripe customerIf you pass the full name in
the `description` field, the connector uses the first space in the `description`
to split the full name into a first name and a last name.
Use metadata

Here’s an example of passing the first name and last name using metadata:

```
Stripe::Customer.create(
 description: "Sample Customer",
 email: "customer@example.com",
 metadata: {
 netsuite_first_name: 'First',
 netsuite_last_name: 'Last'
 }
)

```

### Update customer data in NetSuite

The connector doesn’t automatically update NetSuite customer records after
creating them. This prevents any updates made to the Stripe record from
overriding the updates you make to the customer records in NetSuite.

If you create NetSuite customers in one system (for example, Salesforce to
NetSuite) and want future updates to sync to the NetSuite customer, you can use
your existing integration. Link the NetSuite customer to the Stripe customer by
adding the NetSuite internal ID to the Stripe customer, or by using the
[customer matching
system](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#customer-matching-system).

### Multiple currencies

If you accept payments in multiple currencies, the connector adds all active
NetSuite currencies to your Stripe-created NetSuite customers.

## Link a new Stripe customer to an existing NetSuite customer

If you have customers in both Stripe and NetSuite, you can link customers
between the two systems using either the customer matching system or metadata.
Linking existing customers can prevent duplicate customers in Stripe or
NetSuite.

### Customer matching system

The customer matching system uses standard fields (such as the name or
description) or custom fields (such as metadata in Stripe or custom fields in
NetSuite).

You can automatically link Stripe customers to existing NetSuite customers by
entering fields with matching data in the following: **Customer matching
NetSuite field** and **Customer matching Stripe field**.

For example, you can use an email address or an internal customer ID that’s on
both the Stripe customer and the NetSuite customer.

The customer matching system has the following requirements:

- Only customer records are matched. The connector won’t match leads, contacts,
and so on.
- The full data contained in each field must match.
- You can’t use partial data or strings that contain the data. For example, the
connector can’t match a NetSuite field with ID `12345` to a Stripe description
with `company ID 12345`.
- Whitespace or capitalization don’t affect the matching process.

The connector uses the first match found, if it finds multiple matches. If it
doesn’t find any matches, the connector creates a unique customer record in
NetSuite for the Stripe customer, by default. Alternatively, the connector uses
a generic Stripe customer, if you enabled the `Global Stripe customer workflow`
setting.

### NetSuite ID in Stripe metadata

Link existing NetSuite customer records to Stripe customers by specifying the
internal ID for the NetSuite customer in the Stripe customer metadata. For
example, `netsuite_customer_id: 123`.

The customer sync fails if the connector can’t find a NetSuite customer with the
specified internal ID. To resolve this, you can manually link the NetSuite
customer record and Stripe customer in the Stripe app records synced drawer.

### Update matched customers

Before the customer matching system links a Stripe customer to an existing
customer in NetSuite, the connector verifies if the `externalId` field on the
customer record has a value. If it does, the connector doesn’t update the field,
to prevent overriding an important identifier used by another system.

The connector always attempts to add the Stripe customer ID (starting with
`cus_`) to the `comments` field on the NetSuite record. You can also configure
NetSuite to exclude the `comments` field on the customer. If the external ID
contains a value and the `comments` field is excluded, the connector might not
update the NetSuite customer. You won’t see the customers linked in NetSuite,
only in Stripe.

### Merge duplicate customers

If the connector creates a duplicate customer, you can merge it with an existing
customer while maintaining a link to the Stripe customer. When you merge
customers in NetSuite, the source customer is deleted and the target customer
remains.

You can merge a customer with a NetSuite customer that the connector created or
linked. Make sure the customer that you created or linked is the target customer
(entered, not merged). Doing so allows the same NetSuite customer to remain
linked and the connector to use it for future transactions with that customer.

The merge might delete the NetSuite customer (source customer) that the
connector created or linked. If so, the connector does either of the following,
based on your setup:

- If you use the customer matching system, the connector detects the deleted
customer and searches for an existing customer in NetSuite to match instead. The
connector uses the matching fields that you specify in your app settings.
- If you don’t use the customer matching system, the customer link breaks. You
can use the Stripe ID to search for the customer in the Stripe app records
synced drawer. In the failed customer record, you can use the manual override
tool to re-link the customers with the new NetSuite customer’s internal ID.

## Associate all customers with a single global customer

If you don’t want customer data in NetSuite, you can associate all Stripe
customers with a single global customer called `Stripe Unallocated Charges`. Use
this method if you have a high volume of new customers, signup is self-serve,
and reporting on customers in NetSuite isn’t required.

Stripe charges that were created without a customer appear as charges under
`Stripe Unallocated Charges`.

### NetSuite multi-subsidiary customer

This feature allows you to associate a single NetSuite customer with multiple
subsidiaries. The connector doesn’t support this feature in all cases, and
generally requires that customers in a subsidiary have a 1:1 relationship with
customers in a Stripe account. To prevent issues–for example, with the Stripe
Billing and Invoicing workflow–create unique NetSuite customers for each
subsidiary.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)

## Links

- [Sync a new Stripe customer as a new NetSuite
customer](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#new-customer)
- [Link a new Stripe customer to an existing NetSuite
customer](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#existing-customer)
- [Associate all customers with a single global
customer](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#no-customer-data)
- [adding
metadata](https://docs.stripe.com/connectors/netsuite/custom-payment-application#override-sync-timing)
- [customer](https://docs.stripe.com/api/customers)
- [ISO-3166 standard](https://en.wikipedia.org/wiki/ISO_3166-1)
- [payment source](https://docs.stripe.com/api/payment_methods)
- [customer matching
system](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite#customer-matching-system)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)