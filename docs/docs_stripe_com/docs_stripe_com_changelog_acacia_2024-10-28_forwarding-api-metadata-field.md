# Adds a metadata field to the Vault and Forward API

## What’s new

This change adds a [metadata field](https://docs.stripe.com/api/metadata) to the
[Vault and Forward API](https://docs.stripe.com/payments/vault-and-forward). You
can add additional information when you [create a forwarding
request](https://docs.stripe.com/api/forwarding/forwarding_requests/create).

## Impact

The new metadata field lets you perform reconciliation on forwarding requests.
Previously, you had to rely on the [idempotency
key](https://docs.stripe.com/error-low-level#sending-idempotency-keys) to
attribute forwarding requests to specific customers or invoices.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsmetadataAdded[Forwarding.Request#create](https://docs.stripe.com/api/forwarding/forwarding_requests/create)[Forwarding.Request](https://docs.stripe.com/api/forwarding/request/object)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
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

- [Adds Polish PLN currency support to Terminal tipping
configuration](https://docs.stripe.com/changelog/acacia/2024-10-28/terminal-tipping-pln)
- [Supports domain registration for Amazon
Pay](https://docs.stripe.com/changelog/acacia/2024-10-28/amazon-pay-domain-registration)

## Links

- [metadata field](https://docs.stripe.com/api/metadata)
- [Vault and Forward API](https://docs.stripe.com/payments/vault-and-forward)
- [create a forwarding
request](https://docs.stripe.com/api/forwarding/forwarding_requests/create)
- [idempotency
key](https://docs.stripe.com/error-low-level#sending-idempotency-keys)
- [Forwarding.Request](https://docs.stripe.com/api/forwarding/request/object)
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
- [Adds Polish PLN currency support to Terminal tipping
configuration](https://docs.stripe.com/changelog/acacia/2024-10-28/terminal-tipping-pln)
- [Supports domain registration for Amazon
Pay](https://docs.stripe.com/changelog/acacia/2024-10-28/amazon-pay-domain-registration)