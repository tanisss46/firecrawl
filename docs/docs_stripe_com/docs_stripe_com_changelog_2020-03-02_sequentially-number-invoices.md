# Invoices can now be numbered sequentially across your accountBreaking changes

## What’s new

You can now optionally number invoices [sequentially across your
account](https://docs.stripe.com/invoicing/customize#account-numbering) instead
of sequentially for each customer. To use this feature, enable [account level
numbering](https://dashboard.stripe.com/settings/billing/invoice) in the Stripe
Dashboard. To ensure invoices are numbered sequentially and without gaps,
invoices that can be deleted (drafts) are only assigned numbers when finalized.

## Impact

Lets you configure your Stripe account to number invoices sequentially across
the entire account, rather than sequentially for each individual customer. This
provides more flexibility and control over invoice numbering, as you can now
maintain a consistent, unified sequence of invoice numbers across your business.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2020-03-02`
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

- [sequentially across your
account](https://docs.stripe.com/invoicing/customize#account-numbering)
- [account level
numbering](https://dashboard.stripe.com/settings/billing/invoice)
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