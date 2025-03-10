# Let customers decide what to pay

## Accept tips and donations, or sell pay-what-you-want products and services.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can use this feature to collect a tip for a service provided, accept
donations for a cause, or give your customers the option to pay what they want
for your product or service. Go to Stripe Support to learn more about Stripe’s
[requirements for accepting tips or
donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations).

Pay-what-you-want payments have the following limitations:

- You can’t add any other line items and the quantity can only be 1.
- You can’t use promotion codes or discounts with them.
- They don’t support recurring payments or cross-sells.

![Custom
amounts](https://b.stripecdn.com/docs-statics-srv/assets/custom-amount.4e76797d1a181222160b2754643e4ee1.png)

[Set up your product
catalog](https://docs.stripe.com/payments/checkout/pay-what-you-want#product-catalog)
Stripe Checkout uses [Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) to structure pay-what-you-want
payments. In the following example, Togethere is selling tickets to a
fundraising dinner and wants to allow their customers to pay what they want for
their tickets.

DashboardAPI
To create a pay-what-you-want model on Stripe through the Dashboard, complete
these steps:

- Create the `Fundraising dinner` product.

- Go to **More** > **Product catalog**.
- Click **+Add product**.
- Enter the **Name** of the product (`Fundraising dinner`).
- *(Optional)* Add a **Description**. The customer sees the description at
checkout.
- Create the price for the `Fundraising dinner` product:

- Click on **More pricing options** at the bottom.
- Select **One-off**.
- Select **Customer chooses price** in the **Choose your pricing model**
dropdown.
- *(Optional)* Add a suggested price.
- *(Optional)* Specify limits that the customer can input.
- Click **Next** and **Add product**.
[Create a Checkout
Session](https://docs.stripe.com/payments/checkout/pay-what-you-want#create-checkout-session)
To enable customers to change the amount on the payment page, use the price ID
when you create a Checkout Session. If you select **Customer chooses price** as
your pricing model, you can’t add any other line items and the quantity can only
be 1.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode cancel_url="https://example.com" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success"
```

## Links

- [inline
pricing](https://docs.stripe.com/products-prices/pricing-models#inline-pricing)
- [requirements for accepting tips or
donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [https://example.com](https://example.com)
- [https://example.com/success](https://example.com/success)