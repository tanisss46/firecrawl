# Adds a new webhook event for when funds are deducted as part of a dispute

## What’s new

Adds a new [webhook event](https://docs.stripe.com/api/events) called
`funds_rescinded` that occurs when funds are deducted from your account for an
[Issuing dispute](https://docs.stripe.com/api/issuing/disputes).

Addedissuing_dispute.funds_rescindeddata.object
Occurs whenever funds are deducted from your account for an Issuing dispute.

## Impact

You can use the `funds_rescinded`
[event](https://docs.stripe.com/api/events/types#event_types-issuing_dispute.funds_rescinded)
to monitor when funds are deducted from your account due to an issuing dispute
(commonly due to Stripe clawing back a provisional credit). This is useful for
reacting to to money movements on your account (for example, kicking off
internal accounting logic).

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsissuing_dispute.funds_rescindedAdded[Event.type](https://docs.stripe.com/api/events/object#event_object-type)[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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

- [Updates the default value for shipping address
validation](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation)
- [Adds address validation for physical
cards](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-address-validation)

## Links

- [webhook event](https://docs.stripe.com/api/events)
- [Issuing dispute](https://docs.stripe.com/api/issuing/disputes)
-
[event](https://docs.stripe.com/api/events/types#event_types-issuing_dispute.funds_rescinded)
- [Event.type](https://docs.stripe.com/api/events/object#event_object-type)
-
[WebhookEndpoint#create.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/create#create_webhook_endpoint-enabled_events)
-
[WebhookEndpoint#update.enabled_events[]](https://docs.stripe.com/api/webhook_endpoints/update#update_webhook_endpoint-enabled_events)
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
- [Updates the default value for shipping address
validation](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation)
- [Adds address validation for physical
cards](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-address-validation)