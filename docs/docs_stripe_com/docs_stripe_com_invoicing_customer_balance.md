# Customer credit balance

## Learn how to work with customer credit balances.

#### Customer balance types

This page is about customer credit balances, which are adjustments you can issue
to customers that apply to future
[invoices](https://docs.stripe.com/api/invoices). Credit balances are different
from cash balances. Cash balances are connected to the [customer balance payment
method](https://docs.stripe.com/payments/bank-transfers). To learn more, see
[Bank transfer](https://docs.stripe.com/invoicing/bank-transfer). As explained
below, some features work differently for customers with a cash balance.

Every customer has a credit balance. You can use this to issue a:

- **Credit adjustment**—You owe the customer money.
- **Debit adjustment**—The customer owes you money.

These adjustments sum up to a credit balance that you can apply to future
invoices. Because Stripe computes the credit balance from a ledger—an immutable
list of debit and credit transactions—it provides an audit trail of transactions
for the customer. The [Customer Balance
Transactions](https://docs.stripe.com/api/customer_balance_transactions/object)
can refer to the object related to the adjustment, such as a [credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes), invoice, or
[metadata](https://docs.stripe.com/api/metadata).

Some common use cases for customer credit balances include:

- [Issuing a credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes#issuing) to
create a credit that reduces the amount due on the next invoice.
- Marking an invoice as paid and moving the amount owed to the credit balance as
a debit. This happens when the amount due on an invoice is less than the
[minimum chargeable
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).
This functionality only occurs for users without a [cash
balance](https://docs.stripe.com/invoicing/customer/balance#cash-balances).

## Credit balances

Keep the following in mind when you work with credit balances:

- The credit balance automatically applies to the next finalized invoice to a
customer.
- You ​​can’t choose a specific invoice to apply the credit balance to.
- The credit balance is in the customer’s currency.
- [Customers](https://docs.stripe.com/api/customers) with a [cash
balance](https://docs.stripe.com/api/customers/object#customer_object-cash_balance)
can’t keep a positive balance. In other words, they can’t increase the amount
due on the next invoice.

## Credits and debits

Credits are negative values (a reduction in the amount the customer owes) that
you can apply to the next invoice. Debits, on the other hand, are positive
values (an increase in the amount the customer owes) that you can apply to the
next invoice.

## Transactions

All modifications to the credit balance are recorded as
[Transactions](https://docs.stripe.com/api/customer_balance_transactions/object).
After you create a transaction, you can only update its `description` or
`metadata` (you can’t edit other properties or delete it).

### Transaction types

All
[Transactions](https://docs.stripe.com/api/customer_balance_transactions/object)
that you create with the API or in the Dashboard have a
[type](https://docs.stripe.com/api/customer_balance_transactions/object#customer_balance_transaction_object-type)
value of `adjustment`. A type value of `adjustment` represents a debit or credit
that you manually created for the customer. The following table describes each
of the `type` values:

TypeDescription`adjustment`An explicitly created adjustment transaction to debit
or credit the credit balance. This is the only type of transaction that you can
create by using API integrations and the Dashboard.`applied_to_invoice`Traces
the application of credit against a linked invoice.`credit_note`Traces the
creation of credit to a [credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes) and ​​its
associated invoice.`invoice_too_small`When the amount due on an invoice is less
than Stripe’s [minimum chargeable
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
and the customer does not have a cash balance, the invoice is debited from the
credit balance and added to the amount due on the next
invoice.`invoice_too_large`When the amount due on an invoice is greater than
Stripe’s [maximum chargeable
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
and the customer does not have a cash balance, the invoice is debited from the
credit balance and added to the amount due on the next
invoice.`unapplied_from_invoice`Traces the reversal of an applied credit balance
from a linked invoice. Paired with an earlier ‘applied_to_invoice’
transaction.`unspent_receiver_credit`When unspent funds in [receiver
Sources](https://docs.stripe.com/sources#flow-for-customer-action) attached to a
customer without cash balance aren’t fully charged after 60 days, Stripe
automatically charges them on your behalf and credits your balance. When this
happens, Stripe also creates a corresponding credit
transaction.`initial`Represents the starting value of the credit balance when a
customer is created by using the API with a non-zero credit balance.
### Undo a transaction

You can only undo a transaction by creating a corresponding, reversing
transaction. For example, if you credit the customer ​​10 USD, you’d have to
debit them 10 USD in a new transaction, each canceling the other one out.

## Modify the credit balance

You can modify a customer’s credit balance through both the Dashboard and API.

DashboardAPI
You can modify a customer’s credit balance through the [Customers
page](https://dashboard.stripe.com/customers) in the Dashboard by creating a new
[Customer Balance
Transaction](https://docs.stripe.com/api/customer_balance_transactions/object)
adjustment.

In the **Customers** page, click on the customer and then click **Adjust
balance** under **Credit balance**. From here, set the **Adjustment type**, a
**Currency** (only available if the customer doesn’t have a currency set), an
**Amount**, and an **internal note**.

#### Note

The **internal note** is only visible to Dashboard users.

!

Add a new customer balance transaction adjustment

## Balance transaction history

DashboardAPI
Audit a customer’s balance adjustments in the **Customers** page by scrolling
down to the **Credit balance** section. This section displays the current value
of the customer credit balance.

## Customer cash balances

Customers using the [bank
transfers](https://docs.stripe.com/payments/bank-transfers) payment method have
a [cash balance
object](https://docs.stripe.com/api/customers/object#customer_object-cash_balance)
with one or more currencies in the `available` object. You can use the funds to
[make
payments](https://docs.stripe.com/payments/customer-balance#make-cash-payment)
or pay invoices. Customers with available balances have the following behavior:

- You can’t create a negative customer cash balance since it represents money
sent from the `Customer`.
- You can’t finalize a too-small or too-large invoice with the cash balance (for
example, creating a subscription for 0.01 USD). Learn more about [minimum and
maximum
amounts](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).
- You can delete `Customers` that have a cash balance, but only if their cash
balance is 0.
- You can’t remove a `Customer`’s available balance.

## See also

- [Stripe data](https://docs.stripe.com/stripe-data)

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [customer balance payment
method](https://docs.stripe.com/payments/bank-transfers)
- [Bank transfer](https://docs.stripe.com/invoicing/bank-transfer)
- [Customer Balance
Transactions](https://docs.stripe.com/api/customer_balance_transactions/object)
- [credit note](https://docs.stripe.com/invoicing/dashboard/credit-notes)
- [metadata](https://docs.stripe.com/api/metadata)
- [Issuing a credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes#issuing)
- [minimum chargeable
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
- [Customers](https://docs.stripe.com/api/customers)
- [cash
balance](https://docs.stripe.com/api/customers/object#customer_object-cash_balance)
-
[type](https://docs.stripe.com/api/customer_balance_transactions/object#customer_balance_transaction_object-type)
- [receiver Sources](https://docs.stripe.com/sources#flow-for-customer-action)
- [Customers page](https://dashboard.stripe.com/customers)
- [make
payments](https://docs.stripe.com/payments/customer-balance#make-cash-payment)
- [Stripe data](https://docs.stripe.com/stripe-data)