# Migrate subscriptions to Stripe Billing

## Learn about migrating subscriptions from other sources to Stripe.

You can import existing
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) from
third-party billing systems (such as Zuora, Recurly, Chargify, or Chargebee)
into Stripe Billing. You can also migrate subscriptions from an in-house billing
system or from a different Stripe account.

Use the [Billing migration
toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
to migrate your subscriptions without writing code. Alternatively, you can use
the [Stripe
APIs](https://docs.stripe.com/billing/subscriptions/import-subscriptions) to
import subscriptions with manual scripts.

## Before you begin

You must know:

- Your current payment processor.
- Your current subscription provider.
- Your [pricing model](https://docs.stripe.com/products-prices/pricing-models).

## Getting started

[Migrate subscriptions using toolkitUse the Billing migration toolkit to migrate
your subscriptions to
Stripe.](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)[Migrate
subscriptions with APIsLearn how to migrate your subscriptions to Stripe using
Stripe
APIs.](https://docs.stripe.com/billing/subscriptions/import-subscriptions)[Toolkit
CSV referenceFollow best practices to migrate your subscriptions using the
Billing migration
toolkit.](https://docs.stripe.com/billing/subscriptions/toolkit-reference)
## Migration stages

A typical migration process consists of the following stages:

- [Set up your billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).
- [Migrate your customer and payment processor
information](https://docs.stripe.com/get-started/data-migrations/pan-import).
- [Import your subscriptions to Stripe
Billing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit).

![example
image](https://b.stripecdn.com/docs-statics-srv/assets/billing-migration.f3bae77ee00a04b8d0baf90518a1db2c.png)

### Migration decision matrix

The migration process varies slightly depending on a few factors. Use the
following decision matrix to understand the required steps for your situation.

My customer and payment data is in an external systemMy customer and payment
data is already in StripeMigrate subscription data from a third party- [Set up a
Stripe Billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Request a PAN data import from your current
processor](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [Use the Billing toolkit to migrate subscriptions data to Stripe
Billing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
- [Set up a Stripe Billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Use the Billing toolkit to migrate subscriptions data to Stripe
Billing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
Migrate subscription data between Stripe accounts- [Set up a Stripe Billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [ PAN data across Stripe
accounts](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
- [Billing migration within Stripe
accounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)
- [Set up a Stripe Billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [ PAN data across Stripe
accounts](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
- [Billing migration within Stripe
accounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Billing migration
toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
- [Stripe
APIs](https://docs.stripe.com/billing/subscriptions/import-subscriptions)
- [pricing model](https://docs.stripe.com/products-prices/pricing-models)
- [Toolkit CSV referenceFollow best practices to migrate your subscriptions
using the Billing migration
toolkit.](https://docs.stripe.com/billing/subscriptions/toolkit-reference)
- [Set up your billing
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Migrate your customer and payment processor
information](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [ PAN data across Stripe
accounts](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
- [Billing migration within Stripe
accounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)