# Converts properties on the Account object from a String to an enum

## What’s new

The following [Account](https://docs.stripe.com/api/accounts) properties now use
an enum value instead of a String:

-
[requirements.disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-requirements-disabled_reason)
-
[future_requirements.disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-disabled_reason)

## Impact

When Stripe disables an account, the reason is now based on a finite set of
enums rather than a String value. This change doesn’t add any new disabled
reasons.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETFieldsChangeFrom →
toAccount.future_requirements.disabled_reasonAccount.requirements.disabled_reasonChanged`string
→ enum`
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

- [Account](https://docs.stripe.com/api/accounts)
-
[requirements.disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-requirements-disabled_reason)
-
[future_requirements.disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-disabled_reason)
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