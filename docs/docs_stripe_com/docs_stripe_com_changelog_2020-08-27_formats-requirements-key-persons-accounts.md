# Formats requirements for key persons associated with accountsBreaking changes

## What’s new

The `requirements` hash on the `Account` and `Capability` objects, and the
`verification_fields` hash on the `Country Spec` object have newly formatted
strings for requirements that are related to key persons associated with an
account:

- Fields that are required for persons with `representative`, `owner`,
`director`, and `executive` roles will be prefixed with `representative`,
`owners`, `directors`, and `executives`, respectively. Person requirements are
previewed as follows:- When the representative’s phone number is required, it
appears as `representative.phone` instead of `relationship.representative`.
- When an owner’s full name is required, it appears as `owners.first_name` and
`owners.last_name` instead of `relationship.owner`.
- When an executive’s ID number is required, it appears as
`executives.id_number` instead of `relationship.executive`.
- When a director’s date of birth is required, it appears as
`directors.dob.day`, `directors.dob.month`, and `directors.dob.year` instead of
`relationship.director`.
- The boolean values that indicate the associated owners, executives, or
directors now appear as `company.owners_provided`,
`company.executives_provided`, or `company.directors_provided` instead of
`relationship.owner`, `relationship.executive`, or `relationship.director`,
respectively.

## Impact

The new formatting of the `requirements` and `verification_fields` hashes
creates a more intuitive naming convention, making it easier for you to identify
and address the specific information needed for each person role.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2020-08-27`
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