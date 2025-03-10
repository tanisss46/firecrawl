# Adds option to automatically validate customer tax location during an update

## What’s new

We’re adding `auto` as an option for
[tax.validate_location](https://docs.stripe.com/api/customers/update#update_customer-tax-validate_location)
to simplify integrating with [Stripe Tax](https://docs.stripe.com/tax). If you
try to [update a customer](https://docs.stripe.com/api/customers/update) with an
unrecognized location after the customer’s [tax location is
verified](https://docs.stripe.com/tax/customer-locations), the API returns a
`400` [validation error](https://docs.stripe.com/api/errors). Stripe recommends
setting set `tax[validate_location]="auto"` for all new Stripe Tax integrations.
(Currently, this only works for customers with [automatic tax-enabled
subscriptions](https://docs.stripe.com/tax/subscriptions#estimate-taxes-total).)

To validate customer addresses during collection, set
`tax[validate_location]="immediately"` when you [create a
customer](https://docs.stripe.com/api/customers/create).

## Impact

Helps users of 
Billing

 and 
Tax

avoid [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
errors due to invalid customer tax locations.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumautoAdded[Customer#update.tax.validate_location](https://docs.stripe.com/api/customers/update#update_customer-tax-validate_location)
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
- [Adds support for collecting retail delivery
fees](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee)

## Links

-
[tax.validate_location](https://docs.stripe.com/api/customers/update#update_customer-tax-validate_location)
- [Stripe Tax](https://docs.stripe.com/tax)
- [update a customer](https://docs.stripe.com/api/customers/update)
- [tax location is verified](https://docs.stripe.com/tax/customer-locations)
- [validation error](https://docs.stripe.com/api/errors)
- [automatic tax-enabled
subscriptions](https://docs.stripe.com/tax/subscriptions#estimate-taxes-total)
- [create a customer](https://docs.stripe.com/api/customers/create)
- [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
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
- [Adds support for collecting retail delivery
fees](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee)