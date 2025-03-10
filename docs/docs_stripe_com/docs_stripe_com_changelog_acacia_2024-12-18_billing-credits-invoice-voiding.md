# Adds support for reinstating Billing Credits on Invoice voiding

## What’s new

We added support for reinstating [Billing
Credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
when voiding an [Invoice](https://docs.stripe.com/invoicing).

## Impact

[Voiding an invoice](https://docs.stripe.com/api/invoices/void) with credits
applied reinstates the applied balance to the [credit
grant](https://docs.stripe.com/api/billing/credit-grant). If the credit grant is
past the [expiration
date](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-expires_at),
the reinstated credits expire immediately.

See [Billing credits integration
docs](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits#void-invoices-and-issue-credit-notes)
to learn more.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointscredits_application_invoice_voidedAdded[Billing.CreditBalanceTransaction.credit](https://docs.stripe.com/api/billing/credit-balance-transaction/object#billing_credit_balance_transaction_object-credit)FieldChangeFrom
→
toBilling.CreditBalanceTransaction.credit.typeChanged`literal('credits_granted')
→ enum('credits_application_invoice_voided'|'credits_granted')`
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-12-18.acacia`
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

- [Modify trial subscriptions created by Payment
Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api)
- [Billing Portal Configuration always returns period end date in
responses](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required)

## Links

- [Billing
Credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
- [Invoice](https://docs.stripe.com/invoicing)
- [Voiding an invoice](https://docs.stripe.com/api/invoices/void)
- [credit grant](https://docs.stripe.com/api/billing/credit-grant)
- [expiration
date](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-expires_at)
- [Billing credits integration
docs](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits#void-invoices-and-issue-credit-notes)
-
[Billing.CreditBalanceTransaction.credit](https://docs.stripe.com/api/billing/credit-balance-transaction/object#billing_credit_balance_transaction_object-credit)
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
- [Modify trial subscriptions created by Payment
Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api)
- [Billing Portal Configuration always returns period end date in
responses](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required)