# Designing an integration

## Learn what choices you need to make to integrate subscriptions into your business.

Before you start building your
[subscription](https://docs.stripe.com/billing/subscriptions/creating)
integration, you need to choose the right integration path, especially if you’re
not writing the code yourself and need to collaborate with others. Use this
guide to help you decide on the best way to build your integration, and follow
the links to in-depth, step-by-step guides.

This guide is for users who aren’t necessarily writing code, but want to learn
about the high-level subscription integration process so that they can create
plans and organize resources.

If you already know how you’re going to build your integration, or if you want
to start coding right away, see our [integration
builder](https://docs.stripe.com/billing/quickstart).

[Subscription
models](https://docs.stripe.com/billing/subscriptions/designing-integration#subscription-models)
You need to understand the available subscription models to help you make later
choices, such as which pricing model and payment form to use. First, consider
your business model:

- If you want customers to pay, then provision access to your service, click the
**pay up front** tab below to learn more.
- If you want to collect payment details, then offer customers a free trial
period before billing them, click the **free trial** tab below to learn more.
- If you want to provide users access to your service without asking them for
any payment information (a *freemium* model), click the **freemium** tab below
to learn more.
Pay up frontFree trialFreemium

![Pay-up-front subscription
model](https://b.stripecdn.com/docs-statics-srv/assets/sub_model_pay_up_front.6b48054ef005d5ea359d56a3a07b6085.svg)

Pay-up-front model

In the pay-up-front model, you collect payment details and charge customers
before provisioning access to your service. After the initial charge, you
continue to charge customers the same fixed price for the same service at
regular intervals. In this model, you use the Dashboard or [Subscriptions
API](https://docs.stripe.com/api/subscriptions) manage customer subscriptions.
If you want to allow customers to modify their subscriptions directly, you need
to integrate the [customer portal](https://docs.stripe.com/customer-management).

For example, a photo hosting company that offers basic and premium service
levels and charges customers on a monthly basis might have this setup:

- One product for the basic option
- One product for the premium option
- One price for the basic option (15 USD per month)
- One price for the premium option (25 USD per month)

A typical flow for this model would look like the following:

- The customer chooses their plan (basic or premium).
- You collect payment information.
- You provision access to your service. You know when to do this by monitoring
[webhook events](https://docs.stripe.com/webhooks).
- You continue to provision access for customers throughout the lifecycle of the
subscription. Check regularly to make sure you’re not providing access if a
customer’s payment has failed.

See the [integration
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions) to
learn how to build an integration with a low-code approach that uses a prebuilt
and hosted page from [Stripe
Checkout](https://docs.stripe.com/payments/checkout) or a custom version with
[Stripe Elements](https://docs.stripe.com/payments/elements).

[Metered
billing](https://docs.stripe.com/billing/subscriptions/designing-integration#metered-billing)
If you need to meter usage, see [metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing).
You need to do this when you [create a
price](https://docs.stripe.com/products-prices/manage-prices#create-price).

[Collect payment
information](https://docs.stripe.com/billing/subscriptions/designing-integration#collect-payment-info)
If you don’t want to write a lot of code, use
[Checkout](https://docs.stripe.com/payments/checkout), Stripe’s prebuilt, hosted
payment page. See the [subscriptions with
Checkout](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)
integration guide to get started.

If you want a more customized payment form that you can embed into your existing
website, use [Elements](https://docs.stripe.com/payments/elements), a set of
prebuilt UI elements that’s part of
[Stripe.js](https://docs.stripe.com/payments/elements).

[Display pricing
information](https://docs.stripe.com/billing/subscriptions/designing-integration#pricing-table)
Embed a [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
on your website to show customers pricing information for subscriptions. When
customers choose a subscription option, they’re taken directly to checkout.
Configure, customize, and update directly in the
[Dashboard](https://dashboard.stripe.com/test/pricing-tables) without writing
any code.

[Modify
subscriptions](https://docs.stripe.com/billing/subscriptions/designing-integration#modify-subs)
If you’re collecting payment information with Checkout, you can use the
[customer portal](https://docs.stripe.com/customer-management) to allow
customers to directly update their subscription details, like payment method and
frequency. See the [integration
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)
for detailed instructions on setting this up. (Before integrating, you should
also be aware of the [limitations](https://docs.stripe.com/customer-management)
of the portal.)

If you’re integrating with Elements, you can add a form on the frontend to
collect details about the plan they want to change (such as the price ID and
their customer information) and send that to an endpoint on the backend. For
more details and sample code, see the section about [letting customers change
their
plans](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#change-price)
in the Elements quickstart.

[Pricing
models](https://docs.stripe.com/billing/subscriptions/designing-integration#pricing-models)
If you’re providing the same good every month and don’t expect that to change,
use a simple fixed-price model. If the price varies depending on the number of
users or units, you can use volume-based or tier-based prices. For a complete
list of available models and a detailed description of each one, see [examples
of pricing models](https://docs.stripe.com/products-prices/pricing-models).

[Set up
webhooks](https://docs.stripe.com/billing/subscriptions/designing-integration#webhooks)
Set up [webhook
endpoints](https://docs.stripe.com/billing/subscriptions/webhooks) to receive
notifications about subscription-related events. For example, when you see the
`invoice.paid=true` notification, you can safely provision access to your
service. See [the subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
for more information about [webhook](https://docs.stripe.com/webhooks) events.
See a complete list of [subscription-related
events](https://docs.stripe.com/billing/subscriptions/overview#subscription-events).
To learn about managing access to your product’s feature, see
[Entitlements](https://docs.stripe.com/billing/entitlements).

[OptionalOther
considerations](https://docs.stripe.com/billing/subscriptions/designing-integration#other-considerations)

## Links

- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [integration builder](https://docs.stripe.com/billing/quickstart)
- [Subscriptions API](https://docs.stripe.com/api/subscriptions)
- [customer portal](https://docs.stripe.com/customer-management)
-
[checkout.session.completed](https://docs.stripe.com/billing/subscriptions/build-subscriptions#provision-and-monitor)
- [Elements](https://docs.stripe.com/payments/elements)
-
[invoice.paid](https://docs.stripe.com/billing/subscriptions/build-subscriptions#provision-access)
- [webhook events](https://docs.stripe.com/webhooks)
- [integration
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [create a
price](https://docs.stripe.com/products-prices/manage-prices#create-price)
- [subscriptions with
Checkout](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted)
- [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
- [Dashboard](https://dashboard.stripe.com/test/pricing-tables)
- [letting customers change their
plans](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#change-price)
- [examples of pricing
models](https://docs.stripe.com/products-prices/pricing-models)
- [webhook endpoints](https://docs.stripe.com/billing/subscriptions/webhooks)
- [the subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
- [subscription-related
events](https://docs.stripe.com/billing/subscriptions/overview#subscription-events)
- [Entitlements](https://docs.stripe.com/billing/entitlements)