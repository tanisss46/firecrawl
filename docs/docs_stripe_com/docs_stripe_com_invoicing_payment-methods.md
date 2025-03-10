# Payment methods

## Learn about the supported payment methods for Invoicing.

By default, customers can pay [invoices](https://docs.stripe.com/api/invoices)
with any of the payment methods that you’ve enabled in your [Invoice
template](https://dashboard.stripe.com/settings/billing/invoice). In some
situations, there might be restrictions that prevent payment methods from being
used for an invoice. For instance, a payment method might only operate in one
currency or have limitations on the amount that can be paid. If there’s a
limitation on a payment method, Stripe won’t automatically select it for you.

## Supported payment methods

Stripe Invoicing supports the following payment methods:

Payment methodDescriptionCurrenciesBusiness locationLimitations[ACH Direct
Debit](https://docs.stripe.com/invoicing/ach-direct-debit)Accept debit payments
from customers with a US bank account using the Automated Clearing House (ACH)
payments system operated by Nacha.USDUnited
StatesNone[Affirm](https://docs.stripe.com/payments/affirm)Enable customers to
split their payments over time while your business gets paid up front.CAD,
USDCanada, United StatesYou can only add this payment method to individual
invoices. Invoices that use this payment method only support the `send_invoice`
[collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[Afterpay](https://docs.stripe.com/payments/afterpay-clearpay)
(Clearpay)Enable customers to split their payments over time while your business
gets paid up front.AUD, CAD, GBP, NZD, USDAustralia, Canada, New Zealand, United
Kingdom, United StatesYou can only add this payment method to individual
invoices. Invoices that use this payment method only support the `send_invoice`
[collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[Alipay](https://docs.stripe.com/payments/alipay)Allow
customers to pay on the web or a mobile device using login credentials or the
Alipay app.AUD, CAD, CNY, EUR, GBP, HKD, JPY, MYR, NZD, SGD, USDAustralia,
Canada, Europe, Hong Kong, Japan, New Zealand, Singapore, United
StatesNone[Bancontact](https://docs.stripe.com/payments/bancontact)Allow
customers to authorize payments on the Bancontact website or mobile app and then
return to your website for immediate notification about the success or failure
of the payment.EURAustralia, Canada, Europe, Hong Kong, Japan, Mexico, New
Zealand, Singapore, United StatesNone[Bank
transfer](https://docs.stripe.com/payments/bank-transfers)Receive bank transfers
directly from customers using [Payment
Intents](https://docs.stripe.com/payments/payment-intents).EUR, GBP, IDR, JPY,
MXN, USDEurope (SEPA), Indonesia, Japan, Mexico, United Kingdom, United
StatesYou can only add this payment method to individual invoices. Invoices that
use this payment method only support the `send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[Bacs
Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
Accept debit payments from customers with a UK bank account.GBPUnited
KingdomNone[BECS Direct
Debit](https://docs.stripe.com/payments/au-becs-debit)Accept debit payments from
customers with an Australian bank
account.AUDAustraliaNone[Boleto](https://docs.stripe.com/payments/boleto)Allow
customers to pay for services or goods at authorized agencies or banks, ATMs, or
online bank portals.BRLBrazilNone[Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay)Allow customers to make
single or recurring payments to businesses using their digital wallet. Customers
must authenticate their payment.USDUnited
StatesNone[Cards](https://docs.stripe.com/payments/cards/overview)Allow
customers to pay online using cards, which are linked to a debit or credit
account at a bank.Most currenciesMost
locationsNone[Crypto](https://docs.stripe.com/crypto/pay-with-crypto)Accept
stablecoin payments that settle as fiat in your Stripe balance.USDUnited
StatesInvoices that use this payment method only support the `send_invoice`
[collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[EPS](https://docs.stripe.com/payments/eps)Allow
customers to pay online using their Austrian bank credentials.EURAustralia,
Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesNone[Financial Process Exchange
(FPX)](https://docs.stripe.com/payments/fpx)Allow customers to pay online using
their Malaysian bank
credentials.MYRMalaysiaNone[iDEAL](https://docs.stripe.com/payments/ideal)Allow
customers to pay online using their Netherlands bank credentials.EURAustralia,
Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesNone[Klarna](https://docs.stripe.com/payments/klarna)Enable customers to
pay with flexible payment options, such as pay over time or pay now, while your
business gets paid up front.AUD, CAD, CHF, CZK, DKK, EUR, GBP, NOK, NZD, PLN,
RON, SEK, USDAustralia, Canada, most of Europe, New Zealand, United Kingdom,
United StatesYou can only add this payment method to individual invoices.
Invoices that use this payment method only support the `send_invoice`
[collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[Konbini](https://docs.stripe.com/payments/konbini)Allow
customers in Japan to pay for bills and online purchases at convenience stores
with cash.JPYJapanInvoices that use this payment method only support the
`send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[Link](https://docs.stripe.com/payments/link)Save
and autofill payment and shipping information for your customers so they don’t
need to enter payment details manually.Most currenciesMost
locationsNone[Multibanco](https://docs.stripe.com/payments/multibanco)Allow
customers to pay using a voucher through their online banking platform or at an
ATM.EUREurope, United Kingdom, United StatesInvoices that use this payment
method only support the `send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[PayNow](https://docs.stripe.com/payments/paynow)Allow
customers to pay using their preferred app from participating banks or non-bank
financial institutions.SGDSingaporeInvoices that use this payment method only
support the `send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[PayPal](https://docs.stripe.com/payments/paypal)Allow
customers to pay using their PayPal account. Customers are redirected to the
PayPal website to choose a funding source, such as their PayPal wallet, a linked
card or bank account, or buy-now-pay-later.AUD, CAD, CHF, CZK, DKK, EUR, GBP,
HKD, NOK, NZD, PLN, SEK, SGD, USDEurope, Switzerland, United
KingdomNone[Pre-authorized debit payments
(PADs)](https://docs.stripe.com/payments/acss-debit)Accept debit payments from
customers with a Canadian bank account using the Automated Clearing Settlement
System (ACSS).CAD, USDCanada, United
StatesNone[PromptPay](https://docs.stripe.com/payments/promptpay)Allow customers
to pay using their preferred app from participating banks.THBThailandInvoices
that use this payment method only support the `send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).[Przelewy24](https://docs.stripe.com/payments/p24)Allow
customers to pay online using bank transfers and other methods.EUR,
PLNAustralia, Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore,
United StatesNone[SEPA direct
debit](https://docs.stripe.com/payments/sepa-debit)Accept debit payments from
customers with an EUR-denominated bank account within the SEPA region.EURMost
locationsNone[WeChat Pay](https://docs.stripe.com/payments/wechat-pay)Allow
customers to use WeChat Pay to pay for goods and services inside of business
apps and websites.AUD, CAD, CHF (depending on business location), CNY, DKK, EUR,
GBP, HKD, JPY, NOK, SEK, SGD, USDAustralia, Canada, Europe, Hong Kong, Japan,
Singapore, United Kingdom, United StatesNone
* P.O. boxes don’t accept deliveries from other couriers, such as FedEx or UPS.

## Configure payment methods

You can use the Dashboard or API to add and configure payment methods.

DashboardAPI
To enable payment methods, you need to activate them in the [Invoice default
payment methods
configuration](https://dashboard.stripe.com/settings/billing/invoice).

### Overdue payments

An invoice is considered overdue when its due date has passed and the invoice
hasn’t been paid. By default, Stripe reminds your customer to pay the invoice
even after the due date. However, by modifying your [Automatic collection
settings](https://dashboard.stripe.com/settings/billing/automatic), you can
disable [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
on the invoice when it becomes past due.

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [Invoice template](https://dashboard.stripe.com/settings/billing/invoice)
- [ACH Direct Debit](https://docs.stripe.com/invoicing/ach-direct-debit)
- [Affirm](https://docs.stripe.com/payments/affirm)
- [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Afterpay](https://docs.stripe.com/payments/afterpay-clearpay)
- [Alipay](https://docs.stripe.com/payments/alipay)
- [Bancontact](https://docs.stripe.com/payments/bancontact)
- [Bank transfer](https://docs.stripe.com/payments/bank-transfers)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit)
- [Boleto](https://docs.stripe.com/payments/boleto)
- [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay)
- [Cards](https://docs.stripe.com/payments/cards/overview)
- [Crypto](https://docs.stripe.com/crypto/pay-with-crypto)
- [EPS](https://docs.stripe.com/payments/eps)
- [Financial Process Exchange (FPX)](https://docs.stripe.com/payments/fpx)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [Klarna](https://docs.stripe.com/payments/klarna)
- [Konbini](https://docs.stripe.com/payments/konbini)
- [Link](https://docs.stripe.com/payments/link)
- [Multibanco](https://docs.stripe.com/payments/multibanco)
- [PayNow](https://docs.stripe.com/payments/paynow)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Pre-authorized debit payments
(PADs)](https://docs.stripe.com/payments/acss-debit)
- [PromptPay](https://docs.stripe.com/payments/promptpay)
- [Przelewy24](https://docs.stripe.com/payments/p24)
- [SEPA direct debit](https://docs.stripe.com/payments/sepa-debit)
- [WeChat Pay](https://docs.stripe.com/payments/wechat-pay)
- [Automatic collection
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)