# Subscriptions are now successfully created even if the first payment failsBreaking changes

## What’s new

Creating a subscription succeeds even when the first payment fails. The
subscription is created in an incomplete status, where it remains for up to 23
hours. During that time period, it can be moved into an active state by paying
the first invoice. If no successful payment is made, the subscription moves into
a final `incomplete_expired` state. Updates to a `non-incomplete` subscription
that require a payment also succeed regardless of the payment status. Before
tjhis version, all creations or updates would fail if the corresponding payment
failed. For more details, see our guide on the [subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle).

## Impact

This change allows you to create subscriptions even when the initial payment
fails, introducing an `incomplete` status that lasts up to 23 hours. This gives
your users a grace period to resolve payment issues before a subscription
becomes `incomplete_expired`.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-03-14`
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

- [subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
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