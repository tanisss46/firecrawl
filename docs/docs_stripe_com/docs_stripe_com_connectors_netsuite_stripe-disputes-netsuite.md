# Stripe disputes in NetSuite

## Learn about how NetSuite automatically represents Stripe disputes or chargebacks.

The Stripe Connector for Netsuite automatically creates a corresponding object
in NetSuite for disputes (or chargebacks) immediately after they occur in
Stripe. Depending on your payment flow, the disputes might appear differently.

## How it works

When a customer [disputes](https://docs.stripe.com/disputes) a charge, the
dispute process occurs as follows:

- Stripe charges you a processing fee for the dispute and withdraws the full
amount of the charge from your Stripe account balance.
- You respond to the dispute with evidence, which Stripe sends to the bank for
evaluation and determination of the dispute outcome.
- The connector records the dispute fee as a cash-back line item. By default,
the dispute fee posts to the same account as your credit card processing fees.
You can customize where to post fees by going to **Settings** > **Accounts
mapping** > **Dispute fees** in the Stripe app.
- The connector creates a customer refund and records the fee on the bank
deposit.
- If you applied the customer payment to a NetSuite invoice, the connector also
creates a credit memo against the invoice.
- If you win the dispute, Stripe returns the dispute amount and fee to your
Stripe balance.
- The connector records the returned funds and fee reversal to the bank deposit.

## Dispute reversals

Winning a dispute (or receiving a chargeback reversal) occurs when the bank
grants a dispute in your favor. When you win a dispute, Stripe refunds the
dispute fee and includes the full amount of the original charge in your next
payout.

NetSuite represents this as follows:

- The fee refund appears as an **Other Deposit** line item on the next payout.
- The chargeback reversal appears as an **Other Deposit** line item and posts to
your default income account. You can specify which account to post this line
item to.

The connector makes sure to properly account for cash from dispute reversals,
while allowing you to handle income, revenue recognition, and cash application
using your own manual or automated process.

After you win a dispute, you can specify which account to return the disputed
charge to. To do so, go to **Settings** > **Accounts mapping** > **Dispute
reversals** in the Stripe app.

For example, you can configure the connector to post dispute reversal cash to
accounts receivable instead of income. Then you can manually or automatically
create journal entries or invoices to represent any income entries associated
with the won chargebacks.

## Customize the dispute general ledger impact

Credit memos are always created if the disputed payment is applied to an
invoice. When creating a credit memo for a dispute, the connector includes the
original items on the invoice, by default.

If you don’t want to use the original items on the invoice, you can use a
`Stripe Dispute Item` instead. Use this approach if you want the dispute to post
to a specific account, or you sell physical products and don’t want the
dispute’s credit memo to affect NetSuite inventory levels.

The `Stripe Dispute Item` posts to your default income account. You can specify
where to post dispute items and credit memos. To do so, edit the account of the
item in NetSuite. You can also edit any other aspect of the item, and the
connector won’t override those modifications.

## Handle mismatched amounts

The dispute amount might not match the original payment amount in the following
cases:

- If the connector isn’t managing payment creation, calculation of the cash
amount of the original payment might be incorrect. For example, you might have
shipping and tax calculations that aren’t synced correctly from an external
system, such as Shopify or Magento.
- If Stripe receives a dispute that’s greater than the original charge amount.
For example, you could have a [currency-converted
payment](https://docs.stripe.com/currencies/conversions#conversions-disputes-refunds)
that’s disputed, but the amount you received is converted back to the
presentment currency.

If you have a mismatch between the amounts:

- For a single item on the original invoice, the connector adjusts the item to
match the dispute amount.
- For multiple items on the original invoice, the connector can’t determine
which items to adjust. Instead of using the original items on the invoice, the
connector uses a global `Stripe Dispute Item` to represent the full dispute
amount on the credit memo.

## Test disputes with the connector

To test disputes, use a [test card](https://docs.stripe.com/testing#disputes) to
create a dispute in your Stripe test environment.

## See also

- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Stripe payouts in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite)
- [Stripe refunds in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)

## Links

- [disputes](https://docs.stripe.com/disputes)
- [currency-converted
payment](https://docs.stripe.com/currencies/conversions#conversions-disputes-refunds)
- [test card](https://docs.stripe.com/testing#disputes)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Stripe payouts in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-payouts-netsuite)
- [Stripe refunds in
NetSuite](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)