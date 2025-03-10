# Migrate your customer data to Stripe

## Successfully migrate your customers' data to Stripe.

Migrating your customer data to Stripe is a multi-step process. After you read
through this guide, you’ll:

- Understand the Stripe migration process.
- Be able to scope the timeline for your migration.
- Know the integration elements required for a successful migration.
- Understand how to migrate payment details with minimal disruption to your
users.

If you run into issues while trying to migrate customer data, contact [Stripe
support](https://support.stripe.com/contact/login?email=true&subject=Migration+to+Stripe).

## Build your integration

- Develop your data migration plan, starting with new customers. Your end goal
is to migrate 100% of new customers, then migrate existing customers.
- Design a process for customers to update their card information.

## Learn about the migration process

- Review Stripe’s [migration
documentation](https://docs.stripe.com/get-started/data-migrations/pan-import).
- Contact your previous processor to understand their migrations process.

## Plan a migration and connect with an existing processor

- Identify which payment details you want to migrate.
- Identify which payment methods you want to migrate.
- Find out how many customer records you want to migrate.
- Plan a migration timeline that considers your previous processor, your
customer count, and any upcoming deadlines.
- Send the Stripe Migrations team details about your previous processor, Stripe
account number, number of records to be migrated, and types of payment methods
that you plan to import.

## The Stripe Migrations team

- Introduce your existing processor to Stripe’s Migrations team.
- Complete any action items or provide any additional information requested by
Stripe or your existing processor’s migrations team.

## Migrate and update

- Follow communication between Stripe and your previous processor to ensure your
team is prepared.
- Respond to any issues identified during migration.
- Look for an email from the Stripe Migration team with the JSON mapping file.
- Parse JSON mapping file and update your database accordingly.
- Implement a process for customers to update their card information.
- Design your remapping plan, and include
[subscription](https://docs.stripe.com/billing/subscriptions/creating) remapping
where applicable.
- Begin charging existing customers on Stripe.

## PAN data

If you need to transfer sensitive payment information to or from another payment
processor, or even between Stripe accounts, we can help you do so in a secure
and
[PCI-compliant](https://docs.stripe.com/security/guide#validating-pci-compliance)
way.

The process differs depending on the type of transfer:

- [Transfer PAN data from one Stripe account to another Stripe
account](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
- [Import PAN data to Stripe from another payment
processor](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [Export PAN data from Stripe to another payment
processor](https://docs.stripe.com/get-started/data-migrations/pan-export)

For each type of data migration, we can only assist you if your request includes
both customer records and the associated payment data. Use Stripe’s [Customer
API](https://docs.stripe.com/api/customers) to create, update, or retrieve
customer data that doesn’t include payment information.

#### Note

You can perform PAN data migrations without using Stripe’s Sigma or Data
Pipeline products.

## See also

- [The Customer object](https://docs.stripe.com/api/customers/object)
- [The Subscription object](https://docs.stripe.com/api/subscriptions/object)
- [Default payment
source](https://docs.stripe.com/api/customers/object#customer_object-default_source)
- [Products and prices](https://docs.stripe.com/products-prices/overview)
- [Billing cycle
anchor](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_cycle_anchor)

## Links

- [Stripe
support](https://support.stripe.com/contact/login?email=true&subject=Migration+to+Stripe)
- [migration
documentation](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
-
[PCI-compliant](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [Transfer PAN data from one Stripe account to another Stripe
account](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
- [Export PAN data from Stripe to another payment
processor](https://docs.stripe.com/get-started/data-migrations/pan-export)
- [Customer API](https://docs.stripe.com/api/customers)
- [The Customer object](https://docs.stripe.com/api/customers/object)
- [The Subscription object](https://docs.stripe.com/api/subscriptions/object)
- [Default payment
source](https://docs.stripe.com/api/customers/object#customer_object-default_source)
- [Products and prices](https://docs.stripe.com/products-prices/overview)
- [Billing cycle
anchor](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_cycle_anchor)