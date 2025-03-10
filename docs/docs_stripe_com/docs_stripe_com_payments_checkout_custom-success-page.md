# Customize redirect behavior

## Display a confirmation page with your customer's order information.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
If you have a Checkout integration that uses a Stripe-hosted page, Stripe
redirects your customer to a success page that you create and host on your site.
You can use the details from a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) to display an order
confirmation page for your customer (for example, their name or payment amount)
after the payment.

## Redirect customers to a success page

To use the details from a Checkout Session:

- Modify the
[success_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-success_url)
to pass the Checkout Session ID to the client side.
- Look up the Checkout Session using the ID on your success page.
- Use the Checkout Session to customize what’s displayed on your success page.

## Modify the success URL Server-side

Add the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` when you
create the Checkout Session. Note that this is a literal string and must be
added exactly as you see it here. Do not substitute it with a Checkout Session
ID—this happens automatically after your customer pays and is redirected to the
success page.

```
session = Stripe::Checkout::Session.create(
 success_url: "http://yoursite.com/order/success",
success_url:
"http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID}",
 # other options...,
)
```

## Create the success page Server-side

Look up the Checkout Session using the ID and create a success page to display
the order information. This example prints out the customer’s name:

```
# This example sets up an endpoint using the Sinatra framework.
# Watch this video to get started: https://youtu.be/8aA9Enb8NVc.

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

require 'sinatra'

get '/order/success' do
 session = Stripe::Checkout::Session.retrieve(params[:session_id])
 customer = Stripe::Customer.retrieve(session.customer)

 "<html><body><h1>Thanks for your order, #{customer.name}!</h1></body></html>"
end
```

## Test the integration

To confirm that your redirect is working as expected:

- Click the checkout button.
- Fill in the customer name and other payment details.
- Click **Pay**.

If it works, you’re redirected to the success page with your custom message. For
example, if you used the message in the code samples, the success page displays
this message: **Thanks for your order, Jenny Rosen!**

## Links

- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[success_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-success_url)
- [http://yoursite.com/order/success](http://yoursite.com/order/success)
-
[http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID}](http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID})
- [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)