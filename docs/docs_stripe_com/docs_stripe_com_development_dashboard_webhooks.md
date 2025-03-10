# Add a webhook endpoint

## Use the Developers Dashboard to create a new webhook endpoint and receive events from Stripe.

This guide describes how to create a new webhook endpoint using the Developers
Dashboard.

#### Note

[Workbench](https://docs.stripe.com/workbench) replaces the Developers
Dashboard, and we automatically enable it for all new Stripe accounts by
default. Configure this setting from the
[Developers](https://dashboard.stripe.com/settings/developers) settings in the
Dashboard.

Learn how to [create a new webhook
endpoint](https://docs.stripe.com/workbench/event-destinations#create-webhook-endpoint)
in Workbench.

## Create a new webhook endpoint

Stripe supports two endpoint types: Account and
[Connect](https://docs.stripe.com/connect). Create an endpoint for *Account*
unless you’ve created a [Connect application](https://docs.stripe.com/connect).
You can register up to 16 webhook endpoints on each Stripe account.

#### Note

When you create an endpoint in the Dashboard, you can choose between your
Account’s [API
version](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-api_version)
or the latest API version. You can test other API versions in Workbench using
`stripe webhook_endpoints create`, but you must [create a webhook
endpoint](https://docs.stripe.com/api/webhook_endpoints/create) using the API to
use other API versions in production.

Use the following steps to register a webhook endpoint in the Developers
Dashboard.

- Navigate to the [Webhooks](https://dashboard.stripe.com/webhooks) page.
- Click **Add endpoint**.
- Add your webhook endpoint’s HTTPS URL in **Endpoint URL**.
- If you have a *Stripe Connect* account, enter a description, then click
**Listen to events on Connected accounts**.
- Select the [event types](https://docs.stripe.com/api#event_types) you’re
currently receiving in your local webhook endpoint in **Select events**.
- Click **Add endpoint**.

## Links

- [complete guide to webhook events](https://docs.stripe.com/webhooks)
- [Workbench](https://docs.stripe.com/workbench)
- [Developers](https://dashboard.stripe.com/settings/developers)
- [create a new webhook
endpoint](https://docs.stripe.com/workbench/event-destinations#create-webhook-endpoint)
- [Connect](https://docs.stripe.com/connect)
- [API
version](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-api_version)
- [create a webhook
endpoint](https://docs.stripe.com/api/webhook_endpoints/create)
- [Webhooks](https://dashboard.stripe.com/webhooks)
- [event types](https://docs.stripe.com/api#event_types)