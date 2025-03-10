# Handle verification with the API

## Learn how Connect platforms can use webhooks and the API to handle verification of connected accounts.

Platforms with accounts created using the API can provide Stripe with necessary
information about their users for [Know Your
Customer](https://support.stripe.com/questions/know-your-customer) (KYC)
purposes. Platforms can use [Connect](https://docs.stripe.com/connect)
Onboarding to collect KYC information, or use the
[Accounts](https://docs.stripe.com/api/accounts) and
[Persons](https://docs.stripe.com/api/persons) APIs to provide Stripe with
required information. We’ll then perform verification, asking for more
information when needed.

The rest of this page goes through how platforms:

- Discover verification requirements for a connected account
- Provide the necessary information to Stripe

#### Note

You can’t use the API to respond to Stripe risk reviews. You can enable your
connected accounts to respond using embedded components, Stripe-hosted
onboarding, or remediation links. You can also use the Dashboard to respond to
risk reviews on behalf of your connected accounts.

## Verification process

Before enabling charges and [payouts](https://docs.stripe.com/payouts) for a
connected account, Stripe needs certain information that varies based on:

- The origin country of the connected accounts
- The [service agreement
type](https://docs.stripe.com/connect/service-agreement-types) applicable to the
connected accounts
- The [capabilities](https://docs.stripe.com/connect/account-capabilities)
requested for the connected accounts
- The [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
(for example, individual or company) and
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
(for example, public corporation or private partnership)

Platforms need to choose the proper [onboarding
flow](https://docs.stripe.com/connect/identity-verification#onboarding-flows)
for their business and users to meet the KYC requirements. Broadly speaking,
this means providing all the requisite information upfront or incrementally.
Either way, set up your integration to watch for and respond to requests from
Stripe.

- Establish a [Connect webhook](https://docs.stripe.com/connect/webhooks) URL in
your [webhook settings](https://dashboard.stripe.com/account/webhooks) to watch
for activity, especially events of the `account.updated` type. When using the
[Persons API](https://docs.stripe.com/api/persons), you should also watch for
`person.updated` events.
- Immediately after creating an account, check the `Account` object’s
[requirements.currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
attribute for any additional requirements. Obtain any required information from
the user and update the connected account.
- Continue watching for `account.updated` event notifications to see if the
`requirements` hash changes, and reach out to your user for additional
information as needed.

When you provide additional information, you don’t need to resubmit any
previously verified details. For example, if the `dob` is already verified, you
don’t need to provide it again in subsequent updates.

#### Caution

When `requirements.currently_due` isn’t empty, additional information is
required. Connected accounts might be blocked from creating charges, receiving
payouts, or performing certain tasks if you don’t provide this information in a
timely manner.

### Change information after verification

After an individual or company is verified, you can [change some of their
information](https://docs.stripe.com/connect/update-verified-information), with
limitations. See the [Update
Account](https://docs.stripe.com/api/accounts/update) API for limitations based
on the configuration of the connected account. [Contact
support](https://support.stripe.com/contact) to make changes outside of these
limitations.

## Determine if verification is needed

When you receive an `account.updated` event to your webhook or [fetch an
account](https://docs.stripe.com/api#retrieve_account) with the API, you receive
an [Account](https://docs.stripe.com/api/accounts/object) object. The `Account`
object’s `charges_enabled` and `payouts_enabled` attributes indicate whether the
account can create charges and accept payouts.

The `Account` object has a `requirements` hash, representing the requirements
needed to verify the account.

The `requirements` hash has the following arrays:

- `eventually_due`: Requirements that you might need to collect, depending on
whether the corresponding thresholds are reached. After a requirement becomes
required, it also appears in the `currently_due` list. If a requirement becomes
required and its due date is before the existing `current_deadline`, the
`current_deadline` changes to the corresponding threshold’s enforcement date.
- `currently_due`: Requirements that you must collect by the `current_deadline`
for the Account to remain `active`. `currently_due` is a subset of
`eventually_due`.
- `past_due`: Requirements that have disabled capabilities because they weren’t
verified before the `current_deadline`. `past_due` is a subset of
`currently_due`.
- `errors`: Details about validation and verification failures that require
particular requirements in `currently_due` or `past_due` to be collected again.-
`requirement`: Identifies the requirement corresponding to the error.
- `code`: An enum value describing why the requirement is invalid or can’t be
verified.
- `reason`: An message describing the error in more detail. The reason
string can also suggest how to resolve the error.
- `disabled_reason`: Describes why the Account isn’t enabled and why it can’t
process charges or transfers.
- `current_deadline`: Date by which requirements in `currently_due` must be
collected to keep the Account `active`. It represents the earliest deadline
across all of the Account’s requested capabilities and risk requirements,
including any hidden capabilities.
- `pending_verification`: Requirements that might become required, depending on
the results of verification or review. It’s an empty array unless an
asynchronous verification is pending. Unsuccessful verification moves a
requirement to `eventually_due`, `currently_due`, or `past_due`. A requirement
subject to both failed and pending verifications can also remain in
`pending_verification`.

The example below shows what the `requirements` hash might look like for an
account that has some information that’s `currently_due`, some information
that’s `eventually_due`, and some information that’s raising verification
`errors`.

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "requirements": {
 "disabled_reason": null,
 "current_deadline": 1529085600,
 "past_due": [],
 "currently_due": [
 "company.tax_id",
 "company.verification.document",
 "tos_acceptance.date",
 "tos_acceptance.ip"
 ],
 "eventually_due": [
 "company.address.city",
 "company.address.line1",
 "company.address.postal_code",
 "company.address.state",
 "company.tax_id",
 "company.verification.document",
 "external_account",
 "tos_acceptance.date",
 "tos_acceptance.ip"
 ],
 "errors": [
 {
 "requirement": "company.verification.document",
"reason": "The company name on the account couldn't be verified. Either update
your business name or upload a document containing the business name.",
 "code": "failed_name_match"
 },
 ]
 },
 ...
}
```

If `requirements.currently_due` contains entries, check
`requirements.current_deadline`. The `current_deadline` is a Unix timestamp
identifying when information is needed. Usually, if Stripe doesn’t receive the
information by the `current_deadline`, payouts on the account are disabled.
However, other consequences might apply in some situations. For example, if
payouts are already disabled and the account is unresponsive to our inquiries,
Stripe might also disable the ability to process charges.

Separately, the
[requirements.disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-requirements-disabled_reason)
property can have a value. The value is a string describing the reason why this
account is unable to make payouts or charges. In some instances, platforms and
connected accounts can submit a form to resolve or appeal the reason.

- Connected accounts with access to the full Stripe Dashboard and Standard
accounts can access additional information (if available) in the Dashboard.
- Platforms in any Connect configuration can navigate to [Accounts to
review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts) to
understand an account’s `disabled_reason`. You might be able to provide
additional information on behalf of your connected accounts. If the disabled
reason is associated with an appeal, you can generate a link to a form for the
account to resolve the appeal.
ReasonMeaning`action_required.requested_capabilities`You need to request
capabilities for the connected account. For details, see [Request and unrequest
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting).`listed`Account
might be on a prohibited persons or companies list (Stripe investigates and
either rejects or reinstates the account accordingly).`rejected.fraud`Account is
rejected due to suspected fraud or illegal
activity.`rejected.incomplete_verification`The account is rejected from
incomplete verification requirements within the required
threshold.`rejected.listed`Account is rejected because it’s on a third-party
prohibited persons or companies list (such as financial services provider or
government).`rejected.other`Account is rejected for another
reason.`rejected.terms_of_service`Account is rejected due to suspected terms of
service violations.`requirements.past_due`Additional verification information is
required to enable capabilities on this
account.`requirements.pending_verification`Stripe is currently verifying
information on the connected account. No action is required. Inspect the
[requirements.pending_verification](https://docs.stripe.com/api/accounts/object#account_object-requirements-pending_verification)
array to see the information being verified.`under_review`The account is under
review by Stripe.
## Validation and verification errors

The [Account](https://docs.stripe.com/api/accounts/object) object includes a
[requirements.errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
array that explains why the validation or verification requirements haven’t been
met, which are needed to enable your account and capabilities. The `errors`
array has the following attributes:

- `requirement`: Specifies which information from the `currently_due` array is
needed.
- `code`: Indicates the type of error that occurred. See the [API
reference](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors-code)
for all possible error codes.
- `reason`: Explains why the error occurred and how to resolve the error.

Below is an example that shows what the `errors` array might look like for an
account with requirements that are `currently_due`. The example shows the reason
why the submitted information can’t be used to enable the account, and how to
resolve the error. If verification or validation is unsuccessful, requirements
can reappear in `currently_due` with error information. Set a [Connect
webhook](https://docs.stripe.com/connect/webhooks) to receive the
`account.updated` event to receive these updates.

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "requirements": {
 "current_deadline": 1234567800,
 "currently_due": [
 "company.address.line1",
 "{{PERSON_ID}}.verification.document",
 ],
 "errors": [
 {
 "requirement": "company.address.line1",
 "code": "invalid_street_address",
"reason": "The provided street address cannot be found. Please verify the street
name and number are correct in \"10 Downing Street\"",
 },
 {
 "requirement": "{{PERSON_ID}}.verification.document",
 "code": "verification_document_failed_greyscale",
"reason": "Greyscale documents cannot be read. Please upload a color copy of the
document.",
 }
 ]
 },
 ...
}
```

If verification or validation is unsuccessful but no requirements are currently
due, a webhook triggers indicating that required information is eventually due.

## Business information

When information about a business is submitted, Stripe verifies the new
information. For example, Stripe might verify that the provided business URL is
valid, reachable, and includes information about the business. To retrieve the
status of verification information regarding a business, utilize the
`requirements` on the Account object.

Below is a list of errors related to business information verification:

ErrorResolution`invalid_business_profile_name`Business names must be easy for
people to understand and must consist of recognizable
words.`invalid_business_profile_name_denylisted`Generic or well-known business
names aren’t supported. Make sure the provided business name matches the
account’s business.`invalid_product_description_length`A product description
must be at least 10 characters.`invalid_product_description_url_match`A product
description must be different from the URL of the business.
`invalid_url_denylisted`

`invalid_url_format`

`invalid_url_web_presence_detected`

`invalid_url_website_business_information_mismatch`

`invalid_url_website_empty`

`invalid_url_website_inaccessible`

`invalid_url_website_inaccessible_geoblocked`

`invalid_url_website_inaccessible_password_protected`

`invalid_url_website_incomplete`

`invalid_url_website_incomplete_cancellation_policy`

`invalid_url_website_incomplete_customer_service_details`

`invalid_url_website_incomplete_legal_restrictions`

`invalid_url_website_incomplete_refund_policy`

`invalid_url_website_incomplete_return_policy`

`invalid_url_website_incomplete_terms_and_conditions`

`invalid_url_website_incomplete_under_construction`

`invalid_url_website_other`

See [handling URL verification
errors](https://docs.stripe.com/connect/handling-api-verification#url-verification)
below.

## Statement descriptors

Stripe validates the statement descriptor and statement descriptor prefix when
[set on an account](https://docs.stripe.com/connect/statement-descriptors). For
example, Stripe might verify that the provided statement descriptor matches the
description of the business. When validating the statement descriptor matches
the business description, Stripe uses the first 22 characters of the statement
descriptor, representing the part that is provided to the card networks. A
business description is a close match of the account’s `business_profile.name`,
`business_profile.url`, or the name of the company or individual.

To retrieve the status of verification information regarding statement
descriptors, review the `requirements` on the Account object. Below is a list of
errors related to statement descriptor verification:

ErrorResolution`invalid_statement_descriptor_length`A statement descriptor must
be at least 5 characters.`invalid_statement_descriptor_business_mismatch`A
statement descriptor must be similar to the business name, legal entity name, or
URL of the account.
`invalid_statement_descriptor_denylisted`

`invalid_statement_descriptor_prefix_denylisted`

Generic or well-known statement descriptors aren’t supported.

`invalid_statement_descriptor_prefix_mismatch`The statement descriptor prefix
must be similar to your statement descriptor, business name, legal entity name,
or URL.
## Person information

During the verification process, information about the persons associated with
an account needs to be collected. If you onboard:

- Only companies, use the [Persons](https://docs.stripe.com/api/persons) API to
collect this information.
- Only individuals, you can use the
[Persons](https://docs.stripe.com/api/persons) API or the
[individual](https://docs.stripe.com/api/accounts/object#account_object-individual)
hash on the Account object.
- A combination of individuals and companies, use the
[Persons](https://docs.stripe.com/api/persons) API to collect this information.
This way you collect information in the same manner regardless of business type.

To retrieve the status of verification information regarding a person, use the
[requirements](https://docs.stripe.com/api/persons/object#person_object-requirements)
hash.

Below is a list of errors related to person verification:

ErrorResolution`invalid_address_city_state_postal_code`Stripe couldn’t validate
the combination of the city, state, and postal code in the provided
address.`invalid_address_highway_contract_box`The address of the person must be
a valid physical address from which the account conducts business and can’t be a
Highway Contract Box.`invalid_address_private_mailbox`The address of the person
must be a valid physical address from which the account conducts business and
can’t be a private mailbox.`invalid_dob_age_under_minimum`The person must be at
least 13 years old.`invalid_dob_age_over_maximum`The person’s date of birth must
be within the past 120 years.`invalid_phone_number`Stripe couldn’t validate the
phone number on the account. Make sure the formatting matches the country of the
person.`invalid_street_address`Stripe couldn’t validate the street name and/or
number for the provided address.
`invalid_tax_id`

`invalid_tax_id_format`

Tax IDs must be a unique set of 9 numbers without dashes or other special
characters.

## Acceptable verification documents by country

To learn about specific document requirements, view [Acceptable verification
documents by
country](https://docs.stripe.com/acceptable-verification-documents).

## Company information

During the verification process, you might need to collect information about the
company for an account.

To retrieve the status of verification information regarding an account’s
company, use the Account’s
[company.verification](https://docs.stripe.com/api/accounts/object#account_object-company-verification)
subhash:

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 ...
 "company": {
 "verification": {
 "document": null
 },
 ...
 },
 ...
}
```

You can look up the definition for each verification attribute on the
[Account](https://docs.stripe.com/api/accounts/object#account_object-company-verification)
object.

## Handle document verification problems

Many complications with the verification process involve the uploaded document
itself. To help you recognize and handle the most common problems, the table
below lists possible values for the error `code` (in the `requirements.errors`
array) and the likely resolutions for each error.

Below is a list of errors related to document upload:

ErrorResolution
`verification_document_corrupt`

`verification_document_failed_copy`

`verification_document_failed_greyscale`

`verification_document_incomplete`

`verification_document_not_readable`

`verification_document_not_uploaded`

`verification_document_not_signed`

`verification_document_missing_back`

`verification_document_missing_front`

`verification_document_too_large`

The upload failed due to a problem with the file itself. Ask your user to
provide a new file that meets these requirements:

- Color image (8,000 pixels by 8,000 pixels or smaller)
- 10 MB or less
- Identity documents are JPG or PNG format
- Address or legal entity documents are JPG, PNG, or PDF format
- Legal entity documents must include all pages
- Must not be password protected

`verification_document_country_not_supported`

`verification_document_invalid`

`verification_document_type_not_supported`

The provided file isn’t an acceptable form of ID from a supported country, or
isn’t a type of legal entity document that is expected. Ask your user to provide
a new file that meets that requirement. For a list, see [Acceptable ID types by
country](https://docs.stripe.com/connect/handling-api-verification#acceptable-verification-documents).

`verification_failed_other`

`verification_document_failed_other`

Your team can contact Stripe to learn more about why identity verification
failed.

`verification_document_expired`

`verification_document_issue_or_expiry_date_missing`

The issue or expiry date is missing on the document, or the document is expired.
If it’s an identity document, its expiration date must be after the date the
document was submitted. If it’s an address document, the issue date must be
within the last six months.

Below is a list of errors related to identity verification:

ErrorResolution`verification_failed_keyed_identity`The name on the account
couldn’t be verified. Ask your user to verify that they have provided their full
legal name and to also provide a photo ID matching that name.
`verification_document_name_mismatch`

`verification_document_dob_mismatch`

`verification_document_address_mismatch`

`verification_document_id_number_mismatch`

`verification_document_photo_mismatch`

The information on the ID document doesn’t match the information provided by the
user. Ask your user to verify and correct the provided information on the
account.

`verification_document_fraudulent`

`verification_document_manipulated`

The document might have been altered so it couldn’t be verified. Your team can
contact Stripe to learn more.

Below is a list of errors related to business verification:

ErrorResolution
`verification_failed_keyed_match`

`verification_failed_document_match`

The information on the account couldn’t be verified. Your user can either upload
a document to confirm their account details, or update their information on
their account.

`verification_failed_tax_id_not_issued`

`verification_failed_tax_id_match`

The information that your user provided couldn’t be verified with the IRS. Ask
your user to correct any possible errors in the company name or tax ID, or
upload a document that contains those fields. (US only)

`verification_failed_id_number_match`

`verification_failed_name_match`

`verification_failed_address_match`

The information on the document doesn’t match the information provided by the
user. Ask your user to verify and correct the provided information on the
account, or upload a document with information that matches the account.

`verification_document_address_missing`

`verification_document_id_number_missing`

`verification_document_name_missing`

The uploaded document is missing a required field. Ask your user to upload
another document that contains the missing field.

#### Caution

Don’t resubmit a file that previously failed. Duplicate uploads immediately
trigger an error and aren’t rechecked.

## Handle URL verification errors

URLs for e-commerce businesses need to conform to certain card network
standards. In order to comply with these standards, Stripe conducts a number of
verifications when reviewing URLs. To learn about best practices for URLs and
common elements for e-commerce businesses, see the [website
checklist](https://docs.stripe.com/get-started/checklist/website). There are two
methods to resolve URL verification errors:

- **Using the API**: Please see the list of error codes below in order to
understand and resolve the issue you are facing. If you need to update the URL,
use the [Update Account](https://docs.stripe.com/api/accounts/update) API, which
will trigger Stripe to verify the new URL. If you have made changes to the
website at the provided URL in order to resolve an error, but do not need to
make changes to the URL itself, you can trigger reverification by using the API
to change the URL to any other value and then change it back.
- **Using the Dashboard**: Platforms can use the [Accounts to
review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts)
page or the [Actions
required](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#actions-required)
list on the Account details page in the Stripe Dashboard to understand the
impact to their connected accounts and what actions to take.

Not all URL-related issues can be resolved using the API. Certain types of URL
verification errors require additional information on how to access the
connected account’s website or to attest that the account is exempt from URL
requirements. These types of issues require you or your connected account to
provide supplemental information.

In the Dashboard, visit your [Accounts to
review](https://dashboard.stripe.com/connect/accounts_to_review) page or check
the [Actions
required](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#actions-required)
list (if present) on the Account details page to resolve the error. If you can’t
resolve the issue, direct your connected account to [contact Stripe
Support](https://support.stripe.com/contact). For guidance on how to review your
accounts, see [Review actionable
accounts](https://docs.stripe.com/connect/dashboard/review-actionable-accounts).

#### Note

Stripe’s Terms of Service requires all e-commerce businesses to populate the
[business_profile.url](https://docs.stripe.com/api/accounts/object#account_object-business_profile-url)
property with a working URL of their business website when activating an account
with the `card_payments` capability. An account is considered an e-commerce
business if it promotes or sells any products or services through an online
website, social media profile, or mobile application. If the account doesn’t
operate a website to promote their business, sell products, or accept payments,
they’re required to provide
[business_profile.product_description](https://docs.stripe.com/api/accounts/object#account_object-business_profile-product_description)
instead. A product description needs to detail the type of products being sold
as well as the manner in which the account’s customers are being charged (e.g.
in person transactions). For more information, please see: [Business website for
account activation
FAQ](https://support.stripe.com/questions/business-website-for-account-activation-faq).

To help you handle the most common errors associated with the
`business_profile.url` field, the following table lists the related error codes
(in the `requirements.errors` array) and possible resolutions.

ErrorResolution`invalid_url_denylisted`The provided URL matches a generic
business website that Stripe believes is unrelated to the account. To resolve
the issue, provide a URL that is specific to the
business.`invalid_url_format`The provided URL is in the incorrect format. To
resolve the issue, provide a correctly formatted URL, such as
`https://example.com`.`invalid_url_website_inaccessible`We can’t reach the
website at the provided URL. If you block certain regions from viewing your
website, temporarily remove the blocker until your website has been
verified.`invalid_url_website_business_information_mismatch`Information on the
website at the provided URL does not match the information on the Stripe
account.`invalid_url_website_incomplete`The website at the provided URL is
missing either a business name or a clear description of goods and services
offered.`invalid_url_website_other`We are unable to verify the account’s
business using a website, social media profile, or mobile application at the
provided URL.`invalid_url_web_presence_detected`We have detected that the
account uses a website, social media profile, or mobile application to sell or
promote products or services, but a URL hasn’t been provided. To resolve the
issue, provide a
URL.`invalid_url_website_incomplete_customer_service_details`The website does
not contain customer service
details.`invalid_url_website_incomplete_return_policy`The website does not
contain a return policy and
process.`invalid_url_website_incomplete_refund_policy`The website does not
contain a refund policy.`invalid_url_website_incomplete_cancellation_policy`The
website does not contain a cancellation
policy.`invalid_url_website_incomplete_legal_restrictions`The website does not
contain applicable disclosures for products and services that are subject to
legal or export
restrictions.`invalid_url_website_incomplete_terms_and_conditions`The website
does not contain terms and
conditions.`invalid_url_website_incomplete_under_construction`We are unable to
verify the website at the provided URL, because the website is still under
construction.`invalid_url_website_inaccessible_password_protected`We are unable
to verify the website at the provided URL, because the website is
password-protected.`invalid_url_website_inaccessible_geoblocked`We are unable to
verify the website at the provided URL, because certain regions are blocked from
accessing it. If you block certain regions from viewing your website,
temporarily remove the blocker until your website has been
verified.`invalid_url_website_empty`We are unable to verify the website at the
provided URL, because the website has no content.
## Handle identity verification

You can respond in two ways to an identity verification change. The first is to
perform an [Update
Account](https://docs.stripe.com/connect/updating-service-agreements) call,
correcting or adding information.

Secondarily, we might ask you to upload a document. Depending on how much of the
user’s information Stripe has been able to verify, we might require three
different types of document uploads. You can determine what documents to upload
based on the fields listed in `requirements.currently_due`:

- `person.verification.document`: Requires a color scan or photo of an
acceptable form of ID.
- `person.verification.additional_document`: Requires a color scan or photo of a
document verifying the user’s address, such as a utility bill.
- `company.verification.document`: Requires a proof of entity document
establishing the business’ entity ID number, such as the company’s articles of
incorporation.

Uploading a document is a two-step process:

- Upload the file to Stripe
- Attach the file to the account

#### Note

For security reasons, Stripe doesn’t accept copies of IDs sent by email.

### Upload a file

To upload a file, use the [Create
File](https://docs.stripe.com/api/files/create) API by using a POST to send the
file data as part of a multipart/form-data request.

The uploaded file must meet these requirements:

- Color image (8,000 pixels by 8,000 pixels or smaller)
- 10 MB or less
- Identity documents are JPG or PNG format
- Address or legal entity documents are JPG, PNG, or PDF format

Pass the file data in the `file` parameter and set the `purpose` parameter to
`identity_document`:

```
curl https://files.stripe.com/v1/files \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -F "purpose"="identity_document" \
 -F "file"="@/path/to/a/file"
```

This request uploads the file and returns a token:

```
{
 "id": "{{FILE_ID}}",
 "created": 1403047735,
 "size": 4908
}
```

You may then use the token’s `id` value to attach the file to a connected
account for identity verification.

### Attach the file

After you upload the file and receive a representative token, provide the file
ID using the appropriate field in your [Update
Account](https://docs.stripe.com/connect/updating-service-agreements) call.

Below is an example for an ID document:

```
curl
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons/{{PERSON_ID}}
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "verification[document][front]"={{FILE_ID}}
```

Below is an example for a company document:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "company[verification][document][front]"={{FILE_ID}}
```

This update changes `verification.status` to `pending`. If an additional person
needs to be verified, use the [Persons](https://docs.stripe.com/api/persons) API
to update them.

### Confirm ID verification

If the color scan or photo of the ID passes Stripe’s checks, the document
requirement is removed from `requirements.currently_due`. Satisfying all
verification requirements for the person or company triggers an
`account.updated` webhook notification signaling the verification process is
complete.

Verification can take Stripe from a few minutes, to a couple business days to
complete, depending on how readable the provided image is.

If the verification attempt fails, the `requirements.errors` array contains an
error stating the cause. The `error[reason]`, such as “The image supplied isn’t
readable,” is safe to present to your user, but isn’t localized. The response
also contains an `error[code]` value, such as
`verification_document_not_readable`, which you can use to localize errors for
your users. Upon failure, `requirements.currently_due` indicates that a new ID
upload is required. If the deadline for verification is near,
`requirements.current_deadline` might also be populated with a date.
Verification failure also triggers an `account.updated` webhook notification.

## Handle risk verifications

#### New risk requirements

The following risk-related requirement data will be generally available on
November 12, 2024. You can opt in to receiving it sooner by following [the
instructions provided by Stripe
Support](https://support.stripe.com/questions/get-risk-related-requirements-for-connected-accounts-via-api).

Stripe reports risk and compliance requirements in the
[accounts.requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
attribute. These requirements follow the schema:
`<id>.<requirement_description>.<resolution_path>`:

- `id` uniquely identifies information needed by Stripe or our financial
partners. This identifier is always prefixed with `interv_` to indicate that it
is a risk verification requirement.
- `requirement_description` specifically describes the information needed to
complete the requirement, such as `identity_verification`, `rejection_appeal`,
and so on.
- `resolution_path` specifies how you or your connected account can provide the
requested information:- `challenge`: Connected accounts must directly respond to
challenge prompts. They often require sensitive information, such as a bank
account, or information that only the account owner can provide, such as a
selfie.
- `form`: Connected accounts can complete form requests, or you can complete
them on their behalf.
- `support`: The requirement isn’t directly actionable. Contact [Stripe
Support](https://support.stripe.com/).

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "requirements": {
 "current_deadline": 1234567800,
 "currently_due": [
 "{{REQUIREMENT_ID}}.restricted_or_prohibited_industry_diligence.form"
 ],
 "pending_verification": [],
 ...
 },
 ...
}
```

After satisfying a resolution path, the value of the requirement’s resolution
path might change to `support` and the requirement also appears in the
`pending_verification` section of the requirements hash. Stripe verifies the
submitted information and either dismisses the requirement as resolved or posts
a new currently due requirement.

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "requirements": {
 "current_deadline": 1234567800,
 "currently_due": [],
 "pending_verification": [
 "{{REQUIREMENT_ID}}.restricted_or_prohibited_industry_diligence.support"
 ],
 ...
 },
 ...
}
```

You can remediate risk and compliance requirements in any of the following ways,
depending on the type of requirement:

- **Connect embedded components:** You can [embed Connect
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
directly into your website. When a requirement surfaces, direct your users to
the [account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
embedded component, where they’re prompted to complete outstanding requirements
directly in your UI. Alternatively, use the [Notification
banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
embedded component to prompt your users for any outstanding requirements.
- **Stripe hosted onboarding:** You can generate links to direct your connected
accounts to complete outstanding requirements programmatically through account
links or manually in your [platform
Dashboard](https://docs.stripe.com/connect/dashboard/review-actionable-accounts).
- **Complete on behalf of your accounts:** You can use your [platform
Dashboard](https://docs.stripe.com/connect/dashboard/review-actionable-accounts)
to identify and complete form-based risk requirements from connected account
detail on behalf of your accounts.

The following `requirement_description` values are relevant to requirements
shown in the `account.requirements` attribute.

ValueDescription`business_model_verification`We require additional information
about the nature of the business to verify that we can support the
account.`restricted_or_prohibited_industry_diligence`The business might operate
in [a restricted category](https://stripe.com/legal/restricted-businesses) (for
example, selling alcohol, insurance, or financial products). Stripe might
require more information about the nature of the business or licensing
information to verify that we can support the
account.`intellectual_property_usage`The business might be selling products or
services that are protected by copyright. We require additional information to
verify that the account is authorized to sell those
products.`supportability_rejection_appeal`The Stripe terms of service prohibit
supporting the business. The account can appeal this
determination.`other_supportability_inquiry`We require additional information to
verify that we can support the account.`credit_review`We require additional
information about the nature of the business to verify that we can support the
account.`reserve_appeal`We’ve applied a reserve to the account. The reserve
doesn’t impact the account’s ability to accept payments with Stripe. The account
can appeal our determination.`identity_verification`The person responsible for
the account must verify their identify by uploading an ID document and a
selfie.`url_inquiry`The business URL must reflect the products and services that
it provides. Stripe might require them to change the URL before we can support
the account.`address_verification`We need to verify the address of the business
through document upload.`domain_verification`We need to verify that the account
owner controls the URL or domain that they
provided.`bank_account_verification`We need to verify bank account details
associated with the business.`customer_service_contact`We need to verify
customer service contact information associated with the
business.`fulfillment_policy`We need to verify the business’s fulfillment
policy.`product_description`The business’s Stripe account must include an
accurate product description.`statement_descriptor`We need a statement
descriptor that accurately reflects the business.`capability_disable_appeal`The
Stripe Terms of Service prohibit supporting specific capabilities associated
with this business. The account can appeal this
determination.`rejection_appeal`The Stripe Terms of Service prohibit supporting
the business due to the level of risk it presents. The account can appeal this
determination.`platform_concern`The platform initiated an intervention on its
own connected account. It can be a real intervention or an API integration
test.`other_compliance_inquiry`We require additional compliance information that
doesn’t fit any of the other descriptions.`other_business_inquiry`We require
additional business information that doesn’t fit any of the other descriptions.
## See also

- [Identity verification for connected
accounts](https://docs.stripe.com/connect/identity-verification)
- [Account tokens](https://docs.stripe.com/connect/account-tokens)
- [Testing Connect](https://docs.stripe.com/connect/testing)
- [Testing account identity
verification](https://docs.stripe.com/connect/testing-verification)
- [Required verification
information](https://docs.stripe.com/connect/required-verification-information)

## Links

- [Know Your Customer](https://support.stripe.com/questions/know-your-customer)
- [Connect](https://docs.stripe.com/connect)
- [Accounts](https://docs.stripe.com/api/accounts)
- [Persons](https://docs.stripe.com/api/persons)
- [payouts](https://docs.stripe.com/payouts)
- [service agreement
type](https://docs.stripe.com/connect/service-agreement-types)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
-
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
- [onboarding
flow](https://docs.stripe.com/connect/identity-verification#onboarding-flows)
- [Connect webhook](https://docs.stripe.com/connect/webhooks)
- [webhook settings](https://dashboard.stripe.com/account/webhooks)
-
[requirements.currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
- [change some of their
information](https://docs.stripe.com/connect/update-verified-information)
- [Update Account](https://docs.stripe.com/api/accounts/update)
- [Contact support](https://support.stripe.com/contact)
- [fetch an account](https://docs.stripe.com/api#retrieve_account)
- [Account](https://docs.stripe.com/api/accounts/object)
-
[requirements.disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-requirements-disabled_reason)
- [Accounts to
review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts)
- [Request and unrequest
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
-
[requirements.pending_verification](https://docs.stripe.com/api/accounts/object#account_object-requirements-pending_verification)
-
[requirements.errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
- [API
reference](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors-code)
- [set on an account](https://docs.stripe.com/connect/statement-descriptors)
-
[individual](https://docs.stripe.com/api/accounts/object#account_object-individual)
-
[requirements](https://docs.stripe.com/api/persons/object#person_object-requirements)
- [Acceptable verification documents by
country](https://docs.stripe.com/acceptable-verification-documents)
-
[company.verification](https://docs.stripe.com/api/accounts/object#account_object-company-verification)
- [website checklist](https://docs.stripe.com/get-started/checklist/website)
- [Actions
required](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#actions-required)
- [Accounts to review](https://dashboard.stripe.com/connect/accounts_to_review)
-
[business_profile.url](https://docs.stripe.com/api/accounts/object#account_object-business_profile-url)
-
[business_profile.product_description](https://docs.stripe.com/api/accounts/object#account_object-business_profile-product_description)
- [Business website for account activation
FAQ](https://support.stripe.com/questions/business-website-for-account-activation-faq)
- [Update Account](https://docs.stripe.com/connect/updating-service-agreements)
- [Create File](https://docs.stripe.com/api/files/create)
- [the instructions provided by Stripe
Support](https://support.stripe.com/questions/get-risk-related-requirements-for-connected-accounts-via-api)
-
[accounts.requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [Stripe Support](https://support.stripe.com/)
- [embed Connect
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
- [Notification
banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
- [a restricted category](https://stripe.com/legal/restricted-businesses)
- [Identity verification for connected
accounts](https://docs.stripe.com/connect/identity-verification)
- [Account tokens](https://docs.stripe.com/connect/account-tokens)
- [Testing Connect](https://docs.stripe.com/connect/testing)
- [Testing account identity
verification](https://docs.stripe.com/connect/testing-verification)
- [Required verification
information](https://docs.stripe.com/connect/required-verification-information)