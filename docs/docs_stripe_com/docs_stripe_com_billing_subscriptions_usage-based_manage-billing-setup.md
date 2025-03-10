# Manage your usage-based billing setup

## Learn how to handle billing-related tasks for your usage-based billing model.

After you create your usage-based billing model, you can modify different parts
of your billing setup. For example, you can update a subscription item’s price
during a billing cycle, backdate a subscription to include usage in the next
invoice, or cancel usage-based subscriptions.

## Update prices mid-cycle

You can update a subscription item’s price during a billing cycle. However,
limitations apply when switching from one [meter
price](https://docs.stripe.com/api/prices/object#price_object-recurring-meter)
to another.

On future invoices, we reflect only usage that occurs after the update. For
example, say you have a monthly subscription that you switch from price A to
price B on January 16. At the end of the month, the invoice includes usage from
January 16 to January 31 at price B. Usage from January 1 to January 16 isn’t
billed.

An exception exists if you use [billing
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds)
and have a threshold invoice already generated at the old price. For example,
say you generate a threshold invoice on January 10 using price A. That threshold
invoice is still charged to the customer. At the end of the month, the invoice
includes usage from January 16 to January 31 at price B. The earlier threshold
invoice doesn’t offset any usage for this end-of-month invoice.

Similar restrictions apply if you add a new subscription item with a billing
meter price in the middle of the subscription cycle. For example, say you add a
new subscription item with price C on January 16. At the end of the month, the
invoice includes usage from January 16 to January 31 at price C for that
subscription item.

To update the price for a subscription item:

```
curl https://api.stripe.com/v1/subscription_items/{{SUBSCRIPTION_ITEM_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d price={{NEW_PRICE_ID}}
```

To delete a subscription item:

```
curl -X DELETE
https://api.stripe.com/v1/subscription_items/{{SUBSCRIPTION_ITEM_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

After deletion, the invoice doesn’t reflect any usage from that item.

## Create a backdated subscription

You can record usage for a customer even before creating a subscription for
them. After recording usage for a customer, use the
[backdate_start_date](https://docs.stripe.com/api/subscriptions/create#create_subscription-backdate_start_date)
to create a subscription before the first report. This allows you to include
usage in the next subscription invoice.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d backdate_start_date=1710000000
```

## Cancel usage-based subscriptions

With usage-based billing, the bill the customer pays varies based on consumption
during the billing cycle. When changing the billing cycle results in a
subscription interval ending early, you charge the customer for the usage
accrued during the shortened billing cycle.

#### Note

We don’t support
[proration](https://docs.stripe.com/billing/subscriptions/prorations) with
usage-based billing.

You can’t reactivate canceled subscriptions. Instead, you can collect updated
billing information from your customer, update their default payment method, and
create a new subscription with their existing customer record.

If you use
[cancel_at_period_end](https://docs.stripe.com/api/subscriptions/update#update_subscription-cancel_at_period_end)
to schedule the cancellation of a subscription, you can reactivate the
subscription at any time up to the end of the period. To do so, update
`cancel_at_period_end` to `false`.

For subscriptions that cancel at period end, the final end of cycle invoice
includes metered usage for the last billing cycle. In this case Stripe also
disables the automatic collection of the end of cycle invoice and sets
[auto_advance](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)
to `false`. You can resume automatic collection of the invoices manually by
setting `auto_advance` to `true`.

## Links

- [meter
price](https://docs.stripe.com/api/prices/object#price_object-recurring-meter)
- [billing
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds)
-
[backdate_start_date](https://docs.stripe.com/api/subscriptions/create#create_subscription-backdate_start_date)
- [proration](https://docs.stripe.com/billing/subscriptions/prorations)
-
[cancel_at_period_end](https://docs.stripe.com/api/subscriptions/update#update_subscription-cancel_at_period_end)
-
[auto_advance](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)