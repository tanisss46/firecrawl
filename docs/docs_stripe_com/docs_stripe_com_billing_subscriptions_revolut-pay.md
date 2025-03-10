# Set up a subscription with Revolut Pay

## Learn how to create and charge for a subscription with Revolut Pay.

Use this guide to set up a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[Revolut Pay](https://docs.stripe.com/payments/revolut-pay) as a payment method.

SetupIntents APISubscriptions APIStripe-hosted page
You can use the [Checkout API](https://docs.stripe.com/api/checkout/sessions) to
create and confirm a subscription with a prebuilt checkout page.

[Create a product and
priceDashboard](https://docs.stripe.com/billing/subscriptions/revolut-pay?api-integration=checkout#create-product-plan-code)
[Products](https://docs.stripe.com/api/products) represent the item or service
you’re selling. [Prices](https://docs.stripe.com/api/prices) define how much and
how frequently you charge for a product. This includes how much the product
costs, what currency you accept, and whether it’s a one-time or recurring
charge. If you only have a few products and prices, create and manage them in
the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15
GBP monthly subscription. To model this:

- Navigate to the [Add a
product](https://dashboard.stripe.com/test/products/create) page.
- Enter a **Name** for the product.
- Enter **15** for the price.
- Select **GBP** as the currency.
- Click **Save product**.

After you create the product and the price, record the price ID so you can use
it in subsequent steps. The pricing page displays the ID and it looks similar to
this: `price_G0FvDp6vZvdwRZ`.

[Create a Checkout
SessionServer-side](https://docs.stripe.com/billing/subscriptions/revolut-pay?api-integration=checkout#web-create-checkout-session)
Your customer must authorize you to use their Revolut account for future
payments through Stripe Checkout. This allows you to accept Revolut payments.
Add a checkout button to your website that calls a server-side endpoint to
create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions).

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

Create a Checkout Session in `subscription` mode to collect the required
information. After creating the Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
that the response returns.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "payment_method_types[0]"=card \
 -d "payment_method_types[1]"=revolut_pay \
 -d mode=subscription
```

[Test your
integrationServer-side](https://docs.stripe.com/billing/subscriptions/revolut-pay?api-integration=checkout#web-test-integration)
Select Revolut Pay as the payment method and tap Subscribe. You can test the
successful payment case by authenticating the payment on the redirect page. The
PaymentIntent transitions from `requires_action` to `succeeded`.

## Links

- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Revolut Pay](https://docs.stripe.com/payments/revolut-pay)
- [Checkout API](https://docs.stripe.com/api/checkout/sessions)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)