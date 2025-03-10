# Set up a subscription with Cash App Pay

## Learn how to create and charge for a subscription with Cash App Pay.

Use this guide to set up a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[Cash App Pay](https://docs.stripe.com/payments/cash-app-pay) as a payment
method.

Setup Intents APISubscriptions APIStripe-hosted page
Create and confirm a subscription using two API calls. The [first API
call](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-setup-intent)
uses the [Setup Intents API](https://docs.stripe.com/api/setup_intents) to set
Cash App Pay as a payment method. The [second API
call](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-subscription)
sends customer, product, and payment method information to the [Subscriptions
API](https://docs.stripe.com/api/subscriptions) to create a Subscription and
confirm a payment in one call.

[Create a product and
priceDashboard](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-product-plan-code)
[Products](https://docs.stripe.com/api/products) represent the item or service
you’re selling. [Prices](https://docs.stripe.com/api/prices) define how much and
how frequently you charge for a product. This includes how much the product
costs, what currency you accept, and whether it’s a one-time or recurring
charge. If you only have a few products and prices, create and manage them in
the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15
USD monthly subscription. To model this:

- Navigate to the [Add a
product](https://dashboard.stripe.com/test/products/create) page.
- Enter a **Name** for the product.
- Enter **15** for the price.
- Select **USD** as the currency.
- Click **Save product**.

After you create the product and the price, record the price ID so you can use
it in subsequent steps. The pricing page displays the ID and it looks similar to
this: `price_G0FvDp6vZvdwRZ`.

[Create a
SetupIntentServer-side](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-setup-intent)
Create a [SetupIntent](https://docs.stripe.com/api/setup_intents) to save a
customer’s payment method for future payments. The `SetupIntent` tracks the
steps of this setup process.

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d confirm=true \
 --data-urlencode return_url="https://www.stripe.com" \
 -d usage=off_session \
 -d "payment_method_data[type]"=cashapp \
 -d "payment_method_types[]"=cashapp \
 -d "mandate_data[customer_acceptance][type]"=online \
 -d "mandate_data[customer_acceptance][online][ip_address]"="127.0.0.0" \
 -d "mandate_data[customer_acceptance][online][user_agent]"=device
```

The returned SetupIntent includes a [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret),
which the client side uses to securely complete the setup instead of passing the
entire SetupIntent object. You can use different approaches to [pass the client
secret to the client
side](https://docs.stripe.com/payments/payment-intents#passing-to-client). The
SetupIntent response also includes a payment method ID that you need to use in
the next step to confirm a PaymentIntent.

The SetupIntent response includes the status `requires_action`, which means your
users must perform another action to complete the SetupIntent. Use the
`next_action.cashapp_handle_redirect_or_display_qr_code` object from the
SetupIntent response to redirect your users to a Stripe hosted page that
displays the QR code, or render the QR code directly.

To authenticate users, follow the instructions to [confirm SetupIntent and save
a payment
method](https://docs.stripe.com/payments/cash-app-pay/set-up-payment?platform=web&ui=direct-api#web-create-setup-intent).
After they authenticate, the Cash App mobile application redirects users to the
`return_url` on their mobile device, and the SetupIntent moves to a `succeeded`
state.

[Create a
subscriptionServer-side](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-subscription)
Create a subscription that has a price and customer. Set the value of the
`default_payment_method` parameter to the PaymentMethod ID from the SetupIntent
response.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d default_payment_method={{PAYMENT_METHOD_ID}}
```

Included in the response is the subscription’s first
[PaymentIntent](https://docs.stripe.com/payments/payment-intents), containing
the [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret),
which you use on the client side to securely complete the payment process
instead of passing the entire PaymentIntent object. Return the `client_secret`
to the frontend to complete payment.

#### Note

To create a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) with a
free trial period, see [Subscription
trials](https://docs.stripe.com/billing/subscriptions/cash-app-pay#trial-periods).

## Links

- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay)
- [first API
call](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-setup-intent)
- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [second API
call](https://docs.stripe.com/billing/subscriptions/cash-app-pay#create-subscription)
- [Subscriptions API](https://docs.stripe.com/api/subscriptions)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
- [https://www.stripe.com](https://www.stripe.com)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [pass the client secret to the client
side](https://docs.stripe.com/payments/payment-intents#passing-to-client)
- [confirm SetupIntent and save a payment
method](https://docs.stripe.com/payments/cash-app-pay/set-up-payment?platform=web&ui=direct-api#web-create-setup-intent)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)