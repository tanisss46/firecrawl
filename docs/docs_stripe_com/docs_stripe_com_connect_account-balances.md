# Understanding Connect account balances

## Learn how Stripe account balances work when using Connect.

Both your platform account and a connected account are still just Stripe
accounts, each with their own, separate account balance.

All Stripe accounts can have balances in two states:

- `pending`, meaning the funds are not yet available to pay out
- `available`, meaning the funds are available to pay out now

With non-Connect accounts, processing charges increases the Stripe account
balance. The charged amount, less any Stripe fees, is initially reflected on the
pending balance, and becomes available on a 2-day rolling basis. (This timing
can vary by country and account.) Available funds can be paid out to a bank
account or debit card. [Payouts](https://docs.stripe.com/payouts) reduce the
Stripe account balance accordingly.

With [Connect](https://docs.stripe.com/connect), your platform account and each
connected account has its own `pending` and `available` balances. The allocation
of funds between them depends on [the type of
charges](https://docs.stripe.com/connect/charges) that you use.

Further, a platform account can also have a `connect_reserved` balance, used to
offset negative balances on connected accounts.

#### Note

When you transfer funds between your platform’s balance and a connected
account’s balance, Stripe doesn’t automatically retry failures. For example, if
you attempt to transfer funds from your platform’s balance to a connected
account’s balance, but your platform has insufficient available funds, that
transfer attempt fails. If you then add funds to your available balance, they
don’t automatically transfer to the connected account’s balance. You must
explicitly attempt the transfer again.

## Check a connected account’s balance

To check the balance of a connected account, perform a [retrieve
balance](https://docs.stripe.com/api/balance/balance_retrieve) call
authenticated as the connected account. The returned [Balance
object](https://docs.stripe.com/api#balance_object) reflects the `pending` and
`available` balances.

```
curl https://api.stripe.com/v1/balance \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

## Accounting for negative balances

Some actions, such as refunds and chargebacks, create negative transactions in a
Stripe account. Stripe handles negative transactions to help maintain a positive
Stripe balance for related accounts:

- If at all possible, Stripe automatically offsets negative transactions against
future payments
- Stripe first assigns negative transactions to the account on which the
associated charge was made. For example, when charging on a connected account, a
refund or chargeback comes from the connected account. When charging on your
platform, a refund or chargeback comes from your platform account.

Despite these measures, if a connected account balance becomes negative,
ultimate responsibility depends on the account’s
[controller.losses.payments](https://docs.stripe.com/api/accounts/create#create_account-controller-losses-payments)
property:

- `stripe` (Including Standard accounts): The connected account is responsible
for covering its own negative Stripe balances.
- `application` (Including Express and Custom accounts): The platform is
responsible for covering the connected account’s negative Stripe balances.

If a connected account balance is negative, Stripe debits their external account
on file up to the maximum number of attempts allowed. If all attempts fail,
Stripe pauses payouts to and debits from the external account until the external
account on file is updated.

While an account’s balance is negative, you can’t send payouts to the account’s
bank or debit card on their behalf. Stripe will resume sending payouts to the
connected account when the account’s Stripe balance becomes positive.

### Automatically debit connected accounts

If Stripe hasn’t already attempted to debit a connected account’s external
account for a negative balance, you can allow Stripe to do so by setting
[debit_negative_balances](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-debit_negative_balances)
to true.

#### Caution

Stripe can’t correct a negative Stripe account balance using a debit card.

Auto debit for negative balances is supported for banks in the following
countries:

- Australia
- Canada
- Europe (SEPA countries, which includes the UK)
- New Zealand
- United States

See the [Auto Debit FAQ](https://support.stripe.com/questions/auto-debit-faq)
for a detailed breakdown of which countries and account types are supported.

Enabling `debit_negative_balances` triggers debits as needed, even when the
connected account is on manual payouts. For more details, see [Impact from
chargebacks and negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#impact-from-chargebacks-and-negative-balances).

## Understanding connected reserve balances

To protect against negative connected account `available` balances that your
platform is responsible for, Stripe holds a reserve on your platform account’s
`available` balance. Depending on the connected account’s country, Stripe
initiates a bank withdrawal on the account’s bank account to cover the [negative
balance](https://support.stripe.com/questions/negative-balances-in-stripe-handling-by-country).
Although the `available` balance for the account zeroes out as soon as the
withdrawal is posted, the platform reserve for that account is held for an
additional 3 business days. You’ll see this reserve reflected in the
[Dashboard](https://dashboard.stripe.com/test/balance/overview) and exported
reports (as a **reserve transaction**).

There are three kinds of balance activities related to reserves:

- Funds reserved to cover a negative balance on a connected account. When a
connected account’s balance becomes negative, Stripe temporarily reserves a
portion of your balance to ensure that funds can be covered by creating a
balance transaction with the type `reserve_transaction`.
- Funds released after a positive balance change on a connected account. When a
connected account’s previously negative balance becomes less negative due to
activity on that account (for example, through new charges), a corresponding
portion of your platform’s reserve balance is released through a balance
transaction with the type `reserve_transaction`.
- Funds collected due to a long-standing negative balance on a connected
account. When a connected account holds a negative balance amount for 180 days,
Stripe transfers a portion of your balance to zero out that account’s balance by
creating a balance transaction with the type `connect_collection_transfer`.

To see the current reserves held on your account, perform a retrieve balance API
call but for your own account (that is, not authorized as another user as in the
above).

To clear a connected account’s negative balance, and thereby remove the reserve
on your account, send a
[transfer](https://docs.stripe.com/connect/separate-charges-and-transfers) to
the applicable account. If a connected account has a negative balance for more
than 180 days, Stripe will automatically transfer your reserves to the connected
account to zero out the balance. Dashboard pages and reports show these
transfers as Connect collection transfers.

#### Caution

After a connected account’s balance is cleared through a collection transfer, we
recommend that you [reject](https://docs.stripe.com/api#reject_account) the
account to prevent future losses.

## Holding funds

If you need more granular control over scheduling payouts to connected accounts
where your platform is responsible for negative balances, you can take one of
the following approaches:

- Hold funds in the platform balance before [transferring them to a connected
account balance](https://docs.stripe.com/connect/separate-charges-and-transfers)
- Hold funds in a connected account’s balance before [paying them
out](https://docs.stripe.com/connect/manual-payouts) to an external account

We recommend that platforms hold funds only when there’s a clear purpose and a
commitment to transfer them or pay them out when an event occurs or a
precondition is satisfied. The typical use case for holding funds is on-demand
services platforms, where the marketplace usually waits for the service to be
completed and confirmed before paying out to the service provider (for example,
rentals, delivery services, and ride-sharing).

Platforms should refrain from holding funds arbitrarily, and instead pay out to
their connected accounts as soon as they’re identified. This is usually when the
charge is made. If you aren’t sure about holding funds, speak with your legal
advisor.

For compliance reasons, we can hold funds in reserve for a period of time that’s
based on the merchant’s country, as shown below:

CountryHolding PeriodThailand10 daysUnited States2 yearsAll other countries90
days
## See also

- [Creating Direct Charges](https://docs.stripe.com/connect/direct-charges)
- [Creating Destination Charges on Your
Platform](https://docs.stripe.com/connect/destination-charges)
- [Creating Separate Charges and
Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

## Links

- [payment
source](https://docs.stripe.com/connect/manual-payouts#regular-payouts)
- [Payouts](https://docs.stripe.com/payouts)
- [Connect](https://docs.stripe.com/connect)
- [the type of charges](https://docs.stripe.com/connect/charges)
- [retrieve balance](https://docs.stripe.com/api/balance/balance_retrieve)
- [Balance object](https://docs.stripe.com/api#balance_object)
- [bank account](https://docs.stripe.com/connect/payouts-connected-accounts)
-
[controller.losses.payments](https://docs.stripe.com/api/accounts/create#create_account-controller-losses-payments)
-
[debit_negative_balances](https://docs.stripe.com/api/accounts/object#account_object-settings-payouts-debit_negative_balances)
- [Auto Debit FAQ](https://support.stripe.com/questions/auto-debit-faq)
- [Impact from chargebacks and negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#impact-from-chargebacks-and-negative-balances)
- [negative
balance](https://support.stripe.com/questions/negative-balances-in-stripe-handling-by-country)
- [Dashboard](https://dashboard.stripe.com/test/balance/overview)
- [transfer](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [reject](https://docs.stripe.com/api#reject_account)
- [paying them out](https://docs.stripe.com/connect/manual-payouts)
- [Creating Direct Charges](https://docs.stripe.com/connect/direct-charges)
- [Creating Destination Charges on Your
Platform](https://docs.stripe.com/connect/destination-charges)