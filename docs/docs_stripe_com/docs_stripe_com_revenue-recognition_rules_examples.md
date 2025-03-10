# Rules examples

## Learn how to use rules through examples.

## Tax treatment

To categorize a tax line item (for example, created by Avalara), you can set one
rule like the one in this example:

ComponentsValueApply toInvoices > Line item description contains all of the
following: AvaTaxEffective periodStart: All past dates - End:
IndefiniteTreatmentsTax (100%)
If you have a 10 USD [invoice](https://docs.stripe.com/api/invoices) line item
with the description “Sales Tax calculated by AvaTax," and the invoice finalizes
in April, you’d see the account balances as in the following example:

AccountAprilAccountsReceivable10 USDTaxLiability10 USD
## Passthrough fees

To categorize 10% of an amount as a passthrough fee, you can set one rule like
the following example:

ComponentsValueApply toInvoices > All line itemsEffective periodStart: All past
dates—End: IndefiniteTreatmentsAmortization over line item service period (90%)
and Passthrough fee (10%)
If you have a 100 USD invoice line item (without a service period) that
finalizes in April, you’d see the account balances like the following example:

AccountAprilAccountsReceivable100 USDRevenue90 USDPassthroughFees10 USD
## Exclude transactions from a test customer

To exclude all the standalone payments from a test customer, you can set one
rule like the following example:

ComponentsValue
Apply to

Customers > Customer email contains all of the following: test@stripe.com

Other payments > All other payments

Effective periodStart: All past dates—End: IndefiniteTreatmentsExclude revenue
(100%)
Other payments from the customer, whose email is test@stripe.com, would be
excluded from the report completely.

## Exclude standalone payments

To exclude all standalone payments from the report, set a rule like the
following:

ComponentsValueApply toOther payments > All other paymentsEffective periodStart:
All past dates—End: IndefiniteTreatmentsExclude revenue (100%)
This rule restricts Revenue Recognition to only include recurring payments and
one-time invoice payments in your revenue accounting reports. Standalone
payments are excluded from the report.

## Amortize revenue over custom time period

In this example, we want to (1) amortize other payments from a small set of
customers (for example, `cus_AAA` and `cus_BBB`) over one year and (2) amortize
the remaining other payments over one month.

We can make two rules and use the order of the rules as shown in the following
example:

**Rule 1:** Amortize other payments over one year

ComponentsValue
Apply to

Customers > Customer ID matches any of the following: cus_AAA, cus_BBB

Other payments > All other payments

Effective periodStart: All past dates - End: IndefiniteTreatmentsAmortization
over custom service period (100%) > Amortization starting 0 days from paid time
over 1 year
**Rule 2:** Amortize other payments over one month

ComponentsValueApply toOther payments > All other paymentsEffective periodStart:
All past dates - End: IndefiniteTreatmentsAmortization over custom service
period (100%) > Amortization starting 0 days from paid time over 1 month
Other payments from `cus_AAA` or `cus_BBB` would match Rule 1, and the revenue
would be amortized over one year. Other payments from any other customer would
match Rule 2, and the revenue would be amortized over one month.

## Links

- [invoice](https://docs.stripe.com/api/invoices)