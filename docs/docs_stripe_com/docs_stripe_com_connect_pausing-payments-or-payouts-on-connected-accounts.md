# Pause payments and payouts on connected accounts

## Support risk management by controlling the flow of funds into and out of your connected accounts.

Platforms can pause payments or [payouts](https://docs.stripe.com/payouts) on
accounts where they’re liable for negative balances, including Express and
Custom accounts, through the [Connected Account
details](https://docs.stripe.com/connect/dashboard/managing-individual-accounts)
Dashboard page. Unlike [rejecting an
account](https://docs.stripe.com/api/account/reject), you can pause payments or
payouts regardless of the connected account’s balance. You can unpause payments
or payouts at any time through the same page.

![Risk Action
Dropdown](https://b.stripecdn.com/docs-statics-srv/assets/risk-action-dropdown.2ae7b4d238c08427d9a9f67fbbeda87f.png)

## Effects of pausing payments or payouts

### Pausing payments

Pausing payments blocks creation of any charges. It also makes the
[transfer](https://docs.stripe.com/connect/account-capabilities#transfers),
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
and other [payment
methods](https://docs.stripe.com/connect/account-capabilities#payment-methods)
capabilities `inactive`.

### Pausing payouts

Pausing payouts blocks creation of both automatic and manual payouts. The pause
also stops processing of any in-flight payouts, which remain in `pending` status
for up to 10 days:

- If you unpause payouts within 10 days of a payout’s creation, the payout
resumes.
- If you don’t unpause payouts within 10 days of a payout’s creation, the payout
is canceled and the funds are returned to the connected account’s balance.

#### Note

You can pause payments in both live mode and test mode. However, in test mode we
don’t enforce it. Pausing payments in test mode deactivates the corresponding
capabilities on the account, but that doesn’t block the creation of charges.

After performing an action on a connected account, you can view the change in
the account’s status, which is reflected in the Accounts API. In the API
response for the connected account, the `charges_enabled` or `payouts_enabled`
fields return `false` depending on the action taken, and the `requirements` hash
has a `disabled_reason` of `platform_paused`.

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 ...
 "charges_enabled": false,
 "payouts_enabled": false,
 "requirements": {
 "disabled_reason": "platform_paused"
 }
}
```

### Filter connected accounts by risk action

By visiting the [Connected Account
list](https://docs.stripe.com/connect/dashboard/viewing-all-accounts) page, you
can filter for the accounts that you have restricted either payments or payouts
for.

![Filter by risk
action](https://b.stripecdn.com/docs-statics-srv/assets/risk-action-filter.e5de33081fc98d114e3082284a251f6f.png)

### Connected account notifications

Actioned accounts with access to the Express Dashboard see a notice there,
explaining that their platform paused payments or payouts on their account, and
telling them to direct any questions to their platform.

Actioned accounts without access to a Stripe-hosted Dashboard, including Custom
accounts, don’t see any communication from Stripe. You’re responsible for
notifying them when you pause their payments or payouts.

## Links

- [payouts](https://docs.stripe.com/payouts)
- [Connected Account
details](https://docs.stripe.com/connect/dashboard/managing-individual-accounts)
- [rejecting an account](https://docs.stripe.com/api/account/reject)
- [transfer](https://docs.stripe.com/connect/account-capabilities#transfers)
-
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
- [payment
methods](https://docs.stripe.com/connect/account-capabilities#payment-methods)
- [Connected Account
list](https://docs.stripe.com/connect/dashboard/viewing-all-accounts)