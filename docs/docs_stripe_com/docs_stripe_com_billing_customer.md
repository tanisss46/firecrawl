# Customers

## Learn how to use the Customer resource with Stripe Billing.

The [Customer](https://docs.stripe.com/api/customers) resource is a core entity
within Stripe. Use it to store all of the profile, billing, and tax information
required to bill a customer for
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
one-off [invoices](https://docs.stripe.com/api/invoices).

## Manage customers

Create a customer for every new user or business you want to bill. When creating
a new customer, set a [minimum customer
profile](https://docs.stripe.com/billing/customer#minimum-customer-profile) to
help create useful invoices and enable Smart Retries (dunning). After creating
and configuring this customer, use it to create a subscription and issue one-off
invoices.

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

## Available properties and uses

The Customer resource has many useful properties you can set to customize
billing. This section explains the properties you can store on the Customer, and
the effects of each.

### Customer profile

A basic customer profile is useful for invoice and receipt generation, and can
generally act as a lightweight customer relationship management system (CRM) for
your application. You can also use [Affiliate and referral Stripe
Apps](https://marketplace.stripe.com/categories/affiliate_and_referrals) to set
up and manage referral and affiliate programs with Stripe, get customer
information, and automate commission adjustments from the Stripe Dashboard.

#### Minimal customer profile

When creating a customer, set these properties:

- Email address
- Customer name
- Metadata with a reference to the internal customer ID of your application

An [email
address](https://docs.stripe.com/api/customers/object#customer_object-email)
lets Stripe notify the customer of failed payments or when completing a payment
requires further action, as part of the [Automatic
Collection](https://docs.stripe.com/invoicing/automatic-collection) process.

Store the internal customer ID of your application in the
[metadata](https://docs.stripe.com/api/customers/object#customer_object-metadata)
attribute. Like most Stripe resources, the Customer resource includes a
[Metadata](https://docs.stripe.com/api/metadata) object hash to flexibly store
contextual key-value information. To aid in auditing and support, store your
internal customer ID as a key-value pair on the Customer resource. This allows
you to search for the customer using your internal reference ID. Conversely, we
recommend storing Stripe customer IDs against the internal customer model of
your application.

#### Billing and shipping addresses

Use the address properties to set an
[address](https://docs.stripe.com/api/customers/object#customer_object-address)
for billing (invoicing, credit notes, and so on), and a
[shipping](https://docs.stripe.com/api/customers/object#customer_object-shipping)
address (for physical goods).

While a shipping address is most relevant to businesses delivering physical
goods, a billing address is useful because it displays on invoices, credit
notes, and receipts—a common requirement for tax compliance.

#### Email and PDF language localization

Localize Stripe-generated emails and PDFs by setting the `preferred_locales`
property. This property accepts an ordered list of preferred languages, sorted
by preference. These preferred locale values are based on
[RFC-4646](https://tools.ietf.org/html/rfc4646). Examples include “en” for
, or “fr-CA” for Canadian French. See the [Customizing
invoices](https://docs.stripe.com/invoicing/customize#customer-language) page
for more information.

#### Per-customer invoice settings

For further details on customizing invoice contents on a per-customer basis, see
the [Customizing invoices](https://docs.stripe.com/invoicing/customize) page. It
explains [custom
fields](https://docs.stripe.com/invoicing/customize#custom-fields), [invoice
footer](https://docs.stripe.com/invoicing/customize#footer-field) content, and
how to [customize the invoice
number](https://docs.stripe.com/invoicing/customize#invoice-numbering-schemes).

### Payment

All payments are collected from [payment](https://docs.stripe.com/payments)
details associated with a customer, and a customer can have multiple ways to
make a payment, including:

- [Payment Methods](https://docs.stripe.com/payments/payment-methods)
- [Customer Credit
Balance](https://docs.stripe.com/billing/customer#customer-balance)

Customers are
[single-currency](https://docs.stripe.com/billing/customer#currency), meaning
after you’ve assigned a currency, invoiced the customer, or [set a customer
credit balance](https://docs.stripe.com/billing/customer#customer-balance), you
can’t change the currency. This locked state is visible in the Dashboard in a
disabled **Currency** dropdown.

If you need to bill a single entity with multiple currencies, create a new
customer for each currency.

### Invoicing

All invoicing-related resources are associated with the customer being billed.
These resources include:

- [Pending invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Invoices](https://docs.stripe.com/invoicing/overview)
- [Receipts](https://docs.stripe.com/receipts)
- [Invoice
settings](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings)

### Tax info

To meet tax jurisdiction requirements, you might need to include customer tax ID
numbers and other information on invoices. It’s ultimately your responsibility
to make sure your customer’s invoices contain the correct information. This
includes [tax IDs](https://docs.stripe.com/billing/customer/tax-ids), [tax
exemption
status](https://docs.stripe.com/api/customers/create#create_customer-tax_exempt),
and [addresses](https://docs.stripe.com/billing/customer#addresses).

Tax IDs provide a way to store and render one or more tax ID numbers on
invoices. Tax exemption status indicates whether the entity is taxable. By
default, a customer’s `tax_exempt` status is set to `none`, meaning it’s a
taxable billing entity. However, you can flag a customer as being responsible
for paying the tax on an invoice by setting the `tax_exempt` property to
`reverse`, or flag them as being tax exempt by setting the status to `exempt`.
You can read more about using `tax_exempt` and `reverse` on the [Tax
Rates](https://docs.stripe.com/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)
page.

## Common tasks

This section explains some of the common tasks you might perform with the
Customer resource.

### Create a subscription

Before you can create a new subscription, you need to create a customer for
billing purposes.

- [Create the customer](https://docs.stripe.com/billing/customer#create).
- Define your
[product](https://docs.stripe.com/products-prices/manage-prices#create-product)
catalog and
[prices](https://docs.stripe.com/products-prices/manage-prices#create-price).
- [Create a
subscription](https://docs.stripe.com/billing/subscriptions/overview) using the
customer created in step one and a price (or multiple prices) from step two.

You can continue to update the customer’s details after you create the
subscription until an invoice is [finalized](https://docs.stripe.com/invoicing).
Any changes apply to the next billing cycle, when a new invoice is generated
using the latest state of the customer when rendering PDFs, emails, and the
hosted invoice page. Read the [How subscriptions
work](https://docs.stripe.com/billing/subscriptions/overview) page for more
detailed information.

### Send a one-off (manual) invoice to a customer

Unlike subscription invoices, you manually issue one-off invoices and they don’t
follow an automated schedule. This makes them useful for billing one-off orders
or work, such as setup and installation fees, consultancy fees, or single orders
for physical goods.

- [Create the customer](https://docs.stripe.com/billing/customer#create).
- [Create a new draft
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice) by adding
invoice line items with a description, quantity, unit price, and tax rate.
- [Set the invoice payment
method](https://docs.stripe.com/invoicing/dashboard#create-invoice). You can
collect payment for an invoice either by automatically charging the payment
method on file, or by emailing the invoice to the customer.
- Finalize the invoice.

See the [one-off invoices
documentation](https://docs.stripe.com/invoicing/dashboard#create-invoice) for
full details on how to create and collect payment for one-off invoices.

### Store a customer credit balance

The [customer credit balance](https://docs.stripe.com/billing/customer/balance)
feature allows you to assign credit and debit adjustments to a specific
customer. The resulting balance is applied to future invoices for that customer.

### Add and validate tax ID numbers

Displaying a customer’s tax ID on invoice documents is a common requirement.
With Stripe, you can add one or multiple [tax
IDs](https://docs.stripe.com/billing/customer/tax-ids) to a customer. A
customer’s tax IDs are displayed in the header of invoice and credit note PDFs.
See the [Tax IDs](https://docs.stripe.com/billing/customer/tax-ids) page for
more details.

### Add a coupon to a customer

A [coupon](https://docs.stripe.com/api/coupons) contains information about a
percent-off or amount-off discount. Stripe Billing allows you to associate a
coupon with a customer, resulting in a discount for all invoices billed.

Creating an invoice—either manually or when generated by a subscription—uses the
coupon by applying a corresponding discount to the invoice amount due,
subtracted from the pre-tax amount. You can view this information in the invoice
footer summary table.

### Set the currency for a customer

The `currency` property is a three-letter [ISO code for the
currency](https://docs.stripe.com/currencies) that you charge the customer in
for recurring billing purposes. You can set the currency in the Dashboard by
navigating to the **Customers** > **Details** page and clicking **Update
details**. After you set the currency, you can’t change it. Creating an invoice
or credit balance for the customer also permanently sets the customer’s
currency.

## Links

- [Customer](https://docs.stripe.com/api/customers)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoices](https://docs.stripe.com/api/invoices)
- [Customers page](https://dashboard.stripe.com/customers)
- [Affiliate and referral Stripe
Apps](https://marketplace.stripe.com/categories/affiliate_and_referrals)
- [email
address](https://docs.stripe.com/api/customers/object#customer_object-email)
- [Automatic Collection](https://docs.stripe.com/invoicing/automatic-collection)
-
[metadata](https://docs.stripe.com/api/customers/object#customer_object-metadata)
- [Metadata](https://docs.stripe.com/api/metadata)
-
[address](https://docs.stripe.com/api/customers/object#customer_object-address)
-
[shipping](https://docs.stripe.com/api/customers/object#customer_object-shipping)
- [RFC-4646](https://tools.ietf.org/html/rfc4646)
- [Customizing
invoices](https://docs.stripe.com/invoicing/customize#customer-language)
- [Customizing invoices](https://docs.stripe.com/invoicing/customize)
- [custom fields](https://docs.stripe.com/invoicing/customize#custom-fields)
- [invoice footer](https://docs.stripe.com/invoicing/customize#footer-field)
- [customize the invoice
number](https://docs.stripe.com/invoicing/customize#invoice-numbering-schemes)
- [payment](https://docs.stripe.com/payments)
- [Payment Methods](https://docs.stripe.com/payments/payment-methods)
- [Pending invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Invoices](https://docs.stripe.com/invoicing/overview)
- [Receipts](https://docs.stripe.com/receipts)
- [Invoice
settings](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings)
- [tax IDs](https://docs.stripe.com/billing/customer/tax-ids)
- [tax exemption
status](https://docs.stripe.com/api/customers/create#create_customer-tax_exempt)
- [Tax
Rates](https://docs.stripe.com/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)
-
[product](https://docs.stripe.com/products-prices/manage-prices#create-product)
- [prices](https://docs.stripe.com/products-prices/manage-prices#create-price)
- [finalized](https://docs.stripe.com/invoicing)
- [Create a new draft
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [customer credit balance](https://docs.stripe.com/billing/customer/balance)
- [coupon](https://docs.stripe.com/api/coupons)
- [ISO code for the currency](https://docs.stripe.com/currencies)