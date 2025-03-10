# Recurring pricing models

## Learn about common pricing models and how to create them.

[Pricing models](https://docs.stripe.com/products-prices/pricing-models) are
patterns that represent your business on Stripe. With
[Product](https://docs.stripe.com/api/products) and
[Price](https://docs.stripe.com/api/prices) objects, you can model what you sell
and how you charge for it.

## Flat rate: Good-better-best

Many SaaS businesses offer their customers a choice of escalating service
options. This flat-rate pricing model is called *good-better-best*. Customers
choose a service tier (good, better, or best) and pay a flat rate for it.

Imagine a business called Togethere that sells a collaboration platform. They
offer three different service levels: basic, starter, and enterprise. For each
service level, they offer a monthly and yearly price. Togethere operates in
several countries, so they have prices in multiple currencies.

In this example, Togethere has three products: `Basic`, `Starter`, `Enterprise`.
Each product has several different prices. The basic level has prices for 10 USD
per month and 100 USD per year. Both prices are for the same `Basic` product, so
they share the same product description on the customer’s receipt and invoice.

Here’s what that model looks like on Stripe:

!

Flat rate: Good-better-best pricing model

### Model good-better-best on Stripe

DashboardAPI
To create a good-better-best model on Stripe through the Dashboard follow the
steps below.

First, create the `Basic` product. To learn about all the options for creating a
product, see the [prices
guide](https://docs.stripe.com/products-prices/manage-prices#create-product).

- Go to [Product catalog](https://dashboard.stripe.com/products).
- Click **+ Create product**.
- Enter a **Name** for the product.
- (Optional) Add a **Description**. The description appears at checkout, on the
[customer portal](https://docs.stripe.com/customer-management), and in
[quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the `Basic` product:

- Click **More pricing options**.
- Select **Recurring**.
- For **Choose your pricing model**, select **Flat rate**.
- For **Amount**, enter a price amount.
- For **Billing period**, select **Monthly**.
- Click **Next** to save the price.

Then, create the yearly price for the `Basic` product:

- Click **+ Add another price**.
- Select **Recurring**.
- For **Choose your pricing model**, select **Flat rate**.
- For **Amount**, enter a price amount.
- For **Billing period**, select **Yearly**.
- Click **Next**.
- Click **Add product** to save the product and price. You can edit the product
and price later.

The subscription integration guide explains how to fit pricing models into a
full integration.

- If you’re using Stripe Checkout, the next step is to [create a Checkout
session](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)
for your site. Make sure to set up Stripe.
- If you’re using Stripe Elements, the next step is to [create a
Customer](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#create-customer).
Make sure you set up Stripe and the sample application.

## Per-seat

Togethere, our example collaboration platform company, also wants to offer a
per-seat plan. Per-seat pricing is another common offering for SaaS businesses.
Togethere’s customers pick how many seats they’ll use, and Togethere charges
based on that amount.

To model this scenario, Togethere creates a product and price structure where
each unit represents a user. When Togethere creates a subscription for a
customer, the customer specifies the number of users for that subscription.

Here’s what that model looks like on Stripe:

!

Per-seat pricing model

See the
[advanced](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models)
pricing model section for examples of other models. [Flat rate and
per-seat](https://docs.stripe.com/products-prices/pricing-models#adding-flat-fees)
pricing, where you charge a customer a flat monthly fee in addition to a
per-seat rate, is another common model for SaaS businesses.

### Model per-seat pricing on Stripe

DashboardAPI
To create a per-seat model on Stripe through the Dashboard follow the steps
below.

First, create the `Per-seat` product. To learn about all the options for
creating a product, see the [prices
guide](https://docs.stripe.com/products-prices/manage-prices#create-product).

- Go to [Product catalog](https://dashboard.stripe.com/products).
- Click **+ Create product**.
- Enter a **Name** for the product.
- (Optional) Add a **Description**. The description appears at checkout, on the
[customer portal](https://docs.stripe.com/customer-management), and in
[quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the product:

- Select **Recurring**.
- For **Amount**, enter a price amount.
- For **Billing period**, select **Monthly**.
- Click **Add product** to save the product and price. You can edit the product
and price later.

To create a subscription using that price:

- Go to the **Payments** > **Subscriptions** page.
- Click **+ Create subscription**.
- Find or add a customer.
- Search for the product you created and select the price you want to use.
- (Optional) Select **Collect tax automatically** to use Stripe Tax.
- Click **Start subscription** to start it immmediately or **Schedule
subscription** to start it on another schedule.

The subscription integration guide explains how to fit pricing models into a
full integration.

- If you’re using Stripe Checkout, the next step is to [create a Checkout
session](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)
for your site. Make sure you set up Stripe.
- If you’re using Stripe Elements, the next step is to [create a
Customer](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#create-customer).
Make sure you set up Stripe and the sample application.

For other versions of per-seat pricing, see the
[advanced](https://docs.stripe.com/products-prices/pricing-models#advanced)
models section.

## Usage-based pricing

Usage-based pricing is a common pricing model for SaaS businesses that enables
you to charge based on a customer’s usage of your product or service. As a
business, you provide access to your service and bill your customer based on
their usage. To see what an end-to-end integration based on the usage-based
pricing model looks like, read the [usage-based pricing
models](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models)
guide.

## Tiered pricing

Prices can represent tiers, allowing the unit cost to change with quantity or
usage. Togethere might, for example, want to offer lower rates for customers who
use more projects per month. The following examples show two different ways to
adjust pricing as usage increases: volume-based pricing and graduated pricing.
To demonstrate these approaches to tiered pricing, we’ll use the following
tiers:

Number of projectsPrice per tier1-57 USD6-106.50 USD11+6 USD
Use `tiers` if you need non-linear pricing when `quantity` or
[usage](https://docs.stripe.com/api/billing/meter-event) changes. You can also
combine tiered pricing with base fees to create more [complex pricing
models](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models).

When you [create a price](https://docs.stripe.com/api#create_price) with
`billing_scheme=per_unit`, the `unit_amount` is the same regardless of how many
units a customer buys. Stripe multiplies this amount by the `quantity` to
determine the total cost. For example, a `unit_amount` of 5 USD creates this
billing structure:

Quantity/Usage at end of periodTotal cost15 USD525 USD630 USD20100 USD25125 USD
When you create a price with `billing_scheme=tiered`, the unit cost varies
depending on how many units your customer buys. Here’s an example tier
structure:

TierAmount (unit cost)1-5 (`up_to=5`)5 USD (`unit_amount=500`)6-10 (`up_to=10`)4
USD (`unit_amount=400`)10-15 (`up_to=15`)3 USD (`unit_amount=300`)15-20
(`up_to=20`)2 USD (`unit_amount=200`)20+ (`up_to=inf`)1 USD (`unit_amount=100`)
Multiplication happens:

- At the start of the billing period if the `Price` objects have
`recurring.usage_type = licensed`.
- At the end of the billing period if the `Price` objects have
`recurring.usage_type = metered`.

With tiered billing, you:

- Set the `tiers_mode` to either `volume` or `graduated`.
- Create a `tiers` array to represent the tiers structure.

See also the
[volume-based](https://docs.stripe.com/products-prices/pricing-models#volume-based-pricing)
and
[graduated](https://docs.stripe.com/products-prices/pricing-models#graduated-pricing)
pricing examples.

### Volume-based pricing

With volume-based pricing, the subscription item is billed at the tier
corresponding to the amount of usage at the end of the period. To implement
volume-based billing tiers, set `volume` as the value of `tiers_mode`:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Project Volume Pricing" \
 -d "tiers[0][unit_amount]"=700 \
 -d "tiers[0][up_to]"=5 \
 -d "tiers[1][unit_amount]"=650 \
 -d "tiers[1][up_to]"=10 \
 -d "tiers[2][unit_amount]"=600 \
 -d "tiers[2][up_to]"=inf \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d "recurring[usage_type]"=metered \
 -d product={{PRODUCT_ID}} \
 -d tiers_mode=volume \
 -d billing_scheme=tiered \
 -d "expand[0]"=tiers
```

Under volume-based pricing, a customer with 5 projects is charged 35 USD (5 × 7
USD). If they accumulate 6 projects the following month, then all projects are
billed at the `6-10` rate. That month, they’re charged 39 USD (6 × 6.50 USD).

With `tiers_mode=volume`, the entire `quantity` (or `usage`) is multiplied by
the unit cost of the tier.

Quantity/usage at end of periodUnit costTotal for volume-tiered pricing17 USD7
USD57 USD35 USD66.5 USD39 USD206 USD120 USD256 USD150 USD
Because the tier price applies to the entire `quantity` (or `usage`), the total
might decrease when calculating the final cost.

### Graduated pricing

While similar to volume pricing, graduated pricing charges for the usage in each
tier instead of applying a single price to all usage. To use graduated tiers,
set the value of `tiers_mode` to `graduated`:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Per-minute pricing" \
 -d "tiers[0][unit_amount]"=500 \
 -d "tiers[0][up_to]"=5 \
 -d "tiers[1][unit_amount]"=400 \
 -d "tiers[1][up_to]"=10 \
 -d "tiers[2][unit_amount]"=100 \
 -d "tiers[2][up_to]"=inf \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d "recurring[usage_type]"=metered \
 -d product={{PRODUCT_ID}} \
 -d tiers_mode=graduated \
 -d billing_scheme=tiered \
 -d "expand[0]"=tiers
```

With graduated pricing, 5 projects result in the same charge as volume-based
pricing—35 USD total at 7 USD per project. This changes as usage breaks out of
the first tier. A customer with more than 5 projects is charged 7 USD per
project for the first 5 projects, then 6.50 USD for projects 6 through 10, and
finally 6 USD per project thereafter. A customer with 6 projects is charged
41.50 USD, 35 USD for the first 5 projects and 6.50 USD for the 6th project.

With `tiers_mode=graduated`, the `quantity` is multiplied by the amount that
falls into that tier. Then, the total is summed. For example, the total cost for
an amount of 6 is 29 USD: 25 USD for the 5 `quantity` that falls into the 1-5
tier, plus 4 USD for the single `quantity` that falls into the 6-10 tier.

Quantity and usage at end of the periodTotal for graduated tiered pricing15
USD525 USD629 USD2070 USD2575 USD
### Adding flat fees

You can specify a flat fee (`flat_amount`) to add to the
[invoice](https://docs.stripe.com/api/invoices). This works for both
`tiers_mode=volume` and `tiers_mode=graduated`. For example, you can have a flat
fee that increases when certain usage thresholds are met:

TierAmount (unit cost)Flat fee1-5 (`up_to=5`)5 USD (`unit_amount=500`)10 USD
(`flat_amount=1000`)6-10 (`up_to=10`)4 USD (`unit_amount=400`)20 USD
(`flat_amount=2000`)10-15 (`up_to=15`)3 USD (`unit_amount=300`)30 USD
(`flat_amount=3000`)15-20 (`up_to=20`)2 USD (`unit_amount=200`)40 USD
(`flat_amount=4000`)20+ (`up_to=inf`)1 USD (`unit_amount=100`)50 USD
(`flat_amount=5000`)
In this example, if `quantity` is `12` and `tiers_mode=volume`, the total amount
to be billed is `12 * 3 USD + 30 USD = 66 USD`.

If `quantity` is `12` and `tiers_mode=graduated`, the total amount is `5 * 5 USD
+ 10 USD + 5 * 4 USD + 20 USD + 2 * 3 USD + 30 USD = 111 USD`. A tier can have
either a `unit_amount` or a `flat_amount`, or both, but it must have at least
one of the two.

If `quantity` is `0`, the total amount is `10 USD` regardless of `tiers_mode`.
We always bill the first flat fee tier when `quantity=0`. To bill `0` when
there’s no usage, set up an `up_to=1` tier with an `unit_amount` equal to the
flat fee and omit the `flat_amount`.

## Variable pricing

There are two types of variable pricing models:

- **Inline pricing**: You define the price for your customer when you create a
subscription, invoice, or Checkout Session.
- **Pay-what-you-want pricing**: The customer fills in the price they pay, like
with a tip or donation. This type of variable pricing isn’t supported for
recurring payments. See [Let customers decide what to
pay](https://docs.stripe.com/payments/checkout/pay-what-you-want) for
information about using this type of pricing for single payments.

### Inline pricing

In some cases, you might want to use a custom price that hasn’t been
preconfigured. For example, you might want to use inline prices when you manage
your product catalog outside of Stripe.

#### Note

You can only create inline prices through the API. Inline prices aren’t
compatible with [Payment Links](https://docs.stripe.com/payment-links/api).

To create an inline price use case, pass in
[price_data](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data)
instead of a
[price.id](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-price-id)
when you create a subscription. For example, to subscribe a customer to a
monthly subscription with an inline price:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price_data][unit_amount]"=5000 \
 -d "items[0][price_data][currency]"=usd \
 -d "items[0][price_data][product]"={{PRODUCT_ID}} \
 -d "items[0][price_data][recurring][interval]"=month
```

This creates a monthly recurring price of 50 USD for the basic service offering.
By default, prices created with `price_data` are effectively archived (they’re
marked as `active=false`) so that they you can’t reuse them for other customers
or subscriptions. You can’t update or reuse inline prices after you create them.
You can also use `price_data` with these APIs:

- [Checkout](https://docs.stripe.com/api/checkout/sessions)
- [Invoice Items](https://docs.stripe.com/api/invoiceitems)
- [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules)

## Multi-currency prices

A single [Price](https://docs.stripe.com/api/prices) can support multiple
currencies. This helps you manage localized pricing when selling
internationally.

### Create multi-currency Prices

You can create multi-currency Prices in the
[API](https://docs.stripe.com/api/prices/create) or the Dashboard.

DashboardAPI
To create a multi-currency Price through the Dashboard:

- Go to [Product catalog](https://dashboard.stripe.com/test/products) and select
a product.
- Click **Edit product**.
- Click **+ Add another price** to create a new price. The default currency is
the first currency on your Price. All your Prices must have the same default
currency.
- To add a new currency option to your Price, click **+ Add a price by
currency**. Search and select from the list of supported currencies.- Stripe
suggests an exchange rate based on currency values at 12:00 PM EST, but you can
pick your own. For currencies that are subject to larger fluctuations, we
recommend adding more of a buffer.
- To save the new Price, click **Next** > **Update product**.

[Coupons](https://docs.stripe.com/billing/subscriptions/coupons#coupons),
[Promotion
Codes](https://docs.stripe.com/billing/subscriptions/coupons#promotion-codes),
and [Shipping
Rates](https://docs.stripe.com/payments/during-payment/charge-shipping) also
support multi-currency in a similar way to Prices.

### Render multi-currency Prices

To show your customer the price in their currency, you can retrieve the
multi-currency Price and view its
[currency_options.<currency>.unit_amount](https://docs.stripe.com/api/prices/object#price_object-currency_options-unit_amount)
field. The API response won’t include `currency_options` by default. To include
it in the response, [expand](https://docs.stripe.com/api/expanding_objects) the
`currency_options` field:

```
curl -G https://api.stripe.com/v1/prices/{{PRICE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=currency_options
```

#### Note

To improve latency and avoid problems with rate-limiting, cache the Price
instead of re-fetching it every time a customer visits your site.

### Use multi-currency Prices

Each purchase uses one of the multi-currency Price’s supported currencies,
depending on how you use the Price in your integration.

Stripe CheckoutPayment LinksSubscriptionsQuotesInvoicesOrders
Checkout automatically determines the customer’s local currency from their IP
address, as long as the Price supports that currency. If the customer’s local
currency isn’t supported, Checkout uses the Price’s default currency.

If a Checkout Session uses multiple Prices, Coupons, Promotion Codes, or
Shipping Rates, then they must all support the customer’s local currency, or
else Checkout uses the default currency. They must all have the same default
currency, or else Stripe returns an error when you create the Checkout Session.

Alternatively, you can use the
[currency](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-currency)
parameter to explicitly tell Checkout which currency to use.

Learn more about defining [manual currency
prices](https://docs.stripe.com/payments/checkout/manual-currency-prices) in
Checkout.

### Migrate from single-currency Prices to multi-currency

If you have an existing single-currency Price, you can retroactively add
multiple currencies to it in the Dashboard.

If you use Checkout or Payment Links, then multi-currency Prices take effect
automatically. If Stripe detects that the customer’s local currency is supported
by the Price, then it automatically uses that currency. If you use multiple
Prices, Coupons, Promotion Codes, or Shipping Rates in a single purchase, then
they must all support the customer’s local currency, and they must all have the
same default currency.

If you create Subscriptions directly, the multi-currency Prices don’t take
effect until you pass the `currency` parameter. If you don’t pass the `currency`
parameter, the Subscription always uses the default currency for the Price.

## Multiple prices

Products can use multiple prices to define different pricing options. The
product description is shared between prices and appears the same on the
customer’s receipt and invoice—only the pricing differs.

As Togethere’s product matures, they begin offering the same product at
different price points. Specifically, certain customers are willing to pay for
discounted up-front quarterly and yearly subscriptions. Togethere creates a
quarterly 57 USD option:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Standard Quarterly" \
 -d product={{PRODUCT_ID}} \
 -d unit_amount=5700 \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d "recurring[interval_count]"=3 \
 -d "recurring[usage_type]"=licensed
```

And a yearly 220 USD option:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Standard Yearly" \
 -d product={{PRODUCT_ID}} \
 -d unit_amount=22000 \
 -d currency=usd \
 -d "recurring[interval]"=year \
 -d "recurring[usage_type]"=licensed
```

## Display pricing information

After creating your pricing structures, you can embed a [pricing
table](https://docs.stripe.com/payments/checkout/pricing-table) on your website
to display pricing information to your customers. When customers choose a
subscription option, they’re taken directly to checkout. Configure, customize,
and update directly in the
[Dashboard](https://dashboard.stripe.com/test/pricing-tables) without writing
any code.

## Links

- [Pricing models](https://docs.stripe.com/products-prices/pricing-models)
- [Product](https://docs.stripe.com/api/products)
- [Price](https://docs.stripe.com/api/prices)
- [prices
guide](https://docs.stripe.com/products-prices/manage-prices#create-product)
- [Product catalog](https://dashboard.stripe.com/products)
- [customer portal](https://docs.stripe.com/customer-management)
- [quotes](https://docs.stripe.com/quotes)
- [create a Checkout
session](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)
- [create a
Customer](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#create-customer)
-
[advanced](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models)
- [usage](https://docs.stripe.com/api/billing/meter-event)
- [create a price](https://docs.stripe.com/api#create_price)
-
[volume-based](https://docs.stripe.com/products-prices/pricing-models#volume-based-pricing)
-
[graduated](https://docs.stripe.com/products-prices/pricing-models#graduated-pricing)
- [invoice](https://docs.stripe.com/api/invoices)
- [Let customers decide what to
pay](https://docs.stripe.com/payments/checkout/pay-what-you-want)
- [Payment Links](https://docs.stripe.com/payment-links/api)
-
[price_data](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data)
-
[price.id](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-price-id)
- [Checkout](https://docs.stripe.com/api/checkout/sessions)
- [Invoice Items](https://docs.stripe.com/api/invoiceitems)
- [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules)
- [API](https://docs.stripe.com/api/prices/create)
- [Product catalog](https://dashboard.stripe.com/test/products)
- [Coupons](https://docs.stripe.com/billing/subscriptions/coupons#coupons)
- [Promotion
Codes](https://docs.stripe.com/billing/subscriptions/coupons#promotion-codes)
- [Shipping
Rates](https://docs.stripe.com/payments/during-payment/charge-shipping)
-
[currency_options.<currency>.unit_amount](https://docs.stripe.com/api/prices/object#price_object-currency_options-unit_amount)
- [expand](https://docs.stripe.com/api/expanding_objects)
-
[currency](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-currency)
- [manual currency
prices](https://docs.stripe.com/payments/checkout/manual-currency-prices)
- [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
- [Dashboard](https://dashboard.stripe.com/test/pricing-tables)