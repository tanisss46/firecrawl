# Stripe CLI

## Manage your Stripe resources in a sandbox directly from the command line.

The Stripe CLI is a developer tool to help you build, test, and manage your
integration with Stripe directly from the command line. With the Stripe CLI,
it’s easy to perform many common tasks like calling Stripe APIs, testing your
webhooks integration, and creating an application.

## Start with a guide

[Get started with the Stripe CLIInstall the Stripe CLI on macOS, Windows, and
Linux and get started with a YouTube video from Developer
Advocacy.](https://docs.stripe.com/stripe-cli)[Enable autocompletion for the
Stripe CLIEnable autocompletion so that the Stripe CLI automatically completes
your commands.](https://docs.stripe.com/stripe-cli/autocomplete)[Stripe CLI keys
and permissionsLearn about Stripe CLI keys, where they’re stored locally, and
where to find their
permissions.](https://docs.stripe.com/stripe-cli/keys)[Upgrade the Stripe
CLITake advantage of the latest features of the Stripe
CLI.](https://docs.stripe.com/stripe-cli/upgrade)[Reference guidesUse these
reference guides to explore the CLI and Stripe
APIs.](https://docs.stripe.com/stripe-cli/reference)
## Log into Stripe to authenticate requests

Log in and authenticate your [Stripe user
account](https://docs.stripe.com/get-started/account/activate) to generate a set
of *restricted keys*. To learn more, see [Stripe CLI keys and
permissions](https://docs.stripe.com/stripe-cli/keys).

```
stripe login
```

Press the **Enter** key on your keyboard to complete the authentication process
in your browser.

```
Your pairing code is: enjoy-enough-outwit-win
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit
https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1
(^C to quit)
```

## Specify an API version while running requests

When you call Stripe APIs in the CLI, it uses your default API version in all
requests, which you can [identify in
Workbench](https://docs.stripe.com/workbench/guides#view-api-versions). To try
out different API versions in the CLI, use the following flags:

FlagDescriptionExample`–stripe-version 2025-02-24.acacia`Use the
`--stripe-version` flag in any CLI request to specify an API version.`stripe
products create --name=“My Product” --stripe-version
2025-02-24.acacia``--latest`Use the `--latest` flag in any CLI request to
specify the latest API version.`stripe products create --name="My Product"
--latest`
You can also [view a list of API
versions](https://docs.stripe.com/upgrades#api-versions).

## Stream request logs

Use the `stripe logs tail` command to stream API request logs. Keep this window
open. If you have an error in your API calls, this terminal returns the API
error message and a reason for the error.

```
stripe logs tail
```

## Forward events to your local webhook endpoint

Use the `--forward-to` flag to send all [Stripe
events](https://docs.stripe.com/cli/trigger#trigger-event) in a **sandbox** to
your local webhook endpoint. To disable HTTPS certificate verification, use the
`--skip-verify` flag.

```
stripe listen --forward-to localhost:4242/webhooks
```

```
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

To forward specific events in a comma separated list, use the `--events` flag.

```
stripe listen --events
payment_intent.created,customer.created,payment_intent.succeeded,charge.succeeded,checkout.session.completed,charge.failed
\
 --forward-to localhost:4242/webhook
```

If you’ve already [registered your endpoint in
Stripe](https://docs.stripe.com/webhooks#register-webhook), you can use the
`--load-from-webhooks-api` and `--forward-to` flags.

```
stripe listen --load-from-webhooks-api --forward-to localhost:4242
```

This command forwards events sent to your Stripe-registered **public** webhook
endpoint to your **local** webhook endpoint. It loads your registered endpoint,
parses the path and its registered events, then appends the path to your local
webhook endpoint in the `--forward-to` path. If you’re checking webhook
signatures, use the `{{WEBHOOK_SIGNING_SECRET}}` from the initial output of the
`listen` command.

## List all available events

Use the [–help](https://docs.stripe.com/cli/help) flag to list all possible
events that can occur for an event category. For example, to list all possible
events for the [prebuilt checkout
page](https://docs.stripe.com/checkout/quickstart) for [Stripe
Checkout](https://docs.stripe.com/payments/checkout):

```
stripe trigger checkout --help
```

## Create a one-time product and price

- Make a single API request to [Create a
product](https://docs.stripe.com/api/products/create).

```
stripe products create \
--name="My First Product" \
--description="Created with the Stripe CLI"
```

- Look for the product identifier (in `id`) in the response object. Save it for
the next step.

If everything worked, the command-line displays the following response.

```
{
 "id": "prod_LTenIrmp8Q67sa",
 "object": "product",
```

See all 25 lines- Call [Create a
price](https://docs.stripe.com/api/prices/create) to attach a price of 30 USD.
Swap the placeholder in `product` with your product identifier (for example,
`prod_LTenIrmp8Q67sa`).

```
stripe prices create \
 --unit-amount=3000 \
 --currency=usd \
 --product={{PRODUCT_ID}}
```

If everything worked, the command-line displays the following response.

```
{
 "id": "price_1KzlAMJJDeE9fu01WMJJr79o",
 "object": "price",
```

See all 20 lines
## Trigger a webhook event while testing

Trigger the `checkout.session.completed` event to create the API objects that
result from a checkout session successfully completing.

```
stripe trigger checkout.session.completed
```

Your `stripe listen` terminal displays the following output:

```
Setting up fixture for: checkout_session
Running fixture for: checkout_session
Setting up fixture for: payment_page
Running fixture for: payment_page
Setting up fixture for: payment_method
Running fixture for: payment_method
Setting up fixture for: payment_page_confirm
Running fixture for: payment_page_confirm
Trigger succeeded!
```

To learn more about triggers, read our
[guide](https://docs.stripe.com/stripe-cli/triggers).

## Links

- [Get started with the Stripe CLIInstall the Stripe CLI on macOS, Windows, and
Linux and get started with a YouTube video from Developer
Advocacy.](https://docs.stripe.com/stripe-cli)
- [Enable autocompletion for the Stripe CLIEnable autocompletion so that the
Stripe CLI automatically completes your
commands.](https://docs.stripe.com/stripe-cli/autocomplete)
- [Stripe CLI keys and permissionsLearn about Stripe CLI keys, where they’re
stored locally, and where to find their
permissions.](https://docs.stripe.com/stripe-cli/keys)
- [Upgrade the Stripe CLITake advantage of the latest features of the Stripe
CLI.](https://docs.stripe.com/stripe-cli/upgrade)
- [Reference guidesUse these reference guides to explore the CLI and Stripe
APIs.](https://docs.stripe.com/stripe-cli/reference)
- [Stripe user account](https://docs.stripe.com/get-started/account/activate)
-
[https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1](https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1)
- [identify in
Workbench](https://docs.stripe.com/workbench/guides#view-api-versions)
- [view a list of API versions](https://docs.stripe.com/upgrades#api-versions)
- [Stripe events](https://docs.stripe.com/cli/trigger#trigger-event)
- [registered your endpoint in
Stripe](https://docs.stripe.com/webhooks#register-webhook)
- [–help](https://docs.stripe.com/cli/help)
- [prebuilt checkout page](https://docs.stripe.com/checkout/quickstart)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Create a product](https://docs.stripe.com/api/products/create)
- [Create a price](https://docs.stripe.com/api/prices/create)
- [guide](https://docs.stripe.com/stripe-cli/triggers)