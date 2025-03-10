# Payment method support

## Learn how your integration choices affect payment method support.

Payment methods support certain currencies, countries, products, and API
options. Make sure your chosen payment methods work for your scenario before
choosing an [integration
option](https://docs.stripe.com/payments/payment-methods/integration-options) by
viewing these tables:

- [Country and currency
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support)
- [Product
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
- [API
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)

All payment methods have specific requirements for their use and might contain
additional restrictions that you must comply with, such as marketing guidelines,
additional prohibited and restricted businesses, and information about handling
disputes and refunds. These usage requirements and restrictions are described in
the [documentation](https://docs.stripe.com/payments/payment-methods/overview)
for that payment method or in the applicable [payment
terms](https://stripe.com/payment-terms/legal).

### Troubleshoot a payment method

If a customer doesn’t see a specific payment method, use the [Payment Methods
review](https://dashboard.stripe.com/settings/payment_methods/review) Dashboard
page to troubleshoot the issue using an existing PaymentIntent ID or custom
field.

## Country and currency support

Refer to the following table to see where each [payment
method](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
is supported and what presentment currencies it accepts. This table contains all
of the supported currencies and countries for a given payment method. In some
cases, not all of the countries listed can accept payments in all of the listed
presentment currencies. For more details on exactly what currencies are
accepted, see the individual payment method’s page.

#### Connected accounts

If you have a platform or marketplace integration that uses Connect, your
connected accounts might have different eligibility requirements than your
account. To learn about connected account eligibility and capabilities, see
[Adding payment method
capabilities](https://docs.stripe.com/connect/payment-methods).

Payment methodCurrenciesBusiness locationCustomer country[ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit)USDUnited Kingdom,
United StatesUnited
States[Alma](https://docs.stripe.com/payments/alma)EURFranceFrance[Amazon
Pay](https://docs.stripe.com/payments/amazon-pay)USDUnited StatesWorldwide[Apple
Pay](https://docs.stripe.com/apple-pay)Most currencies[Apple-supported
locations](https://support.apple.com/en-us/HT204916)[Apple-supported
locations](https://support.apple.com/en-us/HT204916)[Bacs Direct
Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment)GBPUnited
KingdomUnited Kingdom[BECS direct
debit](https://docs.stripe.com/payments/au-becs-debit)AUDAustraliaAustralia[Pre-authorized
debit in Canada](https://docs.stripe.com/payments/acss-debit)CAD, USDCanada,
United StatesCanada[SEPA
debit](https://docs.stripe.com/payments/sepa-debit)EURAustralia, Canada,
European Union, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesEurope[Bancontact](https://docs.stripe.com/payments/bancontact)EURAustralia,
Canada, European Union, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesBelgium[Bank
transfers](https://docs.stripe.com/payments/bank-transfers)EUR, GBP, JPY, MXN,
USDEuropean Union, Japan, Mexico, United Kingdom, United StatesEuropean Union,
Japan, Mexico, United Kingdom, United
States[BLIK](https://docs.stripe.com/payments/blik)PLNAustria, Belgium,
Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France,
Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein,
Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania,
Slovakia, Slovenia, Spain,
SwedenPoland[EPS](https://docs.stripe.com/payments/eps)EURAustralia, Austria,
Canada, European Union, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesAustria[FPX](https://docs.stripe.com/payments/fpx)MYRMalaysiaMalaysia[Google
Pay](https://docs.stripe.com/google-pay)Most currencies[Google-supported
locations](https://support.google.com/googlepay/answer/12429287?hl=en#zippy=)[Google-supported
locations](https://support.google.com/googlepay/answer/12429287?hl=en#zippy=)[iDEAL](https://docs.stripe.com/payments/ideal)EURAustralia,
Canada, European Union, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesNetherlands[P24](https://docs.stripe.com/payments/p24)EUR, PLNAustralia,
Canada, European Union, Hong Kong, Japan, Mexico, New Zealand, Singapore, United
StatesPoland[Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)GBPUnited
KingdomUnited Kingdom[PayPal](https://docs.stripe.com/payments/paypal)AUD, CAD,
CHF, CZK, DKK, EUR, GBP, HKD, NOK, NZD, PLN, SEK, SGD, USDAustria, Belgium,
Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France,
Germany, Greece, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg,
Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia,
Spain, Sweden, Switzerland, United
KingdomWorldwide[Affirm](https://docs.stripe.com/payments/affirm)CAD, USDCanada,
United StatesCanada, United States[Afterpay
(Clearpay)](https://docs.stripe.com/payments/afterpay-clearpay)AUD, CAD, EUR,
NZD, GBP, USDAustralia, Canada, New Zealand, United Kingdom, United
StatesAustralia, Canada, New Zealand, United Kingdom, United
States[Klarna](https://docs.stripe.com/payments/klarna)AUD, CAD, CHF, CZK, DKK,
EUR, GBP, NOK, NZD, PLN, RON, SEK, USDAustralia, Austria, Belgium, Canada,
Croatia, Cyprus, Denmark, Estonia, Finland, France, Germany, Greece, Ireland,
Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, New Zealand, Norway,
Poland, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom,
United StatesAustralia, Austria, Belgium, Canada, Finland, France, Germany,
Switzerland[Cards](https://docs.stripe.com/payments/cards/overview)Most
currenciesMost locationsMost
locations[Link](https://docs.stripe.com/payments/link)Most currenciesAustralia,
Austria, Belgium, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark,
Estonia, Finland, France, Germany, Gibraltar, Greece, Hong Kong, Hungary,
Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malaysia,
Malta, Mexico, Netherlands, New Zealand, Norway, Poland, Portugal, Romania,
Singapore, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Arab Emirates,
United Kingdom, United StatesMost locations[MB
WAY](https://docs.stripe.com/payments/mb-way)EURAustralia, Austria, Belgium,
Bulgaria, Canada, Croatia, Cyprus, Czech Republic,Denmark, Estonia, Finland,
France, Germany, Gibraltar, Greece, Hong Kong, Hungary, Ireland, Italy, Japan,
Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Mexico, Netherlands, New
Zealand, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia,
Spain, Sweden, Switzerland, United Kingdom, United
StatesPortugal[PayNow](https://docs.stripe.com/payments/paynow)SGDSingaporeSingapore[PromptPay](https://docs.stripe.com/payments/promptpay)THBThailandThailand[Swish](https://docs.stripe.com/payments/swish)SEKAustria,
Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland,
France, Germany, Greece, Ireland, Iceland, Italy, Latvia, Liechtenstein,
Lithuania, Luxembourg, Netherlands, Norway, Poland, Romania, Slovakia, Slovenia,
Spain, SwedenSweden[TWINT](https://docs.stripe.com/payments/twint)CHFAustria,
Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland,
France, Germany, Gibraltar, Greece, Hungary, Ireland, Iceland, Italy, Latvia,
Liechtenstein, Lithuania, Luxembourg, Malta, Monaco, Netherlands, Norway,
Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, Sweden, Spain,
Switzerland, United
KingdomSwitzerland[Boleto](https://docs.stripe.com/payments/boleto)BRLBrazilBrazil[Konbini](https://docs.stripe.com/payments/konbini)JPYJapanJapan[Multibanco](https://docs.stripe.com/payments/multibanco)EURAustria,
Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland,
France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Liechtenstein,
Lithuania, Luxembourg, Latvia, Malta, Netherlands, Norway, Poland, Portugal,
Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom, United
StatesPortugal[OXXO](https://docs.stripe.com/payments/oxxo)MXNMexicoMexico[Alipay](https://docs.stripe.com/payments/alipay)AUD,
CAD, CNY, EUR, GBP, HKD, JPY, MYR, NZD, SGD, USDAustralia, Canada, European
Union, Hong Kong, Japan, New Zealand, Singapore, United StatesChinese consumers,
overseas Chinese, and Chinese travelers[Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay)USDUnited StatesUnited States
customers (excluding accounts in US
territories)[GrabPay](https://docs.stripe.com/payments/grabpay)MYR, SGDMalaysia,
SingaporeMalaysia,
Singapore[MobilePay](https://docs.stripe.com/payments/mobilepay)DKK, EUR, NOK,
SEKAustria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark,
Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia,
Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland,
Portugal, Romania, Slovakia, Slovenia, Spain, SwedenDenmark, Finland[WeChat
Pay](https://docs.stripe.com/payments/wechat-pay)AUD, CAD, CHF (depending on
business location), CNY, DKK, EUR, GBP, HKD, JPY, NOK, SEK, SGD, USDAustralia,
Canada, European Union, Hong Kong, Japan, Singapore, United Kingdom, United
StatesChinese consumers, overseas Chinese, and Chinese
travelers[Zip](https://docs.stripe.com/payments/zip)AUD, USD (Invite
only)Australia, United States (Invite only)Australia, United States (Invite
only)
## Product support

To determine which payment methods each Stripe product supports, refer to the
following tables:

#### Checkout modes

Checkout has three modes:
[payment](https://docs.stripe.com/payments/accept-a-payment?platform=web),
[subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions?platform=web&ui=stripe-hosted),
and [setup](https://docs.stripe.com/payments/save-and-reuse?platform=web).
Unless specified otherwise, the payment method is available in all modes.

### Bank debits product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments) or [ACH
Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)[Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit) 1[BECS
Debit](https://docs.stripe.com/payments/au-becs-debit)[Pre-authorized debit in
Canada](https://docs.stripe.com/payments/acss-debit) 2 3[SEPA Direct
Debit](https://docs.stripe.com/payments/sepa-debit)
1 You can’t use the Payment Element to create SetupIntents for Bacs Direct
Debit. Use Checkout in [setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
instead.2 Not supported when using Checkout in subscription mode.3 Supports ACSS
debit if you [create a PaymentIntent before rendering the Payment
Element](https://docs.stripe.com/payments/accept-a-payment-deferred).

[Contact us](https://support.stripe.com/contact) to request a new bank debit
method.

### Bank redirects product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Bancontact](https://docs.stripe.com/payments/bancontact)Invite
only[BLIK](https://docs.stripe.com/payments/blik)
1,2[EPS](https://docs.stripe.com/payments/eps) 1,2Invite
only[FPX](https://docs.stripe.com/payments/fpx)
1,2[iDEAL](https://docs.stripe.com/payments/ideal)[P24](https://docs.stripe.com/payments/p24)
1,2Invite only[TWINT](https://docs.stripe.com/payments/twint) 1,2
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.

[Contact us](https://support.stripe.com/contact) to request a new bank redirect
payment method.

### Bank transfers product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)Bank transfers1,2
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.

### Buy now, pay later product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Affirm](https://docs.stripe.com/payments/affirm)1,2[Afterpay
(Clearpay)](https://docs.stripe.com/payments/afterpay-clearpay)1,2[Alma](https://docs.stripe.com/payments/alma)1,2[Billie](https://docs.stripe.com/payments/billie)1,2[Capchase
Pay](https://docs.stripe.com/payments/capchase-pay)1,2[Klarna](https://docs.stripe.com/payments/klarna)1,2Private
PreviewSign
up[Kriya](https://docs.stripe.com/payments/kriya)1,2[Mondu](https://docs.stripe.com/payments/mondu)1,2[SeQura](https://docs.stripe.com/payments/sequra)1,2[Sunbit](https://docs.stripe.com/payments/sunbit)1,2[Zip](https://docs.stripe.com/payments/zip)1,2
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.

### Cards product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Cards](https://docs.stripe.com/payments/cards/overview)
### Link product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Link](https://docs.stripe.com/payments/link)
### Real-time payments product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Pay by
Bank](https://docs.stripe.com/payments/pay-by-bank)1[PayNow](https://docs.stripe.com/payments/paynow)1,2344[PromptPay](https://docs.stripe.com/payments/promptpay)1,2344[Swish](https://docs.stripe.com/payments/swish)1,2
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.3 Only supported on iOS.4 Invoices and
Subscriptions only support the
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
collection method.

### Vouchers product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Boleto](https://docs.stripe.com/payments/boleto)[Konbini](https://docs.stripe.com/payments/konbini)41,233[Multibanco](https://docs.stripe.com/payments/multibanco)33[OXXO](https://docs.stripe.com/payments/oxxo)1,2
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.3 Invoices and Subscriptions only support the
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
collection method.4[Request an
invite](https://support.stripe.com/contact/email?topic=payment_apis) to create
charges [on behalf of](https://docs.stripe.com/connect/charges#on_behalf_of)
other accounts.

### Wallets product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)[Alipay](https://docs.stripe.com/payments/alipay)1,2Invite
onlyInvite only[Amazon Pay](https://docs.stripe.com/payments/amazon-pay)3[Apple
Pay](https://docs.stripe.com/apple-pay)75[Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay)[Google
Pay](https://docs.stripe.com/google-pay)7[GrabPay](https://docs.stripe.com/payments/grabpay)1,2[Link](https://docs.stripe.com/payments/wallets/link)6[MB
WAY](https://docs.stripe.com/payments/mb-way)1,2,3[MobilePay](https://docs.stripe.com/payments/mobilepay)1,2[PayPal](https://docs.stripe.com/payments/paypal)3[Revolut
Pay](https://docs.stripe.com/payments/revolut-pay)[WeChat
Pay](https://docs.stripe.com/payments/wechat-pay)1,244
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.3 Not supported when saving payment details during
payment (`setup_future_usage`).4 Invoices and Subscriptions only support the
`send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).5
Checkout with
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
set to `embedded` supports only Safari version 17 or later and iOS version 17 or
later.6 The Payment Element doesn’t support Link in Brazil or India.7 Stripe
doesn’t display Apple Pay or Google Pay for IP addresses in India.

## Additional API support

To learn about payment method API support, refer to the following tables:

### Bank debits API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2[ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit)`us_bank_account`No[Bacs
Direct
debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)`bacs_debit`
34No[BECS Direct
Debit](https://docs.stripe.com/payments/au-becs-debit)`au_becs_debit`No[Pre-authorized
debit in Canada](https://docs.stripe.com/payments/acss-debit)`acss_debit`No[SEPA
debit](https://docs.stripe.com/payments/sepa-debit)`sepa_debit`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.3 PaymentIntents support confirmation with Bacs Direct Debit payment
methods when the [Mandate](https://docs.stripe.com/api/mandates) has been
collected by a Stripe-owned flow such as
[Checkout](https://docs.stripe.com/payments/checkout), [Payment
Element](https://docs.stripe.com/payments/payment-element), and [Payment
Links](https://docs.stripe.com/payment-links).4 You can create SetupIntents for
Bacs Direct Debit through [Checkout](https://docs.stripe.com/payments/checkout)
using [setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout).

### Bank redirects API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect
2[Bancontact](https://docs.stripe.com/payments/bancontact)`bancontact`Yes[BLIK](https://docs.stripe.com/payments/blik)`blik`No[EPS](https://docs.stripe.com/payments/eps)`eps`Yes[FPX](https://docs.stripe.com/payments/fpx)`fpx`Yes[iDEAL](https://docs.stripe.com/payments/ideal)`ideal`Yes[P24](https://docs.stripe.com/payments/p24)`p24`Yes[Pay
by
Bank](https://docs.stripe.com/payments/pay-by-bank)`pay_by_bank`Yes[TWINT](https://docs.stripe.com/payments/twint)`twint`Yes
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

### Bank transfers API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2Bank transfers`customer_balance`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

### Buy now, pay later API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2[Affirm](https://docs.stripe.com/payments/affirm)`affirm`Yes[Afterpay
(Clearpay)](https://docs.stripe.com/payments/afterpay-clearpay)`afterpay_clearpay`Yes[Alma](https://docs.stripe.com/payments/alma)`alma`Yes[Billie](https://docs.stripe.com/payments/billie)`billie`Yes[Capchase
Pay](https://docs.stripe.com/payments/capchase-pay)`capchase_pay`Yes[Klarna](https://docs.stripe.com/payments/klarna)`klarna`Yes[Kriya](https://docs.stripe.com/payments/kriya)`kriya`Yes[Mondu](https://docs.stripe.com/payments/mondu)`mondu`Yes[SeQura](https://docs.stripe.com/payments/sequra)`sequra`Yes[Sunbit](https://docs.stripe.com/payments/sunbit)`sunbit`Yes[Zip](https://docs.stripe.com/payments/zip)`zip`Yes
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

### Cards API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2Cards`card`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe redirects your customer after they complete the
payment.

### Link API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2[Link](https://docs.stripe.com/payments/link)`link`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe redirects your customer after they complete the
payment.

### Real-time payments API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2[Pay by
Bank](https://docs.stripe.com/payments/pay-by-bank)`pay_by_bank`Yes[PayNow](https://docs.stripe.com/payments/paynow)`paynow`No[PromptPay](https://docs.stripe.com/payments/promptpay)`promptpay`No[Swish](https://docs.stripe.com/payments/swish)`swish`Yes
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

### Vouchers API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2[Boleto](https://docs.stripe.com/payments/boleto)`boleto`No[Konbini](https://docs.stripe.com/payments/konbini)`konbini`No[Multibanco](https://docs.stripe.com/payments/multibanco)`multibanco`No[OXXO](https://docs.stripe.com/payments/oxxo)`oxxo`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

### Wallets API support

Payment methodAPI enum
[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2[Alipay](https://docs.stripe.com/payments/alipay)`alipay`No[Amazon
Pay](https://docs.stripe.com/payments/amazon-pay)`amazon_pay`Yes[Apple
Pay](https://docs.stripe.com/apple-pay)No[Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay)`cashapp`Yes[Google
Pay](https://docs.stripe.com/google-pay)No[GrabPay](https://docs.stripe.com/payments/grabpay)`grabpay`Yes[Link](https://docs.stripe.com/payments/wallets/link)`link`Yes[MB
WAY](https://docs.stripe.com/payments/mb-way)`mb_way`No[MobilePay](https://docs.stripe.com/payments/mobilepay)`mobilepay`Yes[PayPal](https://docs.stripe.com/payments/paypal)`paypal`Yes[Revolut
Pay](https://docs.stripe.com/payments/revolut-pay)`revolut_pay`Yes[Secure Remote
Commerce](https://docs.stripe.com/secure-remote-commerce)A comma-separated list
of accepted card brandsYes[WeChat
Pay](https://docs.stripe.com/payments/wechat-pay)`wechat_pay`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

## Links

- [Link](https://docs.stripe.com/payments/link)
- [integration
option](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Country and currency
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support)
- [Product
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
- [API
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)
- [documentation](https://docs.stripe.com/payments/payment-methods/overview)
- [payment terms](https://stripe.com/payment-terms/legal)
- [Payment Methods
review](https://dashboard.stripe.com/settings/payment_methods/review)
- [payment
method](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
- [Adding payment method
capabilities](https://docs.stripe.com/connect/payment-methods)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [Alma](https://docs.stripe.com/payments/alma)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Apple-supported locations](https://support.apple.com/en-us/HT204916)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment)
- [BECS direct debit](https://docs.stripe.com/payments/au-becs-debit)
- [Pre-authorized debit in Canada](https://docs.stripe.com/payments/acss-debit)
- [SEPA debit](https://docs.stripe.com/payments/sepa-debit)
- [Bancontact](https://docs.stripe.com/payments/bancontact)
- [Bank transfers](https://docs.stripe.com/payments/bank-transfers)
- [BLIK](https://docs.stripe.com/payments/blik)
- [EPS](https://docs.stripe.com/payments/eps)
- [FPX](https://docs.stripe.com/payments/fpx)
- [Google Pay](https://docs.stripe.com/google-pay)
- [Google-supported
locations](https://support.google.com/googlepay/answer/12429287?hl=en#zippy=)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [P24](https://docs.stripe.com/payments/p24)
- [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Affirm](https://docs.stripe.com/payments/affirm)
- [Afterpay (Clearpay)](https://docs.stripe.com/payments/afterpay-clearpay)
- [Klarna](https://docs.stripe.com/payments/klarna)
- [Cards](https://docs.stripe.com/payments/cards/overview)
- [MB WAY](https://docs.stripe.com/payments/mb-way)
- [PayNow](https://docs.stripe.com/payments/paynow)
- [PromptPay](https://docs.stripe.com/payments/promptpay)
- [Swish](https://docs.stripe.com/payments/swish)
- [TWINT](https://docs.stripe.com/payments/twint)
- [Boleto](https://docs.stripe.com/payments/boleto)
- [Konbini](https://docs.stripe.com/payments/konbini)
- [Multibanco](https://docs.stripe.com/payments/multibanco)
- [OXXO](https://docs.stripe.com/payments/oxxo)
- [Alipay](https://docs.stripe.com/payments/alipay)
- [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay)
- [GrabPay](https://docs.stripe.com/payments/grabpay)
- [MobilePay](https://docs.stripe.com/payments/mobilepay)
- [WeChat Pay](https://docs.stripe.com/payments/wechat-pay)
- [Zip](https://docs.stripe.com/payments/zip)
- [payment](https://docs.stripe.com/payments/accept-a-payment?platform=web)
-
[subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions?platform=web&ui=stripe-hosted)
- [setup](https://docs.stripe.com/payments/save-and-reuse?platform=web)
- [Connect](https://docs.stripe.com/connect)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Mobile Payment Element](https://docs.stripe.com/payments/mobile)
- [Subscriptions](https://docs.stripe.com/subscriptions)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Customer Portal](https://docs.stripe.com/customer-management)
- [Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [create a PaymentIntent before rendering the Payment
Element](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [Contact us](https://support.stripe.com/contact)
- [Billie](https://docs.stripe.com/payments/billie)
- [Capchase Pay](https://docs.stripe.com/payments/capchase-pay)
- [Kriya](https://docs.stripe.com/payments/kriya)
- [Mondu](https://docs.stripe.com/payments/mondu)
- [SeQura](https://docs.stripe.com/payments/sequra)
- [Sunbit](https://docs.stripe.com/payments/sunbit)
-
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Request an
invite](https://support.stripe.com/contact/email?topic=payment_apis)
- [on behalf of](https://docs.stripe.com/connect/charges#on_behalf_of)
- [Link](https://docs.stripe.com/payments/wallets/link)
- [Revolut Pay](https://docs.stripe.com/payments/revolut-pay)
-
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [SetupIntents](https://docs.stripe.com/payments/setup-intents)
- [Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Setup future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
-
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
- [Mandate](https://docs.stripe.com/api/mandates)
- [Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce)