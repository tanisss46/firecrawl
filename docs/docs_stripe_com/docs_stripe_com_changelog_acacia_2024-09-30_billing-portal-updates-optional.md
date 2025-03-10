# Makes it optional to update the products and prices of a subscription

## What’s new

If you’ve disabled subscription updates for [Customer Portal
Sessions](https://docs.stripe.com/api/customer_portal/sessions) (by setting
[subscription_update.enabled](https://docs.stripe.com/api/customer_portal/configurations/update#update_portal_configuration-features-subscription_update-enabled)
to `false`), you can now make the following update behaviors optional:

- `subscription_update.products`
- `default_allowed_updates`

## Impact

You won’t encounter a missing parameter error when you set
`subscription_update.enabled` to `false`.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETFieldsChangeFrom →
toBillingPortal.Configuration#create.features.subscription_update.default_allowed_updatesBillingPortal.Configuration#create.features.subscription_update.productsChanged`required
→ optional`
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

- [Customer Portal
Sessions](https://docs.stripe.com/api/customer_portal/sessions)
-
[subscription_update.enabled](https://docs.stripe.com/api/customer_portal/configurations/update#update_portal_configuration-features-subscription_update-enabled)
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