# Adds contextual filters to billing alertsBreaking changes

## What’s new

Moves the `filter` field inside of the [alert
type](https://docs.stripe.com/api/billing/alert/object#billing_alert_object-alert_type)
configuration as a list of `filters`. Also renames the alert type configuration
fields to drop the `_config` suffix.

Current API versionusage_threshold_configenum value
Use `usage_threshold_config` if you intend for an alert to fire when a usage
threshold on a meter is crossed.

Newusage_thresholdenum value
Use `usage_threshold` if you intend for an alert to fire when a usage threshold
on a meter is crossed.

## Why is this a breaking change?

Because this change moves the `filter` parameter into the alert configuration,
you can no longer apply the filter at the top level of alerts.

Additionally, you can no longer specify usage threshold configurations with
`usage_threshold_config` and instead must use `usage_threshold`.

## Impact

With this change, you can create filters that are unique to each alert type. You
can see the filters as part of the alert type configuration.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointsusage_thresholdAdded[Billing.Alert#create](https://docs.stripe.com/api/billing/alert/create)[Billing.Alert](https://docs.stripe.com/api/billing/alert/object)filterusage_threshold_configRemoved[Billing.Alert#create](https://docs.stripe.com/api/billing/alert/create)[Billing.Alert](https://docs.stripe.com/api/billing/alert/object)
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

## Related changes

- [Adds an Alerts API for usage-based
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)

## Links

- [alert
type](https://docs.stripe.com/api/billing/alert/object#billing_alert_object-alert_type)
- [Billing.Alert#create](https://docs.stripe.com/api/billing/alert/create)
- [Billing.Alert](https://docs.stripe.com/api/billing/alert/object)
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
- [Adds an Alerts API for usage-based
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)