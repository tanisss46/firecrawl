# Debit connected accounts

## Collect funds from a connected account by debiting its Stripe balance.

At times, your platform might need to collect funds from your connected
accounts:

- To charge the connected account directly for products or services
- To recover funds for a previous refund
- To make other adjustments to connected [account
balances](https://docs.stripe.com/connect/account-balances) (for example, to
correct an error)

When your platform is responsible for negative balances, such as with Express
and Custom connected accounts, you can debit a connected account’s Stripe
balance, transferring funds to your platform balance.

#### Note

To bill connected accounts where Stripe is responsible for negative balances,
create a customer for each connected account and [charge them using Stripe
Billing
subscriptions](https://docs.stripe.com/connect/subscriptions#connected-account-platform).

This creates a `Transfer` on the connected account and a `Payment` on the
platform account.

#### Caution

Using Account Debits requires getting legally binding consent from your
connected accounts. This feature is available in Australia, Canada, Europe, Hong
Kong, Japan, New Zealand, and the US. Stripe supports Account Debits only when
both your platform and the connected account are in the same region (for
example, both are in Japan). If you have interest in other regions, contact the
[sales team](https://stripe.com/contact/sales). Using Account Debits incurs an
[additional cost](https://stripe.com/connect/pricing).

## Requirements

This functionality is only supported for connected accounts where your platform
is responsible for negative balances, including Express and Custom accounts.
Additionally:

- The connected account and the platform must be in the same region (that is,
both must be in Europe or in the US).
- The `currency` value must match the default currency of the connected account.
- Debiting an account can’t make the connected account balance become negative
unless you have [reserves
enabled](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances)
(on by default for all new platforms created after January 31, 2017) and have a
bank account in the same currency as the debit.
- If a connected account has a [negative
balance](https://docs.stripe.com/connect/account-balances#accounting-for-negative-balances),
Stripe might auto-debit the external account on file, depending on what country
the connected account is in. If the external account hasn’t been verified, the
debit can fail.
- The maximum `amount` is 100,000 USD (or equivalent in your currency).

## Charging a connected account

The [create a charge](https://docs.stripe.com/api#create_charge) API call
supports providing a connected account ID as the `source` value:

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1500 \
 -d currency=usd \
 -d source={{CONNECTED_ACCOUNT_ID}}
```

The API call returns the `Payment` created on the platform account (note: it
does not return a `Charge`).

This approach is appropriate for platforms that charge their connected accounts
for goods and services (that is, for using the platform). For example, a
platform can charge its connected accounts for additional fees or services
through their Stripe balance, minimizing any need to collect an additional
payment method and allowing for nearly instant availability of the funds.

## See also

- [Creating Direct Charges](https://docs.stripe.com/connect/direct-charges)
- [Creating Destination Charges on Your
Platform](https://docs.stripe.com/connect/destination-charges)
- [Creating Separate Charges and
Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

## Links

- [account balances](https://docs.stripe.com/connect/account-balances)
- [charge them using Stripe Billing
subscriptions](https://docs.stripe.com/connect/subscriptions#connected-account-platform)
- [sales team](https://stripe.com/contact/sales)
- [additional cost](https://stripe.com/connect/pricing)
- [reserves
enabled](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances)
- [negative
balance](https://docs.stripe.com/connect/account-balances#accounting-for-negative-balances)
- [create a charge](https://docs.stripe.com/api#create_charge)
- [Creating Direct Charges](https://docs.stripe.com/connect/direct-charges)
- [Creating Destination Charges on Your
Platform](https://docs.stripe.com/connect/destination-charges)
- [Creating Separate Charges and
Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)