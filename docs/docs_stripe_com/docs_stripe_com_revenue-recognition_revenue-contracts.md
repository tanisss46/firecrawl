# Revenue Recognition contracts

## Learn how to configure revenue contracts and model enterprise B2B sales contracts in Stripe Revenue Recognition.

## Interested in using revenue contracts?

Please provide your email address below and our team will be in touch.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
The revenue contracts feature facilitates the representation of enterprise
sales-led contracts in [Revenue
Recognition](https://dashboard.stripe.com/revenue-recognition). It allows you to
customize revenue schedules using custom performance obligations that are
decoupled from billing periods. Additionally, you can track key metrics at a
contract level and improve your financial insights.

## Customize revenue schedules

Revenue contracts enables the creation of custom contract items that dictate how
revenue is recognized instead of invoice line items. It allows you to attach
billing models (for example, invoices, subscriptions, payments) to the contract
used as payment collection containers.

### Example

Given a 2-year B2B contract with monthly billing, you can create a contract item
for the 2-year period:

Contract
ItemAmount10000[Price](https://docs.stripe.com/api/prices)price_1PeriodJan 1,
2022 - Jan 1, 2024
You can then attach a transaction/billing model to the contract to be used for
payment allocation:

Billing ModelTypesub_sched_1[Subscription
Schedule](https://docs.stripe.com/api/subscription_schedules)
Given this contract setup, Revenue Recognition can augment reports by
incorporating non-GAAP accounts like contract assets and deferred revenue. In
turn, this enables us to elevate our metrics as the contract undergoes monthly
billing.

## Track contract-level metrics

When you open up a revenue contract in Revenue Recognition, you can track
high-level metrics across a group of contract items and transactions such as:

- Total contract value
- Annual contract value
- Billing to date
- Revenue to date
- Future schedule billings
- Unbilled deferred revenue

## Integration

### Salesforce CPQ Connector

You can import all your orders and contracts generated in Salesforce using the
[Stripe Billing Connector for Salesforce
CPQ](https://docs.stripe.com/connectors/salesforce-cpq/overview). When this
connection is set up, you can manage Stripe Billing subscriptions and revenue
contracts associated with your Salesforce orders.

### API Private preview

You can create and manage revenue contracts through an API integration.

[Contact us](mailto:revrec-revenue-contracts-beta-submissions@stripe.com) to
participate in the private preview.

## Links

- [privacy policy](https://stripe.com/privacy)
- [Revenue Recognition](https://dashboard.stripe.com/revenue-recognition)
- [Price](https://docs.stripe.com/api/prices)
- [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)
- [Stripe Billing Connector for Salesforce
CPQ](https://docs.stripe.com/connectors/salesforce-cpq/overview)