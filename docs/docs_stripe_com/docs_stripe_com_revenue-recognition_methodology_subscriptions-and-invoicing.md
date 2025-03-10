# Revenue Recognition with subscriptions and invoicing

## Learn how Revenue Recognition works with subscriptions and invoices.

Because of the detailed information available on subscriptions and
[invoices](https://docs.stripe.com/api/invoices), Revenue Recognition can
accurately defer and recognize revenue for these resources. Revenue Recognition
treats each invoice line item and subscription item as its own performance
obligation.

Revenue Recognition amortizes revenue by the millisecond, but our example uses a
daily interval.

## Licensed subscriptions

Licensed subscriptions are subscriptions that generate invoices for a service
offered in an upcoming subscription interval. At the end of the interval, the
subscription cycles and generates a new invoice for the next interval.

Each subscription item corresponds to a single line item on the invoice, and
automatically populates the period for that line item with the period start and
end for the subscription item.

Let’s take a look at an example and timeline for a simple monthly subscription.

- On January 15, a customer starts a monthly subscription that costs 31 USD,
which generates an invoice that gets finalized.

In this case, the period of service is from January 15 to February 14. The 31
USD is therefore recognized over 17 days in January and 14 days in February. If
you inspected the account balances at the end of January, you’d see that 17 USD
of revenue was recognized, and 14 USD of revenue remains deferred (to be
recognized in February).

AccountJanRevenue+17.00DeferredRevenue+14.00
## Metered subscriptions

While licensed subscriptions items bill in advance, metered subscription items
bill in arrears—at the point of invoice, all service has already been provided
and all revenue recognized.

Metered subscriptions allow businesses to submit usage information as service is
provided, prior to generating an invoice. Because service is provided, the
revenue must be recognized prior to the point of invoice.

This example introduces the concept of unbilled accounts receivable, which
represents the amount of cash a business can expect to receive based on the
service that they’ve already provided, but not yet invoiced.

This next example is for a metered subscription item where usage is submitted
over time.

- On January 15, a customer subscribes to a monthly metered subscription at 1
USD per unit, and with `aggregate_usage=sum`.
- On January 25th, they use 15 units.
- On February 4th, they use another 17 units.
- On February 14th, the subscription generates an invoice of 32 USD.
- The invoice is finalized for 32 USD, but isn’t paid yet.

In this case, the period of service is from January 15 to February 14, but you
don’t generate an invoice until February 14. However, the revenue from the 15
units of usage still needs to be recognized in January, for an amount of 15 USD.
If you inspected the account balances at the end of January, you’d see that 15
USD of revenue was recognized, but instead of debiting accounts receivable,
unbilled accounts receivable was debited.

AccountJanRevenue+15.00UnbilledAccountsReceivable+15.00
If you later inspected the account balances at the end of February, you’d
observe the following:

AccountJanFebRevenue+15.00+17.00UnbilledAccountsReceivable+15.00-15.00AccountsReceivable+32.00
## Upgrades and downgrades

Subscriptions can be upgraded and downgraded mid-month, and revenue needs to be
recognized accordingly. If an invoice is cut mid-month to handle the prorated
charges, the revenue schedule is also adjusted accordingly.

This next example is for a subscription that’s upgraded mid-month.

- On April 1, a customer starts a monthly subscription for 90 USD, which
generates and finalizes an invoice.
- On April 21, the customer upgrades the subscription to cost 120 USD instead,
which generates an invoice that accounts for the remaining 10 days of the month.

In this example, the customer receives 20 days of service with the 90 USD
monthly subscription (60 USD in value) and 10 days of service with the 120 USD
monthly subscription (40 USD in value). Therefore, in April, the recognized
revenue is 100 USD.

## Standalone invoices

The algorithm for recognizing revenue for standalone invoices is the same as
that of a licensed subscription—the main difference is that line item periods
aren’t automatically populated.

To recognize revenue correctly, remember to set the period for each invoice line
item. If you don’t set a period on an invoice line item, the amount on that
invoice line item is recognized immediately when the invoice finalizes. If you
need to override or add a new service period, use the [Data Import
feature](https://docs.stripe.com/revenue-recognition/data-import) to configure
your invoice data, or set
[rules](https://docs.stripe.com/revenue-recognition/rules) to customize revenue
treatments on different invoices.

In this example, an invoice has two line items, one with a period set, and one
without.

- On January 15, you create an invoice and finalize it with- A line item for 31
USD with a period from January 15 to February 14.
- A line item for 5 USD with no period set.

In this case, the invoice is for a total of 36 USD. The 31 USD is recognized
over 17 days in January and 14 days in February, but the 5 USD is immediately
recognized on January 15. If you inspected the account balances at the end of
January, you’d see that 22 USD (17 + 5) of revenue was recognized, and 14 USD of
revenue remains deferred (to be recognized in February).

AccountJanRevenue+22.00DeferredRevenue+14.00
## Uncollectible invoices

When an invoice is marked as uncollectible, we clear the accounts receivable
account since we no longer expect payment.

Parts of the revenue for the invoice might have already been recognized. Upon
marking it uncollectible, the recognized revenue is offset by contra revenue in
the bad debt account.

Parts of the revenue for the invoice might still be deferred. Upon marking it
uncollectible, the remaining deferred revenue is cleared.

In this example the invoice for a subscription finalizes and is later marked
uncollectible.

- On January 15, a customer starts a monthly subscription for 31 USD. The
invoice for 31 USD gets created and finalized.
- On February 1, the invoice is marked as uncollectible.

In this case, the customer received 17 days of service, but didn’t pay. The 17
USD that’s recognized at that point would be considered bad debt. The 14 USD in
deferred revenue for a service that has yet to be provided is zeroed out. If you
inspected the account balances on February 1, you’d see the following:

AccountJanFebAccountsReceivable+31.00-31.00Revenue+17.00DeferredRevenue+14.00-14.00BadDebt+17.00
An uncollectible invoice might still be paid. When the invoice is paid, the bad
debt account is cleared out using a part of the received cash amount. The
remaining cash amount goes to the recoverables account.

## Voided invoices

When you void an invoice, the invoice has reached a terminal state. We therefore
clear the accounts receivable account since the invoice can no longer be paid.

You might have already recognized parts of the revenue for the invoice. Upon
voiding, the recognized revenue is offset by contra revenue in the voids
account.

Parts of the revenue for the invoice might still be deferred. Upon voiding, the
remaining deferred revenue is cleared.

In this example, the invoice for a subscription is finalized and later voided.

- On January 15, a customer starts a monthly subscription for 31 USD. The
invoice for 31 USD gets created and finalized.
- On February 1, the invoice is voided.

In this case, the customer received 17 days of service, but didn’t pay. The 17
USD that’s recognized at that point would be voided. The 14 USD in deferred
revenue for service that has yet to be provided, is zeroed out. If you inspected
the account balances on February 1, you’d see the following:

AccountJanFebAccountsReceivable+31.00-31.00Revenue+17.00DeferredRevenue+14.00-14.00Voids+17.00
## Credit notes

Credit notes allow the amount due on an invoice to be reduced after it
finalizes. Since the expected payment is reduced, accounts receivable are
reduced by the amount of the credit note.

If the credit note has no line items, the credit note is divided proportionally
among all line items, based on the line item amounts. If the credit note has a
specified line items, the credit note only applies to that line item.

You might’ve already recognized parts of the revenue for the invoice. When a
credit note is issued, recognized revenue is proportionally offset by contra
revenue in the credit notes account, based on the proportion of revenue that you
recognized.

Parts of the revenue for the invoice might still be deferred. When a credit note
is issued, deferred revenue is reduced, based on the proportion of revenue
that’s still deferred.

In this example, the invoice for a subscription finalizes and a credit note is
issued later.

- On January 1, a customer starts a three month subscription for 90 USD. The
invoice for 90 USD gets created and finalized.
- On February 1, a credit note of 45 USD is issued.

At the end of March, the account balances would resemble the following:

AccountJanFebMarAccountsReceivable+90.00-45.00Revenue+31.00+14.00+15.50DeferredRevenue+59.00-43.50-15.50CreditNotes+15.50
## Tax liability

To accurately handle your tax liability on invoices and subscriptions, use the
`default_tax_rates` and `tax_rates` attribute on those resources to assign tax
rates. If tax is modeled as a regular item, Revenue Recognition doesn’t
automatically differentiate between revenue and tax unless you configure a
[custom rule](https://docs.stripe.com/revenue-recognition/rules).

It’s worth noting that taxes aren’t recognizable as revenue. For example, an
invoice for 50 USD with an exclusive tax of 5 USD has 50 USD in recognizable
revenue and 5 USD of tax liability. The invoice and accounts receivable totals
are both 55 USD.

In this example the invoice has an exclusive tax rate.

- On January 1, a customer starts a monthly subscription for 31 USD with an
exclusive tax rate of 10%. The total due amount on the generated invoice is
34.10 USD.
- The invoice is paid immediately.
AccountJanRevenue+31.00Cash+34.10TaxLiability+3.10
Similarly, let’s take a look at an example for an invoice with an inclusive tax
rate.

- On January 1, a customer starts a monthly subscription for 31 USD with an
inclusive tax rate of 10%. The total due amount on the generated invoice is 31
USD.
- The invoice is paid immediately.
AccountJanRevenue+27.90Cash+31.00TaxLiability+3.10
## Customer credit balance

The customer credit balance is a balance on a customer that gets applied to
future invoices automatically. Because the customer credit balance is treated as
an additional payment (rather than a discount, for example), applying it to an
invoice doesn’t reduce the tax liability for that invoice.

Handling the customer credit balance involves what we call the customer balance
account, which tracks the interactions between customer credit balance and
invoices.

In this example, an invoice is created for a customer that maintains a customer
credit balance.

- On January 15, an invoice for 31 USD is created and finalized. None of the
line items have a service period, so revenue is immediately recognized.
- The customer has -11 USD in their customer credit balance. Stripe
automatically applies -11 USD to the invoice and adjusts the customer credit
balance to 0 USD.
- The customer pays 20 USD.

In this case, the resulting account balances would look like

AccountJanCash+20.00Revenue+31.00CustomerBalance-11.00

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [Data Import feature](https://docs.stripe.com/revenue-recognition/data-import)
- [rules](https://docs.stripe.com/revenue-recognition/rules)