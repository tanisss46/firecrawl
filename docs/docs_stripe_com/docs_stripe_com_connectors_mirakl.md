# Stripe Connector for Mirakl

## Leverage the power of Stripe on Mirakl-built marketplaces.

[Connect](https://docs.stripe.com/connect) is the perfect fit for
[Mirakl](https://www.mirakl.com/) marketplaces:

- Compatible with all the [payment
methods](https://stripe.com/payments/features#payment-options) offered by
Stripe.
- Works for B2C and B2B marketplaces.
- Supports multi-seller and hybrid orders.
- Automated [payouts](https://docs.stripe.com/payouts) based on your
configuration.

## Integration steps

The main tasks to set up payments for your marketplace using Mirakl are:

- First, you need a Stripe account.
[Register](https://dashboard.stripe.com/register).
- Implement the relevant payment methods. Use one of our [existing
plugins](https://docs.stripe.com/connectors) or [build your own
integration](https://docs.stripe.com/payments).
- [Activate Connect](https://dashboard.stripe.com/connect/accounts/overview) in
your Dashboard. Choose **Platform or marketplace** as your integration type.
- Configure your [Connect branding
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding).
- [Configure](https://docs.stripe.com/connectors/mirakl/configuration) and
[install](https://docs.stripe.com/connectors/mirakl/install) the connector on
your test environment.
- Adapt your communication to sellers as described in the [onboarding
workflow](https://docs.stripe.com/connectors/mirakl/onboarding-sellers#communication).
- Adapt your payments requests as described in the [payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-validation)
- Test the different workflows: onboarding, payments, refunds, and payouts.
- [Activate](https://dashboard.stripe.com/account/onboarding) your Stripe
account.
- Complete your [Platform
profile](https://dashboard.stripe.com/connect/profile).
- [Configure](https://docs.stripe.com/connectors/mirakl/configuration) and
[install](https://docs.stripe.com/connectors/mirakl/install) the connector on
your live environment.
- Go live.

Optionally, you can use [Radar](https://docs.stripe.com/radar) for fraud
protection or [Stripe Billing](https://docs.stripe.com/billing) to create and
manage [invoices](https://docs.stripe.com/api/invoices) and recurring payments.

## Workflows

Learn more about each workflow:

- [Onboarding
sellers](https://docs.stripe.com/connectors/mirakl/onboarding-sellers)
- [Payments](https://docs.stripe.com/connectors/mirakl/payments)
- [Payouts](https://docs.stripe.com/connectors/mirakl/payouts)

## Alerting

The workflows supported by the connector don’t require any manual intervention
or operational supervision. In case an operation fails, the [alerting
job](https://docs.stripe.com/connectors/mirakl/reference#alerting) sends you an
email.

## Links

- [Connect](https://docs.stripe.com/connect)
- [Mirakl](https://www.mirakl.com/)
- [payment methods](https://stripe.com/payments/features#payment-options)
- [payouts](https://docs.stripe.com/payouts)
- [Register](https://dashboard.stripe.com/register)
- [existing plugins](https://docs.stripe.com/connectors)
- [build your own integration](https://docs.stripe.com/payments)
- [Activate Connect](https://dashboard.stripe.com/connect/accounts/overview)
- [Connect branding
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding)
- [Configure](https://docs.stripe.com/connectors/mirakl/configuration)
- [install](https://docs.stripe.com/connectors/mirakl/install)
- [onboarding
workflow](https://docs.stripe.com/connectors/mirakl/onboarding-sellers#communication)
- [payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-validation)
- [Activate](https://dashboard.stripe.com/account/onboarding)
- [Platform profile](https://dashboard.stripe.com/connect/profile)
- [Radar](https://docs.stripe.com/radar)
- [Stripe Billing](https://docs.stripe.com/billing)
- [invoices](https://docs.stripe.com/api/invoices)
- [Onboarding
sellers](https://docs.stripe.com/connectors/mirakl/onboarding-sellers)
- [Payments](https://docs.stripe.com/connectors/mirakl/payments)
- [Payouts](https://docs.stripe.com/connectors/mirakl/payouts)
- [alerting job](https://docs.stripe.com/connectors/mirakl/reference#alerting)