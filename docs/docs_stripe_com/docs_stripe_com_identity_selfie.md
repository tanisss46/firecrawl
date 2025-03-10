# Adding selfie checks

## Learn how to add face similarity checks to prevent fraudsters from using stolen documents.

While [document
checks](https://docs.stripe.com/identity/verification-checks?type=document)
provide a defense against the use of fraudulent identity documents, it’s
possible for fraudsters to get access to legitimate stolen documents. To prevent
this, Stripe Identity can perform selfie checks on your users.

Selfie checks look for distinguishing biological traits, such as face geometry,
from a photo ID and a picture of your user’s face. Stripe then uses advanced
machine learning algorithms to ensure the face pictures belong to the same
person.

To add selfie checks to your application, first follow the guide to [collect and
verify identity
documents](https://docs.stripe.com/identity/verify-identity-documents).

## Adding selfie checks to VerificationSessions

When [creating a
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create),
use the
[options.document.require_matching_selfie](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-options-document-require_matching_selfie)
parameter to enable selfie checks.

```
curl https://api.stripe.com/v1/identity/verification_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=document \
 -d "options[document][require_matching_selfie]"=true
```

This configures the verification flow to require a photo ID and a face picture
from your user.

## Accessing selfie check results

After it’s submitted and processed, the VerificationSession
[status](https://docs.stripe.com/identity/how-sessions-work) changes depending
on the result of the checks:

- `verified` — Both the document and selfie checks were successful. The session
[verified_outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
contains extracted information from the document.
- `requires_input` — At least one of the document or the selfie checks failed.

To access the captured selfie and document images, you’ll need to retrieve the
associated
[VerificationReport](https://docs.stripe.com/api/identity/verification_reports),
you can do this by [expanding](https://docs.stripe.com/api/expanding_objects)
the
[last_verification_report](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)
field in the session:

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');
const verificationSession = await stripe.identity.verificationSessions.retrieve(
 '{{SESSION_ID}}',
 {
 expand: ['last_verification_report'],
 }
);
const verificationReport = verificationSession.last_verification_report;
```

The VerificationReport has
[document](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document)
and
[selfie](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie)
fields holding the results of the document and selfie checks. Here’s an example
VerificationReport with successful document and selfie checks:

```
{
 "id": "vr_",
 "object": "identity.verification_report",
 "type": "document",
 "verification_session": "vs_",
 "created": 1611776872,
 "livemode": true,
 "options": {
 "document": {
 "require_matching_selfie": true
 }
 },
 "document": {
 "status": "verified",
 "error": null,
 "first_name": "Jenny",
 "last_name": "Rosen",
 "address": {
 "line1": "1234 Main St.",
 "city": "San Francisco",
 "state": "CA",
 "postal_code": "94111",
 "country": "US"
 },
 "document_type": "id_card",
 "expiration_date": {
 "day": 17,
 "month": 7,
 "year": 2024
 },
 "files": ["file_", "file_"],
 "issued_date": {
 "day": 4,
 "month": 27,
 "year": 2021
 },
 "issuing_country": "US"
 },
 "selfie": {
 "status": "verified",
 "error": null,
 "document": "file_",
 "selfie": "file_",
 }
}
```

To access the collected document and face images, see [Accessing verification
results](https://docs.stripe.com/identity/access-verification-results).

## Understanding selfie check failures

The
[document](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document)
and
[selfie](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie)
VerificationReport fields contain the collected data as well as a `status` and
`error` fields to help you understand whether the check is successful or not.

The `status` field tells you whether each check is successful or not. The
possible values are:

- `verified` - The verification check is successful and the collected data is
verified.
- `unverified` - The verification check failed. You can check the `error` hash
for more information.

When the verification check fails, the `error` field contains `code` and
`reason` values to explain the verification failure. The `error.code` field can
be used to programmatically handle verification failures. The `reason` field
contains a descriptive message explaining the failure reason and can be shown to
your user.

### Document check failures

Failure details are available in the report
[document.error](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document-error)
field.

Error codeDescription`document_expired`The provided identity document has
expired.`document_unverified_other`Stripe couldn’t verify the provided identity
document. [See list of supported document
types](https://docs.stripe.com/identity/verification-checks?type=document).`document_type_not_supported`The
provided identity document isn’t one of the session’s [allowed document
types](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-options-document-allow_document_types).
### Selfie check failures

Failure details are available in the report
[selfie.error](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie-error)
field.

Error codeDescription`selfie_document_missing_photo`The provided identity
document did not contain a picture of a face.`selfie_face_mismatch`The captured
face image did not match with the document’s
face.`selfie_unverified_other`Stripe couldn’t verify the provided
selfie.`selfie_manipulated`The captured face image was manipulated.
## See also

- [Verify your users’ identity
documents](https://docs.stripe.com/identity/verify-identity-documents)
- [The Verification Sessions
API](https://docs.stripe.com/identity/verification-sessions#create)

## Links

- [document
checks](https://docs.stripe.com/identity/verification-checks?type=document)
- [collect and verify identity
documents](https://docs.stripe.com/identity/verify-identity-documents)
- [creating a
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create)
-
[options.document.require_matching_selfie](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-options-document-require_matching_selfie)
- [status](https://docs.stripe.com/identity/how-sessions-work)
-
[verified_outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
-
[VerificationReport](https://docs.stripe.com/api/identity/verification_reports)
- [expanding](https://docs.stripe.com/api/expanding_objects)
-
[last_verification_report](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[document](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document)
-
[selfie](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie)
- [Accessing verification
results](https://docs.stripe.com/identity/access-verification-results)
-
[document.error](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document-error)
- [allowed document
types](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-options-document-allow_document_types)
-
[selfie.error](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie-error)
- [The Verification Sessions
API](https://docs.stripe.com/identity/verification-sessions#create)