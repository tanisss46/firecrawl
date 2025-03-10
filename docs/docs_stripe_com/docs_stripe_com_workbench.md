# Workbench

## Use Workbench to debug, manage, and grow your Stripe integration.

#### Note

Workbench replaces the existing [Developers
Dashboard](https://docs.stripe.com/development/dashboard), and we enable
Workbench by default for all new Stripe accounts. Configure the setting from the
[Developers](https://dashboard.stripe.com/settings/developers) settings in the
Dashboard.

Workbench provides developer tools to help you debug, manage, and grow your
Stripe integration from your browser, anywhere in the Dashboard. For example,
using Workbench you can:

- Review a summary of recent integration errors
- Inspect API objects, request logs, events, and webhook deliveries
- Create and manage your webhook endpoint configuration
- Run API requests using the built-in command line environment, or build them
with the API Explorer

**Share your ideas:** improve Workbench by clicking **Share feedback** at the
top of the tool with feature requests, bug reports, and feedback.

## Get started

To use Workbench, you [need a Stripe
account](https://dashboard.stripe.com/register). Only users with the
**Administrator** or **Developer** role have full access to all Workbench tools.

- Sign in to the [Dashboard](https://dashboard.stripe.com/). From the
**Developers** menu, click [Workbench](https://dashboard.stripe.com/workbench).
- You can drag the top handle of the Workbench pane to resize it, or you can
click the maximize icon () to leave or enter full-screen mode.
- Click the minimize icon () to collapse Workbench to a taskbar at the bottom of
the page, or the expand icon () to reopen the pane. The taskbar lets you quickly
inspect API objects and includes a notification tray that alerts you to critical
API errors and event activity.
- To hide the Workbench taskbar, click the collapse icon () to minimize the
taskbar to an icon on the right of the Dashboard. Hover over the icon to display
the notification tray. Click the icon to reopen the full Workbench pane.

Workbench includes multiple tools in each tab. Learn more about the
functionality of each tab and how to use it below.

#### Note

To open or minimize Workbench from anywhere in the Dashboard, press the tilde
key (**~**) on your keyboard.

### Use Workbench tools

While using Workbench, keep these tools in mind:

- Click ** link** to generate a shareable URL of the current Workbench view.
- Click **Send feedback** to share ideas or questions with the core development
team.

## Overview of your Stripe integration

See an overview of your account’s API activity in the
[Overview](https://dashboard.stripe.com/workbench/overview) tab.

- The **API keys** widget displays a list of standard and restricted keys on
your account. Click **Manage** to create or update your API keys.
- The **API versions** widget displays a breakdown of the API versions specified
by recent API requests to your account. Click **Upgrade available** to [upgrade
the default API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api) of your
Stripe account.
- The **API requests** and **Webhooks** graphs visualize recent API activity on
your account. Choose a time period from the dropdown and the graphs will update
to reflect that interval.
- **Recent errors** summarizes the most recent errors on your Stripe account.

!

The Overview tab shows a quick snapshot of your account’s API activity.

## View recent errors

The [Errors](https://dashboard.stripe.com/workbench/errors) tab summarizes
recent errors for your Stripe account. You can learn more about how to resolve
each type of API error, and review recent API request logs for each error.
Choose a time period from the dropdown to see errors from that interval.

!

The Errors tab summarizes recent API errors and highlights related request logs.

On the left-hand pane, API errors are grouped by error type. Select an error
group to learn more about the error’s details and impact on your integration.

- The number of **Occurrences** shows how frequently this error has occurred in
the specified time period.
- The **Path** specifies the API endpoint used for requests resulting in this
error.
- The **Source** specifies the user agent used for requests resulting in this
error.
- The **Logs** section summarizes requests logs for the specified API errors.
Clicking on one reveals more details in the **Requests** tab, which provides a
complete and detailed view of relevant request logs.

## Use the Inspector to learn about API objects

Use the [Inspector](https://dashboard.stripe.com/workbench/inspector) to explore
a JSON view of API objects on your Stripe account. To inspect an object, you
can:

- Enter an object ID from the **Inspector** tab.
- Visit a Dashboard page for any object (for example, a `Payment`, `Customer`,
or `Subscription`) and click the **Inspector** icon (), or open the
**Inspector** tab in Workbench.

!

The Inspector shows a JSON view of the API object, and any related API objects,
request logs and events.

When inspecting an API object, the Inspector provides several details:

- The left-hand pane shows a **Data map** with a hierarchy of related API
objects.
- The **Overview** tab provides a JSON view of the object.
- The **Logs** tab shows request logs related to the object.
- The **Events** tab summarizes recently generated events related to the object.

When in a [sandbox](https://docs.stripe.com/sandboxes), the **Edit in API
Explorer** button preloads the API object into the API Explorer on the **Shell**
tab. From there, you can update API properties to modify the object.

If the **Auto-inspect** toggle is on, the Inspector automatically updates to
show currently-visible objects as you browse the Dashboard .

## View API request logs

The [Logs](https://dashboard.stripe.com/workbench/logs) tab includes a list of
recent API requests and responses for your Stripe account. Workbench highlights
recent errors with suggestions on how to resolve them. You can filter API
requests by:

- Date of the request
- HTTP status (for example, `200`)
- HTTP method (for example, `POST` or `DELETE`)
- API endpoint (for example, `/v1/checkout/sessions`)
- IP address that created the request
- Source (direct API requests or Dashboard)
- Account (or specifically when using Connect, the platform or connected
accounts)
- API version (for example, `2020-08-27`)
- Error code (for example, `resource_missing`)
- Error type (for example, `invalid_request_error`)
- Error parameter (for example, `line_items[*][price]`)

Workbench doesn’t automatically refresh this tab in real-time as your account
receives new API requests. Click **Refresh logs** to fetch the latest request
logs from your Stripe account.

!

The Logs tool presents a timeline of API activity, with filters for time
endpoint, response code, and other properties.

## Review recent events on your Stripe account

The [Events](https://dashboard.stripe.com/workbench/events) tab includes a list
of recent events on your Stripe account. Click **Refresh events** to fetch the
latest events from your Stripe account. You can filter events by:

- Date of the event
- Delivery status (delivered or failed)
- Event type (for example, `customer.subscription.created`; you can also use
wildcards (for example, `customer.*`)
- API resource (for example, `cus_123`)

!

The Events tab shows recent activity on your Stripe account. Events can be
delivered to webhook endpoints.

Click an event in the list on the left to review the event’s details, payload,
and attempted deliveries on the right:

- Filter the delivery attempts for a specific event by choosing the
**Succeeded** or **Failed** tab.
- From the overflow menu (), click **View webhook endpoint** to see which event
destination this event was sent to.
- Click **Resend** on a delivery attempt to resend that event to the webhook
endpoint.

Learn more about [managing webhook
endpoints](https://docs.stripe.com/workbench/event-destinations) with Workbench.

## Manage webhook endpoints

You can create a new webhook endpoint for Stripe to deliver events to in the
[Webhooks](https://dashboard.stripe.com/webhooks) tab.

- URL endpoints using webhooks
- Your local machine using the [Stripe CLI](https://docs.stripe.com/stripe-cli)

### Create a new endpoint

Click **Create new endpoint** to configure a new webhook endpoint that Stripe
sends events to. Select the API version that Stripe uses to generate webhook
events and the event types to listen for, and specify an HTTPS URL where your
server hosts the webhook endpoint.

On the left, Workbench lists any configured webhook endpoints. The **Overview**
summarizes the activity on that configured endpoint, and **Event deliveries**
provides a complete list of attempts by Stripe to deliver events to that
endpoint. Click **Retry now** next to any delivery attempt so Stripe can
redeliver the event to that endpoint.

!

Set up a new webhook endpoint or route events to your local development machine.

## Run API commands using Shell and Explorer

[Shell](https://dashboard.stripe.com/workbench/shell) provides a command line
interface to manage your Stripe resources within Workbench, similar to the
[Stripe CLI](https://docs.stripe.com/stripe-cli). See [Shell and API
Explorer](https://docs.stripe.com/workbench/shell) for the full list of
available commands.

#### Note

Shell is read-only in live mode. Switch to a
[sandbox](https://docs.stripe.com/sandboxes) to run API requests that create,
modify, or delete API objects.

When using Workbench, a minimal Shell is always available in the pane, or you
can use the **Shell** tab to launch a full-screen session. From the **Shell**
tab, click **New pane** to split the pane into multiple shell sessions.

Click **API Explorer** to reveal the interactive command builder on the right.
Choose the API resource and HTTP method to show the required and optional
parameters for that request. The **Headers** tab allows setting some HTTP
headers, such as the [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
which allows making API requests to a connected account. Click **Run** to
execute the API request.

Filling in parameters in the API Explorer automatically constructs the
corresponding Shell command. Select a programming language, then click **Print
SDK request** to see the corresponding SDK code for the API request.

!

Shell and the API Explorer help you experiment with Stripe’s API from Workbench.

## See also

- [Use cases](https://docs.stripe.com/workbench/guides)
- [Manage event
destinations](https://docs.stripe.com/workbench/event-destinations)
- [Try the Shell and API Explorer](https://docs.stripe.com/workbench/shell)
- [Keyboard shortcuts in
Workbench](https://docs.stripe.com/workbench/keyboard-shortcuts)

## Links

- [Developers Dashboard](https://docs.stripe.com/development/dashboard)
- [Developers](https://dashboard.stripe.com/settings/developers)
- [related set of guides](https://docs.stripe.com/workbench/guides)
- [need a Stripe account](https://dashboard.stripe.com/register)
- [Dashboard](https://dashboard.stripe.com/)
- [Workbench](https://dashboard.stripe.com/workbench)
- [Overview](https://dashboard.stripe.com/workbench/overview)
- [upgrade the default API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api)
- [Errors](https://dashboard.stripe.com/workbench/errors)
- [Inspector](https://dashboard.stripe.com/workbench/inspector)
- [sandbox](https://docs.stripe.com/sandboxes)
- [Logs](https://dashboard.stripe.com/workbench/logs)
- [Events](https://dashboard.stripe.com/workbench/events)
- [managing webhook
endpoints](https://docs.stripe.com/workbench/event-destinations)
- [Webhooks](https://dashboard.stripe.com/webhooks)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Shell](https://dashboard.stripe.com/workbench/shell)
- [Shell and API Explorer](https://docs.stripe.com/workbench/shell)
- [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [Keyboard shortcuts in
Workbench](https://docs.stripe.com/workbench/keyboard-shortcuts)