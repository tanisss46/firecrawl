# Prorations

## Manage prorations for modified subscriptions.

The most complex aspect of changing existing subscriptions are prorations, where
the customer is charged a percentage of a subscription’s cost to reflect partial
use. This page explains how prorations work with subscriptions and how to manage
prorations for your customers.

## How prorations work

For example, [upgrading or
downgrading](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade) a
subscription can result in prorated charges. If a customer upgrades from a 10
USD per month plan to a 20 USD option, they’re charged prorated amounts for the
time spent on each option. Assuming the change occurred halfway through the
billing period, the customer is billed an additional 5 USD: -5 USD for unused
time on the initial price, and 10 USD for the remaining time on the new price.

Proration ensures that customers are billed accurately, but a proration can
result in different payment amounts than you might expect. Negative prorations
aren’t automatically refunded and positive prorations aren’t immediately billed,
although you can do both manually.

You can [preview a
proration](https://docs.stripe.com/billing/subscriptions/prorations#preview-proration)
to view the amount before applying the changes.

### Prorations and discounts

Any adjustments from
[discounts](https://docs.stripe.com/billing/subscriptions/coupons) are reflected
in the proration invoice item’s
[amount](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-amount).
Additional discounts at the [invoice item
level](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-discounts)
or [invoice line item
level](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-discounts)
don’t apply to prorations because they have `discountable=false`.

This behavior is different from non-prorations, which show discount adjustments
in
[discount_amounts](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-discount_amounts).

### What triggers prorations

By default, the following scenarios result in a proration:

- Changing to a price with a different base cost
- Changing to a price with a different billing interval
- Adding a trial period to an active subscription
- Changing the quantity
- [Licensed](https://docs.stripe.com/billing/subscriptions/quantities)
(per-seat) subscriptions (because they’re billed at the start of each billing
period)

### Manually creating your own prorations

To calculate your own prorations outside of Stripe and add them to the
subscription, pass
[add_invoice_items](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-add_invoice_items)
with negative `unit_amount`s (equal to the calculated proration amount) to these
endpoints:

- [CreateSubscription](https://docs.stripe.com/api/subscriptions/create)
- [UpdateSubscription](https://docs.stripe.com/api/subscriptions/update)
-
[CreateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/create)
-
[UpdateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/update)

### When prorations are applied

Prorations only apply to charges that occur ahead of the billing cycle.
[Usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based)
isn’t subject to proration.

The prorated amount is calculated as soon as the API updates the subscription.
The current billing period’s start and end times are used to calculate the cost
of the subscription before and after the change.

### Taxes and prorations

For information about how taxes work with prorations, see [Collect taxes for
recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes).

## Preview a proration

You can [retrieve an upcoming
invoice](https://docs.stripe.com/api#upcoming_invoice) to preview changes to a
subscription. This API call doesn’t modify the subscription, it returns the
upcoming [invoice](https://docs.stripe.com/api/invoices) based only on the
parameters that you pass. Changing the `price` or `quantity` both result in a
proration. This example changes the `price` and sets a date for the proration.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# Set proration date to this moment:
proration_date = Time.now.to_i

subscription = Stripe::Subscription.retrieve('sub_49ty4767H20z6a')

# See what the next invoice would look like with a price switch
# and proration set:
items = [{
 id: subscription.items.data[0].id,
 price: 'price_CBb6IXqvTLXp3f', # Switch to new price
}]

invoice = Stripe::Invoice.upcoming({
 customer: 'cus_4fdAW5ftNQow1a',
 subscription: 'sub_49ty4767H20z6a',
 subscription_items: items,
 subscription_proration_date: proration_date,
})
```

You can expand the example response below to see:

- The credit for unused time at the previous price on lines 36-38.
- The cost for time spent at the new price on lines 107-109.
- The new subtotal and total for the invoice on lines 276-279.

```
{
 "account_country": "US",
 "account_name": "Test account",
 "amount_due": 3627,
 "amount_paid": 0,
 "amount_remaining": 3627,
 "application_fee_amount": null,
 "attempt_count": 0,
 "attempted": false,
 "billing_reason": "upcoming",
```

See all 284 lines
Use this information to confirm the changes with the customer before modifying
the subscription. Because Stripe prorates to the second, prorated amounts might
change between the time they’re previewed and the time the update is made. To
avoid this, pass in a `subscription_proration_date` to the invoice when you
preview a change. When you update the subscription, pass the same date using the
`proration_date` parameter on a subscription so that the proration is calculated
at the same time.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

subscription = Stripe::Subscription.update(
 'sub_49ty4767H20z6a',
 {
 items: [
 {
 id: subscription.items.data[0].id,
 price: 'price_CBb6IXqvTLXp3f',
 },
 ],
 proration_date: proration_date,
 }
)
```

## Control proration behavior

Prorating is controlled by the
[proration_behavior](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_behavior)
parameter, which has three possible parameter options: `create_prorations`,
`always_invoice`, and `none`.

### Default behavior

The default parameter for `proration_behavior` is `create_prorations`, which
creates proration invoice items when applicable. These proration items are only
invoiced immediately under [certain
conditions](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade#immediate-payment).

### Create immediate prorations

To bill a customer immediately for a change to a subscription on the same
billing cycle, set `proration_behavior` to `always_invoice` when you modify the
subscription. This calculates the proration, then immediately generates an
invoice.

### Disable prorations

To disable prorations on a per-request basis, set the `proration_behavior`
parameter to `none`. No parameter turns off all future prorations for a
subscription. To disable prorations indefinitely, set `proration_behavior` to
`none` for every request that generates prorations:

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "items[0][id]"="si_1AkFf6LlRB0eXbMtRFjYiJ0J" \
 -d "items[0][price]"="price_CBb6IXqvTLXp3f" \
 -d "proration_behavior"="none"
```

When prorations are disabled, customers are billed the full amount at the new
price when the next invoice is generated.

## Links

- [upgrading or
downgrading](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)
- [discounts](https://docs.stripe.com/billing/subscriptions/coupons)
-
[amount](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-amount)
- [invoice item
level](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-discounts)
- [invoice line item
level](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-discounts)
-
[discount_amounts](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-discount_amounts)
- [Licensed](https://docs.stripe.com/billing/subscriptions/quantities)
-
[add_invoice_items](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-add_invoice_items)
- [CreateSubscription](https://docs.stripe.com/api/subscriptions/create)
- [UpdateSubscription](https://docs.stripe.com/api/subscriptions/update)
-
[CreateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/create)
-
[UpdateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/update)
- [Usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)
- [Collect taxes for recurring
payments](https://docs.stripe.com/billing/taxes/collect-taxes)
- [retrieve an upcoming invoice](https://docs.stripe.com/api#upcoming_invoice)
- [invoice](https://docs.stripe.com/api/invoices)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[proration_behavior](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_behavior)
- [certain
conditions](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade#immediate-payment)