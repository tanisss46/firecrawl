# Adds new enum values for request history reasonsBreaking changes

## What’s new

Adds new values to the [Issuing
Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
`request_history.reason` enum:

- `card_canceled`
- `card_expired`
- `cardholder_blocked`
- `insecure_authorization_method`
- `pin_blocked`

## Impact

Adds new values to the
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
property for the [Issuing
Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
resource. You can now more precisely track and understand why specific
authorization requests were made

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-06-20`
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

- [Issuing
Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
-
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
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