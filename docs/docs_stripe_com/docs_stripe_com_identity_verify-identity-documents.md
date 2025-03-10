# Verify your users’ identity documents

## Create sessions and collect identity documents.

This guide explains how to use Stripe Identity to securely collect and verify
identity documents.

## Before you begin

- [Activate your account](https://dashboard.stripe.com/account/onboarding).
- Fill out your [Stripe Identity
application](https://dashboard.stripe.com/identity/application).
- (Optional) Customize your brand settings on the [branding settings
page](https://dashboard.stripe.com/settings/branding).

WebiOSAndroidReact NativeNo codeModalRedirect
Show a document upload modal inside your website. Here’s what you’ll do:

- Add a verification button to your webpage that displays a document upload
modal.
- Display a confirmation page on identity document submission.
- Handle verification results.
[Set up
StripeServer-side](https://docs.stripe.com/identity/verify-identity-documents#set-up-stripe)
First, [register](https://dashboard.stripe.com/register) for a Stripe account.

Then install the libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Add a button to your
websiteClient-side](https://docs.stripe.com/identity/verify-identity-documents#add-a-button)
Create a button on your website for starting the verification.

HTML + JSReact
### Add a button

Start by adding a verify button to your page:

```
<html>
 <head>
 <title>Verify your identity</title>
 </head>
 <body>
 <button id="verify-button">Verify</button>
 </body>
</html>
```

### Add the Stripe.js library to your page

Add [Stripe.js](https://docs.stripe.com/payments/elements) to your page by
including a script tag in your HTML document:

```
<html>
 <head>
 <title>Verify your identity</title>
 <script src="https://js.stripe.com/v3/"></script>
 </head>
 <body>
 <button id="verify-button">Verify</button>
 </body>
</html>
```

#### Note

Always load **Stripe.js** directly from `https://js.stripe.com`. You can’t
include it in a bundle or self-host it.

### Initialize Stripe.js

Initialize Stripe.js with your publishable [API
key](https://docs.stripe.com/keys) by passing the following JavaScript to your
page:

```
<html>
 <head>
 <title>Verify your identity</title>
 <script src="https://js.stripe.com/v3/"></script>
 </head>
 <body>
 <button id="verify-button">Verify</button>
 <script type="text/javascript">
// Set your publishable key: remember to change this to your live publishable
key in production
 // See your keys here: https://dashboard.stripe.com/apikeys
 var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
 </script>
 </body>
</html>
```

[Show the document upload
modalClient-sideServer-side](https://docs.stripe.com/identity/verify-identity-documents#show-modal)
Set up the new button to show a document upload modal. After clicking the
button, your user can capture and upload a picture of their passport, driver’s
license, or national ID.

The modal reduces development time and maintenance and allows you to collect
identity documents as part of your existing flows. It also decreases the amount
of private information you handle on your site, allows you to support users in a
variety of platforms and languages, and allows you to customize the style to
match your branding.

### Create a VerificationSession

A
[VerificationSession](https://docs.stripe.com/api/identity/verification_sessions)
is the programmatic representation of the verification. It contains details
about the type of verification, such as what
[check](https://docs.stripe.com/identity/verification-checks) to perform. You
can [expand](https://docs.stripe.com/api/expanding_objects) the [verified
outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
field to see details of the data that was verified.

After successfully creating a `VerificationSession`, send the [client
secret](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-client_secret)
to the frontend to show the document upload modal.

!

You need a server-side endpoint to [create the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create).
Creating the `VerificationSession` server-side prevents malicious users from
overriding verification options and incurring processing charges on your
account. Add authentication to this endpoint by including a user reference in
the session metadata or storing the session ID in your database.

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

// In the route handler for /create-verification-session:
// Authenticate your user.

// Create the session.
const verificationSession = await stripe.identity.verificationSessions.create({
 type: 'document',
 provided_details: {
 email: 'user@example.com',
 },
 metadata: {
 user_id: '{{USER_ID}}',
 },
});

// Return only the client secret to the frontend.
const clientSecret = verificationSession.client_secret;
```

#### Caution

The client secret lets your frontend collect sensitive verification information.
It’s single-use and expires after 24 hours. Don’t store it, log it, embed it in
a URL, or expose it to anyone other than the user. Make sure that you have TLS
enabled on any page that includes the client secret. Send only the client secret
to your frontend to avoid exposing verification configuration or results.

Test your endpoint by starting your web server (for example, `localhost:4242`)
and sending a POST request with curl to create a VerificationSession:

```
curl -X POST -is "http://localhost:4242/create-verification-session" -d ""
```

The response in your terminal looks like this:

```
HTTP/1.1 200 OK
Content-Type: application/json

{ id: "vs_QdfQQ6xfGNJR7ogV6", client_secret:
"vs_QdfQQ6xfGNJR7ogV6_secret_live_..." }
```

### Add an event handler to the verify button

Now that you have a button and an endpoint to create a VerificationSession,
modify the button to show the document upload modal when clicked. Add a call to
[verifyIdentity](https://docs.stripe.com/js/identity/modal) using the client
secret:

HTML + JSReact
```
<html>
 <head>
 <title>Verify your identity</title>
 <script src="https://js.stripe.com/v3/"></script>
 </head>
 <body>
 <button id="verify-button">Verify</button>

 <script type="text/javascript">
// Set your publishable key: remember to change this to your live publishable
key in production
 // See your keys here: https://dashboard.stripe.com/apikeys
 var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

 var verifyButton = document.getElementById('verify-button');

 verifyButton.addEventListener('click', function() {
 // Get the VerificationSession client secret using the server-side
 // endpoint you created in step 3.
 fetch('/create-verification-session', {
 method: 'POST',
 })
 .then(function(response) {
 return response.json();
 })
 .then(function(session) {
 // Show the verification modal.
 return stripe.verifyIdentity(session.client_secret);
 })
 .then(function(result) {
 // If `verifyIdentity` fails, you should display the localized
 // error message to your user using `error.message`.
 if (result.error) {
 alert(result.error.message);
 }
 })
 .catch(function(error) {
 console.error('Error:', error);
 });
 });
 </script>
 </body>
</html>
```

### Event error codes

Error codeDescription`consent_declined`The user declined verification by Stripe.
Check with your legal counsel to see if you have an obligation to offer an
alternative, non-biometric means to verify, such as through a manual
review.`device_unsupported`The verification requires a camera and the user is on
a device without one.`under_supported_age`Stripe doesn’t verify users under the
age of majority.`phone_otp_declined`The user is unable to verify the provided
phone number.`email_verification_declined`The user is unable to verify the
provided email address.
### Test the upload modal

Test that the verify button shows a document upload modal:

- Click the verify button, which opens the Stripe document upload modal.
- Ensure no error messages are shown.

If your integration isn’t working:

- Open the Network tab in your browser’s developer tools.
- Click the verify button to see if it makes an XHR request to your server-side
endpoint (`POST /create-verification-session`).
- Verify that the request returns a 200 status.
- Use `console.log(session)` inside your button click listener to confirm that
it returns the correct data.
[Show a confirmation
pageClient-side](https://docs.stripe.com/identity/verify-identity-documents#show-confirmation-page)
To provide a user-friendly experience, show a confirmation page after users
successfully submit their identity document. Host the page on your site to let
the user know that the verification is processing.

HTML + JSReact
Create a minimal confirmation page:

```
<html>
 <head><title>Your document was submitted</title></head>
 <body>
 <h1>Thanks for submitting your identity document.</h1>
 <p>
 We are processing your verification.
 </p>
 </body>
</html>
```

Next, update the button handler to redirect to this page:

```
<html>
 <head>
 <title>Verify your identity</title>
 <script src="https://js.stripe.com/v3/"></script>
 </head>
 <body>
 <button id="verify-button">Verify</button>

 <script type="text/javascript">
// Set your publishable key: remember to change this to your live publishable
key in production
 // See your keys here: https://dashboard.stripe.com/apikeys
 var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx')

 var verifyButton = document.getElementById('verify-button');

 verifyButton.addEventListener('click', function() {
 // Get the VerificationSession client secret using the server-side
 // endpoint you created in step 3.
 fetch('/create-verification-session', {
 method: 'POST',
 })
 .then(function(response) {
 return response.json();
 })
 .then(function(session) {
 // Show the verification modal.
 return stripe.verifyIdentity(session.client_secret);
 })
 .then(function(result) {
 // If `verifyIdentity` fails, you should display the error message
 // using `error.message`.
 if (result.error) {
 alert(result.error.message);
 } else {
 window.location.href = 'submitted.html';
 }
 })
 .catch(function(error) {
 console.error('Error:', error);
 });
 });
 </script>
 </body>
</html>
```

### Test the confirmation page

Test that your confirmation page works:

- Click your verify button.
- Submit the session by selecting a predefined test case.
- Confirm that the new confirmation page is shown.
- Test the entire flow for failure cases (such as declining consent or refusing
camera permissions) and ensure your app handles them without any issues.

Next, find the verification in the Stripe Dashboard. Verification sessions
appear in the Dashboard’s [list of
VerificationSessions](https://dashboard.stripe.com/identity). Click a session to
go to the Session Detail page. The summary section contains verification
results, which you can use in your app.

[Handle verification
events](https://docs.stripe.com/identity/verify-identity-documents#handle-verification-events)
[Document
checks](https://docs.stripe.com/identity/verification-checks#document-availability)
are typically completed as soon as the user redirects back to your site and you
can retrieve the result from the API immediately. In some rare cases, the
document verification isn’t ready yet and must continue asynchronously. In these
cases, you’re notified through webhooks when the verification result is ready.
After the processing completes, the VerificationSession [status
changes](https://docs.stripe.com/identity/how-sessions-work) from `processing`
to `verified`.

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
Use a [webhook
handler](https://docs.stripe.com/identity/handle-verification-outcomes) to
receive these events and automate actions like sending a confirmation email,
updating the verification results in your database, or completing an onboarding
step. You can also view [verification events in the
Dashboard](https://dashboard.stripe.com/events?type=identity.%2A).

## Receive events and run business actions

### With code

Build a webhook handler to listen for events and build custom asynchronous
verification flows. Test and debug your webhook integration locally with the
Stripe CLI.

[Build a custom
webhook](https://docs.stripe.com/identity/handle-verification-outcomes)

### Without code

Use the Dashboard to view all your verifications, inspect collected data, and
understand verification failures.

[View your test verifications in the
Dashboard](https://dashboard.stripe.com/test/identity/verification-sessions)

## See also

- [Handle verification
outcomes](https://docs.stripe.com/identity/handle-verification-outcomes)
- [Learn about
VerificationSessions](https://docs.stripe.com/identity/verification-sessions)
- [Learn about Stripe.js](https://docs.stripe.com/payments/elements)

## Links

- [Activate your account](https://dashboard.stripe.com/account/onboarding)
- [Stripe Identity
application](https://dashboard.stripe.com/identity/application)
- [branding settings page](https://dashboard.stripe.com/settings/branding)
- [register](https://dashboard.stripe.com/register)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [API key](https://docs.stripe.com/keys)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[VerificationSession](https://docs.stripe.com/api/identity/verification_sessions)
- [check](https://docs.stripe.com/identity/verification-checks)
- [expand](https://docs.stripe.com/api/expanding_objects)
- [verified
outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
- [client
secret](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-client_secret)
-
[verification_flow](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-verification_flow)
- [Verification flows
guide](https://docs.stripe.com/identity/verification-flows)
- [create the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create)
- [verifyIdentity](https://docs.stripe.com/js/identity/modal)
- [list of VerificationSessions](https://dashboard.stripe.com/identity)
- [Document
checks](https://docs.stripe.com/identity/verification-checks#document-availability)
- [status changes](https://docs.stripe.com/identity/how-sessions-work)
-
[identity.verification_session.verified](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.verified)
-
[identity.verification_session.requires_input](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.requires_input)
- [webhook
handler](https://docs.stripe.com/identity/handle-verification-outcomes)
- [verification events in the
Dashboard](https://dashboard.stripe.com/events?type=identity.%2A)
- [View your test verifications in the
Dashboard](https://dashboard.stripe.com/test/identity/verification-sessions)
- [Learn about
VerificationSessions](https://docs.stripe.com/identity/verification-sessions)