# Get real-time updates from Financial Connections with webhooks

## Use webhooks to get notifications about activity on Financial Connections accounts.

After you collect a [Financial Connections
Account](https://docs.stripe.com/api/financial_connections/accounts/object), you
can access account data or listen for account changes with the Financial
Connections API and associated [webhooks](https://docs.stripe.com/webhooks).

Core webhooks notify you of account-level updates and newly created accounts.
These include:

- `financial_connections.account.created`
- `financial_connections.account.deactivated`
- `financial_connections.account.reactivated`

Other webhooks notify you when Stripe completes asynchronous data refreshes for
accounts that your customers have connected.

EventDescription`financial_connections.account.created`Sent when a customer
links a new account. If they link multiple accounts, it emits multiple events
(one per account).`financial_connections.account.deactivated`Sent when the
[status](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-status)
of your user’s account moves from `active` to `inactive`. Accounts can change
status after a
[refresh](https://docs.stripe.com/api/financial_connections/accounts/refresh) if
we detect that the account connection is broken. New data refreshes aren’t
allowed on `inactive` accounts, but previously refreshed data stays available.
`financial_connections.account.reactivated`Sent when the
[status](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-status)
of your user’s account moves from `inactive` to `active`. After an account moves
from `inactive` to `active`, you can refresh account data
again.`financial_connections.account.disconnected`Sent on account disconnection.
See the [disconnections
guide](https://docs.stripe.com/financial-connections/disconnections) for further
detail.`financial_connections.account.refreshed_balance`Sent after a
[balance](https://docs.stripe.com/financial-connections/balances) refresh is
complete.`financial_connections.account.refreshed_ownership`Sent after an
[ownership](https://docs.stripe.com/financial-connections/ownership) refresh is
complete.`financial_connections.account.refreshed_transactions`Sent after a
[transaction](https://docs.stripe.com/financial-connections/transactions)
refresh is complete.
## See also

- [Webhook documentation](https://docs.stripe.com/webhooks)
- [Event object reference](https://docs.stripe.com/api/events)

## Links

- [Financial Connections
Account](https://docs.stripe.com/api/financial_connections/accounts/object)
- [webhooks](https://docs.stripe.com/webhooks)
-
[status](https://docs.stripe.com/api/financial_connections/accounts/object#financial_connections_account_object-status)
- [refresh](https://docs.stripe.com/api/financial_connections/accounts/refresh)
- [disconnections
guide](https://docs.stripe.com/financial-connections/disconnections)
- [balance](https://docs.stripe.com/financial-connections/balances)
- [ownership](https://docs.stripe.com/financial-connections/ownership)
- [transaction](https://docs.stripe.com/financial-connections/transactions)
- [Event object reference](https://docs.stripe.com/api/events)