# Set up future payments with South Korean cards

## Learn how to save local South Korean cards to charge your customers later.

Stripe-hosted pageDirect API
Save local card payment details using
[Checkout](https://docs.stripe.com/payments/checkout), our fully hosted checkout
page.

Learn how to [set up a subscription with local South Korean
cards](https://docs.stripe.com/billing/subscriptions/kr-card) to create
recurring payments after saving a payment method in Checkout.

[Set up
StripeServer-side](https://docs.stripe.com/payments/kr-card/set-up-future-payments#web-set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Access the Stripe API from your application using our official libraries:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Getting permission to save a South Korean
cardServer-side](https://docs.stripe.com/payments/kr-card/set-up-future-payments#web-permissions)
You need permission to save your customer’s payment method for future use.
Creating an agreement (sometimes called a mandate) up front allows you to save
your customer’s payment details and charge them when they’re not actively using
your website or app.

Add terms to your website or app that state how you plan to save your customer’s
payment method details, and let them opt in. If you plan to charge your customer
when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of
payments on their behalf for specified transactions
- The anticipated frequency (one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy (if you’re setting up the payment method for a
subscription service)

Make sure that you keep a record of your customer’s written agreement to these
terms, and only submit charges in accordance with the agreed terms.

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/kr-card/set-up-future-payments#web-create-customer)
To save a South Korean card for future payments, attach it to a
[Customer](https://docs.stripe.com/api/customers).

Create a [Customer object](https://docs.stripe.com/api/customers) when your
customer creates an account with your business, and associate the ID of the
Customer object with your own internal representation of that customer.
Alternatively, you can create a new Customer before saving a payment method for
future payments.

Create a new Customer or retrieve an existing Customer to associate with this
payment. Include the following code on your server to create a new Customer:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode description="My First Test Customer (created for API docs)"
```

[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/kr-card/set-up-future-payments#web-create-checkout-session)
Add a checkout button to your website that calls a server-side endpoint to
create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions).

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

Create a Checkout Session in `setup` mode to collect the required information.
After creating the Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
that the response returns.

```
Stripe::Checkout::Session.create({
 mode: 'setup',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'kr_card'],
 customer: customer.id,
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

[Test your
integration](https://docs.stripe.com/payments/kr-card/set-up-future-payments#web-test-integration)
When testing your Checkout integration, select **Local card** and click Pay. You
will be redirected to a Stripe-hosted page where you can choose to authorize or
fail the payment. See more details
[here](https://docs.stripe.com/testing#redirects) for how to test redirect based
payment methods.

## Links

- [Checkout](https://docs.stripe.com/payments/checkout)
- [set up a subscription with local South Korean
cards](https://docs.stripe.com/billing/subscriptions/kr-card)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [here](https://docs.stripe.com/testing#redirects)