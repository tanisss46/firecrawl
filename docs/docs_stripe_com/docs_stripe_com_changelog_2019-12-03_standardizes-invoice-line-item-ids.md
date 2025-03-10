# Standardizes invoice line item IDsBreaking changes

## What’s new

Changes the
[id](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-id)
field of all invoice line items, prefixing them with `il_`. The new ID has
consistent prefixes across all line items, is globally unique, and can be used
for pagination. Old prefixes included `sub_`, `su_`, `item_`, `sli_`, and `ii_`
and weren`t globally unique.

- You can no longer use the prefix of the ID to determine the source of the line
item. Instead use the `type` field for this purpose.
- For lines with `type=invoiceitem`, use the `invoice_item` field to reference
or update the originating `Invoice Item` object.
- On earlier API versions, the `Invoice Line Item` object also has a `unique_id`
field that you can use to migrate internal references before upgrading to this
version.
- When [setting a tax rate to individual line
items](https://docs.stripe.com/invoicing/taxes/tax-rates#setting-tax-rates-on-individual-items),
use the new `id`. If you’re on an earlier API version, pass in either a line
item `id` or `unique_id`.

## Impact

Lets you work with a more consistent and globally unique invoice line item ID
format. The new IDs are prefixed with “il_” instead of various legacy prefixes,
providing a standardized approach across all line items.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-12-03`
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

## Links

-
[id](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-id)
- [setting a tax rate to individual line
items](https://docs.stripe.com/invoicing/taxes/tax-rates#setting-tax-rates-on-individual-items)
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