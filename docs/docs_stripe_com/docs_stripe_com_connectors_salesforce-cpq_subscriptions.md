# Subscription orders

## Learn about syncing your subscription orders between Salesforce and Stripe.

The Stripe Billing Connector for Salesforce CPQ creates a subscription schedule
in Stripe for every activated order in Salesforce that has a subscription type.
In a Salesforce order, each order line creates a subscription item (for a
recurring product) or an invoice item in Stripe. Order lines can’t be split into
multiple line items in Stripe.

By default, each subscription schedule in Stripe doesn’t automatically renew. To
renew a subscription, do either of the following:

- Create an order amendment with a new subscription start date and term.
- Configure your integration to auto-renew all subscriptions.

#### Note

The “native” quote object–distinct from the `CPQ Quote` object–in Salesforce
isn’t used. The connector uses orders generated from the `CPQ Quote` object.

## Determine which orders to sync

The connector checks Salesforce every 90 seconds for updated orders since the
last successful order sync.

The connector attempts to sync all orders that meet the following conditions:

- The order status is activated. You can remove or customize this default
condition.
- The order type is new.
- At least one of the order lines is a subscription product. This means it’s set
to `SBQQ_SubscriptionType_c`.

If all order lines are one-time purchase items, the connector creates a one-time
invoice instead of a subscription.

### Order dates

When you set up the connector, you can choose a backfill date for orders. Only
orders created after this date sync to Stripe.

You can backdate subscription start dates, which is the order start date used in
Stripe. To prevent errors when activating the order, you must provide a start
date on the quote and related order.

You can optionally provide a trial end date. If you don’t set a trial date, the
customer won’t receive a trial period.

### Order sync conditions

You can add custom conditions to the default sync conditions. These conditions
are described using standard SOQL syntax.

To add custom conditions or remove default conditions, navigate to **Stripe
Billing Setup** > **Sync Preferences** > **Custom Order Sync Conditions**.

### Limitations

The connector can’t sync orders with more than 100 recurring line items. An
error appears in Salesforce if an order has more than 100 recurring lines.

You must specify quantities as an integer in Salesforce. Stripe doesn’t allow
decimal quantities. An error appears in Salesforce if an order has a decimal
quantity.

All line items in an order must have the same interval count and interval type.
The interval count maps from `Billing Frequency`, by default. The interval type
is daily or monthly. Stripe doesn’t allow different billing frequencies in the
same order, which means you can’t have one line item billed every other month
and another line item billed every month.

### Exclude line items

By default, all line items (including zeroed line items) sync from Salesforce to
Stripe. You can exclude certain line items from the subscription schedule that’s
created in Stripe. For example, you can exclude line items that are for
informational purposes only that you don’t want to display on the recurring
invoice in Stripe.

To exclude line items, set `Skip Line Item in Stripe` on the order item to
`true`.

When this field is set to `true`, the connector skips the order item and
excludes it from the line items of the subscription schedule phase in Stripe.
The internal field name is `Skip_Line_Item__c` (not excluding the package
prefix).

## Subscription schedule mapping

An activated order in Salesforce creates a subscription schedule in Stripe. The
fields map as follows.

Salesforce order fieldStripe subscription schedule fieldNotesRequiredQuote,
Start date (`SBQQ_StartDate_c`)[Start
date](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-start_date)Quote,
Subscription term[Phases,
Iterations](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-iterations)[End
behavior](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-end_behavior)The
default value is `cancel`. If you want the subscription to auto-renew, you can
configure this mapping in the data mapper.Payment term
(`SBQQ_PaymentTerm_c`)Default settings, Invoice_settings, [Days until
due](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings-invoice_settings-days_until_due)
## Line item mapping

Each line item of an activated order in Salesforce maps as follows. These fields
are required.

If the unit price for an order item is different from the pricebook unit price,
the connector uses the order item price and creates a new Stripe price.

Salesforce field (OrderItem object)Stripe line item fieldNotesPricebook Entry,
UnitPrice[Price](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-price)The
Stripe price contains the exact unit amount specified on the pricebook item. If
you use a custom field to represent the recurring price billed to the customer,
you can configure this mapping.OrderItem,
UnitPrice[Price](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-price)The
Stripe price contains the exact unit amount specified on the order line item. If
you use a custom field to represent the recurring price billed to the customer,
you can configure this mapping.Quantity
(`OrderItem.SBQQ_OrderedQuantity_c`)[Quantity](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-quantity)You
must specify the quantity as an integer; otherwise, the quantity is forced to
`1` and the price adjusts to represent the net amount of the line item cost. If
the billing type is `arrears` (metered billing), the quantity isn’t set on the
line item. Instead, you must report the quantity to Stripe before the end of the
customer’s billing period.
## Subscription changes

You can’t update an activated order in Salesforce, and any changes you make to
an order in Salesforce won’t sync to Stripe. To adjust or partially cancel a
subscription mid-cycle, you can use an [order
amendment](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments).

By default, subscription schedules won’t automatically renew. To update the
renewal information, create an [order
amendment](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
that’s associated with the original contract.

You can also customize this functionality to auto-renew by default, or manage
the renew logic directly in Stripe.

## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Evergreen
orders](https://docs.stripe.com/connectors/salesforce-cpq/evergreen-orders)

## Links

- [Start
date](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-start_date)
- [Phases,
Iterations](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-iterations)
- [End
behavior](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-end_behavior)
- [Days until
due](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings-invoice_settings-days_until_due)
-
[Price](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-price)
-
[Quantity](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-quantity)
- [order
amendment](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Evergreen
orders](https://docs.stripe.com/connectors/salesforce-cpq/evergreen-orders)