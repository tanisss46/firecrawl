# Evergreen subscription orders

## Learn how to sync your evergreen subscription orders between Salesforce and Stripe.

The Stripe Billing Connector for Salesforce CPQ supports syncing your evergreen
orders to Stripe subscriptions. Evergreen orders are subscriptions in Salesforce
that have no end date, as opposed to renewable orders, which are recurring
subscriptions that have a set end date.

The connector examines `SBQQ_SubscriptionType__c` to determine if an order is
Renewable or Evergreen. A Salesforce order with an `Evergreen` subscription type
syncs into a Stripe subscription, regardless of the value for
`SBQQ_ProductSubscriptionType__c`, which could be Renewable, or Renewable and
Evergreen.

## Requirements

Set the `collection_method` field to `send_invoice` and specify a value for
`days_until_due` on the Stripe subscription. You can map to these fields in the
data mapper.

Set `SBQQ_DefaultSubscriptionTerm__c` on the Salesforce evergreen order to `1`.
To prevent unexpected behavior on the invoices, make sure the evergreen order
has a default subscription term equal to 1.

## Cancel evergreen orders

You can cancel evergreen orders in Salesforce by making an order amendment with
quantity zero and setting the cancellation date as the start date.

To cancel a Stripe subscription immediately, set the amendment start date to the
current date. To cancel a Stripe subscription on a specific date, set the
amendment start date to a date in the future.

If you cancel a subscription during a billing period, the subscription cancels
immediately and the customer won’t receive a credit or refund for the remainder
of the billing period.

## Limitations

The connector doesn’t sync Salesforce orders that contain both evergreen and
non-evergreen products.

The connector only supports canceling Salesforce evergreen orders with one
product. Attempting to cancel a subset of the products in an evergreen order
cancels the entire Stripe subscription. We recommend creating separate
Salesforce evergreen orders for each product, if you want the ability to cancel
orders in Stripe.

You must set the `collection_method` on a Stripe subscription to `send_invoice`.
The default value is `charge_automatically`, but the connector doesn’t support
collecting customer payment methods, which is necessary to charge automatically.

## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)

## Links

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)