# Using OAuth with Express accountsDeprecated

## Use the OAuth connection flow to allow an Express user to connect to your platform.

#### Caution

OAuth isn’t available for new [Connect](https://docs.stripe.com/connect)
platforms. For new accounts, use [Accounts API with
Express](https://docs.stripe.com/connect/express-accounts) instead.
[Extensions](https://docs.stripe.com/building-extensions) shouldn’t use Express
OAuth, as extensions can’t connect to existing Express accounts. If you need
access to OAuth for Express accounts, please [contact
support](https://support.stripe.com/).

## The OAuth connection flow

A user connects to your platform using the following OAuth connection flow:

- On a page on your site, you provide a
[link](https://docs.stripe.com/connect/oauth-express-accounts#integrating-oauth)
that redirects your user to Stripe, passing along your platform’s `client_id`.
- On Stripe’s website, the user provides the necessary information for
[connecting](https://docs.stripe.com/connect/oauth-express-accounts#connect-users)
to your platform.
- Stripe
[redirects](https://docs.stripe.com/connect/oauth-express-accounts#redirected)
the user to your site, along with an authorization code.
- Your site then makes a request to Stripe’s [OAuth token
endpoint](https://docs.stripe.com/connect/oauth-express-accounts#token-request)
to complete the connection and fetch the user’s account ID.

After these steps are complete, you can make API requests for the user with
their [account
ID](https://docs.stripe.com/connect/authentication#stripe-account-header).

## Step 1: You provide the OAuth link

To start your integration, go to your [platform
settings](https://dashboard.stripe.com/account/applications/settings) and:

- Enable onboarding Express accounts with OAuth in the OAuth settings.
- your `client_id`, a unique identifier for your platform that’s generated
by Stripe.
- Set your `redirect_uri`, the URL that your user is redirected to after
connecting their account. You must specify all redirect URLs in your platform
settings. If you don’t include the `redirect_uri` parameter in your request,
Stripe defaults to using the first address you’ve configured in your platform
settings.

Stripe also provides a development `client_id` to help with
[testing](https://docs.stripe.com/connect/testing#using-oauth).

With these two pieces of information in hand, you’re ready to create the OAuth
link. We recommend showing a [Connect
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip)
that sends users to our Express OAuth endpoint:

```

https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}
```

To prevent CSRF attacks, add the `state` parameter with the value set to a
unique token. Stripe includes this `state` value in the redirect URL that sends
the user back to your site. Then, confirm that this `state` parameter has the
same value you originally provided.

Here’s how you can present the example URL, along with our [Connect with Stripe
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip):

[Connect
with](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write)
### Customize Express with OAuth parameters

You can change the behavior of the Express onboarding flow by including
additional URL parameters in your OAuth link. A complete list of available
parameters is available in the [OAuth
reference](https://docs.stripe.com/connect/oauth-reference).

#### Individual or company accounts

You can specify whether Stripe presents an Express onboarding form for
individuals or companies by setting the `stripe_user[business_type]` parameter
to either `individual` or `company`.

Stripe collects the right information for each type of account. For example, to
onboard a company:

```

https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}&stripe_user[business_type]=company
```

#### Prefill form fields

You can prefill some form fields on the user’s Stripe application by including
the relevant [URL parameters](https://docs.stripe.com/connect/oauth-reference)
in your OAuth link.

This example prefills the user’s email address with `stripe_user[email]`:

```

https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=https://connect.stripe.com/connect/default/oauth/test&state={STATE_VALUE}&stripe_user[email]=user@example.com
```

#### Specify capabilities for an account

You can change the capabilities for new connected accounts in the [Dashboard
settings for Express](https://dashboard.stripe.com/settings/connect/express).
However, if you want to request different capabilities for each of your
connected accounts, you can include the `suggested_capabilities[]` parameter in
your OAuth link and override the Dashboard settings on the Express Configuration
page.

An example with the `transfers` capability:

```

https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}&suggested_capabilities[]=transfers
```

Stripe adds the suggested capability to this Express account, unless one of the
following conditions is met:

- If the user is in a country that doesn’t support `transfers`, Stripe attempts
to designate the account as `card_payments`.
- If the user’s account doesn’t support `transfers` *or* `card_payments`, Stripe
marks the account as having no capabilities.

You can verify that Stripe added the suggested capability by using the
`assert_capabilities[]` parameter. This step is optional.

## Step 2: The user creates their account

When the user clicks the link on your site, it takes them to Stripe’s website,
which prompts them to provide contact and
[payout](https://docs.stripe.com/payouts) information.

![Stripe's website for a user to provide their contact and payout
information](https://b.stripecdn.com/docs-statics-srv/assets/rocket-rides-express.33f3b71b60ed5244eef4ff3761e2c480.png)

To test the onboarding process, you can provide *(000) 000-0000* as a phone
number. Instead of sending you an SMS message or email, Stripe lets you complete
verification with the code *000-000*.

Express displays your branding in the onboarding flow and the Express Dashboard.
You can provide your platform name, logo, and optional brand color in the
[Connect settings](https://dashboard.stripe.com/account/applications/settings)
section of the Stripe Dashboard.

## Step 3: Stripe redirects the user to your site

After the user completes the onboarding process, Stripe redirects them back to
your site using the URL defined as your platform’s `redirect_uri`.

For successful connections, the redirect URL includes the following values:

- The `state` value, if provided.
- An authorization code. The authorization code is short-lived, and can be used
only once, in the POST request described in the next step.

```
https://connect.stripe.com/connect/default/oauth/test?code={AUTHORIZATION_CODE}
```

## Step 4: You complete the Express account connection

Include the provided authorization `code` in a POST request to Stripe’s token
endpoint to complete the connection and fetch the user’s account ID:

```
curl https://connect.stripe.com/oauth/token \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "code"="ac_123456789" \
 -d "grant_type"="authorization_code"
```

Stripe returns a response that includes the account ID (`stripe_user_id`) for
the user:

```
{
 "livemode": false,
 "token_type": "bearer",
 "stripe_user_id": "{{CONNECTED_ACCOUNT_ID}}",
 "scope": "express",
 ...
}
```

Or, if there’s a problem, Stripe returns a detailed error message:

```
{
 "error": "invalid_grant",
 "error_description": "Authorization code does not exist: {AUTHORIZATION_CODE}"
}
```

The user is now connected to your platform. The `stripe_user_id` is the Stripe
account ID for the new account. Store this value in your database and use it to
authenticate as the connected account by passing it into requests in the
`Stripe-Account` header.

#### Note

Store `stripe_user_id`, which is the account’s ID. Platforms need this value
(beginning with `acct_`) to transfer funds, create charges, and perform requests
on the user’s behalf.

### Verify the account’s capability

If you provide the `suggested_capabilities[]` parameter, you can add the
`assert_capabilities[]` parameter to verify that the connected account now has
the suggested capabilities. For instance, you can check this if you’re concerned
about URL security. This step is optional, however. Stripe handles any failure
to apply a capability silently.

```
curl https://connect.stripe.com/oauth/token \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "code"="ac_123456789" \
 -d "grant_type"="authorization_code" \
 -d "assert_capabilities[]"="transfers"
```

A success response then looks like this:

```
{
 "livemode": false,
 "token_type": "bearer",
 "stripe_user_id": "{{CONNECTED_ACCOUNT_ID}}",
 "scope": "express",
 "capabilities": "transfers",
 ...
}
```

If the specified `capabilities[]` value doesn’t match, the error response looks
like this:

```
{
 "error": "invalid_request",
 "error_description": "assert_capabilities expects capability: card_payments"
}
```

The most common reason for this request failure is that the specified capability
isn’t available in your user’s country. A less likely reason is a bad actor
changing the URL.

## Webhooks

After you create an account, you can get all account change notifications
delivered to your [webhooks](https://docs.stripe.com/connect/webhooks) as
`account.updated` events. You set your Connect
[webhook](https://docs.stripe.com/webhooks) URL in your [account
settings](https://dashboard.stripe.com/account/webhooks). These events let you
track the onboarding and verification status of connected accounts, which you
can use to provide user support and display notices in your platform’s user
interface. Alternatively, you can let Stripe take your users through the steps
of the onboarding and verification process and handle any issues that arise.

If you created an account in test mode using either a test mode API key or
`client_id`, Stripe doesn’t send any emails while you build your Stripe
integration. (But when you’re live, we do.)

## Links

- [Connect](https://docs.stripe.com/connect)
- [Accounts API with Express](https://docs.stripe.com/connect/express-accounts)
- [Extensions](https://docs.stripe.com/building-extensions)
- [contact support](https://support.stripe.com/)
- [account
ID](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [through the
dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts)
- [platform
settings](https://dashboard.stripe.com/account/applications/settings)
- [testing](https://docs.stripe.com/connect/testing#using-oauth)
- [Connect
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip)
-
[https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}](https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE})
- [Connect
with](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write)
- [OAuth reference](https://docs.stripe.com/connect/oauth-reference)
-
[https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}&stripe_user[business_type]=company](https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}&stripe_user[business_type]=company)
-
[https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=https://connect.stripe.com/connect/default/oauth/test&state={STATE_VALUE}&stripe_user[email]=user@example.com](https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=https://connect.stripe.com/connect/default/oauth/test&state={STATE_VALUE}&stripe_user[email]=user@example.com)
- [Dashboard settings for
Express](https://dashboard.stripe.com/settings/connect/express)
-
[https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}&suggested_capabilities[]=transfers](https://connect.stripe.com/express/oauth/authorize?redirect_uri=https://connect.stripe.com/connect/default/oauth/test&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&state={STATE_VALUE}&suggested_capabilities[]=transfers)
- [payout](https://docs.stripe.com/payouts)
-
[https://connect.stripe.com/connect/default/oauth/test?code={AUTHORIZATION_CODE}](https://connect.stripe.com/connect/default/oauth/test?code={AUTHORIZATION_CODE})
- [webhooks](https://docs.stripe.com/connect/webhooks)
- [webhook](https://docs.stripe.com/webhooks)
- [account settings](https://dashboard.stripe.com/account/webhooks)