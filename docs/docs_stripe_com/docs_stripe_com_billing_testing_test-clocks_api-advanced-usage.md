# API and advanced usage

## Learn advanced strategies for using test clocks in the Dashboard and API.

You can create a test clock separately from a subscription for running advanced
simulations. In this scenario you create the test clock first and then add
different test cases to it.

Not ready for a full integration? See [our
guide](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions)
for running simulations on subscriptions.

![How to set a test clock to simulate subscription time
elpasing.](https://b.stripecdn.com/docs-statics-srv/assets/test-clock-lifecycle.b711b9cf4feb52351e27958b8b924cb3.png)

Test clock lifecycle

Follow these steps to start using test clocks:

- [Create a test
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock)
- [Set up your testing
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
- [Advance the clock’s
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
- [Monitor and handle the
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
- [Update the
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#update-simulation)
- [Delete the
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#delete-clock)

You can advance the clock’s time, monitor changes, and update the simulation as
often as you need to test different cases.

[Create a clock and set its
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock)
To start a simulation, create a clock and set its frozen time. The temporal
starting point for all
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
associated with this clock. You can set this to a time in the future or in the
past to test different simulations, but you can only move it forward in time
after you set it.

DashboardAPI
To create a test clock in the Dashboard, follow the steps below. Set the
Dashboard to **Test mode** to use test clocks.

- Go to the **Subscriptions**
[section](https://dashboard.stripe.com/test/subscriptions) under the **Billing**
tab.
- Click the [test clocks](https://dashboard.stripe.com/test/test-clocks) link in
the banner.
- Click **New simulation**.
- In the **Create new simulation** modal, enter a name for the simulation. You
can use this to describe the simulation you’re testing, like `Annual renewal` or
`Free trial`.
- Set the frozen time of the clock. This is the starting point for your
simulation. You can set this to a time in the future or in the past, but you can
only move it forward in time after you set it.
[Set up your
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
Next, set up the test case for your simulation. You need to create a customer
first, then a subscription for them.

DashboardAPI
To create a customer for your simulation through the Dashboard:

- Go to the [test clocks](https://dashboard.stripe.com/test/test-clocks) page
and find your test clock.
- Click **Add** > **Add customer**.

You can’t choose existing customers during test clock simulations. You can add
up to three new customers to each simulation.

You can optionally enter other [available
properties](https://docs.stripe.com/billing/customer#properties-uses) for the
customer, like their name, email, and billing information, but none are
required. For some simulations, like testing free trials, you might not want to
collect any billing information up front.

Next, you can create up to three subscriptions or subscription schedules for
your customer. To create a subscription for the customer through the Dashboard:

- Go to the [test clocks](https://dashboard.stripe.com/test/test-clocks) page
and find your test clock.
- Click **Add** > **Add subscription**. Select or search for your customer from
the drop-down menu. You can also add the customer to a subscription through the
customer page, by clicking **Actions** > **Create subscription**.
- Select a recurring product and price in the **Pricing** section.
- For the **Subscription schedule**, define the start and end date for the
subscription and when to start the billing cycle.
- Choose a payment collection method:

- Select **Automatically charge a payment method on file** if you want to charge
your customer when the billing cycle starts.
- Select **Email invoice to the customer to pay manually** if you want to
invoice your customer in arrears.
- Click **Start test subscription** to start the subscription and billing cycle.

Both the customer and subscription objects are associated with the clock object
you created in the [first
step](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock).
In the Dashboard, the icon indicates that an object is associated with a clock.

[Advance the simulated
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
After you’ve created the test clock and set up your test case, advance the
simulated time of the clock. The first time you do this, you’ll advance the time
from the initial frozen time you set at the [creation of the
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock).
As you advance time, you can see how your integration works when subscriptions
end, renew, or undergo other changes (like upgrading from a free trial to a paid
subscription).

You can advance test clocks by any increment, but you can only advance them two
intervals at a time from their initial frozen time. The length of the interval
is based on the shortest subscription interval associated with the test clock,
which is determined by the recurring price. For example, if you have a monthly
subscription, you can only advance the clock up to two months at a time. If the
test clock has no subscriptions or subscription schedules, you can advance it up
to two years from the initial frozen time.

DashboardAPI
To advance time through the Dashboard:

- Go to the [test clocks](https://dashboard.stripe.com/test/test-clocks) page
and find your test clock.
- Click **Advance time**.
- Use the calendar modal to select the date you want to advance the clock to.
- Click **Advance**.

When the clock is done advancing, the banner updates and displays the clock’s
current time.

[Monitor and handle
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
After a successful API request or Dashboard operation, the clock takes a few
seconds to advance to the specified time. To know when the clock has changed
state, you can use webhooks to listen for event notifications or you can poll
the clock. The Dashboard also reflects the changes. For example, you can go to
the [invoices page](https://dashboard.stripe.com/test/invoices) to check whether
an invoice was created or paid for your subscription.

If you use [webhooks](https://docs.stripe.com/webhooks), listen to the following
event notifications. Before production, make sure your integration correctly
handles the other [billing-specific event
notifications](https://docs.stripe.com/billing/subscriptions/webhooks) in
addition to the ones listed below.

EventDescription`test_helpers.test_clock.advancing`The clock has started to
advance but hasn’t reached the specified time.`test_helpers.test_clock.ready`The
clock has completed advancing to the specified time.
To poll the state of the clock,
[retrieve](https://docs.stripe.com/api/test_clocks/retrieve) it by ID to examine
its `status`.

```
curl https://api.stripe.com/v1/test_helpers/test_clocks/{{CLOCK_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Update the
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#update-simulation)
You can continue to make changes to your simulation and [advance the
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
for simulations like:

- Adding a [customer balance](https://docs.stripe.com/billing/customer/balance).
- Making a mid-cycle upgrade.
- [Adding one-off invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items).

After each update, [monitor the
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
again. Repeat as many times as you need to satisfy your test case.

[Delete the
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#delete-clock)
Test clocks are automatically deleted 30 days after you create them, but you can
delete them when you’re done testing to ensure a clean test environment.

DashboardAPI
To delete the clock and all of its associated test objects through the
Dashboard:

- Go to the [test clocks](https://dashboard.stripe.com/test/test-clocks) page
and find your test clock.
- Click **Finish simulation**.
- In the confirmation modal, click **Finish**.

Deleting the clock also deletes the test customers associated with the clock and
cancels their subscriptions. Test clocks are only available in test mode, so you
can’t delete any production objects when you delete a clock.

## Use cases

### Test subscription renewals

First, follow these steps to start using test clocks:

- [Create a test
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock)
- [Set up your testing
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
- [Advance the clock’s
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
- [Monitor and handle the
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
- [Update the
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#update-simulation)

Next, you can test certain subscription renewals using test clocks. Let’s say
that you’d like to test that a 50 USD/month subscription renews correctly. To
simulate this situation using test clocks:

- Create a new test clock and set its `frozen_time` to January 1.
- Add a customer and add a payment method for the customer:
DashboardAPI
To add a payment method for a customer in the Dashboard:

- From the customer account page, click **Add > Add card** from the **Payment
methods** section.
- Enter payment information. In this case, use the 4242424242424242 [test
card](https://docs.stripe.com/testing#cards).
- Click **Add card** in the modal.
- After adding a payment method for the customer, create a subscription for the
new customer set at 50 USD/month. In doing so, the invoice of 50 USD is paid
automatically and the subscription is `active`.
- Advance the date to February 1 to see that an invoice of 50 USD is created. By
default, the invoice appears in a `draft` state for [one
hour](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items).
- Advance the time by one hour to see that the invoice is finalized and paid
automatically.

### Test mid-cycle upgrades with prorations

First, follow these steps to start using test clocks:

- [Create a test
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock)
- [Set up your testing
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
- [Advance the clock’s
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
- [Monitor and handle the
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
- [Update the
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#update-simulation)

Next, you can test prorations for customers who upgrade their plans in the
middle of a billing cycle. Let’s say that you have two products. One product is
50 USD/month (‘basic plan’) and the other is 100 USD/month (‘premium plan’). In
this case, you may want to test prorations for a customer who upgrades their
‘basic plan’ to the ‘premium plan’ in the middle of a billing cycle. To simulate
this situation using test clocks:

- Create a new test clock and set its `frozen_time` to January 1.
- Create a customer and add their payment method. In this case, use the
4242424242424242 [test card](https://docs.stripe.com/testing#cards).
- Create a subscription for the ‘basic plan’ at 50 USD/month. After this is
done, you’ll see that the 50 USD/month invoice is created, finalized, and
automatically paid.
- Advance the date by two weeks. In this case, we’ll set the date to January 16.
- Upgrade the subscription to a ‘premium plan’ at 100 USD/month:
DashboardAPI
To upgrade a subscription using the Dashboard:

- From the customer account page or the subscription details page, click the
overflow menu () associated with a subscription, then select **Update
subscription**.
- Make your desired modifications.
- Click **Update subscription** in the top right corner to apply the changes.
- After upgrading the subscription, the
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
webhook event is created.
- Pending invoice items are also created for the prorations. You’ll see a
negative proration of -25 USD for the unused time with the ‘basic plan’ and a
positive proration of 50 USD for using the ‘premium plan’ for half of the
remaining month. At this point, no invoice has been generated.
- Advance the date by two weeks. In this case, we’ll set the date to February 1.
You’ll see that the subscription has cycled. An invoice has been generated in a
`draft` state and has incorporated the pending invoice items, including a
negative proration, a positive proration, and the total payment for the month of
February, resulting in 125 USD. By default, the invoice appears in a `draft`
state for around [one
hour](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items).
- To finalize the invoice, advance the time by one hour.

### Test trials

First, follow these steps to start using test clocks:

- [Create a test
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock)
- [Set up your testing
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
- [Advance the clock’s
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
- [Monitor and handle the
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
- [Update the
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#update-simulation)

Next, you can start testing trials with test clocks. Let’s say that you want
customers to try your product for free with a seven-day trial before they start
paying and want to collect payment information up front. To simulate this
situation using test clocks, follow these steps:

- Create a new test clock and set its `frozen_time` to January 1.
- Add a customer and include their payment method. In this case, use a
4242424242424242 [test card](https://docs.stripe.com/testing#cards).
- Create a subscription and add a seven-day free trial period:
DashboardAPI
To add a trial period to an existing subscription using the Dashboard:

Find the subscription you want to change.

- Click **Actions**.
- Click **Update subscription**.
- Click **Add free trial** and enter seven in **Free trial days** field.
- Click **Update subscription**.
- After creating a subscription with a seven-day free trial period, a
subscription is created in a `trialing` state. An invoice of $0.00 is generated
due to the free trial.
- Advance the date to January 5 to see the
[customer.subscription.trial_will_end](https://docs.stripe.com/api/events/types#event_types-customer.subscription.trial_will_end)
event notification. Stripe sends the notification three days before the trial
ends. You can use this webhook event to inform your customers that the trial
ends soon.
- Advance the date to January 8 to see that the subscription is now `paid` and
an invoice for 50 USD is created.
- Advance the date by one cycle (for example, to February 8 for a monthly
subscription) to see the subscription renew successfully.

## Limitations

For efficient advancement of test clocks, Stripe limits the complexity of each
simulation to:

- Three customers
- Three subscriptions, including [scheduled
subscriptions](https://docs.stripe.com/billing/subscriptions/subscription-schedules),
per customer
- Ten quotes that aren’t attached to customers

### Test clock objects omitted in list all results

Stripe list APIs (such as [List
invoices](https://docs.stripe.com/api/invoices/list)) omit results generated by
test clocks for list all requests. To see results generated by test clocks in
these cases, you must request results within a specific parent, such as
`test_clock`, `customer`, or `subscription`.

For example, `GET /v1/invoices` won’t return test clock generated invoices, but
`GET /v1/invoices/{customer_id}` returns all invoices for that customer,
including those that are test clock generated.

Similarly, you can specify a test clock ID in this example to get all invoices
related to that test clock, or you can specify a subscription ID to return all
invoices billed for that subscription, including test clock generated invoices.

### Rate limit errors

If you make multiple updates to a subscription that has a test clock, Stripe
might return a rate limit error. Since the subscription is frozen to the time of
the test clock, all API requests count toward that time, which can trigger the
rate limit.

To avoid this, advance the simulated time of the clock by a few minutes before
making additional API requests on the subscription.

### Caveats with payment processing

Test clock advancement currently doesn’t support collecting payments through
bank debits (for example, `us_bank_account` payment method types). Stripe
collects payments after the test clock advances. To test payment failures:

- Choose the **Cancel subscription after all payment retries fail** setting.
- Attach a `us_bank_account` payment method type to a customer that fails
payments.
- Create a subscription under the customer.
- Advance the test clock to cycle and collect payment on a subscription.

After the Test Clock advances, the subscription remains in the `active` state.
This indicates that the payment collection hasn’t be attempted during test clock
advancement, and the subscription has yet to enter the `canceled` state due to
`payment_failed`.

Listen to the `invoice.payment_failed` event to monitor the delayed subscription
state and invoice payment. The `customer.subscription.deleted` event indicates
that the subscription state is set to `canceled`.

## Links

- [our
guide](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [section](https://dashboard.stripe.com/test/subscriptions)
- [test clocks](https://dashboard.stripe.com/test/test-clocks)
- [available
properties](https://docs.stripe.com/billing/customer#properties-uses)
- [invoices page](https://dashboard.stripe.com/test/invoices)
- [webhooks](https://docs.stripe.com/webhooks)
- [billing-specific event
notifications](https://docs.stripe.com/billing/subscriptions/webhooks)
- [retrieve](https://docs.stripe.com/api/test_clocks/retrieve)
- [customer balance](https://docs.stripe.com/billing/customer/balance)
- [Adding one-off invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
- [test card](https://docs.stripe.com/testing#cards)
- [one
hour](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
-
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
- [Create a test
clock](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#create-clock)
- [Set up your testing
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
- [Advance the clock’s
time](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#advance-clock)
- [Monitor and handle the
changes](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
- [Update the
simulation](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage#update-simulation)
-
[customer.subscription.trial_will_end](https://docs.stripe.com/api/events/types#event_types-customer.subscription.trial_will_end)
- [scheduled
subscriptions](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [List invoices](https://docs.stripe.com/api/invoices/list)