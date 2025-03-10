# Renames account_balance to balance on Customer objectBreaking changes

## What’s new

Renames the [Customer](https://docs.stripe.com/api/customers) object’s
`account_balance` value to `balance`. With this, a new [Customer Balance
Transactions API](https://docs.stripe.com/api/customer_balance_transactions) is
available:

- Updates the customer’s `balance` by incrementing or decrementing its current
value by a specified `amount` and attaching `metadata` to the change.
- Retrieves a history of changes to the customer’s `balance`.

## Impact

By renaming the `account_balance` property to `balance`, the terminology is now
better aligned with common usage. Additionally, the new Customer Balance
Transactions API provides you with the ability to directly update a customer’s
balance by incrementing or decrementing the value, as well as attach metadata to
these balance changes.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2019-10-17`
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

- [Customer](https://docs.stripe.com/api/customers)
- [Customer Balance Transactions
API](https://docs.stripe.com/api/customer_balance_transactions)
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