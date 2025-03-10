# Adds support for collecting retail delivery fees

## What’s new

This change has two parts:

- Adds `retail_delivery_fee` to the list of possible enum values for
[tax_type](https://docs.stripe.com/api/tax_rates/update#update_tax_rate-tax_type)
in the [Tax Rate](https://docs.stripe.com/api/tax_rates) resource. This makes it
possible to represent retail delivery fees in
[Minnesota](https://docs.stripe.com/tax/supported-countries/united-states/minnesota)
and
[Colorado](https://docs.stripe.com/tax/supported-countries/united-states/colorado).
- Extends
[tax_rate_details](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_breakdown-tax_rate_details)
for [Tax Calculations](https://docs.stripe.com/api/tax/calculations) to
represent flat amount tax rates.

## Impact

Lets you accurately collect taxes when selling tangible personal property in
[Minnesota](https://docs.stripe.com/tax/supported-countries/united-states/minnesota)
and
[Colorado](https://docs.stripe.com/tax/supported-countries/united-states/colorado).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsflat_amountrate_typeAdded[Tax.Calculation.tax_breakdown[].tax_rate_details](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_breakdown-tax_rate_details)[TaxRate](https://docs.stripe.com/api/tax_rates/object)ValueChangeEnumsretail_delivery_feeAdded[Invoice#add_lines.lines[].tax_amounts[].tax_rate_data.tax_type](https://docs.stripe.com/api/invoice-line-item/bulk#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type)[Invoice#update_lines.lines[].tax_amounts[].tax_rate_data.tax_type](https://docs.stripe.com/api/invoice-line-item/invoices/update-lines/bulk#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type)[Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type)
+ 5 more
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

- [Adds support for new countries to the Tax Registration
API](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-registration-new-countries)
- [Adds support for tax ID types in several new
countries](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-ids)
- [Adds option to automatically validate customer tax location during an
update](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto)

## Links

-
[tax_type](https://docs.stripe.com/api/tax_rates/update#update_tax_rate-tax_type)
- [Tax Rate](https://docs.stripe.com/api/tax_rates)
-
[Minnesota](https://docs.stripe.com/tax/supported-countries/united-states/minnesota)
-
[Colorado](https://docs.stripe.com/tax/supported-countries/united-states/colorado)
-
[tax_rate_details](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_breakdown-tax_rate_details)
- [Tax Calculations](https://docs.stripe.com/api/tax/calculations)
- [TaxRate](https://docs.stripe.com/api/tax_rates/object)
-
[Invoice#add_lines.lines[].tax_amounts[].tax_rate_data.tax_type](https://docs.stripe.com/api/invoice-line-item/bulk#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type)
-
[Invoice#update_lines.lines[].tax_amounts[].tax_rate_data.tax_type](https://docs.stripe.com/api/invoice-line-item/invoices/update-lines/bulk#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type)
-
[Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type)
-
[Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type)
-
[Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type)
-
[TaxRate#create.tax_type](https://docs.stripe.com/api/tax_rates/create#create_tax_rate-tax_type)
-
[TaxRate.tax_type](https://docs.stripe.com/api/tax_rates/object#tax_rate_object-tax_type)
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
- [Adds support for new countries to the Tax Registration
API](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-registration-new-countries)
- [Adds support for tax ID types in several new
countries](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-ids)
- [Adds option to automatically validate customer tax location during an
update](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto)