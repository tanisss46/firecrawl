# Work with multiple currencies

## Determine the presentment currency based on the charge type and the country of the Stripe account.

Stripe supports processing charges in [135+
currencies](https://docs.stripe.com/currencies). This allows you to present
prices in a customer’s native currency and avoid conversion costs for customers.
The currencies you can use are determined by the country of the Stripe account
where the charge is made.

Charge typeCurrency determined by[Direct
charges](https://docs.stripe.com/connect/direct-charges)Country of the connected
account[Destination
charges](https://docs.stripe.com/connect/destination-charges)Country of the
platform account[Destination
charges](https://docs.stripe.com/connect/destination-charges) using
`on_behalf_of`Country of the connected account[Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)Country
of the platform account[Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) using
`on_behalf_of` at charge timeCountry of the connected account
## Currency conversions

A currency conversion occurs if the *presentment* currency differs from the
*settlement* currency.

The presentment currency is the currency that’s used for charges. The settlement
currency is the currency that you can receive
[payouts](https://docs.stripe.com/payouts) in, depending on the charge type and
applicable currency conversion. See the [supported presentment
currencies](https://docs.stripe.com/currencies) and the [supported settlement
currencies](https://docs.stripe.com/connect/payouts-connected-accounts#supported-settlement).

Depending on bank account or debit card availability, the following occurs when
paying out a [balance](https://docs.stripe.com/connect/account-balances):

Bank account or debit card availabilityConversion actionAvailable for the
currencyNo conversionMultiple bank accounts or debit cards available for the
currencyNo conversion–Stripe uses the bank account or debit card set as
`default_for_currency`Not available for the currencyStripe converts the payout
balance based on the Stripe account’s default currency
If you regularly charge in multiple currencies, you might be able to establish
[multiple bank accounts](https://docs.stripe.com/payouts#multiple-bank-accounts)
to have multiple settlement currencies.

[Currency conversions](https://docs.stripe.com/currencies/conversions) use the
current exchange rates provided by our service providers, with an additional
conversion fee applied by Stripe. There are online resources for [conversion
calculation](https://dashboard.stripe.com/currency_conversion) that can help you
estimate current market rates. However, these numbers can fluctuate and might
not reflect Stripe’s rates at the time a payment is processed.

## Application fees for direct charges

Although direct charges are in the connected account’s default currency, your
platform receives the [application
fees](https://docs.stripe.com/api#application_fees) for [direct
charges](https://docs.stripe.com/connect/direct-charges) in your platform’s
default currency.

Bank account or debit card availabilityConversion actionAvailable for the
settlement currencyNo conversionNot available for the settlement currencyStripe
converts the application fee based on the platform account’s default currency
If your platform doesn’t use application fees and retains a portion of the
charges instead, those funds are paid out (and converted or not) the same way as
other charges on the platform account.

## Application fees for destination charges and converting balances

Application fees collected using the `application_fee_amount` parameter aren’t
converted again for [destination
charges](https://docs.stripe.com/connect/destination-charges); platforms always
receive application fees in the connected account’s settlement currency. Use the
`transfer_data[amount]` parameter to transfer less of the transaction amount and
collect fees in the platform’s default settlement currency.

If you create charges on the platform using the `destination` or `on_behalf_of`
parameters, you might accumulate balances in multiple currencies. If you don’t
have bank accounts for these other currencies, Stripe provides a way to pay out
balances in non-default currencies to your platform’s default bank account.

These currency conversions are created as manual payouts with `currency` set as
the currency of the source balance:

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=xaf
```

As long as there are sufficient funds in the balance for the specified currency,
Stripe automatically converts the funds to the default bank account’s currency.

## Example scenarios

The following examples illustrate how to work with multiple currencies in
[Connect](https://docs.stripe.com/connect):

### Direct charges

When the [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) is
different from the connected account’s default currency, Stripe converts [direct
charges](https://docs.stripe.com/connect/direct-charges) to the connected
account’s default currency. If the presentment currency is also different from
the platform’s default currency, the [application
fee](https://docs.stripe.com/connect/direct-charges#collect-fees) is converted
to the platform’s default currency.

For example, you accept a charge for a connected account in USD. Your platform
settles in USD and your connected account settles in EUR. The connected
account’s funds are converted to EUR and the application fee settles to your
platform in USD [without
conversion](https://docs.stripe.com/connect/currencies#application-fees-for-direct-charges).

### Destination charges without on_behalf_of

When processing [destination
charges](https://docs.stripe.com/connect/destination-charges) without
`on_behalf_of`, Stripe first converts them from the [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) to the
platform’s default currency. The funds sent to the connected account are then
converted to the connected account’s default currency.

- If an `application_fee_amount` is used, the [application
fee](https://docs.stripe.com/connect/destination-charges?fee-type=application-fee#collect-fees)
is collected after the conversion to the connected account’s default currency.
The fee remains in that currency when added to the platform.
- If `transfer_data[amount]` is used, the fee is collected after the first
currency conversion and remains in the platform’s default currency.

#### Note

This charge flow is subject to Stripe’s regional and [cross-border
policies](https://docs.stripe.com/connect/cross-border-payouts).

For example, you accept a destination charge for a connected account in EUR. The
connected account settles in GBP, and your platform settles in USD. The charge
is converted from EUR to USD and the funds sent to the connected account are
converted to GBP.

- If `application_fee_amount` is used, the application fee amount is converted
from EUR to GBP and taken from the amount that settles on the connected account.
- If `transfer_data[amount]` is used, the fee is retained in USD after
converting from the initial presentment currency.

### Destination charges with on_behalf_of

When processing [destination
charges](https://docs.stripe.com/connect/destination-charges) with
`on_behalf_of`, Stripe first converts them from the [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) to the
connected account’s default currency. The [application
fee](https://docs.stripe.com/connect/destination-charges?fee-type=application-fee#collect-fees)
remains in the connected account’s currency, regardless of whether
`application_fee_amount` or `transfer_data[amount]` is used.

For example, the connected account accepts a charge in USD but settles in EUR.
The charge is converted to EUR and sent to the connected account in EUR. The fee
is collected in EUR regardless of whether `application_fee_amount` or
`transfer_data[amount]` is used.

### Separate charges and transfers without on_behalf_of

[Separate
charges](https://docs.stripe.com/connect/separate-charges-and-transfers) are
converted to the platform’s default currency from the [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) and the
platform later transfers the funds to the connected account. The
`application_fee_amount` and `transfer_data[amount]` parameters are not used to
collect fees, since the platform can choose the appropriate amount to send at
transfer time.

#### Note

This charge flow is subject to Stripe’s regional and [cross-border
policies](https://docs.stripe.com/connect/cross-border-payouts).

### Separate charges and transfers with on_behalf_of

[Separate
charges](https://docs.stripe.com/connect/separate-charges-and-transfers) are
converted to the connected account’s default currency from the [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) and the
platform later transfers the funds to the connected account. The
`application_fee_amount` and `transfer_data[amount]` parameters are not used to
collect fees, since the platform can choose the appropriate amount to send at
transfer time.

#### Note

This charge flow is subject to Stripe’s regional and [cross-border
policies](https://docs.stripe.com/connect/cross-border-payouts).

## See also

- [Creating charges](https://docs.stripe.com/connect/charges)
- [Creating direct charges](https://docs.stripe.com/connect/direct-charges)
- [Using subscriptions](https://docs.stripe.com/connect/subscriptions)

## Links

- [135+ currencies](https://docs.stripe.com/currencies)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[on_behalf_of](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)
- [payouts](https://docs.stripe.com/payouts)
- [supported settlement
currencies](https://docs.stripe.com/connect/payouts-connected-accounts#supported-settlement)
- [balance](https://docs.stripe.com/connect/account-balances)
- [multiple bank
accounts](https://docs.stripe.com/payouts#multiple-bank-accounts)
- [Currency conversions](https://docs.stripe.com/currencies/conversions)
- [conversion calculation](https://dashboard.stripe.com/currency_conversion)
- [application fees](https://docs.stripe.com/api#application_fees)
- [Connect](https://docs.stripe.com/connect)
- [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies)
- [application fee](https://docs.stripe.com/connect/direct-charges#collect-fees)
- [application
fee](https://docs.stripe.com/connect/destination-charges?fee-type=application-fee#collect-fees)
- [cross-border policies](https://docs.stripe.com/connect/cross-border-payouts)
- [Creating charges](https://docs.stripe.com/connect/charges)
- [Using subscriptions](https://docs.stripe.com/connect/subscriptions)