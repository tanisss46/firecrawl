# Adds disabled reason to invoices, subscriptions, and schedules

## What’s new

Adds a `disabled_reason` field under `invoice.automatic_tax` on the [Invoice
object](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-disabled_reason),
`subscription.automatic_tax` on the [Subscription
object](https://docs.stripe.com/api/subscriptions/object#subscription_object-automatic_tax-disabled_reason),
and `subscription_schedule.default_settings.automatic_tax` along with
`subscription_schedule.phases.automatic_tax` on the [Subscription Schedule
object](https://docs.stripe.com/api/subscription_schedules/object).

## Impact

This field allows you to identify when Stripe disabled automatic tax during
invoice finalization because of a missing or incomplete location for your
customer.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsdisabled_reasonAdded[Invoice.automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax)[Subscription.automatic_tax](https://docs.stripe.com/api/subscriptions/object#subscription_object-automatic_tax)[SubscriptionSchedule.default_settings.automatic_tax](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings-automatic_tax)
+ 1 more
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

- [Adds support for tax ID types in 19 new
countries](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-ids-19-new-countries)
- [Adds support for 21 new countries to the Tax Registration
API](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries)

## Links

- [Invoice
object](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-disabled_reason)
- [Subscription
object](https://docs.stripe.com/api/subscriptions/object#subscription_object-automatic_tax-disabled_reason)
- [Subscription Schedule
object](https://docs.stripe.com/api/subscription_schedules/object)
-
[Invoice.automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax)
-
[Subscription.automatic_tax](https://docs.stripe.com/api/subscriptions/object#subscription_object-automatic_tax)
-
[SubscriptionSchedule.default_settings.automatic_tax](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-default_settings-automatic_tax)
-
[SubscriptionSchedule.phases[].automatic_tax](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-automatic_tax)
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
- [Adds support for tax ID types in 19 new
countries](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-ids-19-new-countries)
- [Adds support for 21 new countries to the Tax Registration
API](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries)