# Multi-dimensional quoting (MDQ) products

## Learn about syncing MDQ products between Salesforce and Stripe.

The Stripe Billing Connector for Salesforce CPQ enables you to create, manage,
and bill for deals with annual price or quantity adjustments. Ramp deals can
span a single year or multiple years, and are single subscriptions segmented
into blocks of time. This provides sales representatives with detailed control
over pricing specific units of time within a subscription.

## Create MDQ products

Create a multi-dimensional quoting (MDQ) product in Salesforce by adding a price
dimension to the Price Dimensions related list for your product. The type
determines how your segments appear: by year, quarter, or month. You can also
allow users to edit a segment’s cost, quantity, or discounts. The connector
doesn’t support MDQ products with custom segments.

Using the connector to sync a Salesforce order with an MDQ product results in a
Stripe subscription schedule with a subscription schedule phase for each ramp.
For example, a 3-year contract segmented by year results in a Stripe
subscription schedule with three phases, one for each ramp year. Each phase has
the `salesforce_segment_index` and `salesforce_segment_label` metadata so that
you know which ramp the phase corresponds to.

## Amend MDQ products

MDQ ramps or segments produce multiple quote lines, one for each segment. When
amending an original Salesforce order with MDQ products, the connector supports
the following:

- Terminating the entire Salesforce order
- Adjusting the quantity of a Salesforce product in one or all of the ramps on
the Salesforce order
- Adding a standard product to the Salesforce order
- Removing a standard product from the Salesforce order

When amending an original Salesforce order with an MDQ product, you must set the
`SBQQ__AmendmentStartDate__c` field on the contract equal to the
`SBQQ__StartDate__c` field on the amendment quote. Otherwise, you can create and
sync an [order
amendment](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
as usual.

## Limitations

Consider the following MDQ limitations:

- You can have one ramp schedule per Salesforce order.
- You can sync products with the same billing frequencies across each ramp.
- Ramps must be consecutive time periods.
- You can only amend current and future segments of an MDQ subscription. Past
segments aren’t available.
- Don’t amend the ramp period. For example, you can’t change the ramp deal from
yearly to monthly.
- Don’t shorten a ramp deal. To terminate an order, you must cancel the line
items across all segments.

## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)

## Links

- [order
amendment](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)