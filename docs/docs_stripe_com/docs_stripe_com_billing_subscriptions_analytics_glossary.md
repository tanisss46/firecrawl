# Billing metric definitions

## Metric definitions and examples for Billing metrics.

Below you’ll find definitions and examples for metrics found in the [Billing
analytics Dashboard](https://dashboard.stripe.com/billing) and in downloadable
reports.

## Metric definitions

### Customers, subscribers, and subscriptions

In Stripe, you create [Customer](https://docs.stripe.com/api/customers) and
[Subscription](https://docs.stripe.com/billing/subscriptions/creating) objects.
If a customer has one or more subscriptions attached, Stripe considers that
customer to be a subscriber. If any of the customer’s subscriptions are paid
subscriptions in an `active` or `past_due` state, the customer is an active
subscriber.

When a subscriber’s subscription is canceled or marked as `unpaid`, then the
subscription is considered churn and no longer counts towards MRR.

When all of a subscriber’s subscriptions are canceled or marked as `unpaid`,
then the subscriber is considered to have churned and no longer counts as an
active subscriber.

### Monthly Recurring Revenue (MRR)

MRR is the sum of the monthly-normalized value of all your `active` and
`past_due` subscriptions. MRR calculations exclude subscriptions in trial
periods, any taxes applied to the subscription, any subscribers on free plans,
and any metered (usage based) products.

#### Example

In a given period, 100 subscribers are on Plan A (100 USD per month) and 50
subscribers are on Plan B (600 USD per year). MRR = (100 × 100 USD) + (50 × (800
USD/12)) = 12,500 USD

Learn more about how your [MRR is impacted by taxes, trials, delinquency, and
refunds](https://support.stripe.com/questions/understanding-monthly-recurring-revenue-(mrr)).

If you charge your customers based on usage and want to include usage based
products in your MRR and subscription metrics, sign up below to receive updates
about sign up below for updates.

### MRR growth

MRR growth is the net change in your MRR over a period of time starting with the
MRR at the beginning of the period, adding any new MRR and expansion MRR,
subtracting any contraction MRR and any churn MRR and adjusting for any foreign
currency (FX) impact.

MRR Growth = [(New MRR) + (Reactivation MRR) + (Expansion MRR)] − [(Churned MRR)
+ (Contraction MRR)] + FX adjustment MRR
#### Example

At the start of the period, your MRR is 1,000 USD.

- **New MRR**: During the period, you have one subscriber convert from a free
trial to Plan A (100 USD per month). This is a positive change of +100 USD to
your MRR.
- **Expansion**: During the period, you have one subscriber upgrade from Plan A
(100 USD month) to Plan C (150 USD per month). This is a positive change of +50
USD to your MRR.
- **Contraction**: During the period, you have one subscriber downgrade from
Plan A (100 USD per month) to Plan B (60 USD per month). This is a negative
change of -40 USD to your MRR.
- **Churn**: During the period, you have one subscriber downgrade from Plan B
(60 USD per month). This is a negative change of -60 USD to your MRR.
- **FX Adjustment**: You have a single customer paying in a foreign currency.
They subscribed to Plan A in a foreign currency last period. During that period
it was worth (100 USD per month) but the currency lost value in the current
period and it’s now worth 95 USD per month. This is a negative change of -5 USD
to your MRR.

Here’s a summary breakdown:

MetricAmountBeginning MRR1,000 USDNew MRR100 USDExpansion MRR50 USDContraction
MRR40 USDChurn MRR-60 USDFX adjustment-5 USDMRR growth45 USDEnding MRR1,045 USD
### Active subscribers

Active subscribers only includes subscribers with positive MRR that are in an
`active` or `past_due` state ([read more about subscription states
here](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)).
It doesn’t include subscribers on free plans or trials. A customer with multiple
active subscriptions is counted as a single active subscriber.

If a subscriber drops to 0 USD in MRR, we consider them churned in the period.
This most commonly happens when a subscription is canceled. It can also occur if
you’re choosing to subtract discounts from your MRR. In this case, we consider a
subscriber churned if they have a 100% coupon applied and they become active
again if you remove the coupon.

Total active subscribers = Active subscribers + Past due subscribers
### Active subscriber growth

Active subscriber growth is the net change in your number of active subscribers
over a period of time. Start with the number of active subscribers at the
beginning of the period, add any new active subscribers and any reactivated
subscribers, and subtract any churned subscribers.

Active Subscriber Growth = (New subscribers) + (Reactivated subscribers) -
(Churned subscribers)
### New subscribers

The sum of paid subscribers who became active for the first time during the
period. This doesn’t include subscribers on free plans or trials. We don’t count
existing paid subscribers who add additional subscriptions multiple times. We
also don’t include reactivated customers.

### New trials

New trials refers to the sum of subscriptions that started a trial during the
period. We count the number of trials at the subscription level rather than at
the customer level so a single customer could count as multiple trials.

#### Example

- Jane creates two subscriptions in January.- Each subscription starts with a
7-day free trial period on January 1.
- Jane counts as two new trials in January.
- John enters a 7-day free trial period on January 1.- John doesn’t renew.
- John then enters another 7-day free trial on January 21.
- John counts as two new trials in January.

### Trial conversion rate

The trial conversion rate is the number of subscriptions that converted from a
trial to a paid plan in the last 30 days divided by the number of trials that
ended in the last 30 days. The number might exceed 100% if some subscriptions
convert to a paid plan after the end of their trial period.

The number reflects the trial conversion rate at the end of the selected time
period.

The trial conversion rate = (Total subscriptions that converted from trial to
paid in the last 30 days) / (Total trials that ended in the last 30 days)
#### Example

During the month, 100 new trials were created and 15 trials converted. The trial
conversion rate equals 15 divided by 100, or 15

### Subscriber churn rate

The number of active subscribers lost due to churn over the last 30 days divided
by the number of active subscribers in a given period divided by the number of
active subscribers at the start of the period.

The subscriber churn rate is the total churned subscribers in the past 30 days,
divided by the number of active subscribers 30 days ago, plus the total new
subscribers in the past 30 days:

(Total churned subscribers in the past 30 days) / [(Number of active subscribers
30 days ago) + (Total new subscribers in the past 30 days)]
#### Example

At the start of the month, the business had 1000 subscribers. During the month,
the business added 100 subscribers and churned 100 subscribers. The subscriber
churn rate for the period equals the number of churned subscribers (100) divided
by the number of existing subscribers plus the number of added subscribers (1000
+ 100) or, 9.1

### Churned revenue

The sum of churned MRR and contraction MRR in the period.

Churned revenue = (total churned MRR) + (total contracted MRR)
#### Example

During the period, Jane cancels her 120 USD per year plan and John downgrades
from a 50 USD per month plan to a 25 USD per month plan. The churned revenue
during the period equals 10 (Jane) + 25 USD (John) = 35 USD.

### Retention by cohort

Stripe assigns cohorts to subscribers based off of when they first started
generating positive Monthly Recurring Revenue (MRR) by starting active paying
subscriptions. Revenue retention considers expansion and thus can increase above
100%.

For subscriber retention:

- The start value is the initial number of active subscribers in the cohort.
- Month x refers to the remaining number of active subscribers at the end of
each subsequent month.

For revenue retention:

- The start MRR is the MRR of all active subscribers in the cohort.
- Month x refers to the amount of MRR remaining from subscribers in the cohort
at the end of the each subsequent month. The MRR for a cohort can change due to
upgrades, downgrades, and cancellations and thus can exceed 100%.

#### Example

In January, 100 subscribers become active subscribers. Each month the subscriber
churn rate is 10%. Consequently you’d expect to the following retention rates in
each month:

- Month 1: 90
- Month 2: 81
- Month 3: 73
- Month 4: 66
- Month 5: 59% and so on.

In January, 100 subscribers became active on 10 USD per month plans. The
starting MRR is 1,000 USD. At the end of month 1, 10 subscribers have churned
and 5 subscribers have upgraded to 25 USD per month plans. The net MRR impact
is: 125 USD of expansion MRR − 100 USD of churn MRR = +25 USD. Therefore in
Month 1, you see 102.5% revenue retention.

### Average revenue per user (ARPU)

This is your average MRR per paid subscriber. ARPU is calculated by dividing
your total MRR by the number of active subscribers. The number reflects the ARPU
at the end of the selected time period.

ARPU = (Total MRR) / (Total active subscribers)
#### Example

You have 100 active subscribers at the end of January. The total MRR at the end
of January is 50,000 USD. Your ARPU at the end of January is 500 USD

### Subscriber lifetime value (LTV)

The subscriber lifetime value is calculated by dividing the Average revenue per
user (ARPU) by the subscriber churn rate. This is an estimate of LTV based on
the values at various points in time.

Subscriber lifetime value = (ARPU) / (Subscriber churn rate)
#### Example

January started with 110 subscribers and finished with 100 after 10 subscribers
churned. The total MRR at the end of January is 50,000 USD. The ARPU at the end
of January is 500 USD while the January subscriber churn rate was 9%. Subscriber
lifetime value at the end of January is therefore (500 USD) / (9%) = 5,555 USD

## Links

- [Billing analytics Dashboard](https://dashboard.stripe.com/billing)
- [Customer](https://docs.stripe.com/api/customers)
- [Subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [MRR is impacted by taxes, trials, delinquency, and
refunds](https://support.stripe.com/questions/understanding-monthly-recurring-revenue-(mrr))
- [read more about subscription states
here](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)