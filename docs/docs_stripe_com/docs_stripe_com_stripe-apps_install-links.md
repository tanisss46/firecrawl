# Using install linksPublic preview

## Allow users to install your app outside the Stripe App Marketplace.

Install links allow users to install public apps outside of the Stripe App
Marketplace. With one integrated flow, you can pass state from your application,
complete the installation of the Stripe App, and redirect to your application or
site.

![The install link page showing app
permissions](https://b.stripecdn.com/docs-statics-srv/assets/oauth-permissions.9f11ce1ba29fdd77c9d4fa9ee2944222.png)

The install link page

## Overview

With the following steps, a user can install an app using an install link:

- On your site, the user clicks a link that redirects them to Stripe, passing
along the `app_id`.
- On Stripe, the user selects the appropriate account and accepts permissions
for installing the app.
- After installation, the user [redirects to your
site](https://docs.stripe.com/stripe-apps/install-links#redirect), along with
the Stripe account for the given user.
- Your app can now make authenticated account requests.
[Create an install
link](https://docs.stripe.com/stripe-apps/install-links#create-install-link)
Set your `allowed_redirect_uris` in your app manifest. These are the URLs that
users are redirected to after installing your app. You must specify all redirect
URLs in your app settings.

After you’ve set `allowed_redirect_uris`, [upload a new
version](https://docs.stripe.com/stripe-apps/upload-install-app) of your app.

```
{
 "id": "com.invoicing.[YOUR_APP]",
 "version": "1.2.3",
 "name": "[YOUR APP] Shipment Invoicing",
 "icon": "./[YOUR_APP]_icon_32.png",
 "permissions": [],
 "app_backend": {},
 "ui_extension": {},
 "allowed_redirect_uris": [
 "https://example.com/callback/stripe"
 ]
}
```

[Test your install
link](https://docs.stripe.com/stripe-apps/install-links#test-install-link)
You can use [external testing](https://docs.stripe.com/stripe-apps/test-app)
with the following steps to test the install link before submitting it for
review:

- [Create an external test](https://docs.stripe.com/stripe-apps/test-app) for
your app using the version with `allowed_redirect_uris` defined in the app
manifest. You can update the testing version to the desired one if a test
already exists.
- The **External test** tab shows a test install link and displays the allowed
redirects in a table.
- When you’re ready to publish, make sure that you upload a new version with any
testing URIs and values replaced with the values you intend to use in
production.

![The external test tab showing install
links](https://b.stripecdn.com/docs-statics-srv/assets/external-test.8df1fb2e4ac4df4c934d4acca85ed2de.png)

[Using an install
link](https://docs.stripe.com/stripe-apps/install-links#use-install-link)
When you’ve finished testing, you can make it available for all users with the
following steps:

- [Publish a new version](https://docs.stripe.com/stripe-apps/publish-app) of
your app that defines `allowed_redirect_uris`.
- Click the **Settings** tab. The install link is shown here, and you can copy
it. The link looks like this:
`https://marketplace.stripe.com/apps/install/link/{id}?redirect_uri=https://example.com`.
- Recommended To prevent CSRF attacks, you can add the recommended `state`
parameter and pass along a unique token as the value. We’ll include the `state`
you provided when redirecting users to your site. Your site can confirm that the
`state` parameter hasn’t been modified.
- After a user clicks the install link, Stripe opens the following page where
they can select an account, review app details, and proceed with the
installation.

![Selecting an account to install the app
on](https://b.stripecdn.com/docs-statics-srv/assets/account-selection.13dde83d3b3b16c9d0faee76b98e584b.png)

Install link account selection

[Redirecting to your
site](https://docs.stripe.com/stripe-apps/install-links#redirect)
After the user installs your app, they’re redirected to the `redirect_uri` URL
parameter that matches a defined redirect in `allowed_redirect_uris` in your app
manifest.

### Successful installation

For successful installations, the URL includes:

- The `user_id` value. The ID of the Stripe user that initiated the install.
- The `account_id` value. The ID of the Stripe account that installed your app.
- The `state` value, if provided
- The `install_signature` value. This a hash of the above values that’s
generated using your app’s [signing
secret](https://docs.stripe.com/stripe-apps/build-backend#expire-and-create-secrets).
- If the app is installed into test mode, a `livemode=false` value is appended
to the redirect URL.

*An example of a live mode redirect:*

```

https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}
```

*An example of a test mode redirect:*

```

https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}&livemode=false
```

### Installation failure

If the user cancels the installation, they will still be redirected to your
site, but the URL includes an error instead:

```

https://example.com/callback/stripe?error=access_denied&error_description=The%20user%20denied%20your%20request
```

The user is now connected to your app. Store the `stripe_user_id` in your
database—this is the user’s Stripe account ID. You’ll use this value to
[authenticate as the connected
account](https://docs.stripe.com/connect/authentication) by passing it into
requests in the `Stripe-Account` header.

### Verify app installs with install_signature Recommended

It’s important to verify that your app’s user was authorized to install the app
for the account provided in the redirect URL. An `install_signature` is included
for this reason. This signature is generated from your app’s [signing
secret](https://docs.stripe.com/stripe-apps/build-backend#expire-and-create-secrets)
and the `user_id` and `account_id` that completed the install. The signature
also includes the passed `state`, if provided. The signature can’t be replicated
without access to the signing secret, which is only available internally to
Stripe and to your app’s backend. Because of this, bad actors can’t replicate
the hash if they were to try and spoof the redirect URL. By verifying the app
signature, you can trust that the account is associated with your app user.

To verify the signature, follow these steps:

- [Create your app’s signing
secret](https://docs.stripe.com/stripe-apps/build-backend#expire-and-create-secrets)
if you haven’t done so already.
- [Setup an app
backend](https://docs.stripe.com/stripe-apps/build-backend#send-a-signed-request)
to verify the `install_signature`.

#### Sample backend verifying the install:

The order and naming of the payload fields matter when performing signature
verification. The `state` precedes the `user_id`, which precedes the
`account_id`. The resulting object should be `{ state, user_id, account_id }`.

```
require 'stripe'
require 'sinatra'
require 'json'

Stripe.api_key = 'API_KEY'

get '/' do
 'Install Links verification example'
end

get '/verify' do
 user_id = params[:user_id]
 account_id = params[:account_id]
 state = params[:state]
 install_signature = params[:install_signature]

 payload = JSON.dump({
 state: state,
 user_id: user_id,
 account_id: account_id
 })

 begin
 Stripe::Webhook::Signature.verify_header(
 payload,
 install_signature,
 'STRIPE_APP_SECRET'
 )
 rescue Stripe::SignatureVerificationError => e
 return e.message, 400
 end

 { success: true }.to_json
end

set :port, 3000
```

After it’s verified, you can [make API
calls](https://docs.stripe.com/stripe-apps/build-backend#using-stripe-apis) on
behalf of the installed account.

[Make authenticated
requests](https://docs.stripe.com/stripe-apps/install-links#authenticated-requests)
For server-side API calls, you can make requests as connected accounts using the
special header `Stripe-Account` with the Stripe account identifier (it starts
with the prefix `acct_`) of your platform user. Here’s an example that shows how
to [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)
with your platform’s [API secret key](https://docs.stripe.com/keys) and your
user’s [Account](https://docs.stripe.com/api/accounts) identifier.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card
```

The `Stripe-Account` header approach is implied in any API request that includes
the Stripe account ID in the URL. Here’s an example that shows how to [Retrieve
an account](https://docs.stripe.com/api/accounts/retrieve) with your user’s
[Account](https://docs.stripe.com/api/accounts) identifier in the URL.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

See more examples of making an [authenticated request
here](https://docs.stripe.com/connect/authentication).

## Customize links with URL parameters

You can change the behavior of the app installation by including additional URL
parameters in the install link.

### Supported URL parameters

ParameterDescription`redirect_uri`The URL that users are redirected to after
installing your app. If provided, this must exactly match one of the
comma-separated `redirect_uris` values in your [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest). To
protect yourself from certain man-in-the-middle attacks, the live mode
`redirect_uri` must use a secure HTTPS connection.`state`RecommendedAn arbitrary
string value we pass back to you, which is recommended for CSRF protection.
### Prevent CSRF attacks with the state parameter

To prevent cross-site request forgery (CSRF) attacks, you can use the `state`
parameter. This parameter accepts any string value and returns it unmodified
upon redirecting the installer back to your application or platform. To use this
parameter, pass a unique and non-guessable value when you initiate an install
using an install link. Save the value to use it for verification later.

After the user installs and is redirected back to your application, verify
whether the value of the state parameter provided matches the value present in
the initial install link. This verification process provides a high-level of
confidence to confirm that the `stripe_user_id` returned belongs to the user who
initiated the install and safeguard against potential forgeries.

## Revoking access

An `account.application.deauthorized`
[event](https://docs.stripe.com/api#list_events) occurs when a user disconnects
your app from their account. You can perform any necessary cleanup on your
servers by watching for this event with
[webhooks](https://docs.stripe.com/connect/webhooks).

## See also

- [How Stripe Apps
work](https://docs.stripe.com/stripe-apps/how-stripe-apps-work)
- [Full API reference](https://docs.stripe.com/api)

## Links

- [upload a new version](https://docs.stripe.com/stripe-apps/upload-install-app)
- [https://example.com/callback/stripe](https://example.com/callback/stripe)
- [external testing](https://docs.stripe.com/stripe-apps/test-app)
- [Publish a new version](https://docs.stripe.com/stripe-apps/publish-app)
- [signing
secret](https://docs.stripe.com/stripe-apps/build-backend#expire-and-create-secrets)
-
[https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}](https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE})
-
[https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}&livemode=false](https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}&livemode=false)
-
[https://example.com/callback/stripe?error=access_denied&error_description=The%20user%20denied%20your%20request](https://example.com/callback/stripe?error=access_denied&error_description=The%20user%20denied%20your%20request)
- [authenticate as the connected
account](https://docs.stripe.com/connect/authentication)
- [Setup an app
backend](https://docs.stripe.com/stripe-apps/build-backend#send-a-signed-request)
- [make API
calls](https://docs.stripe.com/stripe-apps/build-backend#using-stripe-apis)
- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)
- [API secret key](https://docs.stripe.com/keys)
- [Account](https://docs.stripe.com/api/accounts)
- [Retrieve an account](https://docs.stripe.com/api/accounts/retrieve)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [event](https://docs.stripe.com/api#list_events)
- [webhooks](https://docs.stripe.com/connect/webhooks)
- [How Stripe Apps
work](https://docs.stripe.com/stripe-apps/how-stripe-apps-work)
- [Full API reference](https://docs.stripe.com/api)