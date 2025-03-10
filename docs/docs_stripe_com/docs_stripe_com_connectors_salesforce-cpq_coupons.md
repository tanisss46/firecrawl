# Sync Stripe coupons

## Learn how to sync Stripe coupons between Salesforce and Stripe.

The Stripe Billing Connector for Salesforce CPQ enables you to add configurable,
stackable coupons to your Stripe subscriptions and subscription items synced
from Salesforce. For example, you can offer your customers a one-time discount
of 10% off or 50 USD off for the first 3 months of their subscription.

## Assign permission sets

For coupons to work properly, you must assign the Salesforce user who adds and
syncs orders to the Stripe Connector Coupon User permission set. To add a user
to the permission set, they must have a Salesforce CPQ license.

## Add a coupon to a Salesforce order or order item

The connector exposes the following custom Salesforce objects that you can use
together to add discounts to your Stripe subscriptions:

Salesforce objectDescriptionQuote Stripe CouponA Salesforce object representing
a Stripe coupon. The `Quote Stripe Coupon` has a one-to-one field mapping with
the [Stripe
Coupon](https://docs.stripe.com/billing/subscriptions/coupons#coupons).Quote
Stripe Coupon AssociationA Salesforce junction object used to correlate a `Quote
Stripe Coupon` to a `Quote`.Quote Line Stripe Coupon AssociationA Salesforce
junction object used to correlate a `Quote Stripe Coupon` to a `Quote Line`.
When a Salesforce order activates, the connector:

- Identifies any `Quote Stripe Coupon` objects corresponding to the Salesforce
order or order line
- Serializes the `Quote Stripe Coupon` onto the corresponding Salesforce order
or order line
- Creates (or re-uses where possible) a Stripe coupon for each Salesforce coupon
- Applies the coupons to the corresponding subscription or subscription item
created in Stripe

## Reuse Stripe coupons

The connector reuses existing Stripe coupons if multiple orders or order items
reuse the corresponding Salesforce coupon. Modifying the original Salesforce
coupon creates a new Stripe coupon.

## Custom mappings for coupons

Similar to other native Salesforce objects, you can use the data mapper to map
the `Quote Stripe Coupon`. By default, the `Quote Stripe Coupon` is a one-to-one
field mapping to the `Stripe Coupon`. You can also add custom metadata to the
`Quote Stripe Coupon`.

## Custom Apex triggers

The connector uses custom Apex triggers to serialize the
`Quote_Stripe_Coupon__c` on the Salesforce order `after update`. If you have
custom workflows that modify the `Quote_Stripe_Coupon__c`, make sure the trigger
occurs `before update` to avoid race conditions between the workflows.

## Multi-currency support

If you enabled
[multi-currency](https://help.salesforce.com/s/articleView?id=sf.admin_enable_multicurrency.htm&type=5)
and you specify an amount off for the coupon, the connector maps the
`CurrencyIsoCode` on the `Quote Stripe Coupon` to the equivalent [Stripe
currency](https://docs.stripe.com/currencies) during Stripe coupon creation.

## See also

- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)

## Links

- [Stripe Coupon](https://docs.stripe.com/billing/subscriptions/coupons#coupons)
-
[multi-currency](https://help.salesforce.com/s/articleView?id=sf.admin_enable_multicurrency.htm&type=5)
- [Stripe currency](https://docs.stripe.com/currencies)
- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)