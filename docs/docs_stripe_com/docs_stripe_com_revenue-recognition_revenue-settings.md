# Revenue Recognition settings

## Learn how to adjust the behavior of Revenue Recognition with settings.

Access the Revenue Recognition settings on the [settings
page](https://dashboard.stripe.com/settings/revenue-recognition) to customize
how revenue is recognized specifically for your business.

When completed, all Revenue Recognition charts and reports reflect the settings
within 24 hours.

## Accounting period

Use accounting period control to configure how to close accounting periods. You
can either manually close the books with all checks and adjustments finished
each month, or you can let Stripe automate closing the books.

You can also reopen past accounting periods using accounting period control.
This is useful when you first start using Revenue Recognition because it allows
you to make adjustments to past data without creating corrections in the current
period. For example, when you apply
[rules](https://docs.stripe.com/revenue-recognition/rules) to fit Revenue
Recognition with your own business model, it changes the history of closed
accounting periods. You can decide to reopen closed accounting periods or make
adjustments in the current accounting period.

## Amortization granularity

Amortization refers to the process of gradually recognizing revenue over the
duration of a service period. By default, Revenue Recognition recognizes revenue
by the millisecond. We also support recognizing revenue by the day, or by the
month with different treatment options for handling the first and last months of
the service period.

AmortizationDescriptionsBy millisecond (default)Recognize revenue down to the
millisecond.By dayRecognize revenue down to the day. Cut off the last day.By
month evenlyRecognize revenue down to the month. Cut off the last month.By month
evenly, first and last month proratedRecognize revenue down to the month.
Prorate the amounts in the first and last months by millisecond.
Adjusting this configuration affects all of your journal entries within Revenue
Recognition. If you want to avoid creating corrections in the current period, we
recommend that you [open all accounting
periods](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)
prior to the adjustment.

## Catch-up revenue

Revenue Recognition primarily recognizes revenue based on the service period
attached to transactions. However, when the service period begins before the
booked date (the finalization date for an invoice, the creation date or imported
booked date for a standalone charge), the revenue from the prior periods is
instead recognized entirely in the month of the booked date to avoid making
changes to the past. We refer to this type of revenue as *catch-up* revenue.

To disable or enable this behavior, toggle **Apply catch-up revenue**.

Toggling this configuration affects any applicable journal entries you have
within Revenue Recognition. If you want to avoid creating corrections in the
current period, we recommend that you [open all accounting
periods](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)
prior to the adjustment.

## See also

-
[Examples](https://docs.stripe.com/revenue-recognition/revenue-settings/examples)

## Links

- [settings page](https://dashboard.stripe.com/settings/revenue-recognition)
- [rules](https://docs.stripe.com/revenue-recognition/rules)
- [open all accounting
periods](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)
-
[Examples](https://docs.stripe.com/revenue-recognition/revenue-settings/examples)