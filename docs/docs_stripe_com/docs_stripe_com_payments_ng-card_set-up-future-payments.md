# Set up future payments with Naira cardPrivate preview

## Learn how to save Naira card to charge customers later.

Stripe-hosted pageDirect API
Save Naira card payment details using
[Checkout](https://docs.stripe.com/payments/checkout), our fully hosted checkout
page.

Learn how to [set up a subscription with Naira
card](https://docs.stripe.com/billing/subscriptions/ng-card) to create recurring
payments after saving a payment method in Checkout.

[Set up
StripeServer-side](https://docs.stripe.com/payments/ng-card/set-up-future-payments#web-set-up-stripe)
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

[Getting permission to save a payment
methodServer-side](https://docs.stripe.com/payments/ng-card/set-up-future-payments#web-permissions)
You need the customer’s permission to save their payment method for future use.
Creating an agreement (sometimes called a mandate) up front allows you to save
the customer’s payment details and charge them when they’re not actively using
your website or app.

Add terms to your website or app that state how you plan to save the customer’s
payment method details, and let them opt in. If you plan to charge the customer
when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of
payments on their behalf for specified transactions
- The anticipated frequency (one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy, if you’re setting up the payment method for a
subscription service

Make sure that you keep a record of the customer’s written agreement to these
terms.

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/ng-card/set-up-future-payments#web-create-customer)
To save a Naira card payment method for future payments, attach it to a
[Customer](https://docs.stripe.com/api/customers).

Create a [Customer object](https://docs.stripe.com/api/customers) when the
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
SessionServer-side](https://docs.stripe.com/payments/ng-card/set-up-future-payments#web-create-checkout-session)
The customer must authorize the use of the local merchant of record service
provider for future payments.

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
After creating the Checkout Session, redirect the customer to the [Checkout
session
URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
that the response returns.

```
Stripe::Checkout::Session.create({
 mode: 'setup',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'ng_card'],
 customer: customer.id,
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

[Test your
integration](https://docs.stripe.com/payments/ng-card/set-up-future-payments#web-test-integration)
Select Naira card as the payment method, then click **Continue to Naira card**.
Test the setup by authenticating the SetupIntent on the redirect page. If the
SetupIntent transitions from `requires_action` to `succeeded`, the setup is
correct.

## Links

- [Checkout](https://docs.stripe.com/payments/checkout)
- [set up a subscription with Naira
card](https://docs.stripe.com/billing/subscriptions/ng-card)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [Checkout session
URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)