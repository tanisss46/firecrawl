# Specify product tax codes and tax behavior

## Add tax codes and tax behavior to your products and prices to automatically calculate tax.

#### Note

[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

Stripe Tax uses product tax codes (PTCs) to associate products with their
applicable tax rates, which might be lower or higher in different cities or
countries. [Assign each of your products a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
to automatically apply the rate and other taxability rules.

If a product doesn’t fit any of the specific codes, use one of the codes with
“General” in its name to apply the standard rate of the jurisdiction. See our
[list of available tax codes](https://docs.stripe.com/tax/tax-codes).

## Preset tax codes

When activating Stripe Tax you can set two types of preset tax codes: one for
products and one for shipping. You can set both in the [Tax
settings](https://dashboard.stripe.com/settings/tax) in the Dashboard.

![The tax settings showing the preset tax codes, and the default shipping tax
code.](https://b.stripecdn.com/docs-statics-srv/assets/pp-settings-v3.4a3660016d805248b9fb49f1bffffd76.png)

The tax settings showing the preset tax codes, and the default shipping tax
code.

### Preset product tax code

The preset product tax code represents your product or service in Stripe Tax. We
use the preset if you don’t explicitly specify a `tax_code` on your
[products](https://docs.stripe.com/api/products) or in
[product_data](https://docs.stripe.com/api/prices/create#create_price-product_data)
on your transactions. As you process payments, we also use the preset tax code
to display the tax thresholds you might be approaching or have exceeded, under
the **Threshold monitoring** section in your tax settings.

If you sell multiple different product types (for example, SaaS and e-books),
you could use test mode to change your preset tax code and review the impact of
different product types on the **Monitor** tab.

### Preset shipping tax code

The preset shipping tax code represents the tax treatment for shipping fees when
charged. We use this if you don’t explicitly specify a `tax_code` on a shipping
rate. Stripe Tax allows you to change the default shipping treatment to
Nontaxable if you don’t want to charge any tax on shipping fees. We recommend
you leave the default as “Shipping” to ensure the correct tax is always charged.

To charge tax on shipping for recurring payments, you can create a Product or
pass `product_data` for a line item called “shipping” and select the shipping
`tax_code`.

The taxability of shipping can vary by US state and country.

![Map of the United States showing states where shipping is taxable, not
taxable, or have no sales
tax.](https://b.stripecdn.com/docs-statics-srv/assets/pp_shipping_us_taxability.e90be097aec68286cbc6a83a4e5bfc13.png)

## Tax behavior

You must specify a `tax_behavior` on a price, or a default tax behavior in the
tax settings in the Dashboard, which determines how tax is presented to the
buyer. This allows you to localize your checkout depending on the market. When
you set tax behavior to exclusive, it adds tax onto the subtotal amount you
specify on your price. This is common in US markets and for B2B sales. When set
to inclusive, the amount your buyer pays never changes, even if the tax rate
varies. This is common practice for B2C buyers in many markets outside the US.

### Setting a default tax behavior (recommended)

You can define a default tax behavior that applies to every price that has no
tax behavior defined. You can setup the default tax behavior in the [Stripe Tax
settings](https://dashboard.stripe.com/settings/tax) under the **Include tax in
prices** section.

After you set the default tax behavior, all prices that don’t have a
`tax_behavior` defined, use this setting and are ready for Stripe Tax. The
options for the default tax behavior are:

- **Automatic**: The tax behavior is based on the currency that’s chosen for a
product price. For the currencies `USD` and `CAD` the tax behavior is exclusive.
For all other currencies the tax behavior is inclusive. This also works with
[multi-currency
Prices](https://docs.stripe.com/products-prices/pricing-models#multicurrency).
- **Inclusive**: Inclusive tax is already included in the price. For example, a
product has the price defined as 5.00 USD. The final price the customer pays is
5.00 USD.
- **Exclusive**: Exclusive tax is added on top of the price. For example, a
product has the price defined as 5.00 USD. The tax charged on this product could
be 10% and would result in a final price of 5.50 USD. (Tax rates might
differ—this is only an explanatory example.)

To override this setting for an individual price, [set a tax behavior on a
price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional)).

## Setting tax behavior on a price (optional)

You can set the tax behavior for a [Price](https://docs.stripe.com/api/prices)
when creating it with the Dashboard or the API. When creating a Price in the
Dashboard, you can inspect the impact of your pricing model on your revenue.

#### Caution

You can’t change `tax_behavior` after it’s been set to one of “exclusive” or
“inclusive”.

![Tax behavior for a Price object in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_pricing.c4124697874540947a451121f0c73c4d.png)

To create a Price with `tax_behavior` through the API, it might look like this:

```
curl https://api.stripe.com/v1/prices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d unit_amount=10000 \
 -d currency=usd \
 -d product=prod_q23fxaHasd \
 -d tax_behavior=exclusive \
 -d "recurring[interval]"=month
```

For a [multi-currency
Price](https://docs.stripe.com/products-prices/pricing-models#multicurrency),
use the
[currency_options.<currency>.tax_behavior](https://docs.stripe.com/api/prices/create#create_price-currency_options-tax_behavior)
parameter to set different tax behaviors for different currencies.

In some cases, you might want to use a custom price that hasn’t been
pre-configured. You can pass in `price_data` instead of a price ID. For example,
accepting a one time payment for a custom price might look like this:

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d success_url="https://example.com/success" \
 -d cancel_url="https://example.com/cancel" \
 -d "payment_method_types[0]"=card \
 -d "line_items[0][price_data][currency]"="usd" \
 -d "line_items[0][price_data][unit_amount]"=10000 \
 -d "line_items[0][price_data][tax_behavior]"="exclusive" \
 -d "line_items[0][price_data][product]"="prod_Jb3wOhvaIOZZTM" \
 -d "line_items[0][quantity]"=2 \
 -d mode=payment
```

## Setting a tax code on a product (recommended)

When creating Products in the Dashboard you can set your `tax_code` in the
dropdown by searching for any available [tax
code](https://docs.stripe.com/tax/tax-codes). If you don’t, Stripe Tax uses the
preset tax code defined on the
[Dashboard](https://dashboard.stripe.com/settings/tax). If a product could fit
multiple codes, for example, a SaaS product used for personal or business use
depending on the type of customer, we recommend creating two separate products
in Stripe and assigning the appropriate code to each.

![Tax codes for a product in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_product_tax_category.e6ad090b235a41108b8843420db18330.png)

To create a Product with `tax_code` using the API, it might look like this:

```
curl https://api.stripe.com/v1/products \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d name="Test Product" \
 -d tax_code=txcd_10000000
```

In some cases, you might want to use a custom product that hasn’t been
pre-configured. You can pass in `product_data` instead of a product ID. For
example, accepting a one time payment for a custom product might look like this:

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d success_url="https://example.com/success" \
 -d cancel_url="https://example.com/cancel" \
 -d "payment_method_types[0]"=card \
 -d "line_items[0][price_data][currency]"="usd" \
 -d "line_items[0][price_data][unit_amount]"=10000 \
 -d "line_items[0][price_data][tax_behavior]"="exclusive" \
 -d "line_items[0][price_data][product_data][name]"="Product name" \
 -d "line_items[0][price_data][product_data][tax_code]"=txcd_10000000 \
 -d "line_items[0][quantity]"=2 \
 -d mode=payment
```

## Creating a shipping rate with tax code (optional)

Checkout payment mode allows you to set shipping rates and charge tax on
shipping. You can automatically calculate tax on shipping charges by setting the
tax code on the shipping rate in the Dashboard or
[API](https://docs.stripe.com/api/shipping_rates).

![Shipping rate with a tax code in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_shipping_rate_v3.a204f73ab02310683aace14717d960f4.png)

```
curl https://api.stripe.com/v1/shipping_rates \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d display_name="Ground shipping" \
 -d type="fixed_amount" \
 -d "fixed_amount[amount]"=500 \
 -d "fixed_amount[currency]"=usd \
 -d tax_behavior="inclusive" \
 -d tax_code="txcd_92010001"
```

## Interested in using Stripe Tax for events where the location differs from a customer's address and might be subject to special local and state taxes?

Provide your email address below and our team will contact you soon.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## See also

- [Checkout and Tax](https://docs.stripe.com/tax/checkout)
- [Invoicing and Tax](https://docs.stripe.com/tax/invoicing)
- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)

## Links

- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [Assign each of your products a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
- [list of available tax codes](https://docs.stripe.com/tax/tax-codes)
- [products](https://docs.stripe.com/api/products)
-
[product_data](https://docs.stripe.com/api/prices/create#create_price-product_data)
- [multi-currency
Prices](https://docs.stripe.com/products-prices/pricing-models#multicurrency)
- [Price](https://docs.stripe.com/api/prices)
-
[currency_options.<currency>.tax_behavior](https://docs.stripe.com/api/prices/create#create_price-currency_options-tax_behavior)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [API](https://docs.stripe.com/api/shipping_rates)
- [privacy policy](https://stripe.com/privacy)
- [Checkout and Tax](https://docs.stripe.com/tax/checkout)
- [Invoicing and Tax](https://docs.stripe.com/tax/invoicing)
- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)