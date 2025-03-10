# Collect tax in the United States

## Learn how to use Stripe Tax to calculate, collect, and report tax in the US.

Businesses selling goods and services to customers in the United States (US)
might need to collect sales tax. That’s the case even if your business isn’t
established (based) in the US. Tax rates and rules vary by region. You can also
use [Stripe to regsiter](https://docs.stripe.com/tax/use-stripe-to-register) on
your behalf.

[OptionalRegions in the
US](https://docs.stripe.com/tax/supported-countries/united-states#us-states)
## When to register for tax collection

Different rules determine when and how you need to register to collect tax
depending on the region. US regions can choose which level and type of activity
in the region means a business needs to collect tax there. This is called
*nexus*. A business can have nexus in a region if they have:

- Physical activity, such as having remote employees based there or storing
inventory in a warehouse.
- Economic activity, such as an amount or total value of transactions within a
time period.

If you have nexus in a US region, you need to register for a license to collect
tax on sales to customers in that region.

To understand the economic nexus thresholds in each region use the [links
above](https://docs.stripe.com/tax/supported-countries/united-states#us-states).
Stripe only monitors if you have reached an economic nexus tax threshold for
sales outside of the region your business is based in. Learn more about
[economic
nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus).

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations. Stripe also notifies you with
email and Dashboard alerts when you need to register to collect tax. Learn more
about how the [monitoring tool works](https://docs.stripe.com/tax/monitoring).

## Register to collect tax

Each US state, US territory, and the US capital has its own tax authority. You
need to individually register to collect sales tax in each region where you have
met the registration requirements. Start by going to the regional tax authority
website. If you need help finding the right links to register for tax, select a
region from the [list
above](https://docs.stripe.com/tax/supported-countries/united-states#us-states).
You can also use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf.

Learn more about [the sales tax registration process in the United
States](https://stripe.com/guides/sales-tax-registration-process-us).

### Streamlined Sales and Use Tax Agreement (SSUTA)

The Streamlined Sales and Use Tax Agreement (SSUTA) was created by a coalition
of states to help businesses manage their sales and use tax obligations across
the United States. Twenty-four US states are members of the SSUTA agreement.
However, individual states can still decide which products and services are
taxable in their state. You can learn more and register for sales and use tax
permits in all SSUTA member states on the [streamlined sales tax registration
website](https://www.streamlinedsalestax.org/).

After you’ve registered with a state, go to
[Registrations](https://dashboard.stripe.com/tax/registrations?location=us) to
add your registrations to Stripe in the Dashboard and start collecting tax on
your transactions in that location.

## How we calculate taxes

What you sell and where you sell impacts how tax is calculated on your sales.
Different rules apply when your customer is located in the same region as your
business or located somewhere else.

Stripe calculates tax on a transaction taking into account the following
factors:

- the location of your business
- the tax registrations you’ve added to Stripe
- the location of the buyer
- the type of the product sold (based on which [product tax
code](https://docs.stripe.com/tax/tax-codes) you assigned to your product)
- the status of the customer (whether they’re an individual or a business)

As part of the tax calculation process, Stripe collects addresses for both your
business and customers. We verify these addresses, convert them into
geographical coordinates, and match them to the relevant tax jurisdiction
boundaries. We then use these jurisdictions as input for the tax calculation
process.

### Sales to a customer located outside the state your business is based in

If your [origin address](https://docs.stripe.com/tax/set-up#origin-address) is
in the US and is different from the state or territory your customer is located
in, Stripe always calculates tax based on your customer’s location. This also
applies if either your origin address or your customer’s location is in the
District of Columbia while the other is not.

### Sales to a customer located within the same state as your business

If your [origin address](https://docs.stripe.com/tax/set-up#origin-address) is
in the US and in the same state or territory as your customer’s state or
territory, Stripe generally calculates sales tax based on your customer’s
location. The customer’s location is also used when your origin address and your
customer’s location are both in the District of Columbia.

However some states use your origin address instead of the customers location
depending on the type of product or service you sell:

- In Arizona, Illinois, Missouri,Pennsylvania, Tennessee, and Virginia, Stripe
applies tax based on your business location.
- In California, state, county, and city taxes are based on the origin address,
while district taxes are based on the customer’s location.
- In Mississippi, Ohio, Texas, and Utah, Stripe applies tax based on the origin
address for physical and digital goods. Sales of services are taxed at the
destination address.

### Sales to US customers from abroad

If your origin address is outside the US and you sell goods or services to US
customers, Stripe generally calculates sales tax based on your customer’s
location. However, if you don’t have a tax registration in your customer’s US
state, Stripe treats a cross-border sale of goods as a
[zero-rated](https://docs.stripe.com/tax/zero-tax#exempt-or-zero-rated-products)
export in the country of your origin address.

[OptionalSales tax
holidays](https://docs.stripe.com/tax/supported-countries/united-states#us-sales-tax-holidays)
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

A marketplace facilitator is an entity that contracts with third parties to
promote their sales of property, digital goods and services by performing
various functions to initiate and complete transactions. In the US, marketplace
facilitator laws now exist in every state and territory with a sales tax, as
well as the District of Columbia. These laws generally require the marketplace
facilitator to collect and remit sales tax on behalf of the third-party sellers
conducting business on the marketplace. As a marketplace facilitator, your
compliance obligations, from registration requirements to reporting and filing,
are determined by the specific laws of each region.

## Links

- [Stripe to regsiter](https://docs.stripe.com/tax/use-stripe-to-register)
- [links
above](https://docs.stripe.com/tax/supported-countries/united-states#us-states)
- [economic
nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [the sales tax registration process in the United
States](https://stripe.com/guides/sales-tax-registration-process-us)
- [streamlined sales tax registration
website](https://www.streamlinedsalestax.org/)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=us)
- [product tax code](https://docs.stripe.com/tax/tax-codes)
- [origin address](https://docs.stripe.com/tax/set-up#origin-address)
-
[zero-rated](https://docs.stripe.com/tax/zero-tax#exempt-or-zero-rated-products)
- [tax filing](https://docs.stripe.com/tax/filing)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)