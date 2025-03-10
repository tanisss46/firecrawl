# Stripe for Visual Studio Code

## Build, test, and use Stripe inside your editor.

Stripe’s
[extension](https://marketplace.visualstudio.com/items?itemName=Stripe.vscode-stripe)
for [Visual Studio Code](https://code.visualstudio.com/) lets you generate
sample code, view API request logs, forward events to your application, and use
Stripe within your editor.

A new Stripe panel in the activity bar provides access to code snippets for
several languages, adds [debug
configurations](https://code.visualstudio.com/docs/editor/debugging#_redirect-inputoutput-tofrom-the-debug-target),
and extends the [command
palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
with common developer workflows.

With Stripe for VS Code, you can:

- [Use an AI Assistant for your Stripe
integration.](https://docs.stripe.com/stripe-vscode#ai-assistant)
- [Get started quickly with a Stripe
Sample.](https://docs.stripe.com/stripe-vscode#samples)
- [Forward Stripe webhook events to your local
application.](https://docs.stripe.com/stripe-vscode#webhooks)
- [Stream request logs in
real-time.](https://docs.stripe.com/stripe-vscode#monitor-logs)
- [Trigger new events while
testing.](https://docs.stripe.com/stripe-vscode#webhooks)
- [Generate snippets for common
scenarios.](https://docs.stripe.com/stripe-vscode#snippets)
- [Verify your source code doesn’t expose API
keys.](https://docs.stripe.com/stripe-vscode#linter)
- [Quickly jump to the API
reference.](https://docs.stripe.com/stripe-vscode#api-reference)
- [Easily access the Stripe
Dashboard.](https://docs.stripe.com/stripe-vscode#dashboard-access)

## Install Stripe for VS Code

#### Note

As a prerequisite, ensure you have the [Stripe
CLI](https://docs.stripe.com/stripe-cli#install) installed.

You can find the Stripe VS Code extension in the [Visual Studio
Marketplace](https://marketplace.visualstudio.com/items?itemName=Stripe.vscode-stripe).
Click **Install** to add the extension to your editor.

## Features

### Use an AI Assistant for your Stripe integration

The Stripe AI assistant applies Stripe knowledge to your VS Code editor to help
you build integrations. It combines large language models with the Stripe
documentation, API reference, code snippets, and developer insights to provide
assistance directly in your development environment.

With the Stripe AI Assistant, you can:

- Get immediate answers about the Stripe API and products
- Receive code suggestions tailored to your integration
- Ask follow-up questions for more detailed information
- Access knowledge from the Stripe documentation and the Stripe developer
community

To use the AI Assistant:

- Open the Stripe panel in the VS Code activity bar.
- Find the [AI Assistant](vscode://stripe.vscode-stripe/chat) section.
- Type your question or request in the input box.
- Receive contextual help based on Stripe’s latest documentation and best
practices.

### Get started quickly with a Stripe Sample

[Stripe Samples](https://github.com/stripe-samples) are built by Stripe, and
provide all of the client and server code you need for common integration
scenarios, such as creating a subscription with Stripe Billing.

The **Start with a Stripe Sample** button allows you to browse through the
catalog and select the right language for your integration. The extension clones
and opens the Sample in a new workspace, automatically populating your API keys
in the .env file of the Sample.

### Trigger and forward webhook events

You can listen for incoming webhook events and forward them to your to your
local machine in one of two ways:

- Click **Forward webhook events to your local machine** in the **Events**
section.
- Run the command `Stripe: Forward webhook events to your local machine` from
the [command
palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

Then, enter the localhost URL that you want to forward events to. If you’re
using Connect, you can set a different URL for events from your Connect
applications. If your localhost URLs use HTTPS, you can skip SSL certificate
verification.

You can use the **Trigger new event** button to test your webhook integration
with events from the Stripe API.

#### Caution

You can only trigger events in test mode.

You can stream events created by members of your account in real time with the
**Start streaming events** button. Clicking on an event entry under **Recent
events** opens event details directly inside your editor.

#### Note

If you’d like to resend an event, you can right click an event entry under
**Recent events** or run a [Stripe
CLI](https://docs.stripe.com/cli/events/resend) command: `stripe events resend
<event>`.

#### Stripe debug configuration

When forwarding events to your local machine, you may find yourself entering the
same URLs over and over. To fix this, you can create a [debug
configuration](https://code.visualstudio.com/docs/editor/debugging#_redirect-inputoutput-tofrom-the-debug-target)
to save your forwarding setup, allowing you to start forwarding to your URLs
with a single button.

Place the following configuration in a
[launch.json](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations)
file, which VS Code uses to track debugging setup details. Then, select the
configuration in the Run view. After selecting your configuration, press `F5` to
quickly start forwarding events.

```
{
 "version": "0.2.0",
 "configurations": [
 {
 "name": "Stripe: Webhooks listen",
 "type": "stripe",
 "request": "launch",
 "command": "listen",
 "forwardTo": "http://localhost:3000",
 "forwardConnectTo": "http://localhost:3000",
 "events": ["payment_intent.succeeded", "payment_intent.canceled"],
 "skipVerify": true
 }
 ]
}
```

You can specify the `forwardTo` and `forwardConnectTo` parameters; these are the
URLs on your local machine that you want to receive your account’s events and
Connect events, respectively. The `events` parameter accepts an optional list to
specify which events to receive. If you’re using HTTPS URLs, the `skipVerify`
parameter accepts a Boolean to skip verifying SSL certificates.

#### Compound configurations

You can launch your local application and forward webhook events simultaneously
using a [compound
configuration](https://code.visualstudio.com/docs/editor/debugging#_compound-launch-configurations).

```
{
 "version": "0.2.0",
 "configurations": [
 {
 "name": "Stripe: Webhooks listen",
 "type": "stripe",
 "request": "launch",
 "command": "listen",
 "forwardTo": "http://localhost:3000",
 "forwardConnectTo": "http://localhost:3000",
 "events": ["payment_intent.succeeded", "payment_intent.canceled"],
 "skipVerify": true
 },
 {
 "type": "node",
 "request": "launch",
 "name": "Node: Launch Program",
 "program": "${workspaceFolder}/examples/standalone.js",
 "skipFiles": ["<node_internals>/**"]
 }
 ],
 "compounds": [
 {
 "name": "Launch: Stripe + API",
 "configurations": ["Node: Launch Program", "Stripe: Webhooks listen"]
 }
 ]
}
```

### Monitor API request logs in real-time

You can stream API request logs created by members of your account in real time
with the **Start streaming API logs** button. Clicking on a log entry under
**Recent logs** opens log details directly inside your editor. From there, you
can hover over the request ID to open the log in your Dashboard.

#### Caution

The extension only delivers logs for requests made in test mode.

### Code snippets for common Stripe scenarios

You can quickly generate code snippets for common scenarios (for example,
creating a Checkout Session and redirecting the user to the browser) or basic
API requests. After generating a snippet, you can tab through it to fill in your
values.

### Verify your source code doesn’t expose API keys

The built-in Stripe linter checks for [API keys](https://docs.stripe.com/keys)
in your source code and marks them as problems if you unsafely expose them.

#### Note

The linter treats unsafe use of test-mode keys as warnings and live-mode keys as
errors.

!

### Access the Stripe API reference

You can hover over a resource method to reveal a link to the [Stripe API
reference](https://docs.stripe.com/api). This is useful for identifying
parameters for an API request or the shape of an API response.

!

### Access the Stripe Dashboard

The **Quick Links** section includes links to quickly jump to the Dashboard to
manage API keys, webhooks, and other resources.

!

## Settings

The following configurations can be set in your [VS Code
settings](https://code.visualstudio.com/docs/getstarted/settings):

Setting nameDescription`stripe.cliInstallPath`Specifies the absolute install
path for the Stripe CLI executable. Default: the default install path for the
Stripe CLI`stripe.projectName`Specifies the project name to read from for the
Stripe CLI configuration. You can define a unique configuration for individual
projects, or use the global configuration by default. See the [Stripe CLI
reference](https://docs.stripe.com/cli/login) for more details. Default:
`default``stripe.telemetry.enabled`Specifies whether to enable Stripe telemetry
(even if enabled still abides by the overall `telemetry.enableTelemetry`
setting). Default: `true`
## Commands

The extension supports various commands to access features through the [command
palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).
To see the full list of supported commands, open the command palette and type
`Stripe`.

!

## See also

- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Webhooks](https://docs.stripe.com/webhooks)

## Links

-
[extension](https://marketplace.visualstudio.com/items?itemName=Stripe.vscode-stripe)
- [Visual Studio Code](https://code.visualstudio.com/)
- [debug
configurations](https://code.visualstudio.com/docs/editor/debugging#_redirect-inputoutput-tofrom-the-debug-target)
- [command
palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
- [Stripe CLI](https://docs.stripe.com/stripe-cli#install)
- [Stripe Samples](https://github.com/stripe-samples)
- [Stripe CLI](https://docs.stripe.com/cli/events/resend)
-
[launch.json](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations)
- [http://localhost:3000](http://localhost:3000)
- [compound
configuration](https://code.visualstudio.com/docs/editor/debugging#_compound-launch-configurations)
- [API keys](https://docs.stripe.com/keys)
- [Stripe API reference](https://docs.stripe.com/api)
- [VS Code settings](https://code.visualstudio.com/docs/getstarted/settings)
- [Stripe CLI reference](https://docs.stripe.com/cli/login)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Webhooks](https://docs.stripe.com/webhooks)