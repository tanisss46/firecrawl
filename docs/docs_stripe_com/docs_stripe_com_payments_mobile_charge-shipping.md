# Charge for shipping

## Create different shipping rates for your customers.

Stripe Elements doesn’t support calculating or defining shipping rates out of
the box. If you’re in need of this functionality, Stripe recommends coding it
yourself or using [Checkout](https://docs.stripe.com/payments/checkout).

If you choose to build this functionality yourself, you can include the shipping
cost as part of the product price or total amount presented to the customer.
This means factoring in the shipping cost when you calculate the total price of
the items in the cart or order. By doing so, the customer pays a single amount
that includes both the product price and the shipping cost.

Here’s a basic outline of the steps involved:

- **Determine your shipping cost**: Decide on the shipping cost. Factor in
destination, weight, distance, or any other criteria applicable to your
business.
- **Calculate the total amount**: Add the shipping cost to the price of the
products to calculate the total amount.
- **Integrate Stripe Elements**: Use the Payment Element to collect the
customer’s payment information.
- **Present the total amount**: Display the total amount, which includes the
product price and the shipping cost, to the customer on the checkout page.
- **Process the payment**: When the customer submits the payment information,
handle the payment processing in your server-side code.

## Links

- [Checkout](https://docs.stripe.com/payments/checkout)