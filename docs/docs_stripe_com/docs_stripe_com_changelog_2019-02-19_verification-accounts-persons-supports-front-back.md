# Verification of accounts or persons now supports uploading both front and back sidesBreaking changes

## What’s new

Changes the `legal_entity[verification][document]`, which is located at
`individual[verification]` and `verification` in the `Person` object, to a hash.

- The `front` and `back` fields support uploading both sides of documents.
- The `details_code` field has new error types: `document_corrupt`,
`document_failed_copy`, `document_failed_greyscale`, `document_failed_other`,
`document_failed_test_mode`, `document_fraudulent`,
`document_id_country_not_supported`, `document_id_type_not_supported`,
`document_invalid`, `document_manipulated`, `document_missing_back`,
`document_missing_front`, `document_not_readable`, `document_not_uploaded`,
`document_photo_mismatch`, and `document_too_large`.

## Impact

This change restructures the verification document property and expands error
reporting.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-02-19`
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