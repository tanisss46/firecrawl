# Platform pricing tools

## Use your Dashboard editor to manage your application fee pricing logic.

If your platform is [responsible for paying Stripe
fees](https://docs.stripe.com/connect/platform-pricing-tools#fee-payer-reference),
[platform pricing
tools](https://dashboard.stripe.com/settings/connect/platform_pricing) allow you
to define how you recoup your payment processing costs from your connected
accounts through application fees.

- Create pricing schemes that apply different application fees based on the
properties of a transaction.
- Define pricing groups to use different pricing schemes for different connected
accounts.

![Shows the Add pricing rule dialog in the
Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/customize-pricing-dialog.a5c604b458b41a572834087aa0d7118a.png)

## Eligibility for payments

The values available for defining your pricing scheme depend on which Stripe
products you use and how you’ve integrated them. The following sections describe
the which platform configurations can use and access the platform pricing tools.

### Requirements

Stripe applies pricing schemes to a payment when the payment meets all of the
following requirements:

- The pricing scheme is enabled.
- Stripe charges fees on the payment to your platform rather than the connected
account.
- Your platform is permitted to charge app fees in the connected account’s
country.
- The payment doesn’t explicitly apply `application_fee or
transfer_data[amount]` parameters that override managed application fees.
- The payment doesn’t use multi-capture.

In addition to the requirements, pricing schemes observe the following
limitations:

- If you use Standard Connect with destination charges, you can’t override
pricing or implement different pricing schemes for individual connected
accounts.
- If a payment’s captured amount is less than the charge, the calculated fee is
against the captured amount of the payment. For example, if only 5 USD is
captured on a 10 USD charge, the fee is based on 5 USD.

### Fee payer reference

Support for platform pricing tools also depends on your [funds
flow](https://docs.stripe.com/connect/charges#types) configuration for your
connected accounts.

- [Controller property
configuration](https://docs.stripe.com/connect/migrate-to-controller-properties):-
You can use platform pricing tools to calculate application fees for all charges
where the `controller.fees.payer` on the account is the Connect platform
(`application`).
- If a connected account uses destination charges, the platform is the fee payer
even if you set `controller.fees.payer=account`.
- Standard, Custom, or Express type configuration:- Configured pricing applies
to destination charges.
- Configured pricing doesn’t apply to direct charges unless the platform is on
[IC+
pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing).

## Eligibility for Instant Payouts

Stripe applies pricing schemes to an Instant Payout when:

- Your platform controls pricing.
- Your pricing scheme is enabled.
- Your connected accounts are eligible for Instant Payouts.- When Stripe is
liable for connected account losses, [Stripe determines connected account
eligibility](https://docs.stripe.com/payouts/instant-payouts#eligibility-and-daily-volume-limits)
and volume limits. You must set up separate pricing rules for each Instant
Payout currency for these connected accounts.
- When your platform is liable for connected account losses, [your platform
manages
eligibility](https://docs.stripe.com/connect/instant-payouts#manage-risk-and-eligibility)
for connected accounts. These connected accounts must be in the same country as
the platform, so different currencies don’t apply.
- A connected account must have an external account that [supports Instant
Payouts](https://docs.stripe.com/payouts/instant-payouts-banks).

Connected accounts can’t pay out more than their available balance. Instant
Payout fees reflect in the
[Payout](https://docs.stripe.com/api/payouts/object#payout_object-application_fee)
object to help with reporting and reconciliation. See
[Transactions](https://dashboard.stripe.com/connect/application_fees) in the
Dashboard to view your collected fees. If an Instant Payout fails, we
automatically refund the application fee.

#### Instant payout application fees API integration impact

Enabling pricing tools for Instant Payouts without using the [Balance API
net-of-fees](https://docs.stripe.com/api/balance/balance_object#balance_object-instant_available-net_available)
attribute can break your API integration.

## Subscriptions and invoices

Stripe also applies your pricing scheme-defined application fees to invoice and
subscription payments. As with standard purchase payments, when you apply an
explicit application fee to an invoice or subscription, that fee overrides any
matching scheme-defined fee.

## Access platform pricing tools

Different roles have different levels of access to pricing schemes.

Roles that don’t have access to the platform’s default pricing can review the
version copied to the connected accounts. Connected accounts can’t view or edit
any pricing schemes.

Platform accountConnected accounts
The following roles can access pricing schemes that apply to all connected
accounts.

RolePermissionsAdministratorRead and writeDeveloperNoneIAM AdminNoneConnect
Onboarding AnalystNoneTransfer AnalystNoneAnalystNoneDispute AnalystNoneRefund
AnalystNoneSupport SpecialistNoneSupport CommunicationsNoneTax AnalystNoneView
OnlyNoneTop-ups SpecialistNone

## Links

- [platform pricing
tools](https://dashboard.stripe.com/settings/connect/platform_pricing)
- [funds flow](https://docs.stripe.com/connect/charges#types)
- [Controller property
configuration](https://docs.stripe.com/connect/migrate-to-controller-properties)
- [IC+
pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [Stripe determines connected account
eligibility](https://docs.stripe.com/payouts/instant-payouts#eligibility-and-daily-volume-limits)
- [your platform manages
eligibility](https://docs.stripe.com/connect/instant-payouts#manage-risk-and-eligibility)
- [supports Instant
Payouts](https://docs.stripe.com/payouts/instant-payouts-banks)
-
[Payout](https://docs.stripe.com/api/payouts/object#payout_object-application_fee)
- [Transactions](https://dashboard.stripe.com/connect/application_fees)
- [Balance API
net-of-fees](https://docs.stripe.com/api/balance/balance_object#balance_object-instant_available-net_available)