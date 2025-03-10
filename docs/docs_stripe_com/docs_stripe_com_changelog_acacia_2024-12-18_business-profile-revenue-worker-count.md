# Adds field-level permissions for revenue and worker count in an Account's business profile

## What’s new

Adds `undefined` as a possible value for the
`Account.business_profile.annual_revenue` and
`Account.business_profile.estimated_worker_count` parameters in
[Accounts](https://docs.stripe.com/api/accounts/object#account_object-business_profile)
API responses.

Previously, `Account.business_profile.annual_revenue` and
`Account.business_profile.estimated_worker_count` contained `null` or a value.
This change allows the API to return `undefined`, `null`, or a value. This
affects all API endpoints that return the
[Account](https://docs.stripe.com/api/accounts/object) object.

## Impact

This change allows you to differentiate how you handle responses returning the
`business_profile` of an Account object. You can update your integration to
handle the response differently depending on whether the `annual_revenue` and
`estimated_worker_count` parameters return `null` or `undefined`.

Even if you don’t handle the values differently, update your integration to
expect either value to make sure your integration remains compatible with all
possible API responses and prevents potential errors when processing Account
data.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETFieldsChangeFrom →
toAccount.business_profile.annual_revenueAccount.business_profile.estimated_worker_countChanged`required
→ optional`
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-12-18.acacia`
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
[Accounts](https://docs.stripe.com/api/accounts/object#account_object-business_profile)
- [Account](https://docs.stripe.com/api/accounts/object)
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