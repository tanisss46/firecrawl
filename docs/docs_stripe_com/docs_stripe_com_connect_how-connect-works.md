# How Connect works

## Learn how Connect's features support multiparty integrations.

Businesses such as marketplaces and software platforms use Connect to manage and
route payments and payouts between sellers, customers, service providers, and
other entities.

- **Onboarding**: Onboard and verify sellers using connected accounts with
Stripe-hosted flows, or build your own with our APIs.
- **Account management**: Enable sellers to manage their account with
Stripe-hosted Dashboards, embedded components, or custom interfaces you can
build with our APIs.
- **Payments**: Integrate payments and route funds to sellers on your platform.
- **Payouts**: Pay out sellers with a variety of payout options. Enable
cross-border payouts for global sellers.
- **Platform tools**: Manage your platform or marketplace with a sophisticated
suite of platform tooling for monetization, seller support, risk management, and
tax reporting.

## Elements of a Connect integration

A Connect integration consists of five main components:

- Your platform’s web or mobile application
- Your platform’s Stripe account
- Connected accounts
- Stripe payments
- Stripe payouts

When onboarding to Connect, you create a Connect application on your platform’s
Stripe account. The Connect application allows you to create and access data on
your connected accounts. You use your Stripe API keys to make [API requests on
behalf of your connected
accounts](https://docs.stripe.com/connect/authentication).

![An overview of interactions between a Connect platform, customers, and
connected
accounts](https://b.stripecdn.com/docs-statics-srv/assets/connect-overview.c6c7d0fac01a655bc51523add1eecd21.png)

Connect offers a number of different options for onboarding connected accounts
and creating payments and payouts on them. Giving connected accounts access to
Stripe-hosted Dashboards and embedded components lets you customize their
financial workflows while minimizing your development effort and time to launch.

Connect charge types offer different ways to orchestrate payments to your
connected accounts, whether enabling them to accept payments directly or
facilitating payments between multiple sellers. Connect payouts enable you to
manage payout timing, destination payout accounts, and payout monetization on
your connected accounts.

## Availability

The countries where you can have connected accounts depends on the business
location of your platform’s country:

- [Cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts):
If your platform qualifies, you can pay out connected accounts in their local
currencies. Stripe determines if your platform meets the criteria to support
cross-border payouts.
- Extra features: If using Connect with additional payment methods or with
[Stripe Terminal](https://docs.stripe.com/terminal), country availability is
also dependent on those features.

### Country availability

## Use cases

Connect is highly flexible and designed to support many multiparty use cases:

- **SaaS platforms**: Enable connected accounts to accept payments directly.
Platforms such as Squarespace enable businesses to build their own online stores
to sell directly to customers.
- **Marketplaces**: Collect payments and pay out to multiple sellers. Platforms
such as Airbnb connect homeowners to potential guests.
- **Top-up and pay out**: Pay out to accounts without accepting payments. Add
funds to your platform account and then transfer funds to your connected
accounts without processing payments on Stripe.
- **In-person payments**: Add Stripe Terminal to your multiparty integration.
Enable your connected accounts to accept in-person payments alongside online
payments with a single integration.

## Design an integration

To determine how to build a Connect integration for your use case:

- Complete the [Connect platform
onboarding](https://dashboard.stripe.com/connect/set-up/welcome) process or view
[example integrations](https://docs.stripe.com/connect#example-integrations).
- After onboarding, review your [integration
guide](https://docs.stripe.com/connect/design-an-integration). The guide is
customized with selections you’ve made in platform onboarding.
- Follow the [onboarding
quickstart](https://docs.stripe.com/connect/onboarding/quickstart) to set up and
start using your integration.

## Links

- [API requests on behalf of your connected
accounts](https://docs.stripe.com/connect/authentication)
- [Cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts)
- [Stripe Terminal](https://docs.stripe.com/terminal)
- [Connect platform
onboarding](https://dashboard.stripe.com/connect/set-up/welcome)
- [example integrations](https://docs.stripe.com/connect#example-integrations)
- [integration guide](https://docs.stripe.com/connect/design-an-integration)
- [onboarding quickstart](https://docs.stripe.com/connect/onboarding/quickstart)