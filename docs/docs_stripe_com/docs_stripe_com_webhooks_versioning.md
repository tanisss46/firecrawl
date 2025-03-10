# Handle webhook versioning

## Learn how to upgrade the API version of your webhook endpoint.

Webhook endpoints either have a specific API version set or use the default API
version of the Stripe account. If you use any of our static language SDKs (.NET,
Java or Go) to process events, the API version set for webhooks should match the
version used to generate the SDKs. Matching these versions ensures successful
deserialization of the event object.

Use this guide to safely upgrade your webhook endpoints to a newer API version
that may have breaking changes.

## Figure out if the new API version has breaking changes

Every API version prior to
[2024-09-30.acacia](https://docs.stripe.com/changelog/acacia#2024-09-30.acacia)
has breaking changes.

Starting with the `2024-09-30.acacia` release, Stripe follows a [new API release
process](https://stripe.com/blog/introducing-stripes-new-api-release-process)
where we release new API versions monthly with no breaking changes. Twice a
year, we issue a new release (for example, Acacia) that starts with an API
version that has breaking changes. You can safely upgrade your webhook endpoints
to any API version in the same release without making changes to your
integration.

## Create a new disabled webhook endpoint

Create a new webhook endpoint with the following parameters:

- `url`: the same URL as your original webhook endpoint, but add a query
parameter to distinguish between events sent to the two different endpoints. For
example `https://example.com/webhooks?version=2024-04-10`.
- `enabled_events`: the same events as your original webhook endpoint.
- `api_version`: the API version you want to upgrade to. If you’re upgrading to
the latest API version, you can use the Dashboard or the API to create the
endpoint. For other versions, use the API to set a specific version.

After you create the new webhook endpoint, disable it. You will re-enable it in
the next step.

![Two endpoints, but only the old one is sending
events](https://b.stripecdn.com/docs-statics-srv/assets/diagram-1.ac21ab637180179813f503649b543e99.png)

## Update your webhook code to ignore events sent to the new endpoint

Update your event processing code:

- If the query parameter is for the older API version, process it as usual.
- If the query parameter is for the newer API version, ignore the event and
return a 200 response to prevent delivery retries.

Next, enable the new webhook endpoint that you created in the previous step. At
this point every event is sent twice: once with the old API version and once
with the new one.

![Two endpoints sending events, but only processing the old
one](https://b.stripecdn.com/docs-statics-srv/assets/diagram-2.f6b4d3cc0c78971b721fe173f19d5e28.png)

## Update your webhook code to process events for the new endpoint

Update the version of the Stripe library you’re using to match the version of
your new webhook endpoint. Make sure to read the changelog and handle any
breaking changes.

Update your event processing code:

- If the query parameter is for the older version, ignore the event. We
recommend returning a 400 status to let Stripe automatically retry the event.
This ensures that if you need to revert, events are re-sent to the older webhook
endpoint.
- If the query parameter is for the new version, process it.

![Two endpoints sending events, but only processing the new
one](https://b.stripecdn.com/docs-statics-srv/assets/diagram-3.8a8b9da70ed66eca60434d406c82f476.png)

## Monitor your new webhook endpoint

If events aren’t being correctly handled by your new code, try the following:

- Revert to the earlier version of your code.
- Temporarily disable the new webhook endpoint.
- Process the failed events (if you returned a 400 status as described in the
previous step, Stripe automatically resends all the events).
- Investigate and fix the issue.
- Enable the new webhook endpoint and resume monitoring.

## Disable the old webhook endpoint

Once the upgrade is successful, disable the old webhook endpoint to stop your
server from returning `400` status. If you don’t disable it, this may cause
issues with integrations that relies on a `200` response.

After you disable the old webhook endpoint, Stripe won’t re-deliver events that
returned a `400`.

![Two endpoints, but only the new one is sending
events](https://b.stripecdn.com/docs-statics-srv/assets/diagram-4.907bbd1016f9fbe79283e8c35be7f3cd.png)

## Links

-
[2024-09-30.acacia](https://docs.stripe.com/changelog/acacia#2024-09-30.acacia)
- [new API release
process](https://stripe.com/blog/introducing-stripes-new-api-release-process)