# Create subscriptions with Stripe Billing

## With Connect, you can create subscriptions for your customers or connected accounts.

Software as a Service (SaaS) and marketplace businesses use Stripe Connect to
route payments between themselves, customers, and connected accounts. You can
use Connect to route payments or [payouts](https://docs.stripe.com/payouts) and
use Stripe Billing to support your recurring revenue model.

## Use cases

You can create
[subscriptions](https://docs.stripe.com/billing/subscriptions/overview) for
connect accounts, which supports several approaches for collecting payments. You
can create subscriptions for your connected account’s customers using direct or
destination charges, for your end customers to directly transact with your
platform, and to charge your connected accounts a fee for using your platform.

CustomerPlatformConnected account
The following use cases describe how to use Stripe Billing to create
subscriptions from end customers to connected accounts, to bill platform end
customers, and to bill connected accounts.

Use caseDescription[Create subscriptions from the end customer to the connected
account](https://docs.stripe.com/connect/subscriptions#customer-connected-account)Create
subscriptions for end customers to your connected accounts, which supports
several approaches for collecting payments. In this example,
[Prices](https://docs.stripe.com/api/prices) reside on the connected
account.[Create subscriptions to bill platform end
customers](https://docs.stripe.com/connect/subscriptions#customer-platform)Marketplaces
can directly offer membership subscriptions without involving your connected
account. In this example, [Prices](https://docs.stripe.com/api/prices) reside on
the platform.[Create subscriptions to bill connected
accounts](https://docs.stripe.com/connect/subscriptions#connected-account-platform)Platforms
can create subscriptions for their connected accounts. In this example,
[Prices](https://docs.stripe.com/api/prices) reside on the platform.
### Restrictions

Using subscriptions with Connect has these restrictions:

- Your platform can’t update or cancel a subscription that it didn’t create.
- Your platform can’t add an `application_fee_amount` to an invoice that it
didn’t create, nor to an invoice that contains invoice items the platform didn’t
create.
- Subscriptions aren’t automatically cancelled when you disconnect from the
platform. You must cancel the subscription after disconnection. You can use
[webhooks to monitor connected account
activity](https://docs.stripe.com/connect/webhooks).

## Create subscriptions from the end customer to the connected account

If you’re building a platform, you can create subscriptions for your connected
accounts’ customers, optionally taking a per-payment fee for your platform.

CustomerPlatformConnected account
This example builds an online publishing platform that allows customers to
subscribe to their favorite authors and pay them a monthly fee to receive
premium blog posts from each author.

## Before you begin

Before you can create subscriptions for your customers or connected accounts,
you must:

- Create a [connected account](https://docs.stripe.com/connect/accounts) for
each person that receives money on your platform. In our online publishing
example, a connected account represents an author.
- Create a pricing model. For this example, we create a flat-rate [pricing
model](https://docs.stripe.com/products-prices/pricing-models#flat-rate) to
charge customers a fee on a recurring basis, but per-seat and usage-based
pricing are also supported.
- Create a [customer with the intended payment
method](https://docs.stripe.com/billing/customer#manage-customers) for each
person that subscribes to a connected account. In our online publishing example,
you create a customer for each reader that subscribes to an author.

### Decide between direct charges and destination charges

You can use either direct charges or destination charges to split a customer’s
payment between the connected account and your platform.

With direct charges, customers won’t be aware of your platform’s existence
because the author’s name, rather than your platform’s name, is shown on the
statement descriptor. In our online publishing example, readers interact with
authors directly.

Direct charges are recommended for connected accounts with access to the full
Stripe Dashboard, which includes Standard accounts.

If you want your platform to be responsible for Stripe fees, refunds, and
chargebacks, use destination charges. In our online publishing example,
customers subscribe to your publishing platform, not directly with specific
authors.

Destination charges are recommended for connected accounts with access to the
Express Dashboard or connected accounts without access to a Stripe-hosted
dashboard, which includes Express and Custom accounts.

For more information about the different types of Connect charges, see [Charge
types](https://docs.stripe.com/connect/charges#types).

### Use direct charges to create a subscription

To create a subscription with
[Charges](https://docs.stripe.com/api/charges/object) associated to the
connected account, [create a
subscription](https://docs.stripe.com/api#create_subscription) while
[authenticated as the connected
account](https://docs.stripe.com/connect/authentication#stripe-account-header).
Make sure to define the customer with a default payment method and the
[Price](https://docs.stripe.com/api/prices) on the connected account. To use a
customer without a default payment method, set `payment_behavior:
"default_incomplete"`. Learn more about [payment
behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior).

Expand `latest_invoice.payment_intent` to include the Payment Element, which is
needed to confirm the payment. Learn more about [Payment
Elements](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#add-the-payment-element-to-your-page).

For an end-to-end example of how to implement a subscription signup and payment
flow in your application, see the [subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
guide.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d "expand[0]"="latest_invoice.payment_intent"
```

### Use destination charges to create a subscription

To create a subscription with
[Charges](https://docs.stripe.com/api/charges/object) associated to the platform
and automatically create transfers to a connected account, make a [create
subscription](https://docs.stripe.com/api#create_subscription) call while
providing the connected account ID as the `transfer_data[destination]`
[value](https://docs.stripe.com/api/subscriptions/object#subscription_object-transfer_data).

Expand `latest_invoice.payment_intent` to include the Payment Element, which you
need to confirm the payment. Learn more about [Payment
Elements](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#add-the-payment-element-to-your-page).

You can optionally specify an
[application_fee_percent](https://docs.stripe.com/api/subscriptions/object#subscription_object-application_fee_percent).
Learn more about [collecting
fees](https://docs.stripe.com/connect/subscriptions#collect-fees).

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d "expand[0]"="latest_invoice.payment_intent" \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

### Additional steps before you create a subscription

To create a destination charge, define both the customer and the price on the
platform account. You must have created a connected account on the platform. The
customer must exist within the platform account. When using destination charges,
the platform is the merchant of record.

## Create subscriptions to bill platform end customers

You can use Stripe Billing to create subscriptions for your end customers to
directly transact with your platform without involving your connected accounts.

CustomerPlatformConnected account
This example builds a marketplace that allows customers to order on-demand
delivery from restaurants. This marketplace offers customers a premium monthly
subscription that waives their delivery fees. Customers who subscribe to the
premium offering pay the marketplace directly and don’t subscribe to any
particular delivery service or restaurant.

## Before you begin

Before you create subscriptions for your customers, you must:

- Create a pricing model. For this example, we create a flat-rate [pricing
model](https://docs.stripe.com/products-prices/pricing-models#flat-rate) to
charge customers a fee on a recurring basis, but per-seat and usage-based
pricing are also supported.
- Create a [customer](https://docs.stripe.com/billing/customer#manage-customers)
record for every customer you want to bill.

You can also create a [connected
account](https://docs.stripe.com/connect/accounts) for each user that receives
money from your marketplace. In our on-demand restaurant delivery example, a
connected account is a restaurant or a delivery service. However, this step
isn’t required for customers to subscribe to your marketplace directly.

### Create a subscription

To create a subscription where your platform receives the funds, without any
money going to connected accounts, follow the [Subscriptions
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions) to
create a subscription with Stripe Billing.

### Create separate charges and transfers

If you want to manually transfer a portion of the funds that your platform
receives to your connected accounts later, use [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) to
pay out funds to one or more connected accounts. In our on-demand restaurant
delivery example, you can use separate charges and transfers to pay out an
affiliate fee to a delivery driver or restaurant who refers a customer to
subscribe to the premium delivery service.

## Create subscriptions to bill connected accounts

You can use Stripe Billing to create subscriptions to charge your connected
accounts a fee for using your platform.

CustomerPlatformConnected account
This example builds a gym management software platform that allows gym
businesses to pay a monthly fee to use the software to manage scheduling and
appointments for classes. The gym businesses pay the subscription fee, not the
gym patrons.

The gym management software also facilitates one-time payments between the gym
patron and gym business for each class that the gym patron enrolls in. The
monthly subscription is between the connected account and the platform, which
doesn’t involve the gym patron in the transaction.

In the diagram above, the gym business is the connected account and the gym
patron is the end customer.

## Before you begin

Before you create subscriptions for your customers or connected accounts, you
must:

- Create a [connected account](https://docs.stripe.com/connect/accounts) for
each user that receives money on your platform. In this example, the connected
account is the gym business.
- Create a pricing model. For this example, we create a flat-rate [pricing
model](https://docs.stripe.com/products-prices/pricing-models#flat-rate) to
charge customers a fee on a recurring basis, but per-seat and usage-based
pricing are also supported.
- Create a [customer](https://docs.stripe.com/billing/customer#manage-customers)
on the platform with the intended payment method for every connected account you
want to bill. In the gym management software example, you create a customer for
each gym business:

### Create a Customer object to represent the connected account

If your connected accounts use Stripe to process payments for their end
customers, they might have already created a
[Customer](https://docs.stripe.com/api/customers) object for each end customer.

To successfully create a subscription for the connected account to pay a
recurring fee to the platform, you must create a separate
[Customer](https://docs.stripe.com/api/customers) object to represent the
connected account.

In the gym example, the gym business uses Stripe to process one-time payments
for its gym patrons. They already created a Customer object for each gym patron,
but you need to create a different Customer object to represent the gym business
itself. Create only one Customer to represent each business entity and don’t
create a Customer to represent each owner, manager, or operator of the business.

### Create a subscription for the connected account

To create a subscription where your platform receives the funds from your
connected accounts, follow the [Subscriptions
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions) to
create a subscription with Stripe Billing. The Customer object involved in the
transaction represents the connected account, not the end customer. In our gym
example, the `CUSTOMER_ID` represents the gym business, not the gym patron.

## Enable your integration to receive event notifications

Stripe creates event notifications when changes happen in your account, like
when a recurring payment succeeds or when a payout fails. To receive these
notifications and use them to automate your integration, set up a
[webhook](https://docs.stripe.com/webhooks) endpoint. For example, you could
provision access to your service when you receive the `invoice.paid` event.

### Event notifications for Connect and subscriptions integrations

Here are the event notifications that Connect integrations typically use.

Eventdata.object
typeDescription`account.application.deauthorized``application`Occurs when a
connected account disconnects from your platform. You can use it to trigger
cleanup on your server. Available for connected accounts with access to the
Stripe Dashboard, which includes [Standard
accounts](https://docs.stripe.com/connect/standard-accounts).`account.external_account.updated`An
external account, such as `card` or `bank_account`Occurs when [a bank account or
debit card attached to a connected account is
updated](https://docs.stripe.com/connect/payouts-bank-accounts), which can
impact payouts. Available for connected accounts that your platform controls,
which includes Custom and Express accounts, and Standard accounts with [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
enabled.`account.updated``account`Allows you to monitor changes to connected
account requirements and status changes. Available for all connected
accounts.`balance.available``balance`Occurs when your Stripe balance has been
updated (for example, when [funds you’ve added from your bank
account](https://docs.stripe.com/connect/add-and-pay-out-guide#add-funds) are
available for transfer to your connected
account).`payment_intent.succeeded``payment_intent`Occurs when a payment intent
results in a successful charge. Available for all payments, including
[destination](https://docs.stripe.com/connect/collect-then-transfer-guide#fulfillment)
and [direct](https://docs.stripe.com/connect/enable-payment-acceptance-guide)
charges.`payout.failed``payout`Occurs when [a payout
fails](https://docs.stripe.com/connect/payouts-connected-accounts#webhooks).
When a payout fails, the external account involved is disabled, and no automatic
or manual payouts can be processed until the external account is
updated.`person.updated``person`If you [use the Persons
API](https://docs.stripe.com/connect/handling-api-verification#verification-process),
allows you to monitor changes to requirements and status changes for
individuals. Available for connected accounts that your platform controls, which
includes Custom and Express accounts, and Standard accounts with [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
enabled.
Here are the event notifications that subscriptions integrations typically use.

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
updated.- [Create a webhook
endpoint](https://docs.stripe.com/webhooks#webhook-endpoint-def)
- [Listen to events with the Stripe
CLI](https://docs.stripe.com/webhooks#local-listener)
- [Connect webhooks](https://docs.stripe.com/connect/webhooks)
- [Subscription
webhooks](https://docs.stripe.com/billing/subscriptions/webhooks)

## Test your integration

After you create your subscription, thoroughly test your integration before you
expose it to customers or use it for any live activity. Learn more about
[testing Stripe Billing](https://docs.stripe.com/billing/testing).

## Additional options

After you create your subscription, you can specify an
[application_fee_percent](https://docs.stripe.com/api/subscriptions/object#subscription_object-application_fee_percent),
set up the [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal), charge
your customer using the `on_behalf_of` parameter, and monitor subscriptions with
webhooks, in addition to other options.

### Collect fees on subscriptions

### Use coupons

### Use trial periods

### Set up the customer portal

### Monitor subscriptions with webhooks

### Make the connected account the settlement merchant using on_behalf_of

### Understand disconnect behavior

### Integrate tax calculation and collection

## See also

- [Creating invoices](https://docs.stripe.com/invoicing/connect)
- [Creating charges](https://docs.stripe.com/connect/charges)
- [Share customers across
accounts](https://docs.stripe.com/connect/cloning-customers-across-accounts)
- [Multiple currencies](https://docs.stripe.com/connect/currencies)

## Links

- [Connect](https://docs.stripe.com/connect)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Stripe Billing pricing](https://stripe.com/billing/pricing)
- [payouts](https://docs.stripe.com/payouts)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Prices](https://docs.stripe.com/api/prices)
- [webhooks to monitor connected account
activity](https://docs.stripe.com/connect/webhooks)
- [connected account](https://docs.stripe.com/connect/accounts)
- [pricing
model](https://docs.stripe.com/products-prices/pricing-models#flat-rate)
- [customer with the intended payment
method](https://docs.stripe.com/billing/customer#manage-customers)
- [Charge types](https://docs.stripe.com/connect/charges#types)
- [Charges](https://docs.stripe.com/api/charges/object)
- [create a subscription](https://docs.stripe.com/api#create_subscription)
- [authenticated as the connected
account](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [payment
behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
- [Payment
Elements](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#add-the-payment-element-to-your-page)
- [subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
-
[value](https://docs.stripe.com/api/subscriptions/object#subscription_object-transfer_data)
-
[application_fee_percent](https://docs.stripe.com/api/subscriptions/object#subscription_object-application_fee_percent)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Customer](https://docs.stripe.com/api/customers)
- [webhook](https://docs.stripe.com/webhooks)
- [Standard accounts](https://docs.stripe.com/connect/standard-accounts)
- [a bank account or debit card attached to a connected account is
updated](https://docs.stripe.com/connect/payouts-bank-accounts)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [funds you’ve added from your bank
account](https://docs.stripe.com/connect/add-and-pay-out-guide#add-funds)
-
[destination](https://docs.stripe.com/connect/collect-then-transfer-guide#fulfillment)
- [direct](https://docs.stripe.com/connect/enable-payment-acceptance-guide)
- [a payout
fails](https://docs.stripe.com/connect/payouts-connected-accounts#webhooks)
- [use the Persons
API](https://docs.stripe.com/connect/handling-api-verification#verification-process)
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
- [Create a webhook
endpoint](https://docs.stripe.com/webhooks#webhook-endpoint-def)
- [Listen to events with the Stripe
CLI](https://docs.stripe.com/webhooks#local-listener)
- [Subscription
webhooks](https://docs.stripe.com/billing/subscriptions/webhooks)
- [testing Stripe Billing](https://docs.stripe.com/billing/testing)
- [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
- [Creating invoices](https://docs.stripe.com/invoicing/connect)
- [Creating charges](https://docs.stripe.com/connect/charges)
- [Share customers across
accounts](https://docs.stripe.com/connect/cloning-customers-across-accounts)
- [Multiple currencies](https://docs.stripe.com/connect/currencies)