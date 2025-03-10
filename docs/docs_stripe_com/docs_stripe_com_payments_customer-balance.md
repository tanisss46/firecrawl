# Customer balance

## Learn how to use the customer balance with payments.

Your customers might have associated balances that contain two types of
funds—cash and credit.

## Cash balances

A customer’s cash balance represents funds that they can use for payment. When
they overpay or send an amount using a bank transfer that isn’t automatically
reconciled with any outstanding payment, we add these funds to the customer cash
balance. You can use these funds for later payments for the same customer, or
[initiate a
refund](https://docs.stripe.com/payments/customer-balance/refunding#create-return-dashboard)
from their cash balance to return the funds to their bank account, limited to
the amount available in the customer balance.

A customer can have cash balances in all currencies that you accept bank
transfer payments in- each with it’s own [funding
instruction](https://docs.stripe.com/payments/bank-transfers#funding-instructions).

You can’t add funds to the customer cash balance directly. This isn’t a balance
that customers can top up and is only there as a reconciliation layer—it’s not a
digital wallet or e-money. You can’t use the cash balance for any other purpose
besides future payments, or returns to the customer it’s associated with.

## Customer invoice balance

In contrast to a cash balance, an *invoice balance* is an
[Invoices](https://docs.stripe.com/api/invoices) feature that represents
liability between you and the customer. You can’t use invoice balance funds for
payment, but you can apply them to offset future invoices. You can update the
invoice balance by creating an adjustment [Customer Balance
Transaction](https://docs.stripe.com/api/customer_balance_transactions/object).

## View the customer balance

You can find a customer’s balance with both the API and through the Stripe
Dashboard. To view a customer’s balance using the API, first retrieve the
`customer` and then expand the `cash_balance` field.

```
curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}}?expand[]=cash_balance \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
```

```
{
 "id": "cus_HgrkK7bxHMy65g",
 "object": "customer",
 "address": null,
 "cash_balance": {
 "available": {
 "usd": 50,
 },
 "settings": {
 "reconciliation_mode": "automatic"
 },
 "livemode": "true",
 "object": "cash_balance",
 },
 "created": 1598918400,
```

See all 78 lines
To view a customer’s balance in the Dashboard, navigate to the **Customer**
page. The customer’s balance appears in the **Payment methods** section.

## Make a payment from the cash balance

When your customer has a cash balance, you can use the funds immediately to make
a payment up to the available amount. To do this, create a PaymentIntent using
the `customer_balance` payment method type.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1099 \
 -d currency=usd \
 -d customer="{{CUSTOMER_ID}}" \
 -d "payment_method_types[]"=customer_balance \
 -d "payment_method_data[type]"=customer_balance \
 -d confirm=true
```

When your customer has a cash balance, you can use the funds immediately to make
a payment up to the available amount. You can do this by using either the API or
the Dashboard.

To make a payment using the API, create a PaymentIntent using the
`customer_balance` payment method type.

The payment succeeds if the cash balance has sufficient funds, and fails
otherwise.

To collect more funds from the customer when the cash balance is insufficient,
use the customer balance with a [bank transfer
funding](https://docs.stripe.com/payments/bank-transfers/accept-a-payment).

## List changes to the customer balance

Changes to the customer’s cash balance are modeled as a list of [cash balance
transactions](https://docs.stripe.com/api/cash_balance_transactions/object). You
can retrieve these transactions for a customer to see how their cash balance has
changed over time.

#### Note

For a customer with multiple cash balances in different currencies, listing
changes to the cash balance will return changes for all the different
currencies.

## Cash balance transaction types

Cash balance transactions have a
[type](https://docs.stripe.com/api/cash_balance_transactions/object#customer_cash_balance_transaction_object-type)
value indicating the type of action that caused the cash balance to change.

TypeDescription`funded`The customer has funded their balance by making a bank
transfer. Funds represented by these transactions might be automatically applied
to payment intents and invoices depending on the
[reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation)
procedure. If these funds are applied automatically, you’ll see additional
transactions of type `applied_to_payment` representing
that.`applied_to_payment`Funds from the cash balance were applied to a payment
intent, either by
[reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-automatic-reconciliation)
after funding arrives, or by [manual
reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-manual-reconciliation).`unapplied_from_payment`A
[partially
funded](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#handling-underpayments-and-overpayments)
payment intent was
[modified](https://docs.stripe.com/api/payment_intents/update) or
[canceled](https://docs.stripe.com/api/payment_intents/cancel), and the funds
were returned to the customer’s cash balance. You can use these funds for future
payments.`refunded_from_payment`A successful payment intent has been [refunded
to the customer cash
balance](https://docs.stripe.com/payments/customer-balance/refunding#refund-customer-balance-payment-customer-balance).
You can use these funds for future payments.`return_initiated`Unspent funds are
being returned to the customer’s bank account from their cash
balance.`return_canceled`An attempt to return funds to the customer’s bank
account has been canceled, either because you [canceled the refund before the
customer submitted their bank
details](https://docs.stripe.com/payments/customer-balance/refunding#create-return-dashboard-cancel),
or we weren’t able to collect bank account details from the customer. For more
information about refund state transitions, see [Refund bank transfer
payments](https://docs.stripe.com/payments/customer-balance/refunding#refund-customer-balance-payment-bank-account).`funding_reversed`Funds
have been debited from the cash balance due to an [ACH
reversal](https://docs.stripe.com/payments/payment-methods/bank-transfers/reversals-us).`adjusted_for_overdraft`Funds
have been returned to the cash balance after an [ACH
reversal](https://docs.stripe.com/payments/payment-methods/bank-transfers/reversals-us)
caused the balance to go negative.`transferred_to_balance`Funds have been moved
from the cash balance to your Stripe balance due to failed refunds or
insufficient refund details.

## Links

- [initiate a
refund](https://docs.stripe.com/payments/customer-balance/refunding#create-return-dashboard)
- [funding
instruction](https://docs.stripe.com/payments/bank-transfers#funding-instructions)
- [Invoices](https://docs.stripe.com/api/invoices)
- [Customer Balance
Transaction](https://docs.stripe.com/api/customer_balance_transactions/object)
- [bank transfer
funding](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [cash balance
transactions](https://docs.stripe.com/api/cash_balance_transactions/object)
-
[type](https://docs.stripe.com/api/cash_balance_transactions/object#customer_cash_balance_transaction_object-type)
-
[reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation)
-
[reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-automatic-reconciliation)
- [manual
reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-manual-reconciliation)
- [partially
funded](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#handling-underpayments-and-overpayments)
- [modified](https://docs.stripe.com/api/payment_intents/update)
- [canceled](https://docs.stripe.com/api/payment_intents/cancel)
- [refunded to the customer cash
balance](https://docs.stripe.com/payments/customer-balance/refunding#refund-customer-balance-payment-customer-balance)
- [canceled the refund before the customer submitted their bank
details](https://docs.stripe.com/payments/customer-balance/refunding#create-return-dashboard-cancel)
- [Refund bank transfer
payments](https://docs.stripe.com/payments/customer-balance/refunding#refund-customer-balance-payment-bank-account)
- [ACH
reversal](https://docs.stripe.com/payments/payment-methods/bank-transfers/reversals-us)