# Collect tax in Thailand

## Learn how to use Stripe Tax to calculate, collect, and report tax in Thailand.

In Thailand, Stripe only supports collecting
[VAT](https://eservice.rd.go.th/rd-ves-web/landing) for digital services. In
Stripe, these are referred to as “digital products.” To collect this tax on
Stripe, you must be a remote seller without a physical presence in the country.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Thailand. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Remote sellers supplying digital goods and services to Thai consumers are
required to register for VAT purposes if their taxable sales of digital goods
and services exceed THB 1.8 million. The threshold period is an accounting
period (for corporations) or a calendar year (for individuals). Remote sellers
are required to register for VAT within 30 days from the day they have satisfied
the registration threshold. As accounting periods vary per company, Stripe uses
a calendar year as the threshold period.

- **Threshold**: THB 1.8 million
- **Time frame**: Calendar year
- **Included transactions**: Business-to-consumer (B2C) sales of digital goods
and services

## Register to collect tax

You must be a remote seller with no physical presence in Thailand to collect
this tax on Stripe.

Find more information on how to register for VAT in Thailand on the [government
website](https://eservice.rd.go.th/rd-ves-web/landing).

After you’ve registered to collect tax in Thailand, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=th) to
add your registrations to Stripe in the Dashboard. This turns on tax calculation
and collection in Stripe for your transactions in Thailand.

Learn more about [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

We only support calculations for [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) (non-physical
items or services that are delivered, given, or rendered electronically) in
Thailand. Stripe doesn’t calculate tax for products that don’t use a digital
product tax code.

View the list of supported [digital product tax
codes](https://docs.stripe.com/tax/tax-codes?type=digital). To calculate taxes
in Thailand, make sure that you [assign a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
to each of your products.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports. Learn more about [the different types of
reports](https://docs.stripe.com/tax/reports).

You’re responsible for filing and remitting your taxes to Thailand. Stripe
doesn’t file taxes on your behalf.

## Links

- [VAT](https://eservice.rd.go.th/rd-ves-web/landing)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=th)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [digital products](https://docs.stripe.com/tax/tax-codes?type=digital)
- [assign a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)