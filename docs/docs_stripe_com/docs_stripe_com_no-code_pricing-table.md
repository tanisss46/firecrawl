# Embeddable pricing table for subscriptions

## Display a subscription pricing table on your website and take customers directly to Stripe Checkout.

You can use the Stripe Dashboard to create a table that displays different
subscription pricing levels to your customers. You don’t need to write any
custom code to create or embed a pricing table. This guide describes how to:

- Use the Stripe Dashboard to configure the UI component
- the generated code from the Dashboard
- Embed the code on your website to show your customers pricing information and
take them to a checkout page

## Overview

![The pricing table is an embedded UI that displays pricing information and
takes customers to
checkout.](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png)

Embed a pricing table on your website to display pricing details and convert
customers to checkout.

A pricing table is an embeddable UI that:

- Displays [pricing
information](https://docs.stripe.com/products-prices/pricing-models) and takes
customers to a prebuilt checkout flow. The checkout flow uses [Stripe
Checkout](https://docs.stripe.com/payments/checkout) to complete the purchase.
- Supports common subscription business models like
[flat-rate](https://docs.stripe.com/products-prices/pricing-models#flat-rate),
[per-seat](https://docs.stripe.com/products-prices/pricing-models#per-seat),
[tiered
pricing](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing),
and free trials.
- Lets you configure, customize, and update product and pricing information
directly in the Dashboard, without needing to write any code.
- Embeds into your website with a `<script>` tag and web component. Stripe
automatically generates the tag. You copy and paste it into your website’s code.

The diagram below summarizes how the customer goes from viewing a pricing table
to completing checkout.

Customer

Your application

Stripe Checkout

Views pricing table

Clicks on “subscribe” button

Completes purchase

Returns to your website

checkout.session.completedPricing table[Create pricing
table](https://docs.stripe.com/payments/checkout/pricing-table#Create)- In the
Dashboard, go to **More** > **Product catalog** > [pricing
tables](https://dashboard.stripe.com/pricing-tables).
- Click **+Create pricing table**.
- Add products relevant to your customers (up to four per pricing interval).
Optionally, include a free trial.
- Adjust the look and feel in **Display settings**. Highlight a specific product
and customize the language, colors, font, and button design, then click
**Continue**.
- Configure **Payment settings** to select the customer information to collect,
options to present to the customer, and whether to display a confirmation page
or redirect customers back to your site after a successful purchase.
#### Confirm maximum quantity

If you have tiered pricing that supports quantities greater than the default
maximum of 99, check the **Let customers adjust quantity** property and increase
the **Max** value accordingly. Tiered pricing options for quantities above the
maximum don’t appear in the selector.
- Configure the [customer
portal](https://docs.stripe.com/no-code/customer-portal) by clicking
**Continue**.
- Click ** code** to copy the generated code and embed it into your website.

![Customizing a pricing
table](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-1.45ac9351d8f043a0a63554b89b2cedfc.png)

Customize your pricing table

![Configure payment
settings](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-2.07d5287026b797b9aa1905c6ad99958d.png)

Configure payment settings

[Embed pricing
table](https://docs.stripe.com/payments/checkout/pricing-table#embed)
After creating a pricing table, Stripe automatically returns an embed code
composed of a `<script>` tag and a `<stripe-pricing-table>` web component. Click
the ** code** button to copy the code and paste it into your website.

![Pricing table detail
page](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-detail-page.dee9a93d69e802759dabd0e4ce62f1bd.png)

 the pricing table’s code and embed it on your website.

If you’re using HTML, paste the embed code into the HTML. If you’re using React,
include the `script` tag in your `index.html` page to mount the
`<stripe-pricing-table>` component.

#### Caution

The pricing table uses your account’s [publishable API
key](https://docs.stripe.com/keys). If you revoke the API key, you need to
update the embed code with your new publishable API key.

```
<body>
 <h1>We offer plans that help any business!</h1>
 <!-- Paste your embed code script here. -->
 <script
 async
 src="https://js.stripe.com/v3/pricing-table.js">
 </script>
 <stripe-pricing-table
 pricing-table-id='{{PRICING_TABLE_ID}}'
 publishable-key="pk_test_TYooMQauvdEDq54NiTphI7jx"
 >
 </stripe-pricing-table>
</body>
```

[Track
subscriptions](https://docs.stripe.com/payments/checkout/pricing-table#track-subscriptions)
When a customer purchases a subscription, you’ll see it on the [subscriptions
page](https://dashboard.stripe.com/subscriptions) in the Dashboard.

### Handle fulfillment with the Stripe API

The pricing table component uses Stripe Checkout to render a prebuilt, hosted
payment page. When a payment is completed using Checkout, Stripe sends the
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event. Register an [event
destination](https://docs.stripe.com/event-destinations) to receive the event at
your endpoint to process fulfillment and reconciliation. See the [Checkout
fulfillment guide](https://docs.stripe.com/checkout/fulfillment) for more
details.

The `<stripe-pricing-table>` web component supports setting the
`client-reference-id` property. When the property is set, the pricing table
passes it to the Checkout Session’s
[client_reference_id](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_reference_id)
attribute to help you reconcile the Checkout Session with your internal system.
This can be an authenticated user ID or a similar string. `client-reference-id`
can be composed of alphanumeric characters, dashes, or underscores, and be any
value up to 200 characters. Invalid values are silently dropped and your pricing
table will continue to work as expected.

#### Caution

Since the pricing table is embedded on your website and is accessible to anyone,
check that `client-reference-id` does not include sensitive information or
secrets, such as passwords or API keys.

```
<body>
 <h1>We offer plans that help any business!</h1>
 <!-- Paste your embed code script here. -->
 <script
 async
 src="https://js.stripe.com/v3/pricing-table.js">
 </script>
 <stripe-pricing-table
 pricing-table-id='{{PRICING_TABLE_ID}}'
 publishable-key="pk_test_TYooMQauvdEDq54NiTphI7jx"
 client-reference-id="{{CLIENT_REFERENCE_ID}}"
 >
 </stripe-pricing-table>
</body>
```

[OptionalAdd product marketing
features](https://docs.stripe.com/payments/checkout/pricing-table#product-marketing-features)[OptionalAdd
a custom
call-to-action](https://docs.stripe.com/payments/checkout/pricing-table#custom-cta)[OptionalPass
the customer
email](https://docs.stripe.com/payments/checkout/pricing-table#customer-email)[OptionalPass
an existing
customer](https://docs.stripe.com/payments/checkout/pricing-table#customer-session)[OptionalCustomize
the post-purchase
experience](https://docs.stripe.com/payments/checkout/pricing-table#post-purchase-experience)[OptionalUpdate
pricing
table](https://docs.stripe.com/payments/checkout/pricing-table#update)[OptionalConfigure
free
trials](https://docs.stripe.com/payments/checkout/pricing-table#free-trials)[OptionalContent
Security
Policy](https://docs.stripe.com/payments/checkout/pricing-table#csp)[OptionalLet
customers manage their subscriptionsNo
code](https://docs.stripe.com/payments/checkout/pricing-table#customer-portal)[OptionalPresent
local
currencies](https://docs.stripe.com/payments/checkout/pricing-table#price-localization)[OptionalAdd
custom
fields](https://docs.stripe.com/payments/checkout/pricing-table#custom-fields)
## Limitations

- **Business models**—The pricing table supports common subscription business
models like flat-rate, per-seat, tiered pricing, and trials. Other [advanced
pricing
models](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models)
aren’t supported.
- **Product and price limits**—You can configure the pricing table to display a
maximum of four products, with up to three prices per product. You can only
configure three unique pricing intervals across all products.
- **Account creation**—The pricing table call-to-action takes customers directly
to checkout. It doesn’t currently support adding an intermediate step (for
example, asking the customer to create an account on your website before
checking out).
- **Rate limit**—The pricing table has a [rate
limit](https://docs.stripe.com/rate-limits) of up to 50 read operations per
second. If you have multiple pricing tables, the rate limit is shared.
- **Checkout redirect**—The pricing table can’t redirect customers to checkout
if your website provider sandboxes the embed code in an iframe without the
`allow-top-navigation` attribute enabled. Contact your website provider to
enable this setting.
- **Testing the pricing table locally**—The pricing table requires a website
domain to render. To test the pricing table locally, run a local HTTP server to
host your website’s `index.html` file over the `localhost` domain. To run a
local HTTP server, use Python’s
[SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server)
or the [http-server](https://www.npmjs.com/package/http-server) npm module.
- **Connect**—The pricing table isn’t designed to work with
[Connect](https://docs.stripe.com/connect) and doesn’t support features like a
platform collecting fees.

## Limit customers to one subscription

You can redirect customers that already have a subscription to the [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal) or your
website to manage their subscription. Learn more about [limiting customers to
one
subscription](https://docs.stripe.com/payments/checkout/limit-subscriptions).

## Links

- [pricing information](https://docs.stripe.com/products-prices/pricing-models)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [flat-rate](https://docs.stripe.com/products-prices/pricing-models#flat-rate)
- [per-seat](https://docs.stripe.com/products-prices/pricing-models#per-seat)
- [tiered
pricing](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
- [pricing tables](https://dashboard.stripe.com/pricing-tables)
- [customer portal](https://docs.stripe.com/no-code/customer-portal)
- [publishable API key](https://docs.stripe.com/keys)
-
[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)
- [subscriptions page](https://dashboard.stripe.com/subscriptions)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [event destination](https://docs.stripe.com/event-destinations)
- [Checkout fulfillment guide](https://docs.stripe.com/checkout/fulfillment)
-
[client_reference_id](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_reference_id)
- [advanced pricing
models](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models)
- [rate limit](https://docs.stripe.com/rate-limits)
-
[SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server)
- [http-server](https://www.npmjs.com/package/http-server)
- [Connect](https://docs.stripe.com/connect)
- [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
- [limiting customers to one
subscription](https://docs.stripe.com/payments/checkout/limit-subscriptions)