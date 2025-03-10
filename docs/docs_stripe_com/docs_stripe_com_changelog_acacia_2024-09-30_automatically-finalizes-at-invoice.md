# Adds option to automatically finalize invoices

## What’s new

Adds option to automatically finalize
[Invoices](https://docs.stripe.com/api/invoices) with the
`automatically_finalizes_at`
[parameter](https://docs.stripe.com/api/invoices/object#invoice_object-automatically_finalizes_at).

Addedautomatically_finalizes_atnullable timestamp
The time when this invoice is currently scheduled to be automatically finalized.
The field will be `null` if the invoice is not scheduled to finalize in the
future. If the invoice is not in the draft state, this field will always be
`null` - see `finalized_at` for the time when an already-finalized invoice was
finalized.

## Impact

This enables you to understand when invoices will finalize and to automatically
advance them.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsautomatically_finalizes_atAdded[Invoice](https://docs.stripe.com/api/invoices/object)
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

- [Adds support for bulk invoice line item
operations](https://docs.stripe.com/changelog/acacia/2024-09-30/invoicing-bulk-line-item-operations)
- [Adds webhook events for when an invoice is due or
overdue](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-due-date-webhooks)

## Links

- [Invoices](https://docs.stripe.com/api/invoices)
-
[parameter](https://docs.stripe.com/api/invoices/object#invoice_object-automatically_finalizes_at)
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
- [Adds support for bulk invoice line item
operations](https://docs.stripe.com/changelog/acacia/2024-09-30/invoicing-bulk-line-item-operations)
- [Adds webhook events for when an invoice is due or
overdue](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-due-date-webhooks)