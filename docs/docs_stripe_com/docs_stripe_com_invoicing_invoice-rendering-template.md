# Invoice Rendering Templates

## Use Invoice Rendering Templates to personalize your invoice appearance for different customers

You can tailor content on your invoices for specific groups of customers.
Examples might include:

- Displaying specific text in your invoice’s footer field for customers from a
particular country
- Displaying a specific memo note for customers with a particular revenue
channel
- Grouping line items in a certain manner for customers with complex
transactions

This guide describes how you can use Invoice Templates to:

- Store and reuse common values for invoice fields instead of entering them for
every relevant invoice
- Store, manage, and update invoice field values that apply to large sets of
customers
- Configure Line Item Grouping rules, which cannot be set outside of Invoice
Templates
- For subscription invoices, customize invoice values without interacting
directly with the invoice

### Set up templates

You can create Invoice templates only in the Dashboard. You can’t create them
using the API.

- In your Billing settings, select the [Invoice templates
tab](https://dashboard.stripe.com/settings/billing/invoice-templates).
- Click **+ Create template**.
- Enter a name for your template.
- Specify values for the fields you want to include in the template. Templates
support the memo, footer, and custom fields.
- Optionally, you can [define one or more line item groups using Common
Expression Language (CEL)
expressions](https://docs.stripe.com/invoicing/group-line-items).
- To see a preview of your template, enter the ID of an applicable invoice in
the **Invoice ID** field of the Preview pane. However, any values set directly
on that invoice override the corresponding template value. For example, if that
invoice has a footer value, the preview displays the invoice’s footer, not the
template’s footer.

### Apply templates to invoices

DashboardAPI
In the Dashboard, you can apply a template to invoices in a few ways:

- In the Invoice editor
- In the Subscriptions editor, to apply to all invoices associated with the
subscription
- In a customer’s invoice settings, to apply to all future invoices associated
with that customer

### Override and update templates

You can configure invoice footer, memo, and custom field values in multiple
places. When multiple values can apply to an invoice field, they’re prioritized
in the following order, from highest to lowest:

PrioritySettingMethod1 On the invoiceDashboard or APIOn the
subscriptionDashboard only2 Template applied to the invoiceDashboard or
APITemplate applied to the subscriptionDashboard only3Template attached to the
customerDashboard or API4Invoice settings on the customerAPI only5Invoice
settings on the accountDashboard only
#### Note

Defined invoice settings always apply unless overridden by a higher-priority
setting. For example, consider a customer that has an attached invoice template.
To create a one-time invoice for that customer without using the attached
template, you must either apply a different template to the invoice or set the
invoice values directly.

When you update or replace a template, the new values apply to all future
invoices associated with the template. For example, consider a customer with an
existing subscription where the customer has an attached invoice template, and
no subscription template overrides it. If you update a value in the customer’s
template, the new value applies to future invoices for that customer’s existing
subscription.

## Links

- [Invoice templates
tab](https://dashboard.stripe.com/settings/billing/invoice-templates)
- [define one or more line item groups using Common Expression Language (CEL)
expressions](https://docs.stripe.com/invoicing/group-line-items)