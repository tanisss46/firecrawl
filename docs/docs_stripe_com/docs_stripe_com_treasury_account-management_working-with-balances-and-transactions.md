# Working with balances and transactions

## Learn about Treasury account balances and the effect transactions have on them.

[Financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
have their own balance separate from the balance of the account they’re attached
to (platform account or connected account). `Balance` objects record the amount
of funds in a financial account and their state of availability. `Transaction`
and `TransactionEntry` objects debit or credit the funds in that balance.

## Balances

A financial account has a balance of funds. The sum total of the balance isn’t
always available for spending, however, as it might include pending transactions
into or out of the financial account. The financial account balance contains
three properties that define the availability of its funds:

- `cash`—funds the user can spend right now.
- `inbound_pending`—funds not spendable yet, but that will become available at a
later time. The `inbound_pending` property is reserved for future functionality
and always has a value of 0.
- `outbound_pending`—funds in the account, but not spendable because they’re
being held for pending outbound flows.

Use `GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}` to retrieve
the balance details of a financial account with the associated ID. Provide the
`Stripe-Account` header if the financial account is attached to one of your
connected accounts. If the financial account is attached to your platform
account, don’t include the `Stripe-Account` header.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response is a
[FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts)
object with a `balance` hash that details the funds and their availability.

```
{
 "object": "treasury.financial_account",
 "id": "{{FINANCIAL_ACCOUNT_ID}}",
 ...
 "balance": {
 // $90 is currently available for use,
 // with an additional $10 held in the outbound_pending sub-balance
 "cash": {"usd": 9000},
 "inbound_pending": {"usd": 0},
 "outbound_pending": {"usd": 1000}
 }
}
```

### Negative balances and overdrafts

If your connected account has a negative balance (for example, if your financial
account receives an ACH credit that gets reversed), you’re responsible for
restoring it to 0 USD. After 180 days of staying negative, Stripe debits your
platform. We also contact you if individual or aggregate balances exceed our
risk limits.

We recommend that you monitor your connected accounts to retrieve funds for
their negative balances. You can top up funds into your financial account using
[Inbound
Transfers](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
or [Stripe Payouts](https://docs.stripe.com/treasury/moving-money/payouts). Make
sure that you regularly monitor your connected account balances and reach out
promptly.

After a financial account has been negative for 180 days, Stripe debits funds
from your platform’s financial account and emails you ahead of time. If the
transfer fails due to insufficient funds, Stripe contacts you with next steps.

## Transactions

All changes to a balance have a corresponding
[Transaction](https://docs.stripe.com/api/treasury/transactions) object that
details money movements. Transactions affect only one balance and are in only
one currency (currently, Stripe Treasury supports only USD).

Each transaction points to the balance-affecting money movement object, such as
an [OutboundTransfer](https://docs.stripe.com/api/treasury/outbound_transfers),
[ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits), or
[ReceivedDebit](https://docs.stripe.com/api/treasury/received_debits).

### Transaction state machine

StatusState appliedDescriptionTransitions to`open`initialThis is the initial
state for all transactions. The transaction results in updates to the
sub-balance amounts, but the current balance isn’t affected until the
transaction posts.`posted` or `void``posted`terminalFunds have successfully
entered or left the account. The current balance was
affected.N/A`void`terminalThe transaction never impacted the balance. For
example, a transaction enters this state if an outbound payment was initiated
but then canceled before the funds left the account.N/A
The available `Transaction` endpoints enable you to retrieve specific
transactions and list or filter transactions affecting a financial account.
There are no webhooks available for transactions, but webhooks are available for
the associated money movement objects (for example, `OutboundPayments`).

## Retrieve a transaction

Use `GET/v1/treasury/transactions/{{TRANSACTION_ID}}` to retrieve the
transaction with the associated ID.

```
curl https://api.stripe.com/v1/treasury/transactions/txn_123 \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response returns the `Transaction` object.

```
{
 "id": "{{TRANSACTION_ID}}",
 "object": "treasury.transaction",
 "created": "{{Timestamp}}",
 "livemode": false,
 // The FinancialAccount this Transaction impacts
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // The flow responsible for this Transaction. Each Transaction is created
 // synchronously (that is, in the same API request for initiated objects) with
 // its flow.
```

See all 75 lines
### List Transactions

Use `GET /v1/treasury/transactions` to list transactions for a financial
account. Set the required `financial_account` parameter in the body to the value
of the financial account ID to retrieve transactions for. Include additional
parameters to filter the results returned.

In addition to the [standard set of list
parameters](https://docs.stripe.com/api/pagination), you can filter transactions
by the following.

- `status`
- `flow`
- Either `created` or `posted_at`, but not both

```
{
 // Standard list parameters
 limit, starting_after, ending_before,
 // Filter by FinancialAccount, required
 financial_account: "{{FINANCIAL_ACCOUNT_ID}}"
 // Filter by status
 status: "open" | "posted" | "void",
 // Filter by flow
 flow: "{{FLOW_OBJECT_ID}}",
// Order the results by the created or posted_at timestamps, default is
`created`.
 // For order_by=posted_at, setting status='posted' is required
 order_by: "created" | "posted_at",
 // created can only be specified with order_by = 'created'
 created: {gt, gte, lt, lte},
 status_transitions: {
// status_transitions.posted_at can only be specified with order_by =
'posted_at' and status = 'posted'
 posted_at: {gt, gte, lt, lte}
 }
}

```

The following request retrieves the three most recent transactions created on
the financial account that have a `status` of `posted`.

```
curl -G https://api.stripe.com/v1/treasury/transactions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d limit=3 \
 -d status=posted \
 -d order_by=created
```

### Webhooks

There are no webhooks for transactions because the various money movements that
initiate a transaction have their own webhooks.

## Transaction entries

[TransactionEntry](https://docs.stripe.com/api/treasury/transaction_entries)
objects are the most granular view of money movements that affect a financial
account balance. A single flow of money comprises multiple individual money
movements, each represented by a transaction. Transactions, in turn, are an
aggregation of transaction entries. For example, when initiating an outbound
payment of 10 USD at time T, funds are moved from the `cash` sub-balance to the
`outbound_pending` sub-balance. The following `Transaction` object response
demonstrates this initial event.

```
{
 "id": "{{TRANSACTION_ID}}",
 "object": "treasury.transaction",
 "created": "{{T}}",
 ...
 "flow": "{{OUTBOUND_PAYMENT_ID}}",
 "flow_type": "outbound_payment",
 "status": "open",
 "amount": -1000,
 "currency": "usd",
```

See all 36 lines
After the outbound payment posts at time T+1, the funds are deducted from
`outbound_pending` and a new transaction entry is added to the transaction. The
following `Transaction` response demonstrates this progression.

```
{
 "id": "{{TRANSACTION_ID}}",
 "object": "treasury.transaction",
 "created": "{{T}}",
 ...
 "flow": "{{OUTBOUND_PAYMENT_ID}}",
 "flow_type": "outbound_payment",
 "status": "posted",
 "amount": -1000,
 "currency": "usd",
```

See all 49 lines
As the preceding responses show, a transaction can contain multiple transaction
entries. The available `TransactionEntry` endpoints enable you to retrieve
specific transaction entries and list or filter them for a particular
transaction.

A `Transaction` in the `void` status won’t have any new transaction entries
added to it. A `Transaction` in the `posted` status where all `balance_impact`
is to the `cash` sub-balance won’t have any new transaction entries added to it,
either.

### Retrieve transaction entries

Use `GET /v1/treasury/transaction_entries/{{TRANSACTIONENTRY_ID}}` to retrieve
details for the transaction entry with the associated ID.

```
curl
https://api.stripe.com/v1/treasury/transaction_entries/{{TRANSACTION_ENTRY_ID}}
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response returns a `TransactionEntry` object with the
following form.

```
{
 "id": "{{TRANSACTION_ENTRY_ID}}",
 "object": "treasury.transaction_entry",
 "created": "{{Timestamp}}",
 "livemode": false,
 // The FinancialAccount this transaction entry impacts.
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // The transaction that this transaction entry belongs to.
 "transaction": "{{TRANSACTION_ID}}",
 // The flow responsible for this transaction entry.
```

See all 56 lines
### List TransactionEntries

Use `GET /v1/treasury/transaction_entries` to list the transaction entries for a
financial account. Set the required `financial_account` parameter in the body to
the value of the financial account ID to retrieve transaction entries for.
Include additional parameters if you want to filter the list.

In addition to the [standard set of list
parameters](https://docs.stripe.com/api/pagination), you can filter transaction
entries by:

- `transaction`
- Either `created` or `effective_at`, but not both

```
{
 // Standard list parameters
 limit, starting_after, ending_before,
 // Filter by FinancialAccount, required
 financial_account: "fa_123"
 // Filter by transaction
 transaction: 'trxn_123',
// Order the results by the created or effective_at timestamps, default is
`created`.
 order_by: "created" | "effective_at",
 // created can only be specified with order_by = 'created'
 created: {gt, gte, lt, lte},
 // effective_at can only be specified with order_by = 'effective_at'
 effective_at: {gt, gte, lt, lte},
}

```

The following request retrieves the transaction entries created before
`{{Timestamp}}` and orders them by `created` date.

```
curl -G https://api.stripe.com/v1/treasury/transaction_entries \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d order_by=created \
 -d "created[lt]"=1234567890
```

### Webhooks

There are no webhooks for transaction entries because the various money
movements that initiate a transaction entry have their own webhooks.

## Links

- [Financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts)
- [Inbound
Transfers](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
- [Stripe Payouts](https://docs.stripe.com/treasury/moving-money/payouts)
- [Transaction](https://docs.stripe.com/api/treasury/transactions)
- [OutboundTransfer](https://docs.stripe.com/api/treasury/outbound_transfers)
- [ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits)
- [ReceivedDebit](https://docs.stripe.com/api/treasury/received_debits)
- [standard set of list parameters](https://docs.stripe.com/api/pagination)
- [TransactionEntry](https://docs.stripe.com/api/treasury/transaction_entries)