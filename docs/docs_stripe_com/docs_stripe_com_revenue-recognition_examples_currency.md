# FX and currency examples

## Learn about revenue recognition with FX and currency examples.

Unless stated otherwise, these foreign exchange (FX) and currency examples
assume that revenue recognition takes place on a per-day basis.

## Multi-currency

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, an invoice finalizes and the customer
immediately pays 30 EUR.
- Your account’s settlement currency is USD.
- The EUR to USD exchange rate is 1.20 at the time of finalization and payment.

In this example, you receive 36 USD. Because the invoice finalizes and is paid
immediately, you have no exposure to fluctuating exchange rates and therefore no
foreign exchange (FX) gains or losses.

AccountJanRevenue+36.00Cash+36.00
## FX loss

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, an invoice finalizes for 30 EUR.
- On February 1, at 00:00:00 UTC, the customer pays the invoice for 30 EUR.
- Your account’s settlement currency is USD.
- The EUR to USD exchange rate is 1.20 at the time of finalization.
- The EUR to USD exchange rate is 1.10 at the time of payment.

In this example, the exchange rate changed between invoice finalization and
payment, so you receive 33 USD instead of 36.

AccountJanFebAccountsReceivable+36.00-36.00Revenue+36.00Cash+33.00FxLoss+3.00
## FX loss from a refund or dispute

This example uses the following assumptions:

- On January 1, at 00:00:00 UTC, an invoice finalizes for 30 EUR.
- On February 1, at 00:00:00 UTC, the customer pays the invoice for 30 EUR.
- On March 1, at 00:00:00 UTC, a refund is issued for 30 EUR.
- Your account’s settlement currency is USD.
- The EUR to USD exchange rate is 1.20 at the time of finalization.
- The EUR to USD exchange rate is 1.20 at the time of payment.
- The EUR to USD exchange rate is 1.30 at the time of refund.

In this example, the exchange rate changed between invoice payment and refund,
so you receive 36 USD but you later refund 39 USD. Therefore, you incur 3 USD
for FxLoss.

AccountJanFebMarAccountsReceivable+36.00-36.00Revenue+36.00Refunds+36.00Cash+36.00-39.00FxLoss+3.00
A dispute works in the same way as a refund, except that it books the disputes
account instead of the refunds account.

## Multiple settlement currencies

This example uses the following assumptions:

- Your account settles in USD by default but EUR is also a supported settlement
currency.
- On January 1, at 00:00:00 UTC, two invoices finalize for separate customers.
One is for 30 EUR, and the other is for 400 NOK.
- The NOK to USD conversion rate is 0.10 at the time of finalization and
payment.
- Both invoices are paid immediately.

In this example, you receive 40 USD from the NOK transaction and 30 EUR from the
EUR transaction. Because EUR is a supported settlement currency, no exchange
rate is applied.

AccountCurrencyJanRevenueUSD+40.00RevenueEUR+30.00CashUSD+40.00CashEUR+30.00