# Field defaults and custom mappings

## Map corresponding fields from Salesforce objects to Stripe objects.

When setting up the Stripe Billing Connector for Salesforce CPQ, you use the
data mapper to map the fields from the Salesforce objects to corresponding
fields on the Stripe objects.

Not all objects have a Stripe ID field in the data mapper. For example, the
subscription schedule phase item doesn’t have a Stripe ID, so you can’t add a
Stripe ID custom field to the Salesforce order line. However, you can still
configure the object in the data mapper.

The connector automatically maps the following objects:

Salesforce objectStripe
objectAccount[Customer](https://docs.stripe.com/api/customers/object)Order[Subscription
Schedule](https://docs.stripe.com/api/subscription_schedules/object) and
[Subscription](https://docs.stripe.com/api/subscriptions/object)OrderItem[Subscription
Item](https://docs.stripe.com/api/subscription_items/object)Product2[Product](https://docs.stripe.com/api/products/object)PricebookEntry[Price](https://docs.stripe.com/api/prices/object)
## Custom mappings

You can create a custom mapping based on the standard and custom fields you use
in Salesforce.

#### Examples

- You use a custom field to identify if a pricebook entry is metered or
licensed. You can map that custom field to
[recurring.usage_type](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
on the Stripe `Price` object.
- You use a custom field for the tax ID number on a Salesforce account. You can
map that custom field to the corresponding field in Stripe.
- You want to identify all customers in your Stripe account that the connector
created. You can add a custom metadata field called `Source` with a default
value of `Salesforce` for the Stripe `Customer` object.

If there’s a one-to-one relationship to map between the object and object type,
you can use the path to a Salesforce field as the mapping source. For example,
you can map a custom field from the account of a Salesforce order to a custom
metadata field on a Stripe subscription schedule. However, if an account has
multiple orders, you can’t create a mapping between the Salesforce account and
an order field.

## See also

- [Accounts and
contacts](https://docs.stripe.com/connectors/salesforce-cpq/accounts-contacts)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)
- [Error
handling](https://docs.stripe.com/connectors/salesforce-cpq/error-handling)

## Links

- [Customer](https://docs.stripe.com/api/customers/object)
- [Subscription
Schedule](https://docs.stripe.com/api/subscription_schedules/object)
- [Subscription](https://docs.stripe.com/api/subscriptions/object)
- [Subscription Item](https://docs.stripe.com/api/subscription_items/object)
- [Product](https://docs.stripe.com/api/products/object)
- [Price](https://docs.stripe.com/api/prices/object)
-
[recurring.usage_type](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
- [Accounts and
contacts](https://docs.stripe.com/connectors/salesforce-cpq/accounts-contacts)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)
- [Error
handling](https://docs.stripe.com/connectors/salesforce-cpq/error-handling)