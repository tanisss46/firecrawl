# Adds Credit Grant APIs and resources

## What’s new

Adds new API for managing [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits).
You can use these APIs to allocate prepaid or promotional credits to customers
which can then be drawn down using subscription invoices for billing meter
prices.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETChangeResourcesAdded[Billing.CreditBalanceSummary](https://docs.stripe.com/api/billing/credit-balance-summary/object)[Billing.CreditBalanceTransaction](https://docs.stripe.com/api/billing/credit-balance-transaction/object)[Billing.CreditGrant](https://docs.stripe.com/api/billing/credit-grant)
 Endpoints

ChangeResourcesretrieveAdded[CreditBalanceSummary](https://docs.stripe.com/api/billing/credit-balance-summary/object)listretrieveAdded[CreditBalanceTransaction](https://docs.stripe.com/api/billing/credit-balance-transaction/object)createexpirelistretrieveupdatevoid_grantAdded[CreditGrant](https://docs.stripe.com/api/billing/credit-grant)
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

- [Adds support for pre-tax credit amount information to
invoices](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice)
- [Adds support for pre-tax credit amount information to credit
notes](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note)

## Links

- [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
-
[Billing.CreditBalanceSummary](https://docs.stripe.com/api/billing/credit-balance-summary/object)
-
[Billing.CreditBalanceTransaction](https://docs.stripe.com/api/billing/credit-balance-transaction/object)
- [Billing.CreditGrant](https://docs.stripe.com/api/billing/credit-grant)
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
- [Adds support for pre-tax credit amount information to
invoices](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice)
- [Adds support for pre-tax credit amount information to credit
notes](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note)