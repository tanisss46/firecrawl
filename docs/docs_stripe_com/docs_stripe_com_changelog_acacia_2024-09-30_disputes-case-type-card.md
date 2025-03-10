# Adds support for identifying the case type for card disputes

## What’s new

Adds the `case_type`
[enum](https://docs.stripe.com/api/disputes/object#dispute_object-payment_method_details-card-case_type)
to [Disputes](https://docs.stripe.com/api/issuing/disputes).

Addedcase_typeenum
The type of dispute opened. Different case types may have varying fees and
financial impact.

## Impact

Lets you determine the case type for a card dispute (chargeback or inquiry).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointscase_typeAdded[Dispute.payment_method_details.card](https://docs.stripe.com/api/disputes/object#dispute_object-payment_method_details-card)
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

-
[enum](https://docs.stripe.com/api/disputes/object#dispute_object-payment_method_details-card-case_type)
- [Disputes](https://docs.stripe.com/api/issuing/disputes)
-
[Dispute.payment_method_details.card](https://docs.stripe.com/api/disputes/object#dispute_object-payment_method_details-card)
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