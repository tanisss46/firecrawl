# Monitor your obligations

## Use our tool to see where you might need to register to collect tax based on past transactions.

Stripe Tax provides insights about your potential tax registration obligations
(called economic nexus in the US). We help you understand where you might have
to register, collect, and remit tax based on your sales into a state or country,
even if you don’t have physical presence there. You can also use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf.

#### Note

Tax provides threshold monitoring primarily for payments processed by Stripe.
The only out of band payments we currently include are invoices processed off of
Stripe and transactions created using the Stripe Tax APIs.

## How it works

Tax uses your preset tax code and [location
attribution](https://docs.stripe.com/tax/monitoring#location-attribution) for
each Stripe-processed sale minus refunds to see how your total sales within a
given [time window](https://docs.stripe.com/tax/monitoring#time-window) compare
to tax thresholds in different jurisdictions. Tax uses time windows defined by
local tax rules and assumes all sales are B2C unless you have included a VAT ID
for your customer. Your obligations might differ if you only sell nontaxable
items or make B2B sales. Learn more about [when you need to register to collect
tax in each location](https://docs.stripe.com/tax/supported-countries).

### Refunds and threshold calculations

When a transaction is refunded, Stripe Tax automatically adjusts your threshold
calculations to account for the refund. The refunded amount is subtracted from
your total sales calculations, which might lower your overall sales volume for a
particular jurisdiction. If the refund brings you below a previously exceeded
threshold, this updates your obligation status. These adjustments typically
process within 24–48 hours of the refund.

After a refund processes, your threshold status includes the refunded amount.
Your Dashboard still shows any threshold notifications you received before
processing the refund.

### Connect

By default, transactions linked to your platform’s connected accounts don’t
count toward your platform’s tax registration thresholds. They only count toward
the connected accounts’ tax thresholds. To change this:

- Go to the [Connect
settings](https://dashboard.stripe.com/settings/connect/tax-threshold-monitoring)
for Sales tax collection.
- Choose to be held liable for sales made by your connected accounts.

Connected accounts’ transactions with the following charge types are then
included in your platform’s threshold monitoring:

Charge typeWithout `on_behalf_of`With `on_behalf_of`[Destination
Charges](https://docs.stripe.com/connect/destination-charges)Included.Included.[Separate
Charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)Not
included.Included.
Separate charges and transfers without `on_behalf_of` aren’t included. This is
because Stripe can’t know who the liable party for the transfer is. Stripe
assumes the [settlement
party](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)
to be the liable entity, which is the Connect Platform.

### Exceptions

- We provide insight into the places where you don’t have a physical presence so
obligations aren’t monitored for your home US state or country.
- Obligations are only monitored in live mode.
- Application fees that Connect platforms charge don’t count toward the
platform’s tax registration thresholds.
- We monitor locations that Stripe Tax supports. [Learn
more](https://docs.stripe.com/tax/supported-countries) about those locations.
- We don’t monitor transactions that might contribute to exceeding a threshold
to collect retail delivery fees.
- We treat obligations for tangible product sales and services the same.
- We can’t differentiate between retail and wholesale sales.
- For Connect platforms liable for sales made by their connected accounts, a
location might be marked as Undetermined. This means that Stripe lacks the
information needed to support you on tax obligations for this location. This can
occur if the customer’s location is outside the United States and not in the
United Kingdom or European Union with a default PTC of Digital Goods.

### Location attribution

Location attribution is an important part of monitoring tax thresholds. To
correctly determine your tax obligations, Stripe Tax attributes a location to
each processed transaction once per day, adding new resulting transactions to
your monitoring threshold in a 24-hour cycle. Location attribution happens even
if tax isn’t calculated for the transactions, and it’s a different process from
the [address validation](https://docs.stripe.com/tax/customer-locations) that we
perform to calculate tax. You might not need specific tax rates and precise
address information for threshold monitoring purposes, unlike when Stripe
calculates and collects tax for transactions.

To attribute a location, Stripe Tax uses available information for that
transaction and prefers some information sources to others—some examples are the
current customer address, country of the card issuer, and the customer’s IP
address.

Stripe Tax uses information in the following order:

- **Stripe Tax validated address:** if we calculated tax for the transaction,
Stripe Tax already validated the address. We use the same address when
calculating the tax threshold.
- **Customer address:** property in the
[Customer](https://docs.stripe.com/api/customers/object) object responsible for
the transaction. Stripe Tax uses the country, state, and postal code fields to
determine a jurisdiction.
- **Address Verification (AVS) postal code:**
[AVS](https://docs.stripe.com/disputes/prevention/verification#avs-check) is a
service that verifies the authenticity of a transaction by checking if the
provided address matches the cardholder’s billing address. If the transaction is
successful, Stripe Tax converts a US or Canadian postal code into a state and
determines the jurisdiction.
- **Country of the card issuer:** Stripe Tax uses the credit card issuer’s bank
country to determine a jurisdiction for the transaction. For transactions in the
US and Canada, we might also need state information.
- **Payment method:** Stripe Tax uses country-specific payment methods to
determine the location of a payment. We assume that a transaction through
[iDeal](https://docs.stripe.com/payments/ideal) is from the Netherlands and that
a transaction through Giropay is from Germany, for example.
- **Customer’s IP address:** as a last resort, we use the customers IP address
to determine a jurisdiction.

When Stripe Tax can’t determine the location for a transaction, we group its
information into an **Unattributed revenue** category. Where possible, we break
out globally unattributed revenue and US unattributed revenue. For example, if
we’re able to determine the customer is in the US (perhaps by using an IP
address) but don’t have enough information to make a granular determination, we
categorize that as US unattributed revenue.

![Unattributed revenue in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/unattributed-revenue.dfbed304297c0e568b633542130bbd39.png)

#### Handling unattributed revenue

The table below explains what information is needed for different countries.

United StatesCanadaEverywhere elseExample addresses ExplanationAttributed -
`country`: US
- `state`: NY

**Country and state**

You need to provide country and state information to calculate tax thresholds in
the US.

- `country`: US
- `postal_code`: 10038

**Country and postal code**

We match the 5 or 9-digit postal code with its corresponding state.

- `country`: US

**Country**

In the US, each state defines it’s rules for when to establish economic nexus.
Therefore, country-only information isn’t enough to attribute locations to
transactions. Transactions without state information appear under US
unattributed revenue.

## Using the Dashboard

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations.

We group your registration obligations into the following categories:

- Exceeded: Your estimated sales or transactions exceed the location’s
registration threshold, and your business likely needs to register for tax. You
can [use Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register).
- Upcoming: Your estimated sales or transactions exceed 85% of the location’s
threshold. We expect you to exceed the threshold soon.
- Monitoring: We’re actively monitoring your obligations for the location and
will let you know when you’re approaching its threshold.
- Not monitoring: We aren’t monitoring your obligations in the location. This is
because either:- Your [preset product tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
is non-taxable in the location.
- We only support monitoring [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) there, and your
[preset product tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
is non-digital. For more details, see the [countries supported by Stripe
Tax](https://docs.stripe.com/tax/supported-countries).
- Undetermined: For [marketplace
facilitators](https://docs.stripe.com/tax/tax-for-marketplaces), we support
monitoring only in the UK, US, and EU. In the UK and EU, we support monitoring
only for [digital products](https://docs.stripe.com/tax/tax-codes?type=digital).

To learn more about an individual state or country comparison, click the
overflow menu (), then **View details**. This page contains information about
the threshold itself and your latest sales.

When downloading your transaction data, the `is_customer_business` and
`is_customer_taxable` fields are included for completeness, but might not be
relevant or applicable in all jurisdictions. Learn more about the tax
requirements in each of our [supported
jurisdictions](https://docs.stripe.com/tax/supported-countries).

If you have questions about your latest sales in a location, send an email to:
[stripe-tax@stripe.com](mailto:stripe-tax@stripe.com).

### Time windows

As noted above, each jurisdiction might have a different time window for
calculating nexus obligations. For example, some only look at the past calendar
month or quarter whereas others use a rolling basis. You can see how each
individual jurisdiction calculates economic nexus as part of the Review flow,
but in general, Stripe Tax supports the following calculation windows and
methodology:

- **Previous or current year:** Stripe Tax uses the previous or current calendar
year to calculate the count and amount of transactions.
- **Previous year:** Stripe Tax uses the previous calendar year to calculate the
count and amount of transactions.
- **Rolling year by quarter:** Stripe Tax uses the last four full quarters to
calculate the count and amount of transactions.
- **Rolling 12 months:** Stripe Tax uses the last 12 months to calculate the
count and amount of transactions.

### Stripe Tax API transactions

By default, Stripe Tax monitors all [Stripe Tax
API](https://docs.stripe.com/tax/custom) transactions. You can choose to exclude
your Stripe Tax API transactions by adjusting the **API transactions** setting
in your [Tax Settings](https://dashboard.stripe.com/settings/tax).

## Tax threshold notifications

Stripe Tax alerts you to potential tax obligations (known as economic nexus in
the US) when your business reaches 10,000 USD in yearly revenue. We send
notifications after you hit a threshold in any location. Stripe sends tax
threshold notifications by email, and displays them in the Dashboard to the
account owner.

### Email notification

We send email notifications from `support+updates@stripe.com` to the account
owner’s email. The email notification includes:

- A list of locations generating over 5% of your revenue where you’re not
registered.
- The count of locations generating less than 5% of your revenue where you’ve
recently exceeded a threshold and aren’t registered.

![Preview of tax threshold
notification](https://b.stripecdn.com/docs-statics-srv/assets/tax-threshold-email-preview.e685687dcb47a209a7aef60cc2402d36.png)

If you’re registered in one of these locations, add your registration in the
[Dashboard](https://dashboard.stripe.com/tax/registrations).

### Dashboard notification

If you log into the Dashboard as the account owner, you can see notifications.
Click the bell icon in the navigation bar to show all of your Dashboard
notifications.

#### Note

Click **Review tax thresholds** inside of the notification to go to the tax
monitoring tool.

Crossing a tax threshold in a single locationCrossing tax thresholds in multiple
locations
You can exceed a tax threshold in a single location.

!

### Tax threshold notification preconditions

Stripe only notifies you when you have exceeded a tax threshold based on
Stripe’s calculations. To receive tax threshold notifications, you must meet the
following requirements:

- You’ve opted into [Stripe Tax](https://dashboard.stripe.com/tax).
- You haven’t disabled [Stripe Tax
notifications](https://dashboard.stripe.com/settings/communication-preferences).
- You’ve had 10,000 USD in revenue in the previous year.
- You don’t have an active live mode tax registration for the location.
- You haven’t received any tax threshold notification within the past 7 days.

### Tax threshold notification frequency

After you cross a threshold, Stripe sends you a notification within 1 or 2 days.
If Stripe sent you a notification in the past 7 days, you receive batched
notifications for new threshold status changes a week after the last
notification.

No grouping of notificationsGrouping of notifications- **March 15**: You exceed
a threshold in Germany.
- **March 16**: Stripe notifies you about exceeding a tax threshold in Germany.
- **March 25**: You exceed a threshold in the Netherlands.
- **March 26**: Stripe notifies you about exceeding a tax threshold in the
Netherlands.

### Disable tax threshold notifications

If you’re the account owner, you can disable tax threshold notifications by
going to the **Product updates** tab in your [communication
preferences](https://dashboard.stripe.com/settings/communication-preferences).

## See also

- [Checkout and Tax](https://docs.stripe.com/tax/checkout)
- [Billing and Tax](https://docs.stripe.com/billing/taxes/collect-taxes)
- [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)

## Links

- [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [location
attribution](https://docs.stripe.com/tax/monitoring#location-attribution)
- [time window](https://docs.stripe.com/tax/monitoring#time-window)
- [when you need to register to collect tax in each
location](https://docs.stripe.com/tax/supported-countries)
- [Connect
settings](https://dashboard.stripe.com/settings/connect/tax-threshold-monitoring)
- [Destination Charges](https://docs.stripe.com/connect/destination-charges)
- [Separate Charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [settlement
party](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)
- [address validation](https://docs.stripe.com/tax/customer-locations)
- [Customer](https://docs.stripe.com/api/customers/object)
- [AVS](https://docs.stripe.com/disputes/prevention/verification#avs-check)
- [iDeal](https://docs.stripe.com/payments/ideal)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [preset product tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
- [digital products](https://docs.stripe.com/tax/tax-codes?type=digital)
- [marketplace facilitators](https://docs.stripe.com/tax/tax-for-marketplaces)
- [Stripe Tax API](https://docs.stripe.com/tax/custom)
- [Tax Settings](https://dashboard.stripe.com/settings/tax)
- [Dashboard](https://dashboard.stripe.com/tax/registrations)
- [Stripe Tax](https://dashboard.stripe.com/tax)
- [Stripe Tax
notifications](https://dashboard.stripe.com/settings/communication-preferences)
- [Checkout and Tax](https://docs.stripe.com/tax/checkout)
- [Billing and Tax](https://docs.stripe.com/billing/taxes/collect-taxes)
- [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)