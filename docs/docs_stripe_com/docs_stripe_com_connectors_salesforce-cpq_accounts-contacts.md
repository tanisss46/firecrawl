# Accounts and contacts

## Learn about syncing the Stripe customer objects for your corresponding Salesforce accounts.

After you set up the Stripe Billing Connector for Salesforce CPQ and [map your
data](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings), Stripe
creates a `Customer` object when an order finalizes. This happens when you
associate an account and a primary contact with a quote from an activated order.

If you use a parent-child hierarchy for your Salesforce accounts, make sure that
only the account that represents the billing entity (customer) correlates to an
activated order. Stripe Billing doesn’t currently support separate billing and
provisioning entities for subscriptions.

## Field mappings for Stripe customers

When you configure the connector to create a Stripe `Customer` object for each
Salesforce account, there isn’t a default mapping to a primary contact or order
on the account. All customer fields are also optional.

The connector syncs a Salesforce account’s `Name` and `Description` fields to
Stripe. To sync additional fields, you can [add field
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings) to
customize the data that’s synced from Salesforce to Stripe.

Salesforce field (Account object)Stripe
customerNotesName[Name](https://docs.stripe.com/api/customers/object#customer_object-name)Phone[Phone](https://docs.stripe.com/api/customers/object#customer_object-phone)Description[Description](https://docs.stripe.com/api/customers/object#customer_object-description)[Email](https://docs.stripe.com/api/customers/object#customer_object-email)By
default, the `Account` object in Salesforce doesn’t have an email field. You can
create a subscription without a payment; however, you must supply an email
address for collections.Billing street[Address, line
1](https://docs.stripe.com/api/customers/object#customer_object-address-line1)This
address might affect the customer’s tax calculation, depending on your tax
configuration. If the address is incomplete or differs from the billing address
on the quote or order, you must provide a custom mapping for this data.Billing
city[Address,
city](https://docs.stripe.com/api/customers/object#customer_object-address-city)Billing
state[Address,
state](https://docs.stripe.com/api/customers/object#customer_object-address-state)Billing
postal code[Address, postal
code](https://docs.stripe.com/api/customers/object#customer_object-address-postal_code)Billing
country[Address,
country](https://docs.stripe.com/api/customers/object#customer_object-address-country)Phone[Shipping,
address,
phone](https://docs.stripe.com/api/customers/object#customer_object-phone)Shipping
street[Shipping, address, line
1](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-line1)Shipping
city[Shipping, address,
city](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-city)Shipping
state[Shipping, address,
state](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-state)Shipping
postal code[Shipping, address, postal
code](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-postal_code)Shipping
country[Shipping, address,
country](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-country)
## Update account data

Account and contact information sync in real time. When you create or update
accounts in Salesforce, the connector creates and updates the Stripe `Customer`
objects with the latest information from Salesforce when an order syncs. Because
Salesforce is the primary source for account and contact information, any
updates you make to a `Customer` object in Stripe aren’t synced to the
corresponding account in Salesforce.

Stripe doesn’t allow merging of accounts. If you want to merge any customers in
Salesforce, you must do so before you sync the account to Stripe. `Customer`
objects synced to Stripe must have a valid ID in the Stripe ID field on the
account.

## Delete accounts

Deleting accounts or account information in Salesforce won’t affect the data in
Stripe. Any subscriptions in Stripe continue to bill and operate as normal. You
can’t delete Salesforce accounts with active subscriptions.

Deleting a customer in Stripe is irreversible, cancels all subscriptions, and
deletes any saved payment methods. The best practice is to retain the customer
unless you created it accidentally.

## Merge accounts

Salesforce allows you to merge up to three Salesforce accounts. Merging deletes
the dependent Salesforce accounts, and their dependent Salesforce records become
the primary Salesforce account’s records.

The connector doesn’t sync these changes into Stripe. Any Stripe subscriptions
that belong to the deleted Salesforce account still belong to the original
Stripe customer that corresponds to the deleted Salesforce account.

#### Note

The child account is the account that’s merged into the primary account.

## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)

## Links

- [map your
data](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Name](https://docs.stripe.com/api/customers/object#customer_object-name)
- [Phone](https://docs.stripe.com/api/customers/object#customer_object-phone)
-
[Description](https://docs.stripe.com/api/customers/object#customer_object-description)
- [Email](https://docs.stripe.com/api/customers/object#customer_object-email)
- [Address, line
1](https://docs.stripe.com/api/customers/object#customer_object-address-line1)
- [Address,
city](https://docs.stripe.com/api/customers/object#customer_object-address-city)
- [Address,
state](https://docs.stripe.com/api/customers/object#customer_object-address-state)
- [Address, postal
code](https://docs.stripe.com/api/customers/object#customer_object-address-postal_code)
- [Address,
country](https://docs.stripe.com/api/customers/object#customer_object-address-country)
- [Shipping, address, line
1](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-line1)
- [Shipping, address,
city](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-city)
- [Shipping, address,
state](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-state)
- [Shipping, address, postal
code](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-postal_code)
- [Shipping, address,
country](https://docs.stripe.com/api/customers/object#customer_object-shipping-address-country)