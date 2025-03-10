# Connect integration guide

## Learn about configuration options for Connect integrations.

Use this guide to explore different Connect integrations, make choices, and
access a personalized integration guide. Before starting your integration in
test mode, you must:

- Create a Stripe Account
- Begin filling out your platform profile

## Select properties

### Create and onboard accounts

Stripe enables you to create accounts on behalf of users, called connected
accounts. When using Connect, you create connected accounts for each user that
receives money on your platform.

Onboarding:Onboarding:HostedEmbeddedAPI
Send connected accounts to a Stripe-hosted onboarding flow. Stripe-hosted
onboarding allows you to redirect your user to Stripe to complete the onboarding
process in a co-branded interface.

![Screenshot of Connect Onboarding
form](https://b.stripecdn.com/docs-statics-srv/assets/Kavholm-Seamless-Standard.78b64d90c0bf87130c8b6ba1ef53df7f.png)

Best for when you want to launch quickly with the lowest integration effort:

- Connected accounts leave your site and are redirected to Stripe to complete
the flow.
- Co-branding with Stripe and limited options to customize.
- Stripe handles all of the onboarding flow logic.
- Automatically supports 46+ countries and 14 languages.

### Set up dashboard flows

Connected accounts need access to a dashboard to manage their account. Provide
connected accounts with access to the Stripe Dashboard, the Express Dashboard,
or a dashboard built using the Stripe API and embedded components.

Dashboard access:Dashboard access:StripeExpressNone
Provide access to the Stripe Dashboard to connected accounts.

The Stripe Dashboard provides connected accounts with a full suite of
functionality, including viewing payouts, managing refunds, handling disputes,
accessing reporting, and processing charges on their own. Users can sign into
their Stripe Dashboard at any time and can access the Dashboard by visiting
Stripe directly. Users have access to Stripe support and Stripe can reach out
and communicate with users about their account.

Use the Stripe Dashboard when:

- Your users need access to powerful payments workflows and advanced user
management features.
- You prefer Stripe to manage risk of loss and take responsibility for negative
balance liability on connected accounts.
- You are comfortable with Stripe branding and limited platform co-branding.

You can always add [embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
to your own website in tandem with providing access to the Stripe Dashboard.

### Accept a payment

You create a charge to accept a payment from a customer on behalf of your
connected account. The type of charge you create:

- Determines how payment funds are split among all parties involved
- Impacts how the charge appears on the customer’s bank or billing statement
(with your platform’s information or your user’s)
- Determines which account Stripe debits for refunds and chargebacks

Charge type:Charge type:DirectDestinationSeparate charges and transfers
A direct charge is a customer payment made directly to a connected account.
Customers directly transact with your connected account, often unaware of your
platform’s existence.

This charge type is best suited for platforms providing software as a service.
For example, Shopify provides tools for building online storefronts, and
Thinkific enables educators to sell online courses.

### Stripe fees

Who pays fees:Who pays fees:Your connected accountsYour platform
Stripe collects Stripe fees directly from your connected accounts. You can
collect an optional application fee when you create the direct charge.

CustomerConnected account
$10 Charge

($1.23) Application fee

$1.23 Application fee

Platform
($0.59) Stripe fees

$8.18 net

StripeDirect charge
### Pay out users

When the funds from the payment settle and your user’s connected account has a
positive Stripe balance, you can pay out those funds to their external account.

By default, Stripe pays out funds that have settled in your connected accounts’
balances on a daily rolling basis. If you prefer, you can configure different
automatic payout schedules, trigger payouts manually instead of automatically,
or pay out instantly.

### Responsibility for negative balances

Negative balance liability:Negative balance liability:StripePlatform
Stripe monitors risk signals on connected accounts, implements risk
interventions on connected accounts in response to observed signals, and seeks
to recover negative balances from your connected accounts.

For most software as a service platforms, this is the best default choice,
especially for those that are new to embedding payments:

- Stripe monitors your connected accounts for credit and fraud risk, as well as
protection against risk of loss in the event of negative balances attributed to
business risk.
- Stripe handles all the end to end communications and remediations directly
with your connected accounts through hosted flows or embedded components.

## Your personalized guide

This list of steps is customized based on your choices above. Use it to get
started building your integration.

- [Use the onboarding
quickstart](https://docs.stripe.com/connect/onboarding/quickstart#init-stripe)
Create connected accounts and collect requirements using Stripe-hosted
onboarding. [Learn more](https://docs.stripe.com/connect/hosted-onboarding)
- [Accept a payment](https://docs.stripe.com/connect/direct-charges)
Create direct charges. Your connected accounts will pay Stripe fees. [Learn
more](https://docs.stripe.com/connect/charges)
- [Set up the Stripe
Dashboard](https://docs.stripe.com/connect/stripe-dashboard)
Understand the Stripe Dashboard and control what your connected accounts can do
with it.
- [Understand Stripe’s merchant risk
responsibilities](https://docs.stripe.com/connect/risk-management/managed-risk)
Understand how Stripe handles negative balance liabilities on your connected
accounts. [Learn more](https://docs.stripe.com/connect/risk-management)
- [Pay out users](https://docs.stripe.com/connect/payouts-connected-accounts)
Understand how to control bank account and debit card payouts.
PropertiesResetOnboardingOnboarding:HostedEmbeddedAPIDashboard accessDashboard
access:StripeExpressNoneCharge typeCharge type:DirectDestinationSeparate charges
and transfersWho pays Stripe feesWho pays fees:Your connected accountsYour
platformNegative balance liabilityNegative balance liability:StripePlatform

## Links

- [embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Use the onboarding
quickstart](https://docs.stripe.com/connect/onboarding/quickstart#init-stripe)
- [Learn more](https://docs.stripe.com/connect/hosted-onboarding)
- [Accept a payment](https://docs.stripe.com/connect/direct-charges)
- [Learn more](https://docs.stripe.com/connect/charges)
- [Set up the Stripe
Dashboard](https://docs.stripe.com/connect/stripe-dashboard)
- [Understand Stripe’s merchant risk
responsibilities](https://docs.stripe.com/connect/risk-management/managed-risk)
- [Learn more](https://docs.stripe.com/connect/risk-management)
- [Pay out users](https://docs.stripe.com/connect/payouts-connected-accounts)