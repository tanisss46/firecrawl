# Using webhooks with subscriptions

## Learn to use webhooks to receive notifications of subscription activity.

You receive notifications from Stripe in your app through webhook events. Use
webhook events to manage
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating), as most
activity happens asynchronously. Process these events at a webhook endpoint or
other destinations like Amazon EventBridge by creating an [event
destination](https://docs.stripe.com/event-destinations).

To use webhooks with your subscriptions:

- Create a webhook endpoint in your app.
- Register your [webhook endpoint](https://docs.stripe.com/webhooks) in
Workbench
- Add logic to handle Stripe events. For subscriptions, these include payment
failures and subscription state changes (like moving from trial to an active
state). You can use the [webhook
quickstart](https://docs.stripe.com/webhooks/quickstart) to build a minimal
webhook endpoint.
- Test your webhook endpoint to confirm that it’s working as expected.

If your application runs on AWS, you can [configure Stripe to send events
directly to AWS EventBridge in your AWS
account](https://docs.stripe.com/event-destinations/eventbridge).

[Subscription
events](https://docs.stripe.com/billing/subscriptions/webhooks#events)
Stripe triggers [events](https://docs.stripe.com/api#event_types) every time a
subscription is created or changed. Some events are sent immediately when a
subscription is created, while others recur on regular billing intervals.

Make sure that your integration properly handles the events. For example, you
may want to email a customer if a payment fails or revoke a customer’s access
when a subscription is canceled.

The following table describes the most common events related to subscriptions
and, where applicable, suggests actions for handling the events.

EventDescription`customer.created`Sent when a
[Customer](https://docs.stripe.com/api/customers/object) is successfully
created.`customer.subscription.created`Sent when the subscription is created.
The subscription `status` might be `incomplete` if customer authentication is
required to complete the payment or if you set `payment_behavior` to
`default_incomplete`. View [subscription payment
behavior](https://docs.stripe.com/billing/subscriptions/overview#subscription-payment-behavior)
to learn more.`customer.subscription.deleted`Sent when a customer’s subscription
ends.`customer.subscription.paused`Sent when a subscription’s `status` changes
to `paused`. For example, this is sent when a subscription is
[configured](https://docs.stripe.com/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)
to pause when a [free trial ends without a payment
method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment).
Invoicing won’t occur until the subscription is
[resumed](https://docs.stripe.com/api/subscriptions/resume). We don’t send this
event if [payment collection is
paused](https://docs.stripe.com/billing/subscriptions/pause-payment) because
invoices continue to be created during that time
period.`customer.subscription.resumed`Sent when a subscription previously in a
`paused` status is resumed. This doesn’t apply when [payment collection is
unpaused](https://docs.stripe.com/billing/subscriptions/pause-payment#unpausing).`customer.subscription.trial_will_end`Sent
three days before the [trial period
ends](https://docs.stripe.com/billing/subscriptions/trials). If the trial is
less than three days, this event is
triggered.`customer.subscription.updated`Sent when a subscription starts or
[changes](https://docs.stripe.com/billing/subscriptions/change). For example,
renewing a subscription, adding a coupon, applying a discount, adding an invoice
item, and changing plans all trigger this
event.`entitlements.active_entitlement_summary.updated`Sent when a customer’s
active entitlements are updated. When you receive this event, you can provision
or de-provision access to your product’s features. Read more about [integrating
with
entitlements](https://docs.stripe.com/billing/entitlements).`invoice.created`Sent
when an invoice is created for a new or renewing subscription. If Stripe fails
to receive a successful response to `invoice.created`, then finalizing all
invoices with [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
is delayed for up to 72 hours. Read more about [finalizing
invoices](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized).-
Respond to the notification by sending a request to the [Finalize an
invoice](https://docs.stripe.com/api/invoices/finalize) API.
`invoice.finalized`Sent when an invoice is successfully finalized and ready to
be paid.- You can send the invoice to the customer. View [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
to learn more.
- Depending on your settings, we automatically charge the default payment method
or attempt collection. View [emails after
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#emails)
to learn more.
`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to
[handle invoice finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
by reading the guide. Learn more about [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
in the invoices overview guide.- Inspect the Invoice’s
[last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s
[automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
field.
- If `automatic_tax[status]=requires_location_inputs`, the invoice can’t be
finalized and payments can’t be collected. Notify your customer and collect the
required [customer location](https://docs.stripe.com/tax/customer-locations).
- If `automatic_tax[status]=failed`, retry the request later.
`invoice.paid`Sent when the invoice is successfully paid. You can provision
access to your product when you receive this event and the subscription `status`
is `active`.`invoice.payment_action_required`Sent when the invoice requires
customer authentication. Learn how to handle the subscription when the invoice
[requires
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action).
`invoice.payment_failed`

A payment for an invoice failed. The PaymentIntent status changes to
`requires_action`. The status of the subscription continues to be `incomplete`
*only* for the subscription’s first invoice. If a payment fails, there are
several possible actions to take:

- Notify the customer. Read about how you can configure [subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings) to
enable [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) and
other revenue recovery features.
- If you’re using PaymentIntents, collect new payment information and [confirm
the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm).
- Update the [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
on the subscription.
`invoice.upcoming`Sent a few days prior to the renewal of the subscription. The
number of days is based on the number set for Upcoming renewal events in the
[Dashboard](https://dashboard.stripe.com/settings/billing/automatic). For
existing subscriptions, changing the number of days takes effect on the next
billing period. You can still add [extra invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items),
if needed.`invoice.updated`Sent when a payment succeeds or fails. If payment is
successful the `paid` attribute is set to `true` and the `status` is `paid`. If
payment fails, `paid` is set to `false` and the `status` remains `open`. Payment
failures also trigger a `invoice.payment_failed`
event.`payment_intent.created`Sent when a
[PaymentIntent](https://docs.stripe.com/api/payment_intents) is
created.`payment_intent.succeeded`Sent when a PaymentIntent has successfully
completed payment.`subscription_schedule.aborted`Sent when a subscription
schedule is canceled because payment delinquency terminated the related
subscription.`subscription_schedule.canceled`Sent when a subscription schedule
is canceled, which also cancels any active associated
subscription.`subscription_schedule.completed`Sent when all
[phases](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-phases)
of a subscription schedule complete.`subscription_schedule.created`Sent when a
new subscription schedule is created.`subscription_schedule.expiring`Sent 7 days
before a subscription schedule is set to
expire.`subscription_schedule.released`Sent when a subscription schedule is
[released](https://docs.stripe.com/api/subscription_schedules/release), or
stopped and disassociated from the subscription, which
remains.`subscription_schedule.updated`Sent when a subscription schedule is
updated.
## Handle payment failures

Events provide a reliable way for Stripe to notify you of payment failures on
subscription invoices. Some payment failures are temporary-for example, a card
issuer might decline the initial charge but allow an automatic retry. Other
payment failures are final and require action, like not having a usable payment
method for the customer.

EventDescription
`invoice.payment_failed`

A payment for an invoice failed. The status of the PaymentIntent changes to
`requires_payment_method`. The status of the subscription changes to
`incomplete`. If a payment fails, there are several possible actions to take:

- Notify the customer.
- If you’re using PaymentIntents, collect new payment information and [confirm
the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm).
- Update the [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
on the subscription.
- Consider enabling [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries).

For more details on how to [handle payment failures that require a payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method),
see the subscriptions overview guide.

## Handle payments that require additional action

Some payment methods might require additional steps to complete, such as
customer authentication. If you receive these events, your app must notify the
customer to complete the required action. To learn how to [handle events that
require additional
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action),
read the subscription overview guide.

EventDescription`invoice.finalization_failed`The invoice couldn’t be finalized.
Learn how to [handle invoice finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
by reading the guide. Learn more about [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
in the invoices overview guide.- Inspect the Invoice’s
[last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s
[automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
field.
- If `automatic_tax[status]=requires_location_inputs`, the invoice can’t be
finalized and payments can’t be collected. Notify your customer and collect the
required [customer location](https://docs.stripe.com/tax/customer-locations).
- If `automatic_tax[status]=failed`, retry the request later.

`invoice.payment_failed`

A payment for an invoice failed. The PaymentIntent status changes to
`requires_action`. The status of the subscription changes to `incomplete`. If a
payment fails, there are several possible actions to take:

- Notify the customer.
- If you’re using PaymentIntents, collect new payment information and [confirm
the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm).
- Update the [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
on the subscription.
- Consider enabling [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries).

`invoice.payment_action_required`

A payment for an invoice failed. The PaymentIntent status changes to
`requires_action`. The status of the subscription changes to `incomplete`. If a
payment fails, there are several possible actions to take:

- Notify the customer.
- If you’re using PaymentIntents, collect new payment information and [confirm
the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm).
- Update the [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
on the subscription.
- Consider enabling [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries).

## Track active subscriptions

Subscriptions require coordination between your site and Stripe-the success or
failure of a customer’s recurring payments determines whether they can continue
to access to your product or service.

For typical integrations, you store customers’ credentials and a mapped
timestamp value that represents the access expiration date for that customer on
your site when a customer subscribes. When the customer logs in, you check
whether the timestamp is still in the future. If the timestamp is in the future
when the customer logs in, the account is active and the customer should still
have access to the service.

When the subscription
[renews](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle),
Stripe bills the customer and tries to collect payment by either [automatically
charging](https://docs.stripe.com/invoicing/automatic-charging) the payment
method on file, or [emailing the
invoice](https://docs.stripe.com/invoicing/integration#accept-invoice-payment)
to customers. Stripe notifies your site of the invoice status by sending a
webhook event:

- Your site receives an `invoice.paid` event.

- When automatically charging a payment method, your site first receives an
`invoice.upcoming` event to your configured [webhook
endpoint](https://docs.stripe.com/webhooks) a few days before renewal. You can
listen for this event to [add extra invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
to the upcoming invoice. If `collection_method=send_invoice`, Stripe doesn’t
send an `invoice.upcoming` event.
- Your application finds the customer the payment was made for.
- Your application updates the customer’s access expiration date in your
database to the appropriate date in the future (plus a day or two for leeway).

## Catch subscription status changes

Make sure that your integration properly monitors and handles transitions
between the subscription statuses described in the following table.

Some status changes require special attention:

- A few days before a trial ends and the subscription moves from `trialing` to
`active`, you receive a `customer.subscription.trial_will_end` event. When you
receive this event, verify that you have a payment method on the customer so you
can bill them. Optionally, notify the customer that they will be charged.
- When a subscription changes to `past_due`, notify the customer directly and
ask them to update their payment details. Stripe offers several features that
help automate this process-read more about [revenue
recovery](https://docs.stripe.com/billing/revenue-recovery).
- When a subscription changes to `canceled` or `unpaid`, revoke access to your
product.
StatusDescription`trialing`The subscription is currently in a trial period and
you can safely provision your product for your customer. The subscription
transitions automatically to `active` when a customer makes the first
payment.`active`The subscription is in good standing. For `past_due`
subscriptions, paying the latest associated invoice or marking it uncollectible
transitions the subscription to `active`. Note that `active` doesn’t indicate
that all outstanding invoices associated with the subscription have been paid.
You can leave other outstanding invoices open for payment, mark them as
uncollectible, or void them as you see fit.`incomplete`The customer must make a
successful payment within 23 hours to activate the subscription. Or the payment
[requires
action](https://docs.stripe.com/billing/subscriptions/webhooks#requires-action),
such as customer authentication. Subscriptions can also be `incomplete` if
there’s a pending payment and the PaymentIntent status is
`processing`.`incomplete_expired`The initial payment on the subscription failed
and the customer didn’t make a successful payment within 23 hours of
subscription creation. These subscriptions don’t bill customers. This status
exists so you can track customers that failed to activate their
subscriptions.`past_due`Payment on the latest finalized invoice either failed or
wasn’t attempted. The subscription continues to create invoices. Your
[subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
determine the subscription’s next state. If the invoice is still unpaid after
all attempted [smart
retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries), you
can configure the subscription to move to `canceled`, `unpaid`, or leave it as
`past_due`. To move the subscription to `active`, pay the most recent invoice
before its due date.`canceled`The subscription was canceled. During
cancellation, automatic collection for all unpaid invoices is disabled
(`auto_advance=false`). This is a terminal state that can’t be
updated.`unpaid`The latest invoice hasn’t been paid but the subscription remains
in place. The latest invoice remains open and invoices continue to generate, but
payments aren’t attempted. Revoke access to your product when the subscription
is `unpaid` because payments were already attempted and retried while
`past_due`. To move the subscription to `active`, pay the most recent invoice
before its due date.`paused`The subscription has ended its trial period without
a default payment method and the
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
is set to `pause`. Invoices are no longer created for the subscription. After
attaching a default payment method to the customer, you can [resume the
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription).
## Webhook endpoints and invoices

Register a webhook endpoint to keep track of invoice statuses. Your subscription
integration depends on correctly finalizing invoices and properly handling
invoice finalization failures.

When you enable [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection),
Stripe automatically finalizes and begins automatic collection of the
[invoice](https://docs.stripe.com/billing/invoices/subscription).

- If Stripe fails to receive a successful response to `invoice.created`, we
delay finalizing all invoices with [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
for up to 72 hours, excluding those where you have [set a custom scheduled
finalization time](https://docs.stripe.com/invoicing/scheduled-finalization).
- Responding properly to `invoice.created` includes handling all webhook
endpoints configured for your account, along with the webhook endpoints of any
platforms that you’ve connected to.
- Updating a subscription in a way that synchronously attempts payment (on the
initial invoice, and on some kinds of updates) doesn’t cause this delay.
- Invoice finalization failure prevents payment collection for the invoice. Make
sure you listen for the `invoice.finalization_failed` event in your webhook
endpoint.

### Webhook events related to invoice finalization

See a complete list of [invoice event
types](https://docs.stripe.com/api/events/types#event_types-invoice.created).

EventDescription`invoice.created`The invoice was successfully created and is
ready to be finalized. Read the docs to learn more about [finalizing
invoices](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized).-
Respond to the notification by sending a request to the [Finalize an
invoice](https://docs.stripe.com/api/invoices/finalize) API.
`invoice.finalized`The invoice was successfully finalized and is ready to be
paid.- You can send the invoice to the customer. Read more about [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized).
- Depending on your settings, Stripe automatically charges the default payment
method or attempts collection. Read more about [emails after
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#emails).
`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to
[handle invoice finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
by reading the guide. Learn more about [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
in the invoices overview guide.- Inspect the Invoice’s
[last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s
[automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
field.
- If `automatic_tax[status]=requires_location_inputs`, the invoice can’t be
finalized and payments can’t be collected. Notify your customer and collect the
required [customer location](https://docs.stripe.com/tax/customer-locations).
- If `automatic_tax[status]=failed`, retry the request later.

### Successful invoice finalization

Stripe waits an hour after receiving a successful response to the
`invoice.created` event before attempting payment. If we don’t receive a
successful response within 72 hours, we attempt to finalize and send the
invoice.

In case you want to treat one-off invoices differently than subscription
invoices, check the `subscription` property in the webhook body. This indicates
whether the invoice was created for a subscription.

In live mode, if your webhook endpoint doesn’t respond properly, Stripe
continues retrying the webhook notification for up to 3 days with an exponential
back off. In test mode, we retry three times over a few hours. During that time,
we won’t attempt to charge the customer unless we receive a successful response.
We’ll also send you an email to notify you that the webhook is failing.

This behavior applies to all webhook endpoints defined on your account,
including cases where a [Connect application](https://stripe.com/works-with) or
other third-party service is having trouble handling incoming webhooks.

### Invoice finalization failure

If Stripe can’t finalize an invoice, it sends a `invoice.finalization_failed`
[event](https://docs.stripe.com/api/events/types#event_types-invoice.finalization_failed)
to your webhook endpoint. Subscriptions remain active if invoices can’t be
finalized, which means that users may still be able to access your product while
you’re not able to collect payments. Make sure to take action on invoices that
fail finalization. You can’t collect payments on an invoice that isn’t
finalized.

To determine why the invoice finalization failed, look at the Invoice object’s
`last_finalization_error`
[field](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error),
which provides more information about the failure, including how to proceed.

If you’re using Stripe Tax, check if the
[automatic_tax.status](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-status)
field is `requires_location_inputs`, indicating that the address details are
invalid or insufficient. If Stripe Tax can’t find a recognized customer
location, we can’t finalize the invoice. Learn how to [handle invoice
finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures).

## Testing

To test your webhook endpoint or [event
destination](https://docs.stripe.com/event-destinations), choose one of these
two options:

- Perform actions in test mode that send legitimate events to your event
destination. For example, to trigger the
[charge.succeeded](https://docs.stripe.com/api#event_types-charge.succeeded)
event, you can use a [test card that produces a successful
charge](https://docs.stripe.com/billing/subscriptions/webhooks#cards).
- [Trigger events using the Stripe
CLI](https://docs.stripe.com/webhooks#test-webhook) or [using Stripe for Visual
Studio Code](https://docs.stripe.com/stripe-vscode#webhooks).

## See also

- [Subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
- [Testing subscriptions](https://docs.stripe.com/billing/testing)

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [event destination](https://docs.stripe.com/event-destinations)
- [webhook endpoint](https://docs.stripe.com/webhooks)
- [webhook quickstart](https://docs.stripe.com/webhooks/quickstart)
- [configure Stripe to send events directly to AWS EventBridge in your AWS
account](https://docs.stripe.com/event-destinations/eventbridge)
- [events](https://docs.stripe.com/api#event_types)
- [Customer](https://docs.stripe.com/api/customers/object)
- [subscription payment
behavior](https://docs.stripe.com/billing/subscriptions/overview#subscription-payment-behavior)
-
[configured](https://docs.stripe.com/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)
- [free trial ends without a payment
method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
- [resumed](https://docs.stripe.com/api/subscriptions/resume)
- [payment collection is
paused](https://docs.stripe.com/billing/subscriptions/pause-payment)
- [payment collection is
unpaused](https://docs.stripe.com/billing/subscriptions/pause-payment#unpausing)
- [trial period ends](https://docs.stripe.com/billing/subscriptions/trials)
- [changes](https://docs.stripe.com/billing/subscriptions/change)
- [integrating with entitlements](https://docs.stripe.com/billing/entitlements)
- [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
- [finalizing
invoices](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
- [Finalize an invoice](https://docs.stripe.com/api/invoices/finalize)
- [emails after
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#emails)
- [handle invoice finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
-
[last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
- [customer location](https://docs.stripe.com/tax/customer-locations)
- [requires
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action)
- [subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
- [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries)
- [confirm the
PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm)
- [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
- [Dashboard](https://dashboard.stripe.com/settings/billing/automatic)
- [extra invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
-
[phases](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-phases)
- [released](https://docs.stripe.com/api/subscription_schedules/release)
- [handle payment failures that require a payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
-
[renews](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
- [automatically charging](https://docs.stripe.com/invoicing/automatic-charging)
- [emailing the
invoice](https://docs.stripe.com/invoicing/integration#accept-invoice-payment)
- [revenue recovery](https://docs.stripe.com/billing/revenue-recovery)
- [resume the
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription)
- [invoice](https://docs.stripe.com/billing/invoices/subscription)
- [set a custom scheduled finalization
time](https://docs.stripe.com/invoicing/scheduled-finalization)
- [invoice event
types](https://docs.stripe.com/api/events/types#event_types-invoice.created)
- [Connect application](https://stripe.com/works-with)
-
[event](https://docs.stripe.com/api/events/types#event_types-invoice.finalization_failed)
-
[automatic_tax.status](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-status)
- [charge.succeeded](https://docs.stripe.com/api#event_types-charge.succeeded)
- [Trigger events using the Stripe
CLI](https://docs.stripe.com/webhooks#test-webhook)
- [using Stripe for Visual Studio
Code](https://docs.stripe.com/stripe-vscode#webhooks)
- [Testing subscriptions](https://docs.stripe.com/billing/testing)