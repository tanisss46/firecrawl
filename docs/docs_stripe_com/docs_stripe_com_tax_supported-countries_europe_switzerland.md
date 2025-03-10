# Collect tax in Switzerland and Liechtenstein

## Learn how to use Stripe Tax to calculate, collect, and report tax in Switzerland and Liechtenstein.

In Switzerland and Liechtenstein, Stripe Tax supports calculation and collection
of [VAT](https://www.estv.admin.ch/estv/en/home/value-added-tax.html).
Switzerland and Liechtenstein apply the same VAT rules and are considered one
country for VAT purposes.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Switzerland and
Liechtenstein. Stripe also notifies you with email and Dashboard alerts when you
need to register to collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Foreign businesses that sell to customers in Liechtenstein or Switzerland must
register with the Swiss tax administration if their global taxable turnover
exceeds 100,000 CHF in a calendar year. They must also register if they expect
their global taxable turnover to exceed 100,000 CHF in the next 12 months.

If your business meets those criteria, then when you make your first taxable
transaction in Switzerland or Liechtenstein, you must appoint a Swiss
representative and register in Switzerland.

You don’t need to register in the following cases:

- Your only sales in Switzerland and Liechtenstein are to businesses (B2B), and
the sales are subject to reverse charge.
- You provide only tax-exempt services to customers in Switzerland and
Liechtenstein.

**Threshold**: 100,000 CHF (global)

**Period**: 12 months

**Included transactions**: All global taxable transactions.

## Register to collect tax

Foreign businesses must appoint a fiscal representative to register for VAT
purposes in Switzerland and provide cash or bank guarantee for future VAT
liabilities.

Find more information on how to register for VAT in Switzerland on the
[government
website](https://www.estv.admin.ch/estv/en/home/value-added-tax.html).

After you’ve registered to collect tax in Switzerland, open your Dashboard and
go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=ch) to
add your registrations to Stripe. That turns on tax calculation and collection
in Stripe for your transactions in Switzerland and Liechtenstein.

Learn more about [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

Stripe calculates VAT for your transactions in Switzerland and Liechtenstein.
Stripe considers most goods and services sales taxable unless explicitly
exempted.

If your business is registered to collect VAT in Switzerland, you must collect
VAT on all taxable services you sell in Switzerland or Liechtenstein. However,
if you’re based outside of Switzerland and Liechtenstein and aren’t registered
to collect VAT, then most services you provide in Switzerland or Liechtenstein
are subject to reverse charge. Reverse charge applies to services provided to
customers who are registered for VAT or who acquire services exceeding 10,000
CHF in a calendar year that are subject to reverse charges.

Stripe does not support the special [Swiss VAT
rule](https://www.gate.estv.admin.ch/mwst-webpublikationen/public/pages/taxInfos/cipherDisplay.xhtml?publicationId=1551451&componentId=1551564)
that mandates foreign businesses with annual sales in low-value goods to Swiss
customers exceeding CHF 100,000 to levy Swiss VAT on their sales of goods. The
definition of low-value goods varies based on the tax rate: it includes items
priced below CHF 62 if the applicable tax rate is 8.1%, and items priced below
CHF 193 if subject to a 2.6% tax rate.

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

- [VAT](https://www.estv.admin.ch/estv/en/home/value-added-tax.html)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=ch)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [Swiss VAT
rule](https://www.gate.estv.admin.ch/mwst-webpublikationen/public/pages/taxInfos/cipherDisplay.xhtml?publicationId=1551451&componentId=1551564)
- [tax filing](https://docs.stripe.com/tax/filing)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)