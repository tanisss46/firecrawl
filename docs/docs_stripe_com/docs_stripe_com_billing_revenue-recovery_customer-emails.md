# Automate customer emails

## Learn how you can use customer emails to recover revenue.

Customer emails help prevent involuntary churn by notifying customers and giving
them a chance to intervene when churn is likely, like when a payment fails.

Enable email notifications for all the use cases that make sense for your
business. We recommend you minimally provide a way for customers to:

- [Confirm
payments](https://docs.stripe.com/billing/revenue-recovery/customer-emails#payment-confirmation-notifications)
- [Correct failed
payments](https://docs.stripe.com/billing/revenue-recovery/customer-emails#failed-payment-notifications)

## Configure emails

You can turn on customer emails in your [subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic) Dashboard
without writing any code. All of these emails and hosted pages use your
[branding settings](https://dashboard.stripe.com/settings/branding).

Emails for the following notification types include a link to a page where the
customer can update their payment method.

- Payment confirmation notifications
- Failed payment notifications
- Trial ending reminders
- Renewal reminders
- Expiring card notifications

You can set the link destination to your own custom link or [a Stripe-hosted
page](https://docs.stripe.com/billing/revenue-recovery/customer-emails#link-to-a-stripe-hosted-page).
If you **Use your own custom link** and don’t provide a URL, we use your
business website.

## Failed payment notifications

Notify your customers about failed payments for subscriptions to encourage them
to resolve the reason for failure, such as an expired card. Enable **Send emails
when card payments fail** in the [revenue recovery
settings](https://dashboard.stripe.com/revenue_recovery/emails) page.

When you enable this setting, Stripe automatically sends an email to your
customer after each failed payment. The email lets your customer know that their
recent subscription payment failed and gives them the opportunity to update
their payment method so it can be retried successfully.

## Unpaid recurring invoice reminders

To send reminder emails about unpaid invoices, enable **Send reminders if a
recurring invoice hasn’t been paid** in the [billing settings
page](https://dashboard.stripe.com/settings/billing/automatic), in the **Manage
invoices sent to customers** section.

This sends payment reminders for recurring invoices with a collection method of
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
on the configured schedule.

## Trial ending reminders

Under [Manage free trial
messaging](https://dashboard.stripe.com/settings/billing/automatic), turn on
**Send a reminder email 7 days before a free trial ends** to send a trial ending
reminder.

When the trial ends without a payment method and the subscription is paused,
customers can activate the subscription on the hosted page. They can add a
payment method to activate the subscription and pay the first invoice.

## Renewal reminders

Under [Prevent failed
payments](https://dashboard.stripe.com/settings/billing/automatic), turn on
**Send emails about upcoming renewals**.

Stripe sends this email before the current renewal period ends based on the days
configured in the **Upcoming renewal events** section.

The renewal date in the email uses the customer’s timezone. If the customer’s
timezone isn’t defined, it uses the timezone set in your [account
settings](https://dashboard.stripe.com/settings/account). Otherwise, it defaults
to UTC.

## Payment confirmation notifications

Some payments might require manual customer intervention, like those that use
[3D Secure](https://docs.stripe.com/payments/3d-secure) or the
[Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment) payment
method. You can [manage payments that require
confirmation](https://dashboard.stripe.com/settings/billing/automatic) in the
Dashboard.

- To automatically send an email to your customer when their payment requires
confirmation, enable **Send a Stripe-hosted link for customers to confirm their
payments when required**. The email includes a link to a Stripe-hosted page
where your customer can confirm the payment.
- To continue sending emails until your customer confirms the payment or it
expires, enable **Send reminders if payment confirmation isn’t completed**. You
can customize the intervals at which Stripe sends these reminders. Each reminder
includes a link similar to the original email where the customer can confirm the
payment.

## Expiring card notifications

Under [Prevent failed
payments](https://dashboard.stripe.com/revenue_recovery/emails), turn on **Send
emails about expiring cards**.

This automatically sends an email 1 month before your customer’s card on file
expires.

## Link to a Stripe-hosted page

With the **Link to a Stripe-hosted page** option, Stripe provides a secure,
private URL to a Stripe-hosted page in the email. Stripe doesn’t include a link
to the Stripe-hosted page if the subscription is set to manually send an
invoice.

On that page, your customer can update their payment method for the relevant
subscription and pay any outstanding invoices if applicable. Otherwise, the new
payment method is used the next time a scheduled payment is attempted.

How a customer updates their payment method on the Stripe-hosted page.

Any of the following conditions invalidate the link to the hosted payment page:

- It’s been 30 days since we sent the trial ending email.
- The [subscription
status](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses)
changes to `cancelled`, `incomplete_expired`, or `unpaid`.
- The trial ended and the customer already provided a payment method for the
subscription.
- The subscription’s current renewal period expired.

## Test your configuration

In [test mode](https://docs.stripe.com/test-mode), Stripe doesn’t automatically
send customer emails. To test your customer email settings, use email addresses
that belong to your verified [email
domain](https://dashboard.stripe.com/settings/emails) or an active [team
member](https://dashboard.stripe.com/settings/team). If a test mode customer’s
email matches either of those conditions, Stripe sends failed payment
notifications, upcoming invoice reminders, trial ending reminders, and card
expiring reminders in test mode.

## Email logs

You can find logs for emails sent within the last 30 days on the
[customer](https://dashboard.stripe.com/customers) page. The logs are updated
daily, so they don’t include emails from the current date.

We log the following types of email notifications:

- Failed payment attempts.
- Finalized invoices.
- Receipts for paid invoices.
- Payments requiring 3D Secure.
- Expiring cards on file.
- Unpaid one-off invoices.
- Created credit notes.
- Issued refunds.
- Ending subscription trials.
- Canceled subscriptions.

## Links

- [subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [branding settings](https://dashboard.stripe.com/settings/branding)
- [revenue recovery
settings](https://dashboard.stripe.com/revenue_recovery/emails)
-
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [account settings](https://dashboard.stripe.com/settings/account)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment)
- [subscription
status](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses)
- [test mode](https://docs.stripe.com/test-mode)
- [email domain](https://dashboard.stripe.com/settings/emails)
- [team member](https://dashboard.stripe.com/settings/team)
- [customer](https://dashboard.stripe.com/customers)