# Adds support for the Payment Element on a Customer Session

## What’s new

Lets you configure the Payment Element within a [Customer
Session](https://docs.stripe.com/api/customer_sessions), which you can use to
save a customer’s payment methods.

Addedcomponents.payment_elementobject
Configuration for the Payment Element.

## Impact

This enables support for [saved payment
methods](https://docs.stripe.com/payments/save-customer-payment-methods) within
Payment Element.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointspayment_elementAdded[CustomerSession#create.components](https://docs.stripe.com/api/customer_sessions/create#create_customer_session-components)[CustomerSession.components](https://docs.stripe.com/api/customer_sessions/object#customer_session_object-components)
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

- [Customer Session](https://docs.stripe.com/api/customer_sessions)
- [saved payment
methods](https://docs.stripe.com/payments/save-customer-payment-methods)
-
[CustomerSession#create.components](https://docs.stripe.com/api/customer_sessions/create#create_customer_session-components)
-
[CustomerSession.components](https://docs.stripe.com/api/customer_sessions/object#customer_session_object-components)
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