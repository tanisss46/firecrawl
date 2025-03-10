# Best practices for setting up invoices in Japan

## Learn the best practices for setting up invoices in Japan.

*Last updated November 7, 2024*

#### Legal Disclaimer

The information on this page is for your general guidance and isn’t legal
advice.

We recommend the following best practices when you make sales to business
customers because Business-to-Business (B2B) sales require compliant invoices
(適格請求書等) under the [Qualified Invoice
System](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0020006-027.pdf)
(適格請求書等保存方式, also known as インボイス制度) in order for the purchaser to claim a tax
credit. Registered businesses (適格請求書等発行事業者)​​ can issue this type of invoice.
There’s no obligation to issue invoices for Business-to-Consumer (B2C) sales.

Invoices (適格請求書)Receipts (適格簡易請求書)
We don’t automatically populate all of the fields on an invoice. In Japan, a
missed or improperly added field can render an invoice noncompliant. If you
intend to utilize the Qualified Invoice System, make sure that you include the
required fields when you prepare your invoices.

You can use [tax calculation with Stripe Tax or Tax
Rates](https://docs.stripe.com/billing/taxes/collect-taxes) to assist with
including tax information in your invoices.

![A sample invoice with various fields annotated, to be referenced against the
table
below](https://b.stripecdn.com/docs-statics-srv/assets/invoice-japan-config-annotations.91eb9198fe857fae2b437125d15460a1.png)

## How to add an invoice field

The following table explains the ways that you can populate different invoice
fields with reference to the Qualified Invoice System. To make sure that your
invoices are compliant and adhere to applicable geographic requirements, we
recommend that you consult with your tax and legal advisors.

KeyFieldRequirementsHow to populate1Invoice numberThere’s no requirement to show
invoice numbers.Stripe populates this by default. You can change how invoices
are numbered (customer or account level) in the [Invoice
template](https://dashboard.stripe.com/settings/billing/invoice).2Date of
issueYou must use this field to list the transaction date (取引年月日), or set line
item supply dates.Stripe populates this by default.3Date dueWhile there’s no
requirement to display the date that a customer must pay an invoice by, it’s a
best practice to do so.Stripe populates this by default.4aBusiness company name
(適格請求書発行事業者の氏名又は名称)This is required.Stripe populates this by default from the
value in [Public business
information](https://dashboard.stripe.com/settings/public) section of the
Dashboard.4bBusiness company addressThere’s no requirement to display your
address.Enter your Support address under [Public business
information](https://dashboard.stripe.com/settings/public). You can also default
to your business address as listed in your [account
settings](https://dashboard.stripe.com/settings/account).5Business registration
number​​Invoices require a business registration number (適格請求書発行事業者の登録番号).You
must add your business registration number as JP TRN in your [invoice
settings](https://dashboard.stripe.com/settings/billing/invoice). Then, each
time you create an invoice, you must set it as your Tax ID under Additional
options.6aRecipient name (書類の交付を受ける事業者の氏名又は名称)This is required.Stripe populates
this by default from the Customer details.6bRecipient addressThere’s no
requirement to display the recipient address.You can add this field by clicking
the Additional details button when you first create a customer.7Name of the good
or service (取引内容)This is required.Stripe populates this by default from the
Invoice Items.8Invoice line item supply date (取引年月日)This is required when the
supply date of individual line items is different from the invoice send date.You
can display line item supply dates by clicking the toggle under Item
options.9Price of the good or serviceIt’s considered a best practice to show the
unit price, quantity, and total payable amount for each invoice line item.Stripe
populates this by default.10Invoice line item tax rate percentageThis is
required to indicate if an item is subject to the reduced tax rate (軽減税率). It’s
sufficient to display the tax percentage amount for an invoice line item. You
aren’t required to display the cash amount of the tax per invoice line
item.Determine the tax to display on an invoice using either of the following
methods:- Use [Stripe Tax](https://docs.stripe.com/tax/invoicing) to
automatically calculate the tax.
- Or, manually add the tax rate when you create an item:- Select **Item taxes
and coupons**.
- Enter your desired tax rate.
- **Create a new tax rate**.
- On the [invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) page, configure
the taxes to round after subtotaling. This setting applies to all invoices
generated from your account.
11Invoice subtotal (excludes tax)This is required.Stripe populates this by
default.12Total tax amounts and rates (税率ごとに区分して合計した対価の額、適用税率、消費税額)This is
required and must include the total tax amount per tax rate.Stripe populates
this by default.13Invoice total (includes tax)This is required.Stripe populates
this by default.
## Facilitate customer payment

After you set up your invoices to meet Japanese requirements, you can facilitate
customer payment by:

- Adding the most popular Japanese payment methods. By accepting a wider range
of payment methods, such as [Bank
Transfers](https://docs.stripe.com/payments/bank-transfers), you can lower your
costs and increase conversions (especially with large customers).
- Using the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page).
- [Localizing your
Invoices](https://docs.stripe.com/invoicing/customize#customer-language) to the
language of your customers.
- Allowing a single invoice to be [paid over multiple due
dates](https://docs.stripe.com/invoicing/payment-plans). By reflecting a payment
schedule, you can extend more flexible net terms or collect a deposit.
If you provide a financial product or service, please consult with your legal
advisors regarding applicable restrictions and requirements before setting up
invoices. Installment payments, lending, credit, and Buy Now Pay Later services
are subject to regulation in Japan and you may need to register or obtain
approvals before engaging in those services.

## Refunds (適格返還請求書)

If you need to produce a refund document (適格返還請求書) for your customer, you can
[issue a credit note](https://docs.stripe.com/invoicing/dashboard/credit-notes).
If you’ve completed the steps above to create invoices with the necessary
fields, such as your business registration number (適格請求書発行事業者の登録番号), the credit
notes will also contain them.

## Connect platforms

Make sure your connected account’s invoices contain the necessary information
required by the Qualified Invoice System, such as the account’s tax ID and
business details. You can [configure the
information](https://docs.stripe.com/invoicing/connect#account-tax-ids) shown on
invoices and receipts that Connect creates.

If you use manual taxes on invoices,
[configure](https://docs.stripe.com/billing/taxes/tax-rates#rounding) the taxes
to round after subtotaling, rather than at the line item level. This setting
applies to all invoices generated across your connected accounts and across
different geographies.

## See also

- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Account tax IDs](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](https://docs.stripe.com/invoicing/taxes/tax-rates)

## Links

- [Qualified Invoice
System](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0020006-027.pdf)
- [tax calculation with Stripe Tax or Tax
Rates](https://docs.stripe.com/billing/taxes/collect-taxes)
- [Invoice template](https://dashboard.stripe.com/settings/billing/invoice)
- [Public business information](https://dashboard.stripe.com/settings/public)
- [account settings](https://dashboard.stripe.com/settings/account)
- [Stripe Tax](https://docs.stripe.com/tax/invoicing)
- [new tax rate](https://dashboard.stripe.com/test/tax-rates)
- [Bank Transfers](https://docs.stripe.com/payments/bank-transfers)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Localizing your
Invoices](https://docs.stripe.com/invoicing/customize#customer-language)
- [paid over multiple due
dates](https://docs.stripe.com/invoicing/payment-plans)
- [issue a credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes)
- [configure the
information](https://docs.stripe.com/invoicing/connect#account-tax-ids)
- [configure](https://docs.stripe.com/billing/taxes/tax-rates#rounding)
- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Account tax IDs](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](https://docs.stripe.com/invoicing/taxes/tax-rates)