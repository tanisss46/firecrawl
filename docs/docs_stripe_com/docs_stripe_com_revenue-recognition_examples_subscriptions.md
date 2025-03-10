# Subscription examples

## Learn about revenue recognition with subscription examples.

Unless stated otherwise, these subscription examples assume that revenue
recognition takes place on a per-day basis.

## Monthly subscription

This example uses the following assumptions:

- On January 15, at 00:00:00 UTC, a customer starts a monthly subscription that
costs 31 USD.
- The subscription generates an [invoice](https://docs.stripe.com/api/invoices).
- The invoice finalizes and the customer pays 31 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to
February 14, 2019. The 31 USD is recognized across 17 days in January and 14
days in February. If you looked at the summary after January ends, you might see
something like:

AccountJanRevenue+17.00DeferredRevenue+14.00
This means that recognized revenue increased by 17 USD for the days in January,
and deferred revenue increased by 14 USD for revenue you expect to recognize in
February.

## Annual subscription

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts an annual subscription that
costs 365 USD.
- The subscription generates an invoice.
- The invoice finalizes and the customer pays 365 USD.

In this example, the invoice and revenue periods are from January 1, 2019 to
December 31, 2019. The 365 USD is recognized daily throughout the year. If you
looked at the summary after March ends, you might see something like:

AccountJan 2019Feb 2019Mar
2019Revenue+31.00+28.00+31.00DeferredRevenue+334.00-28.00-31.00
## Monthly metered subscription

There are four types of
[aggregate_usage](https://docs.stripe.com/api/prices/create#create_price-recurring-aggregate_usage),
each of which has a different implication on how revenue is recognized.

### Sum

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly
[metered](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
subscription at 1 USD per unit, and with `aggregate_usage=sum`.
- On January 25, they use 15 units.
- On February 4, they use another 17 units.
- On February 14, the subscription generates an invoice of 32 USD.
- The invoice finalizes for 32 USD, but isn’t paid yet.

In this example, the invoice and revenue periods are from January 15, 2019 to
February 14, 2019. Although the invoice isn’t generated until February 14, the
15 USD from January 25 still has to be recognized when the usage was reported.
If you looked at the summary after January ends, you might see something like:

AccountJanRevenue+15.00UnbilledAccountsReceivable+15.00
If you looked at the summary after February ends and the invoice hasn’t been
paid yet, you might see something like:

AccountJanFebRevenue+15.00+17.00UnbilledAccountsReceivable+15.00-15.00AccountsReceivable+32.00
### Max

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly
[metered](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
subscription at 1 USD per unit, and with `aggregate_usage=max`.
- On January 25, they use 17 units.
- On February 4, they use another 15 units.
- On February 14, the subscription generates an invoice of 17 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to
February 14, 2019. If you looked at the summary after January ends, you might
see something like:

AccountJanRevenue+17.00UnbilledAccountsReceivable+17.00
If you looked at the summary after February ends and the invoice is yet to be
paid, you might see something like:

AccountJanFebRevenue+17.00UnbilledAccountsReceivable+17.00-17.00AccountsReceivable+17.00
The 15 units recorded on February 4 don’t impact revenue recognition because
they’re not the max usage record.

### Last during period

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly
[metered](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
subscription at 1 USD per unit, and with `aggregate_usage=last_during_period`.
- On January 25, they use 17 units.
- On January 27, they use 10 units.
- On February 4, they use another 15 units.
- On February 14, the subscription generates an invoice of 15 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to
February 14, 2019. If you looked at the summary after January ends, you might
see something like:

AccountJanRevenue+10.00UnbilledAccountsReceivable+10.00
The 17 units recorded on January 25 doesn’t have any impact on revenue
recognition because it’s not the last usage record during the period at the end
of Jan.

If you looked at the summary after February ends and the invoice hasn’t been
paid yet, you might see something like:

AccountJanFebRevenue+10.00+5.00 (-10.00 +
15.00)UnbilledAccountsReceivable+10.00-10.00AccountsReceivable+15.00
The 17 units recorded on January 25 and 10 units recorded on January 27 don’t
have any impact on revenue recognition because they aren’t the last usage during
the period.

### Last ever

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly
[metered](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
subscription at 1 USD per unit, and with `aggregate_usage=last_ever`.
- On January 25, they use 17 units.
- On January 27, they use 10 units.
- On February 4, they use another 15 units.
- On February 8, they use another 18 units.
- On February 14, the subscription generates an invoice of 18 USD.
- On March 14, the subscription generates another invoice of 18 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to
February 14, 2019. If you looked at the summary after January ends, you might
see something like:

AccountJanRevenue+10.00UnbilledAccountsReceivable+10.00
The 10 units recorded on January 25 doesn’t have any impact on revenue
recognition because it’s not the last usage record at the end of Jan.

If you looked at the summary after February ends, you might see something like:

AccountJanFebRevenue+10.00+8.00 (-10.00 +
18.00)UnbilledAccountsReceivable+10.00-10.00AccountsReceivable+18.00
Now in the period of February 14 to March 14, because there’s no usage record
within the period, we recognize 18 USD when the invoice happens. If you looked
at the summary after March ends, you might see something like:

AccountJanFebMarRevenue+10.00+8.00 (-10.00 +
18.00)+18.00UnbilledAccountsReceivable+10.00-10.00AccountsReceivable+18.00+18.00
## Upgrade

This example uses the following assumptions:

- On April 1, at 00:00 UTC, a customer starts a monthly subscription that costs
90 USD.
- The subscription generates an invoice.
- The invoice finalizes on April 1 and the customer pays 90 USD.
- On April 21 at 00:00 UTC, they upgrade to a monthly subscription that costs
120 USD.- Two unbilled invoice items are created to represent (1) -30 USD for
the unused time of the previous plan and (2) 40 USD for the remaining time of
the new plan.
- The next invoice includes the two unbilled invoice items and is finalized on
May 1, at 00:00:00 UTC with 3 line items:- -30 USD for the unused time of the
previous plan with the service period from April 21 at 00:00 UTC to May 1 at
00:00 UTC.
- 40 USD for the remaining time of the new plan with the service period from
April 21 at 00:00 UTC to May 1 at 00:00 UTC.
- 120 USD for the service in May with the service period from May 1 at 00:00 UTC
to June 1 at 00:00 UTC.

If you looked at the summary after May ends, you might see something like:

AccountAprMayRevenue+100.00+120.00AccountsReceivable+90.00+130.00UnbilledAccountsReceivable+10.00-10.00
## Downgrade

This example uses the following assumptions:

- On April 1, at 00:00 UTC, a customer starts a monthly subscription that costs
90 USD.
- The subscription generates an invoice.
- The invoice finalizes on April 1 and the customer pays 90 USD.
- On April 21 at 00:00 UTC, they downgrade to a monthly subscription that costs
30 USD.- Two unbilled invoice items are created to represent (1) -30 USD for the
unused time of the previous plan and (2) 10 USD for the remaining time of the
new plan.
- The next invoice includes the two unbilled invoice items and is finalized on
May 1, at 00:00:00 UTC with 3 line items:- -30 USD for the unused time of the
previous plan with the service period from April 21 at 00:00 UTC to May 1 at
00:00 UTC.
- 10 USD for the remaining time of the new plan with the service period from
April 21 at 00:00 UTC to May 1 at 00:00 UTC.
- 30 USD for the service in May with the service period from May 1 at 00:00 UTC
to June 1 at 00:00 UTC.

If you looked at the summary after May ends, you might see something like:

AccountAprMayRevenue+70.00+30.00AccountsReceivable+90.00+10.00UnbilledAccountsReceivable-20.00+20.00

## Links

- [invoice](https://docs.stripe.com/api/invoices)
-
[aggregate_usage](https://docs.stripe.com/api/prices/create#create_price-recurring-aggregate_usage)
-
[metered](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)