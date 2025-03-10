# Manage products and prices

## Learn how to manage products and prices.

You can create and update products and prices in the Dashboard or through the
API.

Some advanced use cases, like [creating variable
prices](https://docs.stripe.com/products-prices/pricing-models#variable-pricing),
require you to use the API. If you have a large number of products and prices or
if you’re [building a custom
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements)
with Elements, you need to use the API.

- Use the [Dashboard](https://dashboard.stripe.com/test/products) to create and
manage products and prices if you want to avoid writing code or if you only have
a few products and prices. Set up your [pricing
model](https://docs.stripe.com/products-prices/pricing-models) in test mode and
click the ** to live mode** button on the product details page.
- Use the [API](https://docs.stripe.com/api) or the [Stripe
CLI](https://docs.stripe.com/stripe-cli) to create and manage products and
prices. The API is a direct method that you use for production implementations.
The Stripe CLI is a developer tool that helps you build, test, and manage your
integration with Stripe directly from your terminal.

The following API steps use a fictional SaaS collaboration tool (Togethere) as
an example, where the basic product is a project management dashboard.

## Create a product

DashboardAPI
### Create a product and price

#### Create a product

To create a product in the Dashboard:

- Go to **More** > **Product catalog**.
- Click **+Add product**.
- Enter the **Name** of your product.
- *(Optional)* Add a **Description**. The description appears at checkout, on
the [customer portal](https://docs.stripe.com/customer-management), and in
[quotes](https://docs.stripe.com/quotes).
- *(Optional)* Add an **Image** of your product. Use a JPEG, PNG, or WEBP file
that’s smaller than 2MB. The image appears at checkout.
- *(Optional)* If you’re using [Stripe Tax](https://docs.stripe.com/tax), select
a **Tax code** for your product. See [tax
codes](https://docs.stripe.com/tax/tax-codes) for more information about the
appropriate category for your product.
- *(Optional)* Enter a **Statement descriptor**. This descriptor overrides any
account descriptors for recurring payments. Choose something that your customers
would recognize on a bank statement.
- *(Optional)* Enter a **Unit label**. This describes how you sell your product.
For example, if you charge by the seat, enter “seat” so the line item includes
“per seat” for the price. Unit labels appear at checkout, and in invoices,
receipts, and the [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal).

#### Create a price for the product

To save a product in the Dashboard, you must also add at least one price.

The product editor shows the flat-rate pricing model by default. You can create
multiple prices or use a different pricing model with the **Advanced pricing
options**.

- Select a **Pricing model**. For more details about recurring pricing models,
read the [pricing model
guide](https://docs.stripe.com/products-prices/pricing-models).

- **Flat-rate pricing**: Charge the same price for each unit. If you use this
option, select **One time** or **Recurring**.
- **Package pricing**: Charge by the package, or group of units, such as
charging 25 USD for every 5 units. Purchases are rounded up by default, so a
customer buying 8 units pays 50 USD.
- **Graduated pricing**: Use pricing tiers that might result in a different
price for some units in an order. For example, you might charge 10 USD per unit
for the first 100 units and then 5 USD per unit for the next 50. If you use this
option, select the currency for the price and fill in the tier table.
- **Volume pricing**: Charge the same price for each unit based on the total
number of units sold. For example, you might charge 10 USD per unit for 50
units, and 7 USD per unit for 100 units. If you use this option, select the
currency for the price and fill in the tier table.
- **Customer chooses price**: Let the payer decide on the amount to pay for your
product, service, or cause. **Customer chooses price** is only compatible with
Checkout and Payment Links.
- **Usage-based pricing**: Charge your customers based on how much of your
service they use during the billing cycle.
- *(Optional)* If you’re selling in multiple currencies, click **Add another
currency** to set how much to charge in each currency.
- Select a **Billing period** for recurring prices. You can add a custom period
if none of the drop-down options are what you want.
- Select whether to **Include tax in price**. Learn more about [taxes and
subscriptions](https://docs.stripe.com/billing/taxes).
- *(Optional)* Enter a **Price description**. Customers don’t see this
description.
- *(Optional)* Click **Advanced pricing options** if you want to create multiple
prices for your product.
- Click **Add product** to save the product and price. You can [edit
both](https://docs.stripe.com/products-prices/manage-prices#edit-product) later.

## Edit a product

DashboardAPI
To modify a product in the Dashboard:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu (), then click
**Edit product**.
- Make your changes to the product.
- Click **Save product**.

You can also edit products from within the product information page by clicking
the overflow menu () or **Edit**.

## Archive a product

If you want to disable a product so that it can’t be added to new invoices or
subscriptions, you can archive it. If you archive a product, any existing
subscriptions that use the product remain active until they’re canceled and any
existing payment links that use the product are deactivated. You can’t delete
products that have an associated price, but you can archive them.

DashboardAPI
To archive a product:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu (), then click
**Archive product**.

To unarchive a product:

- Go to the **Archived** tab on the **Product catalog**>**Overview** page.
- Find the product you want to modify, click the overflow menu (), then click
**Unarchive product**.

You can also unarchive a product from the product information page.

## Delete a product

You can only delete products that have no prices associated with them.
Alternatively, you can [archive a
product](https://docs.stripe.com/products-prices/manage-prices#archive-product).

DashboardAPI
If a product has a price associated with it, you have to
[delete](https://docs.stripe.com/products-prices/manage-prices#delete-price) or
[archive](https://docs.stripe.com/products-prices/manage-prices#archive-price)
the price before you can delete the product. Stripe keeps a record of the price
and product for historical transactions.

To permanently delete a product:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu (), then click
**Delete product**.

## Create a price

You can create single or multiple prices for a product. For example, Togethere
may have a “starter” level offered at 10 USD per month, 100 USD per year, or 9
EUR as a one-time purchase.

#### Note

After you create a price, you can only update its `metadata`, `nickname`, and
`active` fields.

DashboardAPI
To create a price in the Dashboard, you have to [create a
product](https://docs.stripe.com/products-prices/manage-prices#create-product)
first. Then you can create a price:

- Select a **Pricing model**. For more details about recurring pricing models,
read the [pricing model
guide](https://docs.stripe.com/products-prices/pricing-models).

- **Flat-rate pricing**: Charge the same price for each unit. If you use this
option, select **One time** or **Recurring**.
- **Package pricing**: Charge by the package, or group of units, such as
charging 25 USD for every 5 units. Purchases are rounded up by default, so a
customer buying 8 units pays 50 USD.
- **Graduated pricing**: Use pricing tiers that might result in a different
price for some units in an order. For example, you might charge 10 USD per unit
for the first 100 units and then 5 USD per unit for the next 50. If you use this
option, select the currency for the price and fill in the tier table.
- **Volume pricing**: Charge the same price for each unit based on the total
number of units sold. For example, you might charge 10 USD per unit for 50
units, and 7 USD per unit for 100 units. If you use this option, select the
currency for the price and fill in the tier table.
- **Customer chooses price**: Let the payer decide on the amount to pay for your
product, service, or cause. **Customer chooses price** is only compatible with
Checkout and Payment Links.
- **Usage-based pricing**: Charge your customers based on how much of your
service they use during the billing cycle.
- *(Optional)* If you’re selling in multiple currencies, click **Add another
currency** to set how much to charge in each currency.
- Select a **Billing period** for recurring prices. You can add a custom period
if none of the drop-down options are what you want.
- Select whether to **Include tax in price**. Learn more about [taxes and
subscriptions](https://docs.stripe.com/billing/taxes).
- *(Optional)* Enter a **Price description**. Customers don’t see this
description.
- Click **Create price** to save the price. You can [edit the
price](https://docs.stripe.com/products-prices/manage-prices#edit-price) later.

### Set a default price

A product’s default price is the most common price you want to present to
customers. For example, a product could have multiple prices for seasonal sales,
but the default is the regular (non-sale) price. If your product only has one
price, that is its default price. The default price must be an
[active](https://docs.stripe.com/api/prices/object#price_object-active) Price.

DashboardAPI
To change your product’s default price in the Dashboard:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu (), then click
**Edit product**.
- Under the **Price information** section, find the price you want to set as the
new default price, then click **Set as default price**.
- Click **Save product**.

To create a new price and make it the new default price in the Dashboard:

- Go to **More** > **Product catalog**.
- Find the product you want to modify and click on it to open the product
information page.
- In the **Pricing** section, click the **Add another price** button.
- Enter your pricing details and select **Set as default price**. Read more
about the fields available when you [create a
price](https://docs.stripe.com/products-prices/manage-prices#create-price).
- Click **Add price**.

### Lookup keys

Most businesses display pricing information on their website. If these prices
are hard-coded and you want to change them, the process is often manual and
requires you to deploy new code. To better manage these scenarios, you can use
the
[lookup_key](https://docs.stripe.com/api/prices/create#create_price-lookup_key)
attribute on the [Price
object](https://docs.stripe.com/api/prices/object#price_object). This key allows
you to:

- Render different prices in your frontend.
- Use the rendered price to bill customers.

You can pass a `lookup_key` when you create a price:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d product={{PRODUCT_ID}} \
 -d unit_amount=1000 \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d lookup_key=standard_monthly
```

Instead of hard-coding text like **10 USD per month** on your pricing page and
using a price ID on your backend, you can query for the price using the
`standard_monthly` key and then render that in your frontend:

```
curl -G https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "lookup_keys[]"=standard_monthly
```

#### Note

To improve performance, you might want to add a caching layer to only reload the
price occasionally.

When a customer clicks your subscribe or pay button, you pass the price from the
`GET` request above into the Subscriptions API.

Now that you can render different prices, if you decide that you want to start
charging new users 20 USD per month rather than 10 USD per month, you only need
to create a new price and transfer the lookup key to that new price using
[transfer_lookup_key=true](https://docs.stripe.com/api/prices/create#create_price-transfer_lookup_key):

#### Rounding

Rounding occurs on the line item level of your
[invoices](https://docs.stripe.com/api/invoices). For example, if you create a
price with `unit_amount_decimal = 0.05` and a monthly subscription for that
[price] with `quantity = 30`, rounding occurs after multiplying the quantity by
the decimal amount. In this case, the calculated amount for the line item would
be `0.05 * 30 = 1.5`, which rounds up to 2 cents. If you have multiple line
items, each is rounded up before summing up the total amount for the invoice.
This ensures that customers are still charged an integer minor unit amount, as
decimal amounts only apply for pricing.

Exclusive taxes are added to each line item amount, depending on the tax rate.
If you enable [automatic taxes](https://docs.stripe.com/tax/invoicing),
exclusive taxes are applied and rounded on the total of the invoice, including
invoice level discounts. If you use manual taxes on either the line item level
or the invoice level, you can choose how to apply rounding. Use the [invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) page in the
Dashboard to apply and round taxes for each line item, or apply and round taxes
on the invoice subtotal.

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d product={{PRODUCT_ID}} \
 -d unit_amount=2000 \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d lookup_key=standard_monthly \
 -d transfer_lookup_key=true
```

## Edit a price

Multiple properties can be updated on a price, either in the Dashboard or the
API. For example, you can change whether the price is active, or modify its
metadata.

Note that you can not change a price’s amount in the API. Instead, we recommend
creating a new price for the new amount, switch to the new price’s ID, then
update the old price to be inactive.

DashboardAPI
To modify a price in the Dashboard:

- Go to **More** > **Product catalog**.
- Find the product for the price you want to modify, and click on it
- Find the price you want to modify, click the overflow menu (), then click
**Edit price**.
- Make your changes to the price. You can add another price at this point.
- Click **Save**.

## Archive a price

If you want to disable a price so that it can’t be added to new invoices or
subscriptions, you can archive it. If you archive a price, any existing
subscriptions that use the price remain active until they’re canceled and any
existing payment links that use the product are deactivated.

DashboardAPI
To archive a price through the Dashboard:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu ().
- On the product information page, find the price you want to modify, then click
the overflow menu () next to it and click **Archive price**.

To unarchive a price:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu ().
- On the product information page, find the price you want to modify, then click
the overflow menu () next to it and click **Unarchive price**.

## Delete a price

You can only delete prices that you’ve never used. Otherwise, you can [archive
them](https://docs.stripe.com/products-prices/manage-prices#archive-price).

DashboardAPI
To permanently delete a price in the Dashboard:

- Go to **More** > **Product catalog**.
- Find the product you want to modify, click the overflow menu ().
- On the product information page, find the price you want to modify, then click
the overflow menu () next to it and click **Delete price**.

## Display pricing information

After creating products and prices, you can embed a [pricing
table](https://docs.stripe.com/payments/checkout/pricing-table) on your website
to display pricing information to your customers. When customers choose a
subscription option, they’re taken directly to checkout. Configure, customize,
and update directly in the
[Dashboard](https://dashboard.stripe.com/test/pricing-tables) without writing
any code.

## Links

- [creating variable
prices](https://docs.stripe.com/products-prices/pricing-models#variable-pricing)
- [building a custom
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements)
- [Dashboard](https://dashboard.stripe.com/test/products)
- [pricing model](https://docs.stripe.com/products-prices/pricing-models)
- [API](https://docs.stripe.com/api)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [customer portal](https://docs.stripe.com/customer-management)
- [quotes](https://docs.stripe.com/quotes)
- [Stripe Tax](https://docs.stripe.com/tax)
- [tax codes](https://docs.stripe.com/tax/tax-codes)
- [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
- [taxes and subscriptions](https://docs.stripe.com/billing/taxes)
- [active](https://docs.stripe.com/api/prices/object#price_object-active)
-
[lookup_key](https://docs.stripe.com/api/prices/create#create_price-lookup_key)
- [Price object](https://docs.stripe.com/api/prices/object#price_object)
-
[transfer_lookup_key=true](https://docs.stripe.com/api/prices/create#create_price-transfer_lookup_key)
- [invoices](https://docs.stripe.com/api/invoices)
- [automatic taxes](https://docs.stripe.com/tax/invoicing)
- [invoice settings](https://dashboard.stripe.com/settings/billing/invoice)
- [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
- [Dashboard](https://dashboard.stripe.com/test/pricing-tables)