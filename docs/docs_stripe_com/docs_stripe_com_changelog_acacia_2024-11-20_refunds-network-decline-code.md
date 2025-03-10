# Adds network decline code field for Swish and BLIK refunds

## What’s new

Provides the decline code from our financial partners for failed Swish and BLIK
refunds.

## Impact

The decline code helps you understand why a refund failed.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsnetwork_decline_codeAdded[Refund.destination_details.blik](https://docs.stripe.com/api/refunds/object#refund_object-destination_details-blik)[Refund.destination_details.swish](https://docs.stripe.com/api/refunds/object#refund_object-destination_details-swish)
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

- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Specifying an originating payment method for Inbound Transfers is now
optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)
- [Use configurable capture methods and set up future usage for South Korean
payment
methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)

## Links

-
[Refund.destination_details.blik](https://docs.stripe.com/api/refunds/object#refund_object-destination_details-blik)
-
[Refund.destination_details.swish](https://docs.stripe.com/api/refunds/object#refund_object-destination_details-swish)
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
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Specifying an originating payment method for Inbound Transfers is now
optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)
- [Use configurable capture methods and set up future usage for South Korean
payment
methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)