# Exclusion examples

## Learn about revenue recognition with exclusion examples.

Unless stated otherwise, these exclusion examples assume that revenue
recognition takes place on a per-day basis.

## Exclude transactions

Transactions behave differently when excluded, depending on whether they have
been paid or not. If a transaction is paid in cash, Stripe debits the cash
account and credits the exclusion account after exclusion. If it’s paid by
CustomerBalance, Stripe debits the customer balance account and credits the
customer balance adjustments account after exclusion. Stripe doesn’t generate
journal entries for unpaid transactions; they behave as if the transaction never
occurred.

If you exclude transactions in a closed accounting period, it incurs corrections
for transactions that have already been paid. Learn more about
[corrections](https://docs.stripe.com/revenue-recognition/reports).

### Exclude paid transactions

This example uses the following assumptions:

- On January 5, 2022, at 09:00:00 UTC, you create a one-time payment of 10 USD
using either the Dashboard, the Charges APIs, or the Payment Intents APIs.
- By default, Revenue Recognition immediately recognizes the revenue from this
one-time payment.
- On February 5, 2022, you exclude the payment.
- The accounting periods for January 2022 are either closed or open.

After you exclude the payment:

- The revenue account clears to 0 USD because the payment doesn’t generate
revenue.
- The cash account remains at 10 USD, acknowledging the received payment.
- An amount of 10 USD is added to the exclusion account.

At the end of February, your summary might reflect the following:

AccountJanuaryFebruaryCash+10.00Revenue+10.00-10.00Exclusion+10.00
### Exclude unpaid transactions

This example uses the following assumptions:

- On January 1, 2022, at 00:00:00 UTC, a customer initiates a one-month
subscription (from January 1 to Jan 31) that costs 31 USD.
- The subscription generates an invoice.
- The invoice finalizes, but the customer doesn’t make a payment.
- On February 1, 2022, you exclude the payment.
- The accounting periods are open for January 2022.

If you exclude a finalized invoice during an open accounting period, it leaves
no trace of activity related to the invoice. Stripe removes all of the account
activities, excluding the cash and customer balance account that isn’t involved
in this case, and don’t generate journal entries from the finalization and
exclusion of the invoice.

## Links

- [corrections](https://docs.stripe.com/revenue-recognition/reports)