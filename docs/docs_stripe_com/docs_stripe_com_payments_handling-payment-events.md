# Triggering actions with webhooks

## How to use webhooks to respond to offline payment events.

A [webhook](https://docs.stripe.com/webhooks) is an HTTP endpoint that receives
events from Stripe.

Webhooks allow you to be notified about payment events that happen outside of
your payment flow such as:

- Successful payments (`payment_intent.succeeded`)
- Disputed payments (`charge.dispute.created`)
- Available balance in your Stripe account (`balance.available`)

You can use the Dashboard for one-off actions like refunding a payment or
updating a customer’s information, while webhooks help you scale your payments
integration and process large volumes of business-critical events.

## Build your own webhook

You can build a webhook handler on your own server to manage all your offline
payment flows. Start by exposing an endpoint that can receive requests from
Stripe and use the CLI to locally test your integration. Each request from
Stripe contains an [Event](https://docs.stripe.com/api/events/object) object
with a reference to the object on Stripe that was modified.

[Create a webhook
endpoint](https://docs.stripe.com/payments/handling-payment-events#create-webhook)
Add a new endpoint in your application. You can act on certain events by
checking the `type` field of the event object sent in the request body. Then you
can print to standard output to make sure your webhook is working.

Start your server after adding the new endpoint.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

require 'stripe'
require 'sinatra'
require 'json'

# Using the Sinatra framework
set :port, 4242

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

[Install and set up the Stripe
CLI](https://docs.stripe.com/payments/handling-payment-events#install-cli)
```
# Install Homebrew to run this command: https://brew.sh/
brew install stripe/stripe-cli/stripe

# Connect the CLI to your dashboard
stripe login
```

For additional install options, see [Get started with the Stripe
CLI](https://docs.stripe.com/stripe-cli).

After you have the Stripe CLI installed, run `stripe login` in the command line
to generate a pairing code to link to your Stripe account. Press **Enter** to
launch your browser and log in to your Stripe account to allow access. The
generated API key is valid for 90 days. You can modify or delete the key under
[API Keys](https://dashboard.stripe.com/apikeys) in the Dashboard.

#### Note

You can create a project-specific configuration by including the
[–project-name](https://docs.stripe.com/cli/login#login-project-name) flag when
you log in and when you run commands for that project.

Test

```
stripe login
Your pairing code is: humour-nifty-finer-magic
Press Enter to open up the browser (^C to quit)
```

If you want to use an existing API key, use the `--api-key` flag:

```
stripe login --api-key sk_test_BQokikJOvBiI2HlWgH4olfQ2
Your pairing code is: humour-nifty-finer-magic
Press Enter to open up the browser (^C to quit)
```

[Test your webhook
locally](https://docs.stripe.com/payments/handling-payment-events#use-cli)
Use the CLI to forward events to your local webhook endpoint using the `listen`
command.

Assuming your application is running on port 4242, run:

```
stripe listen --forward-to http://localhost:4242/webhook
```

In a different terminal tab, use the `trigger` CLI command to trigger a mock
webhook event.

```
stripe trigger payment_intent.succeeded
```

The following event appears in your `listen` tab:

```
[200 POST] OK payment_intent.succeeded
```

“PaymentIntent was successful!” appears in the terminal tab your server is
running.

[OptionalCheck webhook
signature](https://docs.stripe.com/payments/handling-payment-events#signature-checking)[Deploy
your webhook
endpoint](https://docs.stripe.com/payments/handling-payment-events#deploy-endpoint)
When you’re ready to deploy your webhook endpoint to production you need to do
the following:

- Use your [live mode API keys](https://docs.stripe.com/keys#test-live-modes)
and not your test mode keys.
- Configure your webhook endpoint in the Stripe Dashboard or with the API.

To configure your endpoint in the Dashboard, go to your [webhook
settings](https://dashboard.stripe.com/webhooks).

Click **Add endpoint** and enter the URL of your endpoint, the Stripe API
version, and the specific events you want Stripe to send.

Replace the webhook endpoint secret in your application with the new secret
shown in the Dashboard view of your endpoint.

Your application is now ready to accept live events. For more information on
configuring your webhook endpoint, see the [Webhook
Endpoint](https://docs.stripe.com/api/webhook_endpoints) API. For testing in
test mode, [see our Development guide](https://docs.stripe.com/webhooks).

## Links

- [webhook](https://docs.stripe.com/webhooks)
- [Event](https://docs.stripe.com/api/events/object)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [https://brew.sh/](https://brew.sh/)
- [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [–project-name](https://docs.stripe.com/cli/login#login-project-name)
- [http://localhost:4242/webhook](http://localhost:4242/webhook)
- [live mode API keys](https://docs.stripe.com/keys#test-live-modes)
- [webhook settings](https://dashboard.stripe.com/webhooks)
- [Webhook Endpoint](https://docs.stripe.com/api/webhook_endpoints)