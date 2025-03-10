# Adds support for tax ID types in 19 new countries

## What’s new

Adds support for new tax ID types for Albania, Angola, Armenia, Bahamas,
Barbados, Bosnia and Herzegovina, Cambodia, Congo (DR), Guinea, Mauritania,
Montenegro, Nepal, North Macedonia, Senegal, Suriname, Tajikistan, Uganda,
Zambia and Zimbabwe across various Stripe API endpoints and objects.

## Impact

This change lets you collect, store, and process tax ID types for customers in
Albania, Angola, Armenia, Bahamas, Barbados, Bosnia and Herzegovina, Cambodia,
Congo (DR), Guinea, Mauritania, Montenegro, Nepal, North Macedonia, Senegal,
Suriname, Tajikistan, Uganda, Zambia and Zimbabwe.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValuesChangeEnumsam_tinao_tinba_tinbb_tinbs_tincd_nifgn_nifkh_tinme_pibmk_vatmr_nifnp_pansn_nineasr_fintj_tinug_tinzm_tinzw_tinAdded[Checkout.Session.customer_details.tax_ids[].type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids-type)[Invoice.customer_tax_ids[].type](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids-type)[Tax.Calculation.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-customer_details-tax_ids-type)
+ 2
moream_tinao_tinba_tinbb_tinbs_tincd_nifgn_nifkh_tinme_pibmk_vatmr_nifnp_pansn_nineasr_fintj_tinug_tinzm_tinzw_tinAdded[Customer#create.tax_id_data[].type](https://docs.stripe.com/api/customers/create#create_customer-tax_id_data-type)[Invoice#create_preview.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-customer_details-tax_ids-type)[Invoice#upcoming.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/upcoming#upcoming_invoice-customer_details-tax_ids-type)
+ 3
moreal_tinAdded[Checkout.Session.customer_details.tax_ids[].type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids-type)[Invoice.customer_tax_ids[].type](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids-type)[Tax.Calculation.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-customer_details-tax_ids-type)
+ 2
moreal_tinAdded[Customer#create.tax_id_data[].type](https://docs.stripe.com/api/customers/create#create_customer-tax_id_data-type)[Invoice#create_preview.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-customer_details-tax_ids-type)[Invoice#upcoming.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/upcoming#upcoming_invoice-customer_details-tax_ids-type)
+ 3 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-12-18.acacia`
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

- [Adds disabled reason to invoices, subscriptions, and
schedules](https://docs.stripe.com/changelog/acacia/2024-12-18/add-disabled-reason)
- [Adds support for 21 new countries to the Tax Registration
API](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries)

## Links

-
[Checkout.Session.customer_details.tax_ids[].type](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-tax_ids-type)
-
[Invoice.customer_tax_ids[].type](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids-type)
-
[Tax.Calculation.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-customer_details-tax_ids-type)
-
[Tax.Transaction.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/transactions/object#tax_transaction_object-customer_details-tax_ids-type)
- [TaxId.type](https://docs.stripe.com/api/tax_ids/object#tax_id_object-type)
-
[Customer#create.tax_id_data[].type](https://docs.stripe.com/api/customers/create#create_customer-tax_id_data-type)
-
[Invoice#create_preview.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-customer_details-tax_ids-type)
-
[Invoice#upcoming.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoices/upcoming#upcoming_invoice-customer_details-tax_ids-type)
-
[Invoice#upcomingLines.customer_details.tax_ids[].type](https://docs.stripe.com/api/invoice-line-item/invoices/upcoming/lines/retrieve#upcoming_invoice_lines-customer_details-tax_ids-type)
-
[Tax.Calculation#create.customer_details.tax_ids[].type](https://docs.stripe.com/api/tax/calculations/create#calculate_tax-customer_details-tax_ids-type)
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
- [Adds disabled reason to invoices, subscriptions, and
schedules](https://docs.stripe.com/changelog/acacia/2024-12-18/add-disabled-reason)
- [Adds support for 21 new countries to the Tax Registration
API](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries)