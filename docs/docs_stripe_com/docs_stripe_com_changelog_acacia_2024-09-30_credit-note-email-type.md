# Adds support for email types to Credit Notes

## What’s new

Adds support for specifying whether to send a credit note email to customers
when creating a [Credit Note](https://docs.stripe.com/api/credit_notes), with
the default being `credit_note`.

Addedemail_typeenum
Type of email to send to the customer, one of `credit_note` or `none` and the
default is `credit_note`.

## Impact

This lets your customers choose to opt out of sending an email or to send a
refund email instead.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsemail_typeAdded[CreditNote#create](https://docs.stripe.com/api/credit_notes/create)[CreditNote#preview_lines](https://docs.stripe.com/api/credit_notes/preview_lines)[CreditNote#preview](https://docs.stripe.com/api/credit_notes/preview)
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

- [Credit Note](https://docs.stripe.com/api/credit_notes)
- [CreditNote#create](https://docs.stripe.com/api/credit_notes/create)
-
[CreditNote#preview_lines](https://docs.stripe.com/api/credit_notes/preview_lines)
- [CreditNote#preview](https://docs.stripe.com/api/credit_notes/preview)
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