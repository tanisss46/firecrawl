# Adds proof of ultimate beneficial ownership as a document type

## What’s new

You can now use the `proof_of_ultimate_beneficial_ownership` document type on
the [Accounts API](https://docs.stripe.com/api/accounts/object) to upload
documentation that identifies [ultimate beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
(UBOs) of a business. This helps fulfill [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
(KYC) requirements.

[Ultimate beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
are persons that, directly or indirectly, own a significant share or exercise
significant control over your business. These persons are usually represented as
[owners](https://docs.stripe.com/api/persons/object#person_object-relationship-owner),
[directors](https://docs.stripe.com/api/persons/object#person_object-relationship-director),
or
[executives](https://docs.stripe.com/api/persons/object#person_object-relationship-executive)
on a Stripe account.

To satisfy UBO requirements, Stripe is required to [identify, collect, and
verify](https://support.stripe.com/questions/company-beneficial-ownership-and-director-requirement)
all owners that have a significant ownership stake or control in the business
(for most businesses, this is defined as having 25% or more ownership). When
businesses are owned by other businesses (holding companies) that have
significant ownership, Stripe is required to identify, collect, and verify all
significant owners of each holding company.

The proof of ultimate beneficial ownership document type isn’t supported in all
countries. Accounts that can use this document type receive the
`proof_of_ultimate_beneficial_ownership` requirement in their requirements
field. If the account supports providing a document for ultimate beneficial
ownership, you can validate the relationship by choosing one document from the
list of [Acceptable verification documents by
country](https://docs.stripe.com/acceptable-verification-documents).

After [uploading a file](https://docs.stripe.com/file-upload), you can attach it
to an account:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
-d
"documents[proof_of_ultimate_beneficial_ownership][files][]"=file_5dtoJkOhAxrMWb
```

## Impact

If your business has a complex ownership structure or involves foreign holding
companies, the existing KYC fields might not sufficiently capture your company’s
UBO declaration. The `proof_of_ultimate_beneficial_ownership` document provides
flexibility by providing an alternative method to comply with KYC requirements.

Some accounts might see a new proof of ultimate beneficial ownership requirement
as part of the [Upcoming requirement
updates](https://docs.stripe.com/connect/upcoming-requirements-updates).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsproof_of_ultimate_beneficial_ownershipAdded[Account#create.documents](https://docs.stripe.com/api/accounts/create#create_account-documents)[Account#update.documents](https://docs.stripe.com/api/accounts/update#update_account-documents)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2025-01-27.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Related changes

- [Adds support for ownership exemption reason to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)
- [Adds directorship declaration to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/directorship-declaration)

## Links

- [Accounts API](https://docs.stripe.com/api/accounts/object)
- [ultimate beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
- [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
-
[owners](https://docs.stripe.com/api/persons/object#person_object-relationship-owner)
-
[directors](https://docs.stripe.com/api/persons/object#person_object-relationship-director)
-
[executives](https://docs.stripe.com/api/persons/object#person_object-relationship-executive)
- [identify, collect, and
verify](https://support.stripe.com/questions/company-beneficial-ownership-and-director-requirement)
- [Acceptable verification documents by
country](https://docs.stripe.com/acceptable-verification-documents)
- [uploading a file](https://docs.stripe.com/file-upload)
- [Upcoming requirement
updates](https://docs.stripe.com/connect/upcoming-requirements-updates)
-
[Account#create.documents](https://docs.stripe.com/api/accounts/create#create_account-documents)
-
[Account#update.documents](https://docs.stripe.com/api/accounts/update#update_account-documents)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)
- [Adds support for ownership exemption reason to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)
- [Adds directorship declaration to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/directorship-declaration)