# Products and prices

## Learn about syncing your products and prices between Salesforce and Stripe.

When you create products and prices in Salesforce, they don’t sync to Stripe
immediately. Instead, the products and prices sync to Stripe when they’re used
in an activated order. You don’t need to manually create this information in
Stripe.

Salesforce is the primary source for product and pricing information. This means
all pricing, product descriptions, SKUs, and so on sync from Salesforce to
Stripe. Any updates you make to this information in Stripe won’t update the
related products and prices in Salesforce. Additionally, if you activate a new
order in Salesforce using updated product or pricing information, this action
updates corresponding changes you’ve made in Stripe.

## Create prices

Pricing data can come from either the Salesforce `OrderItem` or the linked
`PricebookEntry`. When creating the Stripe price, the connector checks for
differences between these Salesforce objects and decides which one to use. If
the `PricebookEntry` data differs from the `OrderItem` data, the connector uses
the `OrderItem` to create the Stripe price. Otherwise, the connector uses the
`PricebookEntry`.

### Reuse Stripe prices

The Stripe Billing Connector for Salesforce CPQ reuses the prices created from a
`PricebookEntry` that the connector previously synced. The connector creates a
new price for prices generated using the `OrderItem`. You can’t reuse order
items because they’re unique, but you can reuse pricebook entries across
multiple order items. In both cases, the corresponding Stripe price ID is
written back to the Salesforce object.

## Field mappings for products

The Stripe Billing Connector for Salesforce CPQ creates a product in Stripe even
if there isn’t relevant data in Salesforce. All product fields are optional.

Salesforce field (Product2 object)Stripe
productName[Name](https://docs.stripe.com/api/products/object#product_object-name)Description[Description](https://docs.stripe.com/api/products/object#product_object-description)
## Field mappings for prices

The connector supports the following price types in Stripe:

- Licensed prices – If the Billing Type (`SBQQ_BillingType_c`) field in
Salesforce is either None or Advanced, the connector creates a licensed price in
Stripe.
- Metered or usage prices – If the Billing Type (`SBQQ_BillingType_c`) field in
Salesforce is Arrears, the connector creates a metered or usage price.
- Decimal prices – If the decimal value of your price has more precision than 12
decimal places, the connector rounds your price to 12 decimals.
- One-time and recurring prices – The connector treats any product with
populated subscription fields as a recurring price. Metered prices must be
recurring, but you can have tiered one-time prices. If you want to create a
one-time price, don’t set the following fields on the Salesforce product:-
Subscription Pricing (`SBQQ__SubscriptionPricing__c`)
- Subscription Type (`SBQQ__SubscriptionType__c`)
- Subscription Term (`SBQQ__SubscriptionTerm__c`)
- Billing Frequency (`SBQQ__BillingFrequency__c`)
Salesforce field (PricebookEntry object)Stripe
priceNotesRequiredProduct[Product](https://docs.stripe.com/api/products/object)Maps
the Stripe `Product` object that’s linked to the Salesforce `Product` and
`Pricebook` objects with the corresponding `Price` object in
Stripe.Description[Description](https://docs.stripe.com/api/products/object#product_object-description)Unit
price[Unit amount
decimal](https://docs.stripe.com/api/prices/object#price_object-unit_amount_decimal)Represents
the amount billed to the customer at the frequency specified in the `Billing
Frequency` field.Billing frequency[Recurring, interval
count](https://docs.stripe.com/api/prices/create#create_price-recurring-interval_count)Required
for recurring prices only. Supported values include monthly, quarterly, semi
annual, and annual. These values map to the integer-equivalent.Billing
type[Recurring, usage
type](https://docs.stripe.com/api/prices/create#create_price-recurring-usage_type)Required
for recurring prices only. An Arrears value maps to metered. An Advanced value
maps to licensed.CPQ global term unit setting[Recurring,
interval](https://docs.stripe.com/api/prices/create#create_price-recurring-interval)Required
for recurring prices only. This is chosen during setup and isn’t a field-level
mapping.Currency[Currency](https://docs.stripe.com/api/prices/create#create_price-currency)If
your Salesforce organization has multi-currency enabled, we map the
`CurrencyIsoCode` on the `PricebookEntry` to a Stripe currency. Otherwise, we
use the default currency from setup.
### Tiered pricing using consumption schedules

You can configure tiered pricing in Stripe by setting up a Salesforce
Consumption Schedule–and associated rates–for products in Salesforce. Stripe
uses the consumption schedule to associate tiered pricing with the line items
billed using metered or licensed billing. You can use only one consumption
schedule per order line.

Stripe Billing requires an unbounded tier to exist, which means a consumption
rate with no value for the upper bound. The connector doesn’t use the processing
order on a consumption rate, or the billing term and billing term unit on the
consumption schedule associated with the order product. The connector uses the
billing frequency and subscription term on the order line instead.

For tiered pricing, the connector maps data from the following Salesforce
objects:

- `OrderLine` – If the `OrderLine` data differs from the corresponding
`PricebookEntry`, the connector uses the `OrderLine` data and creates a new
`Price` object in Stripe.
- `PricebookEntry` – The connector uses this value if the pricing data matches
the `OrderLine` and the consumption schedule and rate data aren’t customized on
a per-customer basis.
- `Consumption Schedule` – Although Salesforce allows you to associate multiple
consumption schedules with a product, the connector supports only one
consumption schedule per order line.
- `Consumption Rate` – The connector uses the rate associated with a consumption
schedule to define each tier entry in the Stripe price. You can have multiple
rates for a consumption schedule.

#### Note

You can’t customize the field mapping to generate the tiered pricing
configuration in Stripe, or use custom fields for price or tier boundaries.

If you customize the consumption schedule and consumption rate data on a
per-customer basis, Stripe creates a new `Price` object to represent the
customized pricing. The new price appears in the Stripe ID field on the `Order
Line` object in Salesforce.

To define a mapping for tiered pricing, add the following `PricebookEntry` to
your prices field mapping. These fields are required.

Salesforce field (PricebookEntry object)Stripe priceNotes[Billing
scheme](https://docs.stripe.com/api/prices/create#create_price-billing_scheme)Set
to tiered when an order line in Salesforce has a consumption schedule associated
with it.Salesforce consumption scheduleStripe priceNotesType[Tiers
mode](https://docs.stripe.com/api/prices/object#price_object-tiers_mode)A slab
type uses graduated. A range type uses volume.
Each consumption rate that’s associated with a consumption schedule results in
an additional tiers entry on the Stripe `Price` object. These fields are
required.

Salesforce consumption rateStripe priceNotesUpper bound[Tiers, Up
to](https://docs.stripe.com/api/prices/object#price_object-tiers-up_to)Stripe
doesn’t have a lower bound and assumes the lower bound value of the first tier
is zero. If this value is empty in Salesforce, Stripe uses the inf value to
indicate there isn’t a limit for the upper bound.Pricing methodA per unit value
instructs the connector to use the `unit_amount_decimal` field when mapping the
price. If the value is flat fee, the connector uses the `flat_amount_decimal`
field for the price.PriceTiers, [Flat amount
decimal](https://docs.stripe.com/api/prices/object#price_object-tiers-flat_amount_decimal)
or [Unit amount
decimal](https://docs.stripe.com/api/prices/object#price_object-tiers-unit_amount_decimal)The
pricing type used depends on the `Pricing Method` field.
## Manually sync products and prices

When testing in a Salesforce sandbox environment, you can manually sync your
entire product catalog for inspection in your Stripe test account. The manual
sync respects any product and price filters you set.

Use the following buttons in the **Settings** section of the connector:

- **Sync all products** – Syncs all products (but not prices) to your Stripe
test account, regardless of when they were last updated. This operation occurs
in the background and can take a couple minutes to complete. If you delete any
products in Salesforce, they aren’t deleted or archived in Stripe.
- **Sync a pricebook** – Manually sync a `PricebookEntry` to your Stripe test
account by entering the record ID into the Manual Sync functionality. This
operation occurs in the background. If you delete any prices in Salesforce, they
aren’t deleted or archived in Stripe. After you create a price and set a
recurring billing schedule in Stripe, you can’t update these parameters and sync
them from Salesforce. Attempting to do so results in sync errors.

If you already synced a product or price to your Stripe account and want a new
sync, you can delete the contents of the Stripe ID field on the Salesforce
object in your Salesforce account. Then sync again to create a new resource in
Stripe.

## Customize product pricing on orders

In the Salesforce CPQ, you can optionally customize the unit price of a product
on a quote. If you customize the price, this causes the information to differ
from the price that’s linked to the product on the activated order. In this
case, the connector creates a unique price in Stripe to represent the customized
price. The Stripe price ID appears on the Stripe ID field for the order.

When you create a data mapping with a customized price for an order, the price
appears on the order line level and not the Salesforce price book entry level.
Pricing is considered customized if any of the related fields (for example,
recurring fields, amount, or currency) differ between the price book entry price
and the order line price.

## Multi-currency support

If your Salesforce organization has [multi-currency
enabled](https://help.salesforce.com/s/articleView?id=sf.admin_enable_multicurrency.htm&type=5),
the connector maps the `CurrencyIsoCode` on the `PricebookEntry` to the
equivalent [Stripe currency](https://docs.stripe.com/currencies) during Stripe
price creation. This makes sure subsequent
[invoices](https://docs.stripe.com/api/invoices) are billed in the proper
currency.

When billing in multiple currencies, consider the following:

##### Multiple currencies per Stripe customer

Stripe supports one active currency per customer. This means each Stripe
customer can’t have multiple active
[subscriptions](https://docs.stripe.com/api/subscription) that use different
currencies. For example, if a customer has an active
[subscription](https://docs.stripe.com/api/subscription) that’s billed in USD,
you must wait until that subscription ends before creating a new subscription in
a different currency, such as GBP.

##### Order amendments

All Salesforce order amendments must use the same currency as the original
order. Orders and order amendments can’t have a mix of currencies among the
order items.

##### Exchange rates

The connector doesn’t handle currency conversion. It simply passes through the
price and currency pair found on the `PricebookEntry`.

## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)
- [MDQ products](https://docs.stripe.com/connectors/salesforce-cpq/mdq-products)

## Links

- [Name](https://docs.stripe.com/api/products/object#product_object-name)
-
[Description](https://docs.stripe.com/api/products/object#product_object-description)
- [Product](https://docs.stripe.com/api/products/object)
- [Unit amount
decimal](https://docs.stripe.com/api/prices/object#price_object-unit_amount_decimal)
- [Recurring, interval
count](https://docs.stripe.com/api/prices/create#create_price-recurring-interval_count)
- [Recurring, usage
type](https://docs.stripe.com/api/prices/create#create_price-recurring-usage_type)
- [Recurring,
interval](https://docs.stripe.com/api/prices/create#create_price-recurring-interval)
- [Currency](https://docs.stripe.com/api/prices/create#create_price-currency)
- [Billing
scheme](https://docs.stripe.com/api/prices/create#create_price-billing_scheme)
- [Tiers
mode](https://docs.stripe.com/api/prices/object#price_object-tiers_mode)
- [Tiers, Up
to](https://docs.stripe.com/api/prices/object#price_object-tiers-up_to)
- [Flat amount
decimal](https://docs.stripe.com/api/prices/object#price_object-tiers-flat_amount_decimal)
- [Unit amount
decimal](https://docs.stripe.com/api/prices/object#price_object-tiers-unit_amount_decimal)
- [multi-currency
enabled](https://help.salesforce.com/s/articleView?id=sf.admin_enable_multicurrency.htm&type=5)
- [Stripe currency](https://docs.stripe.com/currencies)
- [invoices](https://docs.stripe.com/api/invoices)
- [subscriptions](https://docs.stripe.com/api/subscription)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)
- [MDQ products](https://docs.stripe.com/connectors/salesforce-cpq/mdq-products)