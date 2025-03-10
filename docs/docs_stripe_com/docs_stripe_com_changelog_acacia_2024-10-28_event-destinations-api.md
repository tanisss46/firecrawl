# Adds Event Destinations v2 API endpoint

## What’s new

Adds API support for managing [event
destinations](https://docs.stripe.com/event-destinations), which let you receive
events from Stripe across multiple destination types, including [webhook
endpoints](https://docs.stripe.com/webhooks) and [Amazon
EventBridge](https://docs.stripe.com/event-destinations/eventbridge).

## Impact

You can now programmatically manage event destinations to subscribe to events.
The [Event Destinations API](https://docs.stripe.com/api/v2/event-destinations)
includes existing [webhook
endpoints](https://docs.stripe.com/api/webhook_endpoints) and offers new
configuration options:

- Send events directly to AWS using [Amazon
EventBridge](https://docs.stripe.com/event-destinations/eventbridge) as a new
type of destination.
- Use the new [thin event
payload](https://docs.stripe.com/event-destinations#thin-events) for smaller
unversioned event deliveries.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETChangeResourceAdded[V2.EventDestinations](https://docs.stripe.com/api/v2/event-destinations)
 Endpoints

ChangeResourcecreateretrieveupdatelistdeletedisableenablepingAdded[V2.EventDestinations](https://docs.stripe.com/api/v2/event-destinations)
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

- [Adds event type for updated receipt data in Issuing
transactions](https://docs.stripe.com/changelog/acacia/2024-10-28/issuing-transactions-updated-receipt-event)

## Links

- [event destinations](https://docs.stripe.com/event-destinations)
- [webhook endpoints](https://docs.stripe.com/webhooks)
- [Amazon EventBridge](https://docs.stripe.com/event-destinations/eventbridge)
- [Event Destinations API](https://docs.stripe.com/api/v2/event-destinations)
- [webhook endpoints](https://docs.stripe.com/api/webhook_endpoints)
- [thin event payload](https://docs.stripe.com/event-destinations#thin-events)
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
- [Adds event type for updated receipt data in Issuing
transactions](https://docs.stripe.com/changelog/acacia/2024-10-28/issuing-transactions-updated-receipt-event)