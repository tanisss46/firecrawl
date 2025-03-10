# Customer balances are now returned when voiding invoicesBreaking changes

## What’s new

Customer balances applied to all invoices are now debited or credited back to
the customer when voided. Earlier, applied customer balances weren’t returned
back to the customer and were consumed. To achieve this behavior in earlier API
versions:

- Set `consume_applied_balance` to `false` when voiding invoices in
[/v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void).
- Set `invoice_customer_balance_settings[consume_applied_balance_on_void]` to
`false` in `/v1/subscriptions`
[create](https://docs.stripe.com/api/subscriptions/create) or
[update](https://docs.stripe.com/api/subscriptions/update) to force this
behavior for invoices voided by a subscription.
- Set
`subscription_data[invoice_customer_balance_settings][consume_applied_balance_on_void]`
to `false` in `/v1/checkout/sessions`
[create](https://docs.stripe.com/api/checkout/sessions/create) to force this
behavior for invoices voided by subscriptions created with Checkout.

## Impact

Lets you have customer balances properly credited back to the customer when
invoices are voided. Previously, any customer balances applied to the voided
invoices would be consumed and not returned to the customer, which led to
unexpected balance depletion.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-12-03`
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

- [/v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void)
- [create](https://docs.stripe.com/api/subscriptions/create)
- [update](https://docs.stripe.com/api/subscriptions/update)
- [create](https://docs.stripe.com/api/checkout/sessions/create)
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