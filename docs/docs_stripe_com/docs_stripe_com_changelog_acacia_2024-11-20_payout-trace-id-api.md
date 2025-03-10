# Trace payouts with a unique identifier

## What’s new

Introduces a
[trace_id](https://docs.stripe.com/api/payouts/object#payout_object-trace_id)
field on the [Payout](https://docs.stripe.com/api/payouts) resource.

[Trace IDs](https://docs.stripe.com/payouts/trace-id) are unique identifiers for
payouts that our banking partners create to help you track missing or delayed
payouts. If an expected payout hasn’t settled in your bank account after 10
business days, contact your bank for an update and provide the trace ID.

For Connect users, you can provide your connected accounts their payout trace
IDs by [retrieving them from the Stripe
API](https://docs.stripe.com/api/payouts/retrieve).

This enables your connected accounts to self-serve their late or missing payouts
without the need for manual support intervention.

The `trace_id` contains two sub-fields:
[value](https://docs.stripe.com/api/payouts/object#payout_object-trace_id-value)
and
[status](https://docs.stripe.com/api/payouts/object#payout_object-trace_id-status):

- `value`: The trace ID string that we retrieve from our banking partners when a
payout is paid.
- `status`: The current status of the trace ID during retrieval from our banking
partners.
StatusDescription`pending`After you mark a payout as paid, Stripe attempts to
retrieve the trace ID from the banking partner for up to 10 days. During this
time the `status` becomes `pending`.`supported`After the banking partner
provides the trace ID, the `status` becomes `supported` and Stripe updates the
`value`.`unsupported`Some scenarios prevent providing the trace ID, such as a
payout failure or an unsupported country and currency combination. In these
cases the `status` is `unsupported`.
## Impact

You can get the trace ID for a specific payout by [retrieving the
payout](https://docs.stripe.com/api/payouts/retrieve).

For Connect users, providing the trace ID to your connected accounts allows you
to:

- Minimize support requests from your connected accounts relating to late or
missing payouts.
- Improve user satisfaction by letting your connected accounts self-serve their
late or missing payout investigations with their bank.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointstrace_idAdded[Payout](https://docs.stripe.com/api/payouts/object)
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

## Links

- [trace_id](https://docs.stripe.com/api/payouts/object#payout_object-trace_id)
- [Payout](https://docs.stripe.com/api/payouts)
- [Trace IDs](https://docs.stripe.com/payouts/trace-id)
- [retrieving them from the Stripe
API](https://docs.stripe.com/api/payouts/retrieve)
-
[value](https://docs.stripe.com/api/payouts/object#payout_object-trace_id-value)
-
[status](https://docs.stripe.com/api/payouts/object#payout_object-trace_id-status)
- [Payout](https://docs.stripe.com/api/payouts/object)
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