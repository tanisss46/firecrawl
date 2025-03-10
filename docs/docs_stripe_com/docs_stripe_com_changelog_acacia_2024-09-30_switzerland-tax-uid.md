# Adds Switzerland UID as a supported customer tax ID

## What’s new

Adds Switzerland’s UID number, CH UID (`ch_uid`), to the list of [supported
customer tax
IDs](https://docs.stripe.com/billing/customer/tax-ids#supported-tax-id).

## Impact

When you create or update a [Customer](https://docs.stripe.com/api/customers),
you can now select CH UID or CH VAT, the previously supported VAT number.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsch_uidAdded[Checkout.Session.customer_details.tax_ids[].type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids-type)[Customer#create.tax_id_data[].type](https://docs.stripe.com/api/customers/create#create_customer-tax_id_data-type)[Invoice.customer_tax_ids[].type](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids-type)
+ 8 more
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

- [Adds Croatian Personal Identification Number to supported Tax
IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number)
- [Adds support for requiring a customer tax ID on Checkout and Payment
Links](https://docs.stripe.com/changelog/acacia/2024-09-30/requiring-customer-tax-id-checkout-session-paymentlink)

## Links

- [supported customer tax
IDs](https://docs.stripe.com/billing/customer/tax-ids#supported-tax-id)
- [Customer](https://docs.stripe.com/api/customers)
-
[Checkout.Session.customer_details.tax_ids[].type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids-type)
-
[Customer#create.tax_id_data[].type](https://docs.stripe.com/api/customers/create#create_customer-tax_id_data-type)
-
[Invoice.customer_tax_ids[].type](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids-type)
-
[Invoice#create_preview.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-customer_details-tax_ids-type)
-
[Invoice#upcoming.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/upcoming#upcoming_invoice-customer_details-tax_ids-type)
-
[Invoice#upcomingLines.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoice-line-item/invoices/upcoming/lines/retrieve#upcoming_invoice_lines-customer_details-tax_ids-type)
-
[Tax.Calculation.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-customer_details-tax_ids-type)
-
[Tax.Calculation#create.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/calculations/create#calculate_tax-customer_details-tax_ids-type)
-
[Tax.Transaction.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/transactions/object#tax_transaction_object-customer_details-tax_ids-type)
- [TaxId.type](https://docs.stripe.com/api/tax_ids/object#tax_id_object-type)
-
[TaxId#create.type](https://docs.stripe.com/api/tax_ids/create#create_tax_id-type)
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
- [Adds Croatian Personal Identification Number to supported Tax
IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number)
- [Adds support for requiring a customer tax ID on Checkout and Payment
Links](https://docs.stripe.com/changelog/acacia/2024-09-30/requiring-customer-tax-id-checkout-session-paymentlink)