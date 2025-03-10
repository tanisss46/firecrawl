# Payouts

## Show payout information and allow your users to perform payouts.

Payouts renders the balance summary, the payout schedule, and a list of payouts
for the connected account. It can also allow the user to perform instant or
manual payouts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
payouts embedded component by specifying `payouts` in the `components`
parameter. You can enable or disable individual features of the payouts
component by specifying the `features` parameter under `payouts`:

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payouts][enabled]"=true \
 -d "components[payouts][features][instant_payouts]"=true \
 -d "components[payouts][features][standard_payouts]"=true \
 -d "components[payouts][features][edit_payout_schedule]"=true \
 -d "components[payouts][features][external_account_collection]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payouts component in the front end:

```
// Include this element in your HTML
const payouts = stripeConnectInstance.create('payouts');
container.appendChild(payouts);
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