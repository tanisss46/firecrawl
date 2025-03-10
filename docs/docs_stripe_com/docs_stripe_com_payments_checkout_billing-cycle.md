# Set the billing cycle date

## Set a subscription's billing cycle anchor to a fixed date.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can explicitly set a subscription’s [billing cycle
anchor](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-billing_cycle_anchor)
to a fixed date (for example, the 1st of the next month) when creating a
Checkout Session. The billing cycle anchor determines the first full invoice
date, when customers are billed the full subscription amount. The billing cycle
anchor and the recurring interval of its
[price](https://docs.stripe.com/products-prices/overview) also determine a
subscription’s future billing dates. For example, a monthly subscription created
on May 15 with an anchor at June 1 is billed on May 15, then always on the 1st
of the month.

For the initial billing period up until the first full invoice date, you can
customize how to handle
[prorations](https://docs.stripe.com/billing/subscriptions/prorations) with the
[proration_behavior](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-proration_behavior)
parameter. By default, `proration_behavior` is set to `create_prorations`, and
customers receive a prorated [invoice](https://docs.stripe.com/api/invoices). If
`proration_behavior` is `none`, customers receive the initial period up to the
first full invoice date for free.

## Create a Checkout Session with a billing cycle anchor

To configure a billing cycle anchor, set the
`subscription_data.billing_cycle_anchor` parameter when you create a Checkout
Session in `subscription` mode. The anchor must be a future UNIX timestamp
before the next natural subscription billing date.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=subscription \
--data-urlencode
success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
 -d "subscription_data[billing_cycle_anchor]"=1611008505
```

If the billing cycle anchor is during a session’s active period and a customer
attempts payment after it has passed, Checkout displays and charges for the full
period starting with the billing cycle anchor instead of the prorated period
before the billing cycle anchor.

## Disable prorations

To disable prorations, set the `subscription_data.proration_behavior` parameter
to `none` when creating a Checkout Session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=subscription \
--data-urlencode
success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
 -d "subscription_data[billing_cycle_anchor]"=1611008505 \
 -d "subscription_data[proration_behavior]"=none
```

Similar to a free trial, the initial period up to the billing cycle anchor is
free. Unlike a trial, no 0 USD invoice is generated. Customers receive an
invoice with the full subscription amount on the billing cycle anchor date.

In the Checkout Session response object, amounts attached to the [line
items](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-line_items)
and [total
details](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-total_details)
are always 0 when prorations are disabled. Additionally, the [payment
status](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_status)
of the Session is set to `no_payment_required` to reflect that payment is
delayed to a future date.

## Current limitations

- You can’t use trials in Checkout Sessions with a billing cycle anchor.
- One-time prices can’t be used in Checkout Sessions when `proration_behavior`
is `none`.
- You can’t apply [amount_off
coupons](https://docs.stripe.com/api/coupons/create#create_coupon-amount_off) to
Checkout Sessions with a default `proration_behavior` of `create_prorations`.

## See also

- [Prorations](https://docs.stripe.com/billing/subscriptions/prorations)

## Links

- [billing cycle
anchor](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-billing_cycle_anchor)
- [price](https://docs.stripe.com/products-prices/overview)
- [prorations](https://docs.stripe.com/billing/subscriptions/prorations)
-
[proration_behavior](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-proration_behavior)
- [invoice](https://docs.stripe.com/api/invoices)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [line
items](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-line_items)
- [total
details](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-total_details)
- [payment
status](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_status)
- [amount_off
coupons](https://docs.stripe.com/api/coupons/create#create_coupon-amount_off)