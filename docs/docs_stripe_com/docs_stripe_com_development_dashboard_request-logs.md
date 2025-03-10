# View API request logs

## Filter API request logs and view log entries in the Developers Dashboard.

#### Note

[Workbench](https://docs.stripe.com/workbench) replaces the Developers
Dashboard, and we automatically enable it for all new Stripe accounts by
default. Configure this setting from the
[Developers](https://dashboard.stripe.com/settings/developers) settings in the
Dashboard.

Read about how to [view API request
logs](https://docs.stripe.com/workbench#request-logs) in Workbench.

When you send an API request, Stripe creates an object and logs the request for
your account. This page describes how to filter API request logs and view log
entries for your account in the Developers Dashboard.

## How requests are logged

This table describes the different ways Stripe logs an API request for your
account.

SourceAPI callLogsAPIWhen you manually trigger an event with the Stripe CLI.Logs
the API call on the [Logs](https://dashboard.stripe.com/logs) page.APIWhen user
actions in your app or website result in an API call.Logs the API call on the
[Logs](https://dashboard.stripe.com/logs) page.APIWhen you call an API directly
with the Stripe CLI.Logs the API call on the
[Logs](https://dashboard.stripe.com/logs) page.DashboardWhen you call an API by
modifying your Stripe resources in the Dashboard.Logs the API call on the
[Logs](https://dashboard.stripe.com/logs) page.
## View your default API version

When you send requests to Stripe, you may specify an API version with the
`Stripe-Version` header. If you don’t specify an API version, Stripe uses your
account’s default API version. Use these steps to find all of the API versions
used by your account within the last week. If you’re using the latest API
version, the version is labeled `Latest`.

- Open the [Developers Dashboard](https://dashboard.stripe.com/developers).
- Your account’s default **API version** is labeled `Default`.

To view a list of versions, see the [API
changelog](https://docs.stripe.com/upgrades#api-versions).

## View API requests by source

Use these steps to filter requests by an API call source.

- Open the [Logs](https://dashboard.stripe.com/logs) page.
- Click **More**.
- In **Source**, select **Dashboard** or **API** to filter requests by source.
- Click **Apply**.

## Find common integration errors

Use this filter to discover common integration errors by error code and API
endpoint.

- Open the [Developers Dashboard](https://dashboard.stripe.com/).
- In **Recent errors**, select the filter button ().
- Select an error type.
- Click an error to view the request payload that failed and the reason.

## Filter by resource ID

When you create, update, or delete a Stripe resource using Stripe APIs, Stripe
returns a resource ID in the response payload. For example, when you [Create a
customer](https://docs.stripe.com/api/customers/create), Stripe returns a
customer ID (in `id`), such as `cus_ImZZa3EEvvQQQU`. Use these steps to filter
API requests by resource ID.

- Open the [Logs](https://dashboard.stripe.com/logs) page.
- Enter the resource ID in the **Filter by resource** ID text field.

## Apply advanced filters

You can use the inline navigation to filter API requests by **Date**,
**Status**, **Method** and **API endpoint**, or apply additional filters to
troubleshoot requests. Use these steps to filter API requests by API version,
error type, error code, and other filters, such as an IP address.

- Open the [Logs](https://dashboard.stripe.com/logs) page.
- Click **More**.- To filter by version, select an option in the **API version**
dropdown menu. For example, `2025-02-24.acacia`.
- To filter by error type, select an option in the **Error type** dropdown menu.
For example, `card_error`.
- To filter by error message, select an option in the **Error code** dropdown
menu. For example, `bank_account_unverified`.
- Click **Apply**.

![Filter by API
version](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-api-version.2db0c042c6ecb829a34870d93a452aa1.png)

## Links

- [Workbench](https://docs.stripe.com/workbench)
- [Developers](https://dashboard.stripe.com/settings/developers)
- [view API request logs](https://docs.stripe.com/workbench#request-logs)
- [Logs](https://dashboard.stripe.com/logs)
- [Developers Dashboard](https://dashboard.stripe.com/developers)
- [API changelog](https://docs.stripe.com/upgrades#api-versions)
- [Developers Dashboard](https://dashboard.stripe.com/)
- [Create a customer](https://docs.stripe.com/api/customers/create)