# Setting the subscription billing cycle date

## Learn how to set the billing date for subscriptions.

A subscription’s billing cycle depends on two factors:

- The recurring interval of its
[price](https://docs.stripe.com/products-prices/overview) or prices, such as
monthly, yearly, weekly, and so on.
- The [billing cycle
anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_cycle_anchor)
is the reference point that aligns future billing cycle dates. It sets the day
of week for `week` intervals, the day of month for `month` and `year` intervals,
and the month of year for `year` intervals. The default value is either the
subscription creation date or the trial end date (if you’re using a trial
period). You can also explicitly set this value at the time you create the
subscription.

#### Note

Billing cycle anchors are UNIX timestamps in seconds from the current epoch.

The following are examples of monthly subscriptions with different billing
cycles:

- A monthly subscription with a billing cycle anchor date of September 2 always
bills on the 2nd day of the month.
- A monthly subscription with a billing cycle anchor date of January 31 bills
the last day of the month closest to the anchor date, so February 28 (or
February 29 in a leap year), then March 31, April 30, and so on.
- A weekly subscription with a billing cycle anchor date of Friday, June 3 bills
every Friday thereafter.

Full billing periods start on the first full
[invoice](https://docs.stripe.com/api/invoices) date, which is often the same as
the billing cycle anchor and is always interval-aligned with it.

## Specify the billing cycle anchor for new subscriptions

#### Note

The subscription creation time matches the time of the request. It is not the
same as the subscription start date. Learn more about [backdating and billing
cycle
anchors](https://docs.stripe.com/billing/subscriptions/backdating#backdating-billing-cycle).

There are two ways to set the billing cycle anchor on new subscriptions:

- Use `billing_cycle_anchor_config` to calculate the timestamp for you (monthly
or yearly subscriptions only).
- Use `billing_cycle_anchor` to accept the timestamp directly.

If you’re creating a monthly or yearly subscription, we recommend using the
`billing_cycle_anchor_config` parameter because it automatically factors in
short months and leap years for you. If you’re creating a daily or weekly
subscription, or if you prefer to set the cycle date of your subscription using
a timestamp, use the `billing_cycle_anchor` parameter directly.

### Use billing_cycle_anchor_config

To create an integration with monthly and yearly subscriptions, use
`billing_cycle_anchor_config` on [create
subscription](https://docs.stripe.com/api#create_subscription) to specify the
day of the month on which to anchor.

Set `day_of_month` to `31` to create a monthly subscription that cycles at the
end of the month, even in months with less than 31 days. If a month has less
than 31 days, the subscription cycles on the last day of that month.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d "billing_cycle_anchor_config[day_of_month]"=31
```

You can also specify `month` to control the month of year for the anchor on
multi-month and yearly subscriptions.

To cycle your yearly subscriptions on the first of July, create a yearly
subscription with a `month` of `7` and `day_of_month` of `1`.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d "billing_cycle_anchor_config[month]"=7 \
 -d "billing_cycle_anchor_config[day_of_month]"=1
```

You can specify the exact month, day, hour, minute, and second for the billing
cycle anchor by using `billing_cycle_anchor_config`. If you don’t specify the
hour, minute, and second, they default to the values of the subscription
creation time.

The billing cycle anchor uses Coordinated Universal Time (UTC). For example, if
you create a subscription using `billing_cycle_anchor_config` at 5 PM EST
without specifying the hour, the time is recorded in the system as 10 PM UTC.

`billing_cycle_anchor_config` does not support anchoring on a backdated start
date.

For example, if you have an existing monthly subscription with a
`billing_cycle_anchor` timestamp that contains the day of the month, hour,
minute, and second of 15, 12, 30, and 0, you can align a new monthly
subscription with it. To do this, set `day_of_month`, `hour`, `minute`, and
`second` to match those same values, respectively.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d "billing_cycle_anchor_config[day_of_month]"=15 \
 -d "billing_cycle_anchor_config[hour]"=12 \
 -d "billing_cycle_anchor_config[minute]"=30 \
 -d "billing_cycle_anchor_config[second]"=0
```

If you use `billing_cycle_anchor_config`, it might result in a
`billing_cycle_anchor` that’s more than one billing period in the future.
However, the date for the first full invoice always falls within one billing
period from the creation of the subscription or the ending of a free trial.

For example, assume that you create a two-month interval subscription in
February and you cycle it at the end of every month by setting `day_of_month` to
`31`. The next month that has 31 days on two-month intervals from February is
August, which results in a billing cycle anchor on August 31. However, the first
full invoice date for this subscription still occurs in February. There’s an
initial, prorated period from subscription creation until February 28 (or 29
during a leap year), followed by a full two-month billing period.

### Use billing_cycle_anchor

You can create a subscription with an explicit billing cycle anchor using the
Subscriptions API or Checkout.

Subscriptions APICheckout
Call [create subscription](https://docs.stripe.com/api#create_subscription),
setting a timestamp for `billing_cycle_anchor`.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d billing_cycle_anchor=1611008505
```

### Configure proration behavior

Regardless of which API parameter you use, Stripe automatically creates a
prorated invoice to bill for the period between the subscription creation date
and the first full invoice date.

If you don’t want to immediately charge a customer for the period between the
subscription creation and the first full invoice date, either:

- [Disable the
proration](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)
by setting `proration_behavior` to `none`, making the initial period up to the
first full invoice date free. This action doesn’t generate an invoice at all
until the first billing cycle.
- [Combine a trial with the
billing_cycle_anchor](https://docs.stripe.com/billing/subscriptions/trials#combine-trial-anchor)
by setting `trial_end` to a timestamp representing the date when the free trial
ends. Depending on the duration of the free trial and the number of days until
the first full invoice date, this option might result in a prorated invoice
following the trial period. For example, a free trial is 7 days and the billing
cycle is monthly on the 1st. If the customer subscribes on the 15th, we generate
a prorated invoice on the 22nd for the period between the 22nd and the 1st, then
invoice for the full amount on the 1st of each month thereafter. If a customer
subscribes on the 28th, the free trial extends past the 1st, generating a
prorated invoice until the next month.

## Change the billing cycle on pre-existing subscriptions

Use the [Subscriptions API](https://docs.stripe.com/api/subscriptions/update) or
[Dashboard](https://dashboard.stripe.com/subscriptions) to change the billing
date of an existing subscription through one of the following options:

- Reset the billing cycle anchor to the current time.
- Add a [free trial](https://docs.stripe.com/billing/subscriptions/trials) to
automatically set the anchor date to the end of the trial. Trials typically
start when you create a subscription, but you can also apply them to existing
subscriptions, allowing you to credit the customer for the days left in the
previous cycle that they already paid.
- If all the prices are zero-amount, adding one or more paid prices immediately
resets the billing period. See the [upgrade and downgrade
guide](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade#handling-zero-amount-prices-and-quantities)
for more details on this scenario.

### Reset the billing cycle to the current time

To reset the billing cycle anchor, make an update request request with
`billing_cycle_anchor` set to `now`. This sets the billing cycle anchor to the
time of the update request. When you reset the billing cycle anchor, Stripe
immediately sends an invoice. [Enable
proration](https://docs.stripe.com/api/subscriptions/create#create_subscription-proration_behavior)
to credit the customer for any days already paid in the previous period.
Disabling proration might result in overcharging your customer.

APIDashboard
Call [update the subscription](https://docs.stripe.com/api#update_subscription),
setting `billing_cycle_anchor` to `now` and `proration_behavior` to
`create_prorations` to prevent overcharging the customer for any days they
already paid in the previous cycle.

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d billing_cycle_anchor=now \
 -d proration_behavior=create_prorations
```

### Add a trial to change the billing cycle

Adding a non-prorated trial period to an existing subscription allows you to
configure the billing cycle to be any date.

Typically, if you’re using the trial period to change the billing cycle without
issuing a prorated invoice, you disable proration because the length of the
trial period accounts for the portion already paid from the previous billing
cycle.

For example, if a customer has an active subscription set to bill next on July
23, and you introduce a trial period until August 1:

- The customer receives a 0 USD invoice on July 15.
- The customer isn’t billed on July 23.
- The customer is billed next on August 1, then on September 1, and so on.
- The customer already paid through July 23 in the previous cycle, so that
“free” period isn’t actually free.
- The period between July 23 and July 31 isn’t charged.
- The new cycle billed on August 1 is a full cycle at the normal rate.
APIDashboard
Call [update subscription](https://docs.stripe.com/api#update_subscription),
setting `trial_end` to a Unix timestamp representing the end date for the trial
(also the new billing cycle anchor) and `proration_behavior` to `none`.

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d trial_end=1611008505 \
 -d proration_behavior=none
```

## Metered billing

With [metered billing](https://docs.stripe.com/products-prices/pricing-models),
the price paid by the customer varies based on consumption during the billing
cycle. When changing the billing cycle results in ending a subscription interval
early, you charge the customer for the usage accrued during the shortened
billing cycle.

### Thresholds

In addition to the regular cycle, you can configure subscriptions to bill
whenever the amount due reaches a
[threshold](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds).

If you have a subscription configured to invoice this way, you can set it up to
reset the subscription cycle when it hits the threshold.

## See also

- [Using trial periods](https://docs.stripe.com/billing/subscriptions/trials)
- [Update Subscription](https://docs.stripe.com/api#update_subscription)

## Links

- [price](https://docs.stripe.com/products-prices/overview)
- [billing cycle
anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_cycle_anchor)
- [invoice](https://docs.stripe.com/api/invoices)
- [backdating and billing cycle
anchors](https://docs.stripe.com/billing/subscriptions/backdating#backdating-billing-cycle)
- [create subscription](https://docs.stripe.com/api#create_subscription)
- [Disable the
proration](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)
- [Combine a trial with the
billing_cycle_anchor](https://docs.stripe.com/billing/subscriptions/trials#combine-trial-anchor)
- [Subscriptions API](https://docs.stripe.com/api/subscriptions/update)
- [Dashboard](https://dashboard.stripe.com/subscriptions)
- [free trial](https://docs.stripe.com/billing/subscriptions/trials)
- [upgrade and downgrade
guide](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade#handling-zero-amount-prices-and-quantities)
- [Enable
proration](https://docs.stripe.com/api/subscriptions/create#create_subscription-proration_behavior)
- [update the subscription](https://docs.stripe.com/api#update_subscription)
- [metered billing](https://docs.stripe.com/products-prices/pricing-models)
-
[threshold](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds)