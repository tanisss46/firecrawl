# Access verification results

## Learn how to access sensitive verification results.

You wrote code to [display a modal to collect identity
documents](https://docs.stripe.com/identity/verify-identity-documents) and
[handle verification
outcomes](https://docs.stripe.com/identity/handle-verification-outcomes). Now
you might need access to the sensitive verification results such as your user’s
date of birth or pictures of the collected document.

First, consider using the [Identity
Dashboard](https://dashboard.stripe.com/identity) to access sensitive
verification results. If needed, [give team members controlled
access](https://docs.stripe.com/get-started/account/teams) to your Stripe
account. This saves you development time and ensures the sensitive verification
data is kept
[securely](https://support.stripe.com/questions/managing-your-id-verification-information)
on Stripe.

You can [access most verification details
programmatically](https://docs.stripe.com/identity/verification-sessions#results),
such as the result of a verification check or the user’s name and address using
your [secret key](https://docs.stripe.com/keys). Access to more sensitive fields
require the use of [restricted API
keys](https://docs.stripe.com/keys#limit-access).

Verification resultAvailable in DashboardSecret key accessRestricted API key
accessRecommended Verification Session fieldExpand
propertyAddress`verified_outputs.address``verified_outputs`Document
type`last_verification_report.document.type``last_verification_report`First and
last names`verified_outputs.first_name and
verified_outputs.last_name``last_verification_report`Issuing country of the
document`last_verification_report.document.issuing_country``last_verification_report`Result
of the verification check`status`Expand not requiredIssued date of the
document`last_verification_report.document.issued_date``last_verification_report`Type
of ID
number`last_verification_report.document.id_number.type``last_verification_report`Email
address`verified_outputs.email``verified_outputs`Phone
number`verified_outputs.phone``verified_outputs`Expiration date of the
document`last_verification_report.document.expiration_date``last_verification_report.document.expiration_date`Date
of birth`verified_outputs.dob``verified_outputs.dob`Document ID
number`last_verification_report.document.number``last_verification_report.document.number`Document
images`last_verification_report.document.files``last_verification_report`Face
images`last_verification_report.selfie.selfie``last_verification_report`ID
number`verified_outputs.id_number``verified_outputs.id_number`
Restricted API keys allow access based on the security measures associated with
it:

- **Restricted keys** — Allow access to sensitive verification results for
verifications processed in the last 48 hours.
- **IP restricted keys** - Allow access to sensitive verification results for
all verifications.

In this guide, you’ll learn how to:

- Consider your sensitive data access requirements carefully.
- Create restricted API keys.
- Make API requests to obtain sensitive verification results.
- Roll your keys if they’re compromised.
- Communicate your sensitive verification results and security measures to your
users.
- Add IP restrictions to your key for long-term access to sensitive verification
results.
- Consider your sensitive data access requirements carefully.
- Create restricted API keys.
- Make API requests to obtain sensitive verification results.
- Roll your keys if they’re compromised.
- Communicate your sensitive verification results and security measures to your
users.
[Consider your sensitive data access requirements
carefully](https://docs.stripe.com/identity/access-verification-results#decide-access-requirements)
To build an integration with Stripe Identity that prioritizes your user’s
privacy, you must first decide the minimum amount of PII that you need access
to. If you don’t need access to the most sensitive data (that requires
authentication with a restricted API key), then your integration can
authenticate using your secret key only.

To access PII resulting from a verification, you can retrieve a
VerificationSession and [expand](https://docs.stripe.com/api/expanding_objects)
either the
[verified_outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
field or - if you need more granular detail on the verification result - the
[last_verification_report](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report).
Expanding either of these fields automatically includes all of the PII fields
they contain that only require a secret key.

Here is an example of how to expand the `verified_outputs` field to retrieve a
user’s name that was verified by Stripe Identity.

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

const verificationSession = await stripe.identity.verificationSessions.retrieve(
 '{{SESSION_ID}}',
 {
 expand: [
 'verified_outputs',
 ],
 }
);

const firstName = verificationSession.verified_outputs.first_name;
```

If you do need to access sensitive PII that requires a restricted key, follow
the steps in this guide.

[Create a restricted API
keyDashboard](https://docs.stripe.com/identity/access-verification-results#create-restricted-key)
You can use your account’s secret API keys to perform any API request without
restriction. Accessing sensitive verification results requires [restricted
keys](https://docs.stripe.com/keys#limit-access), which are more secure.

To create a new restricted key,

- Go to the [API keys page](https://dashboard.stripe.com/apikeys) in the
Dashboard and click [Create restricted
key](https://dashboard.stripe.com/apikeys/create).
- Name your key.
- Make sure the Identity **Verification Sessions and Reports** and **Access
recent sensitive verification results** permissions are set to **Read**.
- (optional) If you need to access collected images, add the Files **Write**
permission.
- Click **Create key**.
- Store the key securely. [Learn more about keeping your keys
safe](https://docs.stripe.com/keys#safe-keys).

!

[Make API requests to obtain sensitive verification
resultsServer-side](https://docs.stripe.com/identity/access-verification-results#api-request)

[VerificationReports](https://docs.stripe.com/api/identity/verification_reports)
contain all the collected data and verification results from a submitted
session. VerificationReports are created when all verification checks for a
session are processed. They allow you to understand why a verification check
failed and what data was successfully verified.

You can [expand](https://docs.stripe.com/expand) the
[last_verification_report](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)
session field to retrieve the associated VerificationReport.

By default, VerificationReports don’t include sensitive verification results. To
access these, you’ll need to:

- Authenticate using the restricted API key created in step 1.
- [Expand](https://docs.stripe.com/api/expanding_objects) the fields you want to
access.

Here’s an example of accessing the extracted date of birth, ID number, and
document number from a [document
check](https://docs.stripe.com/identity/verification-checks?type=document):

```
// Set your restricted key. Remember to switch to a live restricted key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('rk_test_...');

const verificationSession = await stripe.identity.verificationSessions.retrieve(
 '{{SESSION_ID}}',
 {
 expand: [
 'verified_outputs.dob',
 'verified_outputs.id_number',
 'last_verification_report.document.number',
 'last_verification_report.document.expiration_date',
 ],
 }
);

const dateOfBirth = verificationSession.verified_outputs.dob;
const idNumber = verificationSession.verified_outputs.id_number;
const documentNumber =
verificationSession.last_verification_report.document.number;
const documentExpirationDate =
verificationSession.last_verification_report.document.expiration_date;
```

## Accessing collected images

You can retrieve identity document and face images that you collect as part of a
session using the [File Upload API](https://docs.stripe.com/file-upload). The
following fields on a VerificationReport can hold a reference to a
[File](https://docs.stripe.com/api/files) resource in the Stripe API:

-
[document.files](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document-front)
- images of the identity document
-
[selfie.document](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie-document)
- image of the photo ID front
-
[selfie.selfie](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie-selfie)
- image of the user’s face

#### Note

Document and face images are very sensitive and some countries, such as Germany,
have laws prohibiting ID Document images from being shared or kept longer than
necessary. As much as possible, access image content with short-lived FileLinks,
don’t make copies of the file contents, and [redact
sessions](https://docs.stripe.com/identity/verification-sessions#redact) and
collected images when you’re done using them for the purpose collected.

To access the contents of the file, you need to authenticate using the
previously created restricted key and [Create a
FileLink](https://docs.stripe.com/api/file_links/create) with a short expiration
and send the
[url](https://docs.stripe.com/api/file_links/object#file_link_object-url) to the
client:

```
// Set your restricted key. Remember to switch to a live restricted key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('rk_test_...');

// Get the VerificationReport
const session = await stripe.identity.verificationSessions.retrieve(
 '{{SESSION_ID}}',
 {
 expand: ['last_verification_report'],
 }
);

// Retrieve the File id
const report = session.last_verification_report;
const documentFrontFile = report.document.files[0];

// Create a short-lived FileLink
const fileLink = await stripe.fileLinks.create({
 file: documentFrontFile,
 expires_at: Math.floor(Date.now() / 1000) + 30, // link expires in 30 seconds
});

// Access the FileLink URL to download file contents
const fileUrl = fileLink.url;
```

#### Note

FileLinks for document and selfie files must expire within 30 seconds. We
recommend not downloading the file contents on your server, instead send the
FileLink URL to the client to display the image.

If you believe an attacker has accessed sensitive data collected by Identity,
please [reach out to support](https://support.stripe.com/contact).

[Roll your keys if they’re
compromisedDashboard](https://docs.stripe.com/identity/access-verification-results#roll-keys)
Using restricted API keys that only have Identity permissions allows you to roll
the keys in case of emergency without affecting other Stripe product
integrations.

We recommend that you regularly monitor your restricted key usage to ensure that
no one has gained access to them. In the
[Dashboard](https://dashboard.stripe.com/apikeys), you can use the overflow menu
(**…**) to view request logs for a specific API key to view all the requests
made from that key.

If an API key is compromised, roll the key in the
[Dashboard](https://dashboard.stripe.com/apikeys) to block it and generate a new
one. Make sure to expire it immediately to prevent bad actors from retrieving
sensitive information.

#### Warning

Rolling blocks the API key and generates a new one. We recommend reviewing your
[security history](https://dashboard.stripe.com/security_history) for events
related to this key. Any webhook endpoints created with this key will stay
active, even after the key is rolled.

If you believe an attacker has accessed sensitive data collected by Identity,
please [reach out to support](https://support.stripe.com/contact).

[Communicate your sensitive data use and security
measures](https://docs.stripe.com/identity/access-verification-results#tell-users)
Make sure your privacy policy includes information on your use of sensitive
verification results. It may also help if you provide information about your
security practices.

**See also**

- [Privacy considerations for handling ID verification data as a
business](https://support.stripe.com/questions/privacy-considerations-for-handling-id-verification-data-as-a-business)
- [FAQs to provide to your
users](https://docs.stripe.com/identity/explaining-identity)
[OptionalAdd IP restrictions for long-term access to
resultsDashboard](https://docs.stripe.com/identity/access-verification-results#ip-allowlist)
## See also

- [Expanding responses](https://docs.stripe.com/api/expanding_objects)
- [API Keys](https://docs.stripe.com/keys)
- [Security at Stripe](https://docs.stripe.com/security)

## Links

- [display a modal to collect identity
documents](https://docs.stripe.com/identity/verify-identity-documents)
- [handle verification
outcomes](https://docs.stripe.com/identity/handle-verification-outcomes)
- [Identity Dashboard](https://dashboard.stripe.com/identity)
- [give team members controlled
access](https://docs.stripe.com/get-started/account/teams)
-
[securely](https://support.stripe.com/questions/managing-your-id-verification-information)
- [access most verification details
programmatically](https://docs.stripe.com/identity/verification-sessions#results)
- [secret key](https://docs.stripe.com/keys)
- [restricted API keys](https://docs.stripe.com/keys#limit-access)
- [expand](https://docs.stripe.com/api/expanding_objects)
-
[verified_outputs](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)
-
[last_verification_report](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [Create restricted key](https://dashboard.stripe.com/apikeys/create)
- [Learn more about keeping your keys
safe](https://docs.stripe.com/keys#safe-keys)
-
[VerificationReports](https://docs.stripe.com/api/identity/verification_reports)
- [expand](https://docs.stripe.com/expand)
- [document
check](https://docs.stripe.com/identity/verification-checks?type=document)
- [File Upload API](https://docs.stripe.com/file-upload)
- [File](https://docs.stripe.com/api/files)
-
[document.files](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-document-front)
-
[selfie.document](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie-document)
-
[selfie.selfie](https://docs.stripe.com/api/identity/verification_reports/object#identity_verification_report_object-selfie-selfie)
- [redact
sessions](https://docs.stripe.com/identity/verification-sessions#redact)
- [Create a FileLink](https://docs.stripe.com/api/file_links/create)
- [url](https://docs.stripe.com/api/file_links/object#file_link_object-url)
- [reach out to support](https://support.stripe.com/contact)
- [security history](https://dashboard.stripe.com/security_history)
- [Privacy considerations for handling ID verification data as a
business](https://support.stripe.com/questions/privacy-considerations-for-handling-id-verification-data-as-a-business)
- [FAQs to provide to your
users](https://docs.stripe.com/identity/explaining-identity)
- [Security at Stripe](https://docs.stripe.com/security)