# Adds created, updated, and failed events for all refund types

## What’s new

The following events now apply to all types of
[refunds](https://docs.stripe.com/refunds), including those without a
corresponding charge.

-
[refund.created](https://docs.stripe.com/api/events/types#event_types-refund.created)
-
[refund.updated](https://docs.stripe.com/api/events/types#event_types-refund.updated)
-
[refund.failed](https://docs.stripe.com/api/events/types#event_types-refund.failed)

Previously, these events were only sent for refunds without a corresponding
charge.

## Impact

Previously, you couldn’t find refund details in the
[charge.refunded](https://docs.stripe.com/api/events/types#event_types-charge.refunded)
event, which was sent after you [created a
refund](https://docs.stripe.com/api/refunds/create). You can now listen to the
[refund.created](https://docs.stripe.com/api/events/types#event_types-refund.created)
event to get details about the refund, and don’t need to make an extra API call
to get the refund ID.

This change also improves the consistency of [event
types](https://docs.stripe.com/api/events/types) created for all refunds. You
don’t need to listen to separate [refund-related
events](https://docs.stripe.com/refunds?dashboard-or-api=api#refund-events) (for
example,
[charge.refunded](https://docs.stripe.com/api/events/types#event_types-charge.refunded))
depending on whether the refund has a charge or not.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValuesChangeEnumsrefund.createdrefund.updatedrefund.failedAdded[Event.type](https://docs.stripe.com/api/events/object#event_object-type)[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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

## Links

- [refunds](https://docs.stripe.com/refunds)
-
[refund.created](https://docs.stripe.com/api/events/types#event_types-refund.created)
-
[refund.updated](https://docs.stripe.com/api/events/types#event_types-refund.updated)
-
[refund.failed](https://docs.stripe.com/api/events/types#event_types-refund.failed)
-
[charge.refunded](https://docs.stripe.com/api/events/types#event_types-charge.refunded)
- [created a refund](https://docs.stripe.com/api/refunds/create)
- [event types](https://docs.stripe.com/api/events/types)
- [refund-related
events](https://docs.stripe.com/refunds?dashboard-or-api=api#refund-events)
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