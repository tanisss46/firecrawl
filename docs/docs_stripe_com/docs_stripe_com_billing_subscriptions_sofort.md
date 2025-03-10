# Set up a subscription with Sofort and SEPA Direct Debit

## Learn how to create and charge a subscription with Sofort and SEPA Direct Debit.

#### Warning

New businesses can’t accept SOFORT payments and our financial partners are in
the process of discontinuing SOFORT. For more information, read our [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method).

Sofort is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
each payment. After your customer authenticates the payment, Stripe saves your
customer’s
[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) in a
[SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit) payment method.
You can then use the SEPA Direct Debit payment method to [accept future
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment).

With this integration, Stripe charges the first Subscription payment through
Sofort to collect your customer’s bank details. If you’re offering a free trial,
Stripe charges your customer 1 EUR through Sofort to collect their bank details
and immediately refunds it.

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions) represents
the details of your customer’s intent to purchase. You create a Checkout Session
when your customer wants to start a
[subscription](https://docs.stripe.com/billing/subscriptions/creating). After
redirecting your customer to a Checkout Session, Stripe presents a payment form
where your customer can complete their purchase. After your customer completes a
purchase, they’re redirected back to your site.

[Set up
StripeServer-side](https://docs.stripe.com/billing/subscriptions/sofort#web-setup)
Install the Stripe client of your choice:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

Install the Stripe CLI (optional). The CLI provides [webhook
testing](https://docs.stripe.com/webhooks#test-webhook), and you can run it to
create your products and prices.

```
# Install Homebrew to run this command: https://brew.sh/
brew install stripe/stripe-cli/stripe

# Connect the CLI to your dashboard
stripe login
```

For additional install options, see [Get started with the Stripe
CLI](https://docs.stripe.com/stripe-cli).

[Create the pricing modelDashboardStripe
CLI](https://docs.stripe.com/billing/subscriptions/sofort#create-pricing-model)
Create your [products](https://docs.stripe.com/api/products) and their
[prices](https://docs.stripe.com/api/prices) in the Dashboard or with the Stripe
CLI.

This example uses a fixed-price service with two different service-level
options: Basic and Premium. For each service-level option, you need to create a
product and a recurring price. (If you want to add a one-time charge for
something like a setup fee, create a third product with a one-time price. To
keep things simple, this example doesn’t include a one-time charge.)

In this example, each product bills at monthly intervals. The price for the
Basic product is 5 EUR. The price for the Premium product is 15 EUR.

DashboardStripe CLI
Go to the [Add a product](https://dashboard.stripe.com/test/products/create)
page and create two products. Add one price for each product, each with a
monthly recurring billing period:

- Premium product: Premium service with extra features

- Price: Standard pricing | 15 EUR
- Basic product: Basic service with minimum features

- Price: Standard pricing | 5 EUR

After you create the prices, record the price IDs so you can use them in other
steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the ** to live mode** button at the top right of the
page to clone your product from [test mode to live
mode](https://docs.stripe.com/keys#test-live-modes).

For other pricing models, see [Billing
examples](https://docs.stripe.com/products-prices/pricing-models).

[Create a Checkout
SessionClient-sideServer-side](https://docs.stripe.com/billing/subscriptions/sofort#create-checkout-session)
Add a checkout button to your website that calls a server-side endpoint to
create a Checkout Session.

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

Create a Checkout Session with the ID of an existing
[Price](https://docs.stripe.com/api/prices). Make sure that the mode is set to
`subscription` and that you pass at least one recurring price. You can add
one-time prices in addition to recurring prices. After creating the Checkout
Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

When creating a Session, you can specify `payment_method_types` or have Stripe
automatically pick payment methods based on your
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) settings. If
you don’t specify `payment_method_types`, you must turn on Sofort recurring
payments in the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). This enables
SEPA Direct Debit for recurring Sofort payments only, but doesn’t turn on SEPA
Direct Debit payments as a stand alone payment method.

Listing payment methods manuallyManage payment methods from the Dashboard
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="sofort" \
 -d "line_items[][price]"={{PRICE_ID}} \
 -d "line_items[][quantity]"=1 \
 -d "mode"="subscription" \
-d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
\
 -d "cancel_url"="https://example.com/cancel" \
```

When your customer successfully completes their payment, they’re redirected to
the `success_url`, a page on your website that informs the customer that their
payment was successful. Make the Session ID available on your success page by
including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as
in the above example.

When your customer clicks on your logo in a Checkout Session without completing
a payment, Checkout redirects them back to your website by navigating to the
`cancel_url`. Typically, this is the page on your website that the customer
viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation by default.

#### Caution

Don’t rely on the redirect to the `success_url` alone for detecting payment
initiation, as:

- Malicious users could directly access the `success_url` without paying and
gain access to your goods or services.
- Customers may not always reach the `success_url` after a successful
payment—they might close their browser tab before the redirect occurs.
[Confirm the payment is
successful](https://docs.stripe.com/billing/subscriptions/sofort#payment-success)
When your customer completes a payment, Stripe redirects them to the URL that
you specified in the `success_url` parameter. Typically, this is a page on your
website that informs your customer that their payment is successful.

Sofort is a delayed notification payment method, which means that funds aren’t
immediately available. A Sofort payment takes up to 14 business days to make the
funds available. Because of this possibility, you might want to delay order
fulfillment until the funds are available. After the payment succeeds, the
underlying [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
status changes from `processing` to `succeeded`.

Stripe recommends fulfilling orders during the `processing` state. On average,
approximately 0.2% of Sofort payments fail after entering the `processing`
state.

There are several ways you can confirm the payment is successful:

DashboardWebhooksThird-party plugins
Successful payments appear in the Dashboard’s [list of
payments](https://dashboard.stripe.com/payments). Click a payment to open the
payment detail page. The **Checkout summary** section contains billing
information and the list of items purchased, which you can use to manually
fulfill the order.

!

#### Note

Stripe can help you keep up with incoming payments by sending you email
notifications whenever a customer successfully completes one. Use the Dashboard
to [configure email notifications](https://dashboard.stripe.com/settings/user).

[Test the
integration](https://docs.stripe.com/billing/subscriptions/sofort#testing)
Using your [test API keys](https://docs.stripe.com/keys#test-live-modes), select
Sofort as the payment method and click the **Subscribe** button. After
confirming, you’re redirected to a test page with options to authorize or fail
the payment. Sofort payments remain pending for 3 minutes in a
[sandbox](https://docs.stripe.com/sandboxes).

- Click **Authorize test payment** to test the case when the setup is
successful.
- Click **Fail test payment** to test the case when the customer fails to
authenticate.
[OptionalCreate a trial for your
subscription](https://docs.stripe.com/billing/subscriptions/sofort#trials)
## See also

- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

## Links

- [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [accept future
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [sample on
GitHub](https://github.com/stripe-samples/checkout-single-subscription)
- [demo](https://checkout.stripe.dev/checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [webhook testing](https://docs.stripe.com/webhooks#test-webhook)
- [https://brew.sh/](https://brew.sh/)
- [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [products](https://docs.stripe.com/api/products)
- [prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
- [test mode to live mode](https://docs.stripe.com/keys#test-live-modes)
- [Billing examples](https://docs.stripe.com/products-prices/pricing-models)
- [Create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [list of payments](https://dashboard.stripe.com/payments)
- [configure email notifications](https://dashboard.stripe.com/settings/user)
- [sandbox](https://docs.stripe.com/sandboxes)
- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)