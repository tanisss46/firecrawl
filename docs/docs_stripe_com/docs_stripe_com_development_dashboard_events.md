# View events and event object payloads

## View events triggered by your account and their event object payload in the Developers Dashboard.

#### Note

[Workbench](https://docs.stripe.com/workbench) replaces the Developers
Dashboard, and we automatically enable it for all new Stripe accounts by
default. Configure this setting from the
[Developers](https://dashboard.stripe.com/settings/developers) settings in the
Dashboard.

Read about how to [view event
activity](https://docs.stripe.com/workbench#events) in Workbench.

When you send an API request, Stripe logs one or more events for your account.
This page describes how to view events triggered by your account and their event
object payload in the Developers Dashboard.

## How events are logged

This table describes the different ways Stripe logs an
[Event](https://docs.stripe.com/api/events/types) for your account.

SourceTriggerEventsAPIWhen user actions in your app or website result in an API
call.Logs one or more events on the
[Events](https://dashboard.stripe.com/events) page.DashboardWhen you call an API
by modifying your Stripe resources in the Stripe Dashboard.Logs one or more
events on the [Events](https://dashboard.stripe.com/events) page.APIWhen you
manually trigger an event with the Stripe CLI.Logs one or more events on the
[Events](https://dashboard.stripe.com/events) page.APIWhen you call an API
directly with the Stripe CLI.Logs one or more events on the
[Events](https://dashboard.stripe.com/events) page.
## Filter events

Use these steps to view events and their event object payload.

- Open the [Events](https://dashboard.stripe.com/events) page.
- To filter by event, click **Filter**, **Type**:- Enter an event name. For
example, `payment_intent.created`.
- Enter an event with the wild card character. For example, `payment_intent.*`.

## Next steps

- [Webhooks](https://docs.stripe.com/webhooks)

## Links

- [Workbench](https://docs.stripe.com/workbench)
- [Developers](https://dashboard.stripe.com/settings/developers)
- [view event activity](https://docs.stripe.com/workbench#events)
- [Event](https://docs.stripe.com/api/events/types)
- [Events](https://dashboard.stripe.com/events)
- [Webhooks](https://docs.stripe.com/webhooks)