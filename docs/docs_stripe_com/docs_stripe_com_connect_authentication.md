# Making API calls for connected accounts

## Learn how to add the right information to your API calls so you can make calls for your connected accounts.

You can make API calls for your connected accounts:

- Server-side with the [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
and the connected account ID, per request
- Client-side by passing the connected account ID as an argument to the client
library

To help with performance and reliability, Stripe has established [rate limits
and allocations](https://docs.stripe.com/rate-limits) for API endpoints.

## Adding the Stripe-Account header server-side

To make server-side API calls for connected accounts, use the `Stripe-Account`
header with the account identifier, which begins with the prefix `acct_`. Here
are four examples using your platform’s [API secret
key](https://docs.stripe.com/keys) and the connected account’s
[Account](https://docs.stripe.com/api/accounts) identifier:

Create PaymentIntentRetrieve BalanceList ProductsDelete Customer
```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd
```

The `Stripe-Account` header approach is implied in any API request that includes
the Stripe account ID in the URL. Here’s an example that shows how to [Retrieve
an account](https://docs.stripe.com/api/accounts/retrieve) with your user’s
[Account](https://docs.stripe.com/api/accounts) identifier in the URL.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

All of Stripe’s server-side libraries support this approach on a per-request
basis:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 --data-urlencode email="person@example.com"
```

## Adding the connected account ID to a client-side application

Client-side libraries set the connected account ID as an argument to the client
application:

HTML + JSReactiOSAndroidReact Native
The JavaScript code for passing the connected account ID client-side is the same
for plain JS and for ESNext.

```
var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx', {
 stripeAccount: {{CONNECTED_ACCOUNT_ID}},
});
```

## See also

- [Creating charges](https://docs.stripe.com/connect/charges)
- [Using subscriptions](https://docs.stripe.com/connect/subscriptions)

## Links

- [rate limits and allocations](https://docs.stripe.com/rate-limits)
- [API secret key](https://docs.stripe.com/keys)
- [Account](https://docs.stripe.com/api/accounts)
- [Retrieve an account](https://docs.stripe.com/api/accounts/retrieve)
- [Creating charges](https://docs.stripe.com/connect/charges)
- [Using subscriptions](https://docs.stripe.com/connect/subscriptions)