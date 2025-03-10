# Stripe Connector for Salesforce BillingDeprecated

## Learn about the Stripe Connector for Salesforce Billing that you can install on top of Salesforce CPQ and Salesforce Billing.

#### Note

For integrating with Salesforce CRM, Core, and Platform, we recommend using the
[Stripe Connector for Salesforce
Platform](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/overview).

Stripe Connector for Salesforce Billing is a managed package that you install on
top of Salesforce CPQ and Salesforce Billing. It allows users to process
payments through the Salesforce Payment Gateway using Stripe payment service to
complete transactions.

Stripe exposes four transaction types directly from the Salesforce Billing UI:

- Tokenization—Create a new payment method on an account and set it as the
default.
- Charge Transaction—Charge a specific amount to an account.
- Refund Transaction—Refund a specific amount to an account.
- Bidirectional Data Sync-See related transactions in both Salesforce and Stripe
dashboards.

In addition to the UI-based transaction types, Stripe also offers API-based
transaction types, which developers can use to create methods that take
advantage of the features on the Stripe payment service:

- Void Token—Remove a payment method from an account.
- Authorize Transaction—Allocate a specific amount to an account pending a
charge.
- Capture Transaction—Complete a charge on an authorized transaction.
- Void Transaction—Void a charge on an authorized transaction.
- Get Payment Status—Return the status of a specific charge.
- Get Refund Status—Return the status of a specific refund.

The UI-based transaction types (tokenization, charge, refund) are also supported
through the API.

The Following Payment Methods are supported:

- **Cards**—Support for global and local card networks
- **ACH**—ACH Direct Debit payments from customers with a US bank account

## Next steps

- [Installation](https://docs.stripe.com/connectors/salesforce-billing/install)
-
[Configuration](https://docs.stripe.com/connectors/salesforce-billing/configuration)

## Links

- [Stripe Connector for Salesforce
Platform](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/overview)
- [Installation](https://docs.stripe.com/connectors/salesforce-billing/install)
-
[Configuration](https://docs.stripe.com/connectors/salesforce-billing/configuration)