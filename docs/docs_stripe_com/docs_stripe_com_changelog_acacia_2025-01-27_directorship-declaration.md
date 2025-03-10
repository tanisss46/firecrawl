# Adds directorship declaration to the Accounts API

## What’s new

You can now use the `directorship_declaration.ip`,
`directorship_declaration.date`, and `directorship_declaration.user_agent`
parameters under the
[company](https://docs.stripe.com/api/accounts/update#update_account-company)
field in the [Accounts API](https://docs.stripe.com/api/accounts/object) to
attest that the list of directors on your Stripe account accurately reflects the
directors of your company. This helps fulfill [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
(KYC) requirements.

[Directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
are individuals who are members of your company’s governing board. These persons
are represented as
[directors](https://docs.stripe.com/api/persons/object#person_object-relationship-director)
on a Stripe account.

In certain countries, Stripe is required to collect the information of all
directors of your company and verify that their information match government
records. Accounts that are required to provide this information sees the
`company.directorship_declaration.ip` and
`company.directorship_decalaration.date` requirements in their
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
field.

After adding all directors to your account, attest that the list of directors is
current and correct by setting the `company.directorship_declaration.ip`,
`company.directorship_declaration.date`, and optionally the
`company.directorship_declaration.user_agent` fields in the Accounts API. These
fields represent the ip address, time, and browser user agent that were used at
the time of attestation.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/ \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "company[directorship_declaration][ip]"="67.180.161.149" \
 -d "company[directorship_declaration][date]"=1737936000 \
--data-urlencode "company[directorship_declaration][user_agent]"="Mozilla/5.0
(platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version"
```

If a discrepancy in your list of directors is detected, Stripe might request a
new declaration by returning the `company.directorship_declaration.ip`,
`company.directorship_declaration.date` requirements in the
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
field.

## Impact

Some accounts might see a new directorship declaration requirement as part of
the [upcoming requirement
updates](https://docs.stripe.com/connect/upcoming-requirements-updates).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsdirectorship_declarationAdded[Account#create.company](https://docs.stripe.com/api/accounts/create#create_account-company)[Account#update.company](https://docs.stripe.com/api/accounts/update#update_account-company)[Account.company](https://docs.stripe.com/api/accounts/object#account_object-company)
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

- [Adds support for ownership exemption reason to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)
- [Adds proof of ultimate beneficial ownership as a document
type](https://docs.stripe.com/changelog/acacia/2025-01-27/proof-of-ultimate-beneficial-ownership-document-support)

## Links

- [company](https://docs.stripe.com/api/accounts/update#update_account-company)
- [Accounts API](https://docs.stripe.com/api/accounts/object)
- [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
-
[Directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
-
[directors](https://docs.stripe.com/api/persons/object#person_object-relationship-director)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [upcoming requirement
updates](https://docs.stripe.com/connect/upcoming-requirements-updates)
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
- [Adds support for ownership exemption reason to the Accounts
API](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)
- [Adds proof of ultimate beneficial ownership as a document
type](https://docs.stripe.com/changelog/acacia/2025-01-27/proof-of-ultimate-beneficial-ownership-document-support)