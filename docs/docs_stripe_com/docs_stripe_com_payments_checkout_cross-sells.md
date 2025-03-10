# Cross-sells

## Enable customers to purchase complementary products at checkout by using cross-sells.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview

![Cross-sell product in
Checkout](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-session.32236b96e980634a6c0060050eea5dbf.png)

A cross-sell is a product that you can add to an order using Checkout.

Cross-sells enable customers to optionally purchase other related products using
Checkout. Cross-sells can increase your average order value and revenue. For
Checkout to offer a product as a cross-sell, the product must meet the following
criteria:

- The product must be associated with only a single
[Price](https://docs.stripe.com/api/prices/object#price_object-product).
- The
[currency](https://docs.stripe.com/api/prices/object#price_object-currency) of
the cross-sell product’s price must match the currency of the other prices in
the Checkout Session.
- If the cross-sell product’s price
[type](https://docs.stripe.com/api/prices/object#price_object-type) is
`recurring`, the Checkout Session must be in subscription mode and its recurring
interval must match the recurring interval of the other prices in the Checkout
Session.
- If you’re using [subscription
upsells](https://docs.stripe.com/payments/checkout/upsells), cross-sells only
support products with non-recurring prices. For example, you can cross-sell a
one-time setup fee while also upselling a monthly subscription to annual
billing.
- If you’re using [automatic taxes](https://docs.stripe.com/tax), cross-sells
only support products with prices with specified [tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior).
You can either [set tax behavior for a
price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional))
or set the default tax behavior for all prices under [Tax
Settings](https://dashboard.stripe.com/test/settings/tax) in the Stripe
Dashboard.

## Create a cross-sell

![Configure a cross-sell on the Product detail
page](https://b.stripecdn.com/docs-statics-srv/assets/add-cross-sell.685564769c217a27f88b9ab9605d9c65.gif)

Configure a cross-sell on the Product detail page.

You can configure a cross-sell in the
[Dashboard](https://dashboard.stripe.com/products?active=true) on the Product
details page. Visit the Product details page for the product from which you want
to cross-sell another complementary product. You’ll see a **Cross-sells**
section with a dropdown menu containing your other Products. Select a Product
with a single Price. After you configure it, all eligible Checkout Sessions
cross-sell the product selected from the dropdown menu. For example, a customer
purchasing a ‘Togethere Professional’ subscription would be cross-sold the
‘Professional Services: Deployment’ product.

## Checkout flow

In Checkout, buyers see an option to add the cross-sell to their purchase. If
buyers add the cross-sell to the Checkout Session, they can also remove it. If
they remove it, the option to add the cross-sell appears again.

#### Note

The quantity of cross-sell line items cannot be adjusted. The current maximum is
1.

![Customer preview of a cross-sell on the Product detail
page](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-preview.cc9b1a4716015a18004f62de760cf29a.gif)

Customer preview.

## Retrieve Checkout Session line items

After a customer adds a cross-sell, the `line_items` for the Checkout Session
update to reflect the addition. When [fulfilling your
order](https://docs.stripe.com/checkout/fulfillment#create-payment-event-handler)
using the `checkout.session.completed` webhook, make sure to [retrieve the line
items](https://docs.stripe.com/api/checkout/sessions/line_items).

## Remove a cross-sell

You can remove a cross-sell on the Product details page. After you remove it,
the product won’t be offered to any new Checkout Sessions.

![Remove a cross-sell from the Product detail
page](https://b.stripecdn.com/docs-statics-srv/assets/remove-cross-sell.a08765b1278a8187c282964f89641b92.gif)

Remove a cross-sell.

## Links

- [Price](https://docs.stripe.com/api/prices/object#price_object-product)
- [currency](https://docs.stripe.com/api/prices/object#price_object-currency)
- [type](https://docs.stripe.com/api/prices/object#price_object-type)
- [subscription upsells](https://docs.stripe.com/payments/checkout/upsells)
- [automatic taxes](https://docs.stripe.com/tax)
- [tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior)
- [set tax behavior for a
price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional))
- [Tax Settings](https://dashboard.stripe.com/test/settings/tax)
- [Dashboard](https://dashboard.stripe.com/products?active=true)
- [fulfilling your
order](https://docs.stripe.com/checkout/fulfillment#create-payment-event-handler)
- [retrieve the line
items](https://docs.stripe.com/api/checkout/sessions/line_items)