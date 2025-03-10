# Manage limited inventory

## Prevent customers from holding inventory in carts by expiring Checkout Sessions.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
For some types of limited-inventory businesses, it’s necessary to prevent
customers from reserving items for a long time without completing the purchase.
For example, an event ticket seller wants to allow customers only a few minutes
to buy their selected tickets before cancelling the sale and making those
tickets available again. You can cancel a pending sale by expiring the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions).

Checkout supports both manual and timed session expiration. When a Checkout
Session expires, its [status
property](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-status)
changes to `expired`.

## Manual expiration

To immediately expire an open Checkout Session and cancel any pending purchase,
use the [expire](https://docs.stripe.com/api/checkout/sessions/expire) endpoint.

```
curl -X POST https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}}/expire \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Set an expiration time

When you create a Checkout Session, specify an expiration timestamp by setting
the
[expires_at](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-expires_at)
parameter. The value must be between 30 minutes and 24 hours after the current
time. If you don’t specify `expires_at`, the default value is 24 hours after the
current time.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d customer={{CUSTOMER_ID}} \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d success_url="https://example.com/success" \
 -d expires_at="{{NOW_PLUS_TWO_HOURS}}"
```

## Return items to your inventory

When a [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
expires, Stripe sends the `checkout.session.expired` event. Configure your
webhook endpoint to listen for this event so your webhook handler can return to
inventory any items reserved in the expired session. For more information, see
[Expire a Session](https://docs.stripe.com/api/checkout/sessions/expire).

## Links

- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [status
property](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-status)
- [expire](https://docs.stripe.com/api/checkout/sessions/expire)
-
[expires_at](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-expires_at)