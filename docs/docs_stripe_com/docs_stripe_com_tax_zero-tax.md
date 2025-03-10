# Zero tax amounts and reverse charges

## Learn about cases when Stripe Tax calculates zero tax.

#### Note

[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

Stripe Tax returns a tax calculation result on every request. However, Tax isn’t
collected on a transaction in some situations, and the resulting tax amount is
zero. For example, if you’re expanding `tax_amounts` on an
[invoice](https://docs.stripe.com/api/invoices), you might see something like:

```
{
 "id": "in_1HF0KNFsnTpWVWVzFDgSizOj",
 "object": "invoice",
 ...
 "total_details": {
 "amount_tax": 0,
 "breakdown": {
 "taxes": [
 {
 "amount": 0,
 "taxability_reason": "not_collecting",
 "rate": {
 "id": "txr_1HHwa4Jm3J7Jh9FBnYJ9glJZ",
 "object": "tax_rate",
 "description": "VAT Germany",
 "display_name": "VAT",
 "country": "DE",
 "created": 1597863856,
 "inclusive": false,
 "jurisdiction": "DE",
 "livemode": false,
 "metadata": {},
 "percentage": 0.0,
 "state": null,
 "tax_type": "vat",
 "active": false,
 }
 }
 ]
 },
 },
 ...
}
```

The API returns the reason for a tax result in the
[taxability_reason](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-tax_amounts-taxability_reason)
field.

The most common reasons for a zero tax result are the following:

Reasontaxability_reasonExplanationNot registered`not_collecting`You must
register before collecting tax in a jurisdiction. You can specify where you’re
registered to collect tax on [the Tax settings
page](https://dashboard.stripe.com/settings/tax).Exempt or zero-rated
products`product_exempt`Certain products are exempt from tax or zero-rated. In
both cases the buyer doesn’t pay tax.Reverse charge`reverse_charge`Transactions
between two businesses might be subject to reverse charge. In these cases, the
buyer is responsible for accounting for the VAT due under the reverse
charge.Exempt customers`customer_exempt`Some customers are exempt from paying
indirect tax in certain jurisdictions. You can specify when a customer is exempt
on the Customer object.Excluded territory`not_supported`Some countries have
administrative subdivisions or territories, with the geographic region being
outside the scope of the associated country’s VAT system. A list of these
excluded territories is below.

!

The tax outcome for each payment is available when viewing a payment in [the
Dashboard](https://dashboard.stripe.com/) under Taxability.

## Situations where Stripe calculates zero tax

Stripe Tax calculates zero tax in the following situations:

### Not registered

Taxing authorities require businesses to obtain a license or otherwise register
before starting to collect tax in their jurisdiction. Each jurisdiction has
their own rules regarding when you’re obligated to register and begin collecting
and remitting tax. Obligations can arise from, but are not limited to, a
physical presence in the jurisdiction or from reaching a threshold of sales into
a jurisdiction. For example, as of February 2021, for businesses based outside
of California (for example, no physical presence), you only need to register
when you surpass 500,000 USD in sales.

Stripe automatically aggregates and analyzes your transactions and compares them
to local thresholds. See
[Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights about
your potential tax registration obligations.

Learn more about how to [register for sales tax, VAT, and
GST](https://docs.stripe.com/tax/supported-countries) in each location and, if
you’re a Connect platform, how to [use the Registrations API to manage tax
registrations](https://docs.stripe.com/tax/registrations-api). You can also use
[Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register) on your
behalf.

### Exempt or zero rated products

Products might be exempt or nontaxable in some jurisdictions. For example, as of
February 2021, the state of California considers software as a service to be a
nontaxable service. The buyer pays no tax and the seller usually can’t reclaim
any credits from costs associated with producing the product.

Products can also be zero-rated, meaning while they’re technically taxable, the
applied rate is 0%. For example, as of February 2021, children’s clothing is
zero-rated in Ireland. The buyer pays no tax, however the seller might be able
to reclaim credits from costs associated with producing the product.

The tax treatment of products not only varies by jurisdiction but is subject to
change. If you don’t want to collect tax on a given product, you can assign the
product tax code Nontaxable (`txcd_00000000`) to it, to make sure Stripe Tax
treats it as a nontaxable product. Otherwise, Stripe Tax automatically
determines when a product is exempt or zero rated.

### Reverse charges

While in most transactions, the seller is responsible for collecting and
remitting tax owed by the buyer, in a reverse charge transaction the buyer must
calculate and remit the tax. In that case, the seller’s invoice specifies that
the transaction is a reverse charge and doesn’t include tax in the total amount.
A reverse charge is common in cross-border B2B supply of services. For example,
for businesses with an origin address in the EU, the following logic applies:

Buyers fromB2CB2BSame EU countryCharge VATCharge VATDifferent EU countryCharge
VATNo VAT (reverse charge)
Stripe Tax automatically applies the right logic depending on the presence of a
tax ID and the jurisdictions involved in the transaction.

For transactions with `inclusive` tax behavior where reverse charge applies, the
buyer pays the full `unit_amount` Price, but isn’t charged tax. In these cases,
a “Reverse Charge” indicator appears in the Stripe Dashboard, and the Invoice
reads “Tax to be paid on reverse charge basis” instead of zero.

You can set a customer’s
[tax_exempt](https://docs.stripe.com/api/customers/object#customer_object-tax_exempt)
attribute to `reverse` even if you haven’t collected their tax ID in Stripe.

You can also instruct Checkout to collect tax IDs from your customers by setting
[tax_id_collection](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-tax_id_collection).
For one-time Checkout purchases not associated with a Customer object, Checkout
collects and stores the customer’s tax exemption status and supplied tax IDs in
[customer_details](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details)
on the completed Checkout Session object. You’re responsible for making sure
that customer information is accurate (including their supplied tax
identification numbers).

The following examples show invoices generated with and without a known customer
tax ID:

- [Customer’s tax ID automates reverse charge
(PDF)](https://d37ugbyn3rpeym.cloudfront.net/docs/files/billing/taxes/example-reverse-charge.pdf)
- [Explicitly set reverse charge
(PDF)](https://d37ugbyn3rpeym.cloudfront.net/docs/files/billing/taxes/example-reverse-charge-customer.pdf)

Stripe displays the provided customer tax ID on an invoice, regardless of
whether it’s valid. Stripe Tax automatically validates the tax ID format against
the expected format and the tax ID value against external tax authority systems
for certain countries.

[Learn more about Tax IDs](https://docs.stripe.com/billing/customer/tax-ids)

## Exempt customers

Exempt customers are those who under a jurisdiction’s rules can make tax-exempt
purchases. Each taxing jurisdiction determines the type of individuals or
entities who can make tax-exempt purchases. Common examples are nonprofit
organizations and government entities.

If you have customers that are exempt from paying tax, set their tax status to
`exempt` and provide the customer ID when creating a subscription, invoice, or
Checkout Session. To set a customer’s exempt status, use the API to set
[tax_exempt](https://docs.stripe.com/api/customers/object#customer_object-tax_exempt)
to `exempt` or use the Dashboard:

- On the [Customers page](https://dashboard.stripe.com/customers), select the
customer.
- Open the overflow menu () and select **Edit information**.
- Scroll to the **Tax status** section and select **Exempt** from the dropdown.

For transactions with `inclusive` tax behavior where the customer is exempt, the
buyer pays the full `unit_amount` Price, but there’s no tax charged. In these
cases, an “Exempt” indicator appears in the Stripe Dashboard and the Invoice
reads “Customer is tax exempt” instead of zero.

[Download example exempt invoice
PDF](https://d37ugbyn3rpeym.cloudfront.net/docs/files/billing/taxes/example-exempt.pdf)

Stripe Tax automatically calculates an exemption on the transaction when you set
[tax_exempt](https://docs.stripe.com/api/customers/object#customer_object-tax_exempt)
on the `Customer` object, but it doesn’t perform any validation of required
documentation for supporting an exemption, such as customer exemption
certificates. You are responsible for determining and fulfilling any obligation
to validate your customer’s exempt status and collect any required
documentation, such as an exemption certificate. [EXEMPTAX offers a Stripe
App](https://marketplace.stripe.com/apps/exemptax) that you can use to collect
and verify exemption certificates.

## Excluded territories

#### Note

Stripe Tax fees apply to transactions in excluded territories if you’re
registered in the country the territory is located in.

Some countries include administrative subdivisions or territories that are
outside the scope of their general VAT system. In some of these territories no
tax is levied, while others may have their own tax regulations and rates.

Stripe Tax does not calculate tax in the territories listed below even if you’re
registered in the country where the territory belongs to. Stripe Tax
automatically determines if your customer is based in an excluded or unsupported
territory using the postal code and jurisdiction name.

CountryExcluded TerritoriesAndora- Andora
Denmark- Faroe Islands
- Greenland
Finland- Åland Islands
France- French Guyana
- French Polynesia
- Guadalupe
- Martinique
- Mayotte
- Reunion
- Saint Barthélemy
- Saint Martin
- Saint Pierre and Miquelon
- Wallis and Futuna
Italy- Vatican City
Liechtenstein- Liechtenstein
Monaco- Monaco
Netherlands- Aruba
- Bonaire
- Curacao
- Saba
- Sint Eustatius
- Sint Maarten
Norway- Jan Mayen
- Svalbard
Portugal- Azores
- Madeira
San Marino- San Marino
Spain- Canary Islands
- Ceuta
- Melilla
United Kingdom- British Virgin Islands
- Channel Islands (Guernsey and Jersey)
- Falkland Islands
- Gibraltar

## See also

- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)
- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Use Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [Reporting and filing](https://docs.stripe.com/tax/reports)

## Links

- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [invoice](https://docs.stripe.com/api/invoices)
-
[taxability_reason](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-tax_amounts-taxability_reason)
- [the Dashboard](https://dashboard.stripe.com/)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [register for sales tax, VAT, and
GST](https://docs.stripe.com/tax/supported-countries)
- [use the Registrations API to manage tax
registrations](https://docs.stripe.com/tax/registrations-api)
- [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
-
[tax_exempt](https://docs.stripe.com/api/customers/object#customer_object-tax_exempt)
-
[tax_id_collection](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-tax_id_collection)
-
[customer_details](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details)
- [Customer’s tax ID automates reverse charge
(PDF)](https://d37ugbyn3rpeym.cloudfront.net/docs/files/billing/taxes/example-reverse-charge.pdf)
- [Explicitly set reverse charge
(PDF)](https://d37ugbyn3rpeym.cloudfront.net/docs/files/billing/taxes/example-reverse-charge-customer.pdf)
- [Learn more about Tax IDs](https://docs.stripe.com/billing/customer/tax-ids)
- [Customers page](https://dashboard.stripe.com/customers)
- [Download example exempt invoice
PDF](https://d37ugbyn3rpeym.cloudfront.net/docs/files/billing/taxes/example-exempt.pdf)
- [EXEMPTAX offers a Stripe App](https://marketplace.stripe.com/apps/exemptax)
- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)
- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Reporting and filing](https://docs.stripe.com/tax/reports)