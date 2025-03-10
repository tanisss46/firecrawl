# Taxes

## Learn about Stripe Tax and how to use it with invoices.

On an [invoice](https://docs.stripe.com/api/invoices), Stripe Tax calculates
sales tax, VAT, and GST. To calculate these for each line item, Stripe uses:

- Your [tax settings](https://dashboard.stripe.com/settings/tax)
- The customer’s tax settings and location
- The product tax code and price tax behavior
[Activate Stripe Tax](https://docs.stripe.com/invoicing/taxes#activate)
[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to activate Stripe Tax.

## Set up the customer

We use the customer’s location to determine the relevant taxes to collect.
Customers outside of the US need at least a country-level address, while
customers in the US require a 5-digit postal code. For Canada, we need at least
the province or postal code.

DashboardAPI
You can add customer location information in the **Customer details** page by
clicking **Edit** next to **Details**. To add a customer’s location from the
[Invoice Editor](https://dashboard.stripe.com/invoices/create), click the
overflow menu () next to the customer. Select **Edit customer information**,
click **Add additional details**, and scroll down to **Billing details**.

After you update the location, click **Update customer**. Stripe applies the new
location to all of your customer’s future invoices unless you update it. For
more information, see [Determine customer
locations](https://docs.stripe.com/tax/customer-locations).

## Set up line items

To calculate tax on each line item on an invoice, you need to set a tax behavior
and optionally a tax code.

### Customize tax settings for one-off line items

Customize line items in the Invoice Editor by selecting the tax behavior from
the **Include tax in price** drop-down menu.

![Customize tax settings for one-off line
items](https://b.stripecdn.com/docs-statics-srv/assets/invoicing_price.faa90fb6b3cb833b900e06cb2187d339.png)

Customize tax settings for one-off line items

### Customize tax settings for product-based line items

You can use both the Dashboard and the API to customize tax settings for
product-based line items.

DashboardAPI
On the [Products page](https://dashboard.stripe.com/products), you can select
both the tax behavior for a particular price and the optional tax code for the
product. The tax behavior is per price. You can’t change the tax behavior after
you select it, but you can create new prices or archive old ones. To set up a
tax behavior, click **Add a price** (or **Add another price** if you already
have one) and select it from the **Tax behavior** drop-down menu.

To set up a tax code, select it from the **Tax code** drop-down menu when you
create a new product or edit the details of an existing one.

![Customize tax settings for one-off line
items](https://b.stripecdn.com/docs-statics-srv/assets/invoicing_new_price.517f186f27925e52e501019b9aecc94b.png)

Customize tax settings for one-off line items

## Enable automatic tax

DashboardAPI
Enable the **Use automatic tax collection** toggle in your [tax
settings](https://dashboard.stripe.com/settings/tax) to automatically enable tax
calculation on *new* invoices you create in the Dashboard.

![Stripe Dashboard with the automatic tax toggle set to
true](https://b.stripecdn.com/docs-statics-srv/assets/dashboard_automatic_tax.2338adf39e3a07ad9acd79c036e7c637.png)

Stripe Dashboard with the automatic tax toggle set to true

### Update untaxed invoices

To enable automatic tax calculation for existing invoices:

- Click **Edit invoice** from the **Invoice details** page, or click the
invoice’s overflow menu (), then **Edit invoice** from the [Invoices
page](https://dashboard.stripe.com/test/invoices) to create a new draft in the
**Invoice Editor**.
- In the editor, turn on the **Collect tax automatically** toggle.
- If customer is missing address information required for tax calculation, a
notification badge alerts you and provides instructions to resolve the problem.

![Invoice editor with the warning badge about missing customer
address](https://b.stripecdn.com/docs-statics-srv/assets/invoice_no_address_badge.cf9ee01e250675ea8742a948ddbd59d6.png)

Invoice editor with the warning badge about missing customer address
- Save the invoice to enable automatic tax calculations on all future instances
of the invoice. Learn more about [editing invoices after
finalization](https://docs.stripe.com/invoicing/invoice-edits).

### Update invoices with existing tax rates

To replace invoice [tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
with automatic tax calculation, follow the previous steps to edit the invoice.
Then remove the applied tax rates and enable the **Collect tax automatically**
toggle.

For more information on automatic tax calculation, see [Automatically collect
tax on invoices](https://docs.stripe.com/tax/invoicing).

## Net prices and taxes

You can issue invoices with line item prices that exclude inclusive tax.
Tax-exclusive prices are only shown in the invoice PDF. That means, when using
inclusive tax, the Hosted Invoice Page and invoice emails show tax-inclusive
prices. You can define the settings for net prices in the Dashboard or API.

- **Include inclusive tax**—The invoice PDF displays line item prices including
the inclusive tax. (This is the default.)
- **Exclude tax**—The invoice PDF displays line item prices excluding tax.

#### Order precedence

If you set a default for line item prices at the customer level, it takes
precedence over account-level settings.

DashboardAPI
To set a default for item prices, go to **Default item prices** in the [Invoice
template](https://dashboard.stripe.com/settings/billing/invoice). Your chosen
setting applies to all of the invoices you create through the Dashboard or API.
For one-off invoices, use the [Invoice
Editor](https://dashboard.stripe.com/test/invoices/create) to set tax
exclusivity. Go to **Advanced options** and choose to **Include inclusive tax**
or **Exclude tax**. To learn more, see [Create an
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice).

## See also

- [Determine customer locations](https://docs.stripe.com/tax/customer-locations)
- [Understand zero tax amounts](https://docs.stripe.com/tax/zero-tax)
- [Reporting and filing](https://docs.stripe.com/tax/reports)

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [tax settings](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [Invoice Editor](https://dashboard.stripe.com/invoices/create)
- [Determine customer locations](https://docs.stripe.com/tax/customer-locations)
- [Products page](https://dashboard.stripe.com/products)
- [Invoices page](https://dashboard.stripe.com/test/invoices)
- [editing invoices after
finalization](https://docs.stripe.com/invoicing/invoice-edits)
- [tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
- [Automatically collect tax on invoices](https://docs.stripe.com/tax/invoicing)
- [Invoice template](https://dashboard.stripe.com/settings/billing/invoice)
- [Invoice Editor](https://dashboard.stripe.com/test/invoices/create)
- [Create an
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [Understand zero tax amounts](https://docs.stripe.com/tax/zero-tax)
- [Reporting and filing](https://docs.stripe.com/tax/reports)