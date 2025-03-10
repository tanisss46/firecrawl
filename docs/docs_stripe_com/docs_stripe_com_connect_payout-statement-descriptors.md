# Payout statement descriptors

## Understand and manage how Stripe payouts look on a connected account's bank statements.

The statement descriptor used for Connect payouts varies according to the
properties of the connected account and the conditions of the payout. There is a
precedence order used for
[manual](https://docs.stripe.com/connect/payout-statement-descriptors#manual-payouts)
and
[automatic](https://docs.stripe.com/connect/payout-statement-descriptors#automatic-payouts)
payouts.

Connected accounts can have a customized statement descriptor stored on the
Account object at
[settings.payout.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-statement_descriptor).

## Default statement descriptor

Connect platforms can configure a platform-wide default statement descriptor in
their [Connect
settings](https://dashboard.stripe.com/settings/connect/payouts/statement-descriptor),
which is also used under certain criteria. Even when the precedence order falls
to it, the default statement descriptor configured in your platform’s [Connect
settings](https://dashboard.stripe.com/settings/connect/payouts/statement-descriptor)
only applies to a connected account’s payout under certain criteria.

- The connected account belongs to a platform that pays Stripe fees (including
Custom and Express accounts), or you have [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
for it.
- The connected account doesn’t have access to the Stripe API. Connected
accounts only have access to the Stripe API if they can access the Stripe
Dashboard.
- The connected account isn’t restricted from using the `read_write` OAuth
scope. Connected accounts can use the `read_write` OAuth scope if they have
access to the Stripe Dashboard and aren’t explicitly restricted from using it
with platform controls.

Unless all of these criteria apply, the statement descriptor defaults to STRIPE.
However, this default might be subject to other external factors, such as which
bank processed the payout.

## Precedence order

The precedence order for the statement descriptor is different for manual and
automatic payouts.

### Manual payouts

- The
[statement_descriptor](https://docs.stripe.com/api/payouts/object#payout_object-statement_descriptor)
set on the Payout object.
- The
[settings.payout.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-statement_descriptor)
from the connected account, if your platform and the connected account were
created on or after October 9th, 2023.
- Your platform’s default statement descriptor, if it’s applicable to the
connected account.
- If no other conditions are met, the statement descriptor might default to
STRIPE.

### Automatic payouts

- The
[settings.payout.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-statement_descriptor)
from the connected account, if your platform and the connected account were
created on or after October 9th, 2023.
- Your platform’s default statement descriptor, if it’s applicable to the
connected account.
- If no other conditions are met, the statement descriptor might default to
STRIPE.

## Links

-
[settings.payout.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-statement_descriptor)
- [Connect
settings](https://dashboard.stripe.com/settings/connect/payouts/statement-descriptor)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
-
[statement_descriptor](https://docs.stripe.com/api/payouts/object#payout_object-statement_descriptor)