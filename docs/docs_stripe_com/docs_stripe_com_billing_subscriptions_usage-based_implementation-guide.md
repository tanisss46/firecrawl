# Set up usage-based billing

## Learn how to charge customers based on their usage of your product or service.

Usage-based billing enables you to charge customers based on their usage of your
product or service.

This guide demonstrates how to create a meter, set up pricing and billing, and
send meter events to record customer usage. You’ll learn core concepts of a
usage-based billing model through a fictional GenAI company called Alpaca AI.
Alpaca AI charges their customers 0.04 USD per hundred tokens, and bills them at
the end of the month in arrears.

The following diagram shows the core concepts of usage-based billing:

Customer action

Meter event

Meter

Meter event summaries

Price

Invoice

Subscription

Customer

generatesaggregatesrated with pricerate usage (price x
quantity)generateshashasBilling meter concepts[Create a
meter](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-meter)
Meters specify how to aggregate meter events over a billing period. Meter events
represent the raw actions that customers take in your system. Meters attach to
prices and form the basis of what’s billed.

For the Alpaca AI example, meter events are the number of tokens a customer uses
in a query. The meter is the sum of tokens over a month.

You can use the Stripe Dashboard or API to [create a
meter](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter).
If you want to use the API with the Stripe CLI to create a meter, learn how to
[get started with the Stripe CLI](https://docs.stripe.com/stripe-cli).

DashboardAPI- On the [Meters](https://dashboard.stripe.com/test/meters) page,
click **Create meter**.
- On the **Create meter** page, do the following:- For **Meter name**, enter the
name of the meter to display and for organization purposes. For the Alpaca AI
example, enter `Alpaca AI tokens`.
- For **Event name**, enter the name to display in meter events when reporting
usage to Stripe. For the Alpaca AI example, enter `alpaca_ai_tokens`.
- Select **Sum** from the **Aggregation method** dropdown to set the aggregation
formula.
- Click **Create meter**.
[Create a pricing
model](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-pricing-model)
Use the Stripe Dashboard or API to create a [pricing
model](https://docs.stripe.com/products-prices/pricing-models) that includes
your [Products](https://docs.stripe.com/api/products) and their pricing options.
[Prices](https://docs.stripe.com/api/prices) define the unit cost, currency, and
billing cycle.

For the Alpaca AI example, you create a product with a metered price of 0.04 USD
per hundred units, billed at a monthly interval. You use the meter that you
created in the previous step.

DashboardAPI- On the [Product
catalog](https://dashboard.stripe.com/products?active=true) page, click **Create
product**.
- On the **Add a product** page, do the following:- For **Name**, enter the name
of your product. For the Alpaca AI example, enter `Alpaca AI`.
- *(Optional)* For **Description**, add a description that appears at checkout
in the [customer portal](https://docs.stripe.com/customer-management) and in
[quotes](https://docs.stripe.com/quotes).
- Select **Recurring**.
- Under **Billing period**, select **More pricing options**.
- On the **Add price** page, do the following:- Under **Choose your pricing
model**, select **Usage-based** and **Per package**.
- Under **Price**, set the **Amount** to `0.04 USD` per `1000` units.
- Under **Meter**, select **Alpaca AI tokens** from the dropdown.
- Under **Billing period**, select **Monthly**.
- Click **Next**.
- On the **Add a product** page, click **Add product**.
[Create a
customer](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-customer)
Next, create a [customer](https://docs.stripe.com/api/customers).

DashboardAPI- On the [Customers](https://dashboard.stripe.com/test/customers)
page, click **Add customer**.
- On the **Create customer** page, do the following:- For **Name**, enter the
name of your customer. For the Alpaca AI example, enter `John Doe`.
- *(Optional)* Add an email address and description for your customer.
- Click **Add customer**.
[Create a
subscription](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-subscription)
[Subscriptions](https://docs.stripe.com/api/subscriptions) allow you to charge
recurring amounts by associating a customer with a specific price.

Use the Stripe Dashboard or API to create a subscription that includes your
customer, product, and usage-based price.

For the Alpaca AI example, you create a subscription for the Alpaca AI product,
with a metered price of 0.04 USD per unit, billed monthly to John Doe.

#### Note

You can associate a single metered price with one or more subscriptions.

DashboardAPI- On the
[Subscriptions](https://dashboard.stripe.com/test/subscriptions) page, click
**Create test subscription**.
- On the **Create a test subscription** page, do the following:- Under
**Customer**, select the name of your customer. For the Alpaca AI example,
select **John Doe**.
- Under **Product**, select your price. For the Alpaca AI example, select the
price under **Alpaca AI**.
- *(Optional)* Modify the subscription details and settings as needed.
- Click **Create test subscription**.
[Send a test meter
event](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#test-usage)
Use [Meter Events](https://docs.stripe.com/api/billing/meter-event) to [record
customer
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#record-usage)
for your meter. At the end of the billing period, Stripe bills the reported
usage.

You can test your usage-based billing by sending a meter event through the
Stripe Dashboard or API. When using the API, specify the customer ID and value
for the `payload`.

After you send meter events, you can view usage details for your meter on the
[Meters](https://dashboard.stripe.com/test/meters) page in the Dashboard.

DashboardAPI- On the [Meters](https://dashboard.stripe.com/test/meters) page,
select the meter name. For the Alpaca AI example, select **Alpaca AI tokens**.
- On the meter page, click **Add usage** > **Manually input usage**.
- On the **Add usage** page, do the following:- Select your customer from the
**Customer** dropdown.
- For **Value**, enter a sample value. For the Alpaca AI example, enter `3000`.
- Click **Submit**.
[Retrieve an upcoming
invoice](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#retrieve-upcoming-invoice)
[Retrieve an upcoming invoice](https://docs.stripe.com/api/invoices/upcoming) to
see a preview of a customer’s invoice that includes details such as the meter
price and usage quantity.

DashboardAPI- On the
[Subscriptions](https://dashboard.stripe.com/test/subscriptions) page, select a
subscription. For the Alpaca AI example, select the subscription for **John
Doe**.
- On the subscription details page, scroll down to the **Upcoming invoice**
section. The preview invoice shows the subscription amount to bill the customer
on the specified date.
- Click **View full invoice** to see complete details for the upcoming invoice,
including:

- Customer
- Billing method
- Creation date
- Connected subscription
- Subscription details (usage quantity and meter price)
- Amount due

Because Stripe processes meter events asynchronously, upcoming invoices might
not immediately reflect recently received meter events.
[OptionalRetrieve usage for a custom time
period](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#retrieve-usage)
## Next steps

- [Accept payments with Stripe
Checkout](https://docs.stripe.com/payments/checkout)
- [Set up alerts and
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds)
- [Set up billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide)

## Links

- [create a
meter](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#configure-meter)
- [get started with the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Meters](https://dashboard.stripe.com/test/meters)
- [pricing model](https://docs.stripe.com/products-prices/pricing-models)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [Product catalog](https://dashboard.stripe.com/products?active=true)
- [customer portal](https://docs.stripe.com/customer-management)
- [quotes](https://docs.stripe.com/quotes)
- [customer](https://docs.stripe.com/api/customers)
- [Customers](https://dashboard.stripe.com/test/customers)
- [Subscriptions](https://docs.stripe.com/api/subscriptions)
- [Subscriptions](https://dashboard.stripe.com/test/subscriptions)
- [Meter Events](https://docs.stripe.com/api/billing/meter-event)
- [record customer
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#record-usage)
- [Retrieve an upcoming invoice](https://docs.stripe.com/api/invoices/upcoming)
- [Accept payments with Stripe
Checkout](https://docs.stripe.com/payments/checkout)
- [Set up alerts and
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds)
- [Set up billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide)