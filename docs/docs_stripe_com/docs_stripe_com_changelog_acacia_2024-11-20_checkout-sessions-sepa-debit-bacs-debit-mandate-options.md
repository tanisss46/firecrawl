# Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference prefixes in Checkout Sessions

## What’s new

We added the following API parameter to payment method options for SEPA Direct
Debit and Bacs Direct Debit in [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions):

- `bacs_debit.mandate_options.reference_prefix`
- `sepa_debit.mandate_options.reference_prefix`

## Impact

This change lets you specify mandate options when using Checkout with SEPA
Direct Debit or Bacs Direct Debit.

You can specify a prefix in the `mandate_options.reference_prefix` parameter to
customize either the [SEPA Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-sepa_debit-reference)
or [Bacs Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference)
in Payment and Setup modes.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsmandate_optionsAdded[Checkout.Session#create.payment_method_options.bacs_debit](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-bacs_debit)[Checkout.Session#create.payment_method_options.sepa_debit](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-sepa_debit)[Checkout.Session.payment_method_options.bacs_debit](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-bacs_debit)
+ 1 more
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
- [Specifying an originating payment method for Inbound Transfers is now
optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)
- [Use configurable capture methods and set up future usage for South Korean
payment
methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)

## Links

- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [SEPA Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-sepa_debit-reference)
- [Bacs Direct Debit Mandate
reference](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference)
-
[Checkout.Session#create.payment_method_options.bacs_debit](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-bacs_debit)
-
[Checkout.Session#create.payment_method_options.sepa_debit](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-sepa_debit)
-
[Checkout.Session.payment_method_options.bacs_debit](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-bacs_debit)
-
[Checkout.Session.payment_method_options.sepa_debit](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_options-sepa_debit)
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
- [Specifying an originating payment method for Inbound Transfers is now
optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)
- [Use configurable capture methods and set up future usage for South Korean
payment
methods](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)