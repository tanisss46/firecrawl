# Collect tax in Hawaii

## Learn how to use Stripe Tax to calculate, collect, and report tax in Hawaii.

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Hawaii. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

Remote sellers must register to collect and remit tax in Hawaii when, in the
previous or current calendar year, they meet or exceed one of the following:

- A sales threshold of 100,000 USD
- A volume threshold of 200 transactions

The threshold includes gross sales, including marketplace sales.

## Register to collect tax

Register for sales tax in Hawaii at the [tax
authority](https://tax.hawaii.gov/). Read more about registering for [sales tax
in the US in our
guide](https://stripe.com/guides/sales-tax-registration-process-us). You can
also use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf.

After you’ve registered to collect tax in Hawaii, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=us-hi)
to add your registrations to Stripe in the Dashboard. This turns on tax
calculation and collection in Stripe for your transactions in Hawaii.

Learn [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
in the Dashboard.

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

Instead of a traditional sales tax paid by consumers, Hawaii has a tax on
businesses called General Excise Tax (GET). Businesses can recover GET by
passing it on to their customers. Businesses generally display GET as a separate
item on receipts, but they’re not required to do so.

Because a business must pay GET on the entire amount paid by a customer, it also
owes GET on any GET reimbursement it collects from customers. To cover that
additional tax amount, Hawaii allows businesses to pass GET on to customers at a
higher rate than the base GET rate. Stripe Tax only supports the maximum pass-on
rate, which fully covers a business’ GET liability.

For example:

A product sells for 100 USD and is subject to 4% GET, so the seller owes 4 USD
GET. If the seller passes that on to the customer and collects 104 USD, the
entire amount is subject to 4% GET. As a result, the seller’s GET liability
becomes 4.16 USD.

The seller can recover the entire GET amount from the customer by instead using
the maximum pass-on rate, which for a 4% GET rate is 4.166%. That lets the
seller charge the customer 4.166%, or 4.16 USD, which covers their entire GET
liability. GET rates can vary by county and by business type. To learn more
about GET and the maximum pass-on rates, see [Hawaii’s tax facts
page](https://files.hawaii.gov/tax/legal/taxfacts/tf2015-37-1.pdf).

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
align with Hawaii filing requirements. You have the option to report on an
annual, semiannual, quarterly, or monthly basis.

Reporting-specific considerations:

- In Hawaii, wholesalers are required to identify wholesale sales because
they’re subject to a lower tax rate instead of being completely exempt. You
won’t see a location report for Hawaii if you have any customer-exempt
transactions. Use the [exports](https://docs.stripe.com/tax/reports#exports)
instead for a detailed tax breakdown of each transaction.

### Filing

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax
(HOST)—to help automate your tax filing. These partners automatically sync your
tax transaction data in real time, eliminating the need for manual data entry or
file transfers. Learn more about [tax
filing](https://docs.stripe.com/tax/filing).

## Links

- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [tax authority](https://tax.hawaii.gov/)
- [sales tax in the US in our
guide](https://stripe.com/guides/sales-tax-registration-process-us)
- [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=us-hi)
- [how to add your
registration](https://docs.stripe.com/tax/registering#track-your-registrations-in-the-tax-dashboard)
- [Hawaii’s tax facts
page](https://files.hawaii.gov/tax/legal/taxfacts/tf2015-37-1.pdf)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [tax reporting exports](https://docs.stripe.com/tax/reports#exports)
- [Location reports](https://docs.stripe.com/tax/reports#us-location-reports)
- [tax filing](https://docs.stripe.com/tax/filing)