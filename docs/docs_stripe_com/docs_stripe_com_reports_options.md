# Report filters and settings

## Understand the settings and controls that are common across all financial reports.

This page describes the set of options available on each financial report. These
include filters to select the data to view, including [date
range](https://docs.stripe.com/reports/options#date-range),
[currency](https://docs.stripe.com/reports/options#currency), and [connect
accounts](https://docs.stripe.com/reports/options#connect-accounts).

## Date range

When loading the page, the reports default to displaying data for the prior
month. You can select previous months, current month-to-date, or customize the
date range to specific dates. Selected dates are inclusive. For example, if you
choose a date range of February 7, 2025–February 14, 2025, it includes data from
the beginning of the day on February 7, 2025 (12:00am) through the end of the
day on February 14, 2025 (11:59pm) in the selected time zone.

### Time zone customization

You can view financial reports based on either your Stripe account’s time zone
or Coordinated Universal time (UTC). This selection affects both how the date
range setting filters the report, and how dates and times contained within the
report are presented.

### Data availability

Stripe computes all your data on a daily basis beginning at 12:00am UTC. The
data for each day is defined as account activity that takes place between
12:00am UTC and 11:59pm UTC.

Financial reports tabProcessing timeBalanceWithin 12 hoursPayout
reconciliationWithin 12 hours
#### Caution

SLAs indicate when the reports are available for download. Webhook notifications
might take additional time.

For example, all account activity on February 7, 2025 (from 12:00 am to 11:59 pm
UTC) is available in the **Balance financial reports** tab by February 8, 2025
at 12:00 pm UTC.

Users who view reports in certain non-UTC timezones might experience an
additional day delay. For example, the Balance report for Monday won’t become
available until Wednesday morning when viewed in the America/Los_Angeles
timezone (PST). This is because data is processed by UTC day, and the last few
hours of Monday in PST correspond to Tuesday morning in UTC. As such, the report
can’t be made available until Tuesday’s data has finished processing, which
occurs by Wednesday at 12:00 pm UTC.

## Currency

Financial reports are based on your account’s [settlement
currency](https://docs.stripe.com/connect/payouts-connected-accounts#supported-settlement),
which is the currency Stripe uses to send
[payouts](https://docs.stripe.com/payouts) to your bank.

If your account has multiple settlement currencies, you can view reports for
each currency separately using the currency selector.

## Connect accounts

[Connect](https://docs.stripe.com/connect) platforms often need visibility into
funds and transactions within their connected accounts in addition to their
platform activity. When viewing a report as the platform account, you can toggle
between viewing data:

- For the platform account only
- For all of the platform’s connected accounts (summary reports sum the data
across all connected accounts, while itemized reports include relevant rows for
all connected accounts)
- For a single connected account

To view reporting for a single connected account:

- Go to the [Connect
Accounts](https://dashboard.stripe.com/connect/accounts/overview) page and
search for the account you want.
- Click on the account’s name to go to the account detail page.
- Click the **View financial reports** link under the Reports section.

!

#### Caution

Connect platforms can’t view the financial reports for connected accounts that
can access the full Stripe Dashboard and aren’t [controlled by the
platform](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts).
Holders of such accounts can independently control them if they were created
with Stripe directly. Those accounts can contain transactions that originate
outside of your platform. Because they have access to the full Stripe Dashboard,
they can generate their own financial reports.

## Scheduled reports

To set up a subscription schedule for reports and get notified of new data, read
our [scheduled reports](https://docs.stripe.com/reports/scheduled-reports) docs.

## Links

- [settlement
currency](https://docs.stripe.com/connect/payouts-connected-accounts#supported-settlement)
- [payouts](https://docs.stripe.com/payouts)
- [Connect](https://docs.stripe.com/connect)
- [Connect Accounts](https://dashboard.stripe.com/connect/accounts/overview)
- [controlled by the
platform](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [scheduled reports](https://docs.stripe.com/reports/scheduled-reports)