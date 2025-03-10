# Charge for shipping

## Create different shipping rates for your customers.

Shipping rates let you display various shipping options—like standard, express,
and overnight—with more accurate delivery estimates. Charge your customer for
shipping using different Stripe products, some of which require coding. Before
you create a shipping rate, learn how to [collect billing and shipping
addresses](https://docs.stripe.com/payments/advanced/collect-addresses).

#### Third-party plugins

If you’re using a third-party application with Stripe (for example,
[Thrivecart](https://support.thrivecart.com/help/setting-your-physical-fulfilment-shipping-options/)
or
[Shopify](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/setting-up-shipping-rates))
and want to adjust the shipping rate, visit the docs for that service.

Stripe Elements doesn’t support calculating or defining shipping rates out of
the box. If you’re in need of this functionality, Stripe recommends building it
yourself or using [Checkout](https://docs.stripe.com/payments/checkout).

If you choose to build this functionality yourself, you can include the shipping
cost as part of the product price or total amount. This means factoring in the
shipping cost when calculating the total price of the items in the cart or
order. By doing so, the customer pays a single amount that includes both the
product price and the shipping cost.

Here’s a basic outline of the steps involved:

- **Determine your shipping cost**: Decide on the shipping cost. Factor in
destination, weight, distance, or any other criteria applicable to your
business.
- **Calculate the total amount**: Add the shipping cost to the price of the
products to calculate the total amount.
- **Integrate Stripe Elements**: Use Stripe Elements to create a checkout form
to collect the customer’s payment information.
- **Present the total amount**: Display the total amount, which includes the
product price and the shipping cost, to the customer on the checkout page.
- **Process the payment**: When the customer submits the payment information,
handle the payment processing in your server-side code.

## Links

- [collect billing and shipping
addresses](https://docs.stripe.com/payments/advanced/collect-addresses)
-
[Thrivecart](https://support.thrivecart.com/help/setting-your-physical-fulfilment-shipping-options/)
-
[Shopify](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/setting-up-shipping-rates)
- [Checkout](https://docs.stripe.com/payments/checkout)