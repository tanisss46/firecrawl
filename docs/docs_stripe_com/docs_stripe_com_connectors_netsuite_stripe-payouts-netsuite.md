# Stripe payouts in NetSuite

## Use the connector to automatically reconcile Stripe payouts to NetSuite bank deposits.

The Stripe Connector for NetSuite automates the cash reconciliation process for
any payments, refunds, or disputes processed by Stripe. In addition to creating
bank deposits in NetSuite for all of your [Stripe
payouts](https://support.stripe.com/topics/payouts), the connector records fees
and automates currency conversion. The connector records all fees and
transactions associated with a payout into a single deposit record.

## How it works

When you use the connector, the automated cash reconciliation process occurs as
follows:

- Each Stripe transaction results in a bank deposit that’s posted to the
`Undeposited Funds` account in NetSuite.
- The connector moves the bank deposit from the `Undeposited Funds` account to
the bank account specified on the deposit.
- The connector records fees and reversals as line items on the NetSuite
deposit:- Stripe fees or fee refunds: `Cash Back` and `Other Deposit`
- Dispute fees or dispute reversals: `Cash Back`
- The deposit posts to the NetSuite bank account connected to your Stripe
account.
- The connector verifies that the total amount on the deposit record and
transaction date match your bank statement.

#### Note

If the deposit doesn’t match the payout, the connector adds a note to the memo
field to notify you of the mismatch. This can happen if the connector isn’t set
up for certain Stripe or NetSuite configurations, or if you have transactions
from before the record sync start date.

Stripe

Connector

NetSuite

Cash reconciliation

Stripe creates payment

The connector creates NetSuite payment and posts to the Undeposited Funds
account

The connector adds the payment to the bank deposit and moves the payment to the
bank account specified on the deposit

Stripe issues a refund or chargeback

The connector creates a NetSuite refund and posts it to the Undeposited Funds
account

The connector adds the refund to the bank deposit and moves it to the bank
account specified on the deposit

Stripe sends the payout to your bank

The Stripe payout arrives in your bank account

The connector creates a bank deposit that includes all transactions and
processing fees

A high level overview of the deposit automation flow
## Payout validation process

Every Stripe transaction in a payout goes through a validation process that
compares the payments, refunds, and disputes against their corresponding
NetSuite records.

The connector validates that the records:

- Aren’t already deposited
- Are posted to the `Undeposited Funds` account
- Have matching amounts between NetSuite and Stripe

### Successful validation

If all transactions in a payout pass the validation process, the connector
creates a deposit that’s linked to the associated transactions. This action
changes the status of any payments refunds from `Not Deposited` to `Deposited`.

### Unsuccessful validation

If a payment, refund, or dispute fails the validation process, the connector
doesn’t sync the payout to NetSuite. Your administrators receive a notification
email that provides information about which records failed validation and the
reasons why. Learn about the potential [errors you might
receive](https://docs.stripe.com/connectors/netsuite/error-resolution) and how
to fix them.

The connector automatically retries syncing if payout validation fails, or if
you update a payout in Stripe (for example, by adding metadata). You can also
manually retry a payout through the synced records drawer.

## Types of fees

Different actions in Stripe can result in fees. Most fees post to the `Payment
fees` category, by default. If applicable, you can customize the accounts used
for these fees in the Stripe app under **Settings** > **Accounts mapping**. To
do so, disable `Only show accounts used` and optionally set a specific expense
account for each fee type.

Fee typeDescriptionPayment processing feesThese fees appear in the `Payment
fees` category and are distinct from fees charged by Stripe for other services
outside of payment processing.Stripe feesThese fees are for Stripe software and
services such as premium support, fraud protection, connectors, and so on. These
fees post to the same account as payment processing fees; however, you can
customize the accounts you use for these fees.Application feesApplications
charge these fees for taking actions in your Stripe account on your behalf. For
example, an event ticketing system might charge you a fee for each ticket you
sell. The fees charged by third-party applications appear aggregated on each
payout and post to a unique expense account.Interchange Plus pricing and fees
(IC+)IC+ is a special type of pricing provided by Stripe and changes how your
account represents fees. Because Stripe receives the fee amount later and
directly from the card networks, you won’t see any fees when you look at a
charge in the Stripe Dashboard. You also won’t see IC+ fees in your Stripe test
environment payouts. When you receive a bank payout, fees record under two
categories: `network fees` and `Stripe fees`. These fee categories are
controlled by the `Processing fees` and `Stripe fees` categories in the Stripe
Dashboard. You can post these fee categories to unique income accounts in
NetSuite.
## Multiple currencies and currency conversion

Stripe supports charges and payouts to bank accounts in multiple currencies. If
your Stripe account has multiple bank accounts with different currencies, you
need to provide the NetSuite bank account that you want the connector to use for
each bank account. You can customize the accounts used in the Stripe app under
**Settings** > **Accounts mapping**.

## Subsidiaries

If you use [NetSuite
OneWorld](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N266701.html)
and have multiple subsidiaries, the subsidiaries must match across the different
record types.

For example, the fee account subsidiary must match the bank account subsidiary.
Or you must assign the subsidiary to a parent subsidiary with the `Include
Children` setting enabled in NetSuite. The subsidiary associated with all
payments customers must match the bank account subsidiary. If you use the
connector to create customers and payments, the connector handles this
automatically.

## Automatic payouts

The connector requires you to set up automatic payouts in your Stripe account.
This allows the connector to monitor payouts sent automatically and reconcile
the transactions in the payouts with the created records in NetSuite.

To set up automatic payouts, go to the [External payout accounts and
scheduling](https://dashboard.stripe.com/settings/payouts) page in the Stripe
Dashboard. Set the payout schedule to `Automatic every day`.

NetSuite can create and send up to 10,000 transactions. Setting the payout
schedule to daily maintains a lower volume per payout and prevents backups and
errors. If you have a low transaction volume, you can also set the payout
schedule to weekly.

If you use manual payouts:

- Deposit automation won’t work. This includes recording fees and disputes, or
handling currency conversion.
- NetSuite payments aren’t mapped to any specific charges, refunds, or disputes.
- All payments, refunds, and disputes post to, and remain in, the `Undeposited
Funds` account. You must manually manage these transactions.
- The connector can’t include specific payments in a deposit or move them out of
the `Undeposited Funds` account to your bank account.
- Invoices, cash application, and refunds reconcile and sync as expected.

#### Note

If your NetSuite deposit doesn’t appear as a deposit of funds to your bank
account, your bank might block [debit
payouts](https://support.stripe.com/questions/handling-negative-balances-in-your-stripe-account).
In this case, the payout still syncs to NetSuite as if it succeeded. However, if
your bank blocked the debit payout, it won’t appear on your bank register. To
resolve this, you must group the blocked debit payout with the successful payout
from Stripe.

## Test payouts with the connector

Similar to the Stripe production environment, payouts are created automatically
in your test environment.

To test syncing payouts with the connector, you need to wait for a payout to
bundle your test charges and refunds. Use a [test
card](https://docs.stripe.com/testing#available-balance) to move funds directly
to the available balance instead of the pending balance.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)

## Links

- [Stripe payouts](https://support.stripe.com/topics/payouts)
- [errors you might
receive](https://docs.stripe.com/connectors/netsuite/error-resolution)
- [NetSuite
OneWorld](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N266701.html)
- [External payout accounts and
scheduling](https://dashboard.stripe.com/settings/payouts)
- [debit
payouts](https://support.stripe.com/questions/handling-negative-balances-in-your-stripe-account)
- [test card](https://docs.stripe.com/testing#available-balance)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)