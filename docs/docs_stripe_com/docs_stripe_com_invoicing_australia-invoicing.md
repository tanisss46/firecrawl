# Best practices for setting up invoices in Australia

## Learn the best practices for setting up invoices in Australia.

*Last updated Feb 6, 2025*

#### Legal Disclaimer

The information on this page is for your general guidance and isn’t legal
advice.

Learn the best practices for setting up invoices in Australia when you make
sales to customers, particularly if a customer requests a tax invoice which must
contain certain information.

## Key invoice fields

We don’t automatically populate all of the fields on an invoice. In Australia, a
missed or improperly added field can render an invoice non-compliant. If you
intend to create a tax invoice, make sure that you include the required fields
when you prepare your invoices.

![Key invoice
details](https://b.stripecdn.com/docs-statics-srv/assets/invoice-australia-config-annotation.810aa4be73b8e58cf9d3d1a7319af29a.png)

Key invoice details

## How to add an invoice field

The following table explains how you can populate the invoice fields referenced
in the example image. To make sure that your invoices are compliant and adhere
to applicable geographic requirements, we recommend you consult with your tax
and legal advisors.

KeyFieldRequirementsHow to populate1Invoice titleRequiredStripe applies the
default title Invoice . If issuing tax invoices to Australian businesses, Add
custom field `Tax Invoice` as a subtitle.2Your Business company
nameRequiredStripe populates the seller’s identity by default from the business
profile.3Your Australian Business Number (ABN)RequiredAdd your ABN in your
[invoice settings](https://dashboard.stripe.com/settings/billing/invoice) so
Stripe can include it on your invoices by default.4Date of issueRequiredStripe
populates this by default.5Brief description of the item soldRequiredStripe
populates this by default with the quantity (if applicable) and the pricing.6GST
amount (if any)Exact amount required for sales of AUD1000 or more. Sales of less
than AUD1000 can advise that Total price includes GST (provided the GST amount
is exactly one-eleventh of the total price).Determine the GST to display on an
invoice using [Stripe Tax](https://docs.stripe.com/tax/invoicing) to
automatically calculate the tax, or manually add the tax rate as follows when
you create an item:- Select **Item taxes and coupons**.
- Enter your desired tax rate.
- Create a [new tax rate](https://dashboard.stripe.com/test/tax-rates).
7Invoice total (including GST, if applicable)RequiredStripe populates this by
default, including the GST amount provided in field 6, if applicable.8GST
included in each line itemRequired for sales of AUD1000 or moreDetermine the GST
to display for each line item using the methods described for field 6.9Total
price excluding GSTRecommendedStripe populates this by default.10Buyer’s
identityRequired for sales of AUD1000 or moreStripe populates this by default.
Add this information in the Customer view of the Dashboard or using the [Create
Customer Tax ID](https://docs.stripe.com/api/customer_tax_ids/create)
API.11Invoice numberRecommendedStripe populates this by default. You can specify
invoice numbering (customer or account level) in the [Invoice
template](https://dashboard.stripe.com/settings/billing/invoice).12Date
dueRecommendedStripe populates this by default.13Your Business company
addressRecommendedStripe populates this if you provide your Support address in
the [Public business information](https://dashboard.stripe.com/settings/public)
of your profile. You can also default to your business address as listed in your
[account settings](https://dashboard.stripe.com/settings/account).14Invoice line
item supply dateRecommended if the supply date of individual line items differs
from the invoice send date.Click the toggle under Item options to display line
item supply dates.N/ACustom fieldsRecommended for additional information, such
as:- PO number
- To indicate that the total amount of taxable sale is inclusive or exclusive of
GST
- To add **Tax Invoice** as a subtitle
In the Invoice Editor, click Add custom field from the Additional options
section.
## Facilitate customer payment

After you set up your invoices to meet Australian requirements, you can
facilitate customer payment by:

- Adding the most popular Australian payment methods. By accepting a wider range
of payment methods, such as [BECS Direct
Debit](https://docs.stripe.com/payments/au-becs-debit) and
[PayTo](https://docs.stripe.com/payments/payto), you can lower your costs and
increase conversions.
- Using the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page).
- Allowing a customer to pay a single invoice [over multiple due
dates](https://docs.stripe.com/invoicing/payment-plans). By reflecting a payment
schedule, you can extend more flexible net terms or collect a deposit.

## Invoice payment plans

[Invoice payment plans](https://docs.stripe.com/invoicing/payment-plans) allow
customers to pay a single invoice over multiple due dates. You can specify
flexible net terms or collect a deposit. With this feature, Stripe doesn’t
provide you or your customers with any form of credit, nor does Stripe charge
additional fees to you or your customers for this feature.

Consult your legal advisors regarding any restrictions and requirements that
apply to your implementation before setting up invoices. Any credit, lending, or
“Buy Now Pay Later” type services that you provide might be subject to
regulation in Australia.

## See also

- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Account tax IDs](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](https://docs.stripe.com/invoicing/taxes/tax-rates)

## Links

- [invoice settings](https://dashboard.stripe.com/settings/billing/invoice)
- [Stripe Tax](https://docs.stripe.com/tax/invoicing)
- [new tax rate](https://dashboard.stripe.com/test/tax-rates)
- [Create Customer Tax ID](https://docs.stripe.com/api/customer_tax_ids/create)
- [Public business information](https://dashboard.stripe.com/settings/public)
- [account settings](https://dashboard.stripe.com/settings/account)
- [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit)
- [PayTo](https://docs.stripe.com/payments/payto)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [over multiple due dates](https://docs.stripe.com/invoicing/payment-plans)
- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Account tax IDs](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](https://docs.stripe.com/invoicing/taxes/tax-rates)