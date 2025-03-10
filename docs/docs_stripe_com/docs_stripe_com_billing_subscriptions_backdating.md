# Backdate subscriptions

## Learn how to backdate subscriptions.

You can backdate a subscription to bill customers for time that has already
elapsed. This is often used when migrating to Stripe or for record keeping
purposes. The `backdate_start_date` field specifies the subscription’s backdated
start date. You also have the option to bill customers for this elapsed time and
set the next billing date.

## Backdating and charging users

Sometimes users can have access to your service before you create a subscription
for them, and you want to charge them for that access.

DashboardAPI
To charge users for this time through the Dashboard:

- Go to the **Payments** > **Subscriptions** page.
- Click **+Create subscription**.
- Find or add a customer.
- Enter the pricing and product information.
- In the **Subscription details** section, select the start and end dates of the
subscription. To backdate it, select a start date in the past.
- Select the date that you want to start the billing cycle on.
- (Optional) Set the **Payment** or **Advanced** options.
- Click **Create subscription**. The subscription starts on the date you
selected.

This creates an [invoice](https://docs.stripe.com/api/invoices) with a prorated
amount for the time between the backdated start date and the current time. The
prorated amount is calculated based on an imagined interval that starts on the
backdated start date. For example, if the billing interval is monthly on the
first of the month, and you set the `backdate_start_date` to February 15 (in a
non-leap year), the proration calculation is based on a month running February
15 to March 15. Because that imagined month is 28 days, the prorated amount for
the 14 days of February 15 to March 1 is exactly half the amount of a normal
monthly charge.

Similarly, if you set the `backdate_start_date` to January 15, the proration
calculation is based on an imagined month running January 15 to February 15.
Because that month is 31 days, the prorated amount for the 17 days of January 15
to February 1 is 17 divided by 31 (or 0.548) of a normal monthly charge.

Another way to think about the calculation is to look at the backdated start
date as the original start date and the beginning of the first full billing
period as an updated start date.

## Backdating without charging users

You can also backdate a subscription without charging the customer for the
backdated period, which you can use if you’re migrating to Stripe. To do so,
pass `proration_behavior: 'none'` when you create the subscription. That sets
the `start_date` to the same value as `backdate_start_date`, but it doesn’t
charge the customer for backdated time.

## Backdating and setting the billing cycle anchor

You can combine `backdate_start_date` with `billing_cycle_anchor` to backdate a
subscription and set the billing cycle anchor to a date in the future. This
creates a prorated item on the next invoice for the time between the backdated
start date and the billing cycle anchor. You can use this if you’re migrating to
Stripe and need to carry over the next billing date for your subscriptions while
billing customers for elapsed time.

For example, say it’s October 15 and you’re migrating to Stripe. You have a
subscription that started on September 1, and the next billing date is November
1. To migrate that subscription, create a new subscription and set
`backdate_start_date` to September 1 and `billing_cycle_anchor` to November 1.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d backdate_start_date=1575176400 \
 -d billing_cycle_anchor=1572580800 \
 -d "items[0][price]"={{PRICE_ID}}
```

This immediately issues an invoice for the prorated amount covering the time
between September 1 and November 1. It also sets the `start_date` of the
subscription to September 1. Stripe issues the next invoice on November 1.

!

## Backdating an update

To set the effective date of
[prorations](https://docs.stripe.com/billing/subscriptions/prorations) when
updating a subscription, use the
[proration_date](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_date)
parameter. Pass an integer Unix timestamp within the subscription’s current
period. If the subscription is backed by a subscription schedule, make sure that
the timestamp is before the start date of the next phase of the subscription
schedule.

You can set a `proration_date` earlier than the current period only during the
first period of a backdated subscription. In this case, the `proration_date` can
be on or after the `subscription[start_date]` (backdated start date). In all
other cases, the `proration_date` can’t be before the `current_period_start`.

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [prorations](https://docs.stripe.com/billing/subscriptions/prorations)
-
[proration_date](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_date)