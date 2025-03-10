# Controlling bank and debit card transfers

## Stripe allows platforms to entirely control the transfers for its Custom Connect accounts.

#### Caution

This page describes an older version of
[Connect](https://docs.stripe.com/connect). In the latest version of Connect,
the legacy `transfers` endpoint has been deprecated in favor of `payouts`. The
Dashboard’s user interface reflects this change, using the term
“[payouts](https://docs.stripe.com/payouts)” instead of transfers, regardless of
your Stripe API version. Refer to [bank and debit card
payouts](https://docs.stripe.com/connect/payouts-connected-accounts) for
information about the latest version of the Connect API.

By default, any charge you make on behalf of a connected account accumulates in
the connected account’s [Stripe
balance](https://docs.stripe.com/connect/account-balances) and is paid out on a
daily rolling basis. However, Stripe offers fine-grained control over this
behavior for Custom accounts.

You can:

- Set the destination [bank accounts and debit
cards](https://docs.stripe.com/connect/legacy-transfers#bank-accounts)
- Control [how
frequently](https://docs.stripe.com/connect/legacy-transfers#payout-information)
funds are automatically paid out
- Perform [manual
transfers](https://docs.stripe.com/connect/legacy-transfers#using-manual-transfers)
- Send funds
[instantly](https://docs.stripe.com/connect/legacy-transfers#instant-payouts)

## Managing bank accounts and debit cards

Custom accounts have an `external_accounts` property: a list of all bank
accounts and debit cards associated with the Stripe account. Any external
account is a possible destination for funds.

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "external_accounts": {
 "object": "list",
 "has_more": false,
 "url": "/v1/accounts/acct_14qyt6Alijdnw0EA/external_accounts",
 "data": [
 {
 "id": "{{BANK_ACCOUNT_ID}}",
 "object": "bank_account",
 "account": "acct_14qyt6Alijdnw0EA",
 "account_holder_name": "Jane Austen",
 "account_holder_type": "individual",
 "bank_name": "STRIPE TEST BANK",
 "country": "US",
 "currency": "usd",
 "default_for_currency": false,
 "fingerprint": "sSZ2yLp0EZTH17cF",
 "last4": "6789",
 "metadata": {
 },
 "routing_number": "110000000",
 "status": "new"
 },
 {...},
 {...},
 ],
 ...
}
```

Destination accounts are added via the `external_accounts` parameter when
[creating](https://docs.stripe.com/connect/custom-accounts#create) or
[updating](https://docs.stripe.com/connect/updating-service-agreements) Stripe
accounts. The value should be a bank account or debit card token returned from
[Stripe.js](https://docs.stripe.com/js). Alternatively, you can provide a hash
of the bank account details, but using Stripe.js is preferred as it prevents
sensitive data from hitting your server.

When using debit cards as a transfer destination, the following restrictions
apply:

- Must be a non-prepaid US Visa, Mastercard, or Discover
- Limited to 9,999 USD per transfer on [Instant
Payouts](https://docs.stripe.com/connect/legacy-transfers#instant-payouts)
- Generally limited to 3,000 USD per transfer otherwise

## Managing multiple bank and debit accounts

By default, providing a new value for `external_accounts` while updating a
Custom account *replaces* the existing account with the new one. To *add*
additional bank accounts or debit cards to a connected account, use the [Bank
Account](https://docs.stripe.com/api#account_create_bank_account) and
[Card](https://docs.stripe.com/api#account_create_card) creation API endpoints.

```
curl
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/external_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d external_account={{BANK_ACCOUNT_TOKEN_ID}}
```

When working with multiple currencies, Stripe automatically sends transfers to
an associated bank account or debit card for its currency, thereby avoiding
exchange fees. When there are multiple accounts available for a given currency,
Stripe uses the one set as `default_for_currency`.

Stripe maintains a list of [available country/currency
combinations](https://docs.stripe.com/connect/payouts-connected-accounts) for
your reference and to help your users choose from the supported options.

## Payout information

When using automatic transfers, the `transfer_schedule` property on an account
indicates how often the Stripe account’s balance is automatically paid out:

```
{
 ...
 "transfer_schedule": {
 "delay_days": 7,
 "interval": "daily"
 },
 ...
}
```

The `delay_days` property reflects how long it takes charges (or linked
transfers) to become available for payout. This field is useful for controlling
automatic payouts. For example, if you want your Custom accounts to receive
their funds 2 weeks after the charge is made, set `interval` to `daily` and
`delay_days` to **14**. The default is the lowest permitted value for the
account, determined by the connected account’s country. When setting or updating
this field, you may pass the string **minimum** to choose the lowest permitted
value.

There are four possible settings for the `interval` property:

- **manual** prevents automatic payouts. You will have to manually pay out the
account’s balance using the [Transfers
API](https://docs.stripe.com/api#create_transfer) (acting as the connected
account). Also set an account to `manual` to use [Instant
Payouts](https://docs.stripe.com/connect/legacy-transfers#instant-payouts).
- **daily** automatically pays out charges `delay_days` days after they’re
created. The `delay_days` value cannot be less than your own transfer schedule
or less than the default transfer schedule for the account.
- **weekly** automatically pays out the balance once a week, specified by the
`weekly_anchor` parameter (a lower-case weekday such as **monday**).
- **monthly** automatically pays out the balance once a month, specified by the
`monthly_anchor` parameter (a number from 1 to 31).

## Using manual transfers

If you set `transfer_schedule[interval]` to `manual` using the [Accounts
API](https://docs.stripe.com/api#account_object-transfer_schedule), Stripe will
hold funds in the account holder’s balance until told to pay them out (or until
a maximum of 90 days have passed). To trigger a payout of these funds, use the
[Transfers API](https://docs.stripe.com/api#create_transfer).

The Transfers API is only for moving funds from a connected Stripe account’s
balance into their external account. To move funds between Stripe accounts, see
creating [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) or
[creating destination charges through the
platform](https://docs.stripe.com/connect/destination-charges).

#### Note

*Escrow* has a precise legal definition and Stripe does not support escrow
accounts. However, we do provide escrow-like behavior through manual transfers.
This gives you control over transfer timing, with the ability to delay payouts
to Custom accounts for up to 90 days.

Manual transfers can be used as an alternative to escrow when there may be a
risk of a delayed delivery, or if there’s the possibility of a refund being
needed.

### Standard transfers

As a basic transfer example, to have 10 USD sent from a Custom account’s Stripe
balance to their external account:

```
curl https://api.stripe.com/v1/transfers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -d "amount"=1000 \
 -d "currency"="usd" \
 -d "destination"="default_for_currency"
```

Setting `destination=default_for_currency` tells Stripe to transfer to the
account’s default bank account or debit card for the given currency.

With a standard transfer, you can payout up to the user’s available balance. To
find that amount, perform a [retrieve
balance](https://docs.stripe.com/api#retrieve_balance) call on their behalf.

Stripe tracks balance contributions from different payment sources in separate
balances. The retrieve balance response breaks down the components of each
balance by source type. For example, if you want to create a transfer
specifically for a non-credit-card balance, specify the `source_type` in your
request.

```
curl https://api.stripe.com/v1/transfers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=24784 \
 -d "currency"="usd" \
 -d "destination"="default_for_currency" \
 -d "source_type"="bank_account"
```

Note that it is possible for any source’s balance component to go negative
(through refunds or chargebacks), and transfers can’t be created for greater
than the aggregate available balance.

### Using Instant Payouts

With Instant Payouts, you can immediately send funds to a Custom account’s debit
card. Funds typically appear in the associated bank account within 30 minutes,
making it possible to go from charge to payout in mere moments.

To use Instant Payouts, specify **instant** for the `method` property when
creating the transfer:

```
curl https://api.stripe.com/v1/transfers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -d "amount"=1000 \
 -d "currency"="usd" \
 -d "method"="instant"
```

Instant Payouts differ from other manual transfers in a couple of ways:

- You can transfer an account’s available balance plus its *pending* balance
- Instant Payouts can be requested on weekends and holidays

Initially, platforms can transfer up to 500 USD per day—in total, across all
connected accounts—through Instant Payouts. [Contact
us](https://support.stripe.com/contact) if you need this threshold increased.

Instant Payouts is available for all of the largest US banks, but a small
percentage of banks do not yet support it. For those banks, you will have to
fall back to standard payouts.

When you add a card to an account, Stripe returns a property
`available_payout_methods` in the response, which will be a set containing the
payout methods Stripe supports for that card. Only values in this set should be
passed as the `method` when creating a transfer.

```
{
 "id": "{{CARD_ID}}",
 "object": "card",
 ...
 "account": "acct_1032D82eZvKYlo2C",
 "available_payout_methods": ["standard", "instant"],
}
```

If a Custom account’s card does not support Instant Payouts, you should clearly
communicate to the owner of that account that they will not receive their
payouts instantly.

### Using webhooks with transfers

All transfer activity on connected accounts can be tracked using
[webhooks](https://docs.stripe.com/webhooks). (When using Connect, you should
always be using webhooks.) Specific to transfers, you’ll see these events:

- `transfer.created`
- `transfer.updated`
- `transfer.paid`
- `transfer.failed`

For most transfers, these event notifications occur over a series of days.
Instant Payouts typically send `transfer.paid` within 30 minutes.

If a transfer cannot be completed, a `transfer.failed` event occurs. The event’s
`failure_reason` property indicates why.

## See also

- [Custom accounts](https://docs.stripe.com/connect/custom-accounts)
- [Updating
accounts](https://docs.stripe.com/connect/updating-service-agreements)
- [Understanding Connect account
balances](https://docs.stripe.com/connect/account-balances)

## Links

- [Connect](https://docs.stripe.com/connect)
- [payouts](https://docs.stripe.com/payouts)
- [bank and debit card
payouts](https://docs.stripe.com/connect/payouts-connected-accounts)
- [Standard accounts](https://docs.stripe.com/connect/standard-accounts)
- [Stripe balance](https://docs.stripe.com/connect/account-balances)
- [creating](https://docs.stripe.com/connect/custom-accounts#create)
- [updating](https://docs.stripe.com/connect/updating-service-agreements)
- [Stripe.js](https://docs.stripe.com/js)
- [Bank Account](https://docs.stripe.com/api#account_create_bank_account)
- [Card](https://docs.stripe.com/api#account_create_card)
- [Transfers API](https://docs.stripe.com/api#create_transfer)
- [Accounts API](https://docs.stripe.com/api#account_object-transfer_schedule)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [creating destination charges through the
platform](https://docs.stripe.com/connect/destination-charges)
- [retrieve balance](https://docs.stripe.com/api#retrieve_balance)
- [Contact us](https://support.stripe.com/contact)
- [webhooks](https://docs.stripe.com/webhooks)
- [Custom accounts](https://docs.stripe.com/connect/custom-accounts)