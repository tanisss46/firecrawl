# Supported currencies

## See what currencies you can use for making charges and for paying out to your bank account.

You can charge customers in one of more than [135 native
currencies](https://docs.stripe.com/currencies#presentment-currencies) and
[receive funds in your
currency](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies).
Businesses that have a global presence find this helpful because charging in a
customer’s native currency can increase sales.

## Currency presentment and settlement

Currency affects three aspects of Stripe payments:

- The customer’s payment method currency, such as their credit card or bank
account
- The currency of the charge, called the *presentment* currency
- The currency accepted by your destination bank account or debit card, called
the *settlement* currency

If the charge currency differs from the customer’s payment method currency,
their bank or card issuer might charge the *customer* a foreign exchange fee.
The bank or card issuer might also charge the customer if the payment method and
your business are in different countries, regardless of the currency used.

If the charge currency differs from your settlement currency, Stripe [converts
the charge](https://docs.stripe.com/currencies/conversions) to your settlement
currency. Our [payouts](https://docs.stripe.com/payouts#multiple-bank-accounts)
documentation lists the different bank account currencies we support. See
[Stripe pricing](https://www.stripe.com/pricing) for conversion costs.

## Supported presentment currencies

AustraliaAustriaBelgiumBrazilBulgariaCanadaCroatiaCyprusCzech
RepublicDenmarkEstoniaFinlandFranceGermanyGibraltarGreeceHong
KongHungaryIndiaIrelandItalyJapanLatviaLiechtensteinLithuaniaLuxembourgMalaysiaMaltaMexicoNetherlandsNew
ZealandNorwayPolandPortugalRomaniaSingaporeSlovakiaSloveniaSpainSwedenSwitzerlandThailandUnited
Arab EmiratesUnited KingdomUnited States
Stripe users can process charges in the following list of currencies with these
exceptions:

- UnionPay cards can only be charged in USD and CAD
- Currencies marked with `*` are not supported by American Express
- These currencies apply to card payments: other payment methods are often tied
to a specific currency
- USD
- AED
- AFN*
- ALL
- AMD
- ANG
- AOA*
- ARS*
- AUD
- AWG
- AZN
- BAM
- BBD
- BDT
- BGN
- [BIF](https://docs.stripe.com/currencies#zero-decimal)
- BMD
- BND
- BOB*
- BRL*
- BSD
- BWP
- BYN
- BZD
- CAD
- CDF
- CHF
- [CLP](https://docs.stripe.com/currencies#zero-decimal)*
- CNY
- COP*
- CRC*
- CVE*
- CZK
- [DJF](https://docs.stripe.com/currencies#zero-decimal)*
- DKK
- DOP
- DZD
- EGP
- ETB
- EUR
- FJD
- FKP*
- GBP
- GEL
- GIP
- GMD
- [GNF](https://docs.stripe.com/currencies#zero-decimal)*
- GTQ*
- GYD
- HKD
- HNL*
- HTG
- HUF
- IDR
- ILS
- INR
- ISK
- JMD
- [JPY](https://docs.stripe.com/currencies#zero-decimal)
- KES
- KGS
- KHR
- [KMF](https://docs.stripe.com/currencies#zero-decimal)
- [KRW](https://docs.stripe.com/currencies#zero-decimal)
- KYD
- KZT
- LAK*
- LBP
- LKR
- LRD
- LSL
- MAD
- MDL
- [MGA](https://docs.stripe.com/currencies#zero-decimal)
- MKD
- MMK
- MNT
- MOP
- MUR*
- MVR
- MWK
- MXN
- MYR
- MZN
- NAD
- NGN
- NIO*
- NOK
- NPR
- NZD
- PAB*
- PEN*
- PGK
- PHP
- PKR
- PLN
- [PYG](https://docs.stripe.com/currencies#zero-decimal)*
- QAR
- RON
- RSD
- RUB
- [RWF](https://docs.stripe.com/currencies#zero-decimal)
- SAR
- SBD
- SCR
- SEK
- SGD
- SHP*
- SLE
- SOS
- SRD*
- STD*
- SZL
- THB
- TJS
- TOP
- TRY
- TTD
- TWD
- TZS
- UAH
- [UGX](https://docs.stripe.com/currencies#zero-decimal)
- UYU*
- UZS
- [VND](https://docs.stripe.com/currencies#zero-decimal)
- [VUV](https://docs.stripe.com/currencies#zero-decimal)
- WST
- [XAF](https://docs.stripe.com/currencies#zero-decimal)
- XCD
- [XOF](https://docs.stripe.com/currencies#zero-decimal)*
- [XPF](https://docs.stripe.com/currencies#zero-decimal)*
- YER
- ZAR
- ZMW

You must use all lowercase letters when passing the three-letter ISO code in any
payment request.

Currencies shown as links are
[zero-decimal](https://docs.stripe.com/currencies#zero-decimal) currencies.

## Minor units in API amounts

All API requests expect `amount` values in the [currency’s minor
unit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount).
For example, enter:

- `1000` to charge 10 USD (or any other two-decimal currency).
- `10` to charge 10 JPY (or any other zero-decimal currency).

### Zero-decimal currencies

For the following zero-decimal currencies, the charge and the amount are the
same, without requiring multiplication. For example, to charge 500 JPY, provide
an `amount` value of `500`.

- BIF
- CLP
- DJF
- GNF
- JPY
- KMF
- KRW
- MGA
- PYG
- RWF
- UGX
- VND
- VUV
- XAF
- XOF
- XPF

### Special cases

The following currencies have special conditions that you need to consider when
creating payouts or charges.

Currency DescriptionIcelandic Króna (ISK)ISK transitioned to a zero-decimal
currency, but backwards compatibility requires you to represent it as a
two-decimal value, where the decimal amount is always `00`. For example, to
charge 5 ISK, provide an `amount` value of `500`. You can’t charge fractions of
ISK.Hungarian Forint (HUF)Stripe treats HUF as a zero-decimal currency for
payouts, even though you can charge two-decimal amounts. When you create a
manual payout in HUF, you must provide integer amounts that are evenly divisible
by 100. For example, if you have an available balance of HUF 10.45, you can pay
out HUF 10 by submitting `1000` for the `amount` value. You can’t submit a
payout for the full balance, HUF 10.45, because the `amount` value of `1045`
isn’t evenly divisible by 100.New Taiwan Dollar (TWD)Stripe treats TWD as a
zero-decimal currency for payouts, even though you can charge two-decimal
amounts. When you create a manual payout in TWD, you must provide integer
amounts that are evenly divisible by 100. For example, if you have an available
balance of TWD 800.45, you can pay out TWD 800 by submitting `80000` for the
`amount` value. You can’t submit a payout for the full balance, TWD 800.45,
because the `amount` value of `80045` isn’t evenly divisible by 100.Ugandan
Shilling (UGX)UGX transitioned to a zero-decimal currency, but backwards
compatibility requires you to represent it as a two-decimal value, where the
decimal amount is always `00`. For example, to charge 5 UGX, provide an `amount`
value of `500`. You can’t charge fractions of UGX. For invoices where the
`amount` is fractional after prorations, coupons, or taxes, Stripe automatically
rounds that amount to the nearest number evenly divisible by 100. We credit or
debit any difference from rounding to the customer balance.
## Minimum and maximum charge amounts

Stripe enforces a minimum payment amount for all charges to make sure the Stripe
fee doesn’t exceed your charge. The minimum amount you can charge depends on the
payout [bank account settlement
currency](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies).

Subscription charges support zero-amount charges to account for coupons and free
trials. However, any non-zero amount is still subject to the applicable minimum.

Settlement CurrencyMinimum Charge AmountUSD$0.50AED2.00
د.إAUD$0.50BGNлв1.00BRLR$0.50CAD$0.50CHF0.50
FrCZK15.00KčDKK2.50-kr.EUR€0.50GBP£0.30HKD$4.00HUF175.00
FtINR₹0.50JPY¥50MXN$10MYRRM 2NOK3.00-kr.NZD$0.50PLN2.00
złRONlei2.00SEK3.00-kr.SGD$0.50THB฿10
If you only have one bank account, the minimum amount shown applies to all
charges in the same currency as the account. Charges requiring
[conversion](https://docs.stripe.com/currencies/conversions) into your account’s
[default settlement
currency](https://docs.stripe.com/payouts#multiple-bank-accounts) must meet the
equivalent minimum of the settlement currency. For example, if you have GBP and
USD bank accounts, with GBP set as your default currency, any non-USD charges
you create convert to GBP. These charges must meet the minimum amount required
for GBP (£0.30) after conversion.

Exceptions to the minimum charge amount apply to some payment methods, such as
[iDEAL](https://docs.stripe.com/payments/ideal) (allows `amount` values as low
as `1`).

In general, the number of allowed digits limits the maximum amount you can
charge a customer. The `amount` value supports up to:

- 12 digits for IDR, for a maximum charge of 9,999,999,999.99 IDR
(`999999999999`)
- 9 digits for INR, for a maximum charge of 9,999,999.99 INR (`999999999`)
- 8 digits for all other currencies, for a maximum charge of 999,999.99
(`99999999`)

When accepting card payments, these currencies support higher maximum amounts:

- 11 digits for LBP, for a maximum charge of 999,999,999,999 LBP
(`99999999999999`)
- 10 digits for COP, for a maximum charge of 9,999,999,999.9 COP
(`9999999999999`)
- 10 digits for HUF, for a maximum charge of 9,999,999,999 HUF (`9999999999999`)
- 10 digits for JPY, for a maximum charge of 9,999,999,999 JPY (`9999999999999`)

Card networks can impose charge amount limits that are more restrictive than
digit number.

## European credit cards

Some factors, like pricing, result in distinct treatment of credit cards from
Europe compared to credit cards from other regions. Stripe defines European
cards as cards issued in the following countries:

Country CodeCountryADAndorraATAustriaBEBelgiumBGBulgariaHRCroatiaCYCyprusCZCzech
RepublicDKDenmarkEEEstoniaFOFaroe
IslandsFIFinlandFRFranceDEGermanyGIGibraltarGRGreeceGLGreenlandGGGuernseyVAHoly
See (Vatican City State)HUHungaryISIcelandIEIrelandIMIsle of
ManILIsraelITItalyJEJerseyLVLatviaLILiechtensteinLTLithuaniaLULuxembourgMTMaltaMCMonacoNLNetherlandsNONorwayPLPolandPTPortugalRORomaniaPMSaint
Pierre and MiquelonSMSan
MarinoSKSlovakiaSISloveniaESSpainSESwedenTRTürkiyeGBUnited Kingdom
## See also

- [Creating Payments](https://docs.stripe.com/payments/payment-intents)
- [Getting Paid](https://docs.stripe.com/payouts)
- [Currency Conversions](https://docs.stripe.com/currencies/conversions)

## Links

- [payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support)
- [activate it](https://docs.stripe.com/get-started/account/activate#activation)
- [receive funds in your
currency](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies)
- [converts the charge](https://docs.stripe.com/currencies/conversions)
- [payouts](https://docs.stripe.com/payouts#multiple-bank-accounts)
- [Stripe pricing](https://www.stripe.com/pricing)
- [currency’s minor
unit](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [Creating Payments](https://docs.stripe.com/payments/payment-intents)
- [Getting Paid](https://docs.stripe.com/payouts)