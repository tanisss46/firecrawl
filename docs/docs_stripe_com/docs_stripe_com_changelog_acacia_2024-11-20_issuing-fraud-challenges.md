# Adds support for issuing fraud challenges

## What’s new

[Issuing](https://docs.stripe.com/issuing) users can now see [fraud
challenges](https://docs.stripe.com/issuing/controls/fraud-challenges) sent for
[Authorizations](https://docs.stripe.com/api/issuing/authorizations/object) in
the `fraud_challenges` array, which also contains the status and outcome of the
challenge.

A new `verified_by_fraud_challenge` field shows when fraud risk controls were
bypassed for an authorization due to a previously completed fraud challenge.

## Impact

Fraud challenges allow cardholders to retry transactions that were incorrectly
declined by Stripe Issuing’s fraud risk controls. You can enable fraud
challenges on the [Issuing
settings](https://dashboard.stripe.com/settings/issuing/authorizations)
Dashboard page.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsfraud_challengesverified_by_fraud_challengeAdded[Issuing.Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
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

## Related changes

- [Adds support for merchant amount and currency for test mode
authorizations](https://docs.stripe.com/changelog/acacia/2024-11-20/add-merchant-currency-and-merchant-amount-on-create-testmode-authorization-method)

## Links

- [Issuing](https://docs.stripe.com/issuing)
- [fraud challenges](https://docs.stripe.com/issuing/controls/fraud-challenges)
- [Authorizations](https://docs.stripe.com/api/issuing/authorizations/object)
- [Issuing
settings](https://dashboard.stripe.com/settings/issuing/authorizations)
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
- [Adds support for merchant amount and currency for test mode
authorizations](https://docs.stripe.com/changelog/acacia/2024-11-20/add-merchant-currency-and-merchant-amount-on-create-testmode-authorization-method)