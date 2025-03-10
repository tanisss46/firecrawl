TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Configure your endpoint

Using the synchronous webhook, you can approve or decline authorization requests
in real time.

You can configure your [webhook](https://docs.stripe.com/webhooks) endpoint in
your [Issuing settings](https://dashboard.stripe.com/account/issuing). When a
purchase attempt occurs, Stripe creates an `issuing_authorization.request` event
and sends it to your configured endpoint for your approval.

Server2 Handle requests from Stripe
### Read the event data

Stripe sends the event data in the request body. Each event is structured as an
[Event object](https://docs.stripe.com/api/events) with a `type`, `id`, and
related Stripe resource nested under `data`.

Server
### Handle the event

As soon as you have the event object, check the
[type](https://docs.stripe.com/api/events/types) and filter for
`issuing_authorization.request`. This is the webhook event that Stripe sends
when a card is used to make a purchase.

Write your business logic here to decide to approve or decline the
authorization. For example, you can reject any authorization over a certain
`amount`.

Server
### Respond to the request

The `issuing_authorization.request` webhook is synchronous, which enables you to
approve or decline authorization requests in real time. You can include your
approval decision in the response body of the webhook request. To do so you must
also specify the `Content-Type` header as `application/json`. See [responding
directly to authorization
requests](https://docs.stripe.com/issuing/controls/real-time-authorizations#authorization-handling)
to learn more.

If Stripe doesn’t receive your approve or decline response or request within 2
seconds, the `Authorization` is automatically approved or declined based on your
timeout settings.

Server3 Test the authorization
### Run the server

Build and run your server to test the endpoint at
`http://localhost:4242/webhook`.

`ruby server.rb`Server
### Download the CLI

Use the Stripe CLI to test your webhook locally. [Download the
CLI](https://github.com/stripe/stripe-cli) and log in with your Stripe account.
Alternatively, use a service like ngrok to make your local endpoint publicly
accessible.

`stripe login`Run in the Stripe ShellServer
### Forward events to your webhook

Set up [event forwarding](https://docs.stripe.com/webhooks#test-webhook) with
the CLI to send all Stripe events in testmode to your local webhook endpoint.

`stripe listen --forward-to localhost:4242/webhook`Run in the Stripe ShellServer
### Simulate an authorization

Use the CLI to simulate the authorization request by sending a POST request to
your webhook endpoint with a mocked Stripe event object.

`stripe trigger issuing_authorization.request`Run in the Stripe ShellServer
## Congratulations!

You have a basic webhook endpoint ready to accept authorization requests from
Stripe.

### Secure your webhook

Verify the source of a webhook request to prevent bad actors from sending fake
payloads or injecting SQL that modify your backend systems. Secure your webhook
with a client signature to validate that Stripe generated a webhook request and
that it didn’t come from a server acting like Stripe.

### Add the endpoint secret

Each webhook endpoint has a unique signing secret. Find the secret in the
Dashboard or, if you’re testing locally with the Stripe CLI, from the CLI output
with the command `stripe listen`.

Server
### Verify the event

Use the Stripe library to verify and construct the event from Stripe. You need
the endpoint secret, the request headers, and the raw request body to properly
verify the event. Alternatively, you can [manually
verify](https://docs.stripe.com/webhooks#verify-manually) the signature without
having to use the Stripe library.

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
signature header in each test event. Otherwise use the webhooks view in the
[Dashboard](https://dashboard.stripe.com/webhooks) to send one-off events.

Server
## Next steps

#### [Going live](https://docs.stripe.com/webhooks#register-webhook)

Learn how to deploy your webhook endpoint to production and handle events at
scale by only sending the specific events you need.

#### [Stripe CLI](https://docs.stripe.com/stripe-cli)

The Stripe CLI has several commands that can help test your Stripe application
beyond webhooks.

server.rbDownload
```
# Real-time authorization endpoint builder
Build a webhook to respond to real-time Issuing authorizations. Included are
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
Use the CLI to simulate an Issuing authorization event that tests your webhook
application logic by sending a POST request to your webhook endpoint with a
mocked Stripe event object.
~~~stripe trigger issuing_authorization.request~~~
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [webhook](https://docs.stripe.com/webhooks)
- [Issuing settings](https://dashboard.stripe.com/account/issuing)
- [Event object](https://docs.stripe.com/api/events)
- [type](https://docs.stripe.com/api/events/types)
- [responding directly to authorization
requests](https://docs.stripe.com/issuing/controls/real-time-authorizations#authorization-handling)
- [Download the CLI](https://github.com/stripe/stripe-cli)
- [event forwarding](https://docs.stripe.com/webhooks#test-webhook)
- [manually verify](https://docs.stripe.com/webhooks#verify-manually)
- [Event](https://docs.stripe.com/api/events/object)
- [Dashboard](https://dashboard.stripe.com/webhooks)
- [Going live](https://docs.stripe.com/webhooks#register-webhook)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)