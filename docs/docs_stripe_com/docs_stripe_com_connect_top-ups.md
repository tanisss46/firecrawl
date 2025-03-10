# Add funds to your platform balance

## Platforms can add funds to their balance from a bank account.

Available in: 
Platforms can add funds to their Stripe balance to pay connected accounts for
goods or services. There are a number of different use cases for adding funds to
pay connected accounts for goods or services, including:

- Paying bonuses or other one-off [payouts](https://docs.stripe.com/payouts),
independent of specific charges.
- Providing customer discounts while still paying full price for goods or
services to sellers.
- Adding funds from non-Stripe income (for example, checks or funds from another
processor).
- Enabling faster payouts (for example, pay a vendor before incoming funds
become available).

Where permitted, platforms can also add funds to their Stripe balance to send
funds to recipients off of Stripe (for example, via [cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts)). They can also
pay out added funds to other accounts they own.

#### Note

If a transfer or payout fails due to insufficient funds in your platform
balance, adding funds doesn’t automatically retry the failed action. After
adding funds, you must repeat any failed transfers or payouts.

## Requirements

All of these requirements must be met to add funds to your Stripe balance:

- Your platform is in the US and the connected account receiving the funds
either is in the US or has a
[recipient](https://docs.stripe.com/connect/service-agreement-types#recipient)
service agreement.
- Your platform profile is approved. You can check the status in your
[settings](https://dashboard.stripe.com/connect/settings/profile) after
completing the platform profile.

When adding funds to your balance, use a manual payout schedule. If you enable
automatic payouts, you can’t control whether the system uses added funds for
payouts. You can configure your schedule in your [payout
settings](https://dashboard.stripe.com/settings/payouts).

#### Note

Only [team members](https://docs.stripe.com/get-started/account/teams) with
administrator access to the platform Stripe account and who’ve enabled [two
factor
authentication](https://support.stripe.com/questions/how-do-i-enable-two-step-verification)
can add funds.

If you’re new to [Connect](https://docs.stripe.com/connect), start with a guide
to add funds to your platform balance and [pay out
money](https://docs.stripe.com/connect/add-and-pay-out-guide).

[Confirm funding
purpose](https://docs.stripe.com/connect/top-ups#confirm-funding-purpose)
To add funds, go to the
[Balance](https://dashboard.stripe.com/test/balance/overview) section in the
Dashboard.

!

Click **Add to balance** and select why you are adding funds to your account.

!

Click **Pay out connected accounts** to add funds that are paid out to your
connected accounts. If you are adding funds to your balance to cover future
refunds and disputes, or to repay your platform’s negative balance, click
**Cover negative balances** and see [adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds).

[Verify your bank
account](https://docs.stripe.com/connect/top-ups#verify-bank-account)
You must use a verified bank account to add funds. You’ll go through the
verification process in the Dashboard when you first attempt to add funds from
an unverified bank account.

If your bank account is unverified, you’ll need to confirm two microdeposits
from Stripe. These deposits appear on your online banking statement within 1-2
business days. You’ll see `ACCTVERIFY` for the statement description.

Stripe notifies you in the Dashboard and through email when the microdeposits
should have arrived in your account. To complete the verification process, click
the Dashboard notification in the
[Balance](https://dashboard.stripe.com/balance/overview) section, enter the two
microdeposit amounts, and click **Verify account**.

[Add funds](https://docs.stripe.com/connect/top-ups#add-funds)
Once verified, you can use the
[Dashboard](https://dashboard.stripe.com/test/balance/overview) or the
[API](https://docs.stripe.com/api#topups) to add funds to your account balance.

DashboardAPI- In the Dashboard, go to the
[Balance](https://dashboard.stripe.com/test/balance/overview) section.
- In the **Add to balance** window, enter an amount in USD and click **Connect
payouts**.
- In the resulting modal window (shown below), enter an amount in USD.
- Verify the amount and click **Add funds.**
- The resulting object is called a
[top-up](https://docs.stripe.com/api/topups/object) and can be viewed in the
[Top-ups](https://dashboard.stripe.com/test/topups) section of the Dashboard.
- After the funds are available in your platform’s Stripe balance, you can
transfer funds to a connected account through the
[API](https://docs.stripe.com/api#transfers) or the
[Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#sending-funds).
In the Dashboard, transfer funds to a connected account by clicking **Add
funds** in the **Balance** section of the connected account’s detail page.

## View your funds

View your added funds in the Dashboard on
[Top-ups](https://dashboard.stripe.com/test/topups) tab under the
[Balance](https://dashboard.stripe.com/balance/overview) page. Each time you add
funds, a top-up object is made that has a unique ID with the format `tu_XXXXXX`,
which you can see on the detailed view for the top-up.

## Settlement timing

US platforms add funds via ACH debit, and can take 5-6 business days to become
available in your Stripe balance. You can request a review of your account for
faster settlement timing by contacting [Stripe
Support](https://support.stripe.com/contact).

As we learn more about your account, Stripe might be able to decrease your
settlement timing automatically.

Adding funds for future refunds and disputes or to repay a negative balance can
happen through [bank or wire
transfer](https://docs.stripe.com/get-started/account/add-funds), and be
available in 1-2 business days.

## Testing

You can use the Dashboard or the API to [test adding funds to your
balance](https://docs.stripe.com/connect/testing#testing-top-ups).

## Links

- [payouts](https://docs.stripe.com/payouts)
- [cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts)
- [recipient](https://docs.stripe.com/connect/service-agreement-types#recipient)
- [settings](https://dashboard.stripe.com/connect/settings/profile)
- [payout settings](https://dashboard.stripe.com/settings/payouts)
- [team members](https://docs.stripe.com/get-started/account/teams)
- [two factor
authentication](https://support.stripe.com/questions/how-do-i-enable-two-step-verification)
- [Connect](https://docs.stripe.com/connect)
- [pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide)
- [Balance](https://dashboard.stripe.com/test/balance/overview)
- [adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds)
- [Balance](https://dashboard.stripe.com/balance/overview)
- [API](https://docs.stripe.com/api#topups)
- [top-up](https://docs.stripe.com/api/topups/object)
- [Top-ups](https://dashboard.stripe.com/test/topups)
- [API](https://docs.stripe.com/api#transfers)
-
[Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#sending-funds)
- [Stripe Support](https://support.stripe.com/contact)
- [test adding funds to your
balance](https://docs.stripe.com/connect/testing#testing-top-ups)