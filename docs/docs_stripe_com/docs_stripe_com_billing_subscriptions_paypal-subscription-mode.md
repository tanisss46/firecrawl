# Set up a subscription with PayPal

## Learn how to create and charge for a subscription with PayPal and Checkout.

Use this guide to set up a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[PayPal](https://docs.stripe.com/payments/paypal) and
[Checkout](https://docs.stripe.com/payments/checkout).

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions) represents
the details of a customer’s intent to purchase. Create a Checkout Session when a
customer wants to start a subscription. After redirecting a customer to a
Checkout Session, Stripe presents a payment form where they can complete their
purchase. After they complete a purchase, Stripe redirects them back to your
site.

#### Caution

To start accepting PayPal subscriptions on Stripe, you need to [enable PayPal
recurring
payments](https://docs.stripe.com/payments/paypal/set-up-future-payments?platform=web#enable-recurring-payments-support-from-stripe-dashboard)
from the Dashboard.

[Set up
StripeServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#web-setup)
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

[Create recurring products and
prices](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#create-products-and-prices)
#### Caution

The Prices API unifies how one-time purchases and subscriptions are modeled on
Stripe. Existing integrations that don’t use the Prices API are still
[supported](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations).
However, some Checkout features only support Prices. See the [migration
guide](https://docs.stripe.com/payments/checkout/migrating-prices) to upgrade to
the Prices API.

To use Checkout, you first need to create a
[Product](https://docs.stripe.com/api/products) and a
[Price](https://docs.stripe.com/api/prices). Different physical goods or levels
of service must be represented by products. Each product’s pricing is
represented by one or more prices.

For example, you can create a software *product* that has four *prices*: 10
USD/month, 100 USD/year, 9 eur/month, and 90 eur/year. This allows you to change
and add prices without needing to change the details of your underlying
products. You can either create a product and price [through the
API](https://docs.stripe.com/api/prices) or through [the Stripe
Dashboard](https://dashboard.stripe.com/products).

If your price is determined at checkout (for example, the customer sets a
donation amount) or you prefer not to create prices upfront, you can create
[prices
inline](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#creating-prices-inline)
at Checkout Session creation.

DashboardAPI
Before you start configuring products, make sure you’re in a sandbox. Next,
define the goods and services you plan to sell. To create a new product and
price:

- Navigate to the [Products](https://dashboard.stripe.com/products) section in
the Dashboard
- Click **Add product**
- Select “Recurring” when setting the price
- Configure the pricing plan

You can define multiple pricing plans with different parameters for each
recurring product. Each price has a generated ID that you can use as a reference
during the checkout process.

#### Note

Products created in a sandbox can be copied to live mode so that you don’t need
to re-create them. In the Product detail view in the Dashboard, click ** to
live mode** on the upper right corner. You can only do this once for each
product created in a sandbox. Subsequent updates to the test product are not
reflected for the live product.

[Create a Checkout
SessionClient-sideServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#create-checkout-session)
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
[Price](https://docs.stripe.com/api/prices). Make sure that mode is set to
`subscription` and you pass at least one recurring price. You can add one-time
prices in addition to recurring prices. After creating the Checkout Session,
redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="paypal" \
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
successful](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#payment-success)
#### Note

When a buyer successfully confirms a subscription on Stripe with PayPal, they
receive a receipt from Stripe as well as from PayPal.

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
integration](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#testing)
Test your PayPal integration with your [test API
keys](https://docs.stripe.com/keys#test-live-modes) by viewing the redirect
page. You can test the successful payment case by authenticating the payment on
the redirect page. The PaymentIntent will transition from `requires_action` to
`succeeded`.

To test the case where the user fails to authenticate, use your test API keys
and view the redirect page. On the redirect page, click **Fail test payment**.
The PaymentIntent will transition from `requires_action` to
`requires_payment_method`.

[OptionalAdding a one-time setup
feeServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#adding-setup-fee)[OptionalCreate
prices and products
inlineServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#creating-prices-inline)[OptionalExisting
customersServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#handling-existing-customers)[OptionalPrefill
customer
dataServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#prefilling-customer-data)[OptionalHandling
trialsServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#handling-checkout-trials)[OptionalTax
ratesServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#tax-rates)[OptionalAdding
couponsServer-side](https://docs.stripe.com/billing/subscriptions/paypal-subscription-mode#coupons)
## See also

- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

## Links

- [sample on
GitHub](https://github.com/stripe-samples/checkout-single-subscription)
- [demo](https://checkout.stripe.dev/checkout)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [enable PayPal recurring
payments](https://docs.stripe.com/payments/paypal/set-up-future-payments?platform=web#enable-recurring-payments-support-from-stripe-dashboard)
- [Register now](https://dashboard.stripe.com/register)
-
[supported](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations)
- [migration guide](https://docs.stripe.com/payments/checkout/migrating-prices)
- [Product](https://docs.stripe.com/api/products)
- [Price](https://docs.stripe.com/api/prices)
- [the Stripe Dashboard](https://dashboard.stripe.com/products)
- [Create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [webhook](https://docs.stripe.com/webhooks)
- [list of payments](https://dashboard.stripe.com/payments)
- [configure email notifications](https://dashboard.stripe.com/settings/user)
- [Zapier](https://stripe.com/works-with/zapier)
- [test API keys](https://docs.stripe.com/keys#test-live-modes)
- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)