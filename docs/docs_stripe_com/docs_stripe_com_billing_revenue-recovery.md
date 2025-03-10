# Revenue recovery

## Learn about automated recovery features that reduce and recover failed subscription payments.

Prevent lost revenue and reduce churn with Stripe’s revenue recovery features.
These automated tools make sure you don’t lose revenue to failed payments or
missed trial conversions. None of the features require you to write code, so you
can start recovering revenue today.

#### Recovering one-off invoices

This page describes recovery features for
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
other recurring revenue. Learn more about setting up [automatic
collection](https://docs.stripe.com/invoicing/automatic-collection) and recovery
for one-off [invoices](https://docs.stripe.com/billing/subscriptions/creating).

## Revenue recovery features

Stripe provides a full tool set to help you recover recurring revenue:

[Recovery analyticsAnalyze subscription payment failure rates, recovery rates,
and recent failed payments for top
customers.](https://docs.stripe.com/billing/revenue-recovery/recovery-analytics)[Smart
RetriesAutomatically retry failed payments to prevent involuntary churn due to
temporary
issues.](https://docs.stripe.com/billing/revenue-recovery/smart-retries)[Email
notificationsAutomatically send emails to customers when a payment fails, a card
expires, or a payment method requires an
update.](https://docs.stripe.com/billing/revenue-recovery/customer-emails)[No
code AutomationsImplement your own custom recovery logic without writing
code.](https://docs.stripe.com/billing/automations)[Automatic card updatesStripe
automatically updates your customer’s card information when they get a new card
number.](https://docs.stripe.com/payments/cards/overview#automatic-card-updates)
## Recurring revenue recovery options

Stripe recommends including the following recurring revenue recovery options in
your integration. As you complete each item, check it off. Your browser’s cache
stores the state of each checkbox so you can refer back to this page to see what
you’ve completed so far.

- Set up failed payment retries
Retrying failed payments is one of the most effective ways to recover revenue.
It requires no manual intervention from you or the customer.

You can set up Smart Retries and custom retry schedules in the Stripe Dashboard
without writing any code. Smart Retries use data points to find the best time to
retry the payment and are more effective than scheduled retries.

- [Automate payment
retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries)
- Set up automatic customer emails
Set up automated customer emails to notify customers of possible issues. You can
enable these based on your business’s use cases. Many businesses use failed
payment and 3D Secure emails to help customers immediately fix failing payments.

- [Automate customer
emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails).
- Set up automations
You can set up more automations for custom logic and revenue recovery without
writing code, including workflows such as:

- [Custom dunning flow for annual
subscribers](https://docs.stripe.com/billing/automation-recipes#custom-dunning-flow)
- [Notify your team when high value invoices are
overdue](https://docs.stripe.com/billing/automation-recipes#invoice-overdue-notifications)
- [Email a confirmation when a subscription is
canceled](https://docs.stripe.com/billing/automation-recipes#subscription-cancellation-confirmation)
- [Automation recipes](https://docs.stripe.com/billing/automation-recipes)
- [Automations](https://docs.stripe.com/billing/automations)

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [automatic collection](https://docs.stripe.com/invoicing/automatic-collection)
- [Recovery analyticsAnalyze subscription payment failure rates, recovery rates,
and recent failed payments for top
customers.](https://docs.stripe.com/billing/revenue-recovery/recovery-analytics)
- [Smart RetriesAutomatically retry failed payments to prevent involuntary churn
due to temporary
issues.](https://docs.stripe.com/billing/revenue-recovery/smart-retries)
- [Email notificationsAutomatically send emails to customers when a payment
fails, a card expires, or a payment method requires an
update.](https://docs.stripe.com/billing/revenue-recovery/customer-emails)
- [No code AutomationsImplement your own custom recovery logic without writing
code.](https://docs.stripe.com/billing/automations)
- [Automatic card updatesStripe automatically updates your customer’s card
information when they get a new card
number.](https://docs.stripe.com/payments/cards/overview#automatic-card-updates)
- [Custom dunning flow for annual
subscribers](https://docs.stripe.com/billing/automation-recipes#custom-dunning-flow)
- [Notify your team when high value invoices are
overdue](https://docs.stripe.com/billing/automation-recipes#invoice-overdue-notifications)
- [Email a confirmation when a subscription is
canceled](https://docs.stripe.com/billing/automation-recipes#subscription-cancellation-confirmation)
- [Automation recipes](https://docs.stripe.com/billing/automation-recipes)