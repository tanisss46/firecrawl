# Stripe customer balance in NetSuite

## Use the connector to represent Stripe customer balances in NetSuite.

The connector represents a Stripe [customer
balance](https://docs.stripe.com/billing/customer/balance) in NetSuite only
after it’s used.

The connector creates a credit memo against an invoice for the amount paid when:

- The invoice is paid by a customer’s balance.
- The invoice is marked as paid.

If the invoice is only partially paid by the customer’s balance, a corresponding
Stripe charge for the remaining balance must exist before the connector can
create a credit memo. The connector won’t create a credit memo for a partially
paid invoice that’s open with an outstanding amount.

The credit memo that represents the customer balance contains:

- `Stripe: [invoice ID]. This credit memo was created by a Stripe customer's
balance.`
- The line item from the invoice

## NetSuite items used for customer balances

If a customer balance isn’t completely used on the first invoice created after
downgrading a product price, the connector does the following:

- Applies the credit memo representing the customer balance to future invoices
- Represents the credit memo as a Stripe Customer Balance item in NetSuite

The connector uses a global item to track customer balance usage in NetSuite
because there isn’t a way to determine what the customer balance represents. You
can optionally use a unique item for all customer balance credits. This allows
you to make sure all discounts given through the customer balance post to a
specific general ledger account. You can then run reports by item and see a
breakout of customer balance usage.

## Negative invoices

NetSuite doesn’t support negative amounts on invoices. The connector handles
this scenario by creating an invoice with all line items with a zero amount. The
connector represents a customer balance amount (the negative amount on an
invoice) when it’s used on subsequent invoices.

For example, say you downgrade the price for a customer’s subscription. The
prorated, unused amount on the subscription product price is greater than the
amount of the prorated, new product price. If this occurs, the Stripe invoice
has a negative amount total, which is added to the customer balance.

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

- [customer balance](https://docs.stripe.com/billing/customer/balance)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Invoice
automation](https://docs.stripe.com/connectors/netsuite/invoice-automation)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)