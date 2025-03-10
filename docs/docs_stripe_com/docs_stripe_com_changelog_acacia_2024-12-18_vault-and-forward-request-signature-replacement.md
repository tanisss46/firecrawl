# Adds signature request as a replacement option for the Vault and Forward API

## What’s new

Adds `REQUEST_SIGNATURE` as a possible enum value for
[replacements](https://docs.stripe.com/api/forwarding/request/object#forwarding_request_object-replacements),
which defines the fields to be replaced in the forwarded request.

## Impact

Stripe can now support Vault and Forward requests that require calculating a
request hash as a part of the API. To do this, specify the `REQUEST_SIGNATURE`
[replacement](https://docs.stripe.com/api/forwarding/request/object#forwarding_request_object-replacements)
for relevant endpoints.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsrequest_signatureAdded[Forwarding.Request#create.replacements[]](https://docs.stripe.com/api/forwarding/forwarding_requests/create#forwarding_request_create-replacements)[Forwarding.Request.replacements[]](https://docs.stripe.com/api/forwarding/request/object#forwarding_request_object-replacements)
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
[replacements](https://docs.stripe.com/api/forwarding/request/object#forwarding_request_object-replacements)
-
[Forwarding.Request#create.replacements[]](https://docs.stripe.com/api/forwarding/forwarding_requests/create#forwarding_request_create-replacements)
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