# Adds support for templates to Invoices and Customers

## What’s new

Adds the template field to the [Invoice](https://docs.stripe.com/api/invoices)
and [Customer](https://docs.stripe.com/api/customers) resources.

Addedrendering.templatestring
ID of the invoice rendering template to use for this invoice.

Addedinvoice_settings.rendering_options.templatenullable string
ID of the invoice rendering template to be used for this customer’s invoices. If
set, the template will be used on all invoices for this customer unless a
template is set directly on the invoice.

## Impact

This version allows you to specify which template to apply to invoices or
invoices for specific customers.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointstemplateAdded[Customer#create.invoice_settings.rendering_options](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings-rendering_options)[Customer#update.invoice_settings.rendering_options](https://docs.stripe.com/api/customers/update#update_customer-invoice_settings-rendering_options)[Customer.invoice_settings.rendering_options](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-rendering_options)
+ 3 more
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

- [Adds Invoice Rendering Templates for
Invoices](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-resource)
- [Adds retrieve and archive methods for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods)
- [Adds version support for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version)

## Links

- [Invoice](https://docs.stripe.com/api/invoices)
- [Customer](https://docs.stripe.com/api/customers)
-
[Customer#create.invoice_settings.rendering_options](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings-rendering_options)
-
[Customer#update.invoice_settings.rendering_options](https://docs.stripe.com/api/customers/update#update_customer-invoice_settings-rendering_options)
-
[Customer.invoice_settings.rendering_options](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-rendering_options)
-
[Invoice#create.rendering](https://docs.stripe.com/api/invoices/create#create_invoice-rendering)
-
[Invoice#update.rendering](https://docs.stripe.com/api/invoices/update#update_invoice-rendering)
-
[Invoice.rendering](https://docs.stripe.com/api/invoices/object#invoice_object-rendering)
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
- [Adds Invoice Rendering Templates for
Invoices](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-resource)
- [Adds retrieve and archive methods for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods)
- [Adds version support for Invoice Rendering
Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version)