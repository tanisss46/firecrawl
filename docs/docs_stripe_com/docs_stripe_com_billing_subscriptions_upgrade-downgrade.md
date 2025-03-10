# Upgrade and downgrade subscriptions

## Learn how to upgrade and downgrade subscriptions by changing the price.

When a customer changes their subscription, you must change the subscription
item to reflect the new selection. For example, a customer might upgrade to a
premium tier or downgrade to a basic tier, prompting you to replace the
underlying price of that subscription item. You can do this using a few
different methods.

## Retrieve the identifiers

Regardless of the method you choose, you’ll need to provide identifiers for the
objects you’re updating. Use the [list
subscriptions](https://docs.stripe.com/api/subscriptions/list) method with a
relevant filter (such as the customer ID) to find the subscription and item to
update.

```
curl -G https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}}
```

The returns the set of subscriptions for the specified customer, from which you
can retrieve the subscription ID (`id`), any subscription item IDs
(`items.data.id`) and the subscription items price ID (`items.data.price.id`).

```
{
 "object": "list",
 "url": "/v1/subscriptions",
 "has_more": false,
 "data": [
 {
 "id": "su_1NXPiE2eZvKYlo2COk9fohqA",
 "object": "subscription",
 "application": null,
 "application_fee_percent": null,
 "automatic_tax": {
 "enabled": false
 },
 "items": {
 "object": "list",
 "data": [
 {
 "id": "si_OK3pbS1dvdQYJP",
 "object": "subscription_item",
 "billing_thresholds": null,
 "created": 1690208774,
 "metadata": {},
 "price": {
 "id": "price_1NOhvg2eZvKYlo2CqkpQDVRT",
 "object": "price"
 }
 }
 ]
 }
 }
 ]
}
```

## Update the subscription

[Update a subscription](https://docs.stripe.com/api#update_subscription)
including the following parameters:

- `item ID`: You must specify the subscription item to replace the current price
with the new price. Otherwise, updating the subscription with a new price *adds*
a new subscription item so both prices are active for the subscription.
- `item price`: Provide the identifier for the replacement price.
- `item quantity`: Updating a subscription price automatically reverts the
quantity to the default value of `1`. If the existing subscription quantity is
anything other than `1` and you want to preserve that value, you must include it
in the update.

```
curl https://api.stripe.com/v1/subscriptions/sub_xxxxxxxxx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "items[0][id]"={{SUB_ITEM_ID}} \
 -d "items[0][price]"={{NEW_PRICE_ID}}
```

#### Common mistake

You must specify the subscription item to replace the current price with the new
price. Failing to do so results in *adding* the new price so both prices are
active for the subscription.

Alternatively, you can delete the current subscription item and create a new
subscription item with the updated price.

```
curl https://api.stripe.com/v1/subscriptions/sub_xxxxxxxxx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "items[0][id]"={{SUB_ITEM_ID}} \
 -d "items[0][deleted]"=true \
 -d "items[1][price]"={{NEW_PRICE_ID}}
```

## Update the subscription item

[Update a subscription](https://docs.stripe.com/api/subscription_items/update)
using the following parameter:

- `item price`: Provide the identifier for the replacement price.
- `item quantity`: Updating a subscription price automatically reverts the
quantity to the default value of `1`. If the existing subscription quantity is
anything other than `1` and you want to preserve that value, you must include it
in the update.

Use this option if you don’t need to make any other changes at the subscription
level.

```
curl https://api.stripe.com/v1/subscription_items/si_xxxxxxxxx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d price={{NEW_PRICE_ID}}
```

## Billing periods

If both prices have the same billing periods (combination of `interval` and
`interval_count`), the subscription retains the same billing dates. If the
prices have different billing periods, the new price is billed at the new
interval, starting on the day of the change. For example, switching a customer
from one monthly subscription to another doesn’t change the billing dates.
However, switching a customer from a monthly subscription to a yearly
subscription moves the billing date to the date of the switch. Switching a
customer from one monthly subscription to another monthly subscription while
introducing a trial period also moves the billing date (to the conclusion of the
trial).

### Subscription schedules

If you’re changing a subscription at the end of its billing cycle, consider
using a [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases#changing-subscriptions)
to manage the transition. When using subscription schedules, be sure to follow
[best
practices](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-sub-updates)
to prevent unexpected subscription overwrites.

## Metered billing with Billing Meters

Details on mid-cycle updates for prices attached to a Billing Meter are
described in the [pricing
models](https://docs.stripe.com/billing/subscriptions/usage-based/manage-billing-setup#mid-cycle-updates)
section. Passing `clear_usage` when updating a price with a Billing Meter has no
effect.

## Metered billing with Usage Records Legacy

If you have a metered price backed by legacy usage records and update to a new
usage records price, the usage is transferred to the new price.

```
curl https://api.stripe.com/v1/subscriptions/sub_xxxxxxxxx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "items[0][id]"={{SUB_ITEM_ID}} \
 -d "items[0][price]"={{NEW_PRICE_ID}} \
 -d "items[0][clear_usage]"=true
```

## Proration

Changing a subscription often results in a
[proration](https://docs.stripe.com/billing/subscriptions/prorations) to apply
the new price to the remaining days in the billing period. You can prepare your
customer for any additional expense resulting from a price change by [previewing
a
proration](https://docs.stripe.com/billing/subscriptions/prorations#preview-proration).
Alternatively, you can [disable
prorations](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations).

### Immediate payment

Stripe immediately attempts payment for these subscription changes:

- From a subscription that doesn’t require payment (for example, due to a trial
or free subscription) to a paid subscription
- When the billing period changes

When billing is performed immediately, but the required payment fails, the
subscription change request succeeds and the subscription transitions to
`past_due`.

To bill a customer immediately for a change to a subscription on the same
billing cycle, set `proration_behavior` to `always_invoice`. This calculates the
proration, then immediately generates an
[invoice](https://docs.stripe.com/api/invoices) after making the switch. Combine
this setting with [pending
updates](https://docs.stripe.com/billing/subscriptions/pending-updates) so the
subscription doesn’t update unless payment succeeds on the new invoice.

### Credits for downgrades

When invoicing immediately for a downgrade, the customer might be owed a credit,
which is added to their credit balance to be applied to future invoices. To
refund your customer, issue [refunds](https://docs.stripe.com/refunds#issuing)
and then [adjust their account
balance](https://docs.stripe.com/billing/customer/balance#modifying) back to
zero. Learn more about customer refunds on our [dedicated support
page](https://support.stripe.com/questions/refunding-credit-balance-to-customer-after-subscription-downgrade-or-cancellation).

### Handling zero-amount prices and quantities

If you’ve subscribed a customer to a zero-amount price (for example, as a
trial), changing the price to a non-zero amount generates an invoice and resets
the [billing
period](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade#billing-periods)
to the date of the change.

If you’ve subscribed a customer to a price with a non-zero amount and a
zero-amount quantity, changing the quantity to a non-zero amount does not
generate an invoice or reset the billing period.

## See also

- [Billing cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [Canceling and pausing](https://docs.stripe.com/billing/subscriptions/cancel)
- [Update Subscription API](https://docs.stripe.com/api#update_subscription)

## Links

- [customer portal](https://docs.stripe.com/customer-management)
- [list subscriptions](https://docs.stripe.com/api/subscriptions/list)
- [Update a subscription](https://docs.stripe.com/api#update_subscription)
- [Update a subscription](https://docs.stripe.com/api/subscription_items/update)
- [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases#changing-subscriptions)
- [best
practices](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-sub-updates)
- [pricing
models](https://docs.stripe.com/billing/subscriptions/usage-based/manage-billing-setup#mid-cycle-updates)
- [proration](https://docs.stripe.com/billing/subscriptions/prorations)
- [previewing a
proration](https://docs.stripe.com/billing/subscriptions/prorations#preview-proration)
- [disable
prorations](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)
- [invoice](https://docs.stripe.com/api/invoices)
- [pending
updates](https://docs.stripe.com/billing/subscriptions/pending-updates)
- [refunds](https://docs.stripe.com/refunds#issuing)
- [adjust their account
balance](https://docs.stripe.com/billing/customer/balance#modifying)
- [dedicated support
page](https://support.stripe.com/questions/refunding-credit-balance-to-customer-after-subscription-downgrade-or-cancellation)
- [Billing cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [Canceling and pausing](https://docs.stripe.com/billing/subscriptions/cancel)