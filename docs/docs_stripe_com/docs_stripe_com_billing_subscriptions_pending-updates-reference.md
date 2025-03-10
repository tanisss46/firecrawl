# Pending updates reference

## Learn more about the pending updates feature.

## Supported attributes

Only certain attributes can be used to create a pending update. These attributes
either control proration behavior or generate new
[invoices](https://docs.stripe.com/api/invoices).

The supported attributes for the [update
subscription](https://docs.stripe.com/api/subscriptions/update) endpoint are:

- `expand`
- `payment_behavior`
- `proration_behavior`
- `proration_date`
- `billing_cycle_anchor`
- `items`- `price`
- `quantity`
- `trial_end`
- `trial_from_plan`
- `add_invoice_items`

The supported attributes for the [create subscription
item](https://docs.stripe.com/api/subscription_items/create) and [update
subscription item](https://docs.stripe.com/api/subscription_items/update)
endpoints are:

- `expand`
- `payment_behavior`
- `proration_behavior`
- `proration_date`
- `price`
- `quantity`

## Pending updates lifecycle

If payment succeeds, the invoice is updated to `paid` and the changes are
applied to the
[subscription](https://docs.stripe.com/billing/subscriptions/creating)
immediately. If payment fails, the updated values are added to the
`pending_update` hash on the `Subscription` object. The `latest_invoice` for the
subscription refers to an unpaid invoice in an `open` status. The subscription
will continue to cycle as if no update request was made.

There are two ways to [handle payment
failures](https://docs.stripe.com/billing/subscriptions/pending-updates#handling-failed-payments).
These are related to declines and customer authentication. After resolving these
issues, payment is attempted again. If the payment succeeds, the changes are
applied and the `pending_update` hash is cleared. If payment fails again, the
`pending_update` hash remains on the subscription with the original expiry date
and no changes are applied.

If you [cancel a pending
update](https://docs.stripe.com/billing/subscriptions/pending-updates#canceling-changing),
the `pending_update` hash is cleared and the associated changes are discarded.

### Expiration

If you don’t take any action after an update fails, the invoice is voided and
the pending update is discarded after the `expired_at` time on the
`pending_update` has passed. This time is set to either the [trial
end](https://docs.stripe.com/api/subscriptions/object#subscription_object-trial_end)
time or the [current period
end](https://docs.stripe.com/api/subscriptions/object#subscription_object-current_period_end),
whichever comes first. If these times are greater than 23 hours from the time
the update is made, the `expired_at` time is calculated to 23 hours after the
update call was made.

Stripe also automatically voids the invoice and removes the pending update if
any of the following occurs:

- The subscription reaches a billing threshold.
- A subscription schedule linked to the subscription transitions to a new phase.

## Pending updates events

You can use [webhooks](https://docs.stripe.com/webhooks) to listen for the
following events related to pending updates:

EventPurpose`customer.subscription.updated`Receive notifications for
subscriptions, checking for the `pending_updates` hash and [resolving payment
failures](https://docs.stripe.com/billing/subscriptions/pending-updates#handling-failed-payments)
if needed.`customer.subscription.pending_update_applied`Receive notifications
when pending updates are applied so that you can take further actions like
upgrading, downgrading, provisioning or deprovisioning services, and so
on.`customer.subscription.pending_update_expired`Receive notifications when
pending updates expire or are automatically voided, and if needed, try the
update request again.
## Pending updates and subscription schedules

Pending updates and [subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
can both be used to manage subscriptions. If a pending update exists when a
schedule changes phases, the pending update is discarded and the associated
invoice is voided before the phase transition occurs. You can retry the update
request after the phase transition if needed.

## Usage records

If a subscription includes metered items, Stripe bills any outstanding usage
records on the pending update invoice. However, if payment for the pending
update doesn’t occur before the expiration date, Stripe discards these usage
records, which prevents billing on the subsequent invoice. Additionally, if the
pending update removes a metered price, Stripe disregards any usage reported
between the pending update’s creation and the resulting invoice’s payment,
excluding it from all invoices.

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [update subscription](https://docs.stripe.com/api/subscriptions/update)
- [create subscription
item](https://docs.stripe.com/api/subscription_items/create)
- [update subscription
item](https://docs.stripe.com/api/subscription_items/update)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [handle payment
failures](https://docs.stripe.com/billing/subscriptions/pending-updates#handling-failed-payments)
- [cancel a pending
update](https://docs.stripe.com/billing/subscriptions/pending-updates#canceling-changing)
- [trial
end](https://docs.stripe.com/api/subscriptions/object#subscription_object-trial_end)
- [current period
end](https://docs.stripe.com/api/subscriptions/object#subscription_object-current_period_end)
- [webhooks](https://docs.stripe.com/webhooks)
- [subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)