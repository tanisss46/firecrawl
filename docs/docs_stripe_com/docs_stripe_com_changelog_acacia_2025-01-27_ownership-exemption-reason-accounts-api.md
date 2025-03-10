# Adds support for ownership exemption reason to the Accounts API

## What’s new

Adds the `ownership_exemption_reason` parameter to the
[company](https://docs.stripe.com/api/accounts/update#update_account-company)
field of the [Accounts](https://docs.stripe.com/api/accounts/object) resource.

[Ultimate beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
are persons that, directly or indirectly, own a significant share and/or
exercise significant control over your business. These persons are usually
represented as
[owners](https://docs.stripe.com/api/persons/object#person_object-relationship-owner),
[directors](https://docs.stripe.com/api/persons/object#person_object-relationship-director),
or
[executives](https://docs.stripe.com/api/persons/object#person_object-relationship-executive)
on a Stripe account.

To fulfill [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
(KYC) requirements, Stripe can [collect, match, and
verify](https://support.stripe.com/questions/company-beneficial-ownership-and-director-requirement)
the ultimate beneficial owners for a business. Some businesses might qualify for
an exception to the standard process for collecting and verifying ultimate
beneficial owners. When businesses qualify for an exception, they can submit an
*ownership exemption reason* that resolves ultimate beneficial ownership
requirements and verifications from their account.

After you submit an ownership exemption reason, Stripe verifies the exemption
reason in lieu of verifying the ultimate beneficial owners on the account.
Stripe might reach out to either the account or the platform to collect
additional documentation to complete this verification.

Stripe currently supports two ownership exemption reasons:

- `qualified_entity_exceeds_ownership_threshold`: A qualified entity or set of
qualified entities own a significant share of the account’s business.
- `qualifies_as_financial_institution`: The account qualifies as a financial
institution.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/ \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
-d
"company[ownership_exemption_reason]"=qualified_entity_exceeds_ownership_threshold
```

The ownership exemption reason isn’t supported in all countries. Accounts that
can use this process receive the `ownership_exemption_reason` requirement in
their
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
field. If verification of the ownership exemption reason fails, the account
receives the `verification_rejected_ownership_exemption_reason` [error
code](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
on the requirement and must complete the standard process for ultimate
beneficial ownership verification.

If providing an ownership exemption reason is supported, you see
country-specific guidelines with supported reasons and their definitions.

For example, in Singapore qualified entities are defined as government entities,
public companies, and financial institutions. The ownership threshold is defined
as 75%.

For an account in Singapore to declare that a qualified entity exceeds ownership
threshold, one or more government entities, public companies, or financial
institutions must own 75% or more of the account’s company.

## Impact

You can use the ownership exemption reason field to declare that your connected
account qualifies for an exception to the standard process for ultimate
beneficial ownership verification. This removes requirements and verifications
for ultimate beneficial owners and triggers a verification based on the
ownership exemption reason instead.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsownership_exemption_reasonAdded[Account#create.company](https://docs.stripe.com/api/accounts/create#create_account-company)[Account#update.company](https://docs.stripe.com/api/accounts/update#update_account-company)[Account.company](https://docs.stripe.com/api/accounts/object#account_object-company)
+ 1 more
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

- [Adds directorship declaration to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/directorship-declaration)
- [Adds proof of ultimate beneficial ownership as a document
type](https://docs.stripe.com/changelog/acacia/2025-01-27/proof-of-ultimate-beneficial-ownership-document-support)

## Links

- [company](https://docs.stripe.com/api/accounts/update#update_account-company)
- [Accounts](https://docs.stripe.com/api/accounts/object)
- [Ultimate beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
-
[owners](https://docs.stripe.com/api/persons/object#person_object-relationship-owner)
-
[directors](https://docs.stripe.com/api/persons/object#person_object-relationship-director)
-
[executives](https://docs.stripe.com/api/persons/object#person_object-relationship-executive)
- [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
- [collect, match, and
verify](https://support.stripe.com/questions/company-beneficial-ownership-and-director-requirement)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [error
code](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
-
[Account#create.company](https://docs.stripe.com/api/accounts/create#create_account-company)
-
[Account.company](https://docs.stripe.com/api/accounts/object#account_object-company)
-
[Token#create.account.company](https://docs.stripe.com/api/tokens/create_account#create_account_token-account-company)
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
- [Adds directorship declaration to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/directorship-declaration)
- [Adds proof of ultimate beneficial ownership as a document
type](https://docs.stripe.com/changelog/acacia/2025-01-27/proof-of-ultimate-beneficial-ownership-document-support)