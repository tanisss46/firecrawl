# Collect tax in the European Union

## Learn how to use Stripe Tax to calculate, collect, and report tax in the EU.

Businesses selling goods and services to customers in the European Union (EU)
might need to collect value added tax (VAT), even if your business isn’t
established (based) in the EU. Although the VAT laws are generally similar
across the EU, the tax rates and rules might vary per country.

## Countries in the EU

Stripe can calculate tax in all of the countries in the European Union. Select
the country your business is based in if you need help finding the right links
to register for tax.

-
[Austria](https://docs.stripe.com/tax/supported-countries/european-union/austria)
-
[Belgium](https://docs.stripe.com/tax/supported-countries/european-union/belgium)
-
[Bulgaria](https://docs.stripe.com/tax/supported-countries/european-union/bulgaria)
-
[Croatia](https://docs.stripe.com/tax/supported-countries/european-union/croatia)
-
[Cyprus](https://docs.stripe.com/tax/supported-countries/european-union/cyprus)
-
[Czechia](https://docs.stripe.com/tax/supported-countries/european-union/czechia)
-
[Denmark](https://docs.stripe.com/tax/supported-countries/european-union/denmark)
-
[Estonia](https://docs.stripe.com/tax/supported-countries/european-union/estonia)
-
[Finland](https://docs.stripe.com/tax/supported-countries/european-union/finland)
-
[France](https://docs.stripe.com/tax/supported-countries/european-union/france)
-
[Germany](https://docs.stripe.com/tax/supported-countries/european-union/germany)
-
[Greece](https://docs.stripe.com/tax/supported-countries/european-union/greece)
-
[Hungary](https://docs.stripe.com/tax/supported-countries/european-union/hungary)
-
[Ireland](https://docs.stripe.com/tax/supported-countries/european-union/ireland)
- [Italy](https://docs.stripe.com/tax/supported-countries/european-union/italy)
-
[Latvia](https://docs.stripe.com/tax/supported-countries/european-union/latvia)
-
[Lithuania](https://docs.stripe.com/tax/supported-countries/european-union/lithuania)
-
[Luxembourg](https://docs.stripe.com/tax/supported-countries/european-union/luxembourg)
- [Malta](https://docs.stripe.com/tax/supported-countries/european-union/malta)
-
[Netherlands](https://docs.stripe.com/tax/supported-countries/european-union/netherlands)
-
[Poland](https://docs.stripe.com/tax/supported-countries/european-union/poland)
-
[Portugal](https://docs.stripe.com/tax/supported-countries/european-union/portugal)
-
[Romania](https://docs.stripe.com/tax/supported-countries/european-union/romania)
-
[Slovakia](https://docs.stripe.com/tax/supported-countries/european-union/slovakia)
-
[Slovenia](https://docs.stripe.com/tax/supported-countries/european-union/slovenia)
- [Spain](https://docs.stripe.com/tax/supported-countries/european-union/spain)
-
[Sweden](https://docs.stripe.com/tax/supported-countries/european-union/sweden)

## When and how to register

Different rules determine when and how you need to register for VAT, depending
on the country your business is located in. After you register with a country,
go to [Registrations](https://dashboard.stripe.com/tax/registrations) to add
your registrations to Stripe in the Dashboard to start collecting tax on your
transactions. Learn more about the different registration schemes [in our
guide](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss).

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in each country in the
European Union. Stripe also notifies you with email and Dashboard alerts when
you need to register to collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

## Businesses based in the EU

### Domestic registration

Domestic registration is the standard VAT registration for businesses selling
goods and services within an EU country. Any business can register, regardless
of their physical location.

Some EU countries allow businesses to wait to register for VAT until their sales
exceed a certain amount (tax registration threshold). However, other EU
countries require all businesses to register, regardless of sales volume. Those
countries use tax collection thresholds. Businesses below the threshold can
apply for special schemes that exempt them from VAT collection obligations. For
detailed information, visit the tax administration websites of each country.

Stripe monitors your registration obligations in the EU countries other than the
country where your business is based. You can go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to add your
domestic registrations to Stripe in the Dashboard and start collecting tax.

If you sell digital services or imported low-value goods exclusively through
online marketplaces and the marketplace operator is responsible for collecting
tax on these sales, you aren’t required to register for VAT in the countries
where your customers are located.

### Smaller sellers

If you sell to customers in other EU countries, you might need to register in
those countries too. You don’t need to register in other EU countries if:

- your total sales are under 10,000 EUR in a calendar year *and*
- you sell digital products or physical goods *and*
- your sales are to individuals and not businesses in another EU country

The VAT rate of the EU country your business is based in applies instead. Stripe
refers to this simplification rule as the small seller option. We determine
whether you’re selling digital products or physical goods using the [product tax
code](https://docs.stripe.com/tax/tax-codes) you assigned to your product.

When you select the **domestic registration** option, you’re asked to indicate
if your business is a small seller with sales below the 10,000 EUR threshold.
You only see this option for the country that you have set as your [origin
address](https://docs.stripe.com/tax/set-up#origin-address). If you choose yes,
we monitor your cross-border transactions in the EU and notify you when you
exceed that threshold.

After you exceed the small seller threshold, you’re required to collect tax in
the country your customers are located in. You can do so in two ways:

- Register domestically in the EU countries your customers are located in
- Register for the [Union One Stop Shop (OSS)
scheme](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) in your home EU
country.

There are three steps to reflect this change in Stripe:

- End your domestic small seller registration in Stripe on
[Registrations](https://dashboard.stripe.com/tax/registrations).
- Add a new domestic registration for the location where your business is based
and select **no** when you’re asked if you’re a small seller.
- Add any other new domestic or One Stop Shop registrations to start collecting
tax in those locations.

### Union One Stop Shop (OSS)

If you sell goods or services to individuals (and not to businesses), you can
register for the Union One Stop Shop (OSS) scheme in the EU country your
business is based in. You won’t have to register with each EU country you sell
goods or services to. Instead you can register for OSS through your home country
VAT website and submit one return for your sales across the EU. You remit all
VAT to your local tax authority, who distributes it to the countries where your
customers are located.

Learn more about [One-Stop
Shop](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss). Select the
country your business is based in [from the
table](https://docs.stripe.com/tax/supported-countries/european-union#eu-countries)
if you need help finding the right links.

### Import One Stop Shop (IOSS)

If you sell physical goods to individuals in the EU and the goods are imported
from outside of the EU in packages (consignments) that are valued at or below
150 EUR, you can register for Import One Stop Shop in the EU country where
you’re based. This means your customer pays VAT when they buy the goods and not
when the goods arrive at the border in the EU. After you register, you can
collect VAT on your sales of these goods to customers across the EU without
having to register in every country. You also only submit one return to the
country you’re based in for the sales of these goods. Stripe assumes that goods
purchased together are shipped together. If a transaction is over 150 EUR, IOSS
won’t apply, which means your customers are charged by Customs when the goods
arrive at the border in the EU.

## Businesses based outside the EU

If your business is based outside the EU, you may need to register to collect
VAT from your first sale in an EU country. There are different VAT registration
options for businesses based outside the EU.

### Domestic registration

You can register to collect VAT in each EU country your customers are based in.
You might be required to appoint a tax representative, depending on the country
you and your customer are located in.

Select the country your customer is based in from the list in the sidebar, if
you need help finding the right links.

If you sell digital services or goods exclusively through online marketplaces
and the marketplace operator is responsible for collecting tax on these sales,
you’re not required to register for VAT.

### Non-Union One Stop Shop (OSS)

This scheme is for businesses based outside the EU selling services to
individuals in the EU. You can choose which EU country you register in. After
you register, you can collect VAT on your sales to customers across the EU
without having to register in every country. You also only need to submit one
return for all your EU sales to the country you registered in. You don’t need to
appoint a tax representative to use the OSS non-Union scheme.

### Import One Stop Shop (IOSS)

If you sell physical goods to individuals in the EU and the goods are imported
in packages (consignments) that are valued at or under 150 EUR, you can register
in the EU country of your choice for Import One Stop Shop. This means your
customer pays VAT when they buy the goods and not when the goods arrive at the
border in the EU. After you register, you can collect VAT on your sales of these
goods to customers across the EU without having to register in every country.
You also only need to submit one return for all your EU sales to the country you
registered in. Businesses based outside the EU normally need to appoint a local
intermediary to register for IOSS. Stripe assumes that goods purchased together
are shipped together. If a transaction is over 150 EUR, IOSS won’t apply, which
means your customers might have to pay taxes and customs duties when the goods
arrive at the border in the EU.

### Union One Stop Shop (OSS)

Businesses based outside of the EU can use this scheme if they sell physical
goods that are located in an EU country and shipped to individuals in other EU
countries.

## How we calculate taxes

Stripe calculates VAT on a transaction using the following pieces of
information:

- the location of your business
- the tax registrations you added to Stripe
- the location of the customer
- the type of the product sold (based on the [product tax
code](https://docs.stripe.com/tax/tax-codes) you assigned to your product)
- the status of the customer (whether or not they’re a VAT-registered business).

## Sales of services

When your business is located in the same country as your customer, Stripe
calculates VAT by applying that country’s tax rates.

When you and your customer are in different countries (cross-border sales),
there are more complicated rules that apply. These rules determine where the
services are considered to be delivered and which country is entitled to collect
the tax. Here’s a summary of how Stripe applies tax on sales of services:

- **Digital goods or electronically supplied services**: Generally taxable in
the customer’s country. For cross-border sales of digital services within the
EU, Stripe Tax prioritizes a [single
address](https://docs.stripe.com/tax/customer-locations#address-hierarchy) as
the customer’s location when calculating tax instead of comparing two pieces of
non-conflicting evidence. However, we store and retain all location evidence
used in the transaction on the Customer object. If you indicated your business
is a [small
seller](https://docs.stripe.com/tax/supported-countries/european-union#eu-businesses-domestic-registration-small-sellers),
the VAT of the country your business is based in applies.
- **Services related to immovable property**: Taxable in the country where the
property is located. Stripe assumes that the property is located in the
customer’s country.
- **Services involving work on movable property**: Taxable in the customer’s
country as Stripe assumes that the work is performed in the customer’s country.
- **Services that can be delivered remotely**: Taxable in the customer’s country
when they’re provided to individuals outside the European Union or other
businesses. When they’re provided to individuals in other EU countries, they’re
taxable in the seller’s country.
- **Other services**: Taxable in the country your business is based in when
provided to individuals. Taxable in the customer’s country when provided to
other businesses. These rules apply if you select a [product tax
code](https://docs.stripe.com/tax/tax-codes) `txcd_20030000` General - Services.

### Reverse charge

In some cases, when you sell services to a VAT-registered business in another EU
country, the customer is responsible for calculating and remitting the VAT.
Those transactions are called [reverse
charge](https://docs.stripe.com/tax/zero-tax#reverse-charges). Your business
must provide an invoice that specifies the reverse charge instead of including a
tax amount.

If your customer is eligible for a reverse charge and provides their VAT ID in
Stripe, we treat their transactions as a reverse charge and don’t calculate tax
for them. If your customer provides a domestic tax identification number,
reverse charge doesn’t apply. The transaction is treated as a
business-to-consumer (B2C) sale, and VAT rules for B2C transactions are
followed.

You can also mark a customer as eligible for [reverse
charge](https://docs.stripe.com/tax/zero-tax#reverse-charges) in the Dashboard
or using the API, even if you haven’t collected a tax ID for that customer. For
information about which tax IDs Stripe validates, see [customer tax
IDs](https://docs.stripe.com/invoicing/customer/tax-ids).

Stripe doesn’t support the following types of reverse charge:

- **Domestic reverse charge**: In some EU countries, a reverse charge can apply
to the sale of some goods and services between businesses in that country.
Stripe supports reverse charge only for cross-border sales, not for sales within
the same country.
- **Cross-border conditions**: Some EU countries have conditions under which
types of services are eligible for reverse charge. For example, a country can
require you to have a domestic registration. Stripe assumes that all services
sold to customers with a business tax ID are eligible for reverse charge.

## Sales of physical goods

When your business is located in the same country as your customer and the goods
are shipped within that country, Stripe calculates tax by applying that
country’s tax rates.

When the goods are shipped to a customer in a different EU country to your
business, Stripe calculates the tax based on the type of customer. Different
rules apply depending on if your customer is an individual or a VAT registered
business.

- **Sales to an individual**: if the sales are to an individual and your
business arranges the delivery (transport), then the goods are taxed using the
rules of the country your customer is based in. The exception is if you’re an
EU-based business and have indicated your business is a [small
seller](https://docs.stripe.com/tax/supported-countries/european-union#eu-businesses-domestic-registration-small-sellers)
in Stripe. The tax of the country your business is based in applies instead.
- **Sales to a VAT registered business**: the sales are taxable in the country
your business is based in. Stripe applies the zero rate if the customer provides
their VAT ID number. If you sell to a business in another EU country and your
customer doesn’t provide a valid VAT ID number, collect VAT from the country
your business is based in. However, Stripe processes these sales in the same way
it processes a sale to an individual.

When the goods are shipped to a customer outside of the EU, Stripe Tax treats
this sale as an export and [applies the zero
rate](https://docs.stripe.com/tax/zero-tax). The transaction might still be
subject to taxes and customs duties in the country your customer is in. Stripe
doesn’t calculate these.

## Report and file your taxes

Stripe provides reports of your completed tax transactions in the EU. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports. Learn more about [the different types of
reports](https://docs.stripe.com/tax/reports).

The way you file tax returns and pay (remit) your taxes depend on which types of
registrations you have.

- **Domestic registration**: you file your tax returns in each country you have
a registration. Some EU countries might require you to appoint a local tax
representative to do this if you’re not based in the EU.
- **One Stop Shop**: you file your tax returns for all your eligible sales
across the EU with the country you have a One Stop Shop registration in. If you
use different OSS schemes, you need to submit a separate return for each scheme.
Learn more about [One-Stop
Shop](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss#4-file-vat-returns).

Select the country you need to file in from the list in the sidebar if you need
help finding the right links.

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

## Marketplace tax liability

The EU uses the term “deemed sellers” to refer to marketplace operators that
might have tax collection obligations. To qualify as a deemed seller, the
business must set terms or conditions for the sale, process or enable customer
payments, or handle ordering or delivery of the product. A business isn’t
considered a deemed seller if it only processes payments, lists or advertises
goods, or redirects customers to other websites or apps without further
involvement in the sale.

The tax collection obligation for marketplace operators usually applies to:

- Sales of digital services.
- Sales of goods by non-EU sellers to EU individuals, if the goods are located
in the EU at the point of sale.
- Sales of goods to EU individuals, where the goods are imported into the EU in
packages valued at 150 EUR or less.

Marketplace operators facilitating other types of sales might be required to
collect VAT on these sales based on other indicators and contractual
arrangements.

A marketplace operator that collects VAT on a sale is treated as if it were
buying the product from the merchant and selling it to the customer. This only
applies for VAT purposes and doesn’t change the commercial position where the
title to the product passes from the seller to the buyer.

## Links

-
[Austria](https://docs.stripe.com/tax/supported-countries/european-union/austria)
-
[Belgium](https://docs.stripe.com/tax/supported-countries/european-union/belgium)
-
[Bulgaria](https://docs.stripe.com/tax/supported-countries/european-union/bulgaria)
-
[Croatia](https://docs.stripe.com/tax/supported-countries/european-union/croatia)
-
[Cyprus](https://docs.stripe.com/tax/supported-countries/european-union/cyprus)
-
[Czechia](https://docs.stripe.com/tax/supported-countries/european-union/czechia)
-
[Denmark](https://docs.stripe.com/tax/supported-countries/european-union/denmark)
-
[Estonia](https://docs.stripe.com/tax/supported-countries/european-union/estonia)
-
[Finland](https://docs.stripe.com/tax/supported-countries/european-union/finland)
-
[France](https://docs.stripe.com/tax/supported-countries/european-union/france)
-
[Germany](https://docs.stripe.com/tax/supported-countries/european-union/germany)
-
[Greece](https://docs.stripe.com/tax/supported-countries/european-union/greece)
-
[Hungary](https://docs.stripe.com/tax/supported-countries/european-union/hungary)
-
[Ireland](https://docs.stripe.com/tax/supported-countries/european-union/ireland)
- [Italy](https://docs.stripe.com/tax/supported-countries/european-union/italy)
-
[Latvia](https://docs.stripe.com/tax/supported-countries/european-union/latvia)
-
[Lithuania](https://docs.stripe.com/tax/supported-countries/european-union/lithuania)
-
[Luxembourg](https://docs.stripe.com/tax/supported-countries/european-union/luxembourg)
- [Malta](https://docs.stripe.com/tax/supported-countries/european-union/malta)
-
[Netherlands](https://docs.stripe.com/tax/supported-countries/european-union/netherlands)
-
[Poland](https://docs.stripe.com/tax/supported-countries/european-union/poland)
-
[Portugal](https://docs.stripe.com/tax/supported-countries/european-union/portugal)
-
[Romania](https://docs.stripe.com/tax/supported-countries/european-union/romania)
-
[Slovakia](https://docs.stripe.com/tax/supported-countries/european-union/slovakia)
-
[Slovenia](https://docs.stripe.com/tax/supported-countries/european-union/slovenia)
- [Spain](https://docs.stripe.com/tax/supported-countries/european-union/spain)
-
[Sweden](https://docs.stripe.com/tax/supported-countries/european-union/sweden)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [in our guide](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [product tax code](https://docs.stripe.com/tax/tax-codes)
- [origin address](https://docs.stripe.com/tax/set-up#origin-address)
- [Union One Stop Shop (OSS)
scheme](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)
- [from the
table](https://docs.stripe.com/tax/supported-countries/european-union#eu-countries)
- [single
address](https://docs.stripe.com/tax/customer-locations#address-hierarchy)
- [small
seller](https://docs.stripe.com/tax/supported-countries/european-union#eu-businesses-domestic-registration-small-sellers)
- [reverse charge](https://docs.stripe.com/tax/zero-tax#reverse-charges)
- [customer tax IDs](https://docs.stripe.com/invoicing/customer/tax-ids)
- [applies the zero rate](https://docs.stripe.com/tax/zero-tax)
- [the different types of reports](https://docs.stripe.com/tax/reports)
- [One-Stop
Shop](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss#4-file-vat-returns)
- [tax filing](https://docs.stripe.com/tax/filing)