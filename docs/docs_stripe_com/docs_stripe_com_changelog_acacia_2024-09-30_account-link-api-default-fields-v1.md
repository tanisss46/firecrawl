# Adds additional reasonable defaulting to the Account Link API v1

## What’s new

Applies `currently_due` as the default value for the `fields` parameter when you
[create an Account Link](https://docs.stripe.com/api/account_links/create).

## Impact

By automatically applying a default value for the `fields` parameter, you no
longer need to manually specify `fields` when specifying `future_requirements`
as a [collection
option](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETFieldChangeFrom →
toAccountLink#create.collection_options.fieldsChanged`required → optional`
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
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

- [create an Account Link](https://docs.stripe.com/api/account_links/create)
- [collection
option](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options)
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