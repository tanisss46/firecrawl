# Disconnect a Financial Connections account

## Use the Disconnect API to unlink customer bank accounts.

Disconnect a user’s [Financial Connections
Account](https://docs.stripe.com/api/financial_connections/accounts/object) if
you no longer need data access or if your user writes into you requesting
disconnection. Alternatively, your users can [disconnect their accounts
themselves](https://support.stripe.com/user/how-do-i-disconnect-my-linked-financial-account).

Although you can’t refresh data on a disconnected account, you can access
previously refreshed account data. Disconnecting an account only removes your
ability to refresh data; it doesn’t cause any associated
[PaymentMethods](https://docs.stripe.com/api/payment_methods) to become
unusable.

To regain access to new account data, your user needs to re-authenticate their
account through the [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow).

## Disconnect a Financial Connections account

To disconnect an account, use the [disconnect
API](https://docs.stripe.com/api/financial_connections/accounts/disconnect):

```
curl -X POST
https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}/disconnect
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

This request returns the account with an updated `status` to reflect the
successful disconnection.

```
{
 "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
 "object": "financial_connections.account",
 "account_holder": {
 "customer": "cus_NfjonN9919dELB",
 "type": "customer"
 },
 "institution_name": "PNC Bank",
 "status": "disconnected",
 // ...
}
```

After account disconnection, Stripe emits a
`financial_connections.account.disconnected`
[webhook](https://docs.stripe.com/webhooks).

## Links

- [Financial Connections
Account](https://docs.stripe.com/api/financial_connections/accounts/object)
- [disconnect their accounts
themselves](https://support.stripe.com/user/how-do-i-disconnect-my-linked-financial-account)
- [PaymentMethods](https://docs.stripe.com/api/payment_methods)
- [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow)
- [disconnect
API](https://docs.stripe.com/api/financial_connections/accounts/disconnect)
- [webhook](https://docs.stripe.com/webhooks)