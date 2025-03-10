# Deposit automation

## Use the connector to automate the bank reconciliation process.

The Stripe Connector for NetSuite automates the bank reconciliation process by
creating bank deposits in NetSuite for all of your [Stripe
payouts](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite).
The connector also automates fee calculation, the refund life cycle, the dispute
life cycle, and handling of multiple currencies and subsidiaries. This means you
only need to match the bank deposit record to the Stripe deposits on your bank
statement, reducing the amount of manual work required each month. Every
automated payment workflow that the connector supports includes deposit
automation.

## How it works

When you use the connector, the automated bank reconciliation process occurs
daily as follows:

- The connector creates payments and refunds for each Stripe transaction, and
posts these transactions in the Undeposited Funds account in NetSuite.
- Stripe notifies the connector that a bank transfer (Stripe payout) has
successfully arrived at your bank.
- The connector creates a bank deposit record in NetSuite that contains all of
the payments, refunds, and disputes from that day’s bank deposit.
- The connector calculates any fees for processing, currency conversion,
disputes, and refunds, and includes these as separate line items that post to
your specified expense accounts.
- The connector ensures that the deposit total and deposit date match your bank
statement.

Stripe

Connector

NetSuite

Cash reconciliation

Stripe creates payment

Connector creates NetSuite payment and posts to Undeposited Funds account

Connector adds payment to bank deposit and moves payment to bank account
specified on the deposit

Stripe issues refund or chargeback

Connector creates NetSuite refund and posts to Undeposited Funds account

Connector adds refund to bank deposit and moves refund to bank account specified
on the deposit

Stripe sends payout to your bank

Stripe payout arrives in your bank account

Connector creates bank deposit that includes all transactions and processing
fees

A diagram providing a high level overview of the deposit automation flow
outlined in this doc
## See also

- [Charges in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-charges-netsuite)
- [Payouts in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite)
- [Disputes in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
- [Refunds in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)

## Links

- [Stripe App
Marketplace](https://marketplace.stripe.com/apps/netsuite-connector)
- [Stripe
payouts](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite)
- [Charges in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-charges-netsuite)
- [Disputes in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
- [Refunds in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)