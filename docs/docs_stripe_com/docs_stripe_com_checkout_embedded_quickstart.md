Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a Checkout Session

Add an endpoint on your server that creates a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), setting the
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
to `embedded`.

The Checkout Session response includes a client secret, which the client uses to
mount Checkout. Return the
[client_secret](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_secret)
in your response.

Server
### Supply a return URL

To define how Stripe redirects your customer after payment, specify the URL of
the return page in the
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
parameter while creating the Checkout Session. After the payment attempt, Stripe
directs your customer to return page hosted on your website.

Include the `{CHECKOUT_SESSION_ID}` template variable in the URL. Before
redirecting your customer, Checkout replaces the variable with the Checkout
Session ID. You’re responsible for creating and hosting the return page on your
website.

Server
### Define a product to sell

Define the products you’re selling when you create the Checkout Session by using
[predefined price
IDs](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form#create-product-prices-upfront).

Always keep sensitive information about your product inventory, such as price
and availability, on your server to prevent customer manipulation from the
client.

Server
### Choose the mode

To handle different transaction types, adjust the `mode` parameter. For one-time
payments, use `payment`. To initiate recurring payments with
[subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions?platform=web&ui=embedded-form),
switch the `mode` to `subscription`. And for [setting up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=embedded-form),
set the `mode` to `setup`.

Server2Mount Checkout
### Load Stripe.js

Use [Stripe.js](https://docs.stripe.com/js) to remain [PCI
compliant](https://docs.stripe.com/security/guide#validating-pci-compliance) by
ensuring that payment details are sent directly to Stripe without hitting your
server. Always load Stripe.js from *js.stripe.com* to remain compliant. Don’t
include the script in a bundle or host it yourself.

Client
### Define the payment form

To securely collect the customer’s information, create an empty placeholder
`div`. Stripe inserts an iframe into the `div`.

Client
### Initialize Stripe.js

Initialize Stripe.js with your [publishable API
key](https://docs.stripe.com/keys#obtain-api-keys).

Client
### Fetch a Checkout Session client secret

Create an asynchronous `fetchClientSecret` function that makes a request to your
server to [create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create) and retrieve the
client secret.

Client
### Initialize Checkout

Initialize Checkout with your `fetchClientSecret` function and mount it to the
placeholder `<div>` in your payment form. Checkout is rendered in an iframe that
securely sends payment information to Stripe over an HTTPS connection.

Avoid placing Checkout within another iframe because some payment methods
require redirecting to another page for payment confirmation.

Client3Show a return page
### Create an endpoint to retrieve a Checkout Session

Add an endpoint to retrieve a Checkout Session status.

Server
### Add a return page

To display order information to your customer, create a return page for the URL
you provided as the Checkout Session `return_url`. Stripe redirects to this page
after the customer completes the checkout.

Client
### Retrieve a Checkout session

As soon as your return page loads, immediately make a request to the endpoint on
your server. Use the Checkout Session ID in the URL to retrieve the status of
the Checkout Session.

Client
### Handle session

Handle the result of the session by using its status:

- `complete`: The payment succeeded. Use the information from the Checkout
Session to render a success page.
- `open`: The payment failed or was canceled. Remount Checkout so that your
customer can try again.
Client4Test your page
### Run the application

Start your server and navigate to
[http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

`ruby server.rb`Client
### Try it out

Click the pay button to complete the payment, which redirects you to the
specified return page.

If you see the return page, and the payment in the list of [successful
payments](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful)
in the Dashboard, your integration is successfully working. Use any of the
following test cards to simulate a payment:

Payment succeeds4242 4242 4242 4242Payment requires authentication4000 0025 0000
3155Payment is declined4000 0000 0000 9995
## Congratulations!

You have a basic Checkout integration working. Now learn how to customize the
appearance of your checkout page and automate tax collection.

### Customize the checkout page

[Customize](https://docs.stripe.com/payments/checkout/customization) the
appearance of the embedded form by:

- Adding your color theme and font in your [branding
settings](https://dashboard.stripe.com/settings/branding/checkout).
- Using the [Checkout Sessions
API](https://docs.stripe.com/api/checkout/sessions/create)to activate additional
features, like collecting addresses and prefilling customer data.

### Automate tax collection

Calculate and collect the right amount of tax on your Stripe transactions. Learn
more about [Stripe Tax](https://docs.stripe.com/tax) and [how to add it to
Checkout](https://docs.stripe.com/tax/checkout).

## Next steps

#### [Fulfill orders](https://docs.stripe.com/checkout/fulfillment)

Set up a webhook to fulfill orders after a payment succeeds. Webhooks are the
most reliable way to handle business-critical events.

#### [Receive payouts](https://docs.stripe.com/payouts)

Learn how to move funds out of your Stripe account into your bank account.

#### [Refund and cancel payments](https://docs.stripe.com/refunds)

Handle requests for refunds by using the Stripe API or Dashboard.

#### [Customer management](https://docs.stripe.com/customer-management)

Let your customers self-manage their payment details, invoices, and
subscriptions

Was this page
helpful?Previewserver.rbcheckout.htmlcheckout.jsreturn.htmlreturn.jsDownload
```
require 'stripe'require 'sinatra'
# This test secret API key is a placeholder. Don't include personal details in requests with this key.# To see your test secret API key embedded in code samples, sign in to your Stripe account.# You can also find your test secret API key at https://dashboard.stripe.com/test/apikeys.Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
set :static, trueset :port, 4242
YOUR_DOMAIN = 'http://localhost:4242'
post '/create-checkout-session' do content_type 'application/json'
session = Stripe::Checkout::Session.create({ ui_mode: 'embedded', line_items: [{
# Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
price: '{{PRICE_ID}}', quantity: 1, }], mode: 'payment', return_url: YOUR_DOMAIN
+ '/return.html?session_id={CHECKOUT_SESSION_ID}', })
 {clientSecret: session.client_secret}.to_jsonend
get '/session-status' do session =
Stripe::Checkout::Session.retrieve(params[:session_id])
{status: session.status, customer_email:
session.customer_details.email}.to_jsonend
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-checkout)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
-
[client_secret](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_secret)
-
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
- [predefined price
IDs](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form#create-product-prices-upfront)
-
[subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions?platform=web&ui=embedded-form)
- [setting up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=embedded-form)
- [Stripe.js](https://docs.stripe.com/js)
- [PCI
compliant](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [publishable API key](https://docs.stripe.com/keys#obtain-api-keys)
- [create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create)
- [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)
- [successful
payments](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful)
- [Customize](https://docs.stripe.com/payments/checkout/customization)
- [branding settings](https://dashboard.stripe.com/settings/branding/checkout)
- [Stripe Tax](https://docs.stripe.com/tax)
- [how to add it to Checkout](https://docs.stripe.com/tax/checkout)
- [Fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Receive payouts](https://docs.stripe.com/payouts)
- [Refund and cancel payments](https://docs.stripe.com/refunds)
- [Customer management](https://docs.stripe.com/customer-management)