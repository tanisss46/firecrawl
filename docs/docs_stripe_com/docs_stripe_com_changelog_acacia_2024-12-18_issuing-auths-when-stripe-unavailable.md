# Creates Issuing authorizations when Stripe is unavailable

## What’s new

Creates [Issuing
authorizations](https://docs.stripe.com/api/issuing/authorizations/object) when
the card network responds on Stripe’s behalf because Stripe is unavailable. For
backwards compatibility, network-approved authorizations have a
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
value of `card_active`, while network-declined authorizations have a
`webhook_error` value. These authorizations trigger
`issuing_authorization.created` webhook events. Depending on the failure mode,
Stripe might also send an `issuing_authorization.request` webhook event.

## Impact

This change reveals what the cardholder experienced, in case the card network
can’t contact Stripe because of a Stripe error or outage.

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

## Related changes

- [Issuing authorizations now include merchant tax ID
number](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-merchant-tax-id)

## Links

- [Issuing
authorizations](https://docs.stripe.com/api/issuing/authorizations/object)
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
- [Issuing authorizations now include merchant tax ID
number](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-merchant-tax-id)