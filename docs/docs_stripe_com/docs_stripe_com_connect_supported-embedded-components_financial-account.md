# Financial Account

## Show the details of a Financial Account.

Financial Account renders the view of an individual [Financial
Account](https://docs.stripe.com/api/treasury/financial_accounts) for your
connected accounts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The permission boundary for this component is at the connected account level,
not at the individual financial account level. This UI should be shown to users
that have access to all financial accounts, not to users that have restricted
access to a single financial account.

## External account collection

Use the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-financial_account-features-external_account_collection)
feature to control whether the component collects external account information.
This parameter is enabled by default, and only platforms responsible for
collecting updated information when requirements are due or change (including
Custom accounts) can disable it. When `external_account_collection` is enabled,
[user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
is required. You can opt out of Stripe user authentication with the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-financial_account-features-disable_stripe_user_authentication)
parameter.

## Disable Stripe user authentication

Use the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-financial_account-features-disable_stripe_user_authentication)
feature to control whether the component requires Stripe user authentication.
The default value is the opposite of the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-financial_account-features-external_account_collection)
value. For example, if you don’t set `external_account_collection`, it defaults
to true and `disable_stripe_user_authentication` defaults to false. This value
can only be true for accounts where `controller.requirement_collection` is
`application`.

We recommend implementing 2FA or equivalent security measures as a [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs).
For account configurations that support this feature, such as Custom accounts,
you assume liability for connected accounts if they can’t pay back [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability).

## Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
financial account component by specifying `financial_account` in the
`components` parameter. You can enable or disable individual features of the
financial account component by specifying the `features` parameter under
`financial_account`.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[financial_account][enabled]"=true \
 -d "components[financial_account][features][send_money]"=true \
 -d "components[financial_account][features][transfer_balance]"=true \
 -d "components[financial_account][features][external_account_collection]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the financial account component in the frontend:

```
// Include this element in your HTML
const financialAccount = stripeConnectInstance.create('financial-account');
financialAccount.setFinancialAccount('{{FINANCIAL_ACCOUNT_ID')
container.appendChild(financialAccount);
```

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescriptionDefault`setFinancialAccount``string`The ID of
the Financial Account to display.required

## Links

- [Financial Account](https://docs.stripe.com/api/treasury/financial_accounts)
- [furever.dev](https://furever.dev)
-
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-financial_account-features-external_account_collection)
- [user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-financial_account-features-disable_stripe_user_authentication)
- [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs)
- [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)