# No-cost orders

## Accept orders for no-cost line items or apply 100% off discounts for one-time payments.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can process no-cost orders for one-time payments with [no-cost line
items](https://docs.stripe.com/payments/checkout/no-cost-orders#no-cost-line-items)
or discounts for 100% off with [coupons and customer-facing promotion
codes](https://docs.stripe.com/payments/checkout/no-cost-orders#full-cost-discounts).

#### Note

You must be on API version
[2023-08-16](https://docs.stripe.com/upgrades#2023-08-16) or later to process
no-cost orders using the Checkout Sessions API.

## Create a Checkout Session with no-cost line items

Create a [Price](https://docs.stripe.com/api/prices) with a
[unit_amount](https://docs.stripe.com/api/prices/object#price_object-unit_amount)
of 0, and pass it into the [line
items](https://docs.stripe.com/api/checkout/sessions/line_items) array of the
Checkout Session. See [Products and
prices](https://docs.stripe.com/invoicing/products-prices) for more information
on creating prices.

You can also use the
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
parameter of the `line_items` array to pass in a free price.

If the total amount is 0, Checkout doesn’t collect a payment method from the
customer.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][unit_amount]"=0 \
 -d "line_items[0][price_data][product_data][name]"="Free t-shirt" \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

If the `customer` property isn’t set, the Checkout Session automatically creates
a new Customer object. This means [guest
customers](https://docs.stripe.com/payments/checkout/guest-customers) aren’t
supported.

## Create a discount

Alternatively, create a coupon and a promotion code to allow customers to
complete orders for free.

### Create a coupon

Create a [Coupon](https://docs.stripe.com/api/coupons) that makes your Checkout
Session free. For example, you can create a 100% off coupon.

```
curl https://api.stripe.com/v1/coupons \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d percent_off=100 \
 -d duration=once
```

To create a session with an applied discount, pass the [coupon
ID](https://docs.stripe.com/api/coupons/object#coupon_object-id) in the `coupon`
parameter of the
[discounts](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-discounts)
array.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][quantity]"=1 \
 -d "discounts[0][coupon]"={{COUPON_ID}} \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

You can also create a free Checkout Session by applying a coupon for an amount
equal to or exceeding the Checkout Session total.

### Create a promotion code

Promotion codes are customer-facing codes created on top of coupons. You can
share these codes with customers who can enter them into Checkout to apply a
discount. Create a promotion code from a 100% off coupon to allow customers to
create orders for free.

```
curl https://api.stripe.com/v1/promotion_codes \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d coupon={{COUPON_ID}} \
 -d code=FREECODE
```

Enable user-redeemable promotion codes using the
[allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes)
parameter in a Checkout Session. This enables a field in Checkout to allow users
to enter promotion codes.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d allow_promotion_codes=true \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

Customers can also check out for free if they apply a promotion code for an
amount equal to or exceeding the Checkout Session total. For more ways to apply
discounts, see [Add
discounts](https://docs.stripe.com/payments/checkout/discounts).

## Handle completed orders

After the Checkout Session completes, you can make a request for the finalized
[line items](https://docs.stripe.com/api/checkout/sessions/line_items) and their
quantities. If your customer removes a line item, it also removes it from the
line items response. See the [Fulfillment
guide](https://docs.stripe.com/checkout/fulfillment) to learn how to create an
event handler to handle completed Checkout Sessions.

#### Common mistake

To fulfill no-cost orders, make sure to handle the `checkout.session.completed`
event rather than
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) events.
Completed Checkout Sessions that are free won’t have an associated
[PaymentIntent](https://docs.stripe.com/payments/payment-intents).

You can see your completed no-cost orders in the
[Dashboard](https://dashboard.stripe.com/no-cost-orders). The no-cost orders tab
only appears if you have at least one completed no-cost order.

[OptionalPayment links and pricing
tables](https://docs.stripe.com/payments/checkout/no-cost-orders#payment-links-and-pricing-tables)

## Links

- [2023-08-16](https://docs.stripe.com/upgrades#2023-08-16)
- [Price](https://docs.stripe.com/api/prices)
-
[unit_amount](https://docs.stripe.com/api/prices/object#price_object-unit_amount)
- [line items](https://docs.stripe.com/api/checkout/sessions/line_items)
- [Products and prices](https://docs.stripe.com/invoicing/products-prices)
-
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [guest customers](https://docs.stripe.com/payments/checkout/guest-customers)
- [Coupon](https://docs.stripe.com/api/coupons)
- [coupon ID](https://docs.stripe.com/api/coupons/object#coupon_object-id)
-
[discounts](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-discounts)
-
[allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes)
- [Add discounts](https://docs.stripe.com/payments/checkout/discounts)
- [Fulfillment guide](https://docs.stripe.com/checkout/fulfillment)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Dashboard](https://dashboard.stripe.com/no-cost-orders)