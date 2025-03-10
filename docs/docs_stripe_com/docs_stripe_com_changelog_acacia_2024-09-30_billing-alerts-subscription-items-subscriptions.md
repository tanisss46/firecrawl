# Adds support for subscriptions and subscription items to billing alerts

## What’s new

Adds [Subscriptions](https://docs.stripe.com/api/subscriptions) and
[Subscription Items](https://docs.stripe.com/api/subscription_items) to the
[billing alerts and
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds)
you can configure to monitor when customers reach specific usage levels.

Addedfilter.subscription_itemstring
Filters to limit the scope of an alert to subscription items.

Addedfilter.subscriptionstring
Filters to limit the scope of an alert to subscriptions.

[POST /v1/billing/alertsCreate an alert for subscriptions or subscription items
that exceed specific usage
thresholds.](https://docs.stripe.com/api/billing/alert/create#create_billing_alert-filter)
## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParametersChangeResources or
endpointssubscription_itemsubscriptionAdded[Billing.Alert#create.filter](https://docs.stripe.com/api/billing/alert/create)
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

- [Adds contextual filters to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters)
- [Adds an Alerts API for usage-based
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)

## Links

- [Subscriptions](https://docs.stripe.com/api/subscriptions)
- [Subscription Items](https://docs.stripe.com/api/subscription_items)
- [billing alerts and
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds)
- [POST /v1/billing/alertsCreate an alert for subscriptions or subscription
items that exceed specific usage
thresholds.](https://docs.stripe.com/api/billing/alert/create#create_billing_alert-filter)
-
[Billing.Alert#create.filter](https://docs.stripe.com/api/billing/alert/create)
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
- [Adds contextual filters to billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters)
- [Adds an Alerts API for usage-based
billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alerts](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds billing alert resources and
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds Meter Event v2 API
endpoints](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)