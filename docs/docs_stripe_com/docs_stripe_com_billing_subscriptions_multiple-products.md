# Subscriptions with multiple products

## Create subscriptions with multiple products, all billed in a single invoice.

If you offer multiple products or want to charge different amounts for the same
product, you can attach multiple products to a subscription. This generates a
single [invoice](https://docs.stripe.com/api/invoices) each billing period that
combines every price. Only a single payment for that invoice is required,
reducing your costs and the number of charges your customer sees.

## Creating multiple-product subscriptions

Create multiple-product subscriptions on a customer using the `items` parameter.
Provide the `price` and, optionally, a `quantity` (when using a value other than
1), for each product:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"=price_CBXbz9i7AIOTzr \
 -d "items[1][price]"=price_IFuCu48Snc02bc \
 -d "items[1][quantity]"=2
```

The response includes a list of all the subscription items, prices, and
quantities:

```
{
 "id": "sub_CZEpS1Zt9QLxdo",
 "object": "subscription",
 ...
 "items": {
 "object": "list",
 "data": [
 {
 "id": "si_H1yPnAVzP9vDRW",
 "object": "subscription_item",
 "billing_thresholds": null,
 "created": 1585939321,
 "metadata": {
 },
 "price": {
 "id": "price_H1c8v1liEvrfcd",
 "object": "price",
 "active": true,
 "billing_scheme": "per_unit",
 "created": 1585856460,
 "currency": "usd",
 "livemode": false,
 "lookup_key": null,
 "metadata": {
 },
 "nickname": null,
 "product": "prod_H1c7exjJHbC4sr",
 "recurring": {
 "aggregate_usage": null,
 "interval": "month",
 "interval_count": 1,
 "trial_period_days": null,
 "usage_type": "licensed"
 },
 "tiers": null,
 "tiers_mode": null,
 "transform_quantity": null,
 "type": "recurring",
 "unit_amount": 1000,
 "unit_amount_decimal": "1000"
 },
 "quantity": 1,
 "subscription": "sub_H1yPRslJXa4TUt",
 "tax_rates": [
 ]
```

See all 89 lines
## Billing periods with multiple prices

Conventional prices that charge a fixed amount on an interval are billed at the
start of each [billing
cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle). With each
invoice, the customer effectively pays for the next interval of service. With
[metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing),
the amount paid by the customer varies based on consumption during the billing
cycle, so the customer pays for their usage at the end.

When a subscription combines a fixed rate with metered billing, metered usage
from the previous billing cycle is charged alongside the fixed rate for the new
billing cycle at the start of each interval. The metered billing and fixed rate
are combined in a single invoice.

## Restrictions

Since using multiple products with a subscription results in a single invoice
and payment, all of the prices for those products must use the same currency and
have the same billing interval. You are also limited to 20 products in a single
subscription.

## Discounts, taxes, and trial periods

When using multiple products, you can also create discounts, charge taxes, and
use trial periods as you would with a single-product subscription. Provide these
as top-level arguments to the create or update subscription call, as they apply
to the subscription at large:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d coupon=free-period \
 -d "default_tax_rates[0]"=txr_1EO66sClCIKljWvs98IiVfHW \
 -d trial_end=1610403705 \
 -d "items[0][price]"=price_CBXbz9i7AIOTzr \
 -d "items[1][price]"=price_IFuCu48Snc02bc \
 -d "items[1][quantity]"=2
```

When you create a subscription by passing prices into the `items` attribute, it
will ignore any trial period that is specified on the individual prices. The
trial period is only respected if you create a subscription with a single price
using the legacy plan attribute.

## Multiple subscriptions for a customer

You can simultaneously create multiple subscriptions for a single customer. This
capability is useful when you want to make it possible for your customers to
subscribe to multiple products with separate intervals. Each subscription has
its own separate billing cycle, invoice, and charge—even if the underlying
prices have the same billing interval.

Create multiple subscriptions on a customer by using the same [create
subscription](https://docs.stripe.com/api#create_subscription) code:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_4fdAW5ftNQow1a \
 -d "items[0][price]"=price_CZB2krKbBDOkTS
```

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_4fdAW5ftNQow1a \
 -d "items[0][price]"=price_CZB1AX3KOacNJw
```

A customer can be subscribed to multiple products or even to a single product
multiple times. Each subscription has a unique ID and its state is handled
independently from the customer’s other subscriptions. Each subscription also
has its own independent billing cycle, based on the [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle) of the
subscription.

When a customer has multiple subscriptions, the `Customer` object’s
`subscriptions` property provides a list of every subscription:

```
{
 "id": "cus_4fdAW5ftNQow1a",
 "object": "customer",
 "subscriptions": {
 "object": "list",
 "data": [
 {
 "id": "sub_9RRl3XywPg2P5H",
 "object": "subscription",
 ...
 "price": {
 "id": "price_CZB2krKbBDOkTS",
 "object": "price",
 "amount": 2995,
 ...
 }
 },
 {
 "id": "sub_9RRlIq2t9obFLI",
 "object": "subscription",
 ...
 "price": {
 "id": "price_CZB1AX3KOacNJw",
 "object": "price",
 "amount": 1295,
 ...
 }
 }
 ]
 ...
 }
 ...
}
```

## See also

- [Setting quantities](https://docs.stripe.com/billing/subscriptions/quantities)
- [Use trial periods](https://docs.stripe.com/billing/subscriptions/trials)
- [Subscriptions API](https://docs.stripe.com/api#create_subscription)

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [billing cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [metered
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [multiple
subscriptions](https://docs.stripe.com/billing/subscriptions/multiple-products#multiple-subscriptions-for-a-customer)
- [create subscription](https://docs.stripe.com/api#create_subscription)
- [multiple
quantities](https://docs.stripe.com/billing/subscriptions/quantities)
- [Use trial periods](https://docs.stripe.com/billing/subscriptions/trials)