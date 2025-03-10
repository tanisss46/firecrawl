# Set up a subscription with SEPA Direct Debit

## Learn how to create and charge a subscription with SEPA Direct Debit.

Stripe-hosted pageAdvanced integration
A [Checkout Session](https://docs.stripe.com/api/checkout/sessions) represents
the details of your customer’s intent to purchase. You create a Checkout Session
when your customer wants to start a
[subscription](https://docs.stripe.com/billing/subscriptions/creating). After
redirecting your customer to a Checkout Session, Stripe presents a payment form
where your customer can complete their purchase. Once your customer has
completed a purchase, they will be redirected back to your site.

[Set up
StripeServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#web-setup)
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
CLI](https://docs.stripe.com/billing/subscriptions/sepa-debit#create-pricing-model)
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
SessionClient-sideServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#create-checkout-session)
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
[Price](https://docs.stripe.com/api/prices). Ensure that mode is set to
`subscription` and you pass at least one recurring price. You can add one-time
prices in addition to recurring prices. After creating the Checkout Session,
redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="sepa_debit" \
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

From your [Dashboard](https://dashboard.stripe.com/settings/payment_methods),
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
successful](https://docs.stripe.com/billing/subscriptions/sepa-debit#payment-success)
When your customer completes a payment, Stripe redirects them to the URL that
you specified in the `success_url` parameter. Typically, this is a page on your
website that informs your customer that their payment was successful.

However, SEPA Direct Debit is a delayed notification payment method, which means
that funds aren’t immediately available. A SEPA Direct Debit payment typically
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
integration](https://docs.stripe.com/billing/subscriptions/sepa-debit#testing)
You can test your integration using the IBANs below. The payment method details
are successfully collected for each IBAN but exhibit different behavior when
charged.

##### Test IBANs

AustriaBelgiumCroatiaEstoniaFinlandFranceGermanyGibraltarIrelandLiechtensteinLithuaniaLuxembourgNetherlandsNorwayPortugalSpainSwedenSwitzerlandUnited
KingdomAccount NumberDescription`AT611904300234573201`The PaymentIntent status
transitions from `processing` to `succeeded`.`AT321904300235473204`The
PaymentIntent status transitions from `processing` to `succeeded` after at least
three minutes.`AT861904300235473202`The PaymentIntent status transitions from
`processing` to `requires_payment_method`.`AT051904300235473205`The
PaymentIntent status transitions from `processing` to `requires_payment_method`
after at least three minutes.`AT591904300235473203`The PaymentIntent status
transitions from `processing` to `succeeded`, but a dispute is immediately
created.`AT981904300000343434`The payment fails with a
`charge_exceeds_source_limit` failure code due to payment amount causing account
to exceed its weekly payment volume limit.`AT601904300000121212`The payment
fails with a `charge_exceeds_weekly_limit` failure code due to payment amount
exceeding account's transaction volume limit.[OptionalAdding a one-time setup
feeServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#adding-setup-fee)[OptionalCreate
prices and products
inlineServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#creating-prices-inline)[OptionalExisting
customersServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#handling-existing-customers)[OptionalPrefill
customer
dataServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#prefilling-customer-data)[OptionalHandling
trialsServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#handling-checkout-trials)[OptionalTax
ratesServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#tax-rates)[OptionalAdding
couponsServer-side](https://docs.stripe.com/billing/subscriptions/sepa-debit#coupons)
## See also

- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

## Links

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
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [several payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [list of payments](https://dashboard.stripe.com/payments)
- [configure email notifications](https://dashboard.stripe.com/settings/user)
- [Customize your
integration](https://docs.stripe.com/payments/checkout/customization)
- [Manage subscriptions with the customer
portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)