# Adds new error codes to the Accounts, Persons, and Capabilities APIsBreaking changes

## What’s new

Adds several new error codes to the `requirements.errors` array in the Accounts,
Persons, and Capabilities API:

- `verification_document_issue_or_expiry_date_missing`
- `verification_document_not_signed`
- `verification_failed_tax_id_not_issued`
- `verification_failed_tax_id_match`
- `invalid_address_po_boxes_disallowed`

To learn more, see [Account requirements
errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors).

## Impact

By introducing these new error codes, you can more precisely determine the
nature of the verification failure, such as missing document details, unsigned
documents, or issues with tax IDs and addresses.

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

- [Account requirements
errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
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