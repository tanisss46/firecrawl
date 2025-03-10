# Build a subscriptions integration

## Create and manage subscriptions to accept recurring payments.

WebiOSAndroidReact NativeStripe-hosted pageEmbedded formCustom flow

![Checkout subscription
page](https://b.stripecdn.com/docs-statics-srv/assets/checkout-subs-preview.d409ee79bf1f3280b9dfd3968b314c21.png)

Low code
Customize logo, images, and colors.

Use prebuilt hosted forms to collect payments and manage
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating).

Clone a sample integration [from
GitHub](https://github.com/stripe-samples/checkout-single-subscription).

For an immersive version of this guide, see the [Billing integration
quickstart](https://docs.stripe.com/billing/quickstart).

Explore the [sample on
GitHub](https://github.com/stripe-samples/checkout-single-subscription) or the
[demo](https://checkout.stripe.dev/).

## What you’ll build

This guide describes how to sell fixed-price monthly subscriptions using [Stripe
Checkout](https://docs.stripe.com/payments/checkout).

This guide shows you how to:

- Model your business by building a product catalog
- Add a Checkout session to your site, including a button and success and
cancellation pages
- Monitor subscription events and provision access to your service
- Set up the [customer portal](https://docs.stripe.com/customer-management)
- Add a customer portal session to your site, including a button and redirect
- Let customers manage their subscription through the portal

After you complete the integration, you can extend it to:

- [Display taxes](https://docs.stripe.com/payments/checkout/taxes)
- [Apply
discounts](https://docs.stripe.com/billing/subscriptions/coupons#using-coupons-in-checkout)
- [Offer customers a free trial
period](https://docs.stripe.com/billing/subscriptions/trials)
- [Add more payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Integrate the hosted invoice
page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Use Checkout in setup mode](https://docs.stripe.com/payments/save-and-reuse)
- [Set up metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing),
[pricing
tiers](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing),
and [usage-based
pricing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [Manage prorations](https://docs.stripe.com/billing/subscriptions/prorations)
- [Allow customers to subscribe to multiple
products](https://docs.stripe.com/billing/subscriptions/multiple-products)
- [Integrate entitlements to manage access to your product’s
features](https://docs.stripe.com/billing/entitlements)
[Set up
Stripe](https://docs.stripe.com/billing/subscriptions/build-subscriptions#set-up-stripe)
Install the Stripe client of your choice:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

Install the Stripe CLI (optional). The CLI provides
[webhook](https://docs.stripe.com/webhooks#test-webhook) testing, and you can
run it to create your products and prices.

```
# Install Homebrew to run this command: https://brew.sh/
brew install stripe/stripe-cli/stripe

# Connect the CLI to your dashboard
stripe login
```

For additional install options, see [Get started with the Stripe
CLI](https://docs.stripe.com/stripe-cli).

[Create the pricing modelDashboard or Stripe
CLI](https://docs.stripe.com/billing/subscriptions/build-subscriptions#create-pricing-model)
Create your [products](https://docs.stripe.com/api/products) and their
[prices](https://docs.stripe.com/api/prices) in the Dashboard or with the Stripe
CLI.

This example uses a fixed-price service with two different service-level
options: Basic and Premium. For each service-level option, you need to create a
product and a recurring price. (If you want to add a one-time charge for
something like a setup fee, create a third product with a one-time price. To
keep things simple, this example doesn’t include a one-time charge.)

In this example, each product bills at monthly intervals. The price for the
Basic product is 5 USD. The price for the Premium product is 15 USD.

DashboardStripe CLI
Go to the [Add a product](https://dashboard.stripe.com/test/products/create)
page and create two products. Add one price for each product, each with a
monthly recurring billing period:

- Premium product: Premium service with extra features

- Price: Standard pricing | 15 USD
- Basic product: Basic service with minimum features

- Price: Standard pricing | 5 USD

After you create the prices, record the price IDs so you can use them in other
steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the ** to live mode** button at the top right of the
page to clone your product from [test mode to live
mode](https://docs.stripe.com/keys#test-live-modes).

If you offer multiple billing intervals, use Checkout to
[upsell](https://docs.stripe.com/payments/checkout/upsells) customers on longer
billing intervals and collect more revenue upfront.

For other pricing models, see [Billing
examples](https://docs.stripe.com/products-prices/pricing-models).

[Create a Checkout SessionClient and
Server](https://docs.stripe.com/billing/subscriptions/build-subscriptions#create-session)
Add a checkout button to your website that calls a server-side endpoint to
create a Checkout Session.

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <!-- Note: If using PHP set the action to /create-checkout-session.php -->

 <input type="hidden" name="priceId" value="price_G0FvDp6vZvdwRZ" />
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

On the backend of your application, define an endpoint that [creates the
session](https://docs.stripe.com/api/checkout/sessions/create) for your frontend
to call. You need these values:

- The price ID of the subscription the customer is signing up for—your frontend
passes this value
- Your `success_url`, a page on your website that Checkout returns your customer
to after they complete the payment

You can optionally provide `cancel_url`, a page on your website that Checkout
returns your customer to if they cancel the payment process. You can also
configure a [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle) to your
subscription in this call.

If you created a one-time price in [step
2](https://docs.stripe.com/billing/subscriptions/build-subscriptions#create-pricing-model),
pass that price ID as well. After creating a Checkout Session, redirect your
customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

#### Note

You can use
[lookup_keys](https://docs.stripe.com/products-prices/manage-prices#lookup-keys)
to fetch prices rather than Price IDs. See the [sample
application](https://github.com/stripe-samples/subscription-use-cases/tree/main/fixed-price-subscriptions)
for an example.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# The price ID passed from the front end.
# price_id = params['priceId']
price_id = '{{PRICE_ID}}'

session = Stripe::Checkout::Session.create({
success_url:
'https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}',
 cancel_url: 'https://example.com/canceled.html',
 mode: 'subscription',
 line_items: [{
 # For metered billing, do not pass quantity
 quantity: 1,
 price: price_id,
 }],
})

# Redirect to the URL returned on the session
# redirect session.url, 303
```

This example customizes the `success_url` by appending the Session ID. For more
information about this approach, see the documentation on how to [Customize your
success page](https://docs.stripe.com/payments/checkout/custom-success-page).

From your [Dashboard](https://dashboard.stripe.com/settings/payment_methods),
enable the payment methods you want to accept from your customers. Checkout
supports [several payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support).

[Provision and monitor
subscriptionsServer](https://docs.stripe.com/billing/subscriptions/build-subscriptions#provision-and-monitor)
After the subscription signup succeeds, the customer returns to your website at
the `success_url`, which initiates a `checkout.session.completed`
[webhooks](https://docs.stripe.com/webhooks). When you receive a
`checkout.session.completed` event, you can [provision the
subscription](https://docs.stripe.com/billing/subscriptions/overview#provisioning).
Continue to provision each month (if billing monthly) as you receive
`invoice.paid` events. If you receive an `invoice.payment_failed` event, notify
your customer and send them to the customer portal to update their payment
method.

To determine the next step for your system’s logic, check the event type and
parse the payload of each [event
object](https://docs.stripe.com/api/events/object), such as `invoice.paid`.
Store the `subscription.id` and `customer.id` event objects in your database for
verification.

For testing purposes, you can monitor events in the
[Dashboard](https://dashboard.stripe.com/events). For production, set up a
webhook endpoint and subscribe to appropriate event types. If you don’t know
your `STRIPE_WEBHOOK_SECRET` key, click the
[webhook](https://dashboard.stripe.com/webhooks) in the Dashboard to view it.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/webhook' do
 webhook_secret = '{{STRIPE_WEBHOOK_SECRET}}'
 payload = request.body.read
 if !webhook_secret.empty?
# Retrieve the event by verifying the signature using the raw body and secret if
webhook signing is configured.
 sig_header = request.env['HTTP_STRIPE_SIGNATURE']
 event = nil

 begin
 event = Stripe::Webhook.construct_event(
 payload, sig_header, webhook_secret
 )
 rescue JSON::ParserError => e
 # Invalid payload
 status 400
 return
 rescue Stripe::SignatureVerificationError => e
 # Invalid signature
 puts '⚠️ Webhook signature verification failed.'
 status 400
 return
 end
 else
 data = JSON.parse(payload, symbolize_names: true)
 event = Stripe::Event.construct_from(data)
 end
 # Get the type of webhook event sent
 event_type = event['type']
 data = event['data']
 data_object = data['object']

 case event_type
 when 'checkout.session.completed'
 # Payment is successful and the subscription is created.
# You should provision the subscription and save the customer ID to your
database.
 when 'invoice.paid'
 # Continue to provision the subscription as payments continue to be made.
# Store the status in your database and check when a user accesses your service.
 # This approach helps you avoid hitting rate limits.
 when 'invoice.payment_failed'
 # The payment failed or the customer does not have a valid payment method.
# The subscription becomes past_due. Notify your customer and send them to the
 # customer portal to update their payment information.
 else
 puts "Unhandled event type: \#{event.type}"
 end

 status 200
end
```

The minimum event types to monitor:

Event nameDescription`checkout.session.completed`Sent when a customer
successfully completes the Checkout Session, informing you of a new
purchase.`invoice.paid`Sent each billing interval when a payment
succeeds.`invoice.payment_failed`Sent each billing interval if there is an issue
with your customer’s payment method.
For even more events to monitor, see [Subscription
webhooks](https://docs.stripe.com/billing/subscriptions/webhooks).

[Configure the customer
portalDashboard](https://docs.stripe.com/billing/subscriptions/build-subscriptions#configure-portal)
The [customer portal](https://docs.stripe.com/customer-management) lets your
customers directly manage their existing subscriptions and invoices.

Use [the Dashboard](https://dashboard.stripe.com/test/settings/billing/portal)
to configure the portal. At a minimum, make sure to configure it so that
customers can update their payment methods. See [Integrating the customer
portal](https://docs.stripe.com/customer-management) for information about other
settings you can configure.

[Create a portal
SessionServer](https://docs.stripe.com/billing/subscriptions/build-subscriptions#create-portal-session)
Define an endpoint that [creates the customer portal
session](https://docs.stripe.com/api/customer_portal/sessions/create) for your
frontend to call. Here `CUSTOMER_ID` refers to the customer ID created by a
Checkout Session that you saved while processing the
`checkout.session.completed` webhook. You can also set a default redirect link
for the portal in the Dashboard.

Pass an optional `return_url` value for the page on your site to redirect your
customer to after they finish managing their subscription:

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# This is the URL that users are redirected to after they're done
# managing their billing.
return_url = '{{DOMAIN_URL}}'
customer_id = '{{CUSTOMER_ID}}'

session = Stripe::BillingPortal::Session.create({
 customer: customer_id,
 return_url: return_url,
})

# Redirect to the URL for the session
# redirect session.url, 303
```

[Send customers to the customer
portalClient](https://docs.stripe.com/billing/subscriptions/build-subscriptions#send-to-portal)
On your frontend, add a button to the page at the `success_url` that provides a
link to the customer portal:

```
<html>
 <head>
 <title>Manage Billing</title>
 </head>
 <body>
 <form action="/customer-portal" method="POST">
 <!-- Note: If using PHP set the action to /customer-portal.php -->
 <button type="submit">Manage Billing</button>
 </form>
 </body>
</html>
```

After exiting the customer portal, the Customer returns to your website at the
`return_url`. Continue to [monitor
events](https://docs.stripe.com/billing/subscriptions/webhooks) to track the
state of the Customer’s subscription.

If you configure the customer portal to allow actions such as canceling a
subscription, see [Integrating the customer
portal](https://docs.stripe.com/customer-management/integrate-customer-portal#webhooks)
for additional events to monitor.

[Test your
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions#test)
### Test payment methods

Use the following table to test different payment methods and scenarios.

Payment methodScenarioHow to testBECS Direct DebitYour customer successfully
pays with BECS Direct Debit.Fill out the form using the account number
`900123456` and BSB `000-000`. The confirmed PaymentIntent initially transitions
to `processing`, then transitions to the `succeeded` status three minutes
later.BECS Direct DebitYour customer’s payment fails with an `account_closed`
error code.Fill out the form using the account number `111111113` and BSB
`000-000`.Credit cardThe card payment succeeds and does not require
authentication.Fill out the credit card form using the credit card number `4242
4242 4242 4242` with any expiration, CVC, and postal code.Credit cardThe card
payment requires
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number `4000 0025 0000 3155` with
any expiration, CVC, and postal code.Credit cardThe card is declined with a
decline code like `insufficient_funds`.Fill out the credit card form using the
credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal
code.SEPA Direct DebitYour customer successfully pays with SEPA Direct
Debit.Fill out the form using the account number `AT321904300235473204`. The
confirmed PaymentIntent initially transitions to processing, then transitions to
the succeeded status three minutes later.SEPA Direct DebitYour customer’s
payment intent status transition from `processing` to
`requires_payment_method`.Fill out the form using the account number
`AT861904300235473202`.
### Monitoring events

Set up webhooks to listen to subscription change events, such as upgrades and
cancellations. Learn more about [subscription
webhooks](https://docs.stripe.com/billing/subscriptions/webhooks). You can view
events in the [Dashboard](https://dashboard.stripe.com/test/events) or with the
[Stripe CLI](https://docs.stripe.com/webhooks#test-webhook).

For more details about [testing your Billing
integration](https://docs.stripe.com/billing/testing), read the guide.

## See also

- [Offer customers a free trial
period](https://docs.stripe.com/billing/subscriptions/trials)
- [Apply
discounts](https://docs.stripe.com/billing/subscriptions/coupons#using-coupons-in-checkout)
- [Manage prorations](https://docs.stripe.com/billing/subscriptions/prorations)
- [Integrate entitlements to manage access to your product’s
features](https://docs.stripe.com/billing/entitlements)

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [from GitHub](https://github.com/stripe-samples/checkout-single-subscription)
- [Billing integration quickstart](https://docs.stripe.com/billing/quickstart)
- [demo](https://checkout.stripe.dev/)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [customer portal](https://docs.stripe.com/customer-management)
- [manually in the Dashboard](https://docs.stripe.com/no-code/subscriptions)
- [Payment Links](https://docs.stripe.com/payment-links)
- [designing an
integration](https://docs.stripe.com/billing/subscriptions/designing-integration)
- [Display taxes](https://docs.stripe.com/payments/checkout/taxes)
- [Apply
discounts](https://docs.stripe.com/billing/subscriptions/coupons#using-coupons-in-checkout)
- [Offer customers a free trial
period](https://docs.stripe.com/billing/subscriptions/trials)
- [Add more payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Integrate the hosted invoice
page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Use Checkout in setup mode](https://docs.stripe.com/payments/save-and-reuse)
- [Set up metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [pricing
tiers](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
- [Manage prorations](https://docs.stripe.com/billing/subscriptions/prorations)
- [Allow customers to subscribe to multiple
products](https://docs.stripe.com/billing/subscriptions/multiple-products)
- [Integrate entitlements to manage access to your product’s
features](https://docs.stripe.com/billing/entitlements)
- [webhook](https://docs.stripe.com/webhooks#test-webhook)
- [https://brew.sh/](https://brew.sh/)
- [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [products](https://docs.stripe.com/api/products)
- [prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
- [test mode to live mode](https://docs.stripe.com/keys#test-live-modes)
- [upsell](https://docs.stripe.com/payments/checkout/upsells)
- [Billing examples](https://docs.stripe.com/products-prices/pricing-models)
- [View full
sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/client/index.html)
- [creates the session](https://docs.stripe.com/api/checkout/sessions/create)
- [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [step
2](https://docs.stripe.com/billing/subscriptions/build-subscriptions#create-pricing-model)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[lookup_keys](https://docs.stripe.com/products-prices/manage-prices#lookup-keys)
- [sample
application](https://github.com/stripe-samples/subscription-use-cases/tree/main/fixed-price-subscriptions)
- [View full
sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/server/ruby/server.rb)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}](https://example.com/success.html?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/canceled.html](https://example.com/canceled.html)
- [Customize your success
page](https://docs.stripe.com/payments/checkout/custom-success-page)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [several payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
- [webhooks](https://docs.stripe.com/webhooks)
- [provision the
subscription](https://docs.stripe.com/billing/subscriptions/overview#provisioning)
- [event object](https://docs.stripe.com/api/events/object)
- [Dashboard](https://dashboard.stripe.com/events)
- [webhook](https://dashboard.stripe.com/webhooks)
- [Subscription
webhooks](https://docs.stripe.com/billing/subscriptions/webhooks)
- [the Dashboard](https://dashboard.stripe.com/test/settings/billing/portal)
- [creates the customer portal
session](https://docs.stripe.com/api/customer_portal/sessions/create)
- [View full
sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/client/success.html)
- [Integrating the customer
portal](https://docs.stripe.com/customer-management/integrate-customer-portal#webhooks)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Dashboard](https://dashboard.stripe.com/test/events)
- [testing your Billing integration](https://docs.stripe.com/billing/testing)