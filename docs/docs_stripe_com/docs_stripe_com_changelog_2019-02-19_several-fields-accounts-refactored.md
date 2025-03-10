# Several account fields have been refactored to better describe legal entity, verification status and requirements, and configurable settingsBreaking changes

## What’s new

Includes multiple changes:

- Replaces the `legal_entity` property on the Account API resource with
`individual`, `company`, and `business_type`.
- Replaces the `verification` hash with a `requirements` hash.
- Replaces the `verification[fields_needed]` array with three arrays to better
represent when information is required: `requirements[eventually_due]`,
`requirements[currently_due]`, and `requirements[past_due]`.
- Renames `verification[due_by]` to `requirements[current_deadline]`.
- Renames the `disabled_reason` enum value of `fields_needed` to
`requirements.past_due`.
- Moves properties on the `Account` object that configure behavior within Stripe
into the new `settings` hash.
- Moves the `payout_schedule`, `payout_statement_descriptor` and
`debit_negative_balances` fields to `settings[payouts]`, renaming them to
`schedule`, `statement_descriptor` and `debit_negative_balances`.
- Moves the `statement_descriptor` field to
`settings[payments][statement_descriptor]`.
- Moves `decline_charge_on` fields to `settings[card_payments]`, renaming it to
`decline_on`.
- Moves the `business_logo`, `business_logo_large` and `business_primary_color`
fields to `settings[branding]`, renaming them to `icon`, `logo` and
`primary_color`. Additionally, the `icon` field requires the image file you
upload to be a square.
- Moves the `display_name` and `timezone` fields to `settings[dashboard]`.

## Impact

This change significantly restructures the Account API resource, providing a
more structured and detailed approach to account information and settings. You
need to extensively update your code that interacts with the Account API.

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