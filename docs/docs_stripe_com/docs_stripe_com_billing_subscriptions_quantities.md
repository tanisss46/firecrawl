# Setting subscription quantities

## Vary the cost of a subscription by subscribing a customer to multiple quantities of a product.

By default, each subscription is for one product, but Stripe allows you to
subscribe a customer to multiple quantities of an item. For example, say you run
a hosting company and your customers host sites through it at a cost of 9.99 USD
per site, per month. Most customers host a single site, while some host many.
You could create prices for one site (9.99 USD), two sites (19.98 USD), and so
forth, but a better approach is to subscribe customers to a quantity with a 9.99
USD unit price.

Subscriptions have two kinds of usage-based billing: metered billing, and
per-seat licensing. You can enable these billing models by setting the value of
the `recurring[usage_type]` attribute when creating a price. You can only
specify a quantity when creating a subscription with a `recurring[usage_type]`
of `licensed`. If you want to have granular billing for usage that fluctuates
within a billing interval, consider using [metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
instead of quantities.

## Setting multiple quantities

To set the quantity on a subscription, provide a `quantity` value when
[creating](https://docs.stripe.com/api#create_subscription) or
[updating](https://docs.stripe.com/api#update_subscription) the subscription:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_4fdAW5ftNQow1a \
 -d "items[0][price]"=price_CBb6IXqvTLXp3f \
 -d "items[0][quantity]"=5
```

You still bill multiple quantities using one
[invoice](https://docs.stripe.com/api/invoices), and you
[prorate](https://docs.stripe.com/billing/subscriptions/prorations) them when
the subscription changes. This includes when you change subscription quantities.

## Charging different amounts based on quantity

In some cases, you might want to adjust the cost per seat based on the number of
seats in a subscription. For example, you could offer volume licensing discounts
for subscriptions that exceed certain quantity thresholds. You can use
[tiers](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
to adjust per-seat pricing.

## Quantity transformation

When you bill your customers, you might want to track usage at a different
granularity than you bill. For example, consider a productivity software suite
that charges 10 USD for every 5 users (or portion thereof) using the product.
Without quantity transformation, they would need to increase the `quantity` of
the subscription item by 1 for every 5 users.

Number of UsersSubscription Item Quantity Reported to StripeTotal1110 USD3110
USD5110 USD6220 USD7220 USD
With the `transform_quantity` parameter, you can instruct Stripe to transform
the quantity before applying the per unit cost. The following subscription
allows you to naturally report the current number of users as the subscription
item `quantity`—Stripe’s billing system divides the quantity by 5 and rounds up
before calculating by the unit cost.

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Standard Cost Per 5 Users" \
 -d "transform_quantity[divide_by]"=5 \
 -d "transform_quantity[round]"=up \
 -d unit_amount=1000 \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d "recurring[usage_type]"=licensed \
 -d product={{PRODUCTIVITY_SUITE_ID}}
```

Currently, the only available transformation is division, using the `divide_by`
parameter in conjunction with the `round` parameter.

You can only use `transform_quantity` with `billing_scheme=per_unit`—it’s
incompatible with tiered pricing.

### Rounding

The previous example showed a subscription that charges for every 5 users
rounding up, that is, 6 divided by 5 results in a quantity of 2. For use cases
where you don’t want to charge for a portion of usage, like charging for every
full gigabyte of usage of a broadband internet service, you can also pass `down`
as the value of `round`.

### Metered usage

You can also apply `transform_quantity` in conjunction with metered billing.
This transformation applies to prices with `recurring[usage_type]=metered` at
the end of a billing period in the same way it applies to `quantity` for prices
with `recurring[usage_type]=licensed`.

A marketing email service that creates a metered price to charge 0.10 USD for
every full 1000 emails sent might look something like this:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Metered Emails" \
 -d "transform_quantity[divide_by]"=1000 \
 -d "transform_quantity[round]"=down \
 -d unit_amount=10 \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d "recurring[usage_type]"=metered \
 -d product={{MARKETING_EMAILS_ID}}
```

With this subscription, usage can be reported per email and you can bill the
customer 0.10 USD for every 1000 emails they send.

## See also

- [Change subscriptions](https://docs.stripe.com/billing/subscriptions/change)
- [Multiple
subscriptions](https://docs.stripe.com/billing/subscriptions/multiple-products)
- [Subscriptions API](https://docs.stripe.com/api#subscriptions)

## Links

- [metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [creating](https://docs.stripe.com/api#create_subscription)
- [updating](https://docs.stripe.com/api#update_subscription)
- [invoice](https://docs.stripe.com/api/invoices)
- [prorate](https://docs.stripe.com/billing/subscriptions/prorations)
- [tiers](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
- [Change subscriptions](https://docs.stripe.com/billing/subscriptions/change)
- [Multiple
subscriptions](https://docs.stripe.com/billing/subscriptions/multiple-products)
- [Subscriptions API](https://docs.stripe.com/api#subscriptions)