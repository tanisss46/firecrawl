# Minimum balances for automatic payouts

## Set a minimum balance in your Stripe account to manage cash flow and cover potential refunds, disputes, and fees.

Automatic payouts default to paying out your entire available balance according
to your set schedule. This can result in insufficient funds to manage your
payments business on Stripe, preventing you from processing refunds or disputes.

Minimum balances for automatic payouts let you keep a specified amount in your
Stripe account after an automatic payout. Automatic payouts only pay out funds
exceeding this minimum balance to your bank account. This helps minimize the
risk of a negative balance due to refunds, disputes, or fees after automatic
payouts. You can use **Minimum Balances** to help:

- Improve your cash flow management by keeping a balance to cover refunds,
disputes, and fees.
- Receive comprehensive reconciliation reports with automatic payouts, including
the minimum balance you’ve set.

#### Caution

Only use minimum balances to cover anticipated refunds, disputes, and fees. Not
supported in Brazil, India, and Thailand.

[Express](https://docs.stripe.com/connect/express-accounts) and
[Custom](https://docs.stripe.com/connect/custom-accounts) connected accounts
can’t set a minimum balance.

## Set up minimum balances

Minimum balances work with all automatic payout schedules. If you dip below the
set minimum balance, Stripe attempts to renew first by using your available
balance. If you have no available balance, we use your incoming funds instead.

To set up a minimum balance:

- Log in to the Dashboard. **Minimum Balances** are only available when you have
access to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payouts).
- Navigate to [Payout Settings](https://dashboard.stripe.com/settings/payouts).
Under the **Minimum Balance** section, toggle the option on, and set a fixed
amount.
- Specify the amount you want to keep as a minimum balance. This amount remains
in your account to cover potential refunds, disputes, and fees.
- Save your settings. Your automatic payouts will now retain the specified
minimum balance.

![Minimum balance settings in the
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/minimum-balances.ca159ff2ac6b90b6fe4371eaadceba50.png)

## Manage minimum balances

You can update the minimum balance as needed:

- Navigate to [Payout Settings](https://dashboard.stripe.com/settings/payouts).
- Under the **Minimum Balance** section, change the amount. If you choose a
lower amount to keep as a minimum balance, we include the released funds on your
next scheduled payout. If you choose a higher minimum balance, we accumulate
from new incoming payments. Regularly check your balance to verify it aligns
with your business needs.

You can also disable your **Minimum Balance** in the Dashboard:

- Navigate to [Payout Settings](https://dashboard.stripe.com/settings/payouts).
- Under the **Minimum Balance** section, set the amount to 0 or toggle the
option off. When you turn off minimum balances, Stripe no longer retains the
specified minimum balance during automatic payouts. Your entire available
balance will be disbursed according to your payout schedule.

#### Note

Consider setting a minimum balance that covers your typical refund, dispute, and
fee amounts. We generally recommend four to five times your average daily
processing volumes, as this has proven effective in maintaining healthy cash
flow.

## Negative balances

With a **Minimum Balance** in place, the likelihood of a negative balance is
significantly reduced. However, if you process refund amounts greater than your
minimum balance amount at any given time, your balance becomes negative. To
learn more about handling [negative
balances](https://support.stripe.com/embedded-connect/questions/handling-negative-balances),
see [Fix a negative
balance](https://support.stripe.com/questions/fix-the-negative-balance-on-your-account).

## Reconciliation reports

When you enable **Minimum Balance**, your [Payout Reconciliation
Report](https://docs.stripe.com/reports/payout-reconciliation) displays the
amount retained due to the minimum balance. This helps you see how the minimum
balance affects your payouts and transactions. The timing of your reconciliation
reports remains unchanged. The reports shows the total payout and the amount
retained based on the minimum balance.

The following sections illustrate how Stripe pays out and reconciles an account
with a set minimum balance using USD as example currency, workings for other
currencies will be the same:

- Total Balance: 30,000 USD
- Minimum Balance: 10,000 USD
- Payout Amount: 20,000 USD (30,000 USD Total Balance - 10,000 USD Minimum
Balance)

Stripe initiates an automatic payout of 20,000 USD to your linked bank account.
The minimum balance of 10,000 USD remains in your Stripe account. You can see
the [Balance Transaction API](https://docs.stripe.com/api/balance_transactions)
for more details on the hold made for the minimum balance.

Your reconciliation report shows the following details:

- All transactions leading up to the total balance of 30,000 USD
- A transaction for the retained amount of -10,000 USD (your selected Minimum
Balance)
- Results in a total payout amount of 20,000 USD

## Minimum balances for Platforms

You can follow the above steps to set your own **Minimum Balance**. In most
cases a minimum balance at your Platform should suffice to cover negative
balances and refunds for your connected accounts.

#### Caution

We don’t support setting a minimum balance per connected account.

## Interested in setting minimum balances for connected accounts?

We are working to support setting a minimum balance per connected account.
Please provide your email address below and our team will contact you soon.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## See also

- [Receiving payouts](https://docs.stripe.com/payouts)

## Links

- [Express](https://docs.stripe.com/connect/express-accounts)
- [Custom](https://docs.stripe.com/connect/custom-accounts)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payouts)
- [negative
balances](https://support.stripe.com/embedded-connect/questions/handling-negative-balances)
- [Fix a negative
balance](https://support.stripe.com/questions/fix-the-negative-balance-on-your-account)
- [Payout Reconciliation
Report](https://docs.stripe.com/reports/payout-reconciliation)
- [Balance Transaction API](https://docs.stripe.com/api/balance_transactions)
- [privacy policy](https://stripe.com/privacy)
- [Receiving payouts](https://docs.stripe.com/payouts)