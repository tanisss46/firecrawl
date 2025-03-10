# Create payment links with Connect

## With Connect, you can create payment links for connected accounts, optionally taking fees in the process.

You can create [payment links](https://docs.stripe.com/payment-links) for
connected accounts, which support [several
approaches](https://docs.stripe.com/connect/charges) for collecting payments.
You can use [direct charges](https://docs.stripe.com/connect/direct-charges) to
create them directly on the connected account. Alternatively, you can create
payment links on the platform with transfers to the connected account by using
[destination charges](https://docs.stripe.com/connect/destination-charges). You
can also take an application fee on these payment links.

## Create a payment link using direct charges

To create an payment link that directly charges on a connected account, [create
a payment link](https://docs.stripe.com/api#create_payment_link) while
[authenticated](https://docs.stripe.com/connect/authentication#stripe-account-header)
as the connected account. For this to work, you must also create the
[product](https://docs.stripe.com/api#create_product) and the
[price](https://docs.stripe.com/api#create_price) on the connected account.

```
curl https://api.stripe.com/v1/payment_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1
```

When you use direct charges, the connected account is responsible for the cost
of the Stripe fees, refunds, and chargebacks.

## Create a payment link using destination charges

To create a payment link that charges on the platform and creates automatic
transfers to a connected account, [create a payment
link](https://docs.stripe.com/api#create_payment_link) while providing the
connected account ID as the `transfer_data[destination]`
[value](https://docs.stripe.com/api/payment_links/payment_links/object#payment_link_object-transfer_data).

```
curl https://api.stripe.com/v1/payment_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

For this to work, you must also create the
[product](https://docs.stripe.com/api#create_product) and the
[price](https://docs.stripe.com/api#create_price) on the platform account. When
using automatic transfers, the platform is the business of record.

When performing destination charges, Payment Links uses the brand settings of
your platform account for the payment page. See the [Customize
branding](https://docs.stripe.com/connect/payment-links#customize-branding)
section for more information.

## Create a payment link using destination charges and on_behalf_of

You can also create a destination charge with the `on_behalf_of` parameter set
to the connected account ID (by default, it is the platform). The `on_behalf_of`
parameter determines the settlement merchant, which affects:

- Whose statement descriptor the end user sees
- Whose address and phone number the end user sees
- The settlement currency of the charge
- The payment page branding the customer sees

```
curl https://api.stripe.com/v1/payment_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d on_behalf_of={{CONNECTED_ACCOUNT_ID}} \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

## Fulfill orders placed through payment links

After an end user pays through a payment link you need to enable your connected
accounts to handle any fulfillment necessary.

Configure a [webhook](https://docs.stripe.com/webhooks) endpoint [in the
Dashboard](https://dashboard.stripe.com/account/webhooks).

![Webhooks page in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/account_webhooks.03b71cec87ef2093fe0caa92e5bfce44.png)

Then create an HTTP endpoint on your server to monitor for completed payments.
Make sure to replace the endpoint secret key (`whsec_...`) in the example with
your key.

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

 if event['type'] == 'checkout.session.completed'
 session = event['data']['object']
 connected_account_id = event['account']
 handle_completed_checkout_session(connected_account_id, session)
 end

 status 200
end

def handle_completed_checkout_session(connected_account_id, session)
 # Fulfill the purchase
 puts 'Connected account ID: ' + connected_account_id
 puts session.to_s
end
```

Learn more in our [fulfillment
guide](https://docs.stripe.com/checkout/fulfillment).

[OptionalCollect application
fees](https://docs.stripe.com/connect/payment-links#collecting-fees)[OptionalCustomize
branding](https://docs.stripe.com/connect/payment-links#customize-branding)[OptionalIntegrate
tax calculation and
collection](https://docs.stripe.com/connect/payment-links#connect-tax)

## Links

- [Connect](https://docs.stripe.com/connect)
- [payment links](https://docs.stripe.com/payment-links)
- [several approaches](https://docs.stripe.com/connect/charges)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [create a payment link](https://docs.stripe.com/api#create_payment_link)
-
[authenticated](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [product](https://docs.stripe.com/api#create_product)
- [price](https://docs.stripe.com/api#create_price)
-
[value](https://docs.stripe.com/api/payment_links/payment_links/object#payment_link_object-transfer_data)
- [Customize
branding](https://docs.stripe.com/connect/payment-links#customize-branding)
- [webhook](https://docs.stripe.com/webhooks)
- [in the Dashboard](https://dashboard.stripe.com/account/webhooks)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)
- [fulfillment guide](https://docs.stripe.com/checkout/fulfillment)