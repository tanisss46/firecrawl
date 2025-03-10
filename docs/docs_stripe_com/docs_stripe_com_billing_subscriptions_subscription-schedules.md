# Subscription schedules

## Learn about subscription schedules and how to use them.

Use [subscription schedules](https://docs.stripe.com/api/subscription_schedules)
to automate changes to subscriptions over time. You can
[create](https://docs.stripe.com/api/subscription_schedules/create)
subscriptions directly through a schedule or you can add a schedule to an
existing subscription. Use the
[phases](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases)
attribute to define the changes you want to make to the subscription. After a
schedule completes all of its phases, it completes based on its
[end_behavior](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-end_behavior).

Some changes you might want to schedule include:

- Starting a subscription on a future date
- Backdating a subscription to a past date
- Upgrading or downgrading a subscription

Subscription schedules are available in both the Stripe Billing Dashboard and
the API. Here’s a quick video of how subscription schedules work in the
Dashboard:

Subscription schedules in the Dashboard

The rest of this document explains subscription schedules in more detail. To see
a list of examples, see the [use
cases](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases)
page.

## Phases

When creating a subscription schedule, use the
[phases](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases)
attribute to define when changes occur and what properties of the subscription
to change. For example, you might offer a coupon for 50% off for the first three
months of a subscription. In this scenario, you’d create a subscription schedule
where the first phase is three months long and contains the 50% off coupon. In
the second phase, the subscription would be reverted to the normal cost and the
coupon would be removed. Phases must be sequential, meaning only one phase can
be active at a given time. You can have up to 10 phases.

### Set the length of a phase

The
[interval](https://docs.stripe.com/api/prices/object#price_object-recurring-interval)
of a price determines how often to bill for a subscription. For example, a
monthly interval is billed every month. Phases have an
[iterations](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-iterations)
attribute that you use to specify how long a phase should last. Multiply this
value by the interval to determine the length of the phase. If a subscription
schedule uses a price with a monthly interval and you set `iterations=2`, the
phase lasts for two months.

The `end_date` of one phase has to be the `start_date` for the next phase. Using
`iterations` automatically sets the `start_date` and `end_date` properly. You
can set these values manually, but Stripe recommends using `iterations` instead.
Because manually setting the start and end dates is prone to errors, only use it
for advanced use cases.

### Transition to the next phase

Phase transitions happen automatically after the `end_date` on a phase is
reached. When a phase starts, Stripe updates the subscription based on the
attributes of the next phase. You can optionally enable
[proration](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-proration_behavior)
to credit the user for unused items or time on the plan.

### Use trials

You can add trial periods by setting [trial
end](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-trial_end)
on a phase. If you want the entire phase to be a trial, set the value of
`trial_end` to the same time as the `end_date` of the phase. You can also set
`trial_end` to a time before the `end_date` if you want to make only part of the
phase a trial. When scheduling updates, you must specify the new `trial_end` on
each phase.

### Complete a schedule

Subscription schedules end after the last phase is complete. At this point, the
subscription is left in place and is no longer associated with the schedule. If
you want to cancel a subscription after the last phase of a schedule completes,
you can set
[end_behavior](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-end_behavior)
to `cancel`.

### Phase attribute inheritance

When a phase becomes active, all attributes set on the phase are also set on the
subscription. After the phase ends, attributes remain the same unless the next
phase modifies them, or if the schedule has no default setting. You can set some
attributes on both schedules and phases. This includes:

Schedule attributePhase
attribute[default_settings.billing_thresholds](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings-billing_thresholds)[phases.billing_thresholds](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-billing_thresholds)[default_settings.collection_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-default_settings-collection_method)[phases.collection_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-collection_method)[default_settings.default_payment_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-default_settings-default_payment_method)[phases.default_payment_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-default_payment_method)[default_settings.invoice_settings](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-default_settings-invoice_settings)[phases.invoice_settings](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-invoice_settings)
If one of these attributes is defined on the schedule, it becomes the default
for all phases. When the same property is defined on both the schedule and the
phase, the phase attribute overrides the schedule attribute. This behavior is
explained more below:

Schedule attribute presentPhase attribute presentOutcomeNoNoDefaults to the
customer or account settingsSchedule attribute setYesYesPhase attribute
setNoYesPhase attribute set
### Use phase metadata

You can use subscription schedule phases to set metadata on the underlying
subscription. This allows you to control the metadata on a subscription with
scheduled updates.

APIDashboard
To use phase metadata with the API, set
[metadata](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-metadata)
on the phases of a subscription schedule. When the underlying subscription
enters a phase:

- Metadata from the phase with non-empty values are *added* to the metadata on
the subscription if the keys *aren’t* already present in the latter.
- Metadata from the phase with non-empty values are used to *update* the
metadata on the subscription if the keys *are* already present in the latter.
- Metadata from the phase with *empty values* are used to *unset* the
corresponding keys in the metadata on the subscription.

To unset all keys in the subscription’s metadata, update the subscription
directly or unset every key individually from the phase’s metadata. Updating the
underlying subscription’s metadata directly doesn’t affect the current phase’s
metadata.

The following example illustrates a subscription schedule with two phases, where
each phase has its own metadata:

```
{
 ...
 "object": "subscription_schedule",
 "phases": [
 { // Phase 1
 ...
 "metadata": {
 "channel": "self-serve",
 "region": "apac",
 "upsell-products": "alpha"
 },
 },
 { // Phase 2
 ...
 "metadata": {
 "channel": "sales",
 "churn-risk": "high",
 "upsell-products": ""
 },
 }
 ],
}
```

When this schedule creates a new subscription and the subscription enters `Phase
1`, the three keys in `Phase 1` metadata are added to the subscription’s
metadata. Hence, the subscription in `Phase 1` has the following metadata:

```
{
 ...
 "object": "subscription",
 "metadata": {
 "channel": "self-serve",
 "region": "apac",
 "upsell-products": "alpha"
 },
}
```

When the subscription enters `Phase 2`, the subscription’s metadata is updated:

- The value of `channel` is updated because a value is specified on the phase’s
metadata and the subscription already has metadata with that key.
- The value of `region` is unchanged because it’s not specified on the phase.
- `churn-risk` is added because this is a new key.
- `upsell-products` is unset because an empty value is specified on the phase.

Hence, the subscription in `Phase 2` has the following metadata:

```
{
 ...
 "object": "subscription",
 "metadata": {
 "channel": "sales",
 "region": "apac",
 "churn-risk": "high"
 }
}
```

Learn how to [copy subscription metadata onto subscription
invoices](https://docs.stripe.com/billing/invoices/subscription#subscription-metadata).

## Create subscription schedules

The [use
cases](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases)
page has more thorough examples but below is a basic example of creating a
subscription schedule using a customer. Creating a schedule this way
automatically creates the subscription as well.

#### Note

Unlike when you create a subscription directly, the first invoice of a
subscription schedule with `collection_method` set to `charge_automatically`
behaves like a recurring invoice and *isn’t* immediately finalized at the time
the schedule’s subscription is created. The invoice begins in a `draft` status
and is finalized by Stripe [about 1 hour after
creation](https://docs.stripe.com/billing/subscriptions/webhooks#understand).

This means that, for example, creating a charge-automatically subscription
schedule with `start_date=now` also creates a subscription and an invoice in the
`draft` status. This gives you a 1-hour window to [make edits to the
invoice](https://docs.stripe.com/api/invoices/update). Later, the invoice is
auto-advanced into the `open` or `paid` status depending on the outcome of the
asynchronous payment attempt at finalization time.

APIDashboard
```
curl https://api.stripe.com/v1/subscription_schedules \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_GBHHxuvBvO26Ea \
 -d start_date=now \
 -d end_behavior=release \
 -d "phases[0][items][0][price]"=price_1GqNdGAJVYItwOKqEHb \
 -d "phases[0][items][0][quantity]"=1 \
 -d "phases[0][iterations]"=12
```

This schedule:

- Starts as soon as it’s created.
- Sets the subscription to one instance of the product at
`price_1GqNdGAJVYItwOKqEHb`.
- Goes through 12 iterations and then releases the subscription from the
schedule.

You can also create subscription schedules by passing a subscription ID:

```
curl https://api.stripe.com/v1/subscription_schedules \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d from_subscription=sub_GB98WOvaRAWPl6
```

Creating a schedule this way uses attributes on the subscription to set
attributes on the schedule.

Similar to other Stripe APIs, you can retrieve and update [subscription
schedules](https://docs.stripe.com/api/subscription_schedules). You can also
cancel and release them. Cancelling a subscription schedule cancels the
subscription as well. If you only want to remove a schedule from a subscription,
use the [release](https://docs.stripe.com/api/subscription_schedules/release)
call.

## Update subscription schedules

You can only update the current and future phases on subscription schedules.

APIDashboard
You need to pass in all current and future phases when you update a subscription
schedule. You also need to pass in any previously set parameters that you want
to keep. Any parameters that were previously set are unset for the existing
phase unless you pass those in the update request. You still receive information
in the response about past phases.

You can include up to 10 current or future phases. Updating the active phase
updates the underlying subscription as well. For example, this call maintains
the existing start and end dates, but updates the `quantity` to two:

```
curl
https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "phases[0][items][0][price]"={{PRICE_ID}} \
 -d "phases[0][items][0][quantity]"=2 \
 -d "phases[0][start_date]"=1577865600 \
 -d "phases[0][end_date]"=1580544000
```

You can also end the current phase immediately and start a new phase. This moves
the active phase to the past and immediately applies the new phase to the
subscription. The example below ends the current phase and starts a new phase:

```
curl
https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "phases[0][items][0][price]"={{PRICE_ID}} \
 -d "phases[0][items][0][quantity]"=1 \
 -d "phases[0][start_date]"=1577865600 \
 -d "phases[0][end_date]"=now \
 -d "phases[1][items][0][price]"={{PRICE_ID}} \
 -d "phases[1][items][0][quantity]"=2 \
 -d "phases[1][start_date]"=now \
 -d "phases[1][end_date]"=1580544000
```

To add additional phases to a subscription schedule, pass in the current phase,
and then define your new phases:

```
curl
https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "phases[0][items][0][price]"={{PRICE_ID}} \
 -d "phases[0][items][0][quantity]"=1 \
 -d "phases[0][start_date]"=1577865600 \
 -d "phases[0][end_date]"=1580544000 \
 -d "phases[1][items][0][price]"={{PRICE_ID}} \
 -d "phases[1][items][0][quantity]"=2 \
 -d "phases[1][iterations]"=1
```

## Preview an invoice

Use the
[schedule](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule)
parameter in the [create
preview](https://docs.stripe.com/api/invoices/create_preview) to preview the
next invoice for a subscription schedule.

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d schedule={{SUBSCRIPTION_SCHEDULE_ID}}
```

### Previewing schedule creation and updates

Use the parameters in
[schedule_details](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule_details)
to preview creating or updating a subscription schedule. Pass an existing
[schedule](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule)
to tell Stripe whether it’s a creation or an update.

Pass all of the current and future
[phases](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule_details-phases)
you’re previewing.

For example, the following code previews the first invoice for a subscription
schedule with `1` phase that lasts for `12` billing periods.

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "customer_details[address][line1]"="920 5th Ave" \
 -d "customer_details[address][city]"=Seattle \
 -d "customer_details[address][state]"=WA \
 -d "customer_details[address][postal_code]"=98104 \
 -d "customer_details[address][country]"=US \
 -d "schedule_details[phases][0][start_date]"=now \
 -d "schedule_details[phases][0][items][0][price]"={{PRICE_ID}} \
 -d "schedule_details[phases][0][items][0][quantity]"=1 \
 -d "schedule_details[phases][0][iterations]"=12
```

## Additional considerations

Subscription schedules generally follow the same restrictions as subscriptions,
but also introduce some of their own restrictions. Additionally, the interaction
between subscription schedules and subscriptions can produce unexpected
behavior. Review the following sections to understand limitations, product
behavior, and general best practices when using subscription schedules.

### Restrictions

- You can only define up to 10 current or future phases at a time on a
subscription schedule. Past phases don’t count against this limit.
- Subscription schedule phases also follow [the same restrictions as
subscriptions](https://docs.stripe.com/billing/subscriptions/multiple-products#restrictions)
when creating subscription schedule phases with multiple items.

### Dashboard limitations

You can create and update subscription schedules without code in the
[Dashboard](https://dashboard.stripe.com/test/subscriptions).

In the Dashboard, you can set the following settings globally across all phases,
but not on a per phase basis:

- Billing thresholds
- Payment methods
- Invoice settings
- Subscription description
- Trial days (only works with the first phase)

The following parameters aren’t supported in the Dashboard:

- Subscription schedule metadata
- Phase item metadata
- Currency
- All Connect parameters

### Subscription updates when a schedule is attached

Use [subscription schedules](https://docs.stripe.com/api/subscription_schedules)
to modify subscriptions automatically when time passes and the schedule’s next
phase is entered. Some changes that you make directly to the subscription
propagate to the subscription schedule’s phases, but some don’t. This means that
any modifications you make directly to the subscription might be overwritten by
the subscription schedule when the next phase is entered.

When scheduling changes to a subscription, follow these best practices:

- If a subscription has a subscription schedule attached, use the [Subscription
Schedule](https://docs.stripe.com/api/subscription_schedules) API to modify the
subscription, instead of the
[Subscriptions](https://docs.stripe.com/api/subscriptions#subscriptions) API.
- Store the subscription schedule IDs alongside the subscription ID for future
API updates. The subscription schedule ID returns when you [use the API to
create it](https://docs.stripe.com/api/subscription_schedules/create) or through
the
[subscription_schedule.created](https://docs.stripe.com/api/events/types#event_types-subscription_schedule.created)
webhook when Stripe creates it automatically, such as when a customer scheduled
a downgrade in the [Customer
Portal](https://docs.stripe.com/customer-management/configure-portal#configure-subscription-management).
- Discard the subscription schedule IDs when a subscription schedule is
released. You can make changes to the subscriptions directly or create a new
subscription schedule. The subscription schedule ID is returned when [released
with the API](https://docs.stripe.com/api/subscription_schedules/release) or
through the
[subscription_schedule.released](https://docs.stripe.com/api/events/types#event_types-subscription_schedule.released)
webhook event when the subscription schedule releases.
- Use the Dashboard to modify subscriptions, if possible, which automatically
updates any attached subscription schedule.

Specifically, when you change any of the following subscription attributes
directly on a subscription, this action might automatically create a new
subscription schedule phase:

- `discounts`
- `tax_rates`
- `items`
- `trial_end`, `trial_settings`, `trial_start`
- `application_fee_percent`
- `add_invoice_items`
- `automatic_tax`

For example, consider a subscription with two items. The subscription has a
subscription schedule attached with a single phase, mirroring the current state
of the subscription. If you [use the API to
delete](https://docs.stripe.com/api/subscription_items/delete) one of the items,
this automatically splits the attached subscription schedule’s phase into two
phases:

- The phase that just ended and had two subscription items
- The new phase that has just one item on the subscription

When subscription schedule phases automatically split, the following properties
are copied from the current phase to the new phase:

- `proration_behavior`
- `billing_cycle_anchor`
- `cancel_at_period_end`
- `description`
- `metadata`
- `pause_collection`

Additionally, Stripe might copy the following top-level subscription attributes
to the subscription schedule or its
[default_settings](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings):

Subscription attributeCopied to new subscription schedule phaseCopied to
subscription schedule
`default_settings``coupon`X`trial_end`X`tax_rates`X`application_fee_percent`XX`discounts`X`collection_method`XX`invoice_settings`XX`default_payment_method`XX`default_source`XX`transfer_data`XX`on_behalf_of`XX`billing_thresholds`XX`currency`X`add_invoice_items`X`automatic_tax`XX`items.prices`X
Updates to subscription `metadata` aren’t propagated to an attached subscription
schedule.

## See also

- [Subscription Schedules use
cases](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases)

## Links

- [subscription schedules](https://docs.stripe.com/api/subscription_schedules)
- [create](https://docs.stripe.com/api/subscription_schedules/create)
-
[phases](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases)
-
[end_behavior](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-end_behavior)
- [use
cases](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases)
-
[interval](https://docs.stripe.com/api/prices/object#price_object-recurring-interval)
-
[iterations](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-iterations)
-
[proration](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-proration_behavior)
- [trial
end](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-trial_end)
-
[end_behavior](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-end_behavior)
-
[default_settings.billing_thresholds](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings-billing_thresholds)
-
[phases.billing_thresholds](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-billing_thresholds)
-
[default_settings.collection_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-default_settings-collection_method)
-
[phases.collection_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-collection_method)
-
[default_settings.default_payment_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-default_settings-default_payment_method)
-
[phases.default_payment_method](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-default_payment_method)
-
[default_settings.invoice_settings](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-default_settings-invoice_settings)
-
[phases.invoice_settings](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-invoice_settings)
-
[metadata](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-metadata)
- [copy subscription metadata onto subscription
invoices](https://docs.stripe.com/billing/invoices/subscription#subscription-metadata)
- [about 1 hour after
creation](https://docs.stripe.com/billing/subscriptions/webhooks#understand)
- [make edits to the invoice](https://docs.stripe.com/api/invoices/update)
- [release](https://docs.stripe.com/api/subscription_schedules/release)
-
[schedule](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule)
- [create preview](https://docs.stripe.com/api/invoices/create_preview)
-
[schedule_details](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule_details)
-
[phases](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-schedule_details-phases)
- [the same restrictions as
subscriptions](https://docs.stripe.com/billing/subscriptions/multiple-products#restrictions)
- [Dashboard](https://dashboard.stripe.com/test/subscriptions)
- [Subscriptions](https://docs.stripe.com/api/subscriptions#subscriptions)
-
[subscription_schedule.created](https://docs.stripe.com/api/events/types#event_types-subscription_schedule.created)
- [Customer
Portal](https://docs.stripe.com/customer-management/configure-portal#configure-subscription-management)
-
[subscription_schedule.released](https://docs.stripe.com/api/events/types#event_types-subscription_schedule.released)
- [use the API to delete](https://docs.stripe.com/api/subscription_items/delete)
-
[default_settings](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings)