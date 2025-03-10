# One-time payments with CheckoutClient-only integration

## Learn how to accept one-time card payments with just a few lines of code.

With the client-only integration, you define your products directly in the
Stripe Dashboard and reference them by ID on the client side. This approach
makes it possible to integrate Checkout into your website without any
server-side code.

#### Warning

Client-only Checkout doesn’t support many of the features available with a
[client and server
integration](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
and [Payment Links](https://docs.stripe.com/payment-links), which might better
fit your use case.

[Enable
CheckoutDashboard](https://docs.stripe.com/payments/checkout/client#enable-checkout)
To begin using Checkout, log into the Stripe Dashboard and navigate to the
[Checkout settings](https://dashboard.stripe.com/settings/checkout). From here
you can enable the client-only integration and customize the look and feel of
your checkout page.

!

[Create products and
prices](https://docs.stripe.com/payments/checkout/client#create-products-and-prices)
To use Checkout, you first need to create a
[Product](https://docs.stripe.com/api/products) and a
[Price](https://docs.stripe.com/api/prices). Different physical goods or levels
of service should be represented by products. Each product’s pricing is
represented by one or more prices.

For example, you can create a T-shirt *product* that has 2 *prices* for
different currencies: 20 USD and 15 EUR. This allows you to change and add
prices without needing to change the details of your underlying products. You
can either create a product and price [through the
API](https://docs.stripe.com/api/prices) or through [the Stripe
Dashboard](https://dashboard.stripe.com/products).

#### Caution

If you have an existing Checkout integration that doesn’t use Prices, note that
the Checkout API has changed since Prices was introduced. You can use this
[migration guide](https://docs.stripe.com/payments/checkout/migrating-prices) to
upgrade, or [keep your existing
integration](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations).

DashboardAPI
#### Note

Products created in a sandbox can be copied to live mode so that you don’t need
to re-create them. In the Product detail view in the Dashboard, click ** to
live mode** in the upper right corner. You can only do this once for each
product created in a sandbox. Subsequent updates to the test product are not
reflected for the live product.

Make sure you’re in a sandbox, and define the items you want to sell. To create
a new product and price:

- Navigate to the [Products](https://dashboard.stripe.com/test/products) section
in the Dashboard
- Click **Add product**
- Select **One time** when setting the price

The product name, description, and image that you supply are displayed to
customers in Checkout.

[Redirect to
CheckoutDashboardClient-side](https://docs.stripe.com/payments/checkout/client#generate-checkout-button)
To use Checkout on your website, you must add a snippet of code that includes
the desired price. You can use the Dashboard to generate the necessary code, or
you can write it yourself.

DashboardHTML + JSReact
In the [Products section](https://dashboard.stripe.com/products) of the
Dashboard, select the product that you want to sell.

!

In the product detail view, click the **Get Checkout code snippet** selection in
the overflow menu next to a price to generate a code snippet that you can add to
your website.

!

 and paste the snippet into the body of a web page. The snippet adds a
button to the page that, when clicked, redirects the customer to Checkout. You
can include multiple checkout buttons on the same page.

When your customer successfully completes their payment, they’re redirected to
the success URL that you specified when configuring the code snippet. Typically,
this is a page on your website that informs the customer that their payment
succeeded.

When your customer clicks on your logo in a Checkout session without completing
a payment, Checkout redirects them back to your website by navigating to the
cancel URL you specified when configuring the code snippet. Typically, this is
the page on your website that the customer viewed prior to redirecting to
Checkout.

Before going live, make sure to [configure your domains
list](https://dashboard.stripe.com/account/checkout/settings) in the Dashboard
to match the success and cancel URLs.

#### Caution

Don’t rely on the redirect to the `success_url` alone for detecting payment
initiation, as:

- Malicious users could directly access the `success_url` without paying and
gain access to your goods or services.
- Customers may not always reach the `success_url` after a successful
payment—they might close their browser tab before the redirect occurs.
[Confirm the payment is
successful](https://docs.stripe.com/payments/checkout/client#payment-success)
When your customer completes a payment, they’re redirected to the URL that you
specified as the `success_url`. This is typically a page on your website that
informs your customer that their payment was successful.

Use the Dashboard, a custom [webhook](https://docs.stripe.com/webhooks), or a
third-party plugin to handle post-payment events like sending an order
confirmation email to your customer, logging the sale in a database, or starting
a shipping workflow.

DashboardWebhooks
Successful payments appear in the Dashboard’s [list of
payments](https://dashboard.stripe.com/payments). When you click a payment, it
takes you to the payment detail page. The **Checkout summary** section contains
billing information and the list of items purchased, which you can use to
manually fulfill the order.

![Checkout
summary](https://b.stripecdn.com/docs-statics-srv/assets/source.16d3029596357c80a8efdbbfe106108a.png)

#### Note

Stripe can help you keep up with incoming payments by sending you email
notifications whenever a customer successfully completes one. Use the Dashboard
to [configure email notifications](https://dashboard.stripe.com/settings/user).

You can use plugins like [Zapier](https://stripe.com/works-with/zapier) to
automate updating your purchase fulfillment systems with information from Stripe
payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful
payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or
chat applications
[Test the integration](https://docs.stripe.com/payments/checkout/client#testing)
There are several test cards you can use to make sure your integration is ready
for production. Use them with any CVC, postal code, and future expiration date.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.40000000000032203D Secure 2 authentication must be completed for a
successful payment.4000000000009995Always fails with a decline code of
`insufficient_funds`.
For the full list of test cards see our guide on
[testing](https://docs.stripe.com/testing).

### Apple Pay and Google Pay

No configuration or integration changes are required to enable Apple Pay or
Google Pay in Stripe Checkout. These payments are handled the same way as other
card payments.

Apple PayGoogle Pay
The Apple Pay button is displayed in a given Checkout Session if all of the
following apply:

- Apple Pay is enabled for Checkout in your [Stripe
Dashboard](https://dashboard.stripe.com/settings/checkout).
- The customer’s device is running macOS 10.14.1+ or iOS 12.1+.
- The customer is using the Safari browser.
- The customer has a valid card registered with Apple Pay.

This ensures that Checkout only displays the Apple Pay button to customers who
are able to use it.

[OptionalCollect a billing
addressClient-side](https://docs.stripe.com/payments/checkout/client#collect-billing-address)[OptionalCollect
a shipping
addressClient-side](https://docs.stripe.com/payments/checkout/client#collect-shipping-address)[OptionalCustomize
the Checkout
buttonClient-side](https://docs.stripe.com/payments/checkout/client#customize-checkout-button)[OptionalPrefill
customer
emailClient-side](https://docs.stripe.com/payments/checkout/client#prefilling-customer-email)

## Links

- [donations](https://github.com/stripe-samples/github-pages-stripe-checkout)
- [hosted
version](https://stripe-samples.github.io/github-pages-stripe-checkout/)
- [client and server
integration](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Checkout settings](https://dashboard.stripe.com/settings/checkout)
- [Product](https://docs.stripe.com/api/products)
- [Price](https://docs.stripe.com/api/prices)
- [the Stripe Dashboard](https://dashboard.stripe.com/products)
- [migration guide](https://docs.stripe.com/payments/checkout/migrating-prices)
- [keep your existing
integration](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations)
- [Products](https://dashboard.stripe.com/test/products)
- [configure your domains
list](https://dashboard.stripe.com/account/checkout/settings)
- [webhook](https://docs.stripe.com/webhooks)
- [list of payments](https://dashboard.stripe.com/payments)
- [configure email notifications](https://dashboard.stripe.com/settings/user)
- [Zapier](https://stripe.com/works-with/zapier)
- [testing](https://docs.stripe.com/testing)