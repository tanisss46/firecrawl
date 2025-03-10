# Specifying an originating payment method for Inbound Transfers is now optional

## What’s new

Modifies the
[origin_payment_method](https://docs.stripe.com/api/treasury/inbound_transfers/object#inbound_transfer_object-origin_payment_method_details)
property on the Inbound Transfer resource to be optional.

## Impact

This change makes Inbound Transfers compatible with new money movement rails,
such as check deposits.

All Inbound Transfers over the ACH network still require
[origin_payment_method](https://docs.stripe.com/api/treasury/inbound_transfers/object#inbound_transfer_object-origin_payment_method_details)
and return the field in responses.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETFieldChangeFrom →
toTreasury.InboundTransfer.origin_payment_methodChanged`string →
nullable(string)`
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-11-20.acacia`
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

- [Adds network decline code field for Swish and BLIK
refunds](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Use configurable capture methods and set up future usage for South Korean
payment
methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)

## Links

-
[origin_payment_method](https://docs.stripe.com/api/treasury/inbound_transfers/object#inbound_transfer_object-origin_payment_method_details)
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
- [Adds network decline code field for Swish and BLIK
refunds](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Use configurable capture methods and set up future usage for South Korean
payment
methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)