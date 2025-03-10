you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a new endpoint

A [webhook endpoint](https://docs.stripe.com/webhooks) is a destination on your
server that receives requests from Stripe, notifying you about events that
happen on your account such as a customer disputing a charge or a successful
recurring payment. Add a new endpoint to your server and make sure it’s publicly
accessible so we can send unauthenticated POST requests.

Server2 Handle requests from Stripe
### Read the event data

Stripe sends the event data in the request body. Each event is structured as an
[Event object](https://docs.stripe.com/api/events) with a `type`, `id`, and
related Stripe resource nested under `data`.

Server
### Handle the event

As soon as you have the event object, check the
[type](https://docs.stripe.com/api/events/types) to know what kind of event
happened. You can use one webhook to handle several different event types at
once, or set up individual endpoints for specific events.

Server
### Return a 200 response

[Send a successful 200
response](https://docs.stripe.com/webhooks#handle-events-asynchronously) to
Stripe as quickly as possible because Stripe retries the event if a response
isn’t sent within a reasonable time. Write any long-running processes as code
that can run asynchronously outside the webhook endpoint.

Server3 Test the webhook
### Run the server

Build and run your server to test the endpoint at
`http://localhost:4242/webhook`.

`ruby server.rb`Server
### Download the CLI

Use the Stripe CLI to test your webhook locally. [Download the
CLI](https://docs.stripe.com/stripe-cli) and log in with your Stripe account.
Alternatively, use a service like ngrok to make your local endpoint publicly
accessible.

`stripe login`Run in the Stripe ShellServer
### Forward events to your webhook

Set up [event forwarding](https://docs.stripe.com/webhooks#test-webhook) with
the CLI to send all Stripe events in test mode to your local webhook endpoint.

`stripe listen --forward-to localhost:4242/webhook`Run in the Stripe ShellServer
### Simulate events

Use the CLI to [simulate specific events](https://docs.stripe.com/cli/trigger)
that test your webhook application logic by sending a POST request to your
webhook endpoint with a mocked Stripe event object.

`stripe trigger payment_intent.succeeded`Run in the Stripe ShellServer4 Secure
your webhook
### Secure your webhook

Verify the source of a webhook request to prevent bad actors from sending fake
payloads or injecting SQL that modify your backend systems. Secure your webhook
with a client signature to validate that Stripe generated a webhook request and
that it didn’t come from a server acting like Stripe.

Server
### Add the endpoint signing secret

Each webhook endpoint has a unique signing secret. Find the secret in the
[webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard, or,
if you’re testing locally with the Stripe CLI, from the CLI output with the
command `stripe listen`.

Server
### Verify the event

Use the Stripe library to verify and construct the event from Stripe. You need
the endpoint secret, the request headers, and the raw request body to properly
verify the event. Alternatively, you can [manually
verify](https://docs.stripe.com/webhooks?verify=verify-manually#verify-manually)
the signature without having to use the Stripe library.

Server
### Read the request signature

Each request from Stripe contains a `Stripe-Signature` header. Store a reference
to this header value for later use.

Server
### Verify the request

Use the Stripe library to verify that the request came from Stripe. Pass the raw
request body, `Stripe-Signature` header, and endpoint secret to construct an
[Event](https://docs.stripe.com/api/events/object).

Server
### Handle errors

Checking for errors helps catch improperly configured webhooks or malformed
requests from non-Stripe services. Common errors include using the wrong
endpoint secret, passing a parsed representation (for example, JSON) of the
request body, or reading the wrong request header.

Server
### Test the endpoint

Test your secured endpoint by using the Stripe CLI, which sends the proper
signature header in each test event.

Server
## Next steps

#### [Going live](https://docs.stripe.com/webhooks#register-webhook)

Learn how to deploy your webhook endpoint to production and handle events at
scale by only sending the specific events you need.

#### [Best practices](https://docs.stripe.com/webhooks#best-practices)

Understand best practices for maintaining your endpoint, such as managing
retries or duplicate events.

#### [Stripe CLI](https://docs.stripe.com/stripe-cli)

The Stripe CLI has several commands that can help test your Stripe application
beyond webhooks.

server.rbDownload
```
# Build a webhook endpoint
Build a simple webhook endpoint to listen to events from Stripe. Included are
some basic build and run scripts you can use to start up the application.
## Running the sample
1. Build the server
~~~bundle install~~~
2. Run the server
~~~ruby server.rb -o 0.0.0.0~~~

## Testing the webhook
The easiest way to test your webhook locally is with the Stripe CLI. Download
[the CLI](https://github.com/stripe/stripe-cli) and log in with your Stripe
account. Alternatively, use a service like ngrok to make your local endpoint
publicly accessible.
Set up event forwarding with the CLI to send all Stripe events in test mode to
your local webhook endpoint.
~~~stripe listen --forward-to localhost:4242/webhook~~~
Use the CLI to simulate specific events that test your webhook application logic
by sending a POST request to your webhook endpoint with a mocked Stripe event
object.
~~~stripe trigger payment_intent.succeeded~~~
```

## Links

- [text version of this guide](https://docs.stripe.com/webhooks)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Event object](https://docs.stripe.com/api/events)
- [type](https://docs.stripe.com/api/events/types)
- [Send a successful 200
response](https://docs.stripe.com/webhooks#handle-events-asynchronously)
- [Download the CLI](https://docs.stripe.com/stripe-cli)
- [event forwarding](https://docs.stripe.com/webhooks#test-webhook)
- [simulate specific events](https://docs.stripe.com/cli/trigger)
- [webhooks](https://dashboard.stripe.com/webhooks)
- [manually
verify](https://docs.stripe.com/webhooks?verify=verify-manually#verify-manually)
- [Event](https://docs.stripe.com/api/events/object)
- [Going live](https://docs.stripe.com/webhooks#register-webhook)
- [Best practices](https://docs.stripe.com/webhooks#best-practices)