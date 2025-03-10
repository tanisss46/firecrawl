# Adds support for authorizers to Person API

## What’s new

Adds the authorizer role as a parameter in the `relationship` field of the
Person API.

The Stripe account
[representative](https://docs.stripe.com/api/persons/object#person_object-relationship)
is defined as the person that’s authorized to act as the primary representative
of the account. This person provides information about themselves and is
designated by the business to provide general information about the account.

To fulfill [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
(KYC) requirements, Stripe might be required to verify the [authority of the
representative](https://support.stripe.com/questions/representative-authority-verification).
If the representative on the Stripe account doesn’t match a registered
representative for the business, you can add an authorizer to the account to
grant them authority to represent the business.

An authorizer is usually a person that qualifies as a registered representative
for the business, but isn’t listed as a representative on the business Stripe
account. Stripe might request additional information, such as a [company
authorization
document](https://docs.stripe.com/api/persons/create#create_person-documents-company_authorization),
that allows the authorizer to transfer authority (to authorize) the
representative.

There can only be one authorizer on a Stripe account. The authorizer can’t be
the account representative. This role is only available in countries where the
authorizer can transfer authority to the representative.

```
curl https://api.stripe.com/v1/accounts/acct_xxxxx/persons \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d first_name=John \
 -d last_name=Doe \
 -d "relationship[authorizer]"=true
```

## Impact

You can use the new authorizer `relationship` field to create an authorizer for
your connected accounts. Use this authorizer to satisfy authority verification
requirements on your connected account.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsauthorizerAdded[Account#persons.relationship](https://docs.stripe.com/api/persons/list#list_person-relationship)[Token#create.person.relationship](https://docs.stripe.com/api/tokens/create_person#create_person_token-person-relationship)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-11-20.acacia`
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

## Links

-
[representative](https://docs.stripe.com/api/persons/object#person_object-relationship)
- [Know Your
Customer](https://support.stripe.com/questions/know-your-customer-obligations)
- [authority of the
representative](https://support.stripe.com/questions/representative-authority-verification)
- [company authorization
document](https://docs.stripe.com/api/persons/create#create_person-documents-company_authorization)
-
[Account#persons.relationship](https://docs.stripe.com/api/persons/list#list_person-relationship)
-
[Token#create.person.relationship](https://docs.stripe.com/api/tokens/create_person#create_person_token-person-relationship)
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