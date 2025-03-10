# Collect tax in Illinois

## Learn how to use Stripe Tax to calculate, collect, and report tax in Illinois.

In Illinois, Stripe Tax supports calculation and collection of sales tax.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Illinois. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

### Sales tax

Remote sellers must register to collect and remit tax in Illinois when, in the
last four quarters, they meet or exceed one of the following:

- A sales threshold of 100,000 USD
- A volume threshold of 200 transactions

The thresholds include sales of tangible personal property, whether taxable or
nontaxable. The thresholds exclude sales of services, wholesale sales (sales of
resale), and marketplace sales.

### Other taxes

We also support:

- [Bloomington Amusement
tax](https://www.bloomingtonil.gov/departments/finance/local-tax-information/amusement-tax)—for
businesses selling video or audio streaming on a pay-per-use, rental, or
subscription basis to customers in Bloomington.
- [Chicago Lease Tax (Personal Property Lease Transaction
Tax)](https://www.chicago.gov/city/en/depts/fin/supp_info/revenue/tax_list/personal_propertyleasetransactiontax.html)—for
businesses selling $100,000 or over of software as a service or other leased
products into Chicago.
- [Chicago Amusement
tax](https://www.chicago.gov/city/en/depts/fin/supp_info/revenue/tax_list/amusement_tax.html)—for
businesses selling $100,000 or more of digital entertainment into Chicago,
including selling video or audio streaming and online gaming.
- [East Dundee Amusement
tax](https://eastdundee.net/businesses/streaming_services_amusement_tax.php)—for
businesses selling video or audio streaming, or remotely-accessed online games
on a pay-per-use, rental, or subscription basis to customers in East Dundee.
- [Evanston Amusement
tax](https://www.cityofevanston.org/how-to/home-rule-taxes)—for businesses
selling video or audio streaming, or remotely-accessed online games on a
pay-per-use, rental, or subscription basis to customers in Evanston.
- [Schiller Park Streaming
Surcharge](https://www.villageofschillerpark.com/149/Administration-Department)—for
businesses selling video or audio streaming, or remotely-accessed online games
on a pay-per-use, rental, or subscription basis that are delivered to customers
in Schiller Park.

**Thresholds**

- Chicago Lease and Chicago Amusement tax apply to businesses selling specific
goods to customers in Chicago, even if you don’t have a physical presence there.
- Bloomington, East Dundee, Evanston, and Schiller Park amusement taxes only
apply when there’s a physical presence in those locations.

Transactions for these taxes aren’t included in tax threshold monitoring for
Illinois.

## Register to collect tax

Register for sales tax in Illinois at the [tax
authority](https://tax.illinois.gov/research/taxinformation/sales/rot.html) or
the other taxes we support at the links above. Read more about registering for
[sales tax in the US in our
guide](https://stripe.com/guides/sales-tax-registration-process-us). You can
also use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf.

After you’ve registered to collect tax in Illinois, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=us-il)
to add your registrations to Stripe in the Dashboard. This turns on tax
calculation and collection in Stripe for your transactions in Illinois.

Learn [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

If your [origin address](https://docs.stripe.com/tax/set-up#origin-address) is
in the US and differs from your customer’s state, Stripe always calculates tax
based on your customer’s location.

If your customer is in Illinois and your origin address is also in Illinois,
Stripe applies tax based on your origin address, depending on the type of
product or service you sell.

Stripe still applies tax based on your origin address, if the following are all
true:

- Your customer is in Illinois
- Your origin address is in Illinois
- Your goods [ship
from](https://docs.stripe.com/tax/calculating#how-to-use-ship-from-addresses) a
location outside Illinois

Even if the origin address in Illinois doesn’t perform selling activities, as
defined by Illinois tax law, Stripe can’t determine the activities performed at
each address. This means Stripe defaults to the Illinois address as
participating in the sale.

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
align with Illinois filing requirements. You have the option to report on an
annual, quarterly, or monthly basis.

Reporting-specific considerations:

- The location reports don’t include transactions with Bloomington Amusement
tax, Chicago Lease Tax, Chicago Amusement tax, East Dundee Amusement tax,
Evanston Amusement tax, or Schiller Park Streaming Surcharge as these are filed
to the local jurisdiction using a different report. To see transactions with
these taxes, you can use the
[exports](https://docs.stripe.com/tax/reports#exports).

### Filing

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

## Links

- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Bloomington Amusement
tax](https://www.bloomingtonil.gov/departments/finance/local-tax-information/amusement-tax)
- [Chicago Lease Tax (Personal Property Lease Transaction
Tax)](https://www.chicago.gov/city/en/depts/fin/supp_info/revenue/tax_list/personal_propertyleasetransactiontax.html)
- [Chicago Amusement
tax](https://www.chicago.gov/city/en/depts/fin/supp_info/revenue/tax_list/amusement_tax.html)
- [East Dundee Amusement
tax](https://eastdundee.net/businesses/streaming_services_amusement_tax.php)
- [Evanston Amusement
tax](https://www.cityofevanston.org/how-to/home-rule-taxes)
- [Schiller Park Streaming
Surcharge](https://www.villageofschillerpark.com/149/Administration-Department)
- [tax
authority](https://tax.illinois.gov/research/taxinformation/sales/rot.html)
- [sales tax in the US in our
guide](https://stripe.com/guides/sales-tax-registration-process-us)
- [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=us-il)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [origin address](https://docs.stripe.com/tax/set-up#origin-address)
- [ship
from](https://docs.stripe.com/tax/calculating#how-to-use-ship-from-addresses)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [tax reporting exports](https://docs.stripe.com/tax/reports#exports)
- [Location reports](https://docs.stripe.com/tax/reports#us-location-reports)
- [tax filing](https://docs.stripe.com/tax/filing)