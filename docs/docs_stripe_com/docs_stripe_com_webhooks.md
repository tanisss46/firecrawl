# Receive Stripe events in your webhook endpoint

## Listen to events in your Stripe account on your webhook endpoint so your integration can automatically trigger reactions.

#### Send events to your AWS account

You can now send events directly to [Amazon EventBridge as an event
destination](https://docs.stripe.com/event-destinations/eventbridge).

When building Stripe integrations, you might want your applications to receive
events as they occur in your Stripe accounts, so that your backend systems can
execute actions accordingly.

Create an event destination to receive events at an HTTPS webhook endpoint.
After you register a webhook endpoint, Stripe can push real-time event data to
your application’s webhook endpoint when
[events](https://docs.stripe.com/event-destinations#events-overview) happen in
your Stripe account. Stripe uses HTTPS to send webhook events to your app as a
JSON payload that includes an [Event
object](https://docs.stripe.com/api/events).

Receiving webhook events is particularly useful for listening to asynchronous
events such as when a customer’s bank confirms a payment, a customer disputes a
charge, a recurring payment succeeds, or when collecting subscription payments.

You can also receive events in [Amazon
EventBridge](https://docs.stripe.com/event-destinations/eventbridge) with event
destinations.

## Get started

To start receiving webhook events in your app:

- Create a webhook endpoint handler to receive event data POST requests.
- Test your webhook endpoint handler locally using the Stripe CLI.
- Create a new [event destination](https://docs.stripe.com/event-destinations)
for your webhook endpoint.
- Secure your webhook endpoint.

You can register and create one endpoint to handle several different event types
at the same time, or set up individual endpoints for specific events.

[Create a handler](https://docs.stripe.com/webhooks#webhook-endpoint-def)
Set up an HTTP or HTTPS endpoint function that can accept webhook requests with
a POST method. If you’re still developing your endpoint function on your local
machine, it can use HTTP. After it’s publicly accessible, your webhook endpoint
function must use HTTPS.

Set up your endpoint function so that it:

- Handles POST requests with a JSON payload consisting of an [event
object](https://docs.stripe.com/api/events/object).
- Quickly returns a successful status code (`2xx`) prior to any complex logic
that could cause a timeout. For example, you must return a `200` response before
updating a customer’s invoice as paid in your accounting system.

#### Note

Alternatively, you can build a webhook endpoint function in your programming
language using our [interactive webhook endpoint
builder](https://docs.stripe.com/webhooks/quickstart).

#### Example endpoint

This code snippet is a webhook function configured to check that the event type
was received, to handle the event, and return a 200 response.

```
require 'json'

# Using Sinatra
post '/webhook' do
 payload = request.body.read
 event = nil

 begin
 event = Stripe::Event.construct_from(
 JSON.parse(payload, symbolize_names: true)
 )
 rescue JSON::ParserError => e
 # Invalid payload
 status 400
 return
 end

 # Handle the event
 case event.type
 when 'payment_intent.succeeded'
 payment_intent = event.data.object # contains a Stripe::PaymentIntent
 # Then define and call a method to handle the successful payment intent.
 # handle_payment_intent_succeeded(payment_intent)
 when 'payment_method.attached'
 payment_method = event.data.object # contains a Stripe::PaymentMethod
# Then define and call a method to handle the successful attachment of a
PaymentMethod.
 # handle_payment_method_attached(payment_method)
 # ... handle other event types
 else
 puts "Unhandled event type: #{event.type}"
 end

 status 200
end
```

[Test your handler](https://docs.stripe.com/webhooks#test-webhook)
Before you go-live with your webhook endpoint function, we recommend that you
test your application integration. You can do so by configuring a local listener
to send events to your local machine, and sending test events. You need to use
the [CLI](https://docs.stripe.com/stripe-cli) to test.

#### Forward events to a local endpoint

To forward events to your local endpoint, run the following command with the
[CLI](https://docs.stripe.com/stripe-cli) to set up a local listener. The
`--forward-to` flag sends all [Stripe
events](https://docs.stripe.com/cli/trigger#trigger-event) in **test mode** to
your local webhook endpoint.

```
stripe listen --forward-to localhost:4242/webhook
```

#### Note

You can also run the stripe listen command on the [Stripe
Shell](https://docs.stripe.com/stripe-shell/overview) to see events through the
Stripe shell terminal, although you won’t be able to forward events from the
shell to your local endpoint.

Useful configurations to help you test with your local listener include the
following:

- To disable HTTPS certificate verification, use the `--skip-verify` optional
flag.
- To forward only specific events, use the `--events` optional flag and pass in
a comma separated list of events.

```
stripe listen --events
payment_intent.created,customer.created,payment_intent.succeeded,checkout.session.completed,payment_intent.payment_failed
\
 --forward-to localhost:4242/webhook
```

- To forward events to your local webhook endpoint from the public webhook
endpoint that you already registered on Stripe, use the
`--load-from-webhooks-api` optional flag. It loads your registered endpoint,
parses the path and its registered events, then appends the path to your local
webhook endpoint in the `--forward-to path`.

```
stripe listen --load-from-webhooks-api --forward-to localhost:4242/webhook
```

- To check webhook signatures, use the `{{WEBHOOK_SIGNING_SECRET}}` from the
initial output of the listen command.

```
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)

```

#### Triggering test events

To send test events, trigger an event type that your webhook is subscribed to by
manually creating an object in the Stripe Dashboard. Alternatively, you can use
the following command in either [Stripe
Shell](https://docs.stripe.com/stripe-shell/overview) or [Stripe
CLI](https://docs.stripe.com/stripe-cli).

This example triggers a `payment_intent.succeeded` event:

```
stripe trigger payment_intent.succeeded
Running fixture for: payment_intent
Trigger succeeded! Check dashboard for event details.
```

Learn how to trigger events with [Stripe for VS
Code](https://docs.stripe.com/stripe-vscode).

[Register your endpoint](https://docs.stripe.com/webhooks#register-webhook)
After testing your webhook endpoint function, use the
[API](https://docs.stripe.com/api/v2/event-destinations) or the **Webhooks** tab
in Workbench to register your webhook endpoint’s accessible URL to make sure
that Stripe knows where to deliver events. You can register up to 16 webhook
endpoints with Stripe. Registered webhook endpoints must be publicly accessible
**HTTPS** URLs.

#### Webhook URL format

The URL format to register a webhook endpoint is:

```
https://<your-website>/<your-webhook-endpoint>

```

For example, if your domain is `https://mycompanysite.com` and the route to your
webhook endpoint is `@app.route('/stripe_webhooks', methods=['POST'])`, specify
`https://mycompanysite.com/stripe_webhooks` as the **Endpoint URL**.

#### Create an event destination for your webhook endpoint

Create an event destination using Workbench in the Dashboard or programatically
with the [API](https://docs.stripe.com/api/v2/event-destinations). You can
register up to 16 event destinations on each Stripe account.

DashboardAPI
To create a new webhook endpoint in the Dashboard:

- Open the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench.
- Click **Create an event destination**.
- Select where you want to receive events from. Stripe supports two types of
configurations: **Your account** and [Connected
accounts](https://docs.stripe.com/connect). Select **Account** to listen to
events from your own account. If you created a [Connect
application](https://docs.stripe.com/connect) and want to listen to events from
your connected accounts, select **Connected accounts**.
- Select the API version for the [events
object](https://docs.stripe.com/api/events) you want to consume.
- Select the [event types](https://docs.stripe.com/api/events/types) that you
want to send to a webhook endpoint.
- Select **Continue**, then select **Webhook endpoint** as the destination type.
- Click **Continue**, then provide the **Endpoint URL** and an optional
description for the webhook.

![Register a new webhook using the Webhooks
tab](https://b.stripecdn.com/docs-statics-srv/assets/create-webhook.f728025897e9e4ca2ba623abe34995a0.png)

Register a new webhook using the **Webhooks** tab

#### Note

[Workbench](https://docs.stripe.com/workbench) replaces the existing [Developers
Dashboard](https://docs.stripe.com/development/dashboard). If you’re still using
the Developers Dashboard, see how to [create a new webhook
endpoint](https://docs.stripe.com/development/dashboard/webhooks).

[Secure your
endpoint](https://docs.stripe.com/webhooks#verify-official-libraries)
You need to secure your integration by making sure your handler verifies that
all webhook requests are generated by Stripe. You can verify webhook signatures
using our official libraries or verify them manually.

Verify with official libraries (recommended)Verify manually
### Verify webhook signatures with official libraries

We recommend using our official libraries to verify signatures. You perform the
verification by providing the event payload, the `Stripe-Signature` header, and
the endpoint’s secret. If verification fails, you get an error.

If you get a signature verification error, read our guide about [troubleshooting
it](https://docs.stripe.com/webhooks/signature).

#### Warning

Stripe requires the raw body of the request to perform signature verification.
If you’re using a framework, make sure it doesn’t manipulate the raw body. Any
manipulation to the raw body of the request causes the verification to fail.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

require 'stripe'
require 'sinatra'

# If you are testing your webhook locally with the Stripe CLI you
# can find the endpoint's secret by running `stripe listen`
# Otherwise, find your endpoint's secret in your webhook settings in
# the Developer Dashboard
endpoint_secret = 'whsec_...'

# Using the Sinatra framework
set :port, 4242

post '/my/webhook/url' do
 payload = request.body.read
 sig_header = request.env['HTTP_STRIPE_SIGNATURE']
 event = nil

 begin
 event = Stripe::Webhook.construct_event(
 payload, sig_header, endpoint_secret
 )
 rescue JSON::ParserError => e
 # Invalid payload
 puts "Error parsing payload: #{e.message}"
 status 400
 return
 rescue Stripe::SignatureVerificationError => e
 # Invalid signature
 puts "Error verifying webhook signature: #{e.message}"
 status 400
 return
 end

 # Handle the event
 case event.type
 when 'payment_intent.succeeded'
 payment_intent = event.data.object # contains a Stripe::PaymentIntent
 puts 'PaymentIntent was successful!'
 when 'payment_method.attached'
 payment_method = event.data.object # contains a Stripe::PaymentMethod
 puts 'PaymentMethod was attached to a Customer!'
 # ... handle other event types
 else
 puts "Unhandled event type: #{event.type}"
 end

 status 200
end
```

## Debug webhook integrations

Multiple types of issues can occur when delivering events to your webhook
endpoint:

- Stripe might not be able to deliver an event to your webhook endpoint.
- Your webhook endpoint might have an SSL issue.
- Your network connectivity is intermittent.
- Your webhook endpoint isn’t receiving events that you expect to receive.

### View event deliveries

To view event deliveries, select the webhook endpoint under **Webhooks**, then
select the **Events** tab.

The **Events** tab provides a list of events and whether they’re `Delivered`,
`Pending`, or `Failed`. Click an event to view the `Delivery attempts`, which
includes the HTTP status code of previous delivery attempts and the time of
pending future deliveries.

![View event delivery attempts on a webhook's Events
tab](https://b.stripecdn.com/docs-statics-srv/assets/view-events.a1e821e78eb4ee329f90f584922d6c0d.png)

View event delivery attempts on a webhook endpoint’s **Events** tab.

### Fix HTTP status codes

When an event displays a status code of `200`, it indicates successful delivery
to the webhook endpoint. You might also receive a status code other than `200`.
View the table below for a list of common HTTP status codes and recommended
solutions.

Pending webhook statusDescriptionFix(Unable to connect) ERRWe’re unable to
establish a connection to the destination server.Make sure that your host domain
is publicly accessible to the internet.(`302`) ERR (or other `3xx` status)The
destination server attempted to redirect the request to another location. We
consider redirect responses to webhook requests as failures.Set the webhook
endpoint destination to the URL resolved by the redirect.(`400`) ERR (or other
`4xx` status)The destination server can’t or won’t process the request. This
might occur when the server detects an error (`400`), when the destination URL
has access restrictions, (`401`, `403`), or when the destination URL doesn’t
exist (`404`).- Make sure that your endpoint is publicly accessible to the
internet.
- Make sure that your endpoint accepts a POST HTTP method.
(`500`) ERR (or other `5xx` status)The destination server encountered an error
while processing the request.Review your application’s logs to understand why
it’s returning a `500` error.(TLS error) ERRWe couldn’t establish a secure
connection to the destination server. Issues with the SSL/TLS certificate or an
intermediate certificate in the destination server’s certificate chain usually
cause these errors. Stripe requires
[TLS](https://docs.stripe.com/security/guide#tls) version v1.2 or higher.Perform
an [SSL server test](https://www.ssllabs.com/ssltest/) to find issues that might
cause this error.(Timed out) ERRThe destination server took too long to respond
to the webhook request.Make sure you defer complex logic and return a successful
response immediately in your webhook handling code.
## Event delivery behaviors

This section helps you understand different behaviors to expect regarding how
Stripe sends events to your webhook endpoint.

### Automatic retries

Stripe attempts to deliver events to your destination for up to three days with
an exponential back off in live mode. View when the next retry will occur, if
applicable, in your event destination’s **Event deliveries** tab. We retry event
deliveries created in a sandbox three times over the course of a few hours. If
your destination has been disabled or deleted when we attempt a retry, we
prevent future retries of that event. However, if you disable and then re-enable
the event destination before we’re able to retry, you still see future retry
attempts.

### Manual retries

There are two ways to manually retry events:

- In the Stripe Dashboard, click **Resend** when looking at a specific event.
This works for up to 15 days after the event creation.
- With the [Stripe CLI](https://docs.stripe.com/cli/events/resend), run the
`stripe events resend <event_id> --webhook-endpoint=<endpoint_id>` command. This
works for up to 30 days after the event creation.

### Event ordering

Stripe doesn’t guarantee the delivery of events in the order that they’re
generated. For example, creating a subscription might generate the following
events:

- `customer.subscription.created`
- `invoice.created`
- `invoice.paid`
- `charge.created` (if there’s a charge)

Make sure that your event destination isn’t dependent on receiving events in a
specific order. Be prepared to manage their delivery appropriately. You can also
use the API to retrieve any missing objects. For example, you can retrieve the
invoice, charge, and subscription objects with the information from
`invoice.paid` if you receive this event first.

### API versioning

The API version in your account settings when the event occurs dictates the API
version, and therefore the structure of an
[Event](https://docs.stripe.com/api/v1/events) sent to your destination. For
example, if your account is set to an older API version, such as 2015-02-16, and
you change the API version for a specific request with
[versioning](https://docs.stripe.com/api#versioning), the
[Event](https://docs.stripe.com/api/v1/events) object generated and sent to your
destination is still based on the 2015-02-16 API version. You can’t change
[Event](https://docs.stripe.com/api/v1/events) objects after creation. For
example, if you update a charge, the original charge event remains unchanged. As
a result, subsequent updates to your account’s API version don’t retroactively
alter existing [Event](https://docs.stripe.com/api/v1/events) objects.
Retrieving an older [Event](https://docs.stripe.com/api/v1/events) by calling
`/v1/events` using a newer API version also has no impact on the structure of
the received event. You can set test event destinations to either your default
API version or the latest API version. The
[Event](https://docs.stripe.com/api/v1/events) sent to the destination is
structured for the event destination’s specified version.

## Best practices for using webhooks

Review these best practices to make sure your webhook endpoints remain secure
and function well with your integration.

### Handle duplicate events

Webhook endpoints might occasionally receive the same event more than once. You
can guard against duplicated event receipts by logging the [event
IDs](https://docs.stripe.com/api/events/object#event_object-id) you’ve
processed, and then not processing already-logged events.

In some cases, two separate Event objects are generated and sent. To identify
these duplicates, use the ID of the object in `data.object` along with the
`event.type`.

### Only listen to event types your integration requires

Configure your webhook endpoints to receive only the types of events required by
your integration. Listening for extra events (or all events) puts undue strain
on your server and we don’t recommend it.

You can [change the
events](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
that a webhook endpoint receives in the Dashboard or with the API.

### Handle events asynchronously

Configure your handler to process incoming events with an asynchronous queue.
You might encounter scalability issues if you choose to process events
synchronously. Any large spike in webhook deliveries (for example, during the
beginning of the month when all subscriptions renew) might overwhelm your
endpoint hosts.

Asynchronous queues allow you to process the concurrent events at a rate your
system can support.

### Exempt webhook route from CSRF protection

If you’re using Rails, Django, or another web framework, your site might
automatically check that every POST request contains a *CSRF token*. This is an
important security feature that helps protect you and your users from
[cross-site request
forgery](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF))
attempts. However, this security measure might also prevent your site from
processing legitimate events. If so, you might need to exempt the webhooks route
from CSRF protection.

```
class StripeController < ApplicationController
 # If your controller accepts requests other than Stripe webhooks,
 # you'll probably want to use `protect_from_forgery` to add CSRF
 # protection for your application. But don't forget to exempt
 # your webhook route!
 protect_from_forgery except: :webhook

 def webhook
 # Process webhook data in `params`
 end
end
```

### Receive events with an HTTPS server

If you use an HTTPS URL for your webhook endpoint (required in live mode),
Stripe validates that the connection to your server is secure before sending
your webhook data. For this to work, your server must be correctly configured to
support HTTPS with a valid server certificate. Stripe webhooks support only
[TLS](https://docs.stripe.com/security/guide#tls) versions v1.2 and v1.3.

### Roll endpoint signing secrets periodically

The secret used for verifying that events come from Stripe is modifiable in the
**Webhooks** tab in Workbench. To keep them safe, we recommend that you roll
(change) secrets periodically, or when you suspect a compromised secret.

To roll a secret:

- Click each endpoint in the Workbench **Webhooks** tab that you want to roll
the secret for.
- Navigate to the overflow menu () and click **Roll secret**. You can choose to
immediately expire the current secret or delay its expiration for up to 24 hours
to allow yourself time to update the verification code on your server. During
this time, multiple secrets are active for the endpoint. Stripe generates one
signature per secret until expiration.

### Verify events are sent from Stripe

Stripe sends webhook events from a set list of IP addresses. Only trust events
coming from these [IP addresses](https://docs.stripe.com/ips).

Additionally, verify webhook signatures to confirm that received events are sent
from Stripe. Stripe signs webhook events it sends to your endpoints by including
a signature in each event’s `Stripe-Signature` header. This allows you to verify
that the events were sent by Stripe, not by a third party. You can verify
signatures either using our [official
libraries](https://docs.stripe.com/webhooks#verify-official-libraries), or
[verify manually](https://docs.stripe.com/webhooks#verify-manually) using your
own solution.

The following section describes how to verify webhook signatures:

- Retrieve your endpoint’s secret.
- Verify the signature.

#### Retrieving your endpoint’s secret

Use Workbench and navigate to the **Webhooks** tab to view all your endpoints.
Select an endpoint that you want to obtain the secret for, then click **Click to
reveal**.

Stripe generates a unique secret key for each endpoint. If you use the same
endpoint for both [test and live API
keys](https://docs.stripe.com/keys#test-live-modes), the secret is different for
each one. Additionally, if you use multiple endpoints, you must obtain a secret
for each one you want to verify signatures on. After this setup, Stripe starts
to sign each webhook it sends to the endpoint.

### Preventing replay attacks

A [replay attack](https://en.wikipedia.org/wiki/Replay_attack) is when an
attacker intercepts a valid payload and its signature, then re-transmits them.
To mitigate such attacks, Stripe includes a timestamp in the `Stripe-Signature`
header. Because this timestamp is part of the signed payload, it’s also verified
by the signature, so an attacker can’t change the timestamp without invalidating
the signature. If the signature is valid but the timestamp is too old, you can
have your application reject the payload.

Our libraries have a default tolerance of 5 minutes between the timestamp and
the current time. You can change this tolerance by providing an additional
parameter when verifying signatures. Use Network Time Protocol
([NTP](https://en.wikipedia.org/wiki/Network_Time_Protocol)) to make sure that
your server’s clock is accurate and synchronizes with the time on Stripe’s
servers.

#### Common mistake

Don’t use a tolerance value of `0`. Using a tolerance value of `0` disables the
recency check entirely.

Stripe generates the timestamp and signature each time we send an event to your
endpoint. If Stripe retries an event (for example, your endpoint previously
replied with a non-`2xx` status code), then we generate a new signature and
timestamp for the new delivery attempt.

### Quickly return a 2xx response

Your [endpoint](https://docs.stripe.com/webhooks#example-endpoint) must quickly
return a successful status code (`2xx`) prior to any complex logic that could
cause a timeout. For example, you must return a `200` response before updating a
customer’s invoice as paid in your accounting system.

## See also

- [Send events to Amazon
EventBridge](https://docs.stripe.com/event-destinations/eventbridge)
- [List of notification event
types](https://docs.stripe.com/api/v2/events/event-types)
- [List of change event types](https://docs.stripe.com/api/events/)
- [Interactive webhook endpoint
builder](https://docs.stripe.com/webhooks/quickstart)

## Links

- [Amazon EventBridge as an event
destination](https://docs.stripe.com/event-destinations/eventbridge)
- [events](https://docs.stripe.com/event-destinations#events-overview)
- [Event object](https://docs.stripe.com/api/events)
- [event destination](https://docs.stripe.com/event-destinations)
- [notification event objects](https://stripe.com/api/v2/events/event-types)
- [change event objects](https://docs.stripe.com/api/events/object)
- [interactive webhook endpoint
builder](https://docs.stripe.com/webhooks/quickstart)
- [CLI](https://docs.stripe.com/stripe-cli)
- [Stripe events](https://docs.stripe.com/cli/trigger#trigger-event)
- [Stripe Shell](https://docs.stripe.com/stripe-shell/overview)
- [Stripe for VS Code](https://docs.stripe.com/stripe-vscode)
- [API](https://docs.stripe.com/api/v2/event-destinations)
- [Webhooks](https://dashboard.stripe.com/webhooks)
- [Connected accounts](https://docs.stripe.com/connect)
- [event types](https://docs.stripe.com/api/events/types)
- [Workbench](https://docs.stripe.com/workbench)
- [Developers Dashboard](https://docs.stripe.com/development/dashboard)
- [create a new webhook
endpoint](https://docs.stripe.com/development/dashboard/webhooks)
- [webhook best practices](https://docs.stripe.com/webhooks#best-practices)
- [troubleshooting it](https://docs.stripe.com/webhooks/signature)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [listen for events](https://docs.stripe.com/webhooks#test-webhook)
- [TLS](https://docs.stripe.com/security/guide#tls)
- [SSL server test](https://www.ssllabs.com/ssltest/)
- [Stripe CLI](https://docs.stripe.com/cli/events/resend)
- [Event](https://docs.stripe.com/api/v1/events)
- [versioning](https://docs.stripe.com/api#versioning)
- [event IDs](https://docs.stripe.com/api/events/object#event_object-id)
- [change the
events](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
- [cross-site request
forgery](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF))
- [IP addresses](https://docs.stripe.com/ips)
- [test and live API keys](https://docs.stripe.com/keys#test-live-modes)
- [replay attack](https://en.wikipedia.org/wiki/Replay_attack)
- [NTP](https://en.wikipedia.org/wiki/Network_Time_Protocol)
- [endpoint](https://docs.stripe.com/webhooks#example-endpoint)
- [List of notification event
types](https://docs.stripe.com/api/v2/events/event-types)
- [List of change event types](https://docs.stripe.com/api/events/)