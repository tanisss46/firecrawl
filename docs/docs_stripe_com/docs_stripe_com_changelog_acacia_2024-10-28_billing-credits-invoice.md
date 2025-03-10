# Adds support for pre-tax credit amount information to invoices

## What’s new

Adds the
[pretax_credit_amounts](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-pretax_credit_amounts)
attribute to the [Invoice Line
Item](https://docs.stripe.com/api/invoice-line-item) resource and the
[total_pretax_credit_amounts](https://docs.stripe.com/api/invoices/object#invoice_object-total_pretax_credit_amounts)
attribute to the [Invoice](https://docs.stripe.com/api/invoices) resource. These
fields contains information about [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits),
along with other pre-tax credits like discounts, that were applied to the
invoice.

## Impact

You can now see a breakdown of credits applied to an invoice before tax
calculations, including discounts. This information shows which credit notes
were issued and how they relate to the invoice.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointspretax_credit_amountsAdded[InvoiceLineitem](https://docs.stripe.com/api/invoice-line-item/object)total_pretax_credit_amountsAdded[Invoice](https://docs.stripe.com/api/invoices/object)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
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

- [Adds Credit Grant APIs and
resources](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis)
- [Adds support for pre-tax credit amount information to credit
notes](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note)

## Links

-
[pretax_credit_amounts](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-pretax_credit_amounts)
- [Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)
-
[total_pretax_credit_amounts](https://docs.stripe.com/api/invoices/object#invoice_object-total_pretax_credit_amounts)
- [Invoice](https://docs.stripe.com/api/invoices)
- [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
- [InvoiceLineitem](https://docs.stripe.com/api/invoice-line-item/object)
- [Invoice](https://docs.stripe.com/api/invoices/object)
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
- [Adds Credit Grant APIs and
resources](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis)
- [Adds support for pre-tax credit amount information to credit
notes](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note)