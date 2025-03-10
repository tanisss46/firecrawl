# Treasury fees reportPublic preview

## Analyze Treasury fees at an itemized level.

Use Treasury fee reports to understand Stripe’s approach to the calculation,
application, and reporting of fees. You can create and download detailed reports
in the Dashboard.

## How Stripe assesses Treasury fees

### Administrative Facilitation Fee

Stripe pays Treasury users the Administrative Facilitation Fee (“AFF”) on a
monthly basis. We compound the fee on a daily basis and use the minimum
available balance across all your Treasury financial accounts for that
particular day. Financial Accounts with a negative balance don’t accrue any
fees. The balance is multiplied by: the 50th percentile Effective Federal Funds
Rate (EFFR) published for that day by the [Federal Bank of New
York](https://www.newyorkfed.org/markets/reference-rates/effr) and your
negotiated Administrative Facilitation Fee Rate Multiplier. For non-business
days, we use the previous business day’s EFFR value.

This methodology is as described in the latest Stripe Treasury standardized fee
schedule. Your actual methodology might differ based on your negotiated terms
with Stripe.

View an example calculation below.

DayEOD Available BalanceEFFRRate MultiplierCalculationDaily Yield for one
FA120,000 USD4.3392%20000 * (0.0433 * .92)/360 * .51.11 USD222,000
USD3.892%22000 * (0.038 * .92)/360 * .51.07 USD315,000 USD3.892%22000 * (0.038 *
.92)/360 * .50.73 USD
The total yield for the 3 days is 1.11 + 1.07 + 0.73 = 2.91 USD.

## Available columns

You can customize the columns that appear in the reports when you download them
in the Dashboard. The available columns in each type of report are described
below.

- [Treasury Administrative Facilitation
Fee](https://docs.stripe.com/reports/treasury-fees-reporting#schema-treasury-fees-administrative-facilitation-fee)

### Treasury Administrative Facilitation Fee

API report type: `treasury_fees.administrative_facilitation_fee`

Column nameDefaultDescriptionbalance_amount
The single multi-currency balance of the FinancialAccount. Positive values
represent money that belongs to the user while negative values represent funds
the user owes.

balance_currency
Designated currency of financial accounts balance. Currently, FinancialAccounts
can only carry balances in USD.

date
Date associated with Administrative Facilitation Fee earned…

effr_value
Effective federal funds rate value (50th percentile) used to calculate fee.
Gathered from the [NY
FED](https://www.newyorkfed.org/markets/reference-rates/effr).

fee
Amount of Administrative Facilitation fee paid out in user’s currency.

financial_account
Unique identifier of financial account for which Administrative Facilitation Fee
was incurred.

merchant
Unique identifier of financial account associated with.

## Links

- [Federal Bank of New
York](https://www.newyorkfed.org/markets/reference-rates/effr)