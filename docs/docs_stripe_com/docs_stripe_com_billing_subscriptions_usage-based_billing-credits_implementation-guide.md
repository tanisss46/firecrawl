# Set up billing creditsPublic preview

## Learn how to implement a prepaid billing solution with billing credits.

Use [Meters](https://docs.stripe.com/api/billing/meter) and [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
to offer credits to your customers when they prepay for usage-based products or
services, or as a promotional offering.

## Before you begin

Before you can use billing credits, you must [set up usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide):

- Create a [billing
meter](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-meter).
- Create a [pricing
model](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-pricing-model)
and add the meter to it.
- Create a
[subscription](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-subscription)
that includes your customer, product, and usage-based price.
[Grant billing credits to your
customer](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide#grant-the-billing-credits)
Use the Stripe Dashboard or API to create a credit grant for your customer.

Billing credits only apply to
[subscription](https://docs.stripe.com/api/invoices/object#invoice_object-subscription)
line items that link to a [meter
price](https://docs.stripe.com/api/prices/object#price_object-recurring-meter).
The ([Usage Records API](https://docs.stripe.com/api/usage_records)) isn’t
supported.

DashboardAPI- On the [Customers](https://dashboard.stripe.com/test/customers)
page, select the customer name.
- On the customer page, under **Credit grants**, click the plus (**+**) symbol.
- On the **New credit grant** page, do the following:
- For **Name**, enter a name for your credit grant.
- For **Amount**, specify the amount of the credit grant.
- *(Optional)* Under **Effective date**, specify a date for when to grant the
credit.
- *(Optional)* Under **Expiry date**, specify the date, if any, when the credits
expire.
- *(Optional)* Under **Priority**, specify the priority for this credit grant.
- *(Optional)* Under **Eligibility**, specify a list of usage-based prices that
this credit grant applies to.
- Click **Create grant**.
[Apply billing credits to
invoices](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide#apply-billing-credits-to-invoices)
After the invoice finalizes, Stripe automatically applies all applicable billing
credits. The available balance on the credit grant updates based on the amount
of billing credits applied to the invoice.

You can find the amount of billing credits applied to an invoice in the Stripe
Dashboard.

- On the [Customers](https://dashboard.stripe.com/test/customers) page, select
the customer name.
- On the customer page, under **Invoices**, select an invoice.
- On the invoice page, under **Subtotal**, find the line for **Credit grant
applied**.
[Retrieve the available billing credit
balance](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide#get-available-billing-credit-balance)
Use the Stripe Dashboard or API to see the available billing credit balance for
a customer. When using the API, retrieve the [Credit Balance
Summary](https://docs.stripe.com/api/billing/credit-balance-summary/retrieve)
endpoint.

DashboardAPI- On the [Customers](https://dashboard.stripe.com/test/customers)
page, select the customer name.
- On the customer page, under **Credit grants**, find the list of credit grants
that can apply to invoices. You can see the credit grant’s
[available_balance](https://docs.stripe.com/api/billing/credit-balance-summary/object#billing_credit_balance_summary_object-balances-available_balance)
in the **Available** column.
[List transactions for a credit
grant](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide#list-billing-credit-balance-transactions)
Use the Stripe Dashboard or API to see the transactions for a specific credit
grant or customer. When using the API, call the [Credit Balance
Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction/list)
endpoint.

DashboardAPI- On the [Customers](https://dashboard.stripe.com/test/customers)
page, select the customer name.
- On the customer page, under **Credit grants**, select a credit grant.
- View details for the credit balance transactions.
[OptionalFund the credit
grant](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits/implementation-guide#fund-the-credit-grant)
## See also

- [Credit application
eligibility](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits#credit-grant-eligibility)
- [Usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)

## Links

- [Meters](https://docs.stripe.com/api/billing/meter)
- [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
- [set up usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide)
- [billing
meter](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-meter)
- [pricing
model](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-pricing-model)
-
[subscription](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide#create-subscription)
-
[subscription](https://docs.stripe.com/api/invoices/object#invoice_object-subscription)
- [meter
price](https://docs.stripe.com/api/prices/object#price_object-recurring-meter)
- [Usage Records API](https://docs.stripe.com/api/usage_records)
- [Customers](https://dashboard.stripe.com/test/customers)
- [Credit Balance
Summary](https://docs.stripe.com/api/billing/credit-balance-summary/retrieve)
-
[available_balance](https://docs.stripe.com/api/billing/credit-balance-summary/object#billing_credit_balance_summary_object-balances-available_balance)
- [Credit Balance
Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction/list)
- [Credit application
eligibility](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits#credit-grant-eligibility)
- [Usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)