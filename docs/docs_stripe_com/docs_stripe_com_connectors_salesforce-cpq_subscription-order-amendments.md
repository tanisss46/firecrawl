# Subscription order amendments

## Learn about creating order amendments for your subscription orders.

The Stripe Billing Connector for Salesforce CPQ creates a subscription schedule
in Stripe for every Salesforce order that’s synced with a subscription type. To
modify an existing order, you create an order amendment. An order amendment in
Salesforce results in a new subscription schedule phase on an existing
subscription schedule in Stripe.

Depending on your use case, you might need to create one of the following
amendment types:

- [Insertion
order](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments#insertion-order)
- [Termination
order](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments#termination-order)
- [Prorated
order](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments#prorated-order)

## Insertion order amendments

To adjust or partially cancel an activated order mid-cycle, you use an insertion
order amendment. The connector updates the subscription schedule in Stripe with
the new products and quantity of the order amendment in Salesforce. The
connector uses the same mapping as the initial order integration.

### Start and end dates

Order amendments can’t have gaps between the start and end dates. To prevent any
errors, the start date of the order amendment must be:

- On or before the end date of the previous order or order amendment, or
- The same start date as the previous initial order or order amendment

All order amendments must co-terminate with the initial order. The Salesforce
CPQ uses the start date of a contract combined with the subscription term to
calculate the end date. This means that all order amendments must have the same
end date (start date and subscription term).

### Order deltas

An order amendment includes only the delta from the previous order. The
connector pulls all previous orders and aggregates all previous line items to
determine what subscription items to include in the new subscription schedule
phase. Stripe doesn’t reuse or connect the items from one phase of a
subscription to items from a previous phase.

### Order contracts

To modify a subscription in Stripe, you must connect an order and order
amendment to the same contract. The Salesforce CPQ does this automatically for
each order and order amendment that’s contracted.

We recommend contracting from the order in the Salesforce CPQ. Stripe doesn’t
have a direct representation of the Salesforce `Contract` object.

### Item prices

Unless the order item price changes, Stripe uses the same `Price` object across
subscription schedule phases.

## Revise and terminate order lines

When you partially or fully terminate a previous order line, this action creates
a negative-quantity order line in Salesforce. Stripe doesn’t allow negative line
items. If an order amendment removes a product or some quantity of a product
from a subscription, the negative-quantity order lines aggregate with the
previous order lines that they revise.

For example, an initial order has a line item with a quantity of 2. The order
amendment decreases the quantity by 1. As a result, the new subscription
schedule phase in Stripe has a single subscription item with a quantity of 1.

For positive-quantity order lines, the connector creates a unique subscription
schedule phase item in Stripe.

All order items that modify an order line in a previous order amendment must
exist on the previous subscription phase. In other words, if you skip a line
item on an order, you must skip that line item on the order amendment if you
revise the line item.

## Multiple order lines with the same product and price

Stripe doesn’t allow multiple subscription schedule phase items with the same
price ID. Salesforce doesn’t have this limitation.

If you use the same price on multiple order lines, the connector does the
following:

- Duplicates the price in Stripe
- Adds the price to the subscription schedule phase
- Archives the price after it’s used (`active = false`)

The duplicated prices in Stripe contain the following metadata:

- `salesforce_duplicate = true`—Indicates that the price is a duplicate of
another price
- `salesforce_auto_archive = true`—Auto-archives the price after use
- `salesforce_original_stripe_price_id = price_xyz`—Includes the ID of the price
used for the duplicated price

## Mid-month amendments

The connector requires that all order amendments co-terminate with the initial
order. If the amendment order starts on a different day of the month than the
initial order, you must:

- Set the end date on the amendment order.
- Set the subscription term to the number of whole months in the amendment
order.

Example of a mid-month order amendment:

Initial orderOrder amendmentStart dateJanuary 1, 2022February 15, 2022End
dateDecember 31, 2022December 31, 2022Subscription term1210
## Backdated amendments

The connector processes backdated amendments in current time. A backdated order
amendment starts in the past, which means the latest phase on the subscription
schedule won’t align with the start date on the order amendment.

For example, a customer wants to amend an existing subscription, and pushes the
amendment order through the connector at a later date than its effective date.

## Same-day amendments

The connector can process same-day amendments, such as the following scenarios:

- A subscription starts today, and the customer wants to amend their contract on
the same day that it started.
- A subscription starts on a future date, and the customer wants to amend the
order with a start and end date that’s the same as the original order.

### Same-day amendments with an existing subscription

In this case, the connector treats the amendment as a prorated order amendment,
with some differences:

- The end date of the previous phase uses a special `now` value, instead of
midnight on the current day (which, in this example, already passed).
- The start date of the next phase (for example, the order amendment) uses a
`now` value as well.
- The amounts of the prorated line items are equal to the full billing amount
for the duration of the contract.

### Same-day future amendments

If a subscription hasn’t started, you can’t use the special `now` value in the
same-day amendment when the subscription starts. In this case, the connector
does the following:

- Collects any one-time line items from the order (initial or amendment) that
shares the same order period (for example, the start and end dates)
- Adds these items to the new phase
- Removes the phase that represents the previous order

Stripe completely removes the subscription schedule phase metadata that’s
associated with the previous order.

## Insertion order amendment example

Here’s an example order amendment and how it maps to Stripe Billing.

**Initial order**—The initial order combines the customer and subscription
schedule into a single subscription phase in Stripe.

**Order amendment**—On January 15, 2022, you create an order amendment in
Salesforce for the initial order.

The initial order and order amendment have the following values:

Initial orderOrder amendmentStart dateJanuary 1, 2022February 1,
2022Subscription term1211
**Line items**

One

Product A

- Quantity: 10
- Unit price: 10 USD
- Billing term: Monthly

Two

Product A

- Quantity: 6
- Unit price: 10 USD

Product B

- Quantity: 5
- Unit price: 20 USD

In the Salesforce CPQ, the order amendment represents Product A as an order line
with quantity -4 (decrease of quantity 4). Because the unit price is the same,
Stripe uses the same `Price` object on the subscription schedule phase item.

After the order amendment activates, the subscription schedule updates to
contain the following phases:

Phase 1Phase 2Start dateJanuary 1, 2022February 1, 2022End dateFebruary 1,
2022February 1, 2023ItemsProduct A, Quantity: 10- Product A, Quantity: 6, Same
price
- Product B, Quantity: 5

## Termination order amendments

To fully cancel a contract, you use a termination order amendment. The order
amendment sets the quantity of all line items on the order to 0.

When this happens, the connector updates the end date of the last subscription
schedule phase to the start date of the termination order amendment.

To fully terminate an order on the same day it starts, you
[cancel](https://docs.stripe.com/api/subscription_schedules/cancel) the
subscription schedule instead of modifying the previous phase.

## Prorated order amendments

A prorated order amendment has a start date that falls outside a billing cycle
boundary, and an end date that isn’t equal to the billing frequency.

For example, an order lasts 1.5 years starting on month 6 that amends a 2-year
contract, billed yearly. That order is a prorated order amendment. You bill the
customer a prorated amount on the start date of the amendment for the portion of
the order that doesn’t fall within the standard billing cycle.

When you create a prorated order amendment in Salesforce, the connector does the
following in Stripe for each order line to prorate:

- Creates a new price object to represent the prorated amount
- Adds an invoice item with the newly created price to the newly created phase
to represent the prorated amount
- Updates the subscription item’s quantity to incorporate the amendment at the
time it goes into effect, without billing for anything more than the prorated
amount

Stripe Billing sends an invoice for the full product amount and quantity at the
end of the billing cycle. In the example above, the billing cycle ends on month
12 and the invoice is for 120 USD x 2 = 240 USD.

You can’t prorate the following prices:

- Prices configured for metered billing—The amount due calculates after the end
of the billing cycle.
- One-time, non-recurring prices—These bill immediately and don’t have a billing
cycle associated with them.
- Tiered prices created from consumption schedules.

## Prorated order amendment example

Here’s an example order amendment and how it’s represented in Stripe.

Phase 0Phase 1 at 6 monthsPhase 1 at 12 months- Duration: 0 to 6 months
- Subscription items: Quantity: 1
- Quantity: 1
- Duration: 6 to 24 months
- Subscription items: Product A, Quantity: 2
- Phase `proration_behavior` is set to none
- Invoice items: Single item to represent that the 6-month prorated cost of the
product is added to the phase
A third phase isn’t created. At month 12 of phase 1, a new invoice is created
for the subscription item added in phase 1 at 6 months.
A single proration item in Stripe represents the prorated amount of the order
item. This means a debit for the prorated time through the remainder of the
billing cycle.

The Stripe Billing proration calculation creates two proration items:

- A credit for unused time on the old plan
- A debit for the prorated used time through the rest of the billing period

You won’t see the credit line item in Stripe when using the proration data that
the Salesforce CPQ calculates.

## Use CPQ-calculated prorations

When billing information exists in CPQ, the connector treats it as the source of
truth. This allows other financial systems (such as Stripe) and financial
reporting tools (such as NetSuite or QuickBooks) to reconcile proration and
other financial data. By default, the connector uses `CPQ Subscription Prorate
Precision` equal to `Month` to calculate proration. The connector also supports
`CPQ Subscription Prorate Precision` equal to `Monthly and Daily`.

In some cases, amounts won’t match between Stripe and Salesforce because only
Stripe does some calculations, and they don’t exist in CPQ. For example, data
for taxes and metered billing only exist in Stripe.

## Calculate prorated prices

In Salesforce, a prorated line item contains the following information:

- Subscription term
- Unit amount (mapped to `unit_decimal_amount` in Stripe)
- Quantity
- Billing frequency (mapped to `recurring.interval` and
`recurring.interval_count` in Stripe)
- Start date

### Salesforce CPQ Month prorate precision

To determine what portion of the order item to prorate when `CPQ Subscription
Prorate Precision` is set to `Month`:

- Calculate the months (terms) of the subscription that aren’t included in the
billing cycle. Use the start date, subscription term, and billing frequency of
the line item to determine this value.
- Calculate the per-month cost of the line item. Divide the value that’s mapped
to `unit_amount_decimal` by the subscription term.
- Multiply the per-month cost (value from step 2) by the number of months that
aren’t included in the billing cycle (value from step 1).

For example, a subscription has six months that aren’t included in the billing
cycle. The per-month cost of the line item is 10 USD, which is calculated by
dividing a 180 USD unit amount by an 18-month subscription term. Multiplying the
per-month cost of 10 USD by six months results in 60 USD.

### Salesforce CPQ Monthly and Daily prorate precision

To determine what portion of the order item to prorate when `CPQ Subscription
Prorate Precision` is set to `Monthly and Daily`:

- Calculate the partial month (at the end of the term) of the subscription that
isn’t included in the billing cycle. The partial month equals the number of days
not included in the billing cycle.
- Calculate the per-day cost of the line item. Divide the value that’s mapped to
`unit_amount_decimal` by the number of days in a month. CPQ calculates the
number of days in a month by dividing the number of days in a year by the number
of months in a year (365 divided by 12).
- Multiply the per-day cost (value from step 2) by the number of days that
aren’t included in the billing cycle (value from step 1).

The connector calculates prorations based on the setting for `CPQ Subscription
Prorate Precision`.

## Calculate prorated prices with customized price fields

Typically, `UnitPrice` maps to `unit_price_decimal` in Stripe. You can also use
a custom field for the price. The connector assumes the custom field you specify
is the price of the product for the entire billing cycle.

For example, you specify a custom price field of 120 USD, rather than using the
180 USD value for the `UnitPrice`. For a quarterly billing cycle, the cost per
quarter is 30 USD, which is 120 USD divided by four quarters.

For a prorated order line, the connector expects the full amount of the billing
cycle for the custom price field. The connector calculates the prorated amount
from this value.

## Represent prorations with unique prices

A unique aspect of this approach is generating a Stripe `Price` object to
represent the prorated amount. Each prorated amount creates a `Price` object in
Stripe tied to the same product as the original fully billed price. In other
words, two distinct `Price` objects are created to represent the proration line
item and the non-prorated subscription line item.

The metadata of the `Price` object indicates they were created for this purpose:
`salesforce_proration => true`

These prices are automatically archived (`active=false`) after use in a
subscription.

## How prorated invoice items are billed

When the phase representing the prorated order amendment starts, a pending
invoice item is added to the customer’s subscription.

The connector listens for newly created invoice items to determine if they
represent prorated amounts. If they do, the connector creates and finalizes an
invoice for the subscription. The invoice bills the customer for the prorated
amount of their subscription.

You can’t specify which items in a subscription to bill—the subscription bills
any pending invoice items attached to it.

## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)
- [Evergreen
orders](https://docs.stripe.com/connectors/salesforce-cpq/evergreen-orders)

## Links

- [Insertion
order](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments#insertion-order)
- [Termination
order](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments#termination-order)
- [Prorated
order](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments#prorated-order)
- [cancel](https://docs.stripe.com/api/subscription_schedules/cancel)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)
- [Evergreen
orders](https://docs.stripe.com/connectors/salesforce-cpq/evergreen-orders)