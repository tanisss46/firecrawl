# Adds parameter to link Verification Sessions to Customers

## What’s new

Adds `related_customer` to the Identity [Verification
Session](https://docs.stripe.com/api/identity/verification_sessions) resource.
When you
[create](https://docs.stripe.com/api/identity/verification_sessions/create) or
[update](https://docs.stripe.com/api/identity/verification_sessions/update) a
Verification Session, you can optionally include a token to reference an
existing [Customer](https://docs.stripe.com/api/customers).

Addedrelated_customernullable string
Token referencing a Customer resource.

## Impact

Linking [Customers](https://docs.stripe.com/api/customers) to their identity
verifications provides a more visibility into the risk profile of your customer
base, helping you make more informed decisions about onboarding, monitoring, and
risk mitigation.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsrelated_customerAdded[Identity.VerificationSession#create](https://docs.stripe.com/api/identity/verification_sessions/create)[Identity.VerificationSession#list](https://docs.stripe.com/api/identity/verification_sessions/list)[Identity.VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/object)
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

- [Verification
Session](https://docs.stripe.com/api/identity/verification_sessions)
- [create](https://docs.stripe.com/api/identity/verification_sessions/create)
- [update](https://docs.stripe.com/api/identity/verification_sessions/update)
- [Customer](https://docs.stripe.com/api/customers)
-
[Identity.VerificationSession#list](https://docs.stripe.com/api/identity/verification_sessions/list)
-
[Identity.VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/object)
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