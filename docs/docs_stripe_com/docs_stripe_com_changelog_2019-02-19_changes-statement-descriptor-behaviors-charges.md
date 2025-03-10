# Changes statement descriptor behaviors for card payments created with ChargesBreaking changes

## What’s new

Changes statement descriptor behaviors for card payments created through
[/v1/charges](https://docs.stripe.com/api/charges/create). To learn more, see
our guide on [statement
descriptors](https://docs.stripe.com/payments/charges-api#dynamic-statement-descriptor).

- Instead of using the platform’s statement descriptor, charges created with
`on_behalf_of` or `destination` now use the descriptor of the connected account.
- The full statement descriptor for a card payment is no longer provided at
charge creation. Dynamic descriptors provided at charge time are now prefixed by
the descriptor prefix set in the dashboard or through the new
`settings[card_payments][statement_descriptor_prefix]` parameter in the Accounts
API.
- If an account has no `statement_descriptor` set, the account’s business or
legal name is used as the statement descriptor.
- Statement descriptors can no longer contain `*`, `, and `"`.

## Impact

This change alters how statement descriptors are handled for card payments
created through the Charges API, providing more accurate branding for connected
accounts and standardize descriptor formatting.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-02-19`
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

- [/v1/charges](https://docs.stripe.com/api/charges/create)
- [statement
descriptors](https://docs.stripe.com/payments/charges-api#dynamic-statement-descriptor)
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