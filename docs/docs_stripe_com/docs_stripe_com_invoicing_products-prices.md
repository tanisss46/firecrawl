# Products and prices

## Use the Invoicing API to manage products and prices.

Define all your business and product offerings in one place.
[Products](https://docs.stripe.com/api/products) define what you sell and
[Prices](https://docs.stripe.com/api/prices) track how much and how often to
charge. This is a core entity within Stripe that works with
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating),
[invoices](https://docs.stripe.com/api/invoices), and
[Checkout](https://docs.stripe.com/payments/checkout).

Prices enable these use cases:

- A software provider that charges a one-time setup fee whenever a user creates
a new subscription.
- An e-commerce store that sends a recurring box of goods for 10 USD per month
and wants to allow customers to purchase one-time add-ons.
- A professional services firm that can now create a standard list of services
and choose from that list per invoice instead of typing out each line item by
hand.
- A non-profit organization that allows donors to define a custom recurring
donation amount per customer.

You can manage your product catalog with products and prices. Products define
what you sell and prices track how much and how often to charge. Manage your
products and their prices in the Dashboard or through the API.

DashboardAPI
If you used the Dashboard in test mode to set up your business, you can copy
each of your products over to live mode by using ** to live mode** in the
[Product catalog page](https://dashboard.stripe.com/products). Use our official
libraries to access the Stripe API from your application.

- Navigate to the **Product catalog** page, and click **Add product**.
- Select whether you want to create a **One-time product**, or a **Recurring
one-time product**.
- Give your product a name, and assign it a price.

## Links

- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoices](https://docs.stripe.com/api/invoices)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Product catalog page](https://dashboard.stripe.com/products)