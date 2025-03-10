# Adds Invoice Rendering Templates for Invoices

## What’s new

Use Invoice Rendering Templates to specify rules for how invoices group and
display line items, default descriptions, footers, and custom fields. [Create
the
templates](https://docs.stripe.com/invoicing/group-line-items#create-an-invoice-rendering-template)
in the Dashboard and apply it to
[Invoices](https://docs.stripe.com/api/invoices) and
[Customers](https://docs.stripe.com/api/customers).

InvoiceRenderingTemplateresource
Template that you can apply to Invoices.

## Impact

This version lets you [configure
templates](https://docs.stripe.com/invoicing/group-line-items#create-an-invoice-rendering-template)
to apply to specific Invoices and Customers in the Dashboard or through the API.
You can use the templates to group the lines of an invoice together or provide
default descriptions, footers, and custom fields.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETChangeResourceAdded[InvoiceRenderingTemplate](https://docs.stripe.com/api/invoice-rendering-template/object)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Related changes

- [Adds retrieve and archive methods for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods)
- [Adds support for templates to Invoices and
Customers](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-parameter)
- [Adds version support for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version)

## Links

- [Create the
templates](https://docs.stripe.com/invoicing/group-line-items#create-an-invoice-rendering-template)
- [Invoices](https://docs.stripe.com/api/invoices)
- [Customers](https://docs.stripe.com/api/customers)
-
[InvoiceRenderingTemplate](https://docs.stripe.com/api/invoice-rendering-template/object)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)
- [Adds retrieve and archive methods for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods)
- [Adds support for templates to Invoices and
Customers](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-parameter)
- [Adds version support for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version)