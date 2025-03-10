# Collect tax in the United Kingdom

## Learn how to use Stripe Tax to calculate, collect, and report tax in the UK.

In the United Kingdom (UK), Stripe Tax supports calculation and collection of
[VAT](https://www.gov.uk/how-vat-works).

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in the United Kingdom. Stripe
also notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

If you’re based outside the United Kingdom, you must register in the UK within
30 days of performing the first taxable transaction there. You’re also liable to
register if you have reasonable grounds to believe that you’ll perform taxable
transactions within the next 30 days. A taxable transaction is any sale made in
the UK that’s neither exempt from VAT nor subject to reverse charge. Taxable
transactions include those that are zero-rated for VAT purposes.

For example, if you’re based in the United States (US) and sell digital services
to overseas customers, you must register in the UK as soon as you have
reasonable grounds to believe that a UK customer will purchase your services. If
a UK consumer has already bought your digital services, you must register within
30 days of performing the sale. However, if you only sell to UK businesses, you
don’t need to register because such sales are subject to reverse charge and
don’t constitute taxable transactions for UK VAT purposes.

The HMRC VAT Notice 700/1 [Who should register for
VAT](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-should-i-be-registered-for-vat#Exempt-supplies)
provides more information on registration in the UK.

- **Threshold**: 1 transaction in the UK.
- **Included transactions**: Any taxable transactions that reverse charge
doesn’t apply to.

If a remote business sells digital services or low-value goods into the UK
exclusively through online marketplaces that are responsible for collecting tax
on these sales, the seller isn’t required to register for UK VAT. These sales
don’t count towards the seller’s registration threshold.

## Register to collect tax

Find more information on how to register for VAT in the United Kingdom on the
government website:

- [General information about UK VAT](https://www.gov.uk/how-vat-works)
- [How to register](https://www.gov.uk/register-for-vat)

After you’ve registered to collect tax in the United Kingdom, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=gb) to
add your registrations to Stripe in the Dashboard. This turns on tax calculation
and collection in Stripe for your transactions in the United Kingdom.

Note that the [One-Stop Shop (OSS)
registrations](https://docs.stripe.com/tax/supported-countries/european-union#outside-eu-businesses-non-union-oss)
don’t allow tax calculations in the UK, as the UK is no longer part of the EU.
UK businesses can register for OSS schemes to collect taxes within the EU.

Learn more about [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

Stripe calculates VAT for your transactions in the United Kingdom. Stripe
assumes most sales to be taxable unless specifically exempted. If you’re a
remote seller providing digital services to UK customers, UK VAT is typically
collected on sales to individuals. Tax isn’t charged on sales to business
customers who provide their VAT identification number.

Stripe doesn’t calculate VAT on imported low-value goods that are shipped into
the UK in packages valued at 135 GBP or less.

The United Kingdom has some territories outside the scope of the standard tax
system that have different rules. Stripe won’t calculate tax for customers based
there, even if you’ve added a registration for the UK. This applies to the
following locations:

- British Virgin Islands
- Channel Islands (Guernsey and Jersey)
- Falkland Islands
- Gibraltar

Learn more about how Stripe handles [excluded
territories](https://docs.stripe.com/tax/zero-tax?#excluded-territories).

Northern Ireland applies its own special VAT rules. If you sell goods into
Northern Ireland, you have to follow the same rules as other European Union
countries. But if you sell services, you have to charge taxes based on the laws
of the United Kingdom. Stripe Tax doesn’t support sales of goods to Northern
Ireland.

## Report and file your taxes

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

Stripe also provides reports of your completed tax transactions. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports. Learn more about [the different types of
reports](https://docs.stripe.com/tax/reports).

## Marketplace tax liability

The UK uses the terms “online marketplace operators” and “digital platform
operators” to refer to marketplace operators that might have tax collection
obligations. To qualify as an online marketplace operator, the business must set
terms or conditions for the sale, process or enable customer payments, or handle
ordering or delivery of the product. A business isn’t considered an online
marketplace if it only processes payments, lists or advertises goods, or
redirects customers to other websites or apps without further involvement in the
sale.

The tax collection obligation for marketplace operators typically includes:

- Sales of digital services
- Sales of goods by remote sellers to UK private individuals when the goods are
in the UK at the point of sale.
- Sales of goods to UK private individuals if the goods are imported into the UK
in packages valued at 135 GBP or less.

Marketplace operators facilitating other types of sales might need to collect
VAT based on different indicators and contractual arrangements.

A marketplace operator that collects UK VAT on a sale is treated as if it were
buying the product from the merchant and selling it to the customer. This
applies only for VAT purposes and doesn’t change the commercial position where
the title to the product passes from the seller to the buyer.

## Links

- [VAT](https://www.gov.uk/how-vat-works)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Who should register for
VAT](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-should-i-be-registered-for-vat#Exempt-supplies)
- [How to register](https://www.gov.uk/register-for-vat)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=gb)
- [One-Stop Shop (OSS)
registrations](https://docs.stripe.com/tax/supported-countries/european-union#outside-eu-businesses-non-union-oss)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [excluded
territories](https://docs.stripe.com/tax/zero-tax?#excluded-territories)
- [tax filing](https://docs.stripe.com/tax/filing)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)