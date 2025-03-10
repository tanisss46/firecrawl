# Subscriptions

## Create subscriptions for your customers.

The Checkout Sessions API supports setting up a variety of pricing models,
including flat-rate subscriptions, usage-based pricing, tiered pricing, and
more.

- First, create your [pricing
model](https://docs.stripe.com/products-prices/pricing-models) using the
[Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) APIs.
- Pass the Price in to
[line_items.price](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price)
when you create the Checkout Session.
- Make sure that
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
is set to `subscription`.
[Configure free trialsDelay payments on subscriptions using free trial
periods.](https://docs.stripe.com/payments/checkout/free-trials)[Limit customers
to one subscriptionDirect customers to manage their subscription when they
already have
one.](https://docs.stripe.com/payments/checkout/limit-subscriptions)[Set the
billing cycle dateUse Stripe Checkout to set a billing cycle date for
subscriptions.](https://docs.stripe.com/payments/checkout/billing-cycle)

## Links

- [pricing model](https://docs.stripe.com/products-prices/pricing-models)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
-
[line_items.price](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
- [Configure free trialsDelay payments on subscriptions using free trial
periods.](https://docs.stripe.com/payments/checkout/free-trials)
- [Limit customers to one subscriptionDirect customers to manage their
subscription when they already have
one.](https://docs.stripe.com/payments/checkout/limit-subscriptions)
- [Set the billing cycle dateUse Stripe Checkout to set a billing cycle date for
subscriptions.](https://docs.stripe.com/payments/checkout/billing-cycle)