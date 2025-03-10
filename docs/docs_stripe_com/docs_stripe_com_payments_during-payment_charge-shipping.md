# Charge for shipping

## Create different shipping rates for your customers.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Shipping rates let you display various shipping options—like standard, express,
and overnight—with more accurate delivery estimates. Charge your customer for
shipping using different Stripe products. Before you create a shipping rate,
learn how to [collect billing and shipping
addresses](https://docs.stripe.com/payments/collect-addresses).

[Create a shipping
rateDashboardServer-side](https://docs.stripe.com/payments/during-payment/charge-shipping#create-shipping-rate)DashboardAPI
To add a [shipping rate](https://dashboard.stripe.com/test/shipping-rates) using
the Dashboard:

- Click **Create shipping rate**.
- Enter an amount, a description, and an optional delivery estimate.
- Click **Save**, and copy the shipping rate ID (`shr_123456`).

!

Enter your shipping rate details

[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/during-payment/charge-shipping#create-checkout-session)
To create a Checkout Session that includes your shipping rate, pass in the
generated shipping rate ID to the
[shipping_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_options)
parameter. If you want to create the shipping rate at the same time as a
Checkout Session, use the `shipping_rate_data` parameter with
`shipping_options`. Only Checkout Sessions in [payment
mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
support shipping options.

The following code sample adds two shipping options to the Checkout Session:

- Free shipping, with an estimated delivery of 5-7 business days.
- Next day air, at a cost of 15.00 USD, with an estimated delivery of exactly 1
business day.

In this example, the first option in the `shipping_options` array is
pre-selected for the customer on the checkout page. However, customers can
choose either option.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "shipping_address_collection[allowed_countries][0]"=US \
 -d "shipping_address_collection[allowed_countries][1]"=CA \
 -d "shipping_options[0][shipping_rate_data][type]"=fixed_amount \
 -d "shipping_options[0][shipping_rate_data][fixed_amount][amount]"=0 \
 -d "shipping_options[0][shipping_rate_data][fixed_amount][currency]"=usd \
 -d "shipping_options[0][shipping_rate_data][display_name]"="Free shipping" \
-d
"shipping_options[0][shipping_rate_data][delivery_estimate][minimum][unit]"=business_day
\
-d
"shipping_options[0][shipping_rate_data][delivery_estimate][minimum][value]"=5 \
-d
"shipping_options[0][shipping_rate_data][delivery_estimate][maximum][unit]"=business_day
\
-d
"shipping_options[0][shipping_rate_data][delivery_estimate][maximum][value]"=7 \
 -d "shipping_options[1][shipping_rate_data][type]"=fixed_amount \
 -d "shipping_options[1][shipping_rate_data][fixed_amount][amount]"=1500 \
 -d "shipping_options[1][shipping_rate_data][fixed_amount][currency]"=usd \
 -d "shipping_options[1][shipping_rate_data][display_name]"="Next day air" \
-d
"shipping_options[1][shipping_rate_data][delivery_estimate][minimum][unit]"=business_day
\
-d
"shipping_options[1][shipping_rate_data][delivery_estimate][minimum][value]"=1 \
-d
"shipping_options[1][shipping_rate_data][delivery_estimate][maximum][unit]"=business_day
\
-d
"shipping_options[1][shipping_rate_data][delivery_estimate][maximum][value]"=1 \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success"
```

If successful, the shipping selector appears on your checkout page:

![The shipping selector on the checkout
page](https://b.stripecdn.com/docs-statics-srv/assets/example-checkout-session.5807984bdc0a25ddb53aab00768dd079.jpg)

The shipping selector on the checkout page

[OptionalHandle completed
transactions](https://docs.stripe.com/payments/during-payment/charge-shipping#handling-transactions)[OptionalDefine
a delivery
estimate](https://docs.stripe.com/payments/during-payment/charge-shipping#delivery-estimates)[OptionalCharge
tax for
shipping](https://docs.stripe.com/payments/during-payment/charge-shipping#shipping-rate-with-tax-code)

## Links

- [collect billing and shipping
addresses](https://docs.stripe.com/payments/collect-addresses)
- [shipping rate](https://dashboard.stripe.com/test/shipping-rates)
-
[shipping_options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_options)
- [payment
mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
- [https://example.com/success](https://example.com/success)