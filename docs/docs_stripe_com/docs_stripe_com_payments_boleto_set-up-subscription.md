# Use Boleto with subscriptions

## Learn how to use Boleto with subscriptions.

Learn how to set up [Boleto](https://docs.stripe.com/payments/boleto) as a
[payment method](https://docs.stripe.com/api/payment_methods). Boleto is a
voucher with a generated number that
[Customers](https://docs.stripe.com/api/customers) can obtain from an ATM, a
bank, an online bank portal, or an authorized agency.

[Enable
Boleto](https://docs.stripe.com/payments/boleto/set-up-subscription#enable-boleto)
Before you start your integration, go to **Manage payments that require
confirmation** in your [Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic) and enable
**Send a Stripe-hosted link for customers to confirm their payments when
required**.

Go to your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) and enable
Boleto as a payment method. You can click **Configure** to set the voucher
expiration delay.

[Decide the collection
method](https://docs.stripe.com/payments/boleto/set-up-subscription#set-collection-method)
You can set the collection method in the Dashboard or
[API](https://docs.stripe.com/api/invoices/create#create_invoice-collection_method).
For invoices, you can choose to either send an invoice or charge your customer
automatically. If you’re using the API, the `send_invoice` and
`charge_automatically` values determine the collection method.

Send invoiceCharge automaticallyWhen to use- Your customer hasn’t defined their
preferred payment method to pay invoices or subscriptions. In this case, you
want to give them the option to use either a credit card or Boleto.
- You’re missing important customer information required to use Boleto (full
name, address, and tax ID).
- Your customer already chose to pay for their invoices or subscriptions using
boletos.
- You have the customer information needed to create an invoice that uses Boleto
(full name, address, and tax ID).
Customer experience- Your customer needs to reenter their personal information
details (full name, address, and tax ID) every time you send a new invoice, or
for each new subscription cycle. This collection method doesn’t take into
account the default payment method associated with that customer.
- Your customer has Boleto set up as their default payment method. Your customer
receives an email with a Boleto voucher every time you send them an invoice, or
there’s a subscription cycle.
Expiration and due dates- The invoice must contain a due date.
- Stripe creates the boleto—regardless of the invoice due date—as soon as your
customer enters the needed details. Because boletos have their own expiration
date (the default is 3 days), the invoice due date and the boleto expiration
date won’t necessarily match. The boleto might expire before or after the
invoice is due.
- The invoice doesn’t have a due date.
- Stripe creates the boleto when the merchant creates the invoice with a
selected expiration date (the default is 3 days).
[Create a
customer](https://docs.stripe.com/payments/boleto/set-up-subscription#create-customers)
Create a customer for every new user or business you want to bill. When you
create a new customer, set up a [minimal customer
profile](https://docs.stripe.com/payments/boleto/set-up-subscription#customer-profile)
to help generate more useful invoices, and enable Smart Retries (if you’re an
[Invoicing Plus](https://stripe.com/invoicing/pricing) user). After you set up
your customer, you can issue one-off invoices or create
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating).

#### Caution

Before you create a new customer, make sure that the customer doesn’t already
exist in the Dashboard. Creating multiple customer entries for the same customer
can cause you problems later on, such as when you need to reconcile transaction
history or coordinate saved payment methods.

DashboardAPI
You can create and manage customers on the [Customers
page](https://dashboard.stripe.com/customers) when you don’t want to use code to
create a customer, or if you want to manually bill a customer with a one-off
invoice.

#### Note

You can also create a customer in the Dashboard during invoice creation.

### Create a customer

When you create a new customer, you can set their account and billing
information, such as **Email**, **Name**, and **Country**. You can also set a
customer’s preferred language, currency, and other important details.

To create a customer, complete these steps:

- Verify that the customer doesn’t already exist.
- Click **Add customer**, or press **N**, on the **Customers** page.
- At a minimum, enter your customer’s **Name** and **Account email**.
- Click **Add customer** in the dialog.

### Edit a customer

To edit a customer’s profile, complete these steps:

- Find the customer you want to modify and click the name on the **Customers**
page.
- In the account information page, select **Actions** > **Edit information**.
- Make your changes to the customer profile.
- Click **Update customer**.

### Delete a customer

To delete a customer, complete these steps:

- Find the customer you want to delete on the **Customers** page.
- Click the checkbox next to your customer’s name followed by **Delete**. You
can also click into the customer’s details page and select **Actions** >
**Delete customer**.
[Create a product and
price](https://docs.stripe.com/payments/boleto/set-up-subscription#create-product-price)
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
[Create a
subscription](https://docs.stripe.com/payments/boleto/set-up-subscription#create-subscription)
You can create and update subscriptions from the Dashboard or the API. Use the
API if you have a large number of subscriptions to manage, or if you want to
manage them programmatically.

#### Note

See our integration guide to learn how to [build a complete subscription
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).

DashboardAPI
### Create a subscription

To create a subscription:

- Go to the **Payments** > **Subscriptions** page.
- Click **+Create subscription**.
- Find or add a customer.
- Enter the pricing and product information, which allows you to add multiple
products, a coupon, or trial to the subscription.

In the **Advanced** options section, you can optionally create [thresholds for
metered
usage](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
or add [customized invoice](https://docs.stripe.com/invoicing/customize) fields.
When you’re finished, click **Schedule subscription** or **Start subscription**.
When scheduling a subscription you can start it immediately, the next month, or
customize it. You can end the subscription immediately, after a number of
cycles, or customize a date.

### Edit a subscription

To edit a subscription:

- Go to the **Payments** > **Subscriptions** page.
- Find the subscription you want to modify, click the overflow menu (), then
click **Update subscription**. You can also click the next to the subscription
name. From this menu, you can also:

- **Cancel the subscription**. In the modal that opens, select the date to
cancel the subscription—immediately, at the end of the current period, or on a
custom date. You can also select the option to refund the last payment for this
subscription and create a [credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes) for your
records.
- **Pause payment collection**. In the modal that opens, select the duration of
the pause—indefinite or ending on a custom date, and how invoices should behave
during the pause.
- **Share payment update link**. In the modal that opens, you can share a link
with the customer to update their payment details. For more information, see
[Share payment update
link](https://docs.stripe.com/billing/subscriptions/update-payment-method).
- Add the changes you want to the subscription.
- Click **Update subscription**.

### Delete a subscription

You can’t delete a subscription object, but you can cancel it or pause payment
collection. See [editing a
subscription](https://docs.stripe.com/payments/boleto/set-up-subscription#edit-susbscription)
for those details.

## See also

- [How Subscriptions
work](https://docs.stripe.com/billing/subscriptions/overview)

## Links

- [Boleto](https://docs.stripe.com/payments/boleto)
- [payment method](https://docs.stripe.com/api/payment_methods)
- [Customers](https://docs.stripe.com/api/customers)
- [Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
-
[API](https://docs.stripe.com/api/invoices/create#create_invoice-collection_method)
- [Invoicing Plus](https://stripe.com/invoicing/pricing)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Customers page](https://dashboard.stripe.com/customers)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [invoices](https://docs.stripe.com/api/invoices)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Product catalog page](https://dashboard.stripe.com/products)
- [build a complete subscription
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [thresholds for metered
usage](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- [customized invoice](https://docs.stripe.com/invoicing/customize)
- [credit note](https://docs.stripe.com/invoicing/dashboard/credit-notes)
- [Share payment update
link](https://docs.stripe.com/billing/subscriptions/update-payment-method)
- [How Subscriptions
work](https://docs.stripe.com/billing/subscriptions/overview)