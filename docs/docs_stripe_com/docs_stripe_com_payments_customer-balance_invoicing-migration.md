# Migrate to USD bank transfers from ACH Credit Transfers with Invoicing or Billing

## Learn how to migrate ACH Credit Transfers with Invoicing or Billing to Stripe USD Bank Transfers.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with ACH Credit Transfers, you must [migrate
to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about migrating to USD Bank Transfer supported by the current
APIs, refer to the documentation below.

See [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources)
if you want to learn about the reasons to migrate.

## Before you begin

Confirm if you’re currently using the legacy ACH Credit Transfers product using
the Dashboard or the API:

DashboardAPI
If ACH Credit Transfer is toggled on in your [Invoice Template
Settings](https://dashboard.stripe.com/settings/billing/invoice), then you’re
using ACH Credit Transfers.

If you’re not using ACH Credit Transfers, you can skip this guide because it
doesn’t apply to you.

[Activate USD bank
transfers](https://docs.stripe.com/payments/customer-balance/invoicing-migration#activate-bank-transfers)
To turn on bank transfer payments, navigate to your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

[OptionalTest bank transfers with a single
customer](https://docs.stripe.com/payments/customer-balance/invoicing-migration#test-bank-transfers)
To test bank transfers with an individual invoice or subscription before
enabling bank transfers, use the Dashboard or API:

DashboardAPI- To create a new customer, navigate to the
[Customers](https://dashboard.stripe.com/customers) tab, and click **Add
Customer**.
- After creating the customer, click the row of the customer to navigate to the
customer view page.
- Create an invoice or subscription for the applicable customer by clicking
**Actions** in the top right of the page.
- Under the **Payment Collection** section, add **ACH credit transfer**, and
confirm the invoice or subscription. If you’re testing subscriptions, you need
to wait for a new invoice to be issued or use [Billing
test-clocks](https://docs.stripe.com/billing/testing/test-clocks).
- From the Invoice view page, navigate to the **Details** section, and click the
**Payment page**.
- In the hosted payment page, find the Credit Transfer bank details. Make note
of these details.
- On the same customer, create another invoice or subscription. Under the
**Payment Collection** section, click add **Bank transfer**, and confirm the
invoice or subscription.
- Open the payment page of the bank transfer invoice, and compare the bank
details with the Credit Transfer bank details you noted earlier—the migration is
complete.
[Turn on bank transfers for all
customers](https://docs.stripe.com/payments/customer-balance/invoicing-migration#enable-all-transfers)
After you’ve tested on an individual customer in test mode, attach the payment
method on individual invoices or subscriptions in live mode. To enable Bank
transfers for all of your invoices and subscriptions, navigate to the [Invoice
Template Settings](https://dashboard.stripe.com/settings/billing/invoice),
toggle on **Bank transfers**, and toggle off **ACH credit transfer**.

[OptionalMigrate from the Sources API to the Payment Intents
API](https://docs.stripe.com/payments/customer-balance/invoicing-migration#migrate-from-sources-api)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources)
- [Invoice Template
Settings](https://dashboard.stripe.com/settings/billing/invoice)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Customers](https://dashboard.stripe.com/customers)
- [Billing test-clocks](https://docs.stripe.com/billing/testing/test-clocks)