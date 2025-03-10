# Adds event type for updated receipt data in Issuing transactions

## What’s new

Adds
[issuing_transaction.purchase_details_receipt_updated](https://docs.stripe.com/api/events/types#event_types-issuing_transaction.purchase_details_receipt_updated)
to the list of [event types](https://docs.stripe.com/api/events/types) you can
listen to with a [webhook endpoint](https://docs.stripe.com/webhooks).

Listen for the `issuing_transaction.purchase_details_receipt_updated` event to
get notifications when the
[receipt](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-purchase_details-receipt)
data of an Issuing
[Transaction](https://docs.stripe.com/api/issuing/transactions) is updated.

## Impact

You no longer have to poll the
[Transaction](https://docs.stripe.com/api/issuing/transactions) endpoint to get
all the data you need about Issuing Transactions.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsissuing_transaction.purchase_details_receipt_updatedAdded[Event.type](https://docs.stripe.com/api/events/object#event_object-type)[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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

- [Adds Event Destinations v2 API
endpoint](https://docs.stripe.com/changelog/acacia/2024-10-28/event-destinations-api)

## Links

-
[issuing_transaction.purchase_details_receipt_updated](https://docs.stripe.com/api/events/types#event_types-issuing_transaction.purchase_details_receipt_updated)
- [event types](https://docs.stripe.com/api/events/types)
- [webhook endpoint](https://docs.stripe.com/webhooks)
-
[receipt](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-purchase_details-receipt)
- [Transaction](https://docs.stripe.com/api/issuing/transactions)
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
- [Adds Event Destinations v2 API
endpoint](https://docs.stripe.com/changelog/acacia/2024-10-28/event-destinations-api)