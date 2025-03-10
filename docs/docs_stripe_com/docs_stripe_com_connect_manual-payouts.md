# Using manual payouts

## Send manual payouts to your connected accounts.

If you set the value of
[schedule.interval](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-schedule)
to `manual`, we hold funds in the accountholder’s balance until you specify
otherwise. You must pay out the funds within the time period specified below,
based on the business’s country:

CountryHolding PeriodThailand10 daysUnited States2 yearsAll other countries90
days
To trigger a payout of these funds, use the [Payouts
API](https://docs.stripe.com/api/payouts/create).

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "settings[payouts][schedule][interval]"=manual
```

The Payouts API is only for moving funds from a connected Stripe account’s
balance into their external account. To move funds between the platform and a
connected account, see creating [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) or
creating [destination
charges](https://docs.stripe.com/connect/destination-charges) through the
platform.

#### Note

*Escrow* has a precise legal definition, and Stripe doesn’t provide escrow
services or support escrow accounts. However, you can control payout timing
through manual payouts, which allow you to delay payouts to certain accounts.
When using manual payouts, you must pay out funds within the time frame for the
business’s country.

Delayed payouts can be useful when a delivery is delayed or when there’s a
possibility of a refund.

## Regular payouts

The following example sends 10 USD from a connected account’s Stripe balance to
their external account:

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd
```

With a standard payout, you can move an amount up to the user’s available
balance. To find that amount, perform a [retrieve
balance](https://docs.stripe.com/api#retrieve_balance) call on their behalf.

Stripe tracks balance contributions from different payment sources in separate
balances. The retrieve balance response breaks down the components of each
balance by source type. For example, to create a payout specifically for a
non-credit-card balance, specify the `source_type` in your request.

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=24784 \
 -d currency=usd \
 -d source_type=bank_account
```

While individual balance components can go negative (such as through refunds or
chargebacks), you can’t create payouts for greater than the aggregate available
balance.

## Links

-
[schedule.interval](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-schedule)
- [Payouts API](https://docs.stripe.com/api/payouts/create)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [retrieve balance](https://docs.stripe.com/api#retrieve_balance)