Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a Checkout Session

Add an endpoint on your server that creates a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions). A Checkout Session
controls what your customer sees on the payment page such as line items, the
order amount and currency, and acceptable payment methods. We enable cards and
other common payment methods for you by default, and you can enable or disable
payment methods directly in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods).

Server
### Define a product to sell

Always keep sensitive information about your product inventory, such as price
and availability, on your server to prevent customer manipulation from the
client. Define product information when you create the Checkout Session using
[predefined price
IDs](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted#create-product-prices-upfront)
or on the fly with
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data).

Server
### Choose a mode

To handle different transaction types, adjust the `mode` parameter. For one-time
payments, use `payment`. To initiate recurring payments with
[subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions?platform=web&ui=stripe-hosted),
switch the `mode` to `subscription`. And for [setting up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=stripe-hosted),
set the `mode` to `setup`.

Server
### Supply success and cancel URLs

Specify URLs for success and cancel pages—make sure they’re publicly accessible
so Stripe can redirect customers to them. You can also handle both the success
and canceled states with the same URL.

Server
### Redirect to Checkout

After creating the session, redirect your customer to the URL for the Checkout
page returned in the response.

Server2 Build your checkout
### Add a success page

Create a success page for the URL you provided as the Checkout Session
`success_url` to display order confirmation messaging or order details to your
customer. Stripe redirects to this page after the customer successfully
completes the checkout.

Client
### Add a canceled page

Add another page for `cancel_url`. Stripe redirects to this page when the
customer clicks the back button in Checkout.

Client
### Add an order preview page

Finally, add a page to show a preview of the customer’s order. Allow them to
review or modify their order—as soon as they’re sent to the Checkout page, the
order is final and they can’t modify it without creating a new Checkout Session.

Client
### Add a checkout button

Add a button to your order preview page. When your customer clicks this button,
they’re redirected to the Stripe-hosted payment page.

Client3 Test your page
### Run the application

Start your server and navigate to
[http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

`ruby server.rb`Client
### Try it out

Click the checkout button to be redirected to the Stripe Checkout page. Use any
of these test cards to simulate a payment.

Payment succeeds4242 4242 4242 4242Payment requires authentication4000 0025 0000
3155Payment is declined4000 0000 0000 9995
## Congratulations!

You have a basic Checkout integration working. Now learn how to customize the
appearance of your checkout page and automate tax collection.

### Customize the checkout page

Customize the appearance of the hosted Checkout page by:

- Adding your logo and color theme in your [branding
settings](https://dashboard.stripe.com/settings/branding).
- Using the [Checkout Sessions
API](https://docs.stripe.com/api/checkout/sessions/create) to activate
additional features, like collecting addresses or prefilling customer data.

### Automate tax collection

Calculate and collect the right amount of tax on your Stripe transactions. Learn
more about [Stripe Tax](https://docs.stripe.com/tax) and how to [add it to
Checkout](https://docs.stripe.com/tax/checkout).

## Next steps

#### [Fulfill orders](https://docs.stripe.com/checkout/fulfillment)

Set up an event destination to fulfill orders after a payment succeeds and to
handle other critical events.

#### [Receive payouts](https://docs.stripe.com/payouts)

Learn how to move funds out of your Stripe account into your bank account.

#### [Refund and cancel payments](https://docs.stripe.com/refunds)

Handle requests for refunds by using the Stripe API or Dashboard.

#### [Customer management](https://docs.stripe.com/customer-management)

Let your customers self-manage their payment details, invoices, and
subscriptions.

#### [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)

Automatically present prices in your customer’s local currency.

Preview
### Stubborn Attachments

##### $20.00

Checkoutserver.rbcheckout.htmlsuccess.htmlcancel.htmlDownload
```
require 'stripe'require 'sinatra'
# This test secret API key is a placeholder. Don't include personal details in requests with this key.# To see your test secret API key embedded in code samples, sign in to your Stripe account.# You can also find your test secret API key at https://dashboard.stripe.com/test/apikeys.Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
set :static, trueset :port, 4242
YOUR_DOMAIN = 'http://localhost:4242'
post '/create-checkout-session' do content_type 'application/json'
session = Stripe::Checkout::Session.create({ line_items: [{ # Provide the exact
Price ID (e.g. pr_1234) of the product you want to sell price: '{{PRICE_ID}}',
quantity: 1, }], mode: 'payment', success_url: YOUR_DOMAIN + '/success.html',
cancel_url: YOUR_DOMAIN + '/cancel.html', }) redirect session.url, 303end
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=checkout)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [predefined price
IDs](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted#create-product-prices-upfront)
-
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
-
[subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions?platform=web&ui=stripe-hosted)
- [setting up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=stripe-hosted)
- [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)
- [branding settings](https://dashboard.stripe.com/settings/branding)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions/create)
- [Stripe Tax](https://docs.stripe.com/tax)
- [add it to Checkout](https://docs.stripe.com/tax/checkout)
- [Fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Receive payouts](https://docs.stripe.com/payouts)
- [Refund and cancel payments](https://docs.stripe.com/refunds)
- [Customer management](https://docs.stripe.com/customer-management)
- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)