# Risk controls

## Adjust how aggressively you block fraud for your business with Radar for Fraud Teams.

To adjust the default risk score for blocking payments, use Radar for fraud
teams. Go to the [Radar risk
controls](https://dashboard.stripe.com/settings/radar/risk-controls) page to
make your adjustments.

![Screenshot of the drawer you see when adjusting your Radar risk
controls](https://b.stripecdn.com/docs-statics-srv/assets/new-overview.34e6267dd144e7f58ab45f3b07a7e316.png)

The risk settings dialog shows your block threshold, your dispute rate, and
other important statistics

## How it works

Stripe Radar gives each charge a numerical [risk
score](https://docs.stripe.com/radar/risk-evaluation#risk-outcomes) between 0
and 99, where 0 is the lowest risk and 99 highest.

### Blocking payments

The default *blocking threshold* is 75, meaning Radar blocks charges with a
score of 75 or higher. If you decrease your threshold, you’ll block more
payments.

You need to make sure [the default block
rule](https://docs.stripe.com/radar/rules#built-in-rules) or an equivalent
custom rule is enabled for Radar to block transactions based on this threshold.

### Manual reviews

The default *manual review threshold* is 65, meaning Radar sends charges with a
score of 65 or higher to manual review. Changing the blocking threshold
automatically changes the manual review threshold accordingly.

For Radar to send transactions to manual reviews based on this threshold, you
need to enable [the default review
rule](https://docs.stripe.com/radar/rules#built-in-rules) or equivalent custom
rules.

### Adjusting your threshold

When you change your blocking threshold, you see the following statistics:

MetricDescriptionEstimated fraud volume that is blocked or allowedThe estimated
volume of fraudulent payments that will be blocked or allowed at the new
blocking threshold.Estimated good volume that is blocked or allowedThe estimated
volume of good payments that will be blocked or allowed at the new blocking
threshold.Estimated previously blocked volume that is blocked or allowedThe
estimated volume of previously blocked payments that will be blocked or allowed
at the new blocking threshold. Because these payments were blocked and never
processed, some of these payments might be fraudulent.Fraud rate by volumeThe
percent of payments by volume that have received a dispute, an Early Fraud
Warning (EFW), or were refunded as fraud.Block rate by volumeThe percent of
payments by volume that were attempted but were blocked by Radar or by Stripe.
Payments are blocked by Stripe to protect you from card testing and other risks
that affect all users, regardless of your usage of Radar.
## When to use it

You can customize the default threshold to fit your own business needs. Setting
the risk score threshold requires you to consider a tradeoff between how much
fraud Radar blocks and how many payments it allows.

### Block more fraud

If your business is experiencing higher rates of fraud, you can decrease the
score for blocking payments. To determine what risk score is right for your
business, hover over the **Block additional payments by setting your acceptable
risk score** chart.

![Screenshot that shows the chart with good and fraudulent payments by risk
score](https://b.stripecdn.com/docs-statics-srv/assets/new-blocked-volume-chart.a439ebbb6db56c1245bf744e516120c7.png)

This chart shows how many fraudulent and good payments you would’ve blocked if
you set your threshold at that risk score. Here, you can see:

MetricDescriptionVolume blockedVolume of fraudulent and good payments would be
blocked.% blockedThe percent of fraudulent and good payments that are blocked
respectively. For example, blocking at 65 would result in 55% of your fraud
getting blocked at the expense of only 1% of good payments.# of payments
blockedNumber of fraudulent and good payments would be blocked.
Ultimately, it is up to your business to decide what tradeoff you’re willing to
accept in terms of how much fraud versus good payments you block.

### Allow more payments

If your business has low fraud rates and costs, you might want to increase the
default blocking score so that you can allow more payments overall.

![Screenshot that shows the chart with blocked payments by risk
score](https://b.stripecdn.com/docs-statics-srv/assets/new-allowed-volume-chart.520f969604f2c058be9330391eb05aaa.png)

This chart shows how many payments you would allow if you set your threshold at
that risk score. Here, you can see:

MetricDescriptionVolume allowedVolume of payments would be allowed.# of payments
allowedNumber of payments that would be allowed.
If you’re increasing the risk score for blocking charges, we can’t accurately
predict the impact of this change on your fraud rate (as some charges that were
previously blocked will now be allowed). Be careful when adjusting the risk
score in this direction.

## See also

- [Risk Evaluation](https://docs.stripe.com/radar/risk-evaluation)
- [Review](https://docs.stripe.com/radar/reviews)
- [Integration Checklist](https://docs.stripe.com/radar/integration)

## Links

- [Radar risk
controls](https://dashboard.stripe.com/settings/radar/risk-controls)
- [risk score](https://docs.stripe.com/radar/risk-evaluation#risk-outcomes)
- [the default block rule](https://docs.stripe.com/radar/rules#built-in-rules)
- [contact us](https://support.stripe.com/contact)
- [Risk Evaluation](https://docs.stripe.com/radar/risk-evaluation)
- [Review](https://docs.stripe.com/radar/reviews)
- [Integration Checklist](https://docs.stripe.com/radar/integration)