# Collect tax in Europe (outside the EU)

## Learn how to use Stripe Tax to calculate, collect, and report tax in Europe (outside the EU).

In Europe, Stripe supports tax calculation in the following countries which are
outside of the European Union. Stripe also supports tax calculation in all of
the countries in the European Union (EU). Learn more about [tax support for the
European Union](https://docs.stripe.com/tax/supported-countries/european-union).

Click the links below to learn about the thresholds in each country and the
types of goods and services we support.

- [Albania](https://docs.stripe.com/tax/supported-countries/europe/albania)
- [Belarus](https://docs.stripe.com/tax/supported-countries/europe/belarus)
- [Bosnia and
Herzegovina](https://docs.stripe.com/tax/supported-countries/europe/bosnia-and-herzegovina)
- [Iceland](https://docs.stripe.com/tax/supported-countries/europe/iceland)
- [Moldova](https://docs.stripe.com/tax/supported-countries/europe/moldova)
-
[Montenegro](https://docs.stripe.com/tax/supported-countries/europe/montenegro)
- [North
Macedonia](https://docs.stripe.com/tax/supported-countries/europe/north-macedonia)
- [Norway](https://docs.stripe.com/tax/supported-countries/europe/norway)
- [Russia](https://docs.stripe.com/tax/supported-countries/europe/russia)
- [Serbia](https://docs.stripe.com/tax/supported-countries/europe/serbia)
-
[Switzerland](https://docs.stripe.com/tax/supported-countries/europe/switzerland)
- [Ukraine](https://docs.stripe.com/tax/supported-countries/europe/ukraine)
- [United
Kingdom](https://docs.stripe.com/tax/supported-countries/europe/united-kingdom)

## When and how to register for tax collection

Different rules determine when and how you need to register to collect tax
depending on the country. Click the links above to learn about the thresholds
for tax collection in each location.

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in each location. Stripe only
monitors if you have reached a tax threshold for sales outside of the country
your business is based in. Stripe also notifies you with email and Dashboard
alerts when you need to register to collect tax. Learn more about how the
[monitoring tool works](https://docs.stripe.com/tax/monitoring).

In Albania, Belarus, Bosnia and Herzegovina, Iceland, Moldova, Montenegro, North
Macedonia, Russia, Serbia, and Ukraine your business needs to be a remote seller
with no physical presence (such as a shop or warehouse) to collect tax on
Stripe.

After you’ve registered with a country, go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to add your
registrations to Stripe in the Dashboard to start collecting tax on your
transactions in that location.

## How we calculate taxes

What you sell and where you sell impacts how tax is calculated on your sales.
There are also different rules that apply when your customer is located in the
same country as your business or located somewhere else. Stripe can calculate
tax for [any of the product tax codes you assign to your
products](https://docs.stripe.com/tax/tax-codes) and for domestic and
cross-border sales in Norway, Switzerland, and the United Kingdom. For the other
countries listed, Stripe only supports calculation for [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) sold by remote
sellers.

### Domestic transactions

A transaction where your business and your customer are in the same country is
called a domestic transaction. Stripe assumes the sale of most goods or services
to be taxable unless the tax authority has specifically made them exempt. In
this region, Stripe only supports calculation for domestic transactions in
Norway, Switzerland, United Arab Emirates, and the United Kingdom.

### Cross border transactions

A cross-border transaction is where your customer is located in a different
country to your business or when goods are shipped from one country to another.

Stripe calculates tax on a cross-border transaction taking into account the
following factors:

- the location of your business
- the tax registrations you’ve added to Stripe
- the location of the buyer
- the type of the product sold (based on which [product tax
code](https://docs.stripe.com/tax/tax-codes) you assigned to your product)
- the status of the customer (whether they’re an individual or a business)

#### Digital products

Digital products are non-physical items or services that are delivered, given,
or rendered electronically. This includes digital goods and electronically
supplied services. We determine whether you’re selling digital products or
physical goods using the [product tax
code](https://docs.stripe.com/tax/tax-codes) you assigned to your product.

Digital products are generally taxable in the country where your customer is
located. However sales of digital products to businesses in other countries
might have reverse charge applied. With reverse charge, your business provides
an invoice for the purchase so that your customer can calculate the tax.

#### Physical goods

When physical goods are shipped to a customer in a different country to your
business, the transaction is referred to as an export. Exports are zero rated
and Stripe applies the [zero rate](https://docs.stripe.com/tax/zero-tax). The
transaction might still be subject to taxes and customs duties in the country
your customer is in. Stripe doesn’t calculate these.

In Saudi Arabia and Türkiye, Stripe only supports calculation for [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) and not physical
goods.

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

Stripe also provides reports of your completed tax transactions. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports. Learn more about [the different types of
reports](https://docs.stripe.com/tax/reports).

## Links

- [tax support for the European
Union](https://docs.stripe.com/tax/supported-countries/european-union)
- [Albania](https://docs.stripe.com/tax/supported-countries/europe/albania)
- [Belarus](https://docs.stripe.com/tax/supported-countries/europe/belarus)
- [Bosnia and
Herzegovina](https://docs.stripe.com/tax/supported-countries/europe/bosnia-and-herzegovina)
- [Iceland](https://docs.stripe.com/tax/supported-countries/europe/iceland)
- [Moldova](https://docs.stripe.com/tax/supported-countries/europe/moldova)
-
[Montenegro](https://docs.stripe.com/tax/supported-countries/europe/montenegro)
- [North
Macedonia](https://docs.stripe.com/tax/supported-countries/europe/north-macedonia)
- [Norway](https://docs.stripe.com/tax/supported-countries/europe/norway)
- [Russia](https://docs.stripe.com/tax/supported-countries/europe/russia)
- [Serbia](https://docs.stripe.com/tax/supported-countries/europe/serbia)
-
[Switzerland](https://docs.stripe.com/tax/supported-countries/europe/switzerland)
- [Ukraine](https://docs.stripe.com/tax/supported-countries/europe/ukraine)
- [United
Kingdom](https://docs.stripe.com/tax/supported-countries/europe/united-kingdom)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [any of the product tax codes you assign to your
products](https://docs.stripe.com/tax/tax-codes)
- [digital products](https://docs.stripe.com/tax/tax-codes?type=digital)
- [zero rate](https://docs.stripe.com/tax/zero-tax)
- [tax filing](https://docs.stripe.com/tax/filing)
- [the different types of reports](https://docs.stripe.com/tax/reports)