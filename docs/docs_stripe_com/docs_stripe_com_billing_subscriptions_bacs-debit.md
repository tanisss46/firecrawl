# Set up a subscription with Bacs Direct Debit

## Learn how to create and charge for a subscription with Bacs Direct Debit.

Use this guide to set up a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[Bacs Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
as a payment method and [Checkout](https://docs.stripe.com/payments/checkout).

[Set up
StripeServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#web-setup)
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
prices](https://docs.stripe.com/billing/subscriptions/bacs-debit#create-products-and-prices)
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
USD/month, 100 USD/year, 9 GBP/month, and 90 GBP/year. This allows you to change
and add prices without needing to change the details of your underlying
products. You can create a product and price [through the
API](https://docs.stripe.com/api/prices) or through [the Stripe
Dashboard](https://dashboard.stripe.com/products).

If your price is determined at checkout (for example, the customer sets a
donation amount) or you prefer not to create prices upfront, you can create
[prices
inline](https://docs.stripe.com/billing/subscriptions/bacs-debit#creating-prices-inline)
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
SessionClient-sideServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#create-checkout-session)
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
 -d "line_items[][price]"={{PRICE_ID}} \
 -d "line_items[][quantity]"=1 \
 -d "mode"="subscription" \
-d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
\
 -d "cancel_url"="https://example.com/cancel" \
```

When your customer successfully completes their payment, they’re redirected to
the `success_url`, a page on your website that informs them that their payment
was successful. Make the Session ID available on your success page by including
the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the
above example.

When your customer clicks on your logo in a Checkout Session without completing
a payment, Checkout redirects them back to your website by navigating to the
`cancel_url`. Typically, this is the page on your website that the customer
viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation by default.

From the [Dashboard](https://dashboard.stripe.com/settings/payment_methods),
enable the payment methods you want to accept from your customers. Checkout
supports [several payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support).

#### Caution

Don’t rely on the redirect to the `success_url` alone for detecting payment
initiation, as:

- Malicious users could directly access the `success_url` without paying and
gain access to your goods or services.
- Customers may not always reach the `success_url` after a successful
payment—they might close their browser tab before the redirect occurs.
[Confirm the payment is
successful](https://docs.stripe.com/billing/subscriptions/bacs-debit#payment-success)
When your customer completes a payment, Stripe redirects them to the URL that
you specified in the `success_url` parameter. Typically, this is a page on your
website that informs your customer that their payment was successful.

However, Bacs Direct Debit is a delayed notification payment method, which means
that funds aren’t immediately available. A Bacs Direct Debit payment typically
takes three business days to make the funds available. Because of this, you’ll
want to delay order fulfillment until the funds are available. After the payment
succeeds, the underlying
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) status changes
from `processing` to `succeeded`.

You can confirm the payment is successful in several ways:

DashboardWebhooksThird-party plugins
Successful payments appear in the Dashboard’s [list of
payments](https://dashboard.stripe.com/payments). When you click a payment, it
takes you to the payment detail page. The **Checkout summary** section contains
billing information and the list of items purchased, which you can use to
manually fulfill the order.

!

#### Note

Stripe can help you keep up with incoming payments by sending you email
notifications whenever a customer successfully completes one. Use the Dashboard
to [configure email notifications](https://dashboard.stripe.com/settings/user).

[Test the
integration](https://docs.stripe.com/billing/subscriptions/bacs-debit#testing)
There are several test bank account numbers you can use in [test
mode](https://docs.stripe.com/keys#test-live-modes) to make sure this
integration is ready.

Sort code Account numberDescription10-88-0000012345The payment succeeds and the
Invoice transitions to `paid`.10-88-0090012345The payment succeeds after three
minutes and the Invoice transitions to `paid`.10-88-0033333335The payment fails
with a `debit_not_authorized` failure code and the Invoice transitions to
`open`. The Mandate becomes `inactive` and the PaymentMethod can not be used
again.10-88-0093333335The payment fails after three minutes with a
`debit_not_authorized` failure code and the Invoice transitions to `open`. The
Mandate becomes `inactive` and the PaymentMethod can not be used
again.10-88-0022222227The payment fails with an `insufficient_funds` failure
code and the Invoice transitions to `open`. The Mandate remains `active` and the
PaymentMethod can be used again.10-88-0092222227The payment fails after three
minutes with an `insufficient_funds` failure code and the Invoice transitions to
`open`. The Mandate remains `active` and the PaymentMethod can be used
again.10-88-0055555559The payment succeeds after three minutes and the Invoice
transitions to `paid`, but a dispute is immediately
created.10-88-0000033333Payment Method creation succeeds, but the Mandate is
refused by the customer’s bank and immediately transitions to
inactive.10-88-0000044444The request to set up Bacs Direct Debit fails
immediately due to an invalid account number and the customer is prompted to
update their information before submitting. Payment details are not collected.
You can test using any of the account numbers provided above. However, because
Bacs Direct Debit payments take several days to process, use the test account
numbers that operate on a three-minute delay to better simulate the behavior of
live payments.

#### Note

By default, Stripe automatically sends
[emails](https://docs.stripe.com/payments/payment-methods/bacs-debit#debit-notifications)
to the customer when payment details are initially collected and each time a
debit will be made on their account. These notifications aren’t sent in
testmode.

[OptionalAdding a one-time setup
feeServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#adding-setup-fee)[OptionalCreate
prices and products
inlineServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#creating-prices-inline)[OptionalExisting
customersServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#handling-existing-customers)[OptionalPrefill
customer
dataServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#prefilling-customer-data)[OptionalHandling
trialsServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#handling-checkout-trials)[OptionalTax
ratesServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#tax-rates)[OptionalAdding
couponsServer-side](https://docs.stripe.com/billing/subscriptions/bacs-debit#coupons)
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
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [Checkout](https://docs.stripe.com/payments/checkout)
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
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [several payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [list of payments](https://dashboard.stripe.com/payments)
- [configure email notifications](https://dashboard.stripe.com/settings/user)
- [test mode](https://docs.stripe.com/keys#test-live-modes)
-
[emails](https://docs.stripe.com/payments/payment-methods/bacs-debit#debit-notifications)
- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)