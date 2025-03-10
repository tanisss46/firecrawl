# Renames and updates subscription schedule renewal propertiesBreaking changes

## What’s new

Includes multiple changes to subscription schedules:

- Renames `renewal_behavior` to `end_behavior`, and `cancel` and `release`
values.
- Removes `renewal_interval`.

A side effect of this change is that if you wrote a `renewal_behavior` of `none`
on an old API version, `end_behavior` is now converted to `cancel` when reading
the value back. In the event that you’re upgrading your API and set
`renewal_behavior` as `renew`, with this API version enabled, you’ll see
`end_behavior` as `renew`. However, you can no longer update `renewal_interval`,
or set `end_behavior` to `renew`, as it’s in a read-only state.

## Impact

Lets you more intuitively control how a subscription schedule ends using the
`end_behavior` property. The change handles backward compatibility by
automatically mapping the old `renewal_behavior` value of `none` to the new
cancel end behavior.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-10-17`
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