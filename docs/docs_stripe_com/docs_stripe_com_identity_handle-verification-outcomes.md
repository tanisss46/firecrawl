# Handle verification outcomes

## Listen for verification results so your integration can automatically trigger reactions.

You wrote code to [display a modal to collect identity
documents](https://docs.stripe.com/identity/verify-identity-documents). Now,
when your user submits a document, you can listen to verification results to
trigger reactions in your application.

In this guide, you’ll learn how to:

- Receive an event notification when a verification finishes processing.
- Handle successful and failed verification checks.
- Turn your event handler on in production.

[Verification checks](https://docs.stripe.com/identity/verification-checks) are
asynchronous, which means that verification results aren’t immediately
available. When the processing completes, the VerificationSession status updates
and the verified information is available. Stripe generates
[events](https://docs.stripe.com/api/events) every time a session changes
status. In this guide, we’ll implement
[webhooks](https://docs.stripe.com/webhooks) to notify your app when
verification results become available.

See [How sessions work](https://docs.stripe.com/identity/how-sessions-work) to
learn the status and lifecycle of verification sessions.

[Set up
StripeServer-side](https://docs.stripe.com/identity/handle-verification-outcomes#set-up-stripe)
Install our official libraries for access to the Stripe API from your
application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create a webhook and handle VerificationSession
eventsServer-side](https://docs.stripe.com/identity/handle-verification-outcomes#create-webhook)
A [webhook](https://docs.stripe.com/webhooks) is an endpoint on your server that
receives requests from Stripe, notifying you about events that happen on your
account. In this step, we’ll build an endpoint to receive events on
VerificationSession [status
changes](https://docs.stripe.com/identity/how-sessions-work).

Webhook endpoints must be publicly accessible so Stripe can send unauthenticated
requests. You’ll need to verify that Stripe sent the event by using the Stripe
library and request header:

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

// You can find your endpoint's secret in your webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const express = require('express');

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const app = express();

// Use JSON parser for all non-webhook routes
app.use((req, res, next) => {
 if (req.originalUrl === '/webhook') {
 next();
 } else {
 bodyParser.json()(req, res, next);
 }
});

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (req, res) => {
 let event;

 // Verify the event came from Stripe
 try {
 const sig = req.headers['stripe-signature'];
 event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
 } catch (err) {
 // On error, log and return the error message
 console.log(`❌ Error message: ${err.message}`);
 return res.status(400).send(`Webhook Error: ${err.message}`);
 }

 // Successfully constructed event

 res.json({received: true});
});

app.listen(4242, () => {
 console.log('Running on port 4242');
});
```

Now that you have the basic structure and security in place to listen to
notifications from Stripe, update your webhook endpoint to handle verification
session events.

All [session events](https://docs.stripe.com/identity/how-sessions-work#events)
include the
[VerificationSession](https://docs.stripe.com/api/identity/verification_sessions)
object, which contains details about the verification checks performed. See
[Accessing verification
results](https://docs.stripe.com/identity/access-verification-results) to learn
how to retrieve verified information not included in session events.

Stripe sends the following events when the session status changes:

Event nameDescriptionNext
steps[identity.verification_session.verified](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.verified)Processing
of all the [verification
checks](https://docs.stripe.com/identity/verification-checks) have completed,
and they’re all successfully verified.Trigger relevant actions in your
application.[identity.verification_session.requires_input](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.requires_input)Processing
of all the [verification
checks](https://docs.stripe.com/identity/verification-checks) have completed,
and at least one of the checks failed.Trigger relevant actions in your
application and potentially allow your user to retry the verification.
Your webhook code needs to handle the `identity.verification_session.verified`
and `identity.verification_session.requires_input` events. You can subscribe to
other [session
events](https://docs.stripe.com/identity/how-sessions-work#events) to trigger
additional reactions in your app.

### Handle VerificationSession verified status change

The `identity.verification_session.verified` event is sent when verification
checks have completed and are all successfully verified.

Add code to your event handler to handle all verification checks passing:

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

// You can find your endpoint's secret in your webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const express = require('express');

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const app = express();

// Use JSON parser for all non-webhook routes
app.use((req, res, next) => {
 if (req.originalUrl === '/webhook') {
 next();
 } else {
 bodyParser.json()(req, res, next);
 }
});

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (req, res) => {
 let event;

 // Verify the event came from Stripe
 try {
 const sig = req.headers['stripe-signature'];
 event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
 } catch (err) {
 // On error, log and return the error message
 console.log(`❌ Error message: ${err.message}`);
 return res.status(400).send(`Webhook Error: ${err.message}`);
 }

 // Successfully constructed event
 switch (event.type) {
 case 'identity.verification_session.verified': {
 // All the verification checks passed
 const verificationSession = event.data.object;
 break;
 }
 }

 res.json({received: true});
});

app.listen(4242, () => {
 console.log('Running on port 4242');
});
```

When handling this event, you might also consider:

- Saving the verification status in your own database
- Sending an email to your user letting them know they’ve been verified
- [Expanding](https://docs.stripe.com/api/expanding_objects) the
VerificationSession [verified
outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
and comparing them against an expected value.

### Handle VerificationSession requires_input status changes

The `identity.verification_session.requires_input` event is sent when at least
one of the checks failed. You can inspect the
[last_error](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error)
hash on the verification session to handle specific failure reasons:

- The
[last_error.code](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)
field can be used to programmatically handle verification failures.
- The
[last_error.reason](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-reason)
field contains a descriptive message explaining the failure reason and can be
shown to your user.

#### Event error codes

SessionDocumentSelfieID NumberAddress (Invite only)Error
codeDescription`consent_declined`The user declined to be verified by Stripe.
Check with your legal counsel to see if you have an obligation to offer an
alternative, non-biometric means to verify, such as through a manual
review.`under_supported_age`Stripe doesn’t verify users under the age of
majority.`country_not_supported`Stripe doesn’t verify users from the provided
country.
Add code to your event handler to handle verification check failure:

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

// You can find your endpoint's secret in your webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const express = require('express');

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const app = express();

// Use JSON parser for all non-webhook routes
app.use((req, res, next) => {
 if (req.originalUrl === '/webhook') {
 next();
 } else {
 bodyParser.json()(req, res, next);
 }
});

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (req, res) => {
 let event;

 // Verify the event came from Stripe
 try {
 const sig = req.headers['stripe-signature'];
 event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
 } catch (err) {
 // On error, log and return the error message
 console.log(`❌ Error message: ${err.message}`);
 return res.status(400).send(`Webhook Error: ${err.message}`);
 }

 // Successfully constructed event
 switch (event.type) {
 case 'identity.verification_session.verified': {
 // All the verification checks passed
 const verificationSession = event.data.object;
 break;
 }
 case 'identity.verification_session.requires_input': {
 // At least one of the verification checks failed
 const verificationSession = event.data.object;

console.log('Verification check failed: ' +
verificationSession.last_error.reason);

 // Handle specific failure reasons
 switch (verificationSession.last_error.code) {
 case 'document_unverified_other': {
 // The document was invalid
 break;
 }
 case 'document_expired': {
 // The document was expired
 break;
 }
 case 'document_type_not_supported': {
 // document type not supported
 break;
 }
 default: {
 // ...
 }
 }
 }
 }

 res.json({received: true});
});

app.listen(4242, () => {
 console.log('Running on port 4242');
});
```

Depending on your use case, you might want to allow your users to retry the
verification if it fails. We recommend that you limit the amount of submission
attempts.

When handling this event, you might also consider:

- Manually reviewing the collected information
- Sending an email to your user letting them know that their verification failed
- Providing your user an alternative verification method
[Go live in
production](https://docs.stripe.com/identity/handle-verification-outcomes#go-live)
After you’ve deployed your event handler endpoint to production, set up the
endpoint so Stripe knows where to send live mode events. It’s also helpful to go
through the [development
checklist](https://docs.stripe.com/get-started/checklist/go-live) to ensure a
smooth transition when taking your integration live.

Webhook endpoints are configured in the Dashboard or programmatically using the
API.

### Add an endpoint in the Dashboard

In the Dashboard’s [Webhooks settings](https://dashboard.stripe.com/webhooks)
page, click **Add an endpoint** to add a new webhook endpoint. Enter the URL of
your webhook endpoint and select which events to listen to. See the full list of
[Verification Session
events](https://docs.stripe.com/identity/how-sessions-work#events).

### Add endpoint with the API

You can also programmatically [create webhook
endpoints](https://docs.stripe.com/api/webhook_endpoints/create). As with the
form in the Dashboard, you can enter any URL as the destination for events and
which event types to subscribe to.

```
curl https://api.stripe.com/v1/webhook_endpoints \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "url"="https://{{DOMAIN}}/my/webhook/endpoint" \
 -d "enabled_events[]"="identity.verification_session.verified" \
 -d "enabled_events[]"="identity.verification_session.requires_input"
```

## See also

- [Test a webhook endpoint](https://docs.stripe.com/webhooks#test-webhook)
- [How sessions work](https://docs.stripe.com/identity/how-sessions-work)
- [Best practices for using
webhooks](https://docs.stripe.com/webhooks#best-practices)
- [Webhook development
checklist](https://docs.stripe.com/get-started/checklist/go-live)

## Links

- [display a modal to collect identity
documents](https://docs.stripe.com/identity/verify-identity-documents)
- [Verification checks](https://docs.stripe.com/identity/verification-checks)
- [events](https://docs.stripe.com/api/events)
- [webhooks](https://docs.stripe.com/webhooks)
- [How sessions work](https://docs.stripe.com/identity/how-sessions-work)
- [Build a webhook endpoint](https://docs.stripe.com/webhooks/quickstart)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [session events](https://docs.stripe.com/identity/how-sessions-work#events)
-
[VerificationSession](https://docs.stripe.com/api/identity/verification_sessions)
- [Accessing verification
results](https://docs.stripe.com/identity/access-verification-results)
-
[identity.verification_session.verified](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.verified)
-
[identity.verification_session.requires_input](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.requires_input)
- [Expanding](https://docs.stripe.com/api/expanding_objects)
- [verified
outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
-
[last_error](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error)
-
[last_error.code](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)
-
[last_error.reason](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-reason)
- [development checklist](https://docs.stripe.com/get-started/checklist/go-live)
- [Webhooks settings](https://dashboard.stripe.com/webhooks)
- [create webhook
endpoints](https://docs.stripe.com/api/webhook_endpoints/create)
- [Test a webhook endpoint](https://docs.stripe.com/webhooks#test-webhook)
- [Best practices for using
webhooks](https://docs.stripe.com/webhooks#best-practices)