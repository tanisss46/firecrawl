# Renames phases attributes in subscription schedulesBreaking changes

## What’s new

Renames `phases.plans` to `phases.items` on subscription schedules. This applies
for the [subscription
schedule](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases)
object, as well as the
[create](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases)
and
[update](https://docs.stripe.com/api/subscription_schedules/update#update_subscription_schedule-phases)
requests.

## Impact

By renaming `phases.plans` to `phases.items`, the terminology aligns better with
the broader concept of subscription items, rather than being limited to just
plans. This makes it easier to understand and manage the different components
that make up a subscription schedule.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2020-08-27`
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
schedule](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases)
-
[create](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases)
-
[update](https://docs.stripe.com/api/subscription_schedules/update#update_subscription_schedule-phases)
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