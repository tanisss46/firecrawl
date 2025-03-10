# App analytics

## Access analytics to see how your app performs.

App analytics enables you to better understand how your apps are used and how
your marketplace listings perform. You can export data, such as the number of
installs and listing views, for your public app. This data is available in
Dashboard or the Stripe API.

The Dashboard provides additional tools to help you understand your app’s
performance, such as:

- Single-number summaries for the currently selected period- Rate-based reports
(%): Average for the selected period
- Non-rate-based reports: Sum for the selected period
- Badges that summarize the current period with the previous period (if
sufficient historical data is available)
- Aggregation using a resolution based on your selected date range- To download
higher-resolution data, click **Download CSV**.

![App analytics all charts
dashboard](https://b.stripecdn.com/docs-statics-srv/assets/analytics-overview.646194fb349cbe6ef00b6bdbb83010d4.png)

## Get started

- From the **Developer’s Dashboard > Apps**, select your app.
- Click the **Users** tab, then click **Export app analytics**.
- Choose the report to export and select your preferred date range.

## Available reports

The following reports are available to export as a CSV.

NameDescriptionReport typeApp installsInstalls per day`apps.install_events.1`App
uninstallsUninstalls per day`apps.uninstall_events.1`Cumulative net
installsInstalls to date (`installs - uninstalls`)`apps.total_installs.1`Listing
page viewsTotal daily app listing views`apps.listing_views.1`Unique listing page
viewsTotal unique merchants who have visited your app listing
page`apps.unique_listing_views.1`MoM install conversion rate`# of new installs
in the last 30 days` ÷ `# of leads in the last 30 days` x
`100``apps.lead_conversion_rate.1`MoM listing page views growth rate*(`# of
leads this month` - `# of leads last month`) ÷ `# of leads last month` x
`100``apps.lead_velocity_rate.1`MoM install churn rate`# of uninstalls in the
last 30 days` ÷ `# of active installs 30 days ago` x `100``apps.churn_rate.1`
***MoM listing page views growth rate** might report high values for early data
points. We recommend that you consider data at least 60 days after the first
non-null point.

### Data freshness and definitions

The analytics data lags up to 48 hours before it’s available in reports. If
you’re looking for real-time metrics, you can build your own [custom
analytics](https://docs.stripe.com/stripe-apps/analytics#custom-analytics) using
our platform primitives.

We define “leads” as logged-in merchants who visit the marketplace.

### Accessing using the Stripe API

To access these reports programmatically, you can use the [Reporting
API](https://docs.stripe.com/api/reporting/report_run) to run a report for the
specific metrics you want to fetch. Each of the metrics is available as report
types, which you can request in the following way:

```
curl https://api.stripe.com/v1/reporting/report_runs \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d report_type="apps.install_events.1" \
 -d "parameters[interval_start]"=1680000000 \
 -d "parameters[interval_end]"=1680100000
```

## Users

The **Users** tab in your app’s details page lists all the currently installed
users. If a user reinstalls your app, the `installed` column updates to the most
recent install time.

![App users
tab](https://b.stripecdn.com/docs-statics-srv/assets/users_tab_dashboard.f63737de18de2af888119400fed28007.png)

## Custom analytics

If the provided metrics aren’t sufficient, you can leverage the platform
primitives of Stripe to build your own set of metrics using the following
solutions:

### Using webhooks

Use webhooks to track and respond to users who install or uninstall your app or
extension in real time, where you can get insights about:

- Installed user’s account ID- Date and time of install
- Uninstalled user’s account ID
- Date and time of uninstall
- Stripe app users- [Extension
users](https://docs.stripe.com/stripe-apps/migrate-extension) (if applicable)

For more information, see how to [receive webhook events from your
app](https://docs.stripe.com/stripe-apps/build-backend#receiving-events-webhooks).

### Using Connect List API

Use the Connect List API to return a list of all the users who’ve currently
installed your app and
[extension](https://docs.stripe.com/stripe-apps/migrate-extension) (if
applicable).

For more information, see the [List all connected
accounts](https://docs.stripe.com/api/accounts/list) reference.

## Links

- [Developer’s Dashboard](https://dashboard.stripe.com/developers)
- [Apps](https://dashboard.stripe.com/apps)
- [Reporting API](https://docs.stripe.com/api/reporting/report_run)
- [Extension users](https://docs.stripe.com/stripe-apps/migrate-extension)
- [receive webhook events from your
app](https://docs.stripe.com/stripe-apps/build-backend#receiving-events-webhooks)
- [List all connected accounts](https://docs.stripe.com/api/accounts/list)