# Issuing real-time authorizations

## Learn about real-time authorizations.

Using the synchronous webhook, you can approve or decline authorization requests
in real time.

Your webhook endpoint can be configured in your
[settings](https://dashboard.stripe.com/account/issuing). When a card is used to
make a purchase, Stripe creates an `issuing_authorization.request` and sends it
to your configured endpoint for your approval.

Get started with our [interactive guide to real-time
authorizations](https://docs.stripe.com/issuing/controls/real-time-authorizations/quickstart).

## Responding to authorization requests

You can respond to authorization requests by responding directly to the webhook
event.

### Respond directly

Respond to the `issuing_authorization.request` webhook event directly to either
approve or decline an authorization after it’s received.

#### Webhook response

Our webhook accepts `JSON` responses with the following parameters:

**Status code:** Return `200` to indicate success.

**Header:**

field name required or optional description Stripe-VersionrequiredVersion in
`YYYY-dd-mm` format.Content-TypeoptionalThe only content type accepted for
Authorization webhook responses is `application/json`.
**Body:**

field name required or optional type description approvedrequiredBooleanSet
`true` to approve an authorization and `false` to
decline.amountoptionalIntegerIf the authorization’s
`pending_request.is_amount_controllable` property is `true`, you can provide
this value to control how much to hold for the authorization. It must be
positive.metadataoptionalSet of [key-value
pairs](https://docs.stripe.com/api/metadata)This can be useful for storing
additional information about the object in a structured
format.send_fraud_challenges Public previewoptionalArray of stringsYou can send
a fraud challenge for this authorization only through SMS. Leave it blank if you
don’t want to send a challenge.
```
# Using Sinatra.
require 'sinatra'
require 'stripe'

set :port, 4242

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# Replace with a real secret. You can find your endpoint's secret in your webhook settings.
webhook_secret = 'whsec_...'

post '/webhook' do
 payload = request.body.read
 sig_header = request.env['HTTP_STRIPE_SIGNATURE']

 event = nil

 # Verify webhook signature and extract the event.
 begin
 event = Stripe::Webhook.construct_event(
 payload, sig_header, webhook_secret
 )
 rescue JSON::ParserError => e
 # Invalid payload.
 status 400
 return
 rescue Stripe::SignatureVerificationError => e
 # Invalid signature.
 status 400
 return
 end

 if event['type'] == 'issuing_authorization.request'
 auth = event['data']['object']
 # ... custom business logic

 status 200
header 'Stripe-Version' => '2022-08-01', 'Content-Type' => 'application/json'
 data = { 'approved' => true }
 body data.to_json
 end
 # ...handle other cases
end
```

### Make an API call Deprecated

This documentation is maintained for existing users. If you’re a new user,
respond directly to the webhook. If you’re an existing user, plan to migrate to
the direct webhook response. You can follow [our direct webhook migration
guide](https://docs.stripe.com/issuing/controls/real-time-authorizations/direct-webhook-migration).

Make an API call to either
[approve](https://docs.stripe.com/api/issuing/authorizations/approve) or
[decline](https://docs.stripe.com/api/issuing/authorizations/decline) the
request and include the
[Authorization](https://docs.stripe.com/api/issuing/authorizations/object) ID.
If you use this method, your webhook must approve or decline each authorization
before responding to the incoming webhook request.

```
# Using Sinatra.
require 'sinatra'
require 'stripe'

set :port, 4242

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# Uncomment and replace with a real secret. You can find your endpoint's
# secret in your webhook settings.
# webhook_secret = 'whsec_...'

post '/webhook' do
 payload = request.body.read
 sig_header = request.env['HTTP_STRIPE_SIGNATURE']

 event = nil

 # Verify webhook signature and extract the event.
 begin
 event = Stripe::Webhook.construct_event(
 payload, sig_header, webhook_secret
 )
 rescue JSON::ParserError => e
 # Invalid payload.
 status 400
 return
 rescue Stripe::SignatureVerificationError => e
 # Invalid signature.
 status 400
 return
 end

 if event['type'] == 'issuing_authorization.request'
 auth = event['data']['object']
 handle_authorization(auth)
 end

 status 200
end

def handle_authorization(auth)
 # Authorize the transaction
 authorization = Stripe::Issuing::Authorization.approve(auth["id"])
end
```

We recommend that you only use one of these two methods to respond to
authorization requests. For users migrating from one method to another, both
methods are supported during a migration. In the event both methods are used on
the same authorization, the API call takes precedence over the direct response.
For migrations, we recommend only using one method on a given request at a time.

If Stripe doesn’t receive your approve or decline response or request within 2
seconds, the `Authorization` is automatically approved or declined based on your
[timeout settings](https://dashboard.stripe.com/account/issuing).

#### Note

If your Issuing balance has insufficient funds for the incoming authorization,
the authorization will be denied and your webhook endpoint will not receive the
`issuing_authorization.request` event. To learn more about funding your Issuing
balance, [read here](https://docs.stripe.com/issuing/funding/balance).

## Authorization requests

When an authorization request is sent to your webhook, the `amount` requested is
stored in `pending_request`.

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing_authorization",
 "approved": false,
 "amount": 0,
 "currency": "usd",
 "status": "pending",
 ...
 "pending_request": {
 "amount": 400,
 "currency": "usd",
 "merchant_amount": 360,
 "merchant_currency": "gbp"
 }
}
```

The top-level `amount` in the request is set to 0 and `approved` is false. Once
you respond to the request, the top-level `amount` reflects the total amount
approved or declined, the `approved` field is updated, and `pending_request` is
set to null.

### Testing webhooks locally

To test webhooks locally, you can use [Stripe
CLI](https://docs.stripe.com/stripe-cli). Once you have it installed, you can
forward events to your server:

```
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

In another terminal, you can then manually trigger
`issuing_authorization.request` events from the CLI for more streamlined
testing.

```
stripe trigger issuing_authorization.request
```

Learn more about [setting up webhooks](https://docs.stripe.com/webhooks).

## Autopilot Public preview

Autopilot is a set of fallback options that allow you to continue making
real-time authorization decisions in the event your systems are down or don’t
respond to an authorization request within the allotted time window.

For users with their own dedicated Bank Identification Numbers (BIN), we also
offer Autopilot in the event that Stripe can’t communicate with the network to
prevent any continuity issues that might result.

In both cases, we make an authorization decision on your behalf based on a
predefined set of rules. We create authorization objects for transmission, so
that reconciliation can take place for the Autopilot transactions. When an
authorization is approved or declined through Autopilot while you’re down, the
`request_history.reason` field within the `issuing_authorization.created`
webhook changes to `webhook_timeout`. When an authorization is approved or
declined through Autopilot while Stripe is down, the `request_history.reason`
field within the `issuing_authorization.created` webhook changes to
`network_stip`.

Access to Autopilot is currently limited to US beta users. You must be an
Issuing customer to join the beta. To request access to the beta, log in to your
Stripe account and refresh the page. [Contact
Stripe](https://stripe.com/contact/sales) for more information.

## Fraud challenges Public preview

[Fraud challenges](https://docs.stripe.com/issuing/controls/fraud-challenges)
allow your cardholders to retry non-fraudulent transactions that would have
otherwise been blocked.

To manage the rules that dictate when a fraud challenge is sent, adjust your
response to the `issuing_authorization.request` webhook. You can trigger fraud
challenges in scenarios where you detect spending that appears suspicious and
want additional verification (for example, a cardholder using their card out of
the country).

To do so, decline the `issuing_authorization.request` webhook and include the
`send_fraud_challenges` field with the `["sms"]` value.

Fraud challenges are currently limited to beta users. You must be an Issuing
customer to join the beta. To request access to the beta, log in to your Stripe
account and refresh the page. [Contact Stripe](https://stripe.com/contact/sales)
for more information.

## Enriched merchant data Private preview

The `enriched_merchant_data` hash on Issuing authorization webhooks passes more
comprehensive merchant data in events, such as:

- Merchant categories
- Location data
- Third parties

You can use these details to build more robust authorization logic and
downstream user interfaces.

Common use case examples include:

- Creating real time spend controls
- Automating transaction categorization
- Developing better fraud detection and prevention

## Links

- [settings](https://dashboard.stripe.com/account/issuing)
- [interactive guide to real-time
authorizations](https://docs.stripe.com/issuing/controls/real-time-authorizations/quickstart)
- [key-value pairs](https://docs.stripe.com/api/metadata)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [our direct webhook migration
guide](https://docs.stripe.com/issuing/controls/real-time-authorizations/direct-webhook-migration)
- [approve](https://docs.stripe.com/api/issuing/authorizations/approve)
- [decline](https://docs.stripe.com/api/issuing/authorizations/decline)
- [Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
- [read here](https://docs.stripe.com/issuing/funding/balance)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [setting up webhooks](https://docs.stripe.com/webhooks)
- [Contact Stripe](https://stripe.com/contact/sales)
- [Fraud challenges](https://docs.stripe.com/issuing/controls/fraud-challenges)