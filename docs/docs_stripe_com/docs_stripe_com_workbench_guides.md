# Use cases

## Understand how to accomplish common developer tasks with Workbench.

[Workbench](https://docs.stripe.com/workbench) provides many tools for
developers to debug, manage, and grow their Stripe integration. These guides
help you understand how to accomplish common developer tasks.

## View the API versions used by API requests

When you send requests to Stripe, you can specify an API version with the
`Stripe-Version` header. If you don’t specify an API version, Stripe uses your
account’s [default API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api).

- Open the [Overview](https://dashboard.stripe.com/workbench/overview) tab in
Workbench.
- Review the **API versions** section to see requests made in the last week.
- Your account’s default **API version** is labeled Default. Any requests made
using the latest API version are labeled Latest.

To view a list of versions, see the [API
changelog](https://docs.stripe.com/upgrades#api-versions)

## View recent integration errors

Stripe automatically groups recent integration errors by error type and
endpoint.

- Open the [Errors](https://dashboard.stripe.com/workbench/errors) tab in
Workbench.
- In the **Recent errors** pane, select the time period to filter errors by.
- Click a group of errors to see the **Summary** describing the number of
occurences, API endpoint, and request source.

## View API request logs by HTTP method or status

Use these steps to filter API request logs by HTTP method or status.

- Open the [Logs](https://dashboard.stripe.com/workbench/logs) tab in Workbench.
- Click **Status** to filter by **Succeeded** or **Failed** requests. (See the
[complete list of HTTP status
codes](https://docs.stripe.com/error-low-level#status-codes) that Stripe will
return.)
- Click **Apply**.

## View API request logs by source

Use these steps to filter API request logs by source. API requests can orginate
by either actions in the Dashboard, or by a direct API call (for example, by
using an SDK).

- Open the [Logs](https://dashboard.stripe.com/workbench/logs) tab in Workbench.
- Click **More filters**.
- In **Source**, select **Dashboard** or **API** to filter requests by source.
- Click **Apply**.

## Filter by resource ID

When you create, update, or delete a Stripe resource using Stripe APIs, Stripe
returns a resource ID in the response payload. For example, when you [Create a
customer](https://docs.stripe.com/api/customers/create), Stripe returns a
customer ID (in the `id` field), such as `cus_ImZZa3EEvvQQQU`. Use these steps
to filter API requests by resource ID.

- Open the [Logs](https://dashboard.stripe.com/logs) tab in Workbench.
- Enter the resource ID in the **Filter by resource** ID text field and press
**Enter** on your keyboard.

## Filter events

Use these steps to view events and their event object payload.

- Open the [Events](https://dashboard.stripe.com/events) tab in Workbench.
- To filter by event, click **Event type**:- Enter an event name. For example,
`payment_intent.created`.
- Enter an event with the wildcard character. For example, `payment_intent.*`.
- Click **Apply**.

## Links

- [Workbench](https://docs.stripe.com/workbench)
- [default API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api)
- [Overview](https://dashboard.stripe.com/workbench/overview)
- [API changelog](https://docs.stripe.com/upgrades#api-versions)
- [Errors](https://dashboard.stripe.com/workbench/errors)
- [Logs](https://dashboard.stripe.com/workbench/logs)
- [complete list of HTTP status
codes](https://docs.stripe.com/error-low-level#status-codes)
- [Create a customer](https://docs.stripe.com/api/customers/create)
- [Logs](https://dashboard.stripe.com/logs)
- [Events](https://dashboard.stripe.com/events)