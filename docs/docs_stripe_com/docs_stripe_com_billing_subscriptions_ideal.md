# Set up a subscription with iDEAL and SEPA Direct Debit

## Learn how to create and charge a subscription with iDEAL and SEPA Direct Debit.

iDEAL is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
each payment. After your customer authenticates the payment, Stripe saves your
customer’s
[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) in a
[SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit) payment method.
You can then use the SEPA Direct Debit payment method to [accept future
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment).

With this integration, Stripe charges the first Subscription payment through
iDEAL to collect your customer’s bank details. If you’re offering a free trial,
Stripe charges your customer 0.01 EUR through iDEAL to collect their bank
details and immediately refunds it.

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions) represents
the details of your customer’s intent to purchase. You create a Checkout Session
when your customer wants to start a
[subscription](https://docs.stripe.com/billing/subscriptions/creating). After
redirecting your customer to a Checkout Session, Stripe presents a payment form
where your customer can complete their purchase. After your customer completes a
purchase, they’re redirected back to your site.

[Set up
StripeServer-side](https://docs.stripe.com/billing/subscriptions/ideal#web-setup)
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

From the command-line, use an install script or download and extract a versioned
archive file for your operating system to install the CLI.

homebrewaptyumScoopmacOSLinuxWindowsDocker
To install the Stripe CLI with [homebrew](https://brew.sh/), run:

```
brew install stripe/stripe-cli/stripe
```

This command fails if you run it on the Linux version of homebrew, but you can
use this alternative or follow the instructions on the Linux tab.

```
brew install stripe-cli
```

To run the Stripe CLI, you must also pair it with your Stripe account. Run
`stripe login` and follow the prompts. For more information, see the [Stripe CLI
documentation page](https://docs.stripe.com/stripe-cli).

[Create the pricing modelDashboardStripe
CLI](https://docs.stripe.com/billing/subscriptions/ideal#create-pricing-model)
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
SessionClient-sideServer-side](https://docs.stripe.com/billing/subscriptions/ideal#create-checkout-session)
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

Create a Session with the ID of an existing
[Price](https://docs.stripe.com/api/prices). Make sure that the mode is set to
`subscription` and that you pass at least one recurring price. You can add
one-time prices in addition to recurring prices. After creating the Checkout
Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

When creating a Session, you can specify `payment_method_types` or have Stripe
automatically pick payment methods based on your
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) settings. If
you don’t specify `payment_method_types`, you must turn on iDEAL recurring
payments in the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). This enables
SEPA Direct Debit for recurring iDEAL payments only, but doesn’t turn on SEPA
Direct Debit payments as a stand alone payment method.

Listing payment methods manuallyManage payment methods from the Dashboard
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="ideal" \
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
successful](https://docs.stripe.com/billing/subscriptions/ideal#payment-success)
When your customer completes a payment, they’re redirected to the URL that you
specified as the `success_url`. This is typically a page on your website that
informs your customer that their payment was successful.

Use the Dashboard, a custom [webhook](https://docs.stripe.com/webhooks), or a
third-party plugin to handle post-payment events like sending an order
confirmation email to your customer, logging the sale in a database, or starting
a shipping workflow.

DashboardWebhooks
Successful payments appear in the Dashboard’s [list of
payments](https://dashboard.stripe.com/payments). When you click a payment, it
takes you to the payment detail page. The **Checkout summary** section contains
billing information and the list of items purchased, which you can use to
manually fulfill the order.

![Checkout
summary](https://b.stripecdn.com/docs-statics-srv/assets/source.16d3029596357c80a8efdbbfe106108a.png)

When a customer successfully pays for a recurring service, they’re automatically
subscribed. Their subscription is recorded as a new entry in the Dashboard’s
[list of subscriptions](https://dashboard.stripe.com/subscriptions).

#### Note

Stripe can help you keep up with incoming payments by sending you email
notifications whenever a customer successfully completes one. Use the Dashboard
to [configure email notifications](https://dashboard.stripe.com/settings/user).

You can use plugins like [Zapier](https://stripe.com/works-with/zapier) to
automate updating your purchase fulfillment systems with information from Stripe
payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful
payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or
chat applications
[Test the
integration](https://docs.stripe.com/billing/subscriptions/ideal#testing)
Using your [test API keys](https://docs.stripe.com/keys#test-live-modes), select
any bank from the list. After confirming, you’re redirected to a test page with
options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the setup is
successful.
- Click **Fail test payment** to test the case when the customer fails to
authenticate.
[OptionalCreate a trial for your
subscription](https://docs.stripe.com/billing/subscriptions/ideal#trials)
## See also

- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

## Links

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
- [homebrew](https://brew.sh/)
- [Stripe CLI documentation page](https://docs.stripe.com/stripe-cli)
- [products](https://docs.stripe.com/api/products)
- [prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
- [test mode to live mode](https://docs.stripe.com/keys#test-live-modes)
- [Billing examples](https://docs.stripe.com/products-prices/pricing-models)
- [Create a Session](https://docs.stripe.com/api/checkout/sessions/create)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [webhook](https://docs.stripe.com/webhooks)
- [list of payments](https://dashboard.stripe.com/payments)
- [list of subscriptions](https://dashboard.stripe.com/subscriptions)
- [configure email notifications](https://dashboard.stripe.com/settings/user)
- [Zapier](https://stripe.com/works-with/zapier)
- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)