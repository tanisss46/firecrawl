# Migrate to Stripe Tax

## Learn how to migrate existing subscriptions to Stripe Tax.

[Stripe Tax](https://docs.stripe.com/tax) allows you to calculate the tax to
collect on your transactions. It computes the taxes and adds them to the payment
automatically, based on the product and the customer location.

When you integrate with Stripe Tax, you need to update existing subscriptions to
make sure that tax is automatically calculated going forward. Stripe provides
tooling to help you update your subscriptions. You can also manually update
subscriptions where you want more control over certain options.

[Update existing subscriptions using automated
tooling](https://docs.stripe.com/billing/taxes/migration#update-automated)
First, you need to activate Stripe Tax. To learn how, read the [setup
guide](https://docs.stripe.com/tax/set-up).

To use the tooling, follow these steps:

- Go to the [Dashboard](https://dashboard.stripe.com/tax/migrations).
- Review the subscriptions you need to update.
- Review the recommended actions.
- Make any necessary manual updates.

Stripe removes manual [tax
rates](https://docs.stripe.com/billing/taxes/tax-rates) from the subscriptions,
which can take up to 5 business days. When the process is complete, we notify
you by email.

#### Note

We don’t prorate the tax changes. The updates take effect at the start of the
next billing cycle.

You can use the tooling to update subscriptions that meet the following
criteria:

- Are active
- Don’t automatically collect tax
- Have sufficient [address
information](https://docs.stripe.com/tax/customer-locations#address-hierarchy-other)
to calculate tax

You need to update the following types of subscriptions:

- Subscriptions with schedules. To learn more, see [the Update Subscriptions
with subscription schedules
section](https://docs.stripe.com/billing/taxes/migration#existing-subscription-schedules).
- Subscriptions that use the [charge
types](https://docs.stripe.com/connect/charges#types) destination charges or
separate charges and transfers.
[Update existing subscriptions
manually](https://docs.stripe.com/billing/taxes/migration#update-manually)-
[Review customer
locations](https://docs.stripe.com/billing/taxes/migration#customer-locations)
and make any required updates.
- [Update products and
prices](https://docs.stripe.com/billing/taxes/migration#products_prices) with
tax codes and tax behaviors.
- [Update subscriptions](https://docs.stripe.com/billing/taxes/migration#subs)
to automatically calculate taxes on future invoices.
- [Confirm](https://docs.stripe.com/billing/taxes/migration#confirm) that you’ve
updated the subscriptions correctly.
[Check customer
locations](https://docs.stripe.com/billing/taxes/migration#customer-locations)
To correctly calculate tax, we need to know the customer’s tax location status.
You can check it in the Dashboard or in exported data, or get the information
using the API.

DashboardAPIDashboard Exports
To check a customer’s tax location status through the Dashboard, go to the
[Customers page](https://dashboard.stripe.com/customers), select the customer,
and expand their details. The tax location status (`automatic_tax`) has four
possible values:

StatusDescriptionPossible ActionValid (`supported`)Automatic tax fully
supported.No further action required.Unrecognized location
(`unrecognized_location`)The address isn’t valid for determining a tax
location.Ask the customer for an updated address and set
[customer.address](https://docs.stripe.com/api/customers/update#update_customer-address)
to the new value. You can update the value through the API or Dashboard by
editing the customer’s details.Not registered (`not_collecting`)The address is
recognized and resolved to a location that you haven’t set up a collection
location for.The action to take depends on your [tax
obligations](https://docs.stripe.com/tax/monitoring). If you proceed, Stripe Tax
doesn’t assess any taxes. If you want it to assess tax, [add an active
registration](https://docs.stripe.com/tax/registering) for the jurisdiction the
customer is based in.`failed`An [error](https://docs.stripe.com/error-codes)
occurred with Stripe’s servers. This is rare.Try the request again or contact
Stripe support for additional assistance.
In case the `status=unrecognized_location` you need to update the customer
location with [an address that Stripe Tax can
use](https://docs.stripe.com/tax/customer-locations). In the Dashboard, you can
go into the [Customers page](https://dashboard.stripe.com/customers), select the
customer, and change its billing or shipping address under Details.

For more information on which customer address is valid, how they’re used, or
how to handle errors, see [Collect customer
addresses](https://docs.stripe.com/tax/customer-locations).

[Update products and
prices](https://docs.stripe.com/billing/taxes/migration#products-prices)
Your products and prices use the default tax behavior you assigned when
activating Stripe Tax. If you’d prefer to update active products and prices to
calculate tax independently, set a tax_code and tax_behavior. See the full list
of [available tax codes](https://docs.stripe.com/tax/tax-codes) and the [guide
for setting
up](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior) tax
codes and tax behavior for more information. For more information about
[products and
prices](https://docs.stripe.com/billing/taxes/collect-taxes#product-and-price-setup),
including how to decide whether a price should be inclusive or exclusive, see
the [Tax Setup FAQ](https://docs.stripe.com/tax/faq#set-up).

### Update products

First, update any existing products with a `tax_code`. If you don’t explicitly
define a `tax_code` on your product, Stripe Tax uses the preset product tax code
from your settings.

DashboardAPI
To update a Product with a `tax_code` in the Dashboard, go to the [Products
page](https://dashboard.stripe.com/products?active=true), select a product to
edit and, in the product information page, choose the tax code from the
drop-down menu.

### Update prices

Next, update the tax behavior for your prices.

#### Common mistake

You can’t change `tax_behavior` after it’s been set to one of `exclusive` or
`inclusive`. If you want to change the tax behavior of a price, you need to
create a new price with the desired behavior, and archive the old price.

DashboardAPI
To update a price using the Dashboard:

- Go to the [products page](https://dashboard.stripe.com/products).
- Select the product with the price you want to update.
- Select additional options in the price information section.
- In the **Include tax in price** drop-down menu, select the behavior you want
to associate with the price.
[Update subscriptions](https://docs.stripe.com/billing/taxes/migration#subs)
With your customers, products, and prices updated, you’re ready to update
existing subscriptions.

Get the list of subscriptions that need to be updated from the [subscriptions
page in the Dashboard](https://dashboard.stripe.com/subscriptions). To display
only subscriptions that don’t have automatic tax enabled, click **Filter**,
check **Automatic tax**, and select **Disabled**. Alternatively, you can export
all filtered subscriptions to view them as a CSV file. To do this, click
**Export** and select **All** as the **Date range**.

How you update the subscriptions depends on their state:

- If your subscriptions [don’t have existing tax
rates](https://docs.stripe.com/billing/taxes/migration#no-tax-rates), you only
need to enable automatic tax.
- If your subscriptions have [existing tax
rates](https://docs.stripe.com/billing/taxes/migration#existing-tax-rates) (at
either the subscription or line-item level), you need to clear out any existing
tax rates and enable automatic tax. To avoid creating prorated items, you can
schedule this update.
- If your subscriptions have [subscriptions
schedules](https://docs.stripe.com/billing/taxes/migration#existing-subscription-schedules),
you need to remove instances of `automatic_tax[enabled]=false` in the
subscription schedule plans.

### Update subscriptions with no existing tax rates

DashboardAPI
To update subscriptions with no existing tax rates using the Dashboard, update
the subscription and turn on the **Calculate tax automatically** option.

### Update subscriptions with existing tax rates

DashboardAPI
To update subscriptions with [tax
rates](https://docs.stripe.com/billing/taxes/tax-rates) through the Dashboard,
edit the subscription, then enable the **calculate tax automatically** option.
The Dashboard removes any existing tax rates and automatically calculates tax
going forward. If you haven’t updated your prices to set `tax_behavior`, the
Dashboard prompts you to update any missing details before you can update the
subscription.

### Update Subscriptions with subscription schedules

If you need to collect tax, and any of your subscriptions include a subscription
schedule that sets `automatic_tax[enabled]=false`, you must remove that
parameter. To do so, update all phases of the subscription’s schedule by
removing `automatic_tax[enabled]=false` and setting
`default_settings[automatic_tax][enabled]=true`.

When you update a subscription schedule, you need to pass in all current and
future phases. To do this, verify the set parameters, then enable Stripe Tax in
the subscription schedule.

```
curl
https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

To update the subscription schedule after you obtain it, remove the
`automatic_tax[enabled]=false` parameter, and pass down the other phases and
parameters:

```
curl
https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "phases[0][items][0][price]"=price_1GqNdGAJVYItwOKqEHb \
 -d "phases[0][items][0][quantity]"=1 \
 -d "phases[0][start_date]"=1577865600 \
 -d "phases[0][end_date]"=1578038400 \
 -d "phases[1][items][0][price]"=price_1GqNdGAJVYItwOKqEHb \
 -d "phases[1][items][0][quantity]"=2 \
 -d "phases[1][start_date]"=1578038400 \
 -d "phases[1][end_date]"=1580544000 \
 -d "default_settings[automatic_tax][enabled]"=true
```

#### Schedule the update

If you want to avoid creating a prorated item, you can schedule the update to
occur at the start of the next cycle.

You can currently only schedule subscription updates with the API:

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

subscription = Stripe::Subscription.retrieve(
 '{{SUBSCRIPTION_ID}}',
)
schedule = Stripe::SubscriptionSchedule.create({
 from_subscription: subscription.id
})
Stripe::SubscriptionSchedule.update(
 schedule.id,
 {
 end_behavior: 'release',
 phases: [
 # The first phase contains items for the
 # latest subscription invoice
 {
 items: [
 # Prices and tax_rates for each item
 {
 price: '{{PRICE_ID}}',
 tax_rates: [
 '{{TAX_RATE_ID}}'
 ]
 }
 ],
 default_tax_rates: ['{{TAX_RATE_ID}}'],
 start_date: subscription.current_period_start,
 end_date: subscription.current_period_end
 },
 # The second phase removes manual tax rates and enables
 # automatic tax calculation
 {
 items: [
 # Prices for each item with tax_rates: ''
 {
 price: '{{PRICE_ID}}',
 tax_rates: ''
 }
 ],
 default_tax_rates: '',
 automatic_tax: {enabled: true},
 iterations: 1
 }
 ]
 }
)
```

[Confirm updates](https://docs.stripe.com/billing/taxes/migration#confirm)
To confirm that you’ve properly updated your subscriptions, retrieve the
[upcoming invoice](https://docs.stripe.com/api/invoices/upcoming) of each
subscription and inspect the results of its tax calculation.

You can retrieve the tax amounts from the
[tax](https://docs.stripe.com/api/invoices/object#invoice_object-tax) and
[total_tax_amounts](https://docs.stripe.com/api/invoices/object#invoice_object-total_tax_amounts)
fields on the upcoming invoice, and from the per-line-item
[tax_amounts](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-tax_amounts)
fields. The invoice has an
[automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax)
field showing the status of the calculation, with one of three possible
statuses:

StatusDescriptionPossible Action`complete`Stripe Tax has successfully assessed
the taxes on the payment.You can retrieve the tax amounts from the tax and
`total_tax_amounts` fields on the latest invoice, and from the per-line item
`tax_amounts` fields.`requires_location_inputs`Stripe Tax was unable to assess
taxes because it didn’t have enough information to determine the customer’s
location.Collect more information from a customer (such as a full street
address) and update the
[customer.address](https://docs.stripe.com/api/invoices/object#invoice_object-customer_address)
field.`failed`Internal Stripe error.Try the request again or contact Stripe
support for additional assistance.
## See also

- [Collect taxes for recurring
payments](https://docs.stripe.com/billing/taxes/collect-taxes?tax-calculation=stripe-tax)
- [Products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)

## Links

- [Stripe Tax](https://docs.stripe.com/tax)
- [setup guide](https://docs.stripe.com/tax/set-up)
- [Dashboard](https://dashboard.stripe.com/tax/migrations)
- [tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
- [address
information](https://docs.stripe.com/tax/customer-locations#address-hierarchy-other)
- [charge types](https://docs.stripe.com/connect/charges#types)
- [Customers page](https://dashboard.stripe.com/customers)
-
[customer.address](https://docs.stripe.com/api/customers/update#update_customer-address)
- [tax obligations](https://docs.stripe.com/tax/monitoring)
- [add an active registration](https://docs.stripe.com/tax/registering)
- [error](https://docs.stripe.com/error-codes)
- [an address that Stripe Tax can
use](https://docs.stripe.com/tax/customer-locations)
- [available tax codes](https://docs.stripe.com/tax/tax-codes)
- [guide for setting
up](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [products and
prices](https://docs.stripe.com/billing/taxes/collect-taxes#product-and-price-setup)
- [Tax Setup FAQ](https://docs.stripe.com/tax/faq#set-up)
- [Products page](https://dashboard.stripe.com/products?active=true)
- [products page](https://dashboard.stripe.com/products)
- [subscriptions page in the
Dashboard](https://dashboard.stripe.com/subscriptions)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [upcoming invoice](https://docs.stripe.com/api/invoices/upcoming)
- [tax](https://docs.stripe.com/api/invoices/object#invoice_object-tax)
-
[total_tax_amounts](https://docs.stripe.com/api/invoices/object#invoice_object-total_tax_amounts)
-
[tax_amounts](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-tax_amounts)
-
[automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax)
-
[customer.address](https://docs.stripe.com/api/invoices/object#invoice_object-customer_address)
- [Collect taxes for recurring
payments](https://docs.stripe.com/billing/taxes/collect-taxes?tax-calculation=stripe-tax)