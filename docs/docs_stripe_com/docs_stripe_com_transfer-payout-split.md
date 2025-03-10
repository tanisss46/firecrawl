# Transfer Payout Split: Stripe-Version 2017-04-06

On April 6, 2017, Stripe split the `/v1/transfers` resource into `/v1/transfers`
and `/v1/payouts`. This is a versioned change–your existing integrations don’t
need to change.

Since Stripe was launched, we’ve used the word **transfer** to mean moving money
out of Stripe and into your bank account or debit card. But when
[Connect](https://docs.stripe.com/connect) was launched years later, we co-opted
that term to also mean moving money between a platform and its connected
accounts.

This ultimately turned out to be confusing. These are conceptually different
flows of funds as they apply to a business. This made it difficult to document
transfers, and also bloated the `/v1/transfers` API because the fields needed to
support each flow of funds were different.

As of Stripe-Version `2017-04-06`:

- **Payouts** will mean moving money from Stripe to your bank account or debit
card and will be represented by `/v1/payouts`.
- **Transfers** will mean moving money between Stripe accounts as part of
Connect and will be represented by `/v1/transfers`.
- Relative to the legacy `/v1/transfers` resource, the new `/v1/transfers`
resource won’t have these fields:- `method` - this only applies to
[payouts](https://docs.stripe.com/payouts).
- `status` - this only applies to payouts.
- `type` - this only applies to payouts.
- `bank_account` - this only applies to payouts.
- `card` - this only applies to payouts.
- `failure_message` - this only applies to payouts.
- `failure_code` - this only applies to payouts.
- `description` - description was confusing because it applied to the transfer
but not the resultant payment on the connected account. Use `metadata` to attach
additional information to a transfer.
- `application_fee` - application_fee is no longer necessary. See [Connect
destination charges](https://docs.stripe.com/connect/destination-charges).
- Relative to the legacy `/v1/transfers`, the new `/v1/payouts` resource won’t
have these fields:- `reversals` - payouts can now be simply canceled.
- `reversed` - refer to the payout status.
- `application_fee` - this only applies to legacy transfers.
- `destination_payment` - this only applies to transfers.
- `source_transaction` - this only applies to legacy transfers.
- `description` - description was removed because it didn’t provide enough
value. Use metadata to attach additional information to a payout.
- On the `/v1/payouts` resource, the `date` field was renamed to `arrival_date`.
- To send a payout to your default bank account or debit card, instead of
including the parameter `destination=default_for_currency`, simply omit the
`destination` entirely.
- Canceling a payout is now done via `POST /v1/payouts/:id/cancel`. The balance
transaction resulting from a cancellation is available via the
`cancellation_balance_transaction` field on the payout. The `status` of a
canceled payout is `canceled`.
- When creating a transfer, you can now only use a charge as the
`source_transaction`. Previously, it was possible to use any transaction (such
as an application fee, or an adjustment) as a `source_transaction`. This did not
mesh well with the intended use case of tagging outgoing transfers with the
incoming source of funds, so this is no longer supported on the new API version.
- Payouts now generate these events: `payout.created`, `payout.failed`,
`payout.reversed`, `payout.paid`, `payout.updated`, which are the equivalent of
the legacy `transfer.*` events.
- Transfers no longer generate these events: `transfer.paid` and
`transfer.failed`.
- Balance transactions can have these types as they relate to payouts: `type` ∈
{`payout`, `payout_failure`, `payout_cancel`}
- Balance transactions can have these types as they relate to transfers: `type`
∈ {`transfer`, `transfer_refund`}
- Fields on the [Account API](https://docs.stripe.com/api/accounts) were
renamed:- `transfers_enabled` → `payouts_enabled`
- `transfer_schedule` → `payout_schedule`
- `transfer_statement_descriptor` → `payout_statement_descriptor`
- Transfers to the deprecated Recipients API are no longer represented on this
version of the API. Use a legacy API version to access any transfers to
recipients that you may have.

## Links

- [Connect](https://docs.stripe.com/connect)
- [payouts](https://docs.stripe.com/payouts)
- [Connect destination
charges](https://docs.stripe.com/connect/destination-charges)
- [Account API](https://docs.stripe.com/api/accounts)