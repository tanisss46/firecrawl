# Adds support for bulk invoice line item operations

## What’s new

Lets you create, update, or delete invoice line items in bulk through a single
API call.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NET
 Endpoints

ChangeResourceadd_linesremove_linesupdate_linesAdded[Invoice](https://docs.stripe.com/api/invoices/object)
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

- [Adds webhook events for when an invoice is due or
overdue](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-due-date-webhooks)
- [Adds option to automatically finalize
invoices](https://docs.stripe.com/changelog/acacia/2024-09-30/automatically-finalizes-at-invoice)

## Links

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
- [Adds webhook events for when an invoice is due or
overdue](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-due-date-webhooks)
- [Adds option to automatically finalize
invoices](https://docs.stripe.com/changelog/acacia/2024-09-30/automatically-finalizes-at-invoice)