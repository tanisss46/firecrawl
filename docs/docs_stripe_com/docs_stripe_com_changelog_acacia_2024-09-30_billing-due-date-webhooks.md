# Adds webhook events for when an invoice is due or overdue

## What’s new

Adds two new webhook events emitted by [custom
automations](https://docs.stripe.com/billing/automations). You can now set up an
automation to send `invoice.overdue` or `invoice.will_be_due` events based on
custom conditions or a schedule.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValuesChangeEnumsinvoice.overdueinvoice.will_be_dueAdded[Event.type](https://docs.stripe.com/api/events/object#event_object-type)[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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
- [Adds option to automatically finalize
invoices](https://docs.stripe.com/changelog/acacia/2024-09-30/automatically-finalizes-at-invoice)

## Links

- [custom automations](https://docs.stripe.com/billing/automations)
- [Event.type](https://docs.stripe.com/api/events/object#event_object-type)
-
[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)
-
[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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
- [Adds option to automatically finalize
invoices](https://docs.stripe.com/changelog/acacia/2024-09-30/automatically-finalizes-at-invoice)