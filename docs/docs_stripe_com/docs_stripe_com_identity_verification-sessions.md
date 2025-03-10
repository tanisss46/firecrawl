# The Verification Sessions API

## Learn more about the Verification Sessions API that powers Stripe Identity.

Use the [Verification Session
API](https://docs.stripe.com/api/identity/verification_sessions) to securely
collect information and perform [verification
checks](https://docs.stripe.com/identity/verification-checks). This API tracks a
verification, from initial creation through the entire verification process, and
shows verification results upon completion.

For a step-by-step guide on using the Verification Session API to verify your
users’ identity document, follow the related guide: [Verify your users’ identity
documents](https://docs.stripe.com/identity/verify-identity-documents).

## Creating a VerificationSession

When you [create the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create),
determine which [verification
check](https://docs.stripe.com/identity/verification-checks) to perform by
specifying the session
[type](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-type):

- [document](https://docs.stripe.com/identity/verification-checks?type=document)
- Verify the authenticity and ownership of government-issued identity documents.
Can also include a [selfie check](https://docs.stripe.com/identity/selfie).
-
[id_number](https://docs.stripe.com/identity/verification-checks?type=id-number)
- Verify a user’s name, date of birth and national ID number.

```
curl https://api.stripe.com/v1/identity/verification_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=document
```

### Best practices

If the verification process is interrupted and resumes later, attempt to reuse
the same VerificationSession instead of creating a new one. Each
VerificationSession has a unique ID that you can use to
[retrieve](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
it. In your application’s data model, you can store the VerificationSession’s ID
to facilitate retrieval.

The benefit of reusing the VerificationSession is that the object helps track
any failed verification attempts. If any of the checks fail, the
VerificationSession will have a `requires_input` status.

We recommend that you provide an [idempotency
key](https://docs.stripe.com/api/idempotent_requests) when creating the
VerificationSession to avoid erroneously creating duplicate VerificationSessions
for the same person. This key is typically based on the ID that you associate
with the verification in your application, like a user reference.

## Passing the client secret to the frontend

The VerificationSession contains a [client
secret](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-client_secret),
a key that’s unique to the individual VerificationSession. The front end uses
the client secret to complete the verification.

To use the client secret, you must obtain it from the VerificationSession on
your server and pass it to the frontend. You can retrieve the client secret from
an endpoint on your server using the browser’s `fetch` function on the client.
This approach is generally most suitable when the client is a single-page
application, especially one built with a modern frontend framework such as
React.

This example shows how to create the server endpoint that serves the client
secret:

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

This example demonstrates how to fetch the client secret with JavaScript on the
client side:

```
(async () => {
 const response = await fetch('/create-verification-session');
 const {client_secret: clientSecret} = await response.json();
 // Call stripe.verifyIdentity() with the client secret.
})();
```

#### Note

The client secret is a sensitive token that you can use to complete the
verification. Don’t log it, embed it in URLs, or expose it to anyone but the
user that you’re verifying. Make sure that you have
[TLS](https://docs.stripe.com/security/guide#tls) on any page that includes the
client secret.

## Accessing verification results

Submitting and processing a VerificationSession updates the session `status` and
creates a
[VerificationReport](https://docs.stripe.com/api/identity/verification_reports/object)
object. This normally happens within a few minutes.

Once all of the verification checks have passed, the status changes to
`verified`. You can [expand](https://docs.stripe.com/api/expanding_objects) the
[verified_outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
field to see the verified data.

```
{
 "id": "vs_",
 "object": "identity.verification_session",
 "created": 1610744321,
 "last_error": null,
 "last_verification_report": "vr_",
 "livemode": true,
 "metadata": {},
 "options": {
 "document": {},
 },
 "status": "verified",
 "type": "document",
 "redaction": null,
 "url": null,
 "verified_outputs": {
 "first_name": "Jenny",
 "last_name": "Rosen",
 "address": {
 "line1": "1234 Main St.",
 "city": "San Francisco",
 "state": "CA",
 "postal_code": "94111",
 "country": "US"
 },
 "id_number_type": null
 }
}
```

If any of the verification checks fail, the session will have a `requires_input`
[status](https://docs.stripe.com/identity/how-sessions-work). Verification
failure details are available in the session
[last_error](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error)
hash. The
[last_error.code](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)
value can be used to programmatically handle common verification failures. The
[last_error.reason](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)
will contain a string that explains the failure reason and can be shown to your
user.

```
{
 "id": "vs_",
 "object": "identity.verification_session",
 "created": 1610744321,
 "last_error": {
 "code": "document_expired",
 "reason": "The document is expired.",
 },
 "last_verification_report": "vr_",
 "livemode": true,
 "metadata": {},
 "options": {},
 "status": "requires_input",
 "type": "document",
 "redaction": null,
 "url": null,
}
```

If you want your user to attempt verification again, you’ll need to [Retrieve
the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
to get a fresh URL or client secret to pass to your client.

Learn how to [access sensitive verification
results](https://docs.stripe.com/identity/access-verification-results)

## Cancelling a VerificationSession

You can cancel a VerificationSession at any point before it’s `processing` or
`verified`. This invalidates the VerificationSession for future submission
attempts, and can’t be undone. The session will have a `canceled`
[status](https://docs.stripe.com/identity/how-sessions-work).

```
curl -X POST
https://api.stripe.com/v1/identity/verification_sessions/{{VERIFICATION_SESSION_ID}}/cancel
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Redacting a VerificationSession

One of the reasons that you might want to redact a verification session is if
you receive a data deletion request from your user. You can redact a session to
ensure collected information is no longer returned by the Stripe API or visible
in Dashboard. You can still
[retrieve](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
redacted sessions with the API but you can’t update them. Sessions can be
redacted from the Dashboard or through the API:

```
curl -X POST
https://api.stripe.com/v1/identity/verification_sessions/{{VERIFICATION_SESSION_ID}}/redact
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

Redacted sessions show placeholder values for all fields that previously
contained personally identifiable information (PII). The session includes a
[redaction.status](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-redaction-status)
field indicating the status of the redaction process. An
[identity.verification_session.redacted](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.redacted)
webhook will be sent when the session is redacted. Please note redaction can
take up to 4 days.

If a VerificationSession that has been redacted is retrieved with PII fields
expanded, then these fields will still appear in the response but their values
will not contain any PII. For example, here is a response that has expanded the
`verified_outputs` and `verified_outputs.dob` fields on a redacted
VerificationSession.

```
{
 "id": "vs_",
 "object": "identity.verification_session",
 "created": 1610744321,
 "last_error": null,
 "last_verification_report": "vr_",
 "livemode": true,
 "options": {},
 "status": "verified",
 "type": "document",
 "url": null,
 "client_secret": null,
 "redaction": {
 "status": "redacted"
 },
 "verified_outputs": {
 "first_name": "[redacted]",
 "last_name": "[redacted]",
 "dob": {
 "year": 1,
 "month": 1,
 "day": 1
 },
 "address": {
 "line1": "[redacted]",
 "city": "[redacted]",
 "state": "[redacted]",
 "postal_code": "[redacted]",
 "country": "US"
 },
 "id_number_type": null
 },
 "metadata": {} // Metadata will also be redacted
}
```

Any
[VerificationReports](https://docs.stripe.com/api/identity/verification_reports),
[Events](https://docs.stripe.com/api/events), and [Request
Logs](https://dashboard.stripe.com/logs) associated with the VerificationSession
are also redacted and [File](https://docs.stripe.com/api/files) contents are no
longer downloadable.

If the VerificationSession is in the `processing` state you must wait until it
finishes before redacting it. Redacting a VerificationSession with
`requires_action` status automatically cancels it.

## Storing information in metadata

Stripe supports adding [metadata](https://docs.stripe.com/api#metadata) to the
VerificationSession object. Metadata isn’t shown to customers or factored into
whether a verification check succeeds or fails.

Through metadata, you can associate other information—meaningful to you—with
Stripe activity. Any metadata you include is viewable in the Dashboard (for
example, when looking at the page for an individual session), and is also
available in common reports. As an example, you can attach your application’s
user ID to the VerificationSession used to verify that user. Doing so allows
you, or your team to easily reconcile verifications in Stripe to users in your
system.

```
curl https://api.stripe.com/v1/identity/verification_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=document \
 -d "metadata[user_id]"={{USER_ID}} \
 -d "metadata[reference]"={{IDENTIFIER}}
```

We recommend you don’t store any sensitive information (PII, ID numbers, and so
on) in session metadata. Note that metadata is removed when you redact a
VerificationSession.

## See also

- [How sessions work](https://docs.stripe.com/identity/how-sessions-work)
- [Verify your users’ identity
documents](https://docs.stripe.com/identity/verify-identity-documents)

## Links

- [Verification Session
API](https://docs.stripe.com/api/identity/verification_sessions)
- [verification checks](https://docs.stripe.com/identity/verification-checks)
- [Verify your users’ identity
documents](https://docs.stripe.com/identity/verify-identity-documents)
- [create the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create)
-
[type](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-type)
- [document](https://docs.stripe.com/identity/verification-checks?type=document)
- [selfie check](https://docs.stripe.com/identity/selfie)
-
[id_number](https://docs.stripe.com/identity/verification-checks?type=id-number)
-
[retrieve](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
- [idempotency key](https://docs.stripe.com/api/idempotent_requests)
- [client
secret](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-client_secret)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [TLS](https://docs.stripe.com/security/guide#tls)
-
[VerificationReport](https://docs.stripe.com/api/identity/verification_reports/object)
- [expand](https://docs.stripe.com/api/expanding_objects)
-
[verified_outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
- [status](https://docs.stripe.com/identity/how-sessions-work)
-
[last_error](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error)
-
[last_error.code](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)
- [access sensitive verification
results](https://docs.stripe.com/identity/access-verification-results)
-
[redaction.status](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-redaction-status)
-
[identity.verification_session.redacted](https://docs.stripe.com/api/events/types#event_types-identity.verification_session.redacted)
-
[VerificationReports](https://docs.stripe.com/api/identity/verification_reports)
- [Events](https://docs.stripe.com/api/events)
- [Request Logs](https://dashboard.stripe.com/logs)
- [File](https://docs.stripe.com/api/files)
- [metadata](https://docs.stripe.com/api#metadata)