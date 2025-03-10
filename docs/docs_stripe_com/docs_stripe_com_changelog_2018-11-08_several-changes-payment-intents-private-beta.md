# Includes several changes for users of the Payment Intents API private beta Breaking changes

## What’s new

The following changes only affect users of PaymentIntents as part of the private
beta before November 15, 2018. If you didn’t use PaymentIntents before then, the
following changes don’t affect you:

- The `next_source_action` dictionary on PaymentIntents previously contained a
key called `value`. This replaces that with `authorize_with_url` and
`use_stripe_sdk` keys.
- When creating PaymentIntents, renames the `attempt_confirmation` parameter to
`confirm`.
- The PaymentIntent confirm endpoint no longer supports the `payment_intent`
parameter. To update a PaymentIntent’s source, pass `source` or `source_data` as
a top-level parameter.
- The `return_url` parameter is only allowed when confirming a PaymentIntent.
Passing `return_url` when updating a PaymentIntent is no longer allowed.
- When creating a PaymentIntent with `transfer_data[destination]`, you must
provide the `on_behalf_of` parameter, and it must match the account provided to
`transfer_data[destination]`. This is because when you provide a destination,
Stripe [settles charges in the country of the destination
account](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant).
- The `next_source_action` dictionary on PaymentIntents no longer contains the
`source_type` property. To view the source type when retrieving PaymentIntents,
[expand](https://docs.stripe.com/api/expanding_objects) the `source` parameter.

## Impact

This set of changes affects early Payment Intents beta users, modifying several
aspects of the API. These modifications require significant updates to existing
code that interacts with PaymentIntents, potentially impacting payment flow
logic, error handling, and data processing. You need to update you integration
to align with the new structure and requirements.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2018-11-08`
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

- [settles charges in the country of the destination
account](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)
- [expand](https://docs.stripe.com/api/expanding_objects)
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