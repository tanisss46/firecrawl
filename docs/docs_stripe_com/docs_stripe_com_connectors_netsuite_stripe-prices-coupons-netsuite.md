# Stripe prices and coupons in NetSuite

## Use the connector to represent Stripe prices and coupons in NetSuite.

The Stripe Connector for NetSuite syncs the Stripe
[products](https://docs.stripe.com/products-prices/how-products-and-prices-work),
[prices](https://docs.stripe.com/products-prices/how-products-and-prices-work),
and [coupons](https://docs.stripe.com/billing/subscriptions/coupons) that you
create into the following NetSuite items:

- **Price**: Associated or grouped within a product
- **Coupons**: Used to provide discounts (such as percentage or flat amount) on
an invoice
- **One-time items**: Used for miscellaneous billing charges

Use NetSuite to manage the item configuration, such as account, deferred
revenue, reporting, revenue recognition options, and so on.

## How NetSuite represents products and prices

Products in Stripe are like records that organize groups of price levels. Each
price has a corresponding item in NetSuite, while a product (or group of prices)
isn’t represented in NetSuite.

The connector can represent Stripe prices in NetSuite in three ways:

- **Every price in Stripe creates a unique NetSuite item.** This method provides
detailed reporting and control over revenue recognition and revenue accounts for
each Stripe price. Because this method adds more entries to your item master,
it’s a good fit for businesses with a moderate number of items (less than 100)
created each day. If you receive a very high volume of entries (hundreds per
day), this can impact the connector’s ability to sync other monetary
transactions.
- **All prices use a single global NetSuite item.** This method posts every
price in Stripe to a single revenue account in NetSuite. This method keeps your
item master simple. With this method, you can’t customize revenue recognition
across different prices.

#### Note

To use this method, ask your implementation partner to enable the **Enable
global item workflow** feature in your Stripe app settings. Consult with your
implementation partner to understand all accounting and technical implications.
- **Customize Stripe prices to use specific items in NetSuite.** To set specific
prices to NetSuite items, you can either use the connector’s product to item
matching system or add metadata to the price programmatically. If you receive a
very high volume of entries (hundreds per day), this can impact the connector’s
ability to sync transactions.

### Product to item matching system

When you use the connector, the product to item matching system works as
follows:

- The product to item matching system compares the fields you specify on a
Stripe price and a NetSuite item to identify matching values. Whitespace and
capitalization don’t affect the matching process.
- If the system finds multiple matches, the connector chooses the first match
found.
- If the system doesn’t find a match, the connector does one of the following,
depending on your settings:

- Creates a new, unique item in NetSuite for the Stripe price (default)
- Uses a generic Stripe item

The system can only link certain item types and must match on the full data
contained in each field. It can’t match partial data or strings that contain the
data. For example, the connector can’t match a NetSuite field that contains an
ID of `12345` with Stripe metadata that contains `Item ID 12345` because the
NetSuite field is missing `Item ID`.

#### Note

Using the price matching setting overrides the method of adding the
`netsuite_service_sale_item_id` [metadata
key](https://docs.stripe.com/connectors/netsuite/custom-payment-application#metadata-keys)
to the price object.

### Add metadata to the Stripe price

You can programmatically [add
metadata](https://docs.stripe.com/connectors/netsuite/custom-payment-application#stripe-metadata)
to the price object to specify which NetSuite item the connector can use on the
invoice in NetSuite.

When creating an invoice item using the API, you can create a one-time price
that’s used for a single invoice and then automatically archived. Pass the
[price_data](https://docs.stripe.com/api/invoiceitems/create#create_invoiceitem-price_data)
and include a product ID. The system uses product-to-item matching for one-time
prices; you can’t use metadata to specify which item to use in NetSuite.

#### Note

Ask your implementation partner about item mapping, which allows you to map
existing Stripe prices to NetSuite items.

## How NetSuite represents coupons

[Coupons](https://docs.stripe.com/billing/subscriptions/coupons) in Stripe are
represented as non-posting discount items that are applied to items in NetSuite.
The connector supports multiple discounts on the invoice level and invoice line
item level.

The connector can represent Stripe coupons in NetSuite in three ways:

- **Every coupon creates a unique NetSuite discount item.** This method provides
detailed reporting for each Stripe coupon, but adds more entries to your item
master.
- **All coupons use a single global NetSuite item.** This method posts every
coupon in Stripe to a single item in NetSuite. This method keeps your item
master simple.

#### Note

To use this method, ask your implementation partner to enable the **Enable
global discount workflow** feature in your Stripe app settings. Consult with
your implementation partner to understand all accounting and technical
implications.
- **Customize Stripe coupons to use specific discount items in NetSuite.** You
can have specific coupons use specific discount items by programmatically adding
metadata to the coupon before it’s used. If there’s no metadata present for a
used coupon, the connector does one of the following, depending on your
settings:

- Creates a new, unique coupon (default)
- Uses a global discount item

### Use coupons with revenue recognition

Coupons don’t have a revenue period. For revenue recognition, coupons are
created as non-posting discounts, by default. This means the discount amount is
subtracted from the total revenue recognized for the item it’s applied to.

#### Note

To use this setting, ask your implementation partner to set the field mapping
**Field defaults** in your Stripe app settings with the following JSON:
`"discount_item": { "non_posting": true }`.

### Post discounts

You can create discounts as posting items. If your business later requires
revenue recognition, you must modify the connector to make discounts
non-posting. Coupons that are created as posting discounts can cause problems
with revenue recognition calculation.

### Stripe coupons and NetSuite discounts

There are some notable differences between Stripe coupons and NetSuite
discounts:

- Because the NetSuite discount model differs from Stripe, a coupon line is
reflected in NetSuite as its own line.
- While each discount is its own line in NetSuite, in Stripe you can apply
multiple discounts to a single line item.
- A single line item in Stripe can result in multiple NetSuite line items.
- You can’t add a discount directly to a credit note line item in Stripe. The
discount can only be inherited from the parent invoice.

## Change the default account for a NetSuite item

When creating an item in NetSuite, the connector uses a default income account.
You can modify the income account for the NetSuite item at any time in the
**Account mapping** > **Income** section of your Stripe app settings. Changes to
the NetSuite item’s configurations won’t affect the connector’s link between the
price and the item.

For example, the connector creates an item that posts to the wrong incoming
account. You can modify the item in NetSuite to change the income or deferred
revenue account.

You can’t modify the income account for an item if it contains a transaction
from a closed accounting period. You also can’t modify a discount item after
it’s used on a transaction.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)

## Links

-
[products](https://docs.stripe.com/products-prices/how-products-and-prices-work)
- [coupons](https://docs.stripe.com/billing/subscriptions/coupons)
- [metadata
key](https://docs.stripe.com/connectors/netsuite/custom-payment-application#metadata-keys)
- [add
metadata](https://docs.stripe.com/connectors/netsuite/custom-payment-application#stripe-metadata)
-
[price_data](https://docs.stripe.com/api/invoiceitems/create#create_invoiceitem-price_data)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)