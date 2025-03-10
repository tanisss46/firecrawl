# Place hardware orders

## Learn how to place orders for reader hardware and accessories.

Order pre-certified readers compatible with Stripe Terminal from your Dashboard
or using the [Stripe
API](https://docs.stripe.com/terminal/fleet/order-and-return-readers#use-the-hardware-orders-api).
Purchase readers directly from Stripe so they’re loaded with Stripe’s payment
applications and secure encryption keys.

To get started, navigate to the [Readers](https://dashboard.stripe.com/terminal)
section in your Dashboard. Click **Shop** to view available products.

## What to buy

First, order a [reader](https://dashboard.stripe.com/terminal/shop) and a [test
card](https://dashboard.stripe.com/terminal/shop) to test your full integration
with physical hardware. When your integration is ready, order as many readers as
you need.

Not sure which reader you need? See [Designing an
Integration](https://docs.stripe.com/terminal/designing-integration) to choose
one for your integration.

You can order up to 10000 of each item in a single order. If you’re interested
in volume discounts, you can [contact us](https://stripe.com/contact/sales).

### Pricing

The price for each reader varies by country. You can view the most updated
pricing in the [Dashboard](https://dashboard.stripe.com/terminal/shop).

[Stripe Reader
M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2)[BBPOS
WisePOS
E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e)[BBPOS
WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)[Stripe
Reader
S700](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700)

![Stripe Reader
M2](https://b.stripecdn.com/docs-statics-srv/assets/stripem2.bf6a7eabd353369bfa596a81ab51ca9a.png)

![BBPOS WisePOS
E](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-floating-tall.e8478124cda0e088b2e19f503f574f53.png)

![BBPOS WisePad
3](https://b.stripecdn.com/docs-statics-srv/assets/wisepad-floating-thumb.d6e3015116e0b4295b0106e770b9843e.png)

![Stripe Reader
S700](https://b.stripecdn.com/docs-statics-srv/assets/S700-3D.041eca5dfd580cdc451a41020b4dd45a.png)

Australia– 329 AUD 89 AUD 499 AUD Canada– 299 CAD 79 CAD 449 CAD
AustriaFranceGermanyIrelandBelgiumSpainNetherlandsLuxembourgFinlandPortugalItaly–
199 EUR 59 EUR 299 EUR Czech Republic– 4990 CZK 1490 CZK 7250 CZK Malaysia– 999
MYR 279 MYR 1499 MYR New Zealand– 349 NZ 99 NZ 549 NZ Singapore– 299 SGD 89 SGD
449 SGD United Kingdom– 179 GBP 49 GBP 279 GBP Switzerland– 199 CHF 59 CHF 329
CHF Norway– 1990 NOK 590 NOK 3590 NOK Denmark– 1499 DKK 449 DKK 2400 DKK Sweden–
2195 SEK 645 SEK 3490 SEK United States59 USD 249 USD – 349 USD [Shop
now](https://dashboard.stripe.com/terminal/shop) US only [Shop
now](https://dashboard.stripe.com/terminal/shop) [Shop
now](https://dashboard.stripe.com/terminal/shop) Non-US [Shop
now](https://dashboard.stripe.com/terminal/shop)
## Track and cancel orders

After placing an order, check its status in the Dashboard:

StatusDefinitionPendingWe’ve received your order and will fulfill it soon. If
needed, you can cancel this order in the Dashboard. Orders remain pending for at
least 30 minutes.Ready to shipYour order is being prepared to ship and can no
longer be canceled. After the order ships, you must initiate a return to cancel
the order. The order becomes Shipped after a tracking number is
available.ShippedOrder placed with our distributor. Tracking information is
available on the Order details page.DeliveredItems have been
delivered.CanceledThe order is canceled.
Pending

Ready to ship

Canceled

Shipped

Delivered

Undeliverable

v4 order status diagram
## Self service returns

Self service returns are for orders placed and shipped within specific countries
(see countries below). See the information about [returns outside of supported
self service
countries](https://docs.stripe.com/terminal/fleet/order-and-return-readers#returns-outside-of-supported-self-service-countries)
for all other orders.

If you’ve placed an order in the Stripe Dashboard within a country supporting
self service and need to return some or all of the items in your order, [users
with sufficient
permission](https://docs.stripe.com/terminal/fleet/order-and-return-readers#self-service-return-permissions)
can initiate the return within the Stripe Dashboard. We can accept refunds for
orders in original packaging (along with all accessories) within 30 days of the
date of purchase. For returns past 30 days, please contact [Stripe
Support](https://support.stripe.com/contact/login).

Going through the flow in the Dashboard produces a return shipping label. After
you create the return shipping label, you can drop your package off at a local
shipping carrier.

Stripe refunds the payment when our distribution facility receives the package.
For credit cards, the process can take up to 10 days for the funds to be
returned to the bank account.

### Countries supporting self service returns

[Selecting the Return items
Button](https://docs.stripe.com/terminal/fleet/order-and-return-readers#step-1)
To initiate a Dashboard Return, navigate to your Hardware Orders and select the
order you want to return. After you select the order, click **Return items** to
start the process. The **Return items** button is available on the Terminal
order details page if the hardware order has a status of `Shipped` or
`Delivered`.

![Self Service Returns - Step
1](https://b.stripecdn.com/docs-statics-srv/assets/returns-step1.9346efe2a1f1a81856654b99566f5a0b.png)

[Confirming the number of units to be
returned](https://docs.stripe.com/terminal/fleet/order-and-return-readers#step-2)
When the popup opens, select the number of items you’d like to return for each
product in the order (if you have more than one item). We’ll only show the
number of items eligible for return. So, if you previously purchased three items
and returned one, you’ll only be able to select up to two units to return.

![Self Service Returns - Step
2](https://b.stripecdn.com/docs-statics-srv/assets/returns-step2.18d56b1b58d3126dc3174bc2583d3d7b.png)

[Calculating the refund
amount](https://docs.stripe.com/terminal/fleet/order-and-return-readers#step-3)
The popup displays the amount to be refunded after you select the desired number
of items.

Shipping fees are refunded on the first initiated return for a Terminal hardware
order. For example, if you bought three readers and then returned one unit
through a partial refund, then decided to return another unit, the second
Dashboard return shows $0 for shipping fees to be refunded because these fees
were returned in the first attempt.

[Selecting a reason for the
return](https://docs.stripe.com/terminal/fleet/order-and-return-readers#step-4)
Next, you need to select a reason for the return from the dropdown menu.

![Self Service Returns - Step
4](https://b.stripecdn.com/docs-statics-srv/assets/returns-step4.d3e033266dc193ff0b4c666ad6fe48cf.png)

- **Items arrived defective or broken**—Select this option if any of the items
received were damaged or defective.
- **I ordered too many devices**—Select this option if you ordered too many
devices.
- **Device setup is too complicated**—Select this option if getting started with
Stripe Terminal was too complicated or the product didn’t meet your
expectations.
- **Other** - Select this option if none of the above options match your use
case. A reason is required.
[Confirming and exporting the shipping
label](https://docs.stripe.com/terminal/fleet/order-and-return-readers#step-5)
After you’ve confirmed the information is correct, select **Submit return’**—the
option to download the shipping label appears after you select it. You can
select **View UPS Locations** to find the nearest drop off location.

![Self Service Returns - Step
5](https://b.stripecdn.com/docs-statics-srv/assets/returns-step5.bd0eff6b670cad01b97216f4a32ad627.png)

[Refunds](https://docs.stripe.com/terminal/fleet/order-and-return-readers#step-6)
After the return is processed, you’ll be redirected back to the order details
page. You can download the shipping label again from the details page if needed.
Stripe issues a refund to the payment method you provided when we receive the
return.

## Returns outside of supported self service countries

To return a device where self service returns isn’t available, contact support.
Navigate to your order in the Dashboard and click **Contact support** to
automatically send us your order details. We can accept refunds for orders in
original packaging (along with all accessories) within 30 days of the date of
purchase.

## Shipping

Stripe works with a distribution partner to fulfill Terminal orders. You can
choose standard, express, or priority shipping, depending on the destination
country. Hardware must be shipped to physical addresses (not PO boxes).

If you’re a [Connect platform using
Terminal](https://docs.stripe.com/terminal/features/connect), you can ship
readers directly to your connected accounts by specifying the destination
address during checkout.

Destination countryOrders cutoff timeOrder amount above which signature is
requiredExcluded regions and territories for shipping (all P.O. boxes are
excluded)United States11:00am Eastern Time500 USDVirgin Islands and military
addressesCanada1:00pm Pacific Time400 CAD–Austria11:00am Central European
Time400 EUR–Belgium11:00am Central European Time400 EUR–Czech Republic11:00am
Central European Time9900 CZK–Denmark11:00am Central European Time2975
DKK–Finland11:00am Central European Time400 EUR–France11:00am Central European
Time400 EURSaint-Pierre and Miquelon, Saint Barthélemy, French Southern
Territories, Wallis and Futuna, French Polynesia and New CaledoniaGermany11:00am
Central European Time400 EUR–Ireland11:00am Central European Time400
EUR–Italy11:00am Central European Time400 EUR–Luxembourg11:00am Central European
Time400 EUR–Netherlands11:00am Central European Time400 EURAruba, Curaçao, Sint
Maarten, Bonaire, Sint Eustatius, and SabaNorway11:00am Central European Time400
EURSvalbard and Jan MayenPortugal11:00am Central European Time400
EUR–Spain11:00am Central European Time400 EUR–Sweden11:00am Central European
Time4315 SEK–Switzerland11:00am Central European Time400 EUR–United
Kingdom11:00am Central European Time400 GBPJersey, Guernsey, Isle of Man, and
the British Virgin IslandsAustralia11:00am Australian Eastern Time400
AUD–Malaysia11:00am Australian Eastern Time1200 MYR–New Zealand11:00am
Australian Eastern Time400 NZD–Singapore11:00am Australian Eastern Time400 SGD–
## User roles and permissions

The following table shows which [user
roles](https://docs.stripe.com/get-started/account/teams/roles) can place orders
on behalf of their account via the dashboard:

AdministratorDeveloperAnalystSupport SpecialistView OnlyPlace new orders View
list of orders Cancel an order Self service return
## Use the Hardware Orders API Preview

You can use the Hardware Orders API if you’d like to: The Terminal Hardware
Orders API enables you to programmatically purchase Terminal readers and
accessories that can be sent directly to your users. Orders are fulfilled by
Stripe’s distribution partners, so you don’t have to manage complex logistics
and can instead focus on building your in-person payments business.

- Build an internal tool for your employees, such as store managers, to place
orders for hardware
- Build an e-commerce ordering system for your customers to place orders for
Terminal readers and accessories

To create a hardware order using the API, follow these steps:

- Retrieve available SKUs
- Retrieve available Shipping Methods
- *(Optional)* Preview the order
- Create the order

#### Private preview

You must include a beta header in your API requests with your API version and
the current version of the terminal hardware order preview: `Stripe-Version:
2025-02-24.acacia;terminal_hardware_orders_beta=v5`

### Retrieve SKUs

To render an appropriate product page for users, your integration must request
available items from Stripe. Each item is represented as a SKU and includes
details about the product, such as the product token and price.

Each SKU is associated with a country: a reader available in the US has a
different SKU from the same reader that’s available in Canada. To retrieve SKUs,
you must specify the `country` parameter when making a request to the [Hardware
Order SKUs](https://docs.stripe.com/api/terminal/hardware_skus/list) endpoint:

```
curl https://api.stripe.com/v1/terminal/hardware_skus?country=US \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5"
```

Each SKU is also associated with a [Hardware
Product](https://docs.stripe.com/api/terminal/hardware_products/object).
Products represent different categories of devices. If you’re building an
e-commerce ordering system for your customers, make sure you only show the SKUs
for the products that apply for your Terminal integration. For example, if your
Terminal integration only uses the [BBPOS WisePOS
E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e), don’t make the
[BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt) reader available
for purchase. To retrieve all [BBPOS WisePOS
E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e) SKUs, you can
specify the optional `product` parameter when making a request to the [Hardware
Order SKUs](https://docs.stripe.com/api/terminal/hardware_skus/list) endpoint:

```
curl
'https://api.stripe.com/v1/terminal/hardware_skus?country=US&product={{TERMINAL_HARDWARE_PRODUCT_ID}}'
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5"
```

#### SKUs availability

SKUs and Products might become obsolete as we replace them with newer hardware.
To help you manage planned obsolescence, see the [SKU and Product
status](https://docs.stripe.com/api/terminal/hardware_skus/object#terminal_hardware_sku_object-status)
that indicates which are currently `available` or `unavailable`. You can’t
create an Order if the [SKU
status](https://docs.stripe.com/api/terminal/hardware_products/object#terminal_hardware_sku_object-status)
is `unavailable`.

Additionally, each SKU and Product has an optional [unavailable_after
field](https://docs.stripe.com/api/terminal/hardware_skus/object#terminal_hardware_sku_object-unavailable_after)
that indicates when it might become `unavailable`. Because the availabilities of
these objects change over time, we recommend using an approach to query them
dynamically. You can do this either by making a query before displaying the
`available` objects to your users, or periodically (every day, for example) and
caching the results you present to your users.

We don’t recommend hardcoding the tokens for these objects because such an
integration requires code changes when a shipping method becomes `unavailable`.
If you don’t perform these changes in time, you might attempt to place orders
with `unavailable` objects, causing errors.

### Retrieve Shipping Methods

Another required object used as an input for creating an order is the [Hardware
Shipping
Method](https://docs.stripe.com/api/terminal/hardware_shipping_methods/object).
This object determines the estimated shipping time for your order as well as a
portion of the price. You must use a Shipping Method available in country of the
shipping address when creating an order.

Like SKUs, each Shipping Method is associated with a country: the shipping
methods available in the US might be different from those available in Canada.
Each Shipping Method also has a `name`, which denotes the basic category for
this shipping method. To retrieve Shipping Methods, you must specify the
`country` and can optionally specify the `name` parameter when making a request
to the [Hardware Shipping
Methods](https://docs.stripe.com/api/terminal/hardware_shipping_methods/list)
endpoint:

```
curl https://api.stripe.com/v1/terminal/hardware_shipping_methods?country=US \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5"
```

Like SKUs and Products, Shipping Methods might change over time. To help you
manage these changes, each Shipping Method has a
[status](https://docs.stripe.com/api/terminal/hardware_skus/object#terminal_hardware_sku_object-status)
that indicates whether it’s currently `available` or `unavailable`. This
mechanism works the same way as it does for SKUs and Products, as described
above. As with SKUs and Products, we recommend fetching Shipping Methods
periodically so your integration doesn’t become out of date.

### Preview a hardware order

To preview a hardware order, make a request to Stripe containing the SKUs,
quantities, shipping address, and Shipping Method for the order.

```
curl https://api.stripe.com/v1/terminal/hardware_orders/preview \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5" \
 --data-urlencode "shipping[name]"="Jenny Rosen" \
 --data-urlencode "shipping[address][line1]"="1234 Main Street" \
 --data-urlencode "shipping[address][city]"="San Francisco" \
 --data-urlencode "shipping[address][state]"=CA \
 --data-urlencode "shipping[address][country]"=US \
 --data-urlencode "shipping[address][postal_code]"=94111 \
 --data-urlencode "shipping[company]"="Rocket Rides" \
 --data-urlencode "shipping[phone]"=15555555555 \
 --data-urlencode "shipping[email]"="test@example.com" \
 --data-urlencode shipping_method=thsm_MfuTjLaPEgXMa4 \
 --data-urlencode payment_type=monthly_invoice \
--data-urlencode
"hardware_order_items[][terminal_hardware_sku]"=thsku_JokaJ6KpLMlDID \
 --data-urlencode "hardware_order_items[][quantity]"=2 \
 -G
```

Previewing an order allows you to perform validation on the order and determine
the overall cost of the taxes associated with the order without actually placing
it, which you can use for designing an e-commerce checkout page for your
customers. Calling the preview endpoint doesn’t actually create an order.

Try to minimize the time between making a request to [Preview Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/preview) and [Create
Hardware Order](https://docs.stripe.com/api/terminal/hardware_orders/create) to
reduce the (very unlikely) chance that prices change in the interim. If you’re
concerned about this issue you can save the preview and create an order using
the same parameters. Then you can compare the saved preview with the order and
cancel the order in the event of any changes.

### Create a hardware order

To create a [Terminal Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/object), you can
make a [Create Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/create) request to
Stripe that looks very similar to the [Preview Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/preview) request.
Include the SKUs, quantities, shipping address, and Shipping Method for the
order in your request.

```
curl https://api.stripe.com/v1/terminal/hardware_orders \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5" \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"="1234 Main Street" \
 -d "shipping[address][city]"="San Francisco" \
 -d "shipping[address][state]"="CA" \
 -d "shipping[address][country]"="US" \
 -d "shipping[address][postal_code]"="94111" \
 -d "shipping[company]"="Rocket Rides" \
 -d "shipping[phone]"="15555555555" \
 -d "shipping[email]"="test@example.com" \
 -d "hardware_order_items[][terminal_hardware_sku]"="thsku_JokaJ6KpLMlDID" \
 -d "hardware_order_items[][quantity]"="2" \
 -d shipping_method="thsm_MfuTjLaPEgXMa4" \
 -d payment_type="monthly_invoice"
```

The below example shows a US phone number. If the phone number provided by
`shipping.phone` parameter is an international phone number, prefix it with an
escaped version of the + sign (for example: `shipping[phone]="%2B358131234567"`
instead of `shipping[phone]="+358131234567"`).

The email address provided by the `shipping.email` parameter receives
Stripe-branded update emails when the status of the order changes. Use an email
address that you feel comfortable receiving Stripe-branded emails.

### Retrieve and query hardware orders

After creating an order, you can [Retrieve a Terminal Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/retrieve) using the
following request.

```
curl
https://api.stripe.com/v1/terminal/hardware_orders/{{TERMINAL_HARDWARE_ORDER_ID}}
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5"
```

You can also [List all Terminal Hardware
Orders](https://docs.stripe.com/api/terminal/hardware_orders/list).

```
curl https://api.stripe.com/v1/terminal/hardware_orders \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5"
```

### Webhooks

You can [set up webhook events](https://docs.stripe.com/webhooks) to be updated
about order state transitions. You must add a header version (for example,
`Stripe-Version: 2025-02-24.acacia;terminal_hardware_orders_beta=v5`) to your
webhook endpoints to receive events properly. We support the following webhook
events:

- `terminal_hardware_order.created`
- `terminal_hardware_order.canceled`
- `terminal_hardware_order.ready_to_ship`
- `terminal_hardware_order.shipped`
- `terminal_hardware_order.delivered`
- `terminal_hardware_order.undeliverable`

### Update a test mode order status

You can update the status of a terminal hardware order in test mode using the
following endpoints in the API:

- `/v1/test_helpers/terminal/hardware_orders/:hardware_order/mark_ready_to_ship`
- `/v1/test_helpers/terminal/hardware_orders/:hardware_order/ship`
- `/v1/test_helpers/terminal/hardware_orders/:hardware_order/deliver`
- `/v1/test_helpers/terminal/hardware_orders/:hardware_order/mark_undeliverable`

You can only update the status for terminal hardware orders in [test
mode](https://docs.stripe.com/keys#test-live-modes).

### Taxes

Upon order creation, Stripe returns the tax amounts associated with the order.
We calculate these amounts based on the tax owed to Stripe for the purchase. If
you charge tax to your end users for orders placed using the API, you can
calculate the amounts owed to you and convey those amounts to your users. The
amounts owed to you might differ from those owed to Stripe.

For Italian Tax Invoices, please visit the [Italian Tax
Portal](https://www.agenziaentrate.gov.it/portale/area-riservata) to view
invoices.

### Invoices

During preview, Stripe sends monthly invoices for any orders created with the
API. You can change the email that receives invoices in the
[Dashboard](https://dashboard.stripe.com/settings/terminal).

### Shipment Tracking

As mentioned in the
[Shipping](https://docs.stripe.com/terminal/fleet/order-and-return-readers#shipping)
section, Stripe works with a distribution partner to fulfill Terminal orders.
When our distribution partner gets tracking information for the order it
transions to the `shipped` state. You can set up a webhook endpoint for the
`terminal_hardware_order.shipped` notification to be notified when an order has
a tracking number.

### Changelog

#### New carriers

- Add new values (`canada_post`, `dhl`, `dpd`, and `usps`) to the
[Carrier](https://docs.stripe.com/api/terminal/hardware_orders/object#terminal_hardware_order_object-shipment_tracking-carrier)
enum field.

#### v5 (2024-11-25)

- Add pagination to the [List all Terminal Hardware
SKUs](https://docs.stripe.com/api/terminal/hardware_skus/list), [List all
Terminal Hardware
Products](https://docs.stripe.com/api/terminal/hardware_products/list), and
[List all Terminal Hardware Shipping
Methods](https://docs.stripe.com/api/terminal/hardware_shipping_methods/list)
endpoints.
- Require the `country` filter for the [List all Terminal Hardware
SKUs](https://docs.stripe.com/api/terminal/hardware_skus/list) and [List all
Terminal Hardware Shipping
Methods](https://docs.stripe.com/api/terminal/hardware_shipping_methods/list)
endpoints.

#### v4 (2023-01-23)

- Add a new [Preview Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/preview) endpoint.
Remove `draft` and `expired` order statuses. Remove the
`/v1/terminal/hardware_orders/confirm` endpoint and the `confirm` parameter in
the [Create Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/create) endpoint.
- Add a new
[TerminalHardwareOrder](https://docs.stripe.com/api/terminal/hardware_orders/object)
status called `ready_to_ship`, which represents a state in which the order is no
longer cancelable, but hasn’t yet shipped.
- Add new API endpoints to update the status of test mode terminal hardware
orders to
[ready_to_ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_ready_to_ship),
[shipped](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_ship),
[delivered](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_deliver),
and
[undeliverable](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_undeliverable).
- Add a new [Hardware Shipping
Method](https://docs.stripe.com/api/terminal/hardware_shipping_methods/object)
object to replace the former object in the `shipping_method` field, as well as
API endpoints for querying and retrieving these new objects.
- Add a new [Hardware
Product](https://docs.stripe.com/api/terminal/hardware_products/object) object
to replace the former `product_type` field, as well as API endpoints for
querying and retrieving these new objects.
- Add a new, dynamic `orderable` field to the
[TerminalHardwareSku](https://docs.stripe.com/api/terminal/hardware_skus/object)
object, replacing the older `max_per_order` field.
- Add `status` and `unavailable_after` fields to
[TerminalHardwareSku](https://docs.stripe.com/api/terminal/hardware_skus/object),
which allow you to determine if and when a SKU becomes unavailable to order.
These fields also exist on the new [Hardware Shipping
Method](https://docs.stripe.com/api/terminal/hardware_shipping_methods/object)
and [Hardware
Product](https://docs.stripe.com/api/terminal/hardware_products/object) objects.
- If you have webhooks enabled for v3 and v4 under the same mode (that is, both
test mode or both live mode) at the same time, then Stripe sends the
`terminal_hardware_order.shipped` webhook twice. We send the
`terminal_hardware_order.shipped` webhook when an order transitions to
`ready_to_ship` and `shipped` as opposed to only sending it when an order
transitions to `shipped`. Having v3 in live mode and v4 in test mode doesn’t
cause duplicate webhooks. If you need to have both v3 and v4 active under the
same mode at the same time, make sure to update your integration to handle
duplicate `terminal_hardware_order.shipped` webhooks first.
- Orders that are `ready_to_ship` in v4 appear as `shipped` in v3. You might see
an order with status `shipped` in v3 and `ready_to_ship` in v4 as you’re
updating your migration. This happens because the `ready_to_ship` concept
doesn’t exist in v3; the status of these orders doesn’t actually regress.

#### v3 (2019-04-03) Deprecated

- Update [Terminal Hardware
SKU](https://docs.stripe.com/api/terminal/hardware_skus/object) and the
[Terminal Hardware Order line item SKU
object](https://docs.stripe.com/api/terminal/hardware_orders/object#terminal_hardware_order_object-hardware_order_items-terminal_hardware_sku)
by removing text fields such as `name`, `description`, `images`, and
`attributes`.
- Make the `shipping_country` query parameter in [Hardware Order
SKUs](https://docs.stripe.com/api/terminal/hardware_skus/list) optional and
rename it to `country`.
- Add the ability to query SKUs in the API by `product_type` and `country`.

#### v2 (2019-12-20) Deprecated

- Update [Terminal Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/object) by turning
`total_tax_amounts.rate.jurisdiction` from a structured object into a string.

#### v1 (2019-11-20) Deprecated

- Initial release

## Links

- [available readers and
accessories](https://dashboard.stripe.com/terminal/shop)
- [Stripe
API](https://docs.stripe.com/terminal/fleet/order-and-return-readers#use-the-hardware-orders-api)
- [Readers](https://dashboard.stripe.com/terminal)
- [Designing an
Integration](https://docs.stripe.com/terminal/designing-integration)
- [contact us](https://stripe.com/contact/sales)
- [Stripe Reader
M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2)
- [BBPOS WisePOS
E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e)
- [BBPOS WisePad
3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700)
- [returns outside of supported self service
countries](https://docs.stripe.com/terminal/fleet/order-and-return-readers#returns-outside-of-supported-self-service-countries)
- [Stripe Support](https://support.stripe.com/contact/login)
- [Connect platform using
Terminal](https://docs.stripe.com/terminal/features/connect)
- [user roles](https://docs.stripe.com/get-started/account/teams/roles)
- [Hardware Order SKUs](https://docs.stripe.com/api/terminal/hardware_skus/list)
- [Hardware
Product](https://docs.stripe.com/api/terminal/hardware_products/object)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)
- [SKU and Product
status](https://docs.stripe.com/api/terminal/hardware_skus/object#terminal_hardware_sku_object-status)
- [SKU
status](https://docs.stripe.com/api/terminal/hardware_products/object#terminal_hardware_sku_object-status)
- [unavailable_after
field](https://docs.stripe.com/api/terminal/hardware_skus/object#terminal_hardware_sku_object-unavailable_after)
- [Hardware Shipping
Method](https://docs.stripe.com/api/terminal/hardware_shipping_methods/object)
- [Hardware Shipping
Methods](https://docs.stripe.com/api/terminal/hardware_shipping_methods/list)
- [Preview Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/preview)
- [Create Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/create)
- [Terminal Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/object)
- [Retrieve a Terminal Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders/retrieve)
- [List all Terminal Hardware
Orders](https://docs.stripe.com/api/terminal/hardware_orders/list)
- [set up webhook events](https://docs.stripe.com/webhooks)
- [test mode](https://docs.stripe.com/keys#test-live-modes)
- [Italian Tax Portal](https://www.agenziaentrate.gov.it/portale/area-riservata)
- [Dashboard](https://dashboard.stripe.com/settings/terminal)
-
[Carrier](https://docs.stripe.com/api/terminal/hardware_orders/object#terminal_hardware_order_object-shipment_tracking-carrier)
- [List all Terminal Hardware
Products](https://docs.stripe.com/api/terminal/hardware_products/list)
-
[ready_to_ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)
- [shipped](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_ship)
-
[delivered](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_deliver)
-
[undeliverable](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_undeliverable)
-
[TerminalHardwareSku](https://docs.stripe.com/api/terminal/hardware_skus/object)
- [Terminal Hardware Order line item SKU
object](https://docs.stripe.com/api/terminal/hardware_orders/object#terminal_hardware_order_object-hardware_order_items-terminal_hardware_sku)