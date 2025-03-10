# Promotion codes, upsells and cross-sells

## Use Payment Links to add promotion codes, upsells, and cross-sells to offer discounts and help market related products.

You can use Payment Links and the Stripe Dashboard to offer discounts, allow
customers to upgrade their subscriptions, and market related products during
checkout.

## Add promotion codes

When you [create a payment
link](https://dashboard.stripe.com/payment-links/create) in the Stripe
Dashboard, you have the option of adding promotion codes. Customers can enter
these codes on their payment page to apply discounts on their purchases.

Create a promotion code in the
[Dashboard](https://dashboard.stripe.com/coupons/create) by creating a coupon
and then turning it into a customer-facing promotion code. Use the
`prefilled_promo_code` [URL
parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters)
to prefill a promotion code when sharing a payment link. Learn more about how to
generate [promotion codes for
Checkout](https://docs.stripe.com/payments/checkout/discounts#create-a-promotion-code).

#### Note

By default, payment links create [guest
customers](https://support.stripe.com/questions/guest-customer-faq) for one-time
payments. As a result, promotion codes that are only eligible for first-time
orders won’t work as expected.

## Increase revenue potential with subscription upsells

[Subscription upsells](https://docs.stripe.com/payments/checkout/upsells) give
customers the option to upgrade to a longer-term plan during checkout, such as
progressing from monthly to yearly. This strategy might enhance your average
order value and improve your cash flow.

You can configure a subscription upsell in the Dashboard on the **Price detail**
page. You can view the details for a price by clicking on one you’ve added to a
product. You’ll see a list of eligible upsell prices in the dropdown menu. After
you select an upsell, it immediately applies to eligible payment links that use
that price.

To set up a subscription upsell:

- Choose a subscription under
[Subscriptions](https://dashboard.stripe.com/subscriptions), navigate down to
**Pricing**.
- Use the overflow menu to select **View price details**.
- Navigate down to Upsells, and in the **Upsells to** dropdown menu, select or
add a price.

!

## Offer optional items

You can offer up to 10 optional items on your payment link. Optional items allow
your customers to purchase additional products before checking out. You can
offer multiple products, and specify initial or adjustable quantity.

Customers can add optional items to their order during checkout.

### Dashboard

When you [create a payment
link](https://dashboard.stripe.com/payment-links/create) in the Stripe
Dashboard, you can click **+ Add recommended products** to add up to 10 optional
products to the payment link.

### Add a product-associated optional item

Use [cross-sells](https://docs.stripe.com/payments/checkout/cross-sells) to
specify complementary products that you always want recommended as optional
items at checkout. When you configure a cross-sell associated with a product,
the optional item appears across all eligible payment links with that product.
Cross-sells won’t appear if you specify additional optional items on a payment
link.

To configure a cross-sell:

- On the [Product catalog](https://dashboard.stripe.com/test/products) page,
select your product.
- On the product details page, under **Cross-sells**, find the product you want
to cross-sell.

After you configure a cross-sell, the payment links that contain your designated
product automatically add the cross-sell as an optional item.

## Links

- [create a payment link](https://dashboard.stripe.com/payment-links/create)
- [Dashboard](https://dashboard.stripe.com/coupons/create)
- [URL
parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters)
- [promotion codes for
Checkout](https://docs.stripe.com/payments/checkout/discounts#create-a-promotion-code)
- [guest customers](https://support.stripe.com/questions/guest-customer-faq)
- [Subscription upsells](https://docs.stripe.com/payments/checkout/upsells)
- [Subscriptions](https://dashboard.stripe.com/subscriptions)
- [cross-sells](https://docs.stripe.com/payments/checkout/cross-sells)
- [Product catalog](https://dashboard.stripe.com/test/products)