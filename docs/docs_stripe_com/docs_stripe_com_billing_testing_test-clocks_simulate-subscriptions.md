# Simulate subscriptions

## Learn how to simulate subscriptions in a sandbox or test mode.

Simulating a subscription shows you the events of a subscription, such as
invoices and renewals, that are expected over the course of the simulation time.

#### Note

When you run a simulation on a subscription, it appears in the **Test clocks**
tab of the Subscriptions page. You can delete it by clicking **Finish
simulation**. Finishing a simulation deletes all objects associated with it,
including the customer and subscription, from the sandbox or test mode. It
doesn’t affect live mode.

To simulate a subscription:

- Open the Dashboard and enable **Test mode**.
- In the [subscriptions](https://dashboard.stripe.com/test/subscriptions) page,
click the subscription to test.
- Click **Run simulation** in the banner at the top of the page.
#### Customer ineligible for simulation

The **Run simulation** button might be disabled if the subscription’s customer:

- Is attached to more than three subscriptions, including [scheduled
subscriptions](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- Has a complex profile, with many quotes, invoices or other related objects
- In the modal, set the date and time to simulate and click **Advance time**.

You can advance time by any increment, but you can only advance them two
intervals at a time from the initial frozen time. For example, if you have a
monthly subscription, you can only advance the clock up to two months at a time.

When the clock is done advancing, the banner updates and displays the clock’s
current time.

You can continue to make changes to your simulation and advance the time for
simulations like:

- Adding a [customer balance](https://docs.stripe.com/billing/customer/balance).
- Making a mid-cycle upgrade.
- [Adding one-off invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items).

Repeat as many times as you need to satisfy your test case.

## Links

- [subscriptions](https://dashboard.stripe.com/test/subscriptions)
- [scheduled
subscriptions](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [customer balance](https://docs.stripe.com/billing/customer/balance)
- [Adding one-off invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)