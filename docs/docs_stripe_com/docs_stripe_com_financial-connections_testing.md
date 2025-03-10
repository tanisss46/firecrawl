# Test Financial Connections

## Learn how to test your integration with simulated Financial Connections accounts.

[Get started with test
mode](https://docs.stripe.com/financial-connections/testing#get-started)
To use the test mode features of Financial Connections, follow the relevant [use
case guide](https://docs.stripe.com/financial-connections/use-cases) using a
test API key. Accounts and customers that you make in test mode are invisible to
your live mode integration.

#### Note

The Financial Connections [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow)
is subject to change, so we don’t recommend automated client-side testing.
Stripe’s test mode API is also strictly [rate
limited](https://docs.stripe.com/testing#rate-limits), which you must account
for in your tests.

[How to use test accounts and
institutionsServer-side](https://docs.stripe.com/financial-connections/testing#web-how-to-use-test-accounts)
When you provide [Stripe.js](https://docs.stripe.com/js) with a Financial
Connections Session token created using test keys, the [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow)
exclusively shows a selection of test institutions managed by Stripe. The client
can link accounts from any of these institutions without providing credentials.

Features like
[balances](https://docs.stripe.com/financial-connections/balances), [account
ownership](https://docs.stripe.com/financial-connections/ownership), and
[transactions](https://docs.stripe.com/financial-connections/transactions) work
the same way as they do in live mode, except they return testing data instead of
real account data.

Test mode [webhooks](https://docs.stripe.com/webhooks) are separate from live
webhooks. Learn about [testing your webhook
integrations](https://docs.stripe.com/webhooks#test-webhook).

[Testing different user authentication
scenariosClient-side](https://docs.stripe.com/financial-connections/testing#web-test-institutions)
Stripe provides a set of test institutions exercising different success and
failure scenarios, each represented as a bank in the list of featured
institutions.

#### Simulating successful authentication

- **Test Institution**: Simulates the user successfully logging into their
institution and contains a basic set of test accounts.
- **Test OAuth Institution**: Contains the same test accounts as Test
Institution, but instead of authenticating directly with the modal, it opens an
OAuth popup for authentication.
- **Ownership Accounts**: Contains test accounts representing different
ownership states.
- **Sandbox Bank (OAuth)**: Provides a test institution OAuth popup that allows
you to select accounts to link. Sandbox Bank is the most representative of
account linking for the majority of live mode institutions.
- **Sandbox Bank (Non-OAuth)**: Provides a Stripe-hosted login form to simulate
institutions that don’t support OAuth. Use the following test credentials to
proceed:- The initial prompt asks for username and password. Entering any input
value simulates a successful login.
- In the password field or any subsequent field, enter `options` (selection from
a list), `mfa` (one-time passcode entry), `confirm_mfa` (one-time passcode
confirmation), or `security_question` (secret answer entry) to exercise further
login prompts.
- Entering `error` in any field ends the login session; `incorrect` gives you a
chance to try again.
- **Invalid Payment Accounts**: Contains test accounts that are unusable for ACH
payments.

#### Simulating failed authentication

- **Down Bank (Scheduled)**: The institution’s login API is unavailable for a
known time period that the institution communicated to Stripe.
- **Down Bank (Unscheduled)**: The institution’s login API is unavailable
without any information about the downtime communicated to Stripe.
- **Down Bank (Error)**: Stripe is experiencing an unknown error communicating
with the institution.

#### Note

We recommend manually testing OAuth and non-OAuth institutions to make sure that
both UI flows work within the context your application. See [additional
documentation](https://docs.stripe.com/financial-connections/fundamentals#how-stripe-links-financial-accounts)
about the differences between OAuth and non-OAuth connections.

## Links

- [testing](https://docs.stripe.com/testing)
- [use case guide](https://docs.stripe.com/financial-connections/use-cases)
- [authentication
flow](https://docs.stripe.com/financial-connections/fundamentals#authentication-flow)
- [rate limited](https://docs.stripe.com/testing#rate-limits)
- [Stripe.js](https://docs.stripe.com/js)
- [balances](https://docs.stripe.com/financial-connections/balances)
- [account ownership](https://docs.stripe.com/financial-connections/ownership)
- [transactions](https://docs.stripe.com/financial-connections/transactions)
- [webhooks](https://docs.stripe.com/webhooks)
- [testing your webhook
integrations](https://docs.stripe.com/webhooks#test-webhook)
- [additional
documentation](https://docs.stripe.com/financial-connections/fundamentals#how-stripe-links-financial-accounts)