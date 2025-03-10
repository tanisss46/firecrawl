# How products and prices work

## Learn how products and prices in Stripe model your business.

Products and prices are core resources for many Stripe integrations. Products
define what your business offers, whether that’s goods or services. Prices
define how much and how often to charge for products.

You can create products and prices in Stripe or
[import](https://docs.stripe.com/products-prices/getting-started#import-products-prices)
them into Stripe through the [API](https://docs.stripe.com/api/products). After
you create products and prices, you can use them with [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions/create), [Payment
Links](https://docs.stripe.com/payment-links),
[Invoices](https://docs.stripe.com/invoicing),
[Quotes](https://docs.stripe.com/quotes/create), or a custom integration to
create [Subscriptions](https://docs.stripe.com/billing).

## Products

Products describe the specific goods or services you offer to your customers.

- If you’re an e-commerce store selling clothing, one of your products might be
a large white t-shirt. In Stripe, you can create a separate product for each
size and color combination.
- If you’re a SaaS platform, you might have basic and premium pricing tiers. In
this case, both basic and premium are separate products because they typically
offer unique attributes or features.
- If you’re a donation platform that accepts donations for several different
causes, each cause is a different product.

Each product has a unique ID. Unlike most Stripe resources, you can choose the
ID of the product yourself. We recommend choosing an ID that makes it easy to
integrate Stripe with other systems you use. For example, if you’re selling
physical goods, you can use the internal ID from your own systems.

When you create a product in Stripe, you have to provide a name. You can
optionally add other attributes, like a description or image. If you’re using
[Stripe Tax](https://docs.stripe.com/tax), you can also define a [tax
code](https://docs.stripe.com/tax/tax-codes) for each product, such as pet
grooming, e-books, or SaaS. Stripe Tax uses the tax code to automatically
calculate and collect sales taxes during purchase.

## Prices

In Stripe, price objects are more than a numerical amount to pay. Prices include
additional information, such as tax behavior, volume tiers, and recurrence
intervals for subscriptions. You don’t need to create new prices for each
purchase–if you’re selling a product for one price, you only need to create one
price. You can also make this price the [default
price](https://docs.stripe.com/products-prices/manage-prices#default-price) for
the product.

Prices can either be one-time or recurring. Subscriptions use recurring prices
to charge the customer at an interval, such as “once a month.” If you sell the
same service at several different subscription intervals, it’s best to create
multiple recurring prices for the same product. Learn more about [pricing
models](https://docs.stripe.com/products-prices/pricing-models#flat-rate).

A single Price can support multiple currencies. For example, if you sell a
product in the USA for 10 USD, Europe for 9 EUR, and Japan for 1300 JPY, the
same Price object can cover all three currencies. Each purchase uses one of the
Price’s supported currencies, depending on how you use the Price in your
integration. Learn more about [multi-currency
Prices](https://docs.stripe.com/products-prices/pricing-models#multicurrency).

Because a product can have multiple prices associated with it, you’ll need to
specify which price to use when creating Checkout Sessions, Payment Links,
Invoices, Quotes, or Subscriptions.

Most prices define a fixed `unit_amount`, but you can also configure the price
to function with different tiers or usage-based models. Learn more about [tiered
pricing](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
and [usage-based
pricing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing).

If you’re using Stripe Tax, you can specify the `tax_behavior` for the price to
determine whether the tax is already included in the amount, or if it needs to
be added. Learn more about [tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior).

## Working with products and prices

### Create or import products and prices

The quickest way to get started with products and prices is to create them
through the [Stripe Dashboard](https://dashboard.stripe.com/products).

If you have a large product catalog that you manage using a spreadsheet or other
software, you might prefer to import the product catalog programmatically using
the [Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) API. Learn more about [import
products and
prices](https://docs.stripe.com/products-prices/getting-started#import-products-prices).

If you need to charge an amount of money that’s different for each transaction
(for example, a user-selected donation amount), you can create the product, but
not create a price. Instead, you can use the `price_data` parameter when
creating Checkout Sessions or Subscriptions to set the particular price.

### Use products and prices

Stripe CheckoutPayment LinksSubscriptionsQuotesInvoices
When creating a Checkout Session, specify the price `id` for each line item. The
Checkout Session uses the price to compute the order total. It also retrieves
the product associated with the price, then uses the product’s name and image to
render the Checkout page.

## Manage existing products and prices

You can update product details through the Dashboard or API. For example, you
might change the description of a product, or add new product images to use on
the [Checkout](https://docs.stripe.com/payments/checkout) page.

If you’re no longer selling a product, you can archive both it and the price
through the Dashboard by clicking the **Archive** button, or through the API by
setting `active` to `false`. We store the archived product and price information
indefinitely to maintain records of past transactions.

In general, you can’t delete products or prices, you can only archive them. In
certain cases, you can use the Dashboard to delete a price that has never been
used, or to delete a product that doesn’t have any prices set.

To change the price of a product, create a new price for the new amount, then
archive the existing price by setting `active` to false. Instead of changing the
`unit_amount` on the existing price, you need to create a new price to make sure
that we keep the existing price as an immutable record of past transactions.

You can set a [default
price](https://docs.stripe.com/products-prices/manage-prices#default-price) on a
product to specify the most common price to present to customers. You can change
the default price to another price later, such as if you increase the price of
your product.

## Understand product and price compatibility

Not all features of products and prices are compatible with all Stripe APIs.
Consult the following table for compatibility information.

Feature Checkout Payment Links Quotes Subscriptions Invoices Product
imagesIgnored*Ignored*Ignored*Product descriptionsIgnored*Ignored*Product tax
codesProduct statement descriptorIgnored*Recurring pricesMulti-currency
pricesIgnored*Ignored*Tiered pricesDisallowed*Decimal amounts (for example,
charging half-a-cent per unit)Disallowed*Usage-based pricesDisallowed*Customer
chooses priceDisallowed*Disallowed*Disallowed*
Entries marked as Disallowed indicate that if a product or price uses this
feature, you can’t use that product or price with this Stripe API.

Entries marked as Ignored indicate that the feature has no effect with this
Stripe API, but you can still use the product or price as usual.

## Understand limitations

We don’t limit the number of customers, coupons, products, prices, or most other
objects that you can create in your Stripe account.

When using recurring prices with Subscriptions:

- All prices on a Subscription must have the same
[recurring.interval](https://docs.stripe.com/api/prices/create#create_price-recurring-interval)
and
[recurring.interval_count](https://docs.stripe.com/api/prices/create#create_price-recurring-interval_count)
- The maximum interval time period of a price is 3 years

## Links

-
[import](https://docs.stripe.com/products-prices/getting-started#import-products-prices)
- [API](https://docs.stripe.com/api/products)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/create)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Invoices](https://docs.stripe.com/invoicing)
- [Quotes](https://docs.stripe.com/quotes/create)
- [Subscriptions](https://docs.stripe.com/billing)
- [guide](https://docs.stripe.com/products-prices/getting-started)
- [Stripe Tax](https://docs.stripe.com/tax)
- [tax code](https://docs.stripe.com/tax/tax-codes)
- [default
price](https://docs.stripe.com/products-prices/manage-prices#default-price)
- [pricing
models](https://docs.stripe.com/products-prices/pricing-models#flat-rate)
- [multi-currency
Prices](https://docs.stripe.com/products-prices/pricing-models#multicurrency)
- [tiered
pricing](https://docs.stripe.com/products-prices/pricing-models#tiered-pricing)
- [usage-based
pricing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior)
- [Stripe Dashboard](https://dashboard.stripe.com/products)
- [Prices](https://docs.stripe.com/api/prices)
- [Checkout](https://docs.stripe.com/payments/checkout)
-
[recurring.interval](https://docs.stripe.com/api/prices/create#create_price-recurring-interval)
-
[recurring.interval_count](https://docs.stripe.com/api/prices/create#create_price-recurring-interval_count)