# Write queries

## Use Sigma to compose custom queries in standard ANSI SQL.

Anyone on your account with [permission to view
reports](https://support.stripe.com/questions/can-i-invite-other-team-members-or-my-developer-to-use-my-stripe-account)
can use the [Sigma query editor](https://dashboard.stripe.com/sigma/queries) to
compose new or modify existing queries. Our large language model (LLM)-based
query assistant can even help you generate the SQL you need from a natural
language prompt.

## Query resources

The navigator window to the left of the editor provides a set of tools to help
you build your query. You can see:

- Your previously saved queries.
- Queries saved by your team.
- The table schema to search for data sources.
- Stripe query templates.

### Saved queries and templates

**Reports > Saved** shows the lists of queries previously saved by you and your
team. **Templates** provides a set of example queries representing the most
common metrics and reports. Selecting a saved query or template loads it into
the query editor, where you can click **Run** to regenerate and view the
results.

To use a saved query as a starting point for your own custom report, either
click its overflow menu () and choose **Make a copy** or load it into the editor
and click **Make a copy**. This lets you modify the content in the editor and
[save](https://docs.stripe.com/stripe-data/write-queries#saving-queries) your
changes as a new query.

## Compose a query

When you open the query editor, you can:

- Write standard ANSI SQL directly into the editor.
- Choose an existing query from your previously saved queries or Stripe’s
templates and modify it in the editor to fine-tune the returned data.

The following query uses the `balance_transactions` table to get information
about the five most recent balance transactions related to refunds:

```
select
 date_format(created, '%Y-%m-%d') as day,
 id,
 amount,
 currency,
 source_id
from balance_transactions
where type = 'refund'
order by day desc
limit 5
```

Click **Run** to execute the query and view the results in a table below the
editor. More complex queries might take a few moments longer to complete and
display results. Attempting to run an invalid query generates an error message
that contains the line number and position of the error.

The results of our sample query returns five rows, where each row corresponds to
a particular balance transaction item, along with the requested information
about them.

dayidamountcurrencysource_id3/9/2025txn_qV0EfvLsbxO5oqA-1,000usdre_ybSklKmkKqE5mNd3/9/2025txn_Qt8gHJMtcZQ7p90-1,000usdre_j6S6DyZgyscdAkT3/9/2025txn_wRmklkB75OqhGNW-1,000usdre_b4c3etfBHLgjNQZ3/9/2025txn_tHWSbDfpCJuPtyq-1,000eurre_ayyRg3zE7xj65VK3/9/2025txn_HfQ5OXReeeWujoj-1,000usdre_NIZ45QgfRrY2Y2t
### Join tables

You can join columns of type **Primary key** or **Foreign key** to similar
columns in other tables:

- **Primary key**: Represents the unique identifier (ID) for each record in a
table.
- **Foreign key**: Represents data that refers to the primary key of another
table.

For instance, you can join the `charge_id` column of the `disputes` table (a
foreign key) to the `id` column of the `charges` table (a primary key).

!

Joining tables allows you to return richer results in your datasets. For
example, you can modify our balance transaction example to join with the
`refunds` table to provide further information.

```
select
date_format(date_trunc('day', balance_transactions.created), '%Y-%m-%d') as day,
 balance_transactions.amount,
 balance_transactions.currency,
 balance_transactions.source_id,
 refunds.charge_id
from
 balance_transactions
inner join refunds -- Joining these tables to retrieve additional information
on balance_transactions.source_id=refunds.id
where balance_transactions.type = 'refund'
order by day desc
limit 5
```

This extended query now returns the original charge ID that the refund relates
to.

dayamountcurrencysource_idcharge.id3/9/2025-1,000usdre_KNnd3Yii1RjABnTch_HFwqTQJUmbmOocZ3/9/2025-1,000usdre_MaTQ3Lh9CZChPFzch_5sIcG7nKbHoEcNI3/9/2025-1,000usdre_Kv8OVTs4ct04JB3ch_URr5Dznf44s3IwW3/9/2025-1,000eurre_tzjNctbm8MzRAoOch_Vu7EOC8bgXhb6fe3/9/2025-1,000usdre_ntd7uV6HB3FPbNoch_rJRScCBn1cJ7OfX
## Use the assistant

Stripe’s query editor has a built-in LLM assistant that outputs standard ANSI
SQL from a natural language prompt. The editor can perform the following modes:

- **Generate** uses the prompt question to write a new query, overwriting any
SQL that’s already loaded in the editor window.
- **Edit** uses the prompt question to modify the SQL in the query editor.

#### Check your mode

For the most accurate suggestion, make sure you select the right mode for your
prompt. When the editor contains content, the mode automatically switches to
**Edit**. If you then decide to prompt for a new query without changing the
mode, the resulting suggestion might be unexpectedly constrained based on what’s
already in the editor.

### Prompt the assistant

- Open the [Sigma query editor](https://dashboard.stripe.com/sigma/queries) in
the Dashboard.
- Select the **Generate** mode and enter a question in the prompt field. The
assistant:

- Loads the query suggestion into the editor.
- Displays a summary describing the suggestion.
- Runs the suggested query and returns the results in a table below the editor.
- Switches the mode to **Edit** so you can ask another question to fine-tune the
query as needed.
- Continue to prompt the assistant and view the resulting data until you get the
information you want.

The following screenshot demonstrates how a prompt generated the same SQL as the
example query shown at the beginning of this document:

![Demonstrates prompting the assistant and the
results.](https://b.stripecdn.com/docs-statics-srv/assets/sigma-assistant.5f0ca3dae331a32c4c58cf6ceecdbf65.png)

Additional questions to modify the suggestions might include:

- Sort these results by amount.
- Don’t include the automatic_transfer or reporting_category columns.
- Can I see the customer for each transaction?

#### Explicitly request Connect data

When asking for data about connected accounts, explicitly mention connected
accounts in your query. For example: *How many new subscriptions did I have from
connected accounts last month?*

### View chat history

Sigma saves every interaction you have with the assistant in the chat history
for that query. Click the button in the top-right of the editor to open the chat
history slider.

Within the chat history, you can see each prompt given to the assistant for the
life of the query (not just the current session) and the assistant’s response.
Click **View SQL** to see the SQL suggestion associated with any prompt. When
open, click **View in editor** to reload that suggestion into the main editor
window.

### Limitations

- The query editor assistant responds only to questions in .
- The query editor assistant only answers questions relative to the Stripe
schema. It can’t answer general questions, such as *What color is Stripe’s
logo?* or *What is the weather in San Francisco today?*

### Leave feedback

Help us continue to improve the assistant by responding to the **Was this
response helpful?** prompt between the editor and the results table:

- Click **Yes** or **No**.
- Enter specific details about how the assistant performed for you and what we
can do to improve. We welcome all opinions, whether it’s about the accuracy of
the suggestion, the UI, or any other aspect of your experience with the
assistant.

### Training data consent

By using Sigma Assistant you agree that Stripe may log and use your chat entries
to train and improve the Sigma Assistant capabilities. If you don’t want to have
your chat entries used for this purpose, you can opt-out in your
[settings](https://dashboard.stripe.com/settings/sigma).

## View and download query results

Query results display in a table below the editor. You can:

- View a maximum of 1,000 results.
- Sort the results by clicking the column headers.
- Resize each column to make it easier to read the results.

You can also create a chart visualization for queries with fewer than 10,000
results. You can:

- Create line or bar charts with custom y-axes and x-axes.
- Group by any table column

When you save a chart to a query, the chart appears with your chosen settings
every time you run the query. Charts are only editable by the author of the
query.

Amounts express in the lowest available currency unit, such as cents for USD or
yen for JPY. For example, an amount of `1,000` with a currency of `usd` equates
to 10 USD.

Click **Download CSV** to export your results for use in spreadsheet
applications or other reporting tools. The downloaded CSV includes all query
results, so you’re not limited to the 1,000 viewable results.

## Save queries

After you run a query, click **Save**. Stripe automatically generates an
editable title for your query.

### Share queries

The queries you save are added to **Reports > Saved** and made available to
every team member on your account. Each saved query is given a unique URL you
can share by clicking **Share**. You can use this link as a shortcut to a
particular report you regularly use, or share it directly with other team
members on the Stripe account.

You can only share queries with team members. Shared queries are read-only, so
other team members can’t modify the queries you create. If a team member wants
to make changes to your query, they can make a copy and edit it accordingly.

## Links

- [permission to view
reports](https://support.stripe.com/questions/can-i-invite-other-team-members-or-my-developer-to-use-my-stripe-account)
- [Sigma query editor](https://dashboard.stripe.com/sigma/queries)
- [settings](https://dashboard.stripe.com/settings/sigma)
- [schedule your queries](https://docs.stripe.com/stripe-data/schedule-queries)
- [webhook](https://docs.stripe.com/webhooks)