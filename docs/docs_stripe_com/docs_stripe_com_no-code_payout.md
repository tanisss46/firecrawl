# Pay out to people

## Add money to your Stripe balance and pay out to sellers or service providers.

Use this guide to learn how to add funds to your account balance and transfer
the funds into your users’ bank accounts, without processing payments through
Stripe. This guide uses an example of a Q&A product that pays its writers a
portion of the advertising revenue that their answers generate. The platform and
connected accounts are both in the US.

When adding funds to your balance, best practice is to use a manual
[payout](https://docs.stripe.com/payouts) schedule. If you enable automatic
payouts, you can’t control whether the system uses added funds for payouts. You
can configure your schedule in your [payout
settings](https://dashboard.stripe.com/settings/payouts).

#### Note

Only [team members](https://docs.stripe.com/get-started/account/teams) with
administrator access to the platform Stripe account and [two-factor
authentication](https://support.stripe.com/questions/how-do-i-enable-two-step-verification)
enabled can add funds.

## Prerequisites

- [Register your platform](https://dashboard.stripe.com/connect/set-up).
- Add business details to [activate your
account](https://dashboard.stripe.com/account/onboarding).
- [Complete your platform
profile](https://dashboard.stripe.com/connect/settings/profile).
- [Customize your brand
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding).
Add a business name, icon, and brand color.
[Create a connected
account](https://docs.stripe.com/no-code/payout#create-connected-account)
When a user (seller or service provider) signs up on your platform, create a
user [Account](https://docs.stripe.com/api/accounts) (referred to as a
*connected account*) so you can accept payments and move funds to their bank
account. Connected accounts represent your users in Stripe’s API and facilitate
the collection of information requirements so Stripe can verify the user’s
identity. For a Q&A product that pays for answers, the connected account
represents the writer.

#### Note

This guide uses Express accounts which have certain
[restrictions](https://docs.stripe.com/connect/express-accounts#prerequisites-for-using-express).
You can evaluate [Custom
accounts](https://docs.stripe.com/connect/custom-accounts) as an alternative.

### Customize your signup form

In your [platform
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding),
customize your Express signup form by changing the color and logos that users
see when they click your [Connect](https://docs.stripe.com/connect) link.

Default Express signup form

Branding settings

### Create a connected account link

You can create a connected account onboarding link by clicking **+Create** on
the [accounts overview
page](https://dashboard.stripe.com/connect/accounts/overview), and selecting
**Express** for the account type, along with the **transfers** capability. Click
**Continue** to generate a link to share with the user you want to onboard.

![Create an account in the
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/create-account-unified.450b8fb21ed13bcc165baa7db225e157.png)

Create a connected account

Create an onboarding link

This link directs users to a form where they can provide information in order to
connect to your platform. For example, if you have a Q&A platform, you can
provide a link for writers to connect with the platform. The link is only for
the single connected account you created. After your user completes the
onboarding flow, you can view them in your accounts list.

!

[Add funds to your
balance](https://docs.stripe.com/no-code/payout#add-funds-to-your-balance)
To add funds, go to the
[Balance](https://dashboard.stripe.com/test/balance/overview) section in the
Dashboard. Click **Add to balance** and select why you are adding funds to your
account.

Select **Pay out connected accounts** to add funds to pay out to your connected
accounts. If you are adding funds to your balance to cover future refunds and
disputes, or to repay your platform’s negative balance, select **Cover negative
balances** and see [adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds).

### Verify your bank account

Go through the verification process in the Dashboard when you first attempt to
add funds from an unverified bank account. If your bank account is unverified,
you’ll need to confirm two microdeposits from Stripe. These deposits appear in
your online banking statement within 1-2 business days. You’ll see `ACCTVERIFY`
as the statement description.

Stripe notifies you in the Dashboard and through email when the microdeposits
have arrived in your account. To complete the verification process, click the
Dashboard notification in the
[Balance](https://dashboard.stripe.com/balance/overview) section, enter the two
microdeposit amounts, and click **Verify account**.

### Add funds

Once verified, use the
[Dashboard](https://dashboard.stripe.com/test/balance/overview) to add funds to
your account balance.

- In the Dashboard, go to the
[Balance](https://dashboard.stripe.com/test/balance/overview) section.
- In the **Add to balance** window, enter an amount in USD and select Connect
payouts.
- In the resulting modal (shown below), enter an amount in USD.
- Verify the amount and then click **Add funds.**
- The resulting object is called a
[top-up](https://docs.stripe.com/api/topups/object) and can be viewed in the
[Top-ups](https://dashboard.stripe.com/test/topups) section of the Dashboard.

### View funds

View your funds in the Dashboard on
[Top-ups](https://dashboard.stripe.com/test/topups) tab under the
[Balance](https://dashboard.stripe.com/balance/overview) page. Each time you add
funds, a top-up object is made that has a unique ID in the format **tu_XXXXXX**,
which you can see on the detailed view for the top-up.

### Settlement timing

US platforms add funds via ACH debit and can take 5-6 business days to become
available in your Stripe balance. You can request a review of your account for
faster settlement timing by contacting [Stripe
Support](https://support.stripe.com/contact).

As we learn more about your account, Stripe might be able to decrease your
settlement timing automatically.

Adding funds for future refunds and disputes or to repay a negative balance can
happen through [bank or wire
transfers](https://docs.stripe.com/get-started/account/add-funds) and are
available in 1-2 business days.

[Pay out to your user](https://docs.stripe.com/no-code/payout#pay-out-to-user)
After your user completes [the onboarding
process](https://docs.stripe.com/connect/add-and-pay-out-guide#create-connected-account)
and you’ve added funds to your balance, you can transfer some of your balance to
your connected accounts. In this example, money is transferred from the Q&A
platform’s balance to the individual writer.

To pay your user, go to the **Balance** section of an account’s detail page and
click **Add funds**. By default, any funds you transfer to a connected account
accumulate in the connected account’s Stripe balance and are paid out on a daily
rolling basis. You can change the payout frequency by clicking the right-most
button in the **Balance** section and selecting **Edit payout schedule**.

Send funds to user

Edit payout schedule

## See also

- [Managing connected accounts in the
Dashboard](https://docs.stripe.com/connect/dashboard)

## Links

- [Connect](https://docs.stripe.com/connect)
- [Connect pricing](https://stripe.com/connect/pricing)
- [payout](https://docs.stripe.com/payouts)
- [payout settings](https://dashboard.stripe.com/settings/payouts)
- [team members](https://docs.stripe.com/get-started/account/teams)
- [two-factor
authentication](https://support.stripe.com/questions/how-do-i-enable-two-step-verification)
- [Register your platform](https://dashboard.stripe.com/connect/set-up)
- [activate your account](https://dashboard.stripe.com/account/onboarding)
- [Complete your platform
profile](https://dashboard.stripe.com/connect/settings/profile)
- [Customize your brand
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding)
- [Account](https://docs.stripe.com/api/accounts)
-
[restrictions](https://docs.stripe.com/connect/express-accounts#prerequisites-for-using-express)
- [Custom accounts](https://docs.stripe.com/connect/custom-accounts)
- [accounts overview
page](https://dashboard.stripe.com/connect/accounts/overview)
- [Balance](https://dashboard.stripe.com/test/balance/overview)
- [adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds)
- [Balance](https://dashboard.stripe.com/balance/overview)
- [top-up](https://docs.stripe.com/api/topups/object)
- [Top-ups](https://dashboard.stripe.com/test/topups)
- [Stripe Support](https://support.stripe.com/contact)
- [the onboarding
process](https://docs.stripe.com/connect/add-and-pay-out-guide#create-connected-account)
- [Managing connected accounts in the
Dashboard](https://docs.stripe.com/connect/dashboard)