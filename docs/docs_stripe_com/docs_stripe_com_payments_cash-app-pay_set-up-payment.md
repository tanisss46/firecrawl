# Set up future Cash App Pay payments

## Learn how to save Cash App Pay details and charge your customers later.

WebMobileStripe-hosted pageDirect API
This guide covers how to save a Cash App Pay payment details using
[Checkout](https://docs.stripe.com/payments/checkout), our fully hosted checkout
page.

To create recurring payments after saving a payment method in Checkout, see [Set
up a subscription with Cash App
Pay](https://docs.stripe.com/billing/subscriptions/cash-app-pay) for more
details.

[Set up
StripeServer-side](https://docs.stripe.com/payments/cash-app-pay/set-up-payment#web-set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/cash-app-pay/set-up-payment#web-create-customer)
To reuse a Cash App Pay payment method for future payments, attach it to a
[Customer](https://docs.stripe.com/api/customers).

Create a [Customer object](https://docs.stripe.com/api/customers) when your
customer creates an account with your business, and associate the ID of the
Customer object with your own internal representation of a customer.
Alternatively, you can create a new Customer later, right before saving a
payment method for future payments.

Create a new Customer or retrieve an existing Customer to associate with this
payment. Include the following code on your server to create a new Customer.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode description="My First Test Customer (created for API docs)"
```

[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/cash-app-pay/set-up-payment#web-create-checkout-session)
Your customer must authorize you to use their Cash App account for future
payments through Stripe Checkout. This allows you to accept Cash App payments.
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
returned in the response.

```
Stripe::Checkout::Session.create({
 mode: 'setup',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'cashapp'],
 customer: customer.id,
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

[Test your
integrationServer-side](https://docs.stripe.com/payments/cash-app-pay/set-up-payment#web-test-integration)Mobile
web app testingDesktop web app testing
To test your integration, choose Cash App Pay as the payment method and tap
**Pay**. While testing, this redirects you to a test payment page where you can
approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile
application—you don’t have the option to approve or decline the payment within
Cash App. The payment is automatically approved after the redirect.

## Links

- [Checkout](https://docs.stripe.com/payments/checkout)
- [Set up a subscription with Cash App
Pay](https://docs.stripe.com/billing/subscriptions/cash-app-pay)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)