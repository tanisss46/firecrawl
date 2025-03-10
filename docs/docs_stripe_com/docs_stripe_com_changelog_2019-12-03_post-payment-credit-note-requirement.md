# New requirement for out_of_band_amount when creating post-payment credit notesBreaking changes

## What’s new

When [creating](https://docs.stripe.com/api/credit_notes/create) a post-payment
credit note on an invoice,
[out_of_band_amount](https://docs.stripe.com/api/credit_notes/create#create_credit_note-out_of_band_amount)
is now required if the sum of `credit_amount` and (`refund` or `refund_amount`)
is less than the credit note total. In previous API versions
`out_of_band_amount` is optional and, in the case that the `credit_amount` and
refund amounts are less than the credit note total, the difference was
automatically be allocated to the `out_of_band_amount`.

## Impact

This enforces more explicit specification of the credit note details, ensuring
that all components of the credit note are clearly defined. It removes the
previous automatic allocation of the difference to `out_of_band_amount`, which
gives you greater control and transparency over the credit note creation
process.

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

- [creating](https://docs.stripe.com/api/credit_notes/create)
-
[out_of_band_amount](https://docs.stripe.com/api/credit_notes/create#create_credit_note-out_of_band_amount)
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