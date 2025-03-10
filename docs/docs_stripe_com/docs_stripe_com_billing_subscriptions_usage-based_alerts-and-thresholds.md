# Alerts and thresholdsPublic preview

## Learn how to alert when a customer exceeds a usage threshold or trigger an invoice when a customer hits a billing threshold.

Use alerts to notify you when customers exceed meter usage thresholds, or to
trigger an invoice when customers reach a specific billing threshold. You can
create alerts that apply to specific customers or all customers.

Create usage alerts in your business workflows, such as the following:

- **Email users**: Allow customers to configure usage limits, and send an email
when they hit their limit.
- **De-provision access**: Grant customers a free number of usage units to your
service, and remove access when they exceed the limit.
- **Notify the sales team of an upsell**: Alert your sales team of an enterprise
opportunity when a self-serve user exceeds a usage threshold.

Stripe provides a usage alert type called `One-time per-customer usage alert`.
This alert triggers when a customer exceeds the specified usage level for the
first time, and only triggers one time per customer, regardless of future usage.

## Create usage alerts

You can configure [alerts](https://docs.stripe.com/api/billing/alert/create)
using the Stripe Dashboard or API.

For example, you can create a one-time alert for customers that triggers when
they reach 100 API calls. When a customer reaches 100 API calls, you receive a
webhook notifying you that the customer has exceeded the threshold.

DashboardAPI- On the [Billing
Alerts](https://dashboard.stripe.com/settings/billing/alerts) page, click
**Create alert**.
- On the **New alert** page, do the following:

- For **Name**, enter the name for your alert. This isn’t visible to customers.
- Under **Alert type**, select the meter that you want to set up alerts for.
- For **Unit threshold**, set the usage amount to reach for an alert to trigger.
- *(Optional)* Under **Application**, select **Specific customer** and the
customer name, if you want the alert to apply only to that customer. Otherwise,
leave the default of **Any customer** to configure the alert for all customers.
- Click **Create alert**.

## Create billing thresholds

You can create
[billing_thresholds](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_thresholds)
to issue an [invoice](https://docs.stripe.com/api/invoices) when a customer’s
accrued usage in a subscription cycle reaches a specific monetary threshold. You
can also reset a subscription’s
[billing_cycle_anchor](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_thresholds-reset_billing_cycle_anchor)
when a customer reaches the monetary threshold.

Consider using billing thresholds to limit the amount owed or the products
consumed between invoices or charges.

### Monetary thresholds

When you add a monetary threshold to a subscription, set the value as a multiple
of the cost of one unit of the product being sold. Setting a lower amount for
the threshold results in your customers receiving an invoice for every unit of
usage.

The value is a positive integer in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal) (for example, 100 cents
to charge 1 USD, or 100 to charge 100 JPY, a zero-decimal currency). Set the
value to at least 50 currency units.

You can set monetary thresholds for a subscription using the Stripe
[Dashboard](https://dashboard.stripe.com/test/subscriptions) or the API.

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "billing_thresholds[amount_gte]"=10000 \
 -d "billing_thresholds[reset_billing_cycle_anchor]"=false
```

### Usage thresholds

When you add a usage threshold to a subscription item, set the value to exceed
one unit of usage to prevent frequent invoicing. Stripe doesn’t support setting
usage thresholds in the Dashboard.

```
curl https://api.stripe.com/v1/subscription_items/si_CFhSgkWb0MyTWg \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "billing_thresholds[usage_gte]"=2000
```

### Thresholds and the billing cycle anchor

By default, the [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle) of a
subscription remains unchanged after a customer reaches the usage threshold. If
a customer reaches the threshold mid-month of a monthly subscription, the
subscription resets at the end of the month, similar to a subscription without
thresholds.

You can change the default behavior by configuring the subscription to reset the
billing cycle anchor after it reaches the threshold. Stripe treats this
configured behavior as if the subscription naturally arrived at its rollover
point at the end of the month.

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "billing_thresholds[reset_billing_cycle_anchor]"=true
```

### Thresholds and tiered pricing

Stripe maintains tiers across threshold invoices. By default, tiers reset at the
end of each billing period. You can change the default behavior by configuring
the subscription to reset the billing cycle anchor after it reaches the
threshold, similar to a subscription without thresholds.

For example, you run an ad platform with the following graduated tier structure
for ad impressions:

TierAmount (unit cost)1-10000 (`up_to=10000`)0.50 USD (`unit_amount=50`)10000+
(`up_to=inf`)0.40 USD (`unit_amount=40`)
Because Stripe bills usage retrospectively, you can set a temporary threshold of
100 USD for new customers. Under this plan, you bill your customer every 200
impressions for the first 10,000 impressions (200 × 0.50 USD = 100 USD). When
the customer exceeds 10,000 impressions, they’re billed every 250 impressions
(250 × 0.40 USD = 100 USD). This continues until the end of the billing period,
at which point you can invoice all usage that wasn’t previously invoiced, and
the subscription and tiers reset.

To reset tiers after reaching a threshold, you must configure the subscription
to reset the billing cycle anchor after the usage reaches the thresholds that
you set.

### Volume tiers

Volume tiers define the pricing for all units of usage, as opposed to graduated
tiers, which define pricing for a specific amount of usage. Some pricing models
use volume tiers that decrease the unit cost at each successive tier. You can
use these models to incentivize customers to use more of a product (for example,
ad impressions, or GB of storage).

When combined with thresholds, these pricing models can lead to invoices with
line items for negative amounts under the following conditions:

- A threshold invoice has already been issued.
- Subsequent usage gets billed to customers at a lower unit cost.

For example, consider the following tiered pricing structure:

TierAmount (unit cost)1-10000 (`up_to=10000`)0.50 USD (`unit_amount=50`)10000+
(`up_to=inf`)0.40 USD (`unit_amount=40`)
If a customer uses 10,000 units, the invoice total is 5,000 USD (10,000 x 0.50
USD = 5,000 USD). Any additional usage causes *all* usage to bill at the lower
unit cost of 0.40 USD. If the customer uses one more unit, the invoice total
*drops* to 4,000.40 USD (10,001 x 0.40 USD = 4,000.40 USD).

Without thresholds, Stripe would issue an invoice for 4,000.40 USD at the end of
the billing period.

To demonstrate how negative invoicing can occur, assume you set a monetary
threshold of 5,000 USD. In this scenario, Stripe issues an invoice when the
customer reaches 10,000 units of usage.

If the customer uses one more unit, the invoice total drops to 4,000.40 USD
(10,001 × 0.40 USD = 4,000.40 USD). However, if the customer doesn’t consume
more units, they’re *owed* 999.60 USD (5,000 USD − 4,000.40 USD = 999.60 USD).
At the end of the billing period, Stripe credits this amount to the customer’s
balance, which we use to pay future invoices.

If the customer continues to accrue usage, the cost of the usage reaches 5,000
USD again when the customer uses 12,500 units (5,000 USD / 0.40 USD = 12,500).
However, the previous payment of 5,000 USD covers all of this usage. As a
result, we don’t issue an invoice.

Stripe won’t issue an invoice until either the total usage reaches 25,000 units
(for a total cost of 10,000 USD), or the end of the billing period
arrives—whichever occurs first. The tables below show the line items you see for
the two invoices issued in the scenario where usage reaches 25,000 units.

Invoice 1:

Line itemQuantityAmountUsage (0.50 USD per unit)10,0005,000 USDTotal5,000 USD
Invoice 2:

Line itemQuantityAmountUsage (0.40 USD per unit)25,00010,000 USDAmount
previously billed (at 0.50 USD per unit)-5,000 USDTotal5,000 USD
## Listen for webhooks

After you configure an alert and start sending usage for that meter, you can
listen for [webhooks](https://docs.stripe.com/webhooks). These events trigger
when there’s a status change in Stripe, such as creating a new subscription or
invoice.

In your application, set up an HTTP handler to accept a POST request containing
the webhook event, and verify the signature of the event.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/webhook' do
# You can use webhooks to receive information about asynchronous payment events.
# For more information, see https://stripe.com/docs/webhooks.
webhook_secret = ENV['STRIPE_WEBHOOK_SECRET']
payload = request.body.read
if !webhook_secret.empty?
```

See all 45 lines
During development, use the Stripe CLI to [monitor webhooks and forward them to
your application](https://docs.stripe.com/webhooks#test-webhook). Run the
following in a new terminal while your development app is running:

```
stripe listen --forward-to localhost:4242/webhook
```

For production, set up a webhook endpoint URL in the Dashboard, or use [Webhook
Endpoints](https://docs.stripe.com/api/webhook_endpoints).

## Limitations

Consider the following limitations for usage alerts:

- Alerts are only evaluated on usage data reported after alert creation.
- You can create a maximum of 25 alerts for each combination of a specific meter
and customer. However, you can create an alert for a specific meter for each of
your customers.
- Alerts currently don’t work with test clocks.

Consider the following limitations for billing thresholds:

- Thresholds don’t apply to [trial
subscriptions](https://docs.stripe.com/billing/subscriptions/trials).
- Billing thresholds aren’t evaluated in the 24 hours before a subscription
ends. This helps limit confusion for a customer who receives multiple invoices
on the same date.
- Monetary thresholds must be greater than the sum of any flat fees on metered
subscription items.
- When determining if a monetary threshold has been reached, the value used
excludes taxes but includes discounts and billing credits.
- Subscriptions are only allowed a single monetary threshold.
- Subscription items are only allowed a single usage threshold.
- Invoiced amounts or usage might be slightly higher than the specified
thresholds because invoices aren’t issued at the exact moment a specified
threshold is reached.
- Per-package tiered pricing isn’t currently supported.

## Links

- [alerts](https://docs.stripe.com/api/billing/alert/create)
- [Billing Alerts](https://dashboard.stripe.com/settings/billing/alerts)
-
[billing_thresholds](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_thresholds)
- [invoice](https://docs.stripe.com/api/invoices)
-
[billing_cycle_anchor](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_thresholds-reset_billing_cycle_anchor)
- [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal)
- [Dashboard](https://dashboard.stripe.com/test/subscriptions)
- [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [webhooks](https://docs.stripe.com/webhooks)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [https://stripe.com/docs/webhooks.](https://stripe.com/docs/webhooks)
- [monitor webhooks and forward them to your
application](https://docs.stripe.com/webhooks#test-webhook)
- [Webhook Endpoints](https://docs.stripe.com/api/webhook_endpoints)
- [trial subscriptions](https://docs.stripe.com/billing/subscriptions/trials)