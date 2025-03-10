# Schedule queries

## Learn how to schedule queries in Sigma that run on a recurring basis.

You can automate your Sigma queries by scheduling them to run on a daily,
weekly, or monthly basis. Results for each scheduled query are sent with an
[email](https://docs.stripe.com/stripe-data/schedule-queries#subscribers) to
specified team members or as [webhook
events](https://docs.stripe.com/stripe-data/schedule-queries#receiving-results-as-webhooks).

## Scheduling a query

With a query loaded into the editor, click **Schedule**. We recommend you
uniquely name all your scheduled queries to avoid confusion. If your query
doesn’t already have a name (or you wish to modify it), you can update it during
the scheduling process.

!

### Schedule

Each scheduled query can be run on a daily, weekly, or monthly basis. Queries
run as soon as the data for that period is available.

ScheduleDescriptionDailyQueries run as soon as the data for each day (ending at
12:00am UTC) is processed. Query results for the previous day are usually
available by 2pm UTC.WeeklyQueries run every week as soon as the data for the
previous week (ending on Sunday at 12:00am UTC) is processed. Query results for
the previous week are usually available by 2pm UTC the following
Monday.MonthlyQueries run every month as soon as the data for the previous month
(ending at 12:00am UTC) is processed. Query results for the previous month are
usually available by 2pm UTC on the 1st of the month.
## Subscribers

Creators of scheduled queries are added as subscribers to email notifications by
default. To notify other [team
members](https://docs.stripe.com/get-started/account/teams) as well, enter their
email addresses. Results sent with an email include the name and date of the
scheduled query, and a link to download the results in CSV format. To preview
what the email looks like, click **Preview email**.

You or your team members can stop receiving notifications at any time by
clicking the **Unsubscribe** link in the email. You can also edit the scheduled
query in the Dashboard and add or remove subscribers.

### Timeline

Based upon your chosen schedule, the timeline displays the date your query runs
next, and the processing date of the data it uses (additional time is required
to make your account data available to query).

Managing scheduled queries Upcoming scheduled queries are displayed under
**Scheduled** within the **Queries** tab. Schedules are grouped based on whether
they were created by you or other members of your team.

To edit a scheduled query, select it and click **Edit schedule**. To delete it,
click **—** and select **Delete**.

### Receiving results as webhooks

If you make use of [webhooks](https://docs.stripe.com/webhooks), you can receive
notifications for scheduled queries as webhook events. For example, Stripe sends
the `sigma.scheduled_query_run.created` event each time a scheduled query is
run. See below for a sample event.

The `data.object.file.url` subfield of the webhook payload contains the URL
where you can access the results file **using your live secret API key**. For
example, if your server received the webhook below, it could download the
results using this `curl` command:

```
curl https://files.stripe.com/v1/files/{{ FILE ID }}/contents -u
sk_live_XXXXXXX:
```

For more on how to integrate webhooks, see our [webhook
documentation](https://docs.stripe.com/webhooks).

```
// Sample payload of a sigma.scheduled_query_run.created webhook

{
 "object": "event",
 "pending_webhooks": 2,
 "created": 1504794194,
 "type": "sigma.scheduled_query_run.created",
 "livemode": true,
 "request": null,
 "data": {
 "object": {
 "id": "sqr_",
 "object": "scheduled_query_run",
 "status": "completed",
 "data_load_time": 1504656000,
 "file": {
 "id": "{{ FILE ID }}",
 "object": "file",
 "url": "https://files.stripe.com/v1/files/{{ FILE ID }}/contents",
 "created": 1507841188,
 "purpose": "sigma_scheduled_query",
 "size": 53075,
 "type": "csv"
 },
 "title": "Scheduled Query Example",
 "sql": "SELECT count(*) FROM charges WHERE created >= date('2017-01-01')",
 "created": 1504794194,
 "result_available_until": 1505398933,
 "error": null,
 "livemode": true
 }
 }
}
```

## Links

- [team members](https://docs.stripe.com/get-started/account/teams)
- [webhooks](https://docs.stripe.com/webhooks)