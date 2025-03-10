# Pending updates

## Learn how to handle payment failures when updating subscriptions.

Updating a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) generates
a new [invoice](https://docs.stripe.com/api/invoices) when:

- The subscription requires payment for the first time, such as the end of a
trial period.
- The billing period changes.
- Changing the subscription causes a proration and
`proration_behavior=always_invoice`.

By default, updates are applied regardless of whether payment on the new invoice
succeeds. If payment fails, rolling back the updates is a manual process. You
need to create a new invoice, prorate items on the invoice, and then initiate
payment again. However, with the pending updates feature, you can make changes
to subscriptions only if payment succeeds on the new invoice.

#### Caution

Pending updates aren’t supported when the subscription’s
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
is `send_invoice` or when bank debits are used as the payment method for the
subscription.

[Update the
subscriptionServer-side](https://docs.stripe.com/billing/subscriptions/pending-updates#update-subscription)
You can use pending updates with the [update
subscription](https://docs.stripe.com/api/subscriptions/update), [create
subscription item](https://docs.stripe.com/api/subscription_items/create), and
[update subscription
item](https://docs.stripe.com/api/subscription_items/update) calls. When you
make the update, set `payment_behavior=pending_if_incomplete`. The example below
adds a new price to a subscription. Because `proration_behavior=always_invoice`,
an invoice is created and payment is attempted when the update is made.

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_behavior"="pending_if_incomplete" \
 -d "proration_behavior"="always_invoice" \
 -d "items[0][id]"="si_09IkI4u3ZypJUk5onGUZpe8O" \
 -d "items[0][price]"="price_CBb6IXqvTLXp3f"
```

If payment succeeds, the subscription is updated. If payment fails, the
`Subscription` object that’s returned contains a `pending_update` hash with the
changes:

```
{
 "id": "sub_49ty4767H20z6a",
 "object": "subscription",
 "application_fee_percent": null,
 "pending_update": {
 "expires_at": 1571194285,
 "subscription_items": [
 {
 "id": "si_09IkI4u3ZypJUk5onGUZpe8O",
 "price": "price_CBb6IXqvTLXp3f"
 }
 ]
 },
}
```

[Handling failed
paymentsClient-side](https://docs.stripe.com/billing/subscriptions/pending-updates#handling-failed-payments)
After making the update, check the `pending_update` hash on the subscription. If
you want to be notified automatically, you can build a
[webhook](https://docs.stripe.com/webhooks) that listens for the
`customer.subscription.updated` event. If the `pending_update` hash is
populated, the payment failed and the subscription will continue to cycle as if
no update request was made.

Payments often fail because the payment method is declined or because they
require customer authentication. You should build logic to handle both of these
scenarios.

Use the instructions for [payment
failures](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
to handle card declines. You need to attach a new payment method to the customer
and then use the [pay](https://docs.stripe.com/api/invoices/pay) endpoint to pay
the invoice that the update generates.

Use the [customer
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action)
instructions to handle customer authentication. This walks the user through the
authentication process and then pays the invoice.

A successful payment:

- Immediately applies the changes in the `pending_update` hash.
- Updates the invoice to `paid`.

If payment fails again, the `pending_update` hash remains on the subscription
with the original [expiry
date](https://docs.stripe.com/billing/subscriptions/pending-updates-reference#expiration)
and no changes are applied.

[OptionalCanceling or changing pending
updatesServer-side](https://docs.stripe.com/billing/subscriptions/pending-updates#canceling-changing)
## See also

Details on the lifecycle, webhooks, and supported attributes when using pending
updates:

- [Pending updates
reference](https://docs.stripe.com/billing/subscriptions/pending-updates-reference)

## Links

- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [invoice](https://docs.stripe.com/api/invoices)
-
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
- [update subscription](https://docs.stripe.com/api/subscriptions/update)
- [create subscription
item](https://docs.stripe.com/api/subscription_items/create)
- [update subscription
item](https://docs.stripe.com/api/subscription_items/update)
- [webhook](https://docs.stripe.com/webhooks)
- [payment
failures](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
- [pay](https://docs.stripe.com/api/invoices/pay)
- [customer
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action)
- [expiry
date](https://docs.stripe.com/billing/subscriptions/pending-updates-reference#expiration)
- [Pending updates
reference](https://docs.stripe.com/billing/subscriptions/pending-updates-reference)