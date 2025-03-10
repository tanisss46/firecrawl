# Add server-side logic

## Validate and process user actions and data in your app using backend code.

With Stripe Apps, you can add server-side logic with a self-hosted backend. With
a self-hosted backend service, you can:

- Integrate securely with third-party systems that require a server-side
integration.
- Subscribe to [webhook](https://docs.stripe.com/webhooks) events from Stripe
and synchronize Stripe with other systems.
- Use long-lived app logic that executes when the user closes the browser.
- Build apps that provide cron-job-like functionality to schedule specific
actions.

![App backend
flowchart](https://b.stripecdn.com/docs-statics-srv/assets/app-backend.46a6d040d44872962a59728aaa65ee06.png)

How the self-hosted backend relates to the app

## Authenticate users from your UI to your app’s back end

To authenticate a user from the Dashboard, the backend needs a signature with
the shared secret and the account and user ID of the current, signed-in
Dashboard user. If your user doesn’t have permission to call the API, Stripe
returns a [Permission
error](https://docs.stripe.com/error-handling?lang=node#permission-errors).

## Before you begin

- Make sure your backend service can send and receive HTTP requests. If you
haven’t built an API server before, consider trying the [interactive webhook
endpoint builder](https://docs.stripe.com/webhooks/quickstart).
- Create your shared secret by [uploading your
app](https://docs.stripe.com/stripe-apps/upload-install-app):

```
stripe apps upload
```

Don’t worry if you haven’t finished developing the current version of your app,
uploading won’t update your app in live mode.
- Get your app’s secret to verify the signature in your backend:

a. Go to your Stripe app details page by selecting your app from
[Apps](https://dashboard.stripe.com/apps).

b. Under the application ID, click the overflow menu (), then click **Signing
secret** to open the signing secret dialog.

c. Click the clipboard to copy your app’s secret from the signing secret dialog.

### Send a signed request

![Sending a signed
request](https://b.stripecdn.com/docs-statics-srv/assets/authenticate-ui-extension.9e45231756741ade2e1a73f56585864c.png)

To send a signed request to the app’s backend:

- Get the current signature using the
[fetchStripeSignature](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#fetchStripeSignature)
asynchronous function.
- Add the signature to the `Stripe-Signature` header.
- Include the `user_id` and `account_id` objects in the request.
- On the app’s backend, verify that the request includes the signature, app
secret, `user_id`, and `account_id`.

See an [example of sending a signed request with additional
data](https://docs.stripe.com/stripe-apps/build-backend#send-a-signed-request-with-additional-data).

An example request from a Stripe app with the `Stripe-Signature` header:

```
import {fetchStripeSignature} from '@stripe/ui-extension-sdk/utils';

const App = ({ userContext, environment }: ExtensionContextValue) => {
 const makeRequestToMyBackend = async (endpoint, requestData) => {
 // By default the signature is signed with user id and account id.
 const signaturePayload = {
 user_id: userContext?.id,
 account_id: userContext?.account.id,
 };
 return fetch(`https://example.com/${endpoint}/`, {
 method: 'POST',
 headers: {
 'Stripe-Signature': await fetchStripeSignature(),
 'Content-Type': 'application/json',
 },
 // Include the account ID and user ID in the body to verify on backend.
 body: JSON.stringify({
 ...requestData,
 ...signaturePayload,
 }),
 });
 };
 ...
}
```

Sample backend verifying the request:

Please be aware that the order and naming of the payload fields matters when
performing signature verification. The `user_id` precedes the `account_id` and
the resulting object is as follows: `{ user_id, account_id }`

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')(process.env.STRIPE_API_KEY);
const express = require('express');

// Find your app's secret in your app settings page in the Developers Dashboard.
const appSecret = 'absec_...';

// This example uses Express.
const app = require('express')();
app.use(express.json());

// Match the raw body to content type application/json.
app.post('/do_secret_stuff', (request, response) => {
 const sig = request.headers['stripe-signature'];
 // Retrieve user id and account id from the request body
 const payload = JSON.stringify({
 user_id: request.body['user_id'],
 account_id: request.body['account_id']
 });
 try {
 // Verify the payload and signature from the request with the app secret.
 stripe.webhooks.signature.verifyHeader(payload, sig, appSecret);
 } catch (error) {
 response.status(400).send(error.message);
 }
 // Handle the request by returning a response
 // to acknowledge receipt of the event.
 response.json({ success: true });
});

app.listen(3000, () => console.log('Running on port 3000'));
```

### Send a signed request with additional data

You can authenticate a user by sending a signed request with a payload
(additional data). When you call the `fetchStripeSignature` function with an
additional payload request, you create a signature with `user_id`, `account_id`
and the additional payload you passed into the function. By default, Stripe apps
use `user_id` and `account_id` to generate the signature string.

An example of generating a secret with additional payload:

```
// A valid payload object has keys of type string
// and values of type string, number, or boolean.
const payload = {
 "transaction_id": 'ipi_1KRmFUFRwUQjTSJEjRnCCPyV',
 "amount": 100,
 "livemode": false,
};

fetch(`https://example.com/do_more_secret_stuff/`, {
 method: 'POST',
 headers: {
 'Stripe-Signature': await fetchStripeSignature(payload),
 'Content-Type': 'application/json',
 },
 // Append the account ID and user ID in the body to verify on backend.
 body: JSON.stringify({
 ...payload,
 user_id: 'usr_K6yd2CbXLO9A5G',
 account_id: 'acct_1JSkf6FRwUQjTSJE',
 }),
});
```

Sample backend verifying the signature generated with additional payload:

```
// Match the raw body to content type application/json.
app.post('/do_more_secret_stuff', (request, response) => {
 try {
 // Verify the signature from the header and the request body that
// contains the additional data, user ID, and account ID with the app secret.
 stripe.webhooks.signature.verifyHeader(request.body, sig, appSecret);
 } catch (error) {
 response.status(400).send(error.message);
 }
 // Handle the request by returning a response
 // to acknowledge receipt of the event.
 response.json({ success: true });
});
```

### Verify user roles (optional)

You can verify the user roles assigned to a given `user_id` by including the
`stripe_roles` key in the payload. Provide this with `userContext?.roles`, which
returns a list of
[RoleDefinitions](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#roledefinition).
If any role in the payload isn’t assigned to the `user_id` provided,
`fetchStripeSignature` returns an invalid request error (400).

```
// Provide this special key in the same way you'd
// provide any other key to the additional payload.
const payload = {
 "stripe_roles": userContext?.roles,
};

fetch(`https://example.com/do_more_secret_stuff/`, {
 method: 'POST',
 headers: {
 'Stripe-Signature': await fetchStripeSignature(payload),
 'Content-Type': 'application/json',
 },
 // Append the account ID and user ID in the body to verify on backend.
 body: JSON.stringify({
 ...payload,
 user_id: 'usr_K6yd2CbXLO9A5G',
 account_id: 'acct_1JSkf6FRwUQjTSJE',
 }),
});
```

### Expire and create secrets

If your secret is compromised, you can expire your current app’s secret
immediately for up to 24 hours to update the app’s secret on your backend.
During this time, two secrets are active for the endpoint, the compromised
secret and the newly generated secret. Stripe generates one signature per secret
until expiration.

To expire and create an app secret:

- Go to your Stripe app details page by selecting your app from
[Apps](https://dashboard.stripe.com/apps).
- On the page header, click the overflow menu (), then click **Signing secret**
to open the Signing secret dialog.
- Click **Expire secret** from the signing secret dialog to open the Expire
secret dialog.
- Select an expiration duration for your current’s app secret.
- Click **Expire secret**.

### Handle Cross-Origin Resource Sharing (CORS)

[Cross-Origin Resource Sharing
(CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is an important
part of helping keep apps secure from [cross-site scripting attacks
(XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).
Because Stripe App UI extensions are, by necessity, cross-origin and sandboxed,
you must employ a specific approach to handling cross-origin request headers.

For your UI extension to retrieve data from your backend service, you must
configure your backend service to do the following:

- Allow requests using the [Options
method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS).
- To allow requests from `null` origins, set the `Access-Control-Allow-Origin`
to `*`.

#### Note

UI extensions have a null origin because they run in a sandbox for security
purposes.

Many backend frameworks have libraries and guidance to help you handle CORS.
Check the documentation for your framework for more specific guidance.

To authenticate that a request came from Stripe on behalf of a particular user
or account, see [Authenticate users from your UI to your
backend](https://docs.stripe.com/stripe-apps/build-backend#authenticate-ui-to-backend).

#### Caution

Only configure authenticated endpoints and any endpoints the UI extension
communicates with to use `Access-Control-Allow-Origin: *`. Unauthenticated
endpoints are vulnerable to
[CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF) attacks if no
other measures are in place.

## Use Stripe APIs

To interact with Stripe, you can use and authenticate your requests to the
Stripe API.

### Authenticating requests

To authenticate your requests, use your existing merchant account API key to
interact with Stripe and specify the user’s `stripeAccountId`.

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

In addition, all of Stripe’s server-side libraries support this approach on a
per-request basis, as shown in the following example:

```
Stripe.api_key = "{{PLATFORM_SECRET_KEY}}"
Stripe::Customer.create(
 {email: 'person@example.edu'},
 {stripe_account: '{{CONNECTED_STRIPE_ACCOUNT_ID}}'}
)

# Fetching an account just needs the ID as a parameter
Stripe::Account.retrieve('{{CONNECTED_STRIPE_ACCOUNT_ID}}')
```

### Call your self-hosted backend from your UI extension

When you make requests from your UI extension to your backend, [send a signature
with your
request](https://docs.stripe.com/stripe-apps/build-backend#authenticate-ui-to-backend)
to validate the legitimacy of the requests. From the UI extension, pass the
`stripeAccountId` for the current user so that you can make backend requests on
behalf of that user.

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');
const express = require("express");
const app = express();

app.use(express.static("public"));
app.use(express.json());

app.post("/api/data", async (req, res) => {
 const { stripeAccountId } = req.body;

 const customer = await stripe.customers.create({
 description: 'My First Test Customer (created for API docs)',
 }, {
 stripeAccount: stripeAccountId,
 });

 res.send({
 data: []
 });
});

app.listen(3000, () => console.log("Node server listening on port 3000!"));
```

## Call other APIs

From your self-hosted backend, you can call any API—your own API or one built by
another developer or company.

For more information, learn how to [store secret credentials and tokens in your
app](https://docs.stripe.com/stripe-apps/store-secrets).

If you need to pass user information from Stripe to another service, use the
`stripeAccountId` passed from your UI extension.

```
const express = require('express');
const fetch = require('isomorphic-fetch');
const app = express();

app.use(express.static('public'));
app.use(express.json());

app.get('/api/time', async (req, res) => {
 fetch('http://worldclockapi.com/api/json/est/now')
 .then((response) => response.json())
 .then((data) => {
 res.send({
 data: data,
 });
 });
});

app.listen(3000, () => console.log('Node server listening on port 3000!'));
```

You can also [call a third-party API from your UI
extension](https://docs.stripe.com/stripe-apps/build-ui#use-third-party-apis).

## Receive event notifications about your app

Listen for events (such as user installs or uninstalls) on your Stripe app using
incoming [webhooks](https://docs.stripe.com/webhooks) so your integration can
automatically trigger reactions in your backend such as:

- Creating user accounts
- Updating permissions
- Disabling a user’s account and removing data

### Receive events

You can receive events from Stripe for an app that’s private to your account
only or an app that’s listed on the [App
Marketplace](https://marketplace.stripe.com/):

Public listing on App MarketplacePrivate to your account
To receive events for an app that’s listed publicly on the [App
Marketplace](https://marketplace.stripe.com/):

- [Handle webhook events in your app’s
backend](https://docs.stripe.com/webhooks#webhook-endpoint-def).
- [Register a webhook
endpoint](https://docs.stripe.com/webhooks#webhooks-summary) in the Stripe
Dashboard, and select **Listen to events on Connected accounts** when
registering your webhook endpoint.
- Add the `event_read` permission to your app:
```
stripe apps grant permission "event_read" "Allows reading event data from users
who have installed the app"
```
- For each event that your webhook endpoint is listening to, add the
corresponding permission:
```
stripe apps grant permission "PERMISSION_NAME" "EXPLANATION"
```

Replace:- `PERMISSION_NAME` with the [permission name for an
event](https://docs.stripe.com/stripe-apps/reference/permissions).
- `EXPLANATION` with an explanation for enabling access. Users see this
explanation when they install your app. For example: “Allows reading event data
from users who have installed the app.”

When a merchant triggers an event, Stripe provides the following
[Event](https://docs.stripe.com/api/events/object) object. This event includes
the `account` property specifying the account ID of the merchant who triggers
the event:

```
{
 "id": "evt_",
 "livemode": true,
 "object": "event",
 "type": "account.application.authorized",
 "account": "acct_",
 "pending_webhooks": 2,
 "created": 1349654313,
 "data": {...}
}
```

Using the `account` attribute, you can do the following:

- Monitor how many merchants install and uninstall your app.
- [Make API calls on behalf of users with Stripe
Connect](https://docs.stripe.com/connect/authentication).

### Events for Stripe Apps

In addition to the [types of events Stripe
supports](https://docs.stripe.com/api/events/types), Stripe Apps also supports
the following events:

Merchant actionResulting webhook event sent to the app’s backendConnect or
install your
app[account.application.authorized](https://docs.stripe.com/api/events/types#event_types-account.application.authorized)Disconnect
or uninstall your
app[account.application.deauthorized](https://docs.stripe.com/api/events/types#event_types-account.application.deauthorized)
## Event behavior depends on install mode

Your users can install in either live mode, test mode, both modes, or a sandbox.
Set webhooks according to the following guidelines:

- If the app is installed in a sandbox, events are sent to the sandbox only.
- If the app is installed in live mode only, live mode events are sent to the
live mode endpoint.
- If the app is installed in test mode only, test mode events are sent to the
test mode endpoint.
- If the app is installed in both modes, test mode events are sent to both the
test mode and live mode endpoints, and live mode events are sent to the live
mode endpoint.

Configure the Connect `/webhook` for live and test modes, then use the following
snippet for both modes of the app. See the [webhooks
doc](https://docs.stripe.com/webhooks#example-endpoint) for a full endpoint
example.

```
require 'sinatra'
require 'json'

post '/webhook' do
 event = JSON.parse(request.body.read)

 if event['livemode']
 puts "Handling live event: #{event}"
 # Handle live events
 handle_live_event(event)
 else
 puts "Handling test event: #{event}"
 # Handle test events
 handle_test_event(event)
 end

 status 200
 body 'Event received'
end
```

### Troubleshooting

If you don’t receive expected events, review your configuration for the
following common oversights:

- Make sure live mode webhooks use live mode keys and test mode webhooks use
test mode keys.
- For live mode events, make sure the installing account is activated.
- Make sure that your app can handle both live mode & test mode events.
- Triggering test events doesn’t replicate live event behavior unless explicitly
set up in the app configuration.

### Test webhooks locally

You can test webhooks locally for:

- An app that’s only available to all users on your account and listens to
events on your own account
- An app that’s available on the Stripe App Marketplace and listens to events on
accounts that have installed your app

To test webhooks locally:

- [Install the Stripe CLI](https://docs.stripe.com/stripe-cli).
- Authenticate your account:

```
stripe login
```
- Open two terminal windows:

- In one terminal window, [Set up event
forwarding](https://docs.stripe.com/webhooks#local-listener):

Private to your account onlyPublic listing on App Marketplace
```
stripe listen --forward-to localhost:{{PORT}}/webhook
```
- In the other terminal window, [Trigger events to test your webhooks
integration](https://docs.stripe.com/webhooks#trigger-test-events):

Private to your account onlyPublic listing on App Marketplace
```
stripe trigger {{EVENT_NAME}}
```

For more information, see our docs on [testing a webhook
endpoint](https://docs.stripe.com/webhooks#local-listener).

## See also

- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)
- [Upload and install your
app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [Publish your app](https://docs.stripe.com/stripe-apps/publish-app)

## Links

- [webhook](https://docs.stripe.com/webhooks)
- [Permission
error](https://docs.stripe.com/error-handling?lang=node#permission-errors)
- [interactive webhook endpoint
builder](https://docs.stripe.com/webhooks/quickstart)
- [uploading your app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [Apps](https://dashboard.stripe.com/apps)
-
[fetchStripeSignature](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#fetchStripeSignature)
- [example of sending a signed request with additional
data](https://docs.stripe.com/stripe-apps/build-backend#send-a-signed-request-with-additional-data)
- [https://example.com/${endpoint}/`,](https://example.com/${endpoint}/`,)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://example.com/do_more_secret_stuff/`,](https://example.com/do_more_secret_stuff/`,)
-
[RoleDefinitions](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#roledefinition)
- [Cross-Origin Resource Sharing
(CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [cross-site scripting attacks
(XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting)
- [Options
method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)
- [Authenticate users from your UI to your
backend](https://docs.stripe.com/stripe-apps/build-backend#authenticate-ui-to-backend)
- [CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)
- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)
- [API secret key](https://docs.stripe.com/keys)
- [Account](https://docs.stripe.com/api/accounts)
- [Retrieve an account](https://docs.stripe.com/api/accounts/retrieve)
- [store secret credentials and tokens in your
app](https://docs.stripe.com/stripe-apps/store-secrets)
-
[http://worldclockapi.com/api/json/est/now](http://worldclockapi.com/api/json/est/now)
- [call a third-party API from your UI
extension](https://docs.stripe.com/stripe-apps/build-ui#use-third-party-apis)
- [App Marketplace](https://marketplace.stripe.com)
- [Handle webhook events in your app’s
backend](https://docs.stripe.com/webhooks#webhook-endpoint-def)
- [Register a webhook
endpoint](https://docs.stripe.com/webhooks#webhooks-summary)
- [permission name for an
event](https://docs.stripe.com/stripe-apps/reference/permissions)
- [Event](https://docs.stripe.com/api/events/object)
- [Make API calls on behalf of users with Stripe
Connect](https://docs.stripe.com/connect/authentication)
- [types of events Stripe supports](https://docs.stripe.com/api/events/types)
-
[account.application.authorized](https://docs.stripe.com/api/events/types#event_types-account.application.authorized)
-
[account.application.deauthorized](https://docs.stripe.com/api/events/types#event_types-account.application.deauthorized)
- [webhooks doc](https://docs.stripe.com/webhooks#example-endpoint)
- [Install the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Set up event forwarding](https://docs.stripe.com/webhooks#local-listener)
- [Trigger events to test your webhooks
integration](https://docs.stripe.com/webhooks#trigger-test-events)
- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)
- [Publish your app](https://docs.stripe.com/stripe-apps/publish-app)