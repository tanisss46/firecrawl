# Using OAuth with Standard accounts

## Use the OAuth connection flow to allow a Stripe user to connect to your platform.

OAuth is not recommended for new [Connect](https://docs.stripe.com/connect)
platforms. We recommend using [Connect Onboarding for Standard
accounts](https://docs.stripe.com/connect/standard-accounts) instead.

Starting in June 2021, Platforms using OAuth with `read_write` scope won’t be
able to connect to Standard accounts that are controlled by another platform.

[Extensions](https://docs.stripe.com/building-extensions) will not experience
any changes to how OAuth behaves. Learn more about [OAuth changes for
platform-controlled Standard
accounts](https://docs.stripe.com/connect/oauth-changes-for-standard-platforms).

## The OAuth connection flow

A user connects to your platform using the following OAuth connection flow:

- From a page on your site, the user clicks a
[link](https://docs.stripe.com/connect/oauth-standard-accounts#integrating-oauth)
that redirects them to Stripe, passing along your platform’s `client_id`.
- On Stripe’s website, the user provides the necessary information for
[connecting](https://docs.stripe.com/connect/oauth-standard-accounts#connect-users)
to your platform.
- The user is
[redirected](https://docs.stripe.com/connect/oauth-standard-accounts#redirected)
to your site, along with an authorization code.
- Your site then makes a request to Stripe’s [OAuth token
endpoint](https://docs.stripe.com/connect/oauth-standard-accounts#token-request)
to complete the connection and fetch the user’s account ID.

#### Note

As a platform, remember that data you create for an account (for example,
charges, customers, [invoices](https://docs.stripe.com/api/invoices), and so on)
will be visible on their Stripe account. It also means that if they connect
other platforms, those platforms can access this data too.

[Create the OAuth
link](https://docs.stripe.com/connect/oauth-standard-accounts#integrating-oauth)
To start your integration, go to your [Connect OAuth onboarding
options](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth)
and:

- Enable onboarding accounts with OAuth in [the OAuth
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth).
- your `client_id`, a unique identifier for your platform that’s generated
by Stripe.
- Set your `redirect_uri`, the URL which your user will be redirected to after
connecting their account. You must specify all redirect URLs in your platform
settings. If you do not include the `redirect_uri` parameter in your request,
Stripe defaults to using the first address you have configured in your platform
settings.

Stripe also provides a
[client_id](https://dashboard.stripe.com/test/settings/connect/onboarding-options/oauth)
to help with [testing](https://docs.stripe.com/connect/testing#using-oauth).
Each `client_id` is either a live or test ID. Use a Sandbox `client_id` to
connect to a Sandbox account.

With these pieces of information in hand, you’re ready to create the OAuth link.
We recommend showing a **Connect with Stripe** button that sends users to the
`authorize_url` endpoint:

```

https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write
```

The Stripe endpoint should receive at least these three parameters:

- `response_type`, with a value of **code**
- Your `client_id`
- `scope`, with a value of **read_write**

The `scope` parameter dictates what your platform can do on behalf of the
connected account, with **read_only** being the default.

To prevent CSRF attacks, add the `state` parameter, passing along a unique token
as the value. We’ll include the `state` you gave us when we redirect the user
back to your site. Your site should confirm the `state` parameter hasn’t been
modified.

Here’s how the above URL can be presented to your user to begin the connection,
along with our [Connect with Stripe
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip):

[Connect
with](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write)
### Customize onboarding with OAuth parameters

You can change the behavior of the onboarding flow by including additional URL
parameters in your OAuth link. A complete list of available parameters is
available in the [OAuth
reference](https://docs.stripe.com/connect/oauth-reference).

[User creates or connects their
account](https://docs.stripe.com/connect/oauth-standard-accounts#connect-users)
After the user clicks the link on your site, they’ll be taken to Stripe’s
website where they’ll be prompted to allow or deny the connection to your
platform.

The process of creating a Stripe account is incorporated into our authorization
flow. You don’t need to worry about whether or not your users already have
accounts.

!

The user is logged in and can choose an account to connect to your platform
directly.

!

The user needs to create an account.

[User is redirected back to your
site](https://docs.stripe.com/connect/oauth-standard-accounts#redirected)
After the user connects their existing or newly created account to your
platform, they’re redirected back to your site, to the URL established as your
platform’s `redirect_uri`.

For successful connections, we’ll pass along in the URL:

- The `scope` granted
- The `state` value, if provided
- An authorization code. The authorization code is short-lived, and can be used
only once, in the POST request described in the next step.

```

https://connect.stripe.com/connect/default/oauth/test?scope=read_write&code={AUTHORIZATION_CODE}
```

If the authorization was denied by the user, they’ll still be redirected back to
your site, but the URL includes an error instead of the authorization code:

```

https://connect.stripe.com/connect/default/oauth/test?error=access_denied&error_description=The%20user%20denied%20your%20request
```

[Platform completes the account
connection](https://docs.stripe.com/connect/oauth-standard-accounts#token-request)
Include the provided authorization `code` in a POST request to Stripe’s token
endpoint to complete the connection and fetch the user’s account ID:

```
curl https://connect.stripe.com/oauth/token \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "code"="ac_123456789" \
 -d "grant_type"="authorization_code"
```

Note that you’ll make the request with your live or test secret API key,
depending on whether you want to get a live or test access token back.

Stripe returns a response that includes the account ID (`stripe_user_id`) for
the user:

```
{
 "token_type": "bearer",
 "scope": "read_write",
 "livemode": false,
 "stripe_user_id": "{{CONNECTED_ACCOUNT_ID}}",
}
```

If there was a problem, we instead return an error:

```
{
 "error": "invalid_grant",
 "error_description": "Authorization code does not exist: {AUTHORIZATION_CODE}"
}
```

You’re done! The user is now connected to your platform. Store the
`stripe_user_id` in your database; this is the Stripe account ID for the new
account. You’ll use this value to
[authenticate](https://docs.stripe.com/connect/authentication) as the connected
account by passing it into requests in the `Stripe-Account` header.

In your application, you might want to consider using a dedicated OAuth client
library to simplify these steps. To find an OAuth library for your language or
framework, you can refer to the [list of client
libraries](https://oauth.net/code/) on the OAuth website.

The `refresh_token` can be used to [generate test access
tokens](https://docs.stripe.com/connect/testing#creating-accounts) for a
production `client_id` or to roll your access token. You should hold on to this
value, too, as you’re only able to get it after this initial POST request.

#### Note

**Store the received account ID!** Platforms need this information to perform
requests on the user’s behalf.

## Revoked and revoking access

An `account.application.deauthorized`
[event](https://docs.stripe.com/api#list_events) occurs when a user disconnects
your platform from their account. By watching for this event via
[webhooks](https://docs.stripe.com/connect/webhooks), you can perform any
necessary cleanup on your servers.

To disconnect an account with access to the Stripe Dashboard from your platform,
POST your `client_id` and the connected account’s ID to
`connect.stripe.com/oauth/deauthorize`:

```
curl https://connect.stripe.com/oauth/deauthorize \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d client_id="ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb" \
 -d stripe_user_id=acct_ON3nXtRQkhmUIQ
```

You can use the API on your user’s behalf to accept payments, set up recurring
billing, fetch account data, and so on.

## See also

- [Authentication](https://docs.stripe.com/connect/authentication)
- [OAuth reference](https://docs.stripe.com/connect/oauth-reference)
- [Full API reference](https://docs.stripe.com/api)

## Links

- [Connect](https://docs.stripe.com/connect)
- [Connect Onboarding for Standard
accounts](https://docs.stripe.com/connect/standard-accounts)
- [Extensions](https://docs.stripe.com/building-extensions)
- [OAuth changes for platform-controlled Standard
accounts](https://docs.stripe.com/connect/oauth-changes-for-standard-platforms)
- [invoices](https://docs.stripe.com/api/invoices)
- [through the
dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts)
- [Connect OAuth onboarding
options](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth)
-
[client_id](https://dashboard.stripe.com/test/settings/connect/onboarding-options/oauth)
- [testing](https://docs.stripe.com/connect/testing#using-oauth)
-
[https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write)
- [Connect with Stripe
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip)
- [OAuth reference](https://docs.stripe.com/connect/oauth-reference)
-
[https://connect.stripe.com/connect/default/oauth/test?scope=read_write&code={AUTHORIZATION_CODE}](https://connect.stripe.com/connect/default/oauth/test?scope=read_write&code={AUTHORIZATION_CODE})
-
[https://connect.stripe.com/connect/default/oauth/test?error=access_denied&error_description=The%20user%20denied%20your%20request](https://connect.stripe.com/connect/default/oauth/test?error=access_denied&error_description=The%20user%20denied%20your%20request)
- [authenticate](https://docs.stripe.com/connect/authentication)
- [list of client libraries](https://oauth.net/code/)
- [generate test access
tokens](https://docs.stripe.com/connect/testing#creating-accounts)
- [event](https://docs.stripe.com/api#list_events)
- [webhooks](https://docs.stripe.com/connect/webhooks)
- [Full API reference](https://docs.stripe.com/api)