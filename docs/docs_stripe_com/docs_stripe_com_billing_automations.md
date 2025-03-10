# Automations

## Learn how to customize subscription and invoice workflows with automations.

Stripe Billing automations are a no-code way to build custom, automated
workflows to streamline your business processes, enhance customer communication,
and improve revenue recovery efforts.

Tailor automated workflows to fit your specific use case, for example:

- [Custom dunning flow for annual
subscribers](https://docs.stripe.com/billing/automation-recipes#custom-dunning-flow)
- [Notify your team when high value invoices are
overdue](https://docs.stripe.com/billing/automation-recipes#invoice-overdue-notifications)
- [Email a confirmation when a subscription is
canceled](https://docs.stripe.com/billing/automation-recipes#subscription-cancellation-confirmation)
- [Give new users a 10 USD spend credit at
signup](https://docs.stripe.com/billing/automation-recipes#signup-spend-credit)
Beta

Workflows consist of triggers, filter conditions, and actions. This guide
describes how to use those to build and configure your own custom automation.
Follow an [automation
recipe](https://docs.stripe.com/billing/automation-recipes) to get started with
common use cases.

## Set up automations

To get started with automations, follow these steps:

- In the Stripe Dashboard, go to the [Automations
tab](https://dashboard.stripe.com/test/revenue_recovery/automations) in Billing.
- Click **New automation** or press the **n** key.
- Name the automation.
- Select the event that you want to trigger the automation.
- (Optional) Add [filter
conditions](https://docs.stripe.com/billing/automations#choose-filter-conditions)
so that your automation only runs when the specified conditions are met.
- Add a sequence of actions and delays.
- (Optional) If the selected trigger applies to other automations, drag the new
automation to the desired position in the priority order, then click **Save**.

#### Warning

When using automations, the
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
is no longer set in `invoice.payment_failed` webhooks but is set in
`invoice.updated` webhooks.

## Choose a trigger

You can choose from five triggers:

TriggerDescriptionExample use caseInvoice due date upcomingActions are executed
relative to the due date of the invoice. The automation terminates when the
invoice is paid, voided, or
[auto_advance](https://docs.stripe.com/api/invoices/object#invoice_object-auto_advance)
is turned off. This trigger is only for invoices with `collection_method` set to
`send_invoice`.Manage customer communication by scheduling `invoice.will_be_due`
webhooks at custom intervals.Invoice is finalizedTriggered when an invoice is
finalized. The automation terminates when the invoice is paid, voided, or
[auto_advance](https://docs.stripe.com/api/invoices/object#invoice_object-auto_advance)
is turned off.Mark invoices for certain customer segments as uncollectible
(write-off) after a period of time.Invoice is overdueTriggered when an invoice
becomes overdue. The automation terminates when the invoice is paid, voided, or
[auto_advance](https://docs.stripe.com/api/invoices/object#invoice_object-auto_advance)
is turned off. This trigger is only for invoices of type `send`.Manage customer
communication by scheduling `invoice.overdue` webhooks at custom intervals.
Manage collections by scheduling emails to the collections team.Subscription is
canceledTrigger when a subscription is canceled.Email a cancellation
confirmation to the customer. Optionally include a cancellation reason
survey.Subscription payment failsTriggered when a subscription invoice payment
fails its first attempt. The automation terminates when the invoice is paid,
voided, or
[auto_advance](https://docs.stripe.com/api/invoices/object#invoice_object-auto_advance)
is turned off.- Custom retry behavior for a subset of customers
- Notify your collections team of high-value payment failures.

## Choose filter conditions

After selecting a trigger, you can add one or more filter conditions. These
conditions need to be met for your automation to run. For example, if you filter
for customers on annual subscriptions, the automation only runs if there are
annual subscriptions.

Depending on the trigger, the following filter conditions are available:

ConditionDescriptionCustomer metadataA key-value pair to match on customer
[metadata](https://docs.stripe.com/api/metadata).Invoice metadataA key-value
pair to match on invoice
[metadata](https://docs.stripe.com/api/metadata).Invoice amountA minimum or
maximum amount per invoice defined in your default currency. Invoices not
denominated in your default currency are evaluated against their
conversion.Subscription intervalLimit to yearly or monthly
subscriptions.ProductLimit to invoices or subscriptions that contain at least
one of the products specified.
You can use the [Metadata API field](https://docs.stripe.com/api/metadata) to
directly apply metadata for customers and invoices.

## Choose actions

The following table describes the available actions for the various triggers:

ActionDescriptionSupported triggersSet retry policyA retry policy defines how
failed charges are retried. This action allows you to create a custom policy and
attach it to an invoice.Subscription payment failsMark subscription unpaidThe
subscription continues to generate invoices each billing cycle, which remain in
`draft` state.Subscription payment failsCancel subscriptionCanceling
subscriptions disables creating new invoices for the subscription and stops
automatic collection of all invoices from the subscription by setting
`auto_advance` to `false`. When you cancel a subscription, the Automation
immediately stops running.Subscription payment failsMark invoice
uncollectibleThe customer is unlikely to pay this invoice and you want to treat
it as bad debt in your accounting process.- Subscription payment fails
- Invoice finalized
- Invoice overdue
Send team emailEmail a custom memo, along with details about the trigger to a
team member or internal email address.All triggersSend subscription cancellation
emailEmail a cancellation confirmation to your customers. You also have the
option to include a survey link to collection cancellation reasons.Subscription
is canceledSend `invoice.will_be_due` webhookYou can schedule this webhook to be
triggered with custom delays to get reminders about an invoice that’s about to
be due.Invoice due date is setCreate subscription BetaCreates a subscription for
the newly created customer with a single product and price.Customer is
createdCredit customer balance BetaMakes a positive adjustment to the customer
credit balance in the amount you choose.Customer is created
## Manage and edit your automations

This section describes how to priority order and pause or stop automations.
These actions help make sure your automations run as expected.

### Priority ordering

You can configure multiple automations for the same trigger, but each event only
triggers one automation. When an event occurs that applies to multiple
automations, Stripe checks their filter conditions in priority order and runs
the first one that matches. All other automations are ignored.

If an automation executes, it ignores your global settings.

- **Scenario A**: You create an automation for the `Subscription payment fails`
event with no conditions applied. In this scenario, the automation runs every
time a subscription payment fails. Your default settings for subscription
payment failure won’t run.
- **Scenario B**: You create an automation for the `Subscription payment fails`
event with the condition that the invoice must be greater than 100 USD. In this
scenario, the automation runs if the subscription payment fails and the invoice
is over 100 USD. If a subscription payment fails and the invoice is less than
100 USD, your default settings for subscription payment failure run instead.

To change a trigger’s priority order, open the list of automations, click the
overflow menu () for any of that trigger’s automations, and select **Update
priority**. You can also select it from the **Actions** menu on the automation
details page. In the **Set priority** panel, drag each automation to the desired
position and then click **Save**.

### Pausing or stopping automations

To switch off or pause an automation, go to the [Automations
tab](https://dashboard.stripe.com/test/revenue_recovery/automations) on the
Revenue recovery page and turn off that automation’s toggle. If any executions
are in progress for that automation, you can let them finish or immediately
cancel all of them.

You can turn the automation on again at any time.

## Join our automations beta

If you're interested in early access to triggers and actions that are still in
beta, please register your interest below.

Collect EmailSubmitRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Custom dunning flow for annual
subscribers](https://docs.stripe.com/billing/automation-recipes#custom-dunning-flow)
- [Notify your team when high value invoices are
overdue](https://docs.stripe.com/billing/automation-recipes#invoice-overdue-notifications)
- [Email a confirmation when a subscription is
canceled](https://docs.stripe.com/billing/automation-recipes#subscription-cancellation-confirmation)
- [Give new users a 10 USD spend credit at
signup](https://docs.stripe.com/billing/automation-recipes#signup-spend-credit)
- [automation recipe](https://docs.stripe.com/billing/automation-recipes)
- [Automations
tab](https://dashboard.stripe.com/test/revenue_recovery/automations)
- [filter
conditions](https://docs.stripe.com/billing/automations#choose-filter-conditions)
-
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
-
[auto_advance](https://docs.stripe.com/api/invoices/object#invoice_object-auto_advance)
- [metadata](https://docs.stripe.com/api/metadata)
- [privacy policy](https://stripe.com/privacy)