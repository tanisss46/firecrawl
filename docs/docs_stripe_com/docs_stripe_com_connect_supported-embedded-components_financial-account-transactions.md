# Financial account transactions

## Show a table of all transactions for a financial account.

Financial account transactions renders the view of a list of
[transactions](https://docs.stripe.com/api/treasury/transactions) associated
with a [financial
account](https://docs.stripe.com/api/treasury/financial_accounts) for your
connected accounts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The permission boundary for this component is at the connected account level,
not at the individual financial account level. This UI should be shown to users
that have access to all financial accounts, not to users that have restricted
access to a single financial account.

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
financial account transactions component by specifying
`financial_account_transactions` in the `components` parameter. You can enable
or disable individual features of the financial account component by specifying
the `features` parameter under `financial_account_transactions`.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[financial_account_transactions][enabled]"=true \
-d
"components[financial_account_transactions][features][card_spend_dispute_management]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the financial account transactions component in the frontend:

```
// Include this element in your HTML
const financialAccountTransactions =
stripeConnectInstance.create('financial-account-transactions');
financialAccountTransactions.setFinancialAccount('{{FINANCIAL_ACCOUNT_ID')
container.appendChild(financialAccountTransactions);
```

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setFinancialAccount``string`The ID of the
financial account which you want to display a list of transactions forrequired

## Links

- [transactions](https://docs.stripe.com/api/treasury/transactions)
- [financial account](https://docs.stripe.com/api/treasury/financial_accounts)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)