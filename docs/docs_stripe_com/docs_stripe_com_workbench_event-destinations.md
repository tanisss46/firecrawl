# Manage event destinations

## Use Workbench to set up event destinations and receive events from Stripe.

This guide describes how to set up an event destination using Workbench.

For an overview and best practices on receiving events about your Stripe
account, read the [events guide](https://docs.stripe.com/event-destinations).

## Create a new event destination

You can create new event destinations for webhook endpoints and AWS EventBridge
destinations.

- Open the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench.
- Click **Create new destination**.
- Select the API version for the [events
object](https://docs.stripe.com/api/events) you want to consume.
- If you’re using [Connect](https://docs.stripe.com/connect), you can listen for
**Events on connected accounts**. Otherwise, choose **Events on your account**.
- Select the [event types](https://docs.stripe.com/api/events/types) that you
want to send to the destination, then click **Continue**.
- Select **Webhook** to send events to an HTTPS endpoint.
- Provide the **Endpoint URL** for Stripe to send webhooks to and an optional
description for the endpoint.
- Click **Create destination** to create your webhook endpoint.

![Register a new webhook endpoint in the Webhooks
tab](https://b.stripecdn.com/docs-statics-srv/assets/create-webhook-endpoint.92271ebcb6d3c1f936baaeeda36feafc.png)

## Configure an existing event destination

You can update or delete existing event destinations in the
[Webhooks](https://dashboard.stripe.com/webhooks) tab. You can also temporarily
disable a destination. Stripe won’t attempt to resend any events generated while
the destination is disabled. Additionally, you can [manage event
destinations](https://docs.stripe.com/api/v2/core/event_destinations)
programmatically.

## View event deliveries

To view event deliveries:

- Open the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench.
- Select the event destination.
- Click the **Event deliveries** tab.

The **Event deliveries** tab provides a list of events and whether they’re
Delivered, Pending, or Failed. Click an event to view the **Delivery attempts**,
which includes the HTTP status code of previous delivery attempts and the time
of pending future deliveries.

![View event delivery attempts on a webhook endpoint's Event deliveries
tab](https://b.stripecdn.com/docs-statics-srv/assets/view-event-deliveries.375483a863ab143a0e92f01fa01c14b0.png)

View event delivery attempts on a webhook endpoint’s **Event deliveries** tab.

## Retry sending an event

In live mode, Stripe attempts to deliver a given event to your webhook endpoint
for up to 3 days with an exponential back off. In the **Event deliveries**
section of your webhook endpoint listed on Workbench, you can view when the next
retry will occur.

In test mode, Stripe retries three times over a few hours. You can manually
retry transmitting individual events to your webhook endpoint after this time
using the Workbench **Webhooks** tab by navigating to the **Event deliveries**
listed for your desired endpoint. You can also [query for missed
events](https://docs.stripe.com/api/events/list) to reconcile the data over any
time period.

![Retry sending events using a webhook endpoint's Event deliveries
tab](https://b.stripecdn.com/docs-statics-srv/assets/retry-failed-event-deliveries.225753ebf217cd1e9d0798f0c6f0a198.png)

Retry sending events using a webhook endpoint’s **Event deliveries** tab.

## See also

- [Interactive webhook endpoint
builder](https://docs.stripe.com/webhooks/quickstart)

## Links

- [events guide](https://docs.stripe.com/event-destinations)
- [Webhooks](https://dashboard.stripe.com/webhooks)
- [events object](https://docs.stripe.com/api/events)
- [Connect](https://docs.stripe.com/connect)
- [event types](https://docs.stripe.com/api/events/types)
- [manage event
destinations](https://docs.stripe.com/api/v2/core/event_destinations)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [listen for events](https://docs.stripe.com/webhooks#test-webhook)
- [query for missed events](https://docs.stripe.com/api/events/list)
- [Interactive webhook endpoint
builder](https://docs.stripe.com/webhooks/quickstart)