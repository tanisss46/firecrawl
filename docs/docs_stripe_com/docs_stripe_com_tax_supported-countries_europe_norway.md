# Collect tax in Norway

## Learn how to use Stripe Tax to calculate, collect, and report tax in Norway.

In Norway, Stripe Tax supports calculation and collection of
[VAT](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/).

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Norway. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

If you’re based outside Norway, you must register in Norway as soon as your
taxable sales in Norway reach 50,000 NOK during a period of 12 months and no
reverse charge applies. Businesses located in the [European Economic
Area](https://en.wikipedia.org/wiki/European_Economic_Area) can register
directly with the Norwegian tax administration. Businesses located outside the
EEA must appoint a Norwegian VAT representative unless they use the simplified
registration procedure (VOEC), which is available for B2C sales of digital
services and low-value goods (< ​3,000 NOK).

For example, if you’re based in the US, sell digital services to Norwegian
consumers and exceed the threshold during a period of 12 months (from February
of the past year to January of the current year), you must register in Norway.
However, if you sell digital services only to Norwegian businesses, you don’t
need to register because these services are subject to reverse charge.

- **Threshold**: 50,000 NOK
- **Period**: 12 months
- **Included transactions**: Any taxable transactions that reverse charge
doesn’t apply to.

## Register to collect tax

Find more information on how to register for VAT in Norway on the government
website:

- [General information about VAT in
Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/)
- [How to
register](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/)

After you’ve registered to collect tax in Norway, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=no) to
add your registrations to Stripe in the Dashboard. This turns on tax calculation
and collection in Stripe for your transactions in Norway.

Learn more about [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

Stripe calculates VAT for your transactions in Norway.

Generally, most transactions are taxable in the jurisdiction where your customer
is. Stripe assumes the sale of most goods or services to be taxable unless
specifically exempted.

In Norway, there are some territories outside of the scope of the standard tax
system and might have different rules that apply. Stripe won’t calculate tax for
customers based there, even if you’ve added a registration for Norway. Learn
more about how Stripe handles [excluded
territories](https://docs.stripe.com/tax/zero-tax?#excluded-territories). This
applies to the following locations:

- Jan Mayen
- Svalbard

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

## Links

-
[VAT](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [How to
register](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=no)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [excluded
territories](https://docs.stripe.com/tax/zero-tax?#excluded-territories)
- [tax filing](https://docs.stripe.com/tax/filing)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)