# Connect webhooks

## Learn how to use webhooks with Connect to be notified of Stripe activity.

Stripe uses [webhooks](https://docs.stripe.com/webhooks) to notify your
application when an event happens in your account. All
[Connect](https://docs.stripe.com/connect) integrations should establish a
[webhook endpoint](https://dashboard.stripe.com/account/webhooks) to listen for
Connect events.

## Connect webhooks

There are a few types of webhooks:

- *Account* webhooks are for activity on your own account (for example, most
requests made using your API keys and without [authenticating as another Stripe
account](https://docs.stripe.com/connect/authentication)). This includes all
types of charges, except those made directly on a connected account.
- *Connect* webhooks are for activity on any connected account. All events on
the connected account are sent to the Connect webhooks. This includes the
important `account.updated` event for any connected account and direct charges.

When creating your webhook, ensure it is correctly configured to receive Connect
webhook events. You can do this with the API by setting the [connect
parameter](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-connect)
to `true` when creating the webhook endpoint, or [through the
Dashboard](https://dashboard.stripe.com/test/webhooks).

![Webhook settings in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/webhooks.ac3d6c19a5281fbbd2b85a335cd887b3.png)

For Connect webhooks, only test webhooks are sent to your development webhook
URLs, but *both live and test* webhooks are sent to your production webhook
URLs. This is because you can perform both live and test transactions under a
production application. For this reason, we recommend that you check the
`livemode` value when receiving an event webhook to know what action, if any,
users should take.

As we state in the [event object
reference](https://docs.stripe.com/api/events/object), each event for a
connected account also contains a top-level `account` property. It identifies
the account that the webhook is sent to and the `data[object]` it belongs to.
Because these objects belong to other accounts, you must make the API requests
[as the corresponding connected
account](https://docs.stripe.com/connect/authentication) to access them.

```
{
 "id": "{{EVENT_ID}}",
 "livemode": true,
 "object": "event",
 "type": "customer.created",
 "account": "{{CONNECTED_ACCOUNT_ID}}",
 "pending_webhooks": 2,
 "created": 1349654313,
 "data": {...}
}
```

There are several events related to accounts that Stripe recommends listening
for:

Eventdata.object
typeDescription`account.application.deauthorized``application`Occurs when a
connected account disconnects from your platform. You can use it to trigger
cleanup on your server. Available for connected accounts with access to the
Stripe Dashboard, which includes [Standard
accounts](https://docs.stripe.com/connect/standard-accounts).`account.external_account.updated`An
external account, such as `card` or `bank_account`Occurs when [a bank account or
debit card attached to a connected account is
updated](https://docs.stripe.com/connect/payouts-bank-accounts), which can
impact payouts. Available for connected accounts that your platform controls,
which includes Custom and Express accounts, and Standard accounts with [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
enabled.`account.updated``account`Allows you to monitor changes to connected
account requirements and status changes. Available for all connected
accounts.`balance.available``balance`Occurs when your Stripe balance has been
updated (for example, when [funds you’ve added from your bank
account](https://docs.stripe.com/connect/add-and-pay-out-guide#add-funds) are
available for transfer to your connected
account).`payment_intent.succeeded``payment_intent`Occurs when a payment intent
results in a successful charge. Available for all payments, including
[destination](https://docs.stripe.com/connect/collect-then-transfer-guide#fulfillment)
and [direct](https://docs.stripe.com/connect/enable-payment-acceptance-guide)
charges.`payout.failed``payout`Occurs when [a payout
fails](https://docs.stripe.com/connect/payouts-connected-accounts#webhooks).
When a payout fails, the external account involved is disabled, and no automatic
or manual payouts can be processed until the external account is
updated.`person.updated``person`If you [use the Persons
API](https://docs.stripe.com/connect/handling-api-verification#verification-process),
allows you to monitor changes to requirements and status changes for
individuals. Available for connected accounts that your platform controls, which
includes Custom and Express accounts, and Standard accounts with [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
enabled.Event:account.application.deauthorizedaccount.updatedperson.updatedpayment_intent.succeeded,
direct chargepayment_intent.succeeded, non-direct
chargebalance.availableaccount.external_account.updatedpayout.failed
```
# Using Sinatra.
require 'sinatra'
require 'stripe'

set :port, 4242

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# If you are testing your webhook locally with the Stripe CLI you
# can find the endpoint's secret by running `stripe listen`
# Otherwise, find your endpoint's secret in your webhook settings in
# the Developer Dashboard
endpoint_secret = 'whsec_...'

post '/webhook' do
 payload = request.body.read
 sig_header = request.env['HTTP_STRIPE_SIGNATURE']

 event = nil

 # Verify webhook signature and extract the event.
 # See https://stripe.com/docs/webhooks#verify-events for more information.
 begin
 event = Stripe::Webhook.construct_event(
 payload, sig_header, endpoint_secret
 )
 rescue JSON::ParserError => e
 # Invalid payload.
 status 400
 return
 rescue Stripe::SignatureVerificationError => e
 # Invalid Signature.
 status 400
 return
 end

 if event['type'] == 'account.application.deauthorized'
 application = event['data']['object']
 connected_account_id = event['account']
 handle_deauthorization(connected_account_id, application)
 end

 status 200
end

def handle_deauthorization(connected_account_id, application)
 # Clean up account state.
 puts 'Connected account ID: ' + connected_account_id
 puts application.to_s
end
```

The events listed above are the ones we typically recommend Connect integrations
listen for, but there are [many other event
types](https://docs.stripe.com/api/events/types) you may be interested in.

## Test webhooks locally

You can test webhooks locally with the Stripe CLI.

- If you haven’t already, [install the Stripe
CLI](https://docs.stripe.com/stripe-cli#install) on your machine.
- Log in to your Stripe account and set up the CLI by running `stripe login` on
the command line.
- Allow your local host to receive a simulated event on your connected account
by running `stripe listen --forward-to localhost:{PORT}/webhook` in one terminal
window, and running `stripe trigger {{EVENT_NAME}}` in another.

#### Note

For Connect webhooks, use
[–forward-connect-to](https://docs.stripe.com/cli/listen#listen-forward-connect-to)
with `stripe listen` and
[–stripe-account](https://docs.stripe.com/cli/trigger#trigger-stripe_account)
with `stripe trigger`.

## See also

- [Webhook documentation](https://docs.stripe.com/webhooks)
- [Event object reference](https://docs.stripe.com/api#events)

## Links

- [webhooks](https://docs.stripe.com/webhooks)
- [Connect](https://docs.stripe.com/connect)
- [webhook endpoint](https://dashboard.stripe.com/account/webhooks)
- [authenticating as another Stripe
account](https://docs.stripe.com/connect/authentication)
- [connect
parameter](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-connect)
- [through the Dashboard](https://dashboard.stripe.com/test/webhooks)
- [event object reference](https://docs.stripe.com/api/events/object)
- [Standard accounts](https://docs.stripe.com/connect/standard-accounts)
- [a bank account or debit card attached to a connected account is
updated](https://docs.stripe.com/connect/payouts-bank-accounts)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [funds you’ve added from your bank
account](https://docs.stripe.com/connect/add-and-pay-out-guide#add-funds)
-
[destination](https://docs.stripe.com/connect/collect-then-transfer-guide#fulfillment)
- [direct](https://docs.stripe.com/connect/enable-payment-acceptance-guide)
- [a payout
fails](https://docs.stripe.com/connect/payouts-connected-accounts#webhooks)
- [use the Persons
API](https://docs.stripe.com/connect/handling-api-verification#verification-process)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)
- [many other event types](https://docs.stripe.com/api/events/types)
- [install the Stripe CLI](https://docs.stripe.com/stripe-cli#install)
-
[–forward-connect-to](https://docs.stripe.com/cli/listen#listen-forward-connect-to)
- [–stripe-account](https://docs.stripe.com/cli/trigger#trigger-stripe_account)
- [Event object reference](https://docs.stripe.com/api#events)