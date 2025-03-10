# Best practices for setting up invoices in Europe

## Learn the best practices for setting up invoices in Europe.

*Last updated January 12, 2023*

#### Legal Disclaimer

The information on this page is for your general guidance and isn’t legal
advice.

The invoice compliance process can vary across European countries. Stripe
recommends the following as best practices when you make sales to business
customers as Business-to-Business (B2B) sales require compliant invoices.
There’s no general obligation to issue invoices for Business-to-Consumer (B2C)
sales.

#### Note

Our recommendations are for standard (full) invoices. In most countries, you can
also issue simplified invoices for lower amounts, which are subject to less
strict legal requirements.

## Key invoice fields

Stripe doesn’t automatically populate all of the fields on an invoice. In
certain European countries, a missed or improperly added field can render an
invoice noncompliant. We recommend that you include the noted fields when you
prepare your invoices as they’re required throughout most of Europe.

![Key invoice
details](https://b.stripecdn.com/docs-statics-srv/assets/invoice-global-config-annotations.97e5b50ca2d6c3a761449564cfe3946f.png)

Key invoice details

## How to add an invoice field

The following table explains the ways that you can populate different invoice
fields. To ensure that your invoices are compliant and adhere to geographic and
business regulations, Stripe recommends that you consult with your tax and legal
advisors.

KeyFieldRequired?How to populate1Invoice numberThis is always required.Stripe
populates this by default. You can change how invoices are numbered (customer or
account level) in the [Invoice
template](https://dashboard.stripe.com/settings/billing/invoice).2Date of
issueThis is always required.Stripe populates this by default.3Date dueThere’s
no requirement to display the date by which a customer must pay an invoice.
However, it’s a best practice.Stripe populates this by default.4aMerchant
company nameThis is always required.Stripe populates this by default.4bMerchant
company addressSending an invoice to another business always requires this
field.Enter your Support address under [Public business
information](https://dashboard.stripe.com/settings/public). You can also default
to your business address as listed in your [account
settings](https://dashboard.stripe.com/settings/account).5Merchant VAT
ID​​Invoices generally require a merchant VAT ID (or tax ID). If you sell goods
or services to a business customer in another EU country, you must mention your
VAT ID, which is a number that contains a country prefix.Add your relevant tax
or VAT ID by navigating to Manage tax information in the Invoice
template.6aRecipient nameThis is always required.Stripe populates this by
default.6bRecipient addressThis is always required.You can add this field by
clicking the Additional details button when you first create a
customer.7Recipient VAT IDSending an invoice to another business typically
requires this field. ​​If you sell goods or services to a business customer in
another EU country, you must mention the customer’s VAT ID, which is a number
that contains a country prefix.You can add this field by:- Clicking **Add
additional details** (just like with the recipient address) when you create a
new customer, and scrolling down to **Tax ID** at the bottom of the dialog.
- Adding it as a custom field under **Additional options** when you create an
invoice.
8Name of the good or serviceThis is always required.Stripe populates this by
default.9Invoice line item supply dateThis is always required when the supply
date of individual line items is different from the invoice send date.You can
display line item supply dates by clicking the toggle under Item options.10Price
of the good or serviceFor an invoice to be compliant, it must display
tax-exclusive prices. For each invoice line item, you must show the following:-
Unit price (excluding VAT).
- Quantity.
- Any applicable discounts.
- Total amount payable (excluding VAT), which is the unit price times the
quantity, minus discounts.
You must display tax-exclusive prices to comply with EU invoicing
rules.111Invoice line item tax rate percentage2This is always required. It’s
sufficient to display the tax percentage amount for an invoice line item. You’re
not required to display the cash amount per invoice line item.You can determine
the tax to display on an invoice by:- Using [Stripe
Tax](https://docs.stripe.com/tax/invoicing) to automatically calculate the tax.
- ​​Manually adding the tax rate when you are create an item. Select **Item
taxes and coupons**, enter your desired tax rate, then **Create a new tax
rate**.
12Invoice subtotal (excludes VAT)This is always required.Stripe populates this
by default.13VAT amountThis is always required.Stripe populates this by
default.14Invoice total (includes VAT)This is always required.Stripe populates
this by default.N/ACustom fieldsIn some European countries, you must also
display additional information including the business registration number,
purchase order (PO), or payment due date.Under Additional options in the
[Invoice Editor](https://dashboard.stripe.com/invoices/create), click Add custom
field.
1To display tax-exclusive prices with Stripe Tax, select **No** under **Include
tax in price** to exclude tax. This excludes tax in prices in the invoice PDF,
the Invoice Details page, and in the invoice email. You can also select **Yes**
under **Include tax in price**, then check the **Display tax-exclusive prices**
option in the **Items Options** dialog of the **Items** section. This excludes
tax in prices in the invoice PDF, but includes tax on the Invoice Details page
and in the email. If you’re adding tax rates manually for a business, you can
either set **Include tax in price** to **No**, or set **Include tax in price**
to **Yes** and check **Display tax-exclusive prices** in the **Items Options**
dialog. The second approach includes tax on the Invoice Details page and in the
email, but not in the invoice PDF.

2​​If a transaction isn’t subject to tax, you must state the reason for not
applying it. For example, if the tax liability shifts to your customer (that is,
your customer now has to account for tax), you must mention it as a “reverse
charge” on the invoice. In the case of an EU business selling to another EU
business, you must mention “zero-rated intra-Community supply." To include these
references in your invoice, add a custom field under **Additional options** in
the [Invoice Editor](https://dashboard.stripe.com/test/invoices/create).

## Facilitate customer payment

After you set up your invoices to meet European regulations and requirements,
facilitate customer payment by:

- Adding the most popular European payment methods. Lower your costs for B2B and
B2C invoices by accepting bank methods such as [SEPA Direct
Debit](https://docs.stripe.com/payments/sepa-debit) or [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit), or offer
[Klarna](https://docs.stripe.com/payments/klarna) for B2C invoices to give your
customers more flexible payment options, such as [Pay in
3](https://docs.stripe.com/payments/klarna#payment-options) installments.
- Using the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page).
- Picking the right net terms.
- [Localizing your
Invoice](https://docs.stripe.com/invoicing/customize#customer-language) to the
language of your customer.

#### Caution

Stripe Invoicing doesn’t integrate with the Italian government’s e-invoicing
platform.

## See also

- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Account tax IDs](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](https://docs.stripe.com/invoicing/taxes/tax-rates)

## Links

- [Invoice template](https://dashboard.stripe.com/settings/billing/invoice)
- [Public business information](https://dashboard.stripe.com/settings/public)
- [account settings](https://dashboard.stripe.com/settings/account)
- [Stripe Tax](https://docs.stripe.com/tax/invoicing)
- [new tax rate](https://dashboard.stripe.com/test/tax-rates)
- [Invoice Editor](https://dashboard.stripe.com/invoices/create)
- [Invoice Editor](https://dashboard.stripe.com/test/invoices/create)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [Klarna](https://docs.stripe.com/payments/klarna)
- [Pay in 3](https://docs.stripe.com/payments/klarna#payment-options)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Localizing your
Invoice](https://docs.stripe.com/invoicing/customize#customer-language)
- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Account tax IDs](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](https://docs.stripe.com/invoicing/taxes/tax-rates)