# Stripe Billing and Invoicing automation

## Use the connector to sync your Stripe invoices into NetSuite.

The Stripe Connector for NetSuite automatically syncs the invoices that you
create from Stripe Billing
[subscriptions](https://docs.stripe.com/billing/subscriptions/overview) or
[Stripe Invoicing](https://docs.stripe.com/invoicing/overview) into NetSuite.
The sync includes details such as [credit
notes](https://docs.stripe.com/invoicing/dashboard/credit-notes),
[discounts](https://docs.stripe.com/billing/subscriptions/coupons),
[uncollectible
invoices](https://docs.stripe.com/revenue-recognition/examples/contra#uncollectible),
[taxes](https://docs.stripe.com/billing/taxes/collect-taxes), and
[prorations](https://docs.stripe.com/billing/subscriptions/prorations).

You can complete your accounting workflows entirely in Stripe using the
automated process, which means you don’t need to manually reconcile activity.
Stripe transaction data syncs at the transaction level in NetSuite, allowing you
to use advanced reporting on Stripe data in NetSuite.

## How it works

When you use the connector with [Stripe
Billing](https://docs.stripe.com/billing) or [Stripe
Invoicing](https://docs.stripe.com/invoicing/overview), the invoice automation
process is as follows:

- A customer provides their payment information through a Stripe payment flow on
your website. This action creates a Stripe `Customer` object.
- Stripe creates an invoice at the beginning of each billing period, which
prompts the connector to create an invoice in NetSuite. The connector also
creates a new customer or links to an existing NetSuite customer.
- If you enabled NetSuite revenue recognition, the connector splits revenue over
the correct period on the line item level.
- When a customer successfully pays the Stripe invoice, the connector creates a
NetSuite `Customer Payment` and applies it to the corresponding invoice in
NetSuite. If payment fails, resulting in a canceled subscription, the connector
can automatically close the NetSuite invoice with a credit memo, or whatever
action you configure for failed payments.
- The connector automatically syncs refunds and disputes from Stripe to
NetSuite, and creates credit memos and customer refunds.
- The connector [automatically
reconciles](https://docs.stripe.com/connectors/netsuite/deposit-automation)
Stripe payments against a bank deposit in NetSuite. This includes calculating
and recording any processing fees or currency conversion fees.

## Customer flow

Customer

Stripe

Connector

NetSuite

To initiate the [customer
flow](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite), a
customer submits payment on your website

Stripe creates a Customer object to store payment details

The connector creates a NetSuite customer when creating an invoice

A diagram providing a high level overview of the customer flow for billing and
invoice automation outlined in this doc
## Invoice flow

Business

Stripe

Connector

NetSuite

You initiate the Stripe [invoice
flow](https://docs.stripe.com/connectors/netsuite/stripe-invoices-netsuite)
through the backend or Dashboard

Stripe finalizes the invoice

The connector creates a NetSuite invoice

A diagram providing a high level overview of the invoice flow for billing and
invoice automation outlined in this doc
## Payment flow

Customer

Stripe

Connector

NetSuite

Cash reconciliation

To initiate the [payment
flow](https://docs.stripe.com/connectors/netsuite/stripe-charges-netsuite#charges-for-invoices),
a customer pays an invoice

Stripe applies the charge to the invoice

The connector creates and posts the customer payment to the Undeposited Funds
account, and applies it to the invoice

The connector moves the settled deposit from the bank to a general ledger
account

A diagram providing a high level overview of the payment flow for billing and
invoice automation outlined in this doc
## Refund or chargeback flow

Customer

Stripe

Connector

NetSuite

Cash reconciliation

To initiate the
[refund](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite) or
[chargeback](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
flow, a customer requests a refund or disputes a charge

Stripe issues a refund or chargeback

The connector creates a credit memo and customer refund, and posts it to the
Undeposited Funds account for a full or partial refund

The connector moves the settled deposit from the bank to a general ledger
account

A diagram providing a high level overview of the refund or chargeback flow for
billing and invoice automation outlined in this doc
## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Stripe invoices in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-invoices-netsuite)
- [Stripe prices and coupons in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-prices-coupons-netsuite)
- [Revenue
recognition](https://docs.stripe.com/connectors/netsuite/revenue-recognition)

## Links

- [Stripe App
Marketplace](https://marketplace.stripe.com/apps/netsuite-connector)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Stripe Invoicing](https://docs.stripe.com/invoicing/overview)
- [credit notes](https://docs.stripe.com/invoicing/dashboard/credit-notes)
- [discounts](https://docs.stripe.com/billing/subscriptions/coupons)
- [uncollectible
invoices](https://docs.stripe.com/revenue-recognition/examples/contra#uncollectible)
- [taxes](https://docs.stripe.com/billing/taxes/collect-taxes)
- [prorations](https://docs.stripe.com/billing/subscriptions/prorations)
- [Stripe Billing](https://docs.stripe.com/billing)
- [automatically
reconciles](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [customer
flow](https://docs.stripe.com/connectors/netsuite/stripe-customers-netsuite)
- [invoice
flow](https://docs.stripe.com/connectors/netsuite/stripe-invoices-netsuite)
- [payment
flow](https://docs.stripe.com/connectors/netsuite/stripe-charges-netsuite#charges-for-invoices)
- [refund](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)
-
[chargeback](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
- [Stripe prices and coupons in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-prices-coupons-netsuite)
- [Revenue
recognition](https://docs.stripe.com/connectors/netsuite/revenue-recognition)