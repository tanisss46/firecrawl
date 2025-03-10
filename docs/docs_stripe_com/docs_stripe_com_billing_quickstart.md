steps, such as adding pricing data, the builder updates the sample code.

Download and customize the sample app locally to test your integration.

Download full appDon't code? Use Stripe’s [no-code
options](https://docs.stripe.com/no-code) or get help from [our
partners](https://stripe.partners/).1 Set up products, pricing, and payment
methods
### Add your products and prices

Create new [Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) that you can use in this sample.

#### Note

Sign in to your Stripe account to interact directly with your test mode data.

Client
### Add features to your product

Create features, such as an annual birthday gift, and associate them with your
subscription to [entitle](https://docs.stripe.com/billing/entitlements) new
subscribers to them. Listen to the [active entitlements summary
events](https://docs.stripe.com/billing/entitlements#webhooks) for your [event
destination](https://docs.stripe.com/event-destinations), and use the [list
active entitlements
API](https://docs.stripe.com/api/entitlements/active-entitlement/list) for a
given customer to fulfill your customer’s entitlements.

#### Note

Create or select a product before adding a feature.Client
### Enable payment methods

Use your [Dashboard](https://dashboard.stripe.com/settings/payment_methods) to
enable [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support)
that you want to accept in addition to cards. Checkout dynamically displays your
enabled payment methods in order of relevance, based on the customer’s location
and other characteristics.

2 Build your subscription page
### Add a pricing preview page

Add a page to your site that displays your product and allows your customers to
subscribe to it. Clicking **Checkout**, redirects them to a Stripe-hosted
[Checkout](https://docs.stripe.com/payments/checkout) page, which finalizes the
order and prevents further modification.

Consider embedding a [pricing
table](https://docs.stripe.com/payments/checkout/pricing-table) to dynamically
display your pricing information through the Dashboard. Clicking a pricing
option redirects your customer to the checkout page.

Client
### Add a checkout button

The button on your order preview page redirects your customer to the
Stripe-hosted Checkout page and uses your product’s `lookup_key` to retrieve the
`price_id` from the server.

Client
### Add a success page

Create a success page to display order confirmation messaging or order details
to your customer. Associate this page with the Checkout Session `success_url`,
which Stripe redirects to after the customer successfully completes the
checkout.

Client
### Add a customer portal button

Add a button to redirect to the customer portal to allow customers to manage
their subscription. Clicking this button redirects your customer to the
Stripe-hosted customer portal page.

Client
### Add a cancel page

Add a page to associate with the Checkout Session `cancel_url`, which Stripe
redirects to when the customer clicks the back button in Checkout.

Client3Call the Stripe API
### Install the Stripe Ruby library

Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a Checkout Session

The [Checkout Session](https://docs.stripe.com/api/checkout/sessions) controls
what your customer sees in the Stripe-hosted payment page such as line items,
the order amount and currency, and acceptable payment methods.

Server
### Get the price from lookup key

Pass the lookup key you defined for your product in the
[Price](https://docs.stripe.com/api/prices/list) endpoint to apply its price to
the order.

Server
### Define the line items

Always keep sensitive information about your product inventory, such as price
and availability, on your server to prevent customer manipulation from the
client. Pass in the predefined price ID retrieved above.

Server
### Set the mode

Set the mode to `subscription`. Checkout also supports
[payment](https://docs.stripe.com/checkout/quickstart) and
[setup](https://docs.stripe.com/payments/save-and-reuse) modes for non-recurring
payments.

Server
### Supply success and cancel URLs

Specify publicly accessible URLs that Stripe can redirect customers after
success or cancellation. You can provide the same URL for both properties. Add
the `session_id` query parameter at the end of your URL so you can retrieve the
customer later and so Stripe can generate the customer’s hosted Dashboard.

Server
### Redirect from Checkout

After creating the session, redirect your customer to the URL returned in the
response (either the success or cancel URL).

Server
### Create a customer portal session

Initiate a secure, Stripe-hosted [customer portal
session](https://docs.stripe.com/api/customer_portal/sessions/create) that lets
your customers manage their subscriptions and billing details.

Server
### Redirect to customer portal

After creating the portal session, redirect your customer to the URL returned in
the response.

Server
### Fulfill the subscription

Create a `/webhook` endpoint and obtain your webhook secret key in the
[Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench to listen for
events related to subscription activity. After a successful payment and redirect
to the success page, verify that the subscription status is `active` and grant
your customer access to the products and features they subscribed to.

Server4 Test your page
### Run the server

Start your server and navigate to
[http://localhost:4242/](http://localhost:4242/)

`ruby server.rb`Server
### Try it out

Click the checkout button. In the Stripe Checkout page, use any of these test
cards to simulate a payment.

Payment succeeds4242 4242 4242 4242Payment requires authentication4000 0025 0000
3155Payment is declined4000 0000 0000 9995Client
## Add customization features

If you successfully subscribed to your product in your test, you have a working,
basic subscriptions checkout integration. Use the toggles below to see how to
customize this sample with additional features.

### Add trials

Attach a trial period to a Checkout session.

### Set billing cycle date

Specify a billing cycle anchor when creating a Checkout session.

### Automate tax collection

Calculate and collect the right amount of tax on your Stripe transactions. Learn
more about [Stripe Tax](https://docs.stripe.com/tax) and [how to add it to
Checkout](https://docs.stripe.com/tax/checkout). [Activate Stripe
Tax](https://dashboard.stripe.com/settings/tax/activate) in the Dashboard before
integrating.

## Next steps

#### [Update subscription prices](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)

Update subscriptions to handle customers upgrading or downgrading their
subscription plan.

#### [Apply prorations](https://docs.stripe.com/billing/subscriptions/prorations)

Learn how to adjust a customer’s invoice to accurately reflect mid-cycle pricing
changes.

#### [Offer upsells](https://docs.stripe.com/payments/checkout/upsells)

Incentivize customers with discounts for committing to longer billing intervals.

#### [More features](https://docs.stripe.com/billing/subscriptions/features)

Review the features to further customize your integration to offer discounts,
pause payment collection, and more.

Was this page
helpful?checkout.htmlsuccess.htmlcancel.htmlclient.jsserver.rbDownload
```
<!DOCTYPE html><html> <head> <title>Subscribe to a cool new product</title>
<link rel="stylesheet" href="style.css"> <script
src="https://js.stripe.com/v3/"></script> </head> <body> <section> <div
class="product"> <svg xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink" width="14px" height="16px" viewBox="0
0 14 16" version="1.1"> <defs/> <g id="Flow" stroke="none" stroke-width="1"
fill="none" fill-rule="evenodd"> <g id="0-Default"
transform="translate(-121.000000, -40.000000)" fill="#E184DF"> <path d="M127,50
L126,50 C123.238576,50 121,47.7614237 121,45 C121,42.2385763 123.238576,40
126,40 L135,40 L135,56 L133,56 L133,42 L129,42 L129,56 L127,56 L127,50 Z M127,48
L127,42 L126,42 C124.343146,42 123,43.3431458 123,45 C123,46.6568542
124.343146,48 126,48 L127,48 Z" id="Pilcrow"/> </g> </g> </svg> <div
class="description"> <h3>Starter plan</h3> <h5>$20.00 / month</h5> </div> </div>
<form action="/create-checkout-session" method="POST"> <!-- Add a hidden field
with the lookup_key of your Price --> <input type="hidden" name="lookup_key"
value="{{PRICE_LOOKUP_KEY}}" /> <button id="checkout-and-portal-button"
type="submit">Checkout</button> </form> </section> </body></html>
```

## Links

- [text version of this
guide](https://docs.stripe.com/billing/subscriptions/build-subscription)
- [View the text-based
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Stripe Billing](https://docs.stripe.com/billing)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [entitle](https://docs.stripe.com/billing/entitlements)
- [active entitlements summary
events](https://docs.stripe.com/billing/entitlements#webhooks)
- [event destination](https://docs.stripe.com/event-destinations)
- [list active entitlements
API](https://docs.stripe.com/api/entitlements/active-entitlement/list)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [Price](https://docs.stripe.com/api/prices/list)
- [payment](https://docs.stripe.com/checkout/quickstart)
- [setup](https://docs.stripe.com/payments/save-and-reuse)
- [customer portal
session](https://docs.stripe.com/api/customer_portal/sessions/create)
- [Webhooks](https://dashboard.stripe.com/webhooks)
- [http://localhost:4242/](http://localhost:4242/)
- [Stripe Tax](https://docs.stripe.com/tax)
- [how to add it to Checkout](https://docs.stripe.com/tax/checkout)
- [Activate Stripe Tax](https://dashboard.stripe.com/settings/tax/activate)
- [Update subscription
prices](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)
- [Apply prorations](https://docs.stripe.com/billing/subscriptions/prorations)
- [Offer upsells](https://docs.stripe.com/payments/checkout/upsells)
- [More features](https://docs.stripe.com/billing/subscriptions/features)