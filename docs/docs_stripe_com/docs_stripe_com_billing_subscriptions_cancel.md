# Cancel subscriptions

## Learn how to cancel existing subscriptions.

This guide describes how to use the [Subscription
API](https://docs.stripe.com/api#cancel_subscription) or the
[Dashboard](https://dashboard.stripe.com/test/subscriptions) to manage customer
subscriptions.

If you want to keep a subscription active but temporarily stop collecting
payment, you can [pause payment
collection](https://docs.stripe.com/billing/subscriptions/pause-payment).
Pausing payment collection doesn’t affect the [subscription
status](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses),
which we recommend using as the trigger for starting or stopping service to your
customer.

[Subscriptions](https://docs.stripe.com/billing/subscriptions/creating) cancel
automatically after up to eight unsuccessful attempts to bill the customer. You
can configure the number of attempts in your [subscription lifecycle
settings](https://docs.stripe.com/billing/subscriptions/overview#settings).
Learn more about revenue recovery settings, such as [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries#smart-retries)
and configurable [customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails#configure-emails).

## Cancel subscriptions

You can cancel customer subscriptions manually with the
[API](https://docs.stripe.com/api/subscriptions/cancel) or in the
[Dashboard](https://dashboard.stripe.com/test/subscriptions). By default,
cancellation takes effect immediately and
[invoices](https://docs.stripe.com/api/invoices) are no longer generated for
canceled subscriptions. After it’s canceled, you can no longer update the
subscription or its [metadata](https://docs.stripe.com/metadata).

#### Common mistake

If you set a custom cancellation date, you can’t provide a refund. A credit
proration is always generated. To prevent a credit proration from generating,
make sure the custom cancellation date is within the current billing period and
`proration_behavior` is set to `none`.

DashboardAPI
To cancel a subscription in the Dashboard:

- From the [Subscriptions](https://dashboard.stripe.com/test/subscriptions)
page, click the overflow menu (), then select **Cancel subscription**.
- Choose when to end the subscription: immediately, at the end of the period, or
on a custom day.
- Choose to provide a refund for a
[prorated](https://docs.stripe.com/billing/subscriptions/prorations) amount,
refund the last payment in full, or provide no
[refund](https://docs.stripe.com/refunds).
- After finalizing all settings, click **Cancel subscription**.

### Prorate for usage-based billing

If a subscription is part of the way through a paid billing period, you can
prorate the cancellation by passing the
[prorate](https://docs.stripe.com/api/subscriptions/cancel#cancel_subscription-prorate)
parameter.

When you prorate a cancellation, you can optionally invoice for:

- Outstanding prorations
- [Metered
usage](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)

If you don’t prorate the subscription, all metered usage gets discarded and the
customer won’t receive credit for any potential prorations.

Create a final invoice immediately using the
[invoice_now](https://docs.stripe.com/api/subscriptions/cancel#cancel_subscription-invoice_now)
parameter. If you owe the customer a credit after cancellation, you can add the
credit to their credit balance to apply to future invoices. To [refund your
customer](https://support.stripe.com/questions/refunding-credit-balance-to-customer-after-subscription-downgrade-or-cancellation),
issue [refunds](https://docs.stripe.com/refunds#issuing) and then [adjust their
account balance](https://docs.stripe.com/billing/customer/balance#modifying)
back to zero.

### Cancel at the end of the current billing cycle

To cancel a subscription at the end of the current billing period, set
`cancel_at_period_end` to `true`:

```
curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cancel_at_period_end=true
```

This allows the subscription to complete the duration of time the customer has
already paid for. You can reactivate subscriptions scheduled for cancellation by
updating `cancel_at_period_end` to `false`. You can reactivate the subscription
at any time up to the end of the period.

### Cancel after scheduled changes or future billing cycles

To schedule a subscription to end after a specified number of billing cycles,
[create a subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules).
Set the schedule length by specifying one or more phases and intervals, and set
its
[end_behavior](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-end_behavior)
attribute to `cancel`.

With an end behavior of `cancel`, subscription schedules automatically manage
the subscription’s
[cancel_at](https://docs.stripe.com/billing/subscriptions/cancel#custom-cancel-date)
attribute. When the schedule is in its last phase, the subscription’s cancel
date is set to the phase’s end date, otherwise, the cancel date isn’t set on the
subscription.

As a result, adding a new phase to a schedule that’s currently in its last phase
removes the cancel date. If the subscription is in its last billing period when
extending or removing the cancel date, this might update the period end and
billing cycle anchor. See how to [set a custom cancel
date](https://docs.stripe.com/billing/subscriptions/cancel#custom-cancel-date)
for more details.

### Configure automatic cancellation after a dispute

#### Limited support

This feature is only supported for disputed credit and debit card payments
opened in the *full amount*.

When a customer [disputes](https://docs.stripe.com/disputes) a charge for a
subscription, the subscription continues to cycle, which can create more
disputed charges. You can change this behavior in the
[Dashboard](https://dashboard.stripe.com/settings/billing/automatic) to cancel
subscriptions instead. Changes to the subscription take effect after
approximately one hour.

Under [Manage disputed
payments](https://dashboard.stripe.com/settings/billing/automatic), select one
of the following:

- **cancel the subscription immediately without prorating** – The subscription
cancels immediately without any prorating. You can’t restart a canceled
subscription. You must create a new subscription for the customer if you want to
continue billing them.
- **cancel the subscription at the end of the period** – The subscription
cancels at the end of the current billing period and
[cancel_at_period_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-cancel_at_period_end)
is set to `true`. This allows you time to work through the dispute process
before the cancellation occurs.

For subscriptions managed with
[schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules),
the subscription is first released from the schedule and then canceled. This
means the rest of the scheduled changes won’t take effect.

## Handle invoice items when canceling subscriptions

Your customer might still be billed for pending [invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
on a subscription in the following cases:

- The subscription cancellation includes a final invoice
- Your customer has another active subscription

To prevent billing your customer for pending invoice items, you must [manually
delete](https://docs.stripe.com/api#delete_invoiceitem) the invoice items.

Similarly, any
[usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage)
reported during the billing period bills at the end of the period. To avoid a
final usage charge, use the
[clear_usage](https://docs.stripe.com/api#update_subscription-items-clear_usage)
parameter to [update the
subscription](https://docs.stripe.com/api#update_subscription) and remove the
metered price.

If you set the subscription to cancel at period end, any pending prorations are
left in place and still collected at the end of the period. If you cancel the
subscription before the end of the period, invoice items remain and won’t be
processed unless you specifically generate an invoice that includes them.

When you cancel a subscription, all `open` and `draft` invoices for that
subscription have their `auto_advance` property set to `false`. This [pauses
automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
for these invoices and prevents automatic reminder emails from sending. You can
still manually attempt to collect payment and send emails.

## Identify cancellation events

Stripe sends the following events for canceled subscriptions.

EventDescription`customer.subscription.deleted`Sent when you cancel a customer’s
subscription immediately. If the event’s `request` property isn’t `null`, that
indicates the cancellation is a result of your request rather than based on your
subscription settings.`customer.subscription.updated`Sent when you cancel a
customer’s subscription at the end of the billing period. This triggers when you
set `cancel_at_period_end` to `true` and the event reflects a change in the
`cancel_at_period_end` value for the subscription.
## Stop a pending cancellation

You can stop a scheduled cancellation through the [Update Subscription
API](https://docs.stripe.com/api/subscriptions/update) or the
[Dashboard](https://dashboard.stripe.com/test/subscriptions). You can’t
reactivate a canceled subscription.

DashboardAPI
To stop a scheduled cancellation in the Dashboard:

- On the [Subscriptions page](https://dashboard.stripe.com/test/subscriptions),
select the subscription you want to update.
- From the Subscription details page, click **Actions**, then select **Don’t
cancel**.

## Set a custom cancel date

Use the
[cancel_at](https://docs.stripe.com/api/subscriptions/update#update_subscription-cancel_at)
parameter to cancel a subscription at a future timestamp.

```
curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cancel_at=1723766400
```

When you schedule a cancel date that occurs before the billing period ends, the
subscription’s
[current_period_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-current_period_end)
updates to match the `cancel_at` date. This creates prorations for the change in
the current period, unless your update
[disables](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)
prorations.

If you schedule a cancel date that occurs more than one period away, the
subscription’s cycle remains unaffected until the subscription renews into the
period that contains the `cancel_at` date. Then, the `current_period_end` for
the renewal shortens to match the `cancel_at` date.

For example, your customer subscribes to a 120 USD per year licensed
subscription that renews on January 1, 2024. They set the subscription to cancel
on July 1, 2024. The final invoice subtotal on January 1 calculates as 60 USD
and the `current_period_end` is July 1.

Changing, adding, or removing a scheduled cancel date within the current period
updates the `current_period_end` and creates prorations. In the above example,
on February 15 you update the cancel date to October 1. The current period end
becomes October 1, and Stripe creates prorations for 30 USD for the additional
quarter. To invoice the prorated items immediately instead of in a final invoice
on October 1, pass a
[proration_behavior](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_behavior)
of `always_invoice` in the update, or separately [create a one-off
invoice](https://docs.stripe.com/billing/invoices/subscription#generating-invoices).

The subscription’s [billing cycle
anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_cycle_anchor)
property might change if it tracked the previous cancel date. During the first
period, Stripe preserves any anchor you [originally
set](https://docs.stripe.com/billing/subscriptions/billing-cycle#new-subscriptions)
on the subscription. When the first period has finished, or if you didn’t
provide a custom anchor when creating the subscription, the anchor resets to the
[current period
start](https://docs.stripe.com/api/subscriptions/object#subscription_object-current_period_start).

Adding a cancel date or moving an existing one closer to the current time
shortens the [billing cycle
anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_cycle_anchor)
to match the new cancel date. In the above example, on February 15 you update
the cancel date to April 1. The period end and billing anchor become April 1,
and Stripe creates prorations for -30 USD to credit your customer for unused
time for April 1 to July 1.

## See also

- [Using trial periods](https://docs.stripe.com/billing/subscriptions/trials)
- [Update subscription](https://docs.stripe.com/api#update_subscription)
- [Cancel subscription](https://docs.stripe.com/api#cancel_subscription)

## Links

- [customer portal cancellation
page](https://docs.stripe.com/customer-management/cancellation-page)
- [Subscription API](https://docs.stripe.com/api#cancel_subscription)
- [Dashboard](https://dashboard.stripe.com/test/subscriptions)
- [pause payment
collection](https://docs.stripe.com/billing/subscriptions/pause-payment)
- [subscription
status](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [subscription lifecycle
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
- [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries#smart-retries)
- [customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails#configure-emails)
- [API](https://docs.stripe.com/api/subscriptions/cancel)
- [invoices](https://docs.stripe.com/api/invoices)
- [metadata](https://docs.stripe.com/metadata)
- [prorated](https://docs.stripe.com/billing/subscriptions/prorations)
- [refund](https://docs.stripe.com/refunds)
-
[prorate](https://docs.stripe.com/api/subscriptions/cancel#cancel_subscription-prorate)
- [Metered
usage](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
-
[invoice_now](https://docs.stripe.com/api/subscriptions/cancel#cancel_subscription-invoice_now)
- [refund your
customer](https://support.stripe.com/questions/refunding-credit-balance-to-customer-after-subscription-downgrade-or-cancellation)
- [refunds](https://docs.stripe.com/refunds#issuing)
- [adjust their account
balance](https://docs.stripe.com/billing/customer/balance#modifying)
- [create a subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
-
[end_behavior](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-end_behavior)
-
[cancel_at](https://docs.stripe.com/billing/subscriptions/cancel#custom-cancel-date)
- [disputes](https://docs.stripe.com/disputes)
- [Dashboard](https://dashboard.stripe.com/settings/billing/automatic)
-
[cancel_at_period_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-cancel_at_period_end)
- [invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
- [manually delete](https://docs.stripe.com/api#delete_invoiceitem)
-
[usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage)
-
[clear_usage](https://docs.stripe.com/api#update_subscription-items-clear_usage)
- [update the subscription](https://docs.stripe.com/api#update_subscription)
- [pauses automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
- [Update Subscription API](https://docs.stripe.com/api/subscriptions/update)
-
[cancel_at](https://docs.stripe.com/api/subscriptions/update#update_subscription-cancel_at)
-
[current_period_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-current_period_end)
-
[disables](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)
-
[proration_behavior](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_behavior)
- [create a one-off
invoice](https://docs.stripe.com/billing/invoices/subscription#generating-invoices)
- [billing cycle
anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_cycle_anchor)
- [originally
set](https://docs.stripe.com/billing/subscriptions/billing-cycle#new-subscriptions)
- [current period
start](https://docs.stripe.com/api/subscriptions/object#subscription_object-current_period_start)
- [Using trial periods](https://docs.stripe.com/billing/subscriptions/trials)