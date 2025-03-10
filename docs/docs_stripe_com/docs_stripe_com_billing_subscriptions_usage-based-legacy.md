# Usage-based billingLegacy

## Charge customers based on how much they use your product or service.

#### Note

We’ve updated the way usage-based billing works. See the [updated usage-based
billing docs](https://docs.stripe.com/billing/subscriptions/usage-based).

Learn how to
[migrate](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide).

## Getting started

[Usage-based pricing modelLearn how to model usage-based pricing on
Stripe.](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/pricing-models)[Record
usageRecord the usage of your users and report it to
Stripe.](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/recording-usage)[Usage-based
billing overviewUnderstand the major pieces of a usage-based billing
integration.](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#sample-integration)
## Usage-based billing lifecycle

Here’s what the lifecycle of a usage-based billing looks like.

This diagram illustrates what happens after you’ve implemented a customer
experience.

Customer

Typographic

Stripe

Select plan

Create subscription with `payment_behavior` set to
[default_incomplete](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)

Return subscription object

Present new subscription

Provision access

Notify customer that they have access

Use service

Create [usage records](https://docs.stripe.com/api/usage_records)

Report usage to Stripe

Send invoice for amount of service used

Usage-based billing
## Sample integration

This example walks through the implementation of a fictional font service called
Typographic.

## Create a product and pricing

Model your business on stripe with products and prices.

Create your [products](https://docs.stripe.com/api/products) and their pricing
options with the Stripe API or Dashboard. Typographic has three products, each
with two tiers:

- Standard- Tier one: 10 USD per month for 10,000 requests
- Tier two: An additional $0.10 USD for each request after 10,000
- Growth- Tier one: 25 USD per month for 10,000 requests
- Tier two: An additional $0.10 USD for each request after 10,000
- Enterprise- Tier one: 75 USD per month for 10,000 requests
- Tier two: An additional $0.0075 USD for each request after 10,000

To achieve this kind of pricing, you charge a flat fee and an additional amount
based on how much customers use. With [graduated
tiers](https://docs.stripe.com/products-prices/pricing-models#graduated-pricing),
customers initially pay the flat fee for the first 10,000 requests. If they make
more requests than that, they reach tier two and start paying for each
additional request. You could also charge solely based on usage without the flat
fee.

During each billing period, you create [usage
records](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/recording-usage)
for each customer and then Stripe adds them up to determine how much to bill
for. This process is explained in a subsequent step but understanding the
default behavior might impact how you create prices.

DashboardAPI
To create a metered usage pricing model on Stripe through the Dashboard:

First, create the `Standard` product. To learn about all the options for
creating a product, see the [prices
guide](https://docs.stripe.com/products-prices/manage-prices#create-product).

- Go to the **Products** [tab](https://dashboard.stripe.com/products).
- Click **+ Add product**.
- Enter the **Name** of the product: `Standard`, in this case.
- *(Optional)* Add a **Description**. The description appears at checkout, on
the [customer portal](https://docs.stripe.com/customer-management), and in
[quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the `Standard` product. Select **Graduated
pricing** for the **Pricing model**, then select **Recurring**.

Create two graduated pricing tiers:

First unitLast unitPer unitFlat feeFor the first010,0000.00 USD10.00 USDFor the
next10,001∞0.10 USD0.00 USD
Then, select **Monthly** for the **Billing period** and check **Usage is
metered**.

Repeat the steps for the `Growth` and `Enterprise` products, filling in the
appropriate values as necessary.

Read the docs to learn more about different [pricing
models](https://docs.stripe.com/products-prices/pricing-models).

## Sign up customers

To let your customers sign up for your services, you need to present a payment
form on your website. Use [Stripe
Checkout](https://docs.stripe.com/checkout/quickstart) to embed the form on your
site or redirect customers to a Stripe-hosted form. When a customer selects a
recurring product and enters their billing information in the Payment Link,
Stripe creates two records:

- [Customer](https://docs.stripe.com/api/customers/object)
- [Subscription](https://docs.stripe.com/api/subscriptions/object) These records
are both stored within Stripe.

Stripe offers other options for setting up your payment form:

- [Pricing tables](https://docs.stripe.com/payments/checkout/pricing-table):
Create a pricing table from the Stripe Dashboard and embed it on your site. When
a customer selects a plan, they’re taken to your checkout page. Pricing tables
don’t support sub-cent pricing.
- [Web Elements](https://docs.stripe.com/payments/elements): Build custom
checkout flows to integrate with your site.

## Create a usage record

Throughout each billing period, you need to report usage to Stripe so that
customers are billed the correct amounts. You can maintain your own system for
recording customer usage and provide usage information for subscriptions to
Stripe.

Learn how to [record and report
usage](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/recording-usage).

## Test your integration

Test your integration to make sure it behaves as you expect. Learn more about
[testing subscriptions integrations](https://docs.stripe.com/billing/testing).

You can use test clocks to test different scenarios, including mock usage
records. When you make a usage reporting call, you need to sync the timestamp of
the test clock with the usage records. Make a note of the test clock timestamp
so that your usage records fall within the same time window. Learn more about
[test clocks](https://docs.stripe.com/billing/testing/test-clocks).

[OptionalFree
trials](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#trials)[OptionalCancellations](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#cancellations)[OptionalBilling
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#thresholds)[OptionalAggregate
metered
usage](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#aggregate-metered-usage)[OptionalTransforming
quantities](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#transforming-quantities)
## See also

- [Sample implementation
repository](https://github.com/stripe-samples/subscription-use-cases/tree/main/usage-based-subscriptions)
- [Usage-based billing video
tutorial](https://www.youtube.com/watch?v=v8cN4pEofy8)

## Links

- [updated usage-based billing
docs](https://docs.stripe.com/billing/subscriptions/usage-based)
-
[migrate](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide)
- [Usage-based pricing modelLearn how to model usage-based pricing on
Stripe.](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/pricing-models)
- [Record usageRecord the usage of your users and report it to
Stripe.](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/recording-usage)
- [Usage-based billing overviewUnderstand the major pieces of a usage-based
billing
integration.](https://docs.stripe.com/billing/subscriptions/usage-based-legacy#sample-integration)
-
[default_incomplete](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
- [usage records](https://docs.stripe.com/api/usage_records)
- [products](https://docs.stripe.com/api/products)
- [graduated
tiers](https://docs.stripe.com/products-prices/pricing-models#graduated-pricing)
- [prices
guide](https://docs.stripe.com/products-prices/manage-prices#create-product)
- [tab](https://dashboard.stripe.com/products)
- [customer portal](https://docs.stripe.com/customer-management)
- [quotes](https://docs.stripe.com/quotes)
- [pricing models](https://docs.stripe.com/products-prices/pricing-models)
- [Stripe Checkout](https://docs.stripe.com/checkout/quickstart)
- [Customer](https://docs.stripe.com/api/customers/object)
- [Subscription](https://docs.stripe.com/api/subscriptions/object)
- [Pricing tables](https://docs.stripe.com/payments/checkout/pricing-table)
- [Web Elements](https://docs.stripe.com/payments/elements)
- [testing subscriptions integrations](https://docs.stripe.com/billing/testing)
- [test clocks](https://docs.stripe.com/billing/testing/test-clocks)
- [Sample implementation
repository](https://github.com/stripe-samples/subscription-use-cases/tree/main/usage-based-subscriptions)
- [Usage-based billing video
tutorial](https://www.youtube.com/watch?v=v8cN4pEofy8)