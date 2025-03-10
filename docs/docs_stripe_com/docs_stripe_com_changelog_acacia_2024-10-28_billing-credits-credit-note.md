# Adds support for pre-tax credit amount information to credit notes

## What’s new

Adds `pretax_credit_amounts` attribute to the `CreditNote` and
`CreditNoteLineItem` resources. This field contains information about billing
credits, along with other pre-tax credits like discounts, that were applied to
the original invoice for which a credit note was issued.

## Impact

You can now see a breakdown of credits applied to an invoice before tax
calculations, including discounts. This information shows which credit notes
were issued and how they relate to the invoice.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointspretax_credit_amountsAdded[CreditNote](https://docs.stripe.com/api/credit_notes/object)[CreditNoteLineItem](https://docs.stripe.com/api/credit_notes/line_item)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
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

- [Adds Credit Grant APIs and
resources](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis)
- [Adds support for pre-tax credit amount information to
invoices](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice)

## Links

- [CreditNote](https://docs.stripe.com/api/credit_notes/object)
- [CreditNoteLineItem](https://docs.stripe.com/api/credit_notes/line_item)
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
- [Adds Credit Grant APIs and
resources](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis)
- [Adds support for pre-tax credit amount information to
invoices](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice)