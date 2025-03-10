# Shell and API Explorer

## Use a command line interface to manage your integration and explore APIs.

Shell is a command line interface within Workbench that provides many of the
same commands built into the [Stripe CLI](https://docs.stripe.com/stripe-cli).
When using Workbench, a minimal Shell is always available at the bottom of the
pane, or use the **Shell** tab to launch a full-screen session.

Use the following Shell features to help you manage and debug your Stripe
integration:

- **Autocompletion**: Shell provides tab completion for API requests and CLI
commands.
- **API Explorer:** Use the built-in API Explorer to visually explore API
resources and build API calls from Shell.

#### Note

Shell runs in the browser, so it has some limitations when compared to the
[Stripe CLI](https://docs.stripe.com/stripe-cli), which can receive and trigger
webhook events on your local machine with a local event listener. See [Test a
webhooks integration with the Stripe
CLI](https://docs.stripe.com/webhooks#test-webhook) to learn more.

## Initial setup

Sign in to the [Dashboard](https://dashboard.stripe.com/). From the
**Developers** menu, click **Workbench**. Switch to the **Shell** tab.

#### Common mistake

Shell is read-only in live mode. Switch to a
[sandbox](https://docs.stripe.com/sandboxes) to run API requests that create,
modify, or delete API objects.

[Listen for events](https://docs.stripe.com/workbench/shell#listen)- From the
command line prompt, type `stripe listen` to listen for [webhook
events](https://docs.stripe.com/event-destinations#events-overview), then press
**Enter** on your keyboard to run the command.

```
stripe listen
```

This listens to incoming events for your Stripe account.

[Run your first API request](https://docs.stripe.com/workbench/shell#first)-
Click **New pane** to open a new session in a pane alongside your existing
session.
- the command, paste it into the command line prompt, then press **Enter**
on your keyboard.
- the object identifier (in `id`) from the response for subsequent
requests.

```
stripe products create \
--name="Introductory offer (Monthly)" \
--description="$0.99 per month"
```

This creates a product with a name and description.

[Use the API Explorer](https://docs.stripe.com/workbench/shell#explorer)- Click
**API Explorer** to show the interactive API Explorer on the right.
- Choose the `Products` resource and the `Update` method. The API Explorer shows
all the required and optional parameters for the Products resource.
- Paste the object identifier from the previous step into the `Value` for the
`id` path argument. When you provide the API Explorer with an existing object’s
identifier, it loads the properties of the existing product.
- Update the optional parameter `description` to 1.99 USD per month. The API
Explorer automatically populates Shell with the equivalent API command to update
the product’s description. Press **Enter** to run the command and update the
product.
- Click **Print SDK code** to see the equivalent code snippet in the language of
your choice.

## Available commands

Shell provides multiple commands in addition to the `stripe` command (see the
[Stripe CLI reference](https://docs.stripe.com/cli)).

CommandPurpose`cd`Navigates to other documentation pages`clear`Clears all prior
text from the shell`ls`Lists Dashboard pages relative to the current
one`pwd`Prints the current page slug and title`shortcuts`Displays keyboard
shortcuts that you can use with Shell`stripe`Available Stripe CLI commands (see
the [complete reference](https://docs.stripe.com/cli))`whoami`Displays logged in
merchant details

## Links

- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Test a webhooks integration with the Stripe
CLI](https://docs.stripe.com/webhooks#test-webhook)
- [Dashboard](https://dashboard.stripe.com/)
- [sandbox](https://docs.stripe.com/sandboxes)
- [webhook events](https://docs.stripe.com/event-destinations#events-overview)
- [Stripe CLI reference](https://docs.stripe.com/cli)