# Balances

## Show balance information and allow your connected accounts to perform payouts.

Balances renders the balance summary and the payout schedule. It can also allow
the connected account to perform instant or manual payouts.

#### Note

This component is part of the [payouts
component](https://docs.stripe.com/connect/supported-embedded-components/payouts).

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable balances
by specifying `balances` in the `components` parameter. You can enable or
disable individual features of the balances component by specifying the
`features` parameter under `balances`:

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[balances][enabled]"=true \
 -d "components[balances][features][instant_payouts]"=true \
 -d "components[balances][features][standard_payouts]"=true \
 -d "components[balances][features][edit_payout_schedule]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the balances component in the front end:

```
// Include this element in your HTML
const balances = stripeConnectInstance.create('balances');
container.appendChild(balances);
```

Enabling Instant Payouts might require additional steps:

- If your platform collects fees for a connected account, you must set up
Instant Payout monetization in the
[Dashboard](https://dashboard.stripe.com/settings/connect/payouts/instant-payouts).
- If your platform is liable for a connected account’s negative balances, your
platform must be in a supported country and the account must be in the [same
country as the platform and must be in the local
currency](https://docs.stripe.com/connect/instant-payouts#eligible-connected-accounts).
- If Stripe is liable for a connected account’s negative balances, [Stripe
controls
eligibility](https://docs.stripe.com/payouts/instant-payouts#eligibility-and-daily-volume-limits)
for the account.

#### Note

To use standard manual payouts, the connected account needs to have their
[payout schedule](https://docs.stripe.com/connect/manage-payout-schedule) set to
`manual`. You can enable payout schedule editing in the payouts component by
setting the `edit_payout_schedule` feature to `true`.

## Links

- [payouts
component](https://docs.stripe.com/connect/supported-embedded-components/payouts)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
-
[Dashboard](https://dashboard.stripe.com/settings/connect/payouts/instant-payouts)
- [same country as the platform and must be in the local
currency](https://docs.stripe.com/connect/instant-payouts#eligible-connected-accounts)
- [Stripe controls
eligibility](https://docs.stripe.com/payouts/instant-payouts#eligibility-and-daily-volume-limits)
- [payout schedule](https://docs.stripe.com/connect/manage-payout-schedule)