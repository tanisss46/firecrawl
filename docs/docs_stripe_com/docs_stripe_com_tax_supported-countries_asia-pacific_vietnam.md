# Collect tax in Vietnam

## Learn how to use Stripe Tax to calculate, collect, and report tax in Vietnam.

In Vietnam, the Foreign Contractor Tax (FCT) applies to sales of digital
services by remote sellers without a physical presence in the country. This tax
consists of VAT and income tax. Stripe only supports collecting VAT for digital
services, which Stripe refers to as digital products. Stripe doesn’t calculate
the income tax component of the FCT.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Vietnam. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Remote sellers providing digital goods or electronically supplied services
(digital products) must register for tax from their first sale there. Sales to
business customers don’t trigger any tax registration obligations as remote
sellers aren’t required to collect tax on those sales.

- **Threshold**: 1 transaction
- **Included transactions**: Sales of digital goods and services

## Register to collect tax

You must be a remote seller with no physical presence in Vietnam to collect this
tax on Stripe.

Find more information on how to register for VAT in Vietnam on the [government
website](https://etaxvn.gdt.gov.vn/nccnn/Request).

After you’ve registered to collect tax in Vietnam, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=vn) to
add your registrations to Stripe in the Dashboard. This turns on tax calculation
and collection in Stripe for your transactions in Vietnam.

Learn more about [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

We only support calculations for [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) (non-physical
items or services that are delivered, given, or rendered electronically) in
Vietnam. Stripe doesn’t calculate tax for products that don’t use a digital
product tax code.

View the list of supported [digital product tax
codes](https://docs.stripe.com/tax/tax-codes?type=digital). To calculate taxes
in Vietnam, make sure that you [assign a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
to each of your products.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports. Learn more about [the different types of
reports](https://docs.stripe.com/tax/reports).

You’re responsible for filing and remitting your taxes to Vietnam. Stripe
doesn’t file taxes on your behalf.

## Links

- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [government website](https://etaxvn.gdt.gov.vn/nccnn/Request)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=vn)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [digital products](https://docs.stripe.com/tax/tax-codes?type=digital)
- [assign a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)