# Displays CHIPS tracking details for outbound wire payments and transfers

## What’s new

Tracking details for US domestic wires sent through the CHIPS network is now
available in the `tracking_details.us_domestic_wire.chips` field for [Outbound
Payments](https://docs.stripe.com/api/treasury/outbound_payments) and [Outbound
Transfers](https://docs.stripe.com/api/treasury/outbound_transfers). See the
[upgrade
guide](https://docs.stripe.com/treasury/moving-money/moving-money-out-of-financial-accounts)
for more information about how to upgrade and use this feature.

## Impact

Enables tracking of a US domestic wires sent through the CHIPS network.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointschipsAdded[Treasury.OutboundPayment.testHelpers#update.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_update#test_mode_outbound_payment_update-tracking_details-us_domestic_wire)[Treasury.OutboundPayment.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_payments/object#outbound_payment_object-tracking_details-us_domestic_wire)[Treasury.OutboundTransfer.testHelpers#update.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_update#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire)
+ 1 moreFieldsChangeFrom →
toTreasury.OutboundPayment.tracking_details.us_domestic_wire.imadTreasury.OutboundTransfer.tracking_details.us_domestic_wire.imadChanged`string
→ nullable(string)`
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

- [Outbound Payments](https://docs.stripe.com/api/treasury/outbound_payments)
- [Outbound Transfers](https://docs.stripe.com/api/treasury/outbound_transfers)
- [upgrade
guide](https://docs.stripe.com/treasury/moving-money/moving-money-out-of-financial-accounts)
-
[Treasury.OutboundPayment.testHelpers#update.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_update#test_mode_outbound_payment_update-tracking_details-us_domestic_wire)
-
[Treasury.OutboundPayment.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_payments/object#outbound_payment_object-tracking_details-us_domestic_wire)
-
[Treasury.OutboundTransfer.testHelpers#update.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_update#test_mode_update_outbound_transfer-tracking_details-us_domestic_wire)
-
[Treasury.OutboundTransfer.tracking_details.us_domestic_wire](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-tracking_details-us_domestic_wire)
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