# Automation recipes

## View example recipes for common automations.

In this guide, we provide popular automation recipes to give you an idea of how
to use automations in different scenarios. To get an overview of the different
triggers, filter conditions, and actions available, see
[Automations](https://docs.stripe.com/billing/automations).

## Custom dunning flow for annual subscribers

Increase your recovery rate by customizing dunning behavior based on billing
interval, invoice amount, or customer segment. For example, you might want to
grant longer grace periods to annual or high-value customers, or retry more
frequently for a specific customer segment.

To customize automations:

- Click **New automation**.
- Give the automation a descriptive name, such as “Annual subscriber dunning.”
- Select the **Subscription payment fails** as the trigger.
- (Optional) Choose the conditions that must be met for the automation to run.
In this case, Subscription interval is: **yearly**.
- Add the **Start retry policy** action, and select **+ Create new retry
policy** in the dropdown. Choose **Smart Retries for subscriptions** and retry
up to **8 times** within **2 months**.
- (Optional) Add a delay of 7 days as an additional grace period for manual
outreach.
- Add the **Cancel subscription** action.
- Add the **Mark invoice uncollectible** action (which makes it a write-off for
[Revenue
Recognition](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing#uncollectible-invoices)).

## Notify your team when high value invoices are overdue

To improve cash flow and customer communications, keep track of high-value
unpaid invoices. This recipe automates notifications for high-value invoices,
enabling your team to take proactive measures to encourage the customer to pay
the outstanding invoice.

To implement these notifications:

- Click **New automation**.
- Give the automation a descriptive name, such as “Notify Collections team of
high-value late invoices.”
- Select the **Invoice is overdue** as the trigger.
- Add a filter condition to select invoices **greater than** **$500**.
- Add a **Send email** action and select a recipient using the company email
domain.
- Write a short memo such as “Invoice over $500 is overdue by X days” in the
memo field.

Modify this recipe to meet your specific business needs, such as adjusting the
overdue dollar amount and length of overdue period. The recipient must use the
company email domain or be a user on the Stripe account.

## Email a confirmation when a subscription is canceled

To enhance customer communication, automatically send subscribers a confirmation
email when their subscription is canceled.

Sending the confirmation email doesn’t prevent churn, but it can help to
maintain a positive customer relationship and provide an opportunity to gather
the cancellation reason, which allows you to further improve your service.

To set up this recipe with automations:

- Click **New automation**.
- Give the automation a descriptive name, such as “Subscription cancellation
confirmation.”
- Select the **Subscription is canceled** as the trigger.
- (Optional) Add a filter condition to restrict the automation by customer
segment, subscription product or plan, or subscription amount.
- Select the **Send email to customer** action.
- Stripe provides a predefined email template for the confirmation email. The
email includes the subscription details and confirms the cancellation date. You
also have the option to include a link to a cancellation reason survey.

## Give new users a spend credit at signup

Businesses with usage based pricing models can give new users a spend credit to
get started. This can lower the barrier to entry for new users trying your
products by helping reduce friction to sign up and increase activation rates.

To set this recipe with automations:

- Click **New automation**.
- Give the automation a descriptive name, such as “New customer spend credit.”
- Select **Customer is created** as the trigger.
- (Optional) Select the **Create a subscription** action.
- Select the **Credit customer balance** action.
- At the prompt, enter the amount of the credit.

Modify this recipe to meet your specific needs, such as adjusting the dollar
amount of the credit adjustment and whether you want to create a subscription
for this new customer.

## Links

- [Automations](https://docs.stripe.com/billing/automations)
- [Revenue
Recognition](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing#uncollectible-invoices)