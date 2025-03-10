# Collect tax in Puerto Rico

## Learn how to use Stripe Tax to calculate, collect, and report tax in Puerto Rico.

Stripe supports calculation and collection of sales tax in the US territory of
Puerto Rico.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Puerto Rico. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Remote sellers must register to collect and remit tax in Puerto Rico when, in
the previous or current calendar year, they do one of the following:

- Exceed a sales threshold of 100,000 USD
- Meet or exceed a volume threshold of 200 transactions

The threshold includes sales of tangible personal property and taxable services.
It includes wholesales (sales of resale). The threshold excludes sales of
nontaxable services and marketplace sales.

## Register to collect tax

Register for sales tax in Puerto Rico at the [tax
authority](https://suri.hacienda.pr.gov/_/).

After you’ve registered to collect tax in Puerto Rico, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=us-pr)
to add your registrations to Stripe in the Dashboard. This turns on tax
calculation and collection in Stripe for your transactions in Puerto Rico.

Learn [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

### If you enabled Tax after May 12, 2023

You can add your registration in Puerto Rico and start collecting tax. Your
customers in Puerto Rico will be asked for a country + postal code for the
transaction to go ahead.

### If you started using Tax on or before May 12, 2023

You won’t be able to turn on tax collection for Puerto Rico yet. If you don’t
use Payment Links or Checkout, some customer addresses in these locations might
not contain all the detail needed for tax calculation. Invoicing, Subscriptions,
and custom payment integrations won’t require the postal code automatically.

We’ve released a tool that enables you to export your customer addresses and see
which addresses won’t have the required address information for tax calculation
in Puerto Rico. Use the form below to request access. If you have existing
subscriptions, update any customer addresses to include a postal code. If you
don’t update this information, the [invoice won’t
finalize](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
and the payment won’t be collected.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports.

### Exports

The tax transaction data export provides a comprehensive and aggregated view of
transactions by location, including a breakdown of individual tax amounts. Learn
more about [tax reporting exports](https://docs.stripe.com/tax/reports#exports).

### Location reports

[Location reports](https://docs.stripe.com/tax/reports#us-location-reports)
offer a summary of transaction and refund data for specific US locations and
align with Puerto Rico filing requirements. You have the option to report on an
annual, quarterly, or monthly basis.

### Filing

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

## Need access to collect tax in Puerto Rico?

Please provide your email address below and we'll get in touch with more
information

Collect EmailRequest accessRead our [privacy
policy](https://stripe.com/privacy).

## Links

- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [tax authority](https://suri.hacienda.pr.gov/_/)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=us-pr)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [invoice won’t
finalize](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [tax reporting exports](https://docs.stripe.com/tax/reports#exports)
- [Location reports](https://docs.stripe.com/tax/reports#us-location-reports)
- [tax filing](https://docs.stripe.com/tax/filing)
- [privacy policy](https://stripe.com/privacy)