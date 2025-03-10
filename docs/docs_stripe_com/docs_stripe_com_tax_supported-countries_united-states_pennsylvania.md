# Collect tax in Pennsylvania

## Learn how to use Stripe Tax to calculate, collect, and report tax in Pennsylvania.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Pennsylvania. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Remote sellers must register to collect and remit tax in Pennsylvania when, in
the previous calendar year, they meet or exceed a sales threshold of 100,000
USD.

The threshold includes gross sales. The threshold excludes marketplace sales if
the marketplace provider collects tax on behalf of sellers.

## Register to collect tax

Register for sales tax in Pennsylvania at the [tax
authority](https://www.revenue.pa.gov/TaxTypes/SUT/Pages/default.aspx). Read
more about registering for [sales tax in the US in our
guide](https://stripe.com/guides/sales-tax-registration-process-us).

After you’ve registered to collect tax in Pennsylvania, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=us-pa)
to add your registrations to Stripe in the Dashboard. This turns on tax
calculation and collection in Stripe for your transactions in Pennsylvania.

Customers in the city of Philadelphia or Allegheny county owe use tax on
purchases from remote sellers outside those locations. If you are a remote
seller you can voluntarily collect and remit these local taxes on their behalf.
You’ll be able to indicate whether you want to collect these local taxes as part
of adding your registration to Stripe.

Learn [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

If your [origin address](https://docs.stripe.com/tax/set-up#origin-address) is
in the US and differs from your customer’s state, Stripe always calculates tax
based on your customer’s location.

If your customer is in Pennsylvania and your origin address is also in
Pennsylvania, Stripe applies tax based on your origin address, depending on the
type of product or service you sell.

Sellers based in Philadelphia city or Allegheny county will have the local tax
calculated automatically. If you are a remote seller and selected the local
taxes for Philadelphia city and Allegheny county in Stripe then we will
calculate and collect that additional tax. You can change this by [editing the
tax registration](https://docs.stripe.com/tax/registering#edit-a-registration)
on the **Dashboard**.

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
align with Pennsylvania filing requirements. You have the option to report on an
annual, semiannual, quarterly, or monthly basis.

Reporting-specific considerations:

- You’ll only see amounts under Allegheny county and Philadelphia city sections
if you chose to voluntarily collect local taxes or have an origin address in
these jurisdictions.

### Filing

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

## Links

- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [tax authority](https://www.revenue.pa.gov/TaxTypes/SUT/Pages/default.aspx)
- [sales tax in the US in our
guide](https://stripe.com/guides/sales-tax-registration-process-us)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=us-pa)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [origin address](https://docs.stripe.com/tax/set-up#origin-address)
- [editing the tax
registration](https://docs.stripe.com/tax/registering#edit-a-registration)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [tax reporting exports](https://docs.stripe.com/tax/reports#exports)
- [Location reports](https://docs.stripe.com/tax/reports#us-location-reports)
- [tax filing](https://docs.stripe.com/tax/filing)