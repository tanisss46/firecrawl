# Disputes on Connect platforms

## Learn about the dispute responsibilities on Connect platforms.

## Direct charges

For connected accounts that use [direct
charges](https://docs.stripe.com/connect/direct-charges) and where your platform
isn’t liable for negative balances (including Standard accounts), those accounts
handle their own disputes. The disputed funds are taken from their balance, not
the platform’s.

For connected accounts where your platform is [liable for negative
balances](https://docs.stripe.com/connect/risk-management) (including Custom and
Express accounts), you’re ultimately responsible for any disputes involving
those accounts.

For direct payments on connected accounts where your platform is liable for
negative balances, Stripe debits disputed amounts and fees from the connected
account’s balance. However, your platform is ultimately liable. If Stripe can’t
debit the disputed amount and fee from the connected account, Stripe debits it
from your platform account.

## Destination and separate charges and transfers

For [destination charges](https://docs.stripe.com/connect/destination-charges)
and [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers), with
or without `on_behalf_of`, Stripe debits dispute amounts and fees from your
platform account.

We recommend setting up [a webhook](https://docs.stripe.com/webhooks) to listen
to [dispute created
events](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created).
When that happens, you can attempt to recover funds from the connected account
by reversing the transfer through the
[Dashboard](https://dashboard.stripe.com/test/transfers) or by [creating a
transfer reversal](https://docs.stripe.com/api/transfer_reversals/create).

If the connected account has a negative balance, Stripe attempts to [debit its
external
account](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts)
if `debit_negative_balances` is set to `true`.

If you challenge the dispute and win, you can transfer the funds that you
previously reversed back to the connected account. If your platform has an
insufficient balance, the transfer fails. Prevent insufficient balance errors by
[adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds).

#### Common mistake

Retransferring a previous reversal is subject to [cross-border transfer
restrictions](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border),
meaning you might have no means to repay your connected account. Instead, wait
to recover disputed cross-border payment transfers for destination charges with
`on_behalf_of` until after a dispute is lost.

To automate dispute management and handle chargebacks, browse [Fraud Stripe
Apps](https://marketplace.stripe.com/categories/fraud) on the App Marketplace.

## See also

- [Responding to disputes](https://docs.stripe.com/disputes/responding)
- [Dispute categories](https://docs.stripe.com/disputes/categories)
- [Preventing disputes and fraud](https://docs.stripe.com/disputes/prevention)
- [Using Radar with Connect](https://docs.stripe.com/connect/radar)

## Links

- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [liable for negative
balances](https://docs.stripe.com/connect/risk-management)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [a webhook](https://docs.stripe.com/webhooks)
- [dispute created
events](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created)
- [Dashboard](https://dashboard.stripe.com/test/transfers)
- [creating a transfer
reversal](https://docs.stripe.com/api/transfer_reversals/create)
- [debit its external
account](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts)
- [adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds)
- [cross-border transfer
restrictions](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border)
- [Fraud Stripe Apps](https://marketplace.stripe.com/categories/fraud)
- [Responding to disputes](https://docs.stripe.com/disputes/responding)
- [Dispute categories](https://docs.stripe.com/disputes/categories)
- [Preventing disputes and fraud](https://docs.stripe.com/disputes/prevention)
- [Using Radar with Connect](https://docs.stripe.com/connect/radar)