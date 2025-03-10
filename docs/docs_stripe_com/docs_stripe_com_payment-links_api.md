# Use the API to create and manage payment links

## Create and manage payment links with the API.

You can use the [Payment Links
API](https://docs.stripe.com/api/payment_links/payment_links) to create a
payment link that you can share with your customers. Stripe redirects customers
who open this link to a Stripe-hosted payment page.

[Set up your product
catalog](https://docs.stripe.com/payment-links/api#product-catalog)
Payment Links use [Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) to model what your business is
selling. To get started with Payment Links, [create a
product](https://docs.stripe.com/api/products/create), then use that product to
[create a price](https://docs.stripe.com/api/prices/create).

Payment Links supports *flat rate*, *tiered*, *package* and *Customer chooses*
(letting your customer specify the price) prices. *Customer choose prices*
currently doesn’t support recurring payments or donations.

Standard pricingCustomer chooses price
Use *Standard pricing* to create a product or subscription with a fixed amount.

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d currency=usd \
 -d unit_amount=1000 \
 -d product={{PRODUCT_ID}}
```

[Create a payment link](https://docs.stripe.com/payment-links/api#create-link)
To create a payment link, pass in
[line_items](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-line_items).
Each line item contains a
[price](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-line_items-price)
and
[quantity](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-line_items-quantity).
Payment links can contain up to 20 line items when using Standard pricing and 1
line item when using *Customer chooses price*.

```
curl https://api.stripe.com/v1/payment_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1
```

[Share your payment link](https://docs.stripe.com/payment-links/api#share-link)
Each payment link contains a
[url](https://docs.stripe.com/api/payment_links/payment_links/object#payment_link_object-url)
that you can share with your customers through email, on social media, with a
website link, in an app, or through other channels.

[Track payments](https://docs.stripe.com/payment-links/api#tracking-payments)
When customers use a payment link to complete a payment, Stripe sends a
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
webhook that you can use for fulfillment and reconciliation.

Make sure to listen to additional webhooks in case you’ve enabled payment
methods like bank debits or vouchers, which can take 2-14 days to confirm the
payment. For more information, see our guide on [fulfilling orders after a
customer pays](https://docs.stripe.com/checkout/fulfillment).

After a customer completes a purchase, you can redirect them to a URL or display
a custom message by setting
[after_completion](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-after_completion)
on the payment link.

```
curl https://api.stripe.com/v1/payment_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "after_completion[type]"=redirect \
 --data-urlencode "after_completion[redirect][url]"="https://example.com"
```

[Deactivate a payment
link](https://docs.stripe.com/payment-links/api#deactivate-link)
After you’ve created a payment link, you can’t delete it. What you can do is
deactivate a payment link by setting the
[active](https://docs.stripe.com/api/payment_links/payment_links/update#update_payment_link-active)
attribute to `false`.

After you deactivate a link, customers can’t finalize purchases using the link
anymore and are redirected to an expiration page. If you want to reuse a
deactivated payment link, turn it back on by setting the
[active](https://docs.stripe.com/api/payment_links/payment_links/update#update_payment_link-active)
attribute to `true`.

[Configure payment
methods](https://docs.stripe.com/payment-links/api#configure-payment-method)
By default, Stripe selects the relevant payment methods that you enabled in your
Dashboard. To add [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support),
enable them in your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

[OptionalAllow coupons and promotion
codes](https://docs.stripe.com/payment-links/api#promotion-codes)[OptionalCollect
taxes on your payment
link](https://docs.stripe.com/payment-links/api#stripe-tax)[OptionalCollect
billing and shipping
addresses](https://docs.stripe.com/payment-links/api#address-collection)[OptionalAllow
adjustable
quantities](https://docs.stripe.com/payment-links/api#allow-adjustable-quantities)[OptionalCreate
subscriptions](https://docs.stripe.com/payment-links/api#creating-subscriptions)[OptionalSpecify
the payment methods you want to
accept](https://docs.stripe.com/payment-links/api#payment-methods)[OptionalCollect
a terms of service
agreement](https://docs.stripe.com/payment-links/api#terms-of-service)[OptionalAdd
custom
fields](https://docs.stripe.com/payment-links/api#custom-fields)[OptionalCollect
application fees using
Connect](https://docs.stripe.com/payment-links/api#application-fees)[OptionalSend
post-payment
invoices](https://docs.stripe.com/payment-links/api#post-payment-invoices)

## Links

- [Payment Links API](https://docs.stripe.com/api/payment_links/payment_links)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [create a product](https://docs.stripe.com/api/products/create)
- [create a price](https://docs.stripe.com/api/prices/create)
-
[line_items](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-line_items)
-
[price](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-line_items-price)
-
[quantity](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-line_items-quantity)
-
[url](https://docs.stripe.com/api/payment_links/payment_links/object#payment_link_object-url)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [fulfilling orders after a customer
pays](https://docs.stripe.com/checkout/fulfillment)
-
[after_completion](https://docs.stripe.com/api/payment_links/payment_links/create#create_payment_link-after_completion)
- [https://example.com](https://example.com)
-
[active](https://docs.stripe.com/api/payment_links/payment_links/update#update_payment_link-active)
- [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)