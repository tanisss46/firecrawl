# Reporting chartPrivate preview

## Show charts to your connected accounts.

Reporting chart renders a UI component for connected accounts to view charts
similar to those on the Stripe Dashboard, such as the Net Volume and Gross
Volume charts.

SizeDesktopLocale (United States)This demo is read-only. Write operations
(like performing a refund or saving account information) are not supported for
this demo.
## Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable Reporting
chart by specifying `reporting_chart` in the `components` parameter.

#### Note

The Reporting chart component is in private preview, so the Stripe SDKs don’t
include it yet. To enable it when creating an account session, use this code
snippet with the Stripe beta SDK:

```
Stripe.api_key = '{{sk_INSERT_YOUR_SECRET_KEY}}'
Stripe.api_version = '2023-10-16; embedded_connect_beta=v2;'
account_session = Stripe::AccountSession.create({
 account: '{{CONNECTED_ACCOUNT_ID}}',
 components: {
 reporting_chart: {enabled: true}
 }
})
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Reporting chart component in the frontend:

## Render the component

```
// Include this element in your HTML
const container = document.getElementById("container");
const reportingChart = stripeConnectInstance.create("reporting-chart");
reportingChart.setReportName("net_volume");
reportingChart.setIntervalStart(new Date(2023, 11, 17));
reportingChart.setIntervalEnd(new Date(2024, 08, 18));
reportingChart.setIntervalType("day");
container.appendChild(reportingChart);
```

HTML + JSReactMethodTypeDescriptionDefaultRequired or
Optional`setReportName``'net_volume' | 'gross_volume'`The name of the report to
render as a chart.required`setIntervalStart``Date`The start time to query data.
Returned data might start later than this timestamp if data is sparse.The time
of the connected account’s first data point for the report
specified.optional`setIntervalEnd``Date`The end time to query data. Returned
data might end earlier than this timestamp if data is sparse.The time of the
connected account’s last data point for the report
specified.optional`setIntervalType``'day' | 'month' | 'quarter' | 'year'`Used to
determine granularity of the data.Based on the duration between `intervalStart`
and `intervalEnd`. A longer time frame defaults to showing less granular
data.optional
## Request access Private preview

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Freporting-chart)
to request access to this Connect embedded component in private preview.

If you don’t have a Stripe account, you can [register
here](https://dashboard.stripe.com/register).

## Links

- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Freporting-chart)
- [register here](https://dashboard.stripe.com/register)