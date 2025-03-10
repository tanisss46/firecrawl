# Revenue Recognition accounting period control

## Learn how to configure accounting periods for your Revenue Recognition.

Accounting period control allows you to configure how to close accounting
periods. You can either manually close the books with all checks and adjustments
finished each month, or you can let Stripe automate closing the books.

You can also reopen past accounting periods using accounting period control.
This is useful when you first start using Revenue Recognition because it allows
you to make adjustments to past data without creating corrections in the current
period. For example, when you apply
[rules](https://docs.stripe.com/revenue-recognition/rules) to fit Revenue
Recognition with your own business model, it’s likely to change the history of
closed accounting periods. You can decide on whether to reopen the closed
accounting periods or make adjustments in the current accounting period.

## Setting accounting periods

You can find the accounting periods section on [the Revenue Recognition controls
page](https://dashboard.stripe.com/settings/revenue-recognition).

![Accounting periods
controls](https://b.stripecdn.com/docs-statics-srv/assets/accounting_period_controls.64932706c8bd298d267ed8aa9148214f.png)

[Select the mode for accounting
periods](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control#accounting-period-mode)
To get started, select the `mode` for your accounting periods. The default is
`automatic`.

ModeDescriptionsAutomaticAccounting periods automatically close at the end of
each month.ManualYou control when to close the accounting periods.[Choose the
latest closed accounting period in manual
mode](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control#latest-closed-accounting-period)
When you set `latest closed accounting period`, you close the selected
accounting period along with all previous accounting periods, and you open all
following periods. You can choose one of the periods in the past 24 months, and
you can also choose `no closed accounting periods`. For example, when you choose
the `latest closed accounting period` to be February 2021 in `manual` mode, the
accounting periods looks like the following example:

Before Jan 2021Jan 2021Feb 2021Mar 2021Apr 2021May 2021Jun
2021ClosedClosedClosedOpenOpenOpenOpen
## How accounting period control works

**Controlling closing process for your accounting period cycle**

Accounting period control allows you to configure the closing process with your
own workflow for the accounting period cycle. You can choose the `manual` mode,
and check all terms and fix the human errors before closing the accounting
periods manually, or you can automate closing your Revenue Recognition book
using the `automatic` mode.

**Getting started with Revenue Recognition**

If you’re new to Revenue Recognition, use accounting period control to get
started. For example, when you apply
[rules](https://docs.stripe.com/revenue-recognition/rules) to fit Revenue
Recognition with your own business model, you can set `manual` mode with `no
closed accounting periods`. In this way, all the changes go into the original
accounting periods, which can help you understand your books.

You can open accounting periods after setting [revenue recognition
rules](https://docs.stripe.com/revenue-recognition/rules), unless you need to
issue corrections. In that case, you must close the accounting period before
setting any rules.

Adjustments for accounting periods take up to 24 hours to complete. When
completed, you can see the setting in monthly summary charts and CSV-only
reports in the Dashboard. For example, when you choose the `latest closed
accounting period` to be February 2021 in `manual` mode, the charts and reports
look like the following example:

![Revenue chart with manual mode and latest closed accounting period as February
2021](https://b.stripecdn.com/docs-statics-srv/assets/accounting-period-control-revenue-chart.d6ab06169fb7d15f27f2e7cfe5a2282e.png)

![Income statement report with manual mode and latest closed accounting period
as February
2021](https://b.stripecdn.com/docs-statics-srv/assets/accounting-period-control-income-statement-report.da2f6a5fb6491e4e4da58c115c7089f7.png)

## Links

- [rules](https://docs.stripe.com/revenue-recognition/rules)
- [the Revenue Recognition controls
page](https://dashboard.stripe.com/settings/revenue-recognition)