# Collect tax in Serbia

## Learn how to use Stripe Tax to calculate, collect, and report tax in Serbia.

In Serbia, Stripe only supports collecting
[VAT](https://www.purs.gov.rs/sr/pravna-lica/pdv/opste-o-pdv.html) for
electronically supplied services. In Stripe, these are referred to as “digital
products.” To collect this tax on Stripe, you must be a remote seller without a
physical presence in the country.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Serbia. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Remote sellers providing electronically supplied services (digital products) to
individuals in Serbia have to register for tax from their first sale there.
Sales to business customers in Serbia don’t trigger any tax registration
obligations because non-resident businesses aren’t required to collect tax on
these sales.

- **Threshold**: 1 transaction
- **Included transactions**: Business-to-consumer (B2C) sales of digital goods
or electronically supplied services (digital products)

## Register to collect tax

You must be a remote seller with no physical presence in Serbia to collect this
tax on Stripe.

Find more information on how to register for VAT in Serbia on the [government
website](https://www.purs.gov.rs/sr/pravna-lica/pdv/opste-o-pdv.html) (Serbian
content).

After you’ve registered to collect tax in Serbia, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=rs) to
add your registrations to Stripe in the Dashboard. This turns on tax calculation
and collection in Stripe for your transactions in Serbia.

Learn more about [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

We only support calculations for [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) (non-physical
items or services that are delivered, given, or rendered electronically) in
Serbia. Stripe doesn’t calculate tax for products that don’t use a digital
product tax code.

View the list of supported [digital product tax
codes](https://docs.stripe.com/tax/tax-codes?type=digital). To calculate taxes
in Serbia, make sure that you [assign a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
to each of your products.

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

- [VAT](https://www.purs.gov.rs/sr/pravna-lica/pdv/opste-o-pdv.html)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=rs)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [digital products](https://docs.stripe.com/tax/tax-codes?type=digital)
- [assign a tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
- [tax filing](https://docs.stripe.com/tax/filing)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)