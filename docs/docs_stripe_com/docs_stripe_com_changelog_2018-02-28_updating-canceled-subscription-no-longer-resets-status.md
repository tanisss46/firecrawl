# Updating a canceled subscription on a future date no longer resets its statusBreaking changes

## What’s new

Updating a subscription set to cancel on a future date no longer clears the
cancellation status. To clear the cancellation status, specify
[cancel_at_period_end=false](https://docs.stripe.com/api#update_subscription-cancel_at_period_end)
when updating a subscription.

## Impact

This change maintains the future cancellation status of a subscription when it’s
updated, unless explicitly cleared. You must now specify
`cancel_at_period_end=false` to remove a planned cancellation when updating a
subscription. This modification provides more control over subscription
cancellation management, but might require updates to existing code that assumes
updating a subscription automatically clears its cancellation status.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2018-02-28`
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
[cancel_at_period_end=false](https://docs.stripe.com/api#update_subscription-cancel_at_period_end)
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