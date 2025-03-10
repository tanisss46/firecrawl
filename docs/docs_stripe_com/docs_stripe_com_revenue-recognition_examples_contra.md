# Contra examples

## Learn about revenue recognition with contra examples.

Unless stated otherwise, these contra examples assume that revenue recognition
takes place on a per-day basis.

## Customer credit balance

This example uses the following assumptions:

- On January 15, at 00:00:00 UTC, a customer starts a monthly subscription that
costs 31 USD.
- The subscription generates an invoice.
- The invoice finalizes on January 15, at 00:00:00 UTC.
- The customer has -11 USD in its customer credit balance. Stripe automatically
applies -11 USD to the invoice and adjusts the customer credit balance to 0 USD.
- The customer pays 20 USD on February 9.

In this example, the invoice and revenue periods are from 1/15/2019 to
2/14/2019. The 31 USD is recognized across 17 days in January and 14 days in
February. If you looked at the summary after January ends, you might see
something like:

AccountJanFebAccountsReceivable+20.00-20.00Cash+20.00CustomerBalance-11.00Revenue+17.00+14.00DeferredRevenue+14.00-14.00
In this scenario, the customer has an existing customer credit balance that’s
used to pay the invoice. It’s also possible for a negative amount on an invoice
to credit the customer credit balance, which is then used to pay the invoice.
This often happens when a customer downgrades to a cheaper subscription. For
example, assume that:

- A -31 USD invoice with one invoice line item finalizes on January 15, at
00:00:00 UTC.
- The service period for the -31 USD invoice line item is from January 15
00:00:00 UTC to February 15 00:00:00 UTC.
- Stripe automatically credits 31 USD to the customer credit balance and closes
the invoice.

The -31 USD line item books a journal entry that debits DeferredRevenue and
credits AccountsReceivable. When Stripe credits the customer credit balance, it
books another journal entry that debits AccountsReceivable and credits
CustomerBalance. In the summary at the end of January, you might see something
like:

AccountJanFebAccountsReceivableCashCustomerBalance+31.00Revenue-17.00-14.00DeferredRevenue-14.00+14.00
Notice that eventually the net revenue is -31 USD.

## Refund

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes and the customer pays 90 USD.
- On February 1, they receive a full refund.

When you make a full refund:

- The customer receives cash.
- Recognized revenue is offset by contra revenue in the refunds account.
- Deferred revenue from the subscription that hasn’t been recognized is cleared.

In this example, the customer received one month of service, so they receive a
31 USD refund. The refund also decreases the cash balance in your Stripe account
by 90 USD. At the time of the refund, there was 59 USD remaining in deferred
revenue, so this is also cleared. If you viewed the summary after March ends, it
might look something like this:

AccountJan 2019Feb 2019Mar
2019Revenue+31.00DeferredRevenue+59.00-59.00Cash+90.00-90.00Refunds+31.00
## Partial refund

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes and the customer pays 90 USD.
- On February 1, they receive a partial refund of 9 USD.

When the partial refund is made:

- The customer receives 9 USD.
- Recognized revenue is proportionally offset by contra revenue in the refunds
account.
- Deferred revenue from the subscription that hasn’t been recognized is also
proportionally reduced.

In this example, the customer received one month of service, so 31 USD has been
recognized. There is 59 USD remaining in deferred revenue. The partial refund of
9 USD is 10% of 90 USD. Therefore, the refunds account (part of contra revenue)
increased by 3.10 USD (10% of 31 USD), and deferred revenue decreased by 5.90
USD (10% of 59 USD). If you viewed the summary after March ends, it might look
something like this:

AccountJan 2019Feb 2019March
2019Revenue+31.00+25.20+27.90DeferredRevenue+59.00-31.10 (= -25.20 +
-5.90)-27.90Cash+90.00-9.00Refunds+3.10
## Void

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes, but the customer hasn’t paid yet.
- On February 1, you void the invoice.

When you void the invoice:

- The accounts receivable account is cleared because we don’t expect to get
paid.
- Recognized revenue is offset by contra revenue in the voids account.
- Deferred revenue from the subscription that hasn’t been recognized is cleared.

In this example, the customer received one month of service, so 31 USD in
recognized revenue is voided. At the time of the invoice being voided, there was
59 USD remaining in deferred revenue, so this is also cleared. If you viewed the
summary after March ends, it might look something like this:

AccountJan 2019Feb 2019Mar
2019AccountsReceivable+90.00-90.00Revenue+31.00DeferredRevenue+59.00-59.00Voids+31.00
## Uncollectible

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes, but the customer hasn’t paid yet.
- On February 1, the invoice is marked as uncollectible.

When the invoice is marked as uncollectible:

- The accounts receivable account is cleared because we don’t expect to get
paid.
- Recognized revenue is offset by contra revenue in the bad debt account.
- Deferred revenue from the subscription that hasn’t been recognized is cleared.

In this example, the customer received one month of service, so 31 USD in
recognized revenue becomes bad debt. At the time of the invoice being marked as
uncollectible, there was 59 USD remaining in deferred revenue, so this is also
cleared. If you viewed the summary after March ends, it might look something
like this:

AccountJan 2019Feb 2019Mar
2019AccountsReceivable+90.00-90.00Revenue+31.00DeferredRevenue+59.00-59.00BadDebt+31.00
An uncollectible invoice might still be paid. When the invoice is paid, the bad
debt account is cleared out using a part of the received cash amount. The
remaining cash amount goes to the recoverables account. If the invoice is paid
in April, the summary might look something like this:

AccountJan 2019Feb 2019Mar 2019Apr
2019AccountsReceivable+90.00-90.00Revenue+31.00DeferredRevenue+59.00-59.00BadDebt+31.00-31.00Cash+90.00Recoverables+59.00
An uncollectible invoice might still be voided. When the invoice is voided, the
bad debt account is cleared out and the contents are moved into the void
account. If the invoice is voided in April, the summary might look something
like this:

AccountJan 2019Feb 2019Mar 2019Apr
2019AccountsReceivable+90.00-90.00Revenue+31.00DeferredRevenue+59.00-59.00BadDebt+31.00-31.00Void+31.00
## Uncollectible invoice with applied customer credit balance

This example uses the following assumptions:

- On January 15 at 00:00:00 UTC, a customer starts a monthly subscription that
costs 31 USD.
- The subscription generates an invoice.
- The invoice finalizes on January 15 at 00:00:00 UTC.
- The customer’s credit balance is -11 USD. Stripe automatically applies -11 USD
to the invoice and adjusts the credit balance accordingly.
- On February 15, the invoice is marked as uncollectible.

In this example, the invoice and revenue periods are from January 15, 2019 to
February 14, 2019. Stripe recognizes the 31 USD across 17 days in January and 14
days in February.

Stripe automatically offsets recognized revenue with the bad debt account if an
invoice is set as uncollectible. With the customer’s 11 USD credit balance,
Stripe considers 6 USD (11 × 17 / 31) as recognized revenue and 5 USD (11 × 14 /
31) as deferred revenue. The portion of paid deferred revenue is considered as a
gain and booked in the recoverables account.

The summary after February end might look something like:

AccountStartingJanFebEndingAccountsReceivable0.00+20.00-20.000.00BadDebt0.00+11.0011.00CustomerBalance11.00-11.000.00Recoverables0.00+5.005.00Revenue0.00+17.0017.00DeferredRevenue0.00+14.00-14.000.00
As another example, you can increase the customer’s invoice due amount when
there’s an outstanding balance (that is, they owe some amount to you). Consider
the following:

- A 31 USD invoice with one invoice line item finalizes on January 15 at
00:00:00 UTC.
- The service period for the 31 USD invoice line item is from January 15
00:00:00 UTC to February 15 00:00:00 UTC.
- There is a customer credit balance of 10 USD. Because of this, Stripe adds
that amount to the invoice making the outstanding balance be 0 USD.- This debits
AccountsReceivable and credits CustomerBalance for 10 USD.
- Stripe marks the invoice as uncollectible on February 15.

For an uncollectible invoice, the portion of due customer credit balance isn’t
collected. Because of this, it’s considered a negative gain and booked as a
negative amount to the recoverables account.

The summary after February end might look something like:

AccountStartingJanFebEndingAccountsReceivable0.00+41.00-41.000.00BadDebt0.00+17.0017.00CustomerBalance-10.00+10.000.00Recoverables0.00-10.00-10.00Revenue0.00+17.0017.00DeferredRevenue0.00+14.00-14.000.00
## Uncollectible and disputed or refunded

An uncollectible invoice can be paid, then later disputed or refunded.

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes, but the customer hasn’t paid yet.
- On February 1, the invoice is marked as uncollectible.
- On April 1, the invoice is paid.
- On May 1, the corresponding charge is disputed.

As shown in the
[uncollectible](https://docs.stripe.com/revenue-recognition/examples/contra#uncollectible)
example, when the invoice is marked as uncollectible and later paid:

- The bad debt account is cleared out.
- The remainder is booked as recoverables.

In this example, the customer later decides to dispute the charge. When a
dispute occurs, the summary might look something like:

AccountJan 2019Feb 2019Mar 2019Apr 2019May
2019AccountsReceivable+90.00-90.00Revenue+31.00DeferredRevenue+59.00-59.00BadDebt+31.00-31.00Cash+90.00-90.00Disputes+31.00Recoverables+59.00-59.00
An invoice marked as uncollectible, paid, and later refunded works in a similar
manner except that it uses the refunds account instead of the disputes account.

## Dispute

In case of a dispute, Revenue Recognition works similarly to how a refund works
except that it uses the disputes account instead.

This example also shows what happens if you win a dispute. It uses the following
assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a three month subscription
that costs 90 USD.
- The subscription generates an invoice.
- The invoice finalizes and the customer pays 90 USD.
- On February 1, they dispute the payment.
- On April 1, you win the dispute because the bank rules in your favor.

When the customer makes the dispute:

- Cash is returned to the customer.
- Recognized revenue is offset by contra revenue in the disputes account.
- Deferred revenue from the subscription that hasn’t been recognized is cleared.

When you win the dispute:

- Cash is returned to you.
- Recognized revenue and deferred revenue don’t change.
- Cash is offset by an increase in the recoverables account.

In this example, the customer received one month of service, so 31 USD in
recognized revenue is disputed. The dispute also decreases the cash balance in
your Stripe account by 90 USD. At the time of the dispute, there was 59 USD
remaining in deferred revenue, so this is also cleared. Later in time, in April,
the bank rules in your favor, so the cash is returned to you.

If you viewed the summary after April ends, it might look something like this:

AccountJan 2019Feb 2019Mar 2019Apr
2019Revenue+31.00DeferredRevenue+59.00-59.00Cash+90.00-90.00+90.00Disputes+31.00Recoverables+90.00
## Other loss

This example is based on the following details:

- On January 1, at 00:00:00 UTC, a customer starts a 10 month subscription that
costs 100 USD.
- One month of revenue is recognized (10 USD).
- The invoice is paid.
- On February 1, an 80 USD refund happened, and a proportionate amount of
revenue was recognized.
- On March 1, an 80 USD dispute happened.

AccountJanFebMarCash+100.00-80.00-80.00Revenue+10.00+2.00DeferredRevenue+90.00-74.00-16.00Refund+8.00Dispute+4.00OtherLoss+60.00