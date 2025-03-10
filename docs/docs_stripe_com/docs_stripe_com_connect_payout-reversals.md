# Payout reversals

## Learn how to reverse a payout sent to a connected account.

When the platform is responsible for risk and negative balances, you can make a
[payout](https://docs.stripe.com/payouts) reversal from an external bank account
back to the connected account’s balance.

You can make payout reversals from the Dashboard payout details page or by
calling [reverse payout](https://docs.stripe.com/api/payouts/reverse).

![Reverse payouts in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/reverse_payout_button.cb224dbe2ceae893b5a0ecef855f8f7b.png)

```
curl -X POST https://api.stripe.com/v1/payouts/{{PAYOUT_ID}}/reverse \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

## Requirements

To be reversed, a payout:

- Must be to a bank account in the US.
- Must be expected to arrive less than 90 days ago.
- Can’t be a debit or an [Instant
Payout](https://docs.stripe.com/connect/instant-payouts).

## Webhooks

Payout reversals are considered debits and have the same webhooks as other
payouts. For example, when a payout reversal is first requested, a
`payout.updated` event is sent for the original payout. Then, events for the
payout reversal are sent, including `payout.created`, `payout.updated`,
`payout.paid`, and possibly a `payout.failed` event.

## Failures

If the original payout fails while the payout reversal is in a `pending` state,
Stripe cancels the reversing payout. A payout reversal in the `paid` state can
later be refused by the associated bank and transition to the `failed` state.
This results in a `payout.failed` event. Failed payout reversals aren’t retried.

## Links

- [payout](https://docs.stripe.com/payouts)
- [reverse payout](https://docs.stripe.com/api/payouts/reverse)
- [Instant Payout](https://docs.stripe.com/connect/instant-payouts)