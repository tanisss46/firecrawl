# Currency conversions

## Learn more about how Stripe handles currency conversions for you.

Stripe supports processing charges in [135+
currencies](https://docs.stripe.com/currencies), allowing you to present prices
in a customer’s native currency. This can improve sales and help customers avoid
conversion costs. To present prices in your customer’s currency, specify the
presentment currency when [creating a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create).

Payments automatically convert to your default settlement currency. Stripe uses
the exchange rate at the time of the charge to protect your earnings from rate
fluctuations between the payment and your anticipated payouts.

In certain countries, Stripe might support settlement in additional currencies.
If you need liquidity in additional currencies, you can enable settlement in
those currencies and add a bank account in the [payout settings of your
Dashboard](https://dashboard.stripe.com/account/payouts).

#### Adaptive Pricing

Payment Links and integrations using the [Checkout Sessions
API](https://docs.stripe.com/api/checkout/sessions) can automatically convert
this price to an international customer’s local currency based on their
location. Learn more about [Adaptive
Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing).

## Interested in localizing your prices to your buyers' currency?

Please provide your email address below and our team will contact you soon.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Calculate foreign exchange rates

When Stripe provides currency conversion services for transactions, Stripe
generally applies the mid-market rate based on pricing data sourced from
third-party service providers. Mid-market rate is the average between the buy
and the sell price of a currency. Currency conversion on Stripe is subject to
fees as detailed on [our pricing page](https://stripe.com/pricing).

In certain circumstances, Stripe might apply the rate at which we source the
currency owed to you. For example, this can happen if a new exchange rate is
mandated by a government or if there is a large discrepancy in rates between our
service providers. Stripe does so to mitigate exchange rate risk to you and to
Stripe. Rarely, Stripe may take other actions to mitigate risk. If we do so,
we’ll provide additional notice to you.

You can check the current rate for currency conversions on Stripe by using our
[estimation page](https://dashboard.stripe.com/currency_conversion). You can
also see the actual exchange rate applied in a transaction through the [Balance
Transactions
API](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-exchange_rate)
or in your [Dashboard](https://dashboard.stripe.com/test/payments). Note that
the estimation page shows the baseline exchange rate and excludes the Stripe
fees for currency conversion, which is incremental to this rate.

## Conversions on disputes and refunds

If a currency-converted payment is disputed or refunded, the amount you received
is converted back to the [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) at the
current exchange rate. Exchange rates fluctuate with the market, so the rate
used during the payment often differs from the rate used when a dispute or
refund occurs. The amount deducted from your merchant balance depends on the
current rate and this amount might be more or less than the original payment.
The customer is always refunded the exact amount they paid and in the currency
they paid in, regardless of any rate fluctuations.

For example, if your settlement currency is EUR and you process a 60 USD payment
at a rate of 0.88 EUR per 1 USD, the converted amount is 52.80 EUR (excluding
the Stripe fee). If the rate is 0.86 EUR per 1 USD at the time of refund, the
amount deducted from your account balance is only 51.60 EUR.

## Countries with foreign exchange control

Remittance to or from countries with foreign exchange control (including, but
not limited to, Brazil) is carried out exclusively through authorized channels,
pursuant to the legislation applicable in those countries.

## Additional settlement currencies

In some countries, additional currencies might be enabled for settlement. If you
have liquidity needs in additional currencies, you can enable or disable these
on the [payout settings of your
dashboard](https://dashboard.stripe.com/account/payouts). If there are multiple
bank accounts available for a given currency, Stripe uses the one set as
`default_for_currency` for settlement and payouts.

If you have accumulated a balance in a currency without an associated bank
account, a conversion occurs if you create a manual payout in that currency.

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=xaf
```

As long as there are sufficient funds in the balance for the specified currency,
Stripe automatically converts the funds to the default bank account’s currency.

#### Note

If you enable a currency as a settlement currency by mistake, you can pay out
funds in your default currency using a manual payout, then disable the
accidental settlement currency so you don’t continue to accrue funds in that
currency.

## Conversions on Stripe fees

If you incur a Stripe fee in a currency for which you don’t have a linked bank
account, we automatically convert that fee to your default settlement currency
at the time the fee is incurred before charging you. This conversion uses the
baseline exchange rate and does not incur any additional fees. For example, if
you’re a Stripe Billing user whose default currency is USD, you might incur the
0.5% variable fee when you present in a non-USD currency. If you have a
subscriber to whom you present in EUR for their monthly
[subscription](https://docs.stripe.com/billing/subscriptions/creating) of 100
EUR, we convert that 0.50 EUR Stripe Billing fee to USD at the baseline rate at
the time of the charge at no additional conversion cost to you.

## See also

- [Payouts](https://docs.stripe.com/payouts)
- [Multi-currency
settlement](https://docs.stripe.com/payouts/multicurrency-settlement)

## Links

- [Connect](https://docs.stripe.com/connect)
- [additional considerations](https://docs.stripe.com/connect/currencies)
- [135+ currencies](https://docs.stripe.com/currencies)
- [creating a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)
- [payout settings of your
Dashboard](https://dashboard.stripe.com/account/payouts)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)
- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)
- [privacy policy](https://stripe.com/privacy)
- [our pricing page](https://stripe.com/pricing)
- [estimation page](https://dashboard.stripe.com/currency_conversion)
- [Balance Transactions
API](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-exchange_rate)
- [Dashboard](https://dashboard.stripe.com/test/payments)
- [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Payouts](https://docs.stripe.com/payouts)
- [Multi-currency
settlement](https://docs.stripe.com/payouts/multicurrency-settlement)