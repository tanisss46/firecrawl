# Revenue Recognition settings examples

## Learn about revenue settings through examples.

## Amortization granularity

This example uses the following assumptions:

- On June 15th, 2024 at 12:00:00 PM UTC, a customer starts a 4-month
subscription that costs 120 USD.
- The subscription generates an [invoice](https://docs.stripe.com/api/invoices).
- The invoice finalizes and the customer pays 120 USD.

In this example, the invoice and revenue periods are from June 15, 2024 12:00:00
PM UTC to October 13, 2024 12:00:00 PM UTC. The 120 USD is recognized across
15.5 days in June, 31 days in July, 31 days in August, 30 days in September and
12.5 days in October. We can use this example to demonstrate the differences
between our supported amortization methods.

If you looked at the summary after October ends, amortization by millisecond
applied, you might see something like:

AccountJunJulAugSepOctRevenue+15.50+31.00+31.00+30.00+12.50DeferredRevenue+104.50-31.00-31.00-30.00-12.50
If you looked at the summary after October ends, amortization by day applied,
you might see something like:

AccountJunJulAugSepOctRevenue+16.00+31.00+31.00+30.00+12.00DeferredRevenue+104.00-31.00-31.00-30.00-12.00
If you looked at the summary after October ends, amortization by month evenly
applied, you might see something like:

AccountJunJulAugSepRevenue+30.00+30.00+30.00+30.00DeferredRevenue+90.00-30.00-30.00-30.00
If you looked at the summary after October ends, amortization by month evenly,
first and last month prorated applied, you might see something like:

AccountJunJulAugSepOctRevenue+15.50+30.66+30.66+30.68+12.50DeferredRevenue+104.50-30.66-30.66-30.68-12.50
## Catch-up revenue

This example uses the following assumptions:

- On November 1st, 2024, at 00:00:00 UTC, a customer is billed for an
[invoice](https://docs.stripe.com/api/invoices) that costs 92 USD.
- The invoice has service periods from Oct 1, 2024 to Jan 1, 2025 for all of its
line items.
- The invoice finalizes and the customer pays 92 USD.

In this example, the service period for the transaction begins prior to the
invoice finalization, triggering the catch-up revenue effect. We can use this
example to demonstrate the differences between enabling and disabling catch-up
revenue.

After December ends, with catch-up revenue enabled, the summary might look like:

AccountNovDecRevenue+61.00+31.00DeferredRevenue+31.00-31.00
After December ends, with catch-up revenue disabled, the summary might look
like:

AccountOctNovDecRevenue+31.00+30.00+31.00DeferredRevenue+31.00 (= +61.00 +
-30.00)-31.00UnbilledAccountsReceivable+31.00-31.00AccountsReceivable+92.00

## Links

- [invoice](https://docs.stripe.com/api/invoices)