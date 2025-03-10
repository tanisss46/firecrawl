# Radar analytics center

## Review fraud patterns and their impact on your business in the Dashboard.

The [Radar analytics center](https://dashboard.stripe.com/radar) in the
Dashboard helps you analyze and understand the state of fraud for your business.
Stripe provides several reports with information about how much fraud
[Radar](https://docs.stripe.com/radar) blocks for your business and the top
fraud-related metrics for your business over time.

Using [Fraud insights](https://docs.stripe.com/radar/analytics/fraud-insights),
[Sigma](https://stripe.com/sigma), or [Data
Pipeline](https://stripe.com/data-pipeline), you can use [Radar rule
attributes](https://docs.stripe.com/radar/rules/reference#supported-attributes)
alongside your own dataset to:

- [Continuously improve your fraud
management](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data).
- Identify fraudulent payments.
- Create a deeper understanding of your customers.
- Analyze data in an environment that works best for you.

We’ve enhanced the depth and breadth of data we analyze in the new Radar
analytics center view, which appears by default in your **Radar Overview** tab
of the Dashboard. To return to the legacy overview page, use the **New
overview** toggle.

Radar Analytics centerPreviewLegacy Radar overview
The **Overview** tab of your Radar Dashboard acts as a command center to help
you gauge the efficacy of your fraud prevention strategy and Radar
interventions. From here, you can:

- View graphs detailing how fraud affects your business and how effectively
Radar manages it.
- Compare your fraud intervention results to other businesses like yours.
- Track your fraud performance with network monitoring programs.
- Learn more about fraud risk management tools and practices.

## Configure your data set

### Specify your time period

By default, statistics reflect the prior 30 days of transaction history,
following a 24-hour delay. To see data for a different time period:

- Click the **Date** filter to open the time period editor.
- Use the drop-down to choose a relative comparator.
- Depending on the comparator you choose, set the parameters, such as *in the
last 1 months* or *between 2/26/2024 and 3/18/2024*.
- Click **Apply**.

### Choose how and which data appears

Click **Configure** to customize the way data displays in the charts.

- **Calculate rates by transaction volume** instead of payment count.
Transaction volume is the cumulative amount charged for payments rather than the
number of payments.
- **Calculate fraud rates by fraud arrival date** instead of payment date. Fraud
arrival date is the timestamp when a transaction counts as fraud. This might be
the time the issuer flagged it or the time the card holder filed a dispute.
- **De-duplicate multiple attempts per payment intent** so retries of the same
payment count as a single instance.
- **Include setup intents** to see activity from off-session payments like
subscriptions, invoices, and on-demand purchases.

## Rate charts

The rate charts help you evaluate your fraud prevention strategy. They provide
details about the level of fraudulent activity affecting your Radar-screened
transactions for a given time period and the portion of transactions you block.
Together, these snapshots give you a complete view of how well you’re managing
fraud.

Each chart includes the following elements:

- The rate totals show the aggregate ratios for each metric represented in the
chart for the entire time period.
- The comparison icon indicates whether your rate is higher (exclamation icon)
or lower (checkmark icon) than other Stripe businesses in your demographic. You
can click the icon to see details.
- The bar chart shows the category ratios and rate at regular intervals for the
time period. You can hover over points in the graph to see metrics for specific
points in time.

The following sections describe the specific information provided for each rate
category.

### Fraud

The **Fraud** panel shows the aggregate ratios of transactions that resulted in
either a fraud dispute or an early fraud warning that hasn’t escalated to a
dispute. For each fraud indicator, you see the percentage of total transactions
in the time period and the number of transactions or total amount charged for
transactions, depending on your
[setting](https://docs.stripe.com/radar/analytics#choose-how-and-which-data-appears).

The totals section also shows your total fraud rate for the period with an icon
indicating how your rate’s standing among comparable Stripe businesses. Hover
over the icon to view detailed information about the fraud rates of similar
Stripe businesses and Stripe businesses within the same geographic region.

The interactive bar chart compares the ratio of fraud attributed to disputes
versus early fraud warnings. Regularly reviewing this information can help you
identify and address spikes and avoid monitoring program repercussions. The
chart also includes a line graph showing your fraud rate for the time period.

Enable the **Estimate worst case fraud rate** toggle to impose a second line
graph showing the machine learning prediction of what fraud might be for the
period, based on historical fraud arrival patterns. Cardholders can file
disputes 120 days or more after a payment, so the rate can fluctuate over time.

#### Note

If you don’t see the **Estimate worst case fraud rate** toggle in your
Dashboard, your fraud volume is too low for Stripe to accurately model possible
fraud or you enabled [Calculate fraud rates by fraud arrival
date](https://docs.stripe.com/radar/analytics#choose-how-and-which-data-appears).

Hover over specific points in the chart to view a modal with details for the
specific date. Details include the following data, if applicable for the date:

- Rates of fraudulent disputes, early fraud warning payments, and possible fraud
- Number of fraudulent dispute payments, early fraud warning payments, and
possible fraud payments
- Total amount charged in fraudulent dispute payments, early fraud warning
payments, and possible fraud payments

### Disputes

The **Disputes** panel shows the aggregate percentages of disputes due to fraud
compared with all other [types of
disputes](https://docs.stripe.com/disputes/categories) for the time period. It
also gives the dispute rate for the time period, calculated as the number of
disputed payments of any type divided by successful payments during the same
period. The icon indicates your rate’s standing among comparable Stripe
businesses. Hover over the icon to view detailed information about the dispute
rates of similar Stripe businesses and Stripe businesses within the same
geographic region.

The interactive bar chart compares the ratio of disputes due to fraud to
disputes of any other type, such as “product not received.” Disputes for reasons
other than fraud don’t count against your fraud rate. The chart also includes a
line graph showing your dispute rate for the time period.

Hover over specific points in the chart to view a modal with details for the
specific date. Details include the following data, if applicable for the date:

- Rates of fraudulent disputes, other disputes, and total disputes
- Number of fraudulent disputes, other disputes, and total disputes
- Total amount charged in fraudulent dispute payments, other dispute payments,
and total disputed payments

### Blocks

The **Blocks** panel shows the aggregate percentages of payments that Radar
blocked due to a [high risk
score](https://docs.stripe.com/radar/rules#machine-learning-risk-checks)
compared to payments blocked by a custom rule. It also gives the block rate for
the time period, calculated as the total number of blocked payments divided by
successful payments during the same period. The icon indicates your rate’s
standing among comparable Stripe businesses. Hover over the icon to view
detailed information about the block rates of similar Stripe businesses and
Stripe businesses within the same geographic region.

The interactive bar chart compares the ratio of high risk blocks to rule blocks.
The chart also includes a line graph showing your block rate for the time
period.

Hover over specific points in the chart to view a modal with details for the
specific date. Details include the following data, if applicable for the date:

- Rates of high risk blocks, rule blocks, and total blocks
- Number of high risk blocks, rule blocks, and total blocks
- Total amount for high risk blocks, rule blocks, and total blocks

## Rule matches

The **Rule matches** section gives you insight into how your rules are
performing. It shows which rules Radar acted on for all screened transactions
during the time period. The top of the panel shows the total number of
transactions processed during the time period and summary information for each
rule action type:

- Percentage of transactions where a rule match resulted in the prescribed
action.
- Total number of transactions where a rule match resulted in the prescribed
action.

You can click any of the rule action type summary cards to view details about
the rule matches within that type.

### Transactions

The **Transactions** detail shows a ratio graph of actions taken for all
transactions processed during the time period. For each action type, you see the
aggregate amount charged for all transactions where a rule match triggered the
specified action. Click an action type to view its details page.

Below the totals, an interactive line graph shows the transactions for each rule
action type in a timeline for the period. Click the graph to view a modal with
the following statistics for each action type on that date:

- **Rate** is the percentage of total transactions on that date where a rule
match resulted in the prescribed action.
- **Count** is the total number of transactions on that date where a rule match
resulted in the prescribed action.
- **Volume** is the total amount charged for transactions on that date where a
rule match resulted in the prescribed action.

### Blocked

The **Blocked** detail shows a ratio graph depicting the most matched block
rules for the time period. You also see the number of, and total amount charged
for, transactions that each of the most matched rules blocked.

Below the totals for the time period, you can review the bar graph showing the
ratio of blocked payments for each of the most matched rules on each interval of
the time period.

### 3DS

The **3DS** detail shows a ratio graph depicting the outcomes for transactions
in the time period where a 3DS rule triggered 3DS authentication requests. You
also see the total amount charged for 3DS requests that succeeded and failed.

Below the totals for the time period, you can review the bar graph showing the
ratio of 3DS authentication outcomes for each interval of the time period.

### Allow

The **Allow** detail shows a ratio graph depicting the outcomes of payments
occurring during the time period for transactions that matched an allow rule.
You also see the total amount charged for allowed transactions in each outcome
category:

- **Legitimate**: Allowed transactions where no further action occurred.
- **Disputes and Early fraud warnings**: Allowed transactions disputed for fraud
or issued early fraud warning.
- **Refunded** Allowed transactions that were refunded.

Below the totals for the time period, you can review the bar graph showing the
ratio of allowed payment outcomes for each interval of the time period.

### Review

The **Review** detail allows you to monitor how well your manual review rules
foreshadow a need for more decisive action. It might also act as a reminder to
take action on unreviewed transactions. The ratio graph compares the status of
transactions that triggered a manual review during the time period. You also see
the total amount charged for review transactions in each status category:

- **Currently in review**: No review action taken.
- **Approved**: Transactions reviewed and determined legitimate.
- **Rejected**: Transactions reviewed and either refunded or canceled.
- **Failed**: Transactions matched for review, but declined.
- **Disputed**: Transactions matched for review, then ultimately disputed.
Transactions previously counted as either still in review or approved only count
as disputed after the cardholder files a dispute.

Click any row in the table to open the **Rules** tab of the Dashboard, showing
the **Rule performance** metrics.

Below the totals for the time period, you can review the bar graph showing the
ratio of allowed payment outcomes for each interval in the time period.

## Card monitoring programs

Card networks track your fraud and dispute rates as part of their risk
evaluation process. If your rates exceed their defined thresholds, they can
place your business in a monitoring program that assesses fines and fees until
you maintain fraud and disputes at acceptable levels.

Radar analytics monitors your fraud and dispute rates against the thresholds for
the card monitoring programs and provides your current status. Click a program
card to see details about the program, including the penalties associated with
rates in excess of the threshold.

## Links

- [Radar analytics center](https://dashboard.stripe.com/radar)
- [Radar](https://docs.stripe.com/radar)
- [Fraud insights](https://docs.stripe.com/radar/analytics/fraud-insights)
- [Sigma](https://stripe.com/sigma)
- [Data Pipeline](https://stripe.com/data-pipeline)
- [Radar rule
attributes](https://docs.stripe.com/radar/rules/reference#supported-attributes)
- [Continuously improve your fraud
management](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [types of disputes](https://docs.stripe.com/disputes/categories)
- [high risk
score](https://docs.stripe.com/radar/rules#machine-learning-risk-checks)