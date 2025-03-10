# How Tax works

## Learn how Stripe Tax helps you automate tax compliance.

To be tax compliant, you need to:

- Understand which locations require you to collect tax.
- Register for tax in those locations.
- Calculate and collect tax.
- Report, file, and remit the tax you collected.

Register for tax

Calculate and collect tax

Report and file your taxes

Monitor where you have tax obligations

You register, Stripe Tax tracks your registrations

Stripe Tax calculates and collects taxes

Stripe Tax exports, you have to report and file (or use our partners)

The Stripe Tax monitoring tool highlights where you have obligations based on
your transactions

The tax compliance cycle
## Indirect taxes with Stripe Tax

Each country handles tax on sold products and services differently, often
calling it by a different name. In the US, businesses deal with [sales
tax](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus).
Throughout Europe, it’s called value-added tax
([VAT](https://stripe.com/guides/introduction-to-eu-vat-and-european-vat-oss)).
Canada and most countries in the Asia Pacific region refer to it as goods and
services tax ([GST](https://stripe.com/guides/tax-registration-process-canada)).

Taxability and tax rates vary by location and category of products you’re
selling. For example, children’s footwear is zero rated in Ireland, but adult
footwear isn’t. Digital services are usually taxed at the standard rate in most
EU countries. However, e-books are subject to the reduced rate.

[Stripe Tax](https://stripe.com/tax) uses your business address, tax
registrations, product tax codes, customers’ locations, and customer status to
determine the correct tax rates for products you sell, in all supported
locations. Read more about [tax
codes](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior) and
[how we calculate](https://docs.stripe.com/tax/calculating) for different
jurisdictions.

## Monitor your obligations and register

You need to identify the locations where you have sales tax, VAT, or GST
obligations and need to register to collect tax. If you sell into multiple
locations, you need to be familiar with the [tax laws in those
locations](https://docs.stripe.com/tax/supported-countries) because the place
where your transaction takes place determines where you’re required to collect
tax. This can be the seller’s country, the buyer’s country, or another location.

As your business grows and you sell to more locations, you need to register to
collect tax in more locations. Stripe Tax tracks your Stripe transactions and
helps you monitor your tax obligations. [Read more about tax obligation
monitoring](https://docs.stripe.com/tax/monitoring).

You must register with the tax authority in a location to collect taxes there.
In some countries and states you have to register before your first transaction,
while others have a registration threshold (such as the number of sales or sales
volume). Take a look at the [locations Stripe Tax
supports](https://docs.stripe.com/tax/supported-countries) along with the
different tax thresholds that apply and links to the tax authority websites.

Stripe Tax tracks your registrations and uses them to calculate and collect
taxes. [Read more about adding your registrations to
Stripe](https://docs.stripe.com/tax/registering).

After you have registered to collect tax with a tax authority, go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to add your
registrations to Stripe in the Dashboard. This turns on tax calculation and
collection in Stripe for your transactions.

## Calculate and collect

After you [set up Stripe Tax in the
Dashboard](https://docs.stripe.com/tax/set-up), Stripe automatically calculates
and collects taxes on your transactions. Alternatively you can use [Stripe Tax
API](https://docs.stripe.com/tax/custom) to calculate taxes on your own custom
payment flows. In either case, to determine which taxes to collect, you or your
customers have to provide customer location information. [Read more about how
Stripe calculates tax](https://docs.stripe.com/tax/calculating).

If you sell to other businesses, your transactions might be subject to reverse
charges. This means that the tax liability shifts to the customer and we don’t
charge tax on the transaction. Stripe Tax uses customer tax identification
numbers to determine whether a transaction is B2B. Adding a tax identification
number to the customer might affect the tax calculation result. Stripe Tax
doesn’t validate whether the provided tax identification number exists or is
valid. [Read about supported tax ID
formats](https://docs.stripe.com/tax/invoicing/tax-ids#supported-tax-ids).

Some individuals or entities might be tax exempt. For example, some US states
have a reseller exemption. You can set an exempt status on customers to reflect
this. [Read more about reverse charges and exempt
customers](https://docs.stripe.com/tax/zero-tax).

## Report, file, and remit

If you’re collecting taxes, you must report, file, and remit (transfer) the
taxes collected in every location that you’re registered in. Make sure you
understand and comply with obligations of each state or country and consult your
tax advisor if you need help. Stripe Tax supports exporting your transactions in
an itemized format to aid with tax reporting. [Read more about Stripe Tax
reports](https://docs.stripe.com/tax/reports).

Stripe Tax doesn’t currently file or remit taxes on your behalf. Submitting tax
returns is key to your tax compliance. For more information, browse the [Tax
Stripe Apps](https://marketplace.stripe.com/categories/tax) on the App
Marketplace.

## See also

- [Frequently asked questions](https://docs.stripe.com/tax/faq)
- [Stripe Tax guides](https://stripe.com/guides/tax-guides)

## Links

- [sales
tax](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)
- [VAT](https://stripe.com/guides/introduction-to-eu-vat-and-european-vat-oss)
- [GST](https://stripe.com/guides/tax-registration-process-canada)
- [Stripe Tax](https://stripe.com/tax)
- [tax
codes](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [how we calculate](https://docs.stripe.com/tax/calculating)
- [tax laws in those locations](https://docs.stripe.com/tax/supported-countries)
- [Read more about tax obligation
monitoring](https://docs.stripe.com/tax/monitoring)
- [Read more about adding your registrations to
Stripe](https://docs.stripe.com/tax/registering)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [set up Stripe Tax in the Dashboard](https://docs.stripe.com/tax/set-up)
- [Stripe Tax API](https://docs.stripe.com/tax/custom)
- [Read about supported tax ID
formats](https://docs.stripe.com/tax/invoicing/tax-ids#supported-tax-ids)
- [Read more about reverse charges and exempt
customers](https://docs.stripe.com/tax/zero-tax)
- [Read more about Stripe Tax reports](https://docs.stripe.com/tax/reports)
- [Tax Stripe Apps](https://marketplace.stripe.com/categories/tax)
- [Frequently asked questions](https://docs.stripe.com/tax/faq)
- [Stripe Tax guides](https://stripe.com/guides/tax-guides)