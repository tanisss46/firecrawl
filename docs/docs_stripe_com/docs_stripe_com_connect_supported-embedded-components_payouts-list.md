# Payouts list

## Show a filterable list of payouts.

Payouts list renders a list of payouts for the connected account.

#### Note

This component is part of the [payouts
component](https://docs.stripe.com/connect/supported-embedded-components/payouts).

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable payouts
list by specifying `payouts_list` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payouts_list][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payouts list component in the front end:

```
// Include this element in your HTML
const payoutsList = stripeConnectInstance.create('payouts-list');
container.appendChild(payoutsList);
```

## Links

- [payouts
component](https://docs.stripe.com/connect/supported-embedded-components/payouts)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)