# Capital metricsPrivate preview

## Access financing offer data in the Stripe Dashboard.

The [Capital Dashboard](https://dashboard.stripe.com/connect/capital) helps you
understand the performance of your Capital program. The Dashboard contains key
metrics for originations, conversion, and connected account engagement with
financing offers being delivered, and ways to see the details and state of these
offers.

These metrics refresh nightly and include:

- Topline metrics for pending offers, active offers, in-progress financings and
fully repaid financings where pending offers denote accounts that have potential
offers, but the offers haven’t been created yet
#### Note

These offers might not be able to be created if the user is deny-listed or has
unsubscribed from offers, or if we don’t have a valid email address for the
account.
- Monthly charts with the amount of loans originated, and loan balances repaid
- A daily chart with all time adoption
- A daily chart with 30-day conversion
- A daily chart with the rolling weekly average number of users who are eligible
for Capital including an export option that allows you to download a CSV of
users who are eligible for Capital today
- A daily chart with the rolling weekly average loan size

In the **Financing offers** table, you can view the status of the different
financing offers and active loans.

StatusDefinitionUndeliveredThe financing offer has been created but hasn’t been
marketed to the connected account.DeliveredThe financing offer has been
delivered to the connected account, either by you or by Stripe.AcceptedAn
application for the offer has been submitted and is pending review by Stripe
Servicing.Paid outThe application has passed review and the accepted financing
has been disbursed.RejectedThe application didn’t pass review and has been
rejected by Stripe Servicing.CanceledThe application has been canceled.Fully
repaidThe financing has been fully paid down.ExpiredThe 30-day period has passed
for the connected account to apply for and accept the offer. When the offer is
expired, it’s inaccessible to the user.
## Financing offer details

View a financing offer from the table to get the following information:

- Offered and accepted financing details including terms such as fee and
withholding rate
- Offer creation date
- Remaining balance
- Engagement events for the offer if Stripe delivered the offer email
- Paydown activity

To improve navigation, you can also copy the connected account’s account ID and
financing offer ID, which you can use to filter or search.

## Download data

From the financing offer table, you can export the table’s data as a CSV file.
Click **Export** and select the time zone, date range, and columns you want to
export. If any filters are applied to the financing offer table, these filters
will apply to the resulting data export.

## Capital Data in Sigma

Sigma makes all your transactional data available in an interactive SQL
environment in the Stripe Dashboard. You can find Capital data in three tables
within Sigma:

Table nameTable contentsfinancing_offersThis table contains all information
about the financing offers we have created for merchants on your platform, such
as an offered principal or premium, and the terms for offers that have been
accepted.financing_balancesThis table contains daily balance snapshots for each
paid out loan for connected accounts on your platform. Starting from payout to
being fully paid down, each loan has a daily balance snapshot in the table. You
can see these broken down by the remaining principal and
premium.connected_account_financing_transactionsThis table contains all
financing transactions, such as payouts, paydowns, and reversals, for all
Capital loans for connected accounts on your platform. This information mirrors
what’s available in the Financing Transactions API.
For detailed documentation on how to use Sigma for Capital data, refer to
[Financing
offers](https://dashboard.stripe.com/stripe-schema?tableName=financing_offers)
in the Stripe Data Schema.

## Revshare

Capital revshare is calculated per financing and paid out on a monthly cadence
at the start of the month. It’s categorized as a Stripe fee.

You can check your Capital revshare in two places in the Dashboard:

- The **All activity** section of the [Balances
page](https://dashboard.stripe.com/balance). Use the Dashboard filter **Type:
Stripe fees** to identify the line item with a description that matches
**Revenue Share: Capital**.
- The [Balance Report](https://dashboard.stripe.com/reports/balance). Navigate
to the **Balance change from activity** section and download the file for
**Additional Stripe fees** to identify transactions with a description that
matches **Revenue Share: Capital**.

## Links

- [Capital Dashboard](https://dashboard.stripe.com/connect/capital)
- [Financing
offers](https://dashboard.stripe.com/stripe-schema?tableName=financing_offers)
- [Balances page](https://dashboard.stripe.com/balance)
- [Balance Report](https://dashboard.stripe.com/reports/balance)