# Collect taxes

## Learn how to collect taxes with Stripe Tax.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Stripe Tax allows you to calculate the tax on your one-time and recurring
payments when you use Checkout. You can enable Stripe Tax to automatically
compute taxes on all of your Checkout purchases and subscriptions.

[Activate Stripe Tax](https://docs.stripe.com/payments/checkout/taxes#activate)
[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to activate Stripe Tax.

## Update your Products and Prices

When calculating tax, Stripe Tax uses information stored on the
[Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) APIs to determine the right rates
and rules. You can update your Checkout products and prices to include:

- `tax_behavior`—Specifies whether the price is considered `inclusive` or
`exclusive` of taxes.
- `tax_code` (*optional*)—Specifies the product tax code. If you don’t set a
`tax_code` on a product, we apply your preset product tax code. For more
information, consult our [list of tax
codes](https://docs.stripe.com/tax/tax-codes).

When you set the `tax_behavior` parameter to `exclusive`, it adds tax to the
subtotal. This is common in US markets and for business-to-business (B2B) sales.
If you set the `tax_behavior` to `inclusive`, the amount your buyer pays never
changes (even if the tax rate varies). This is common practice for
business-to-consumer (B2C) buyers in markets outside of the US. If you don’t
want to create your products and prices upfront, you can pass the
`price_data.tax_behavior` and `product_data.tax_code` parameters in your
Checkout session.

#### Note

Learn more about [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior).

## Create a Checkout Session

After updating your products and prices, you’re ready to start calculating tax
on your Checkout sessions. You can create sessions for one-time and recurring
purchases.

To calculate tax for new customers, Checkout validates and uses the provided
shipping or billing address. For existing customers, Checkout calculates tax by
validating and using the attached customer shipping or billing address. If you
capture a new billing or shipping address for an existing customer, Checkout
won’t automatically override the previous billing or shipping information. You
must explicitly request customer address changes.

### Apple Pay and Google Pay

If you wish to ensure that Google Pay is offered as a payment method while using
Stripe Tax in Checkout, you must require collecting a shipping address. Apple
Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay
version 12 or greater.

## Calculate tax for new customers

If you don’t pass in an existing customer when creating a Checkout session,
Checkout creates a new customer and automatically saves the billing address and
shipping information. Checkout uses the shipping address entered during the
session to determine the customer’s location for calculating tax. If you don’t
collect shipping information, Checkout uses the billing address.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 -d "automatic_tax[enabled]"=true \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return"
```

[OptionalCalculate tax for existing
customers](https://docs.stripe.com/payments/checkout/taxes#existing-customers)[OptionalCheck
the
response](https://docs.stripe.com/payments/checkout/taxes#check-the-response)

## Links

- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [list of tax codes](https://docs.stripe.com/tax/tax-codes)
- [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [https://example.com/return](https://example.com/return)