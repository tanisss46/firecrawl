# Customers

## Learn how to use the Customer resource with Stripe Invoicing.

Create a customer for every new user or business you want to bill. When you
create a new customer, set up a [minimal customer
profile](https://docs.stripe.com/invoicing/customer#customer-profile) to help
generate more useful invoices, and enable Smart Retries (if you’re an [Invoicing
Plus](https://stripe.com/invoicing/pricing) user). After you set up your
customer, you can issue one-off invoices or create
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

## Customer profiles

​​Use a basic customer profile for invoice and receipt generation or as a
lightweight customer relationship management system (CRM) for your application.
To create a minimal customer profile, set these properties:

- Email address.
- Customer name.
- Metadata with a reference to your application’s internal customer ID.

Stripe uses your customer’s [email
address](https://docs.stripe.com/api/customers/object#customer_object-email) to
notify them of payment failures. Stripe also uses email addresses to notify
customers when they need to perform an action to complete a payment.

Store the internal customer ID for your application in the
[metadata](https://docs.stripe.com/api/customers/object#customer_object-metadata)
attribute. Like most Stripe resources, the `Customer` resource includes a
[Metadata](https://docs.stripe.com/api/metadata) object hash to flexibly store
contextual key-value information. To aid in auditing and support, store your
internal customer ID as a key-value pair on the `Customer` resource. This allows
you to search for the customer using your internal reference ID. We recommend
storing Stripe customer IDs against the internal customer model of your
application.

### Billing and shipping addresses

Use the [address
attributes](https://docs.stripe.com/api/customers/object#customer_object-address)
to set a billing address for invoicing and credit notes. For physical good
delivery, add a
[shipping](https://docs.stripe.com/api/customers/object#customer_object-shipping)
address.

#### Note

Invoices, credit notes, and receipts display the billing address—a common
requirement for tax compliance.

### Email and PDF language localization

When you create a customer, use the **Language** dropdown to add their preferred
language. (You can also add or edit a customer’s preferred language in the
**Customer details** page or when creating an invoice.) Stripe uses the chosen
language to localize invoice emails and PDFs, receipt emails and PDFs, and
credit note PDFs.

To update the language through the API, use the
[preferred_locales](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)
parameter. This parameter accepts an ordered list of preferred languages sorted
by preference. These preferred locale values are based on
[RFC-4646](https://tools.ietf.org/html/rfc4646). Examples include en for
, or fr-CA for Canadian French. To learn more, see [Customer preferred
languages](https://docs.stripe.com/invoicing/customize#customer-language).

## Customer properties

The following table contains additional customer properties:

PropertyDescriptionPayment propertiesStripe uses the
[payment](https://docs.stripe.com/payments) details associated with a customer
to collect payment. A customer can have multiple ways to make a payment,
including the [Payment Methods
API](https://docs.stripe.com/payments/payment-methods) and [Customer credit
balance](https://docs.stripe.com/invoicing/customer/balance). Customers are
single-currency, which means that after you assign a currency, invoice the
customer, or set a customer credit balance, you can’t change the currency. You
can see this locked state in the Dashboard in a disabled Currency dropdown. If
you need to bill a single entity with multiple currencies, create a new customer
for each currency.Invoicing propertiesAll [invoicing-related
resources](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings)
are associated with the billed customer.Tax propertiesTo meet tax jurisdiction
requirements, you might need to include customer tax ID numbers and other
tax-related information on your invoices. ​​It’s your responsibility to make
sure your customer’s invoices contain all of the correct information, such as
[tax IDs](https://docs.stripe.com/invoicing/customer/tax-ids), [tax exemption
status](https://docs.stripe.com/api/customers/create#create_customer-tax_exempt),
and [addresses](https://docs.stripe.com/invoicing/customer#addresses). Tax IDs
provide a way to store and render one or more tax ID numbers on invoices. The
tax exemption status indicates whether the entity is taxable. By default, a
customer’s `tax_exempt` status is set to `none`—meaning it’s a taxable billing
entity. However, you can set the `tax_exempt` parameter to `reverse` for
customers that must pay the invoice’s tax. You can also flag the customer as
being tax exempt by setting the status to `exempt`. To learn more about using
`tax_exempt` and `reverse`, see [Tax
Rates](https://docs.stripe.com/billing/taxes/tax-rates#tax-exempt-and-reverse-charge).
## Common tasks

Here are some of the common tasks you can perform with the `Customer` resource:

- **Send an invoice to a customer**: After you create the customer, you can
[send them an
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice).
- **Store a customer credit balance**: The customer credit balance feature
allows you to assign credit and debit adjustments to a specific customer and
then apply the resulting balance toward future invoices for them.
- **Add and validate tax ID numbers**: Displaying a customer’s tax ID on an
invoice is a common requirement, and Stripe allows you to add multiple tax IDs
to a customer. Their tax IDs display in the header of invoice and credit note
PDFs. See the [Customer tax
IDs](https://docs.stripe.com/invoicing/customer/tax-ids) page for more details.
- **Add a coupon to a customer**: A
[coupon](https://docs.stripe.com/api/coupons) contains information about a
percent-off or amount-off discount, and Stripe Invoicing allows you to associate
a coupon with a customer. Coupons apply a discount to the invoice amount due, on
a pre-tax basis.
- **Set the currency for a customer**: You can set the default currency to
charge a customer for invoices using the Dashboard by navigating to the
**Customers** page, selecting your customer, and clicking **Edit** next to
**Details**. See the [Multi-currency
customers](https://docs.stripe.com/invoicing/multi-currency-customers) page for
more details on billing the same customer using a different currency than their
default currency.
- **Create customers in bulk**: Bulk upload Customers using [Productivity Stripe
Apps](https://marketplace.stripe.com/categories/productivity).

## Links

- [Invoicing Plus](https://stripe.com/invoicing/pricing)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Customers page](https://dashboard.stripe.com/customers)
- [email
address](https://docs.stripe.com/api/customers/object#customer_object-email)
-
[metadata](https://docs.stripe.com/api/customers/object#customer_object-metadata)
- [Metadata](https://docs.stripe.com/api/metadata)
- [address
attributes](https://docs.stripe.com/api/customers/object#customer_object-address)
-
[shipping](https://docs.stripe.com/api/customers/object#customer_object-shipping)
-
[preferred_locales](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)
- [RFC-4646](https://tools.ietf.org/html/rfc4646)
- [Customer preferred
languages](https://docs.stripe.com/invoicing/customize#customer-language)
- [payment](https://docs.stripe.com/payments)
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
- [Customer credit balance](https://docs.stripe.com/invoicing/customer/balance)
- [invoicing-related
resources](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings)
- [tax IDs](https://docs.stripe.com/invoicing/customer/tax-ids)
- [tax exemption
status](https://docs.stripe.com/api/customers/create#create_customer-tax_exempt)
- [Tax
Rates](https://docs.stripe.com/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)
- [send them an
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [coupon](https://docs.stripe.com/api/coupons)
- [Multi-currency
customers](https://docs.stripe.com/invoicing/multi-currency-customers)
- [Productivity Stripe
Apps](https://marketplace.stripe.com/categories/productivity)