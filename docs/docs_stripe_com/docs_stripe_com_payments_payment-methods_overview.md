# Supported payment methods

## Learn about the types of payment methods that your Stripe integration can support.

We categorize payment methods into eight families:

- [Cards](https://docs.stripe.com/payments/payment-methods/overview#cards)
- [Bank
debits](https://docs.stripe.com/payments/payment-methods/overview#bank-debits)
- [Bank
redirects](https://docs.stripe.com/payments/payment-methods/overview#bank-redirects)
- [Bank
transfers](https://docs.stripe.com/payments/payment-methods/overview#bank-transfers)
- [Buy now, pay
later](https://docs.stripe.com/payments/payment-methods/overview#buy-now-pay-later)
- [Real-time
payments](https://docs.stripe.com/payments/payment-methods/overview#real-time-payments)
- [Vouchers](https://docs.stripe.com/payments/payment-methods/overview#vouchers)
- [Wallets](https://docs.stripe.com/payments/payment-methods/overview#wallets)

Each family has similar features, a single integration, and common checkout
experiences. After you’ve integrated one payment method, you can add another
within the same family with minimal changes to your integration.

To learn more about which payment methods are right for your business, see our
[payment method guide](https://stripe.com/payments/payment-methods-guide).

## Cards

Cards are a common way for consumers and businesses to pay online or in person.
Stripe supports global and local card networks. See the [card
brands](https://docs.stripe.com/payments/cards#supported-card-brands) that
Stripe supports.

GlobalUS and CanadaEuropeAsiaLatin
America[Visa](https://docs.stripe.com/payments/cards#supported-card-brands)[Discover](https://docs.stripe.com/payments/cards#supported-card-brands)[Cartes
Bancaires](https://docs.stripe.com/payments/cartes-bancaires)[JCB](https://docs.stripe.com/payments/cards#supported-card-brands)—[Mastercard](https://docs.stripe.com/payments/cards#supported-card-brands)[InteracIn-person
only](https://docs.stripe.com/terminal/payments/regional?country=CA)[China Union
Pay](https://docs.stripe.com/payments/cards#supported-card-brands)[American
Express](https://docs.stripe.com/payments/cards#supported-card-brands)[South
Korean
Cards](https://docs.stripe.com/payments/countries/korea)[Diners](https://docs.stripe.com/payments/cards#supported-card-brands)
In-person payments support different card brands, depending on the country and
card reader type. For more information, see Terminal’s [supported card
brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands#in-person-brand-capabilities).

## Bank debits

By debiting your customer’s bank account directly, you can save on transaction
fees when compared to cards. For details, see the [bank debits
documentation](https://docs.stripe.com/payments/bank-debits).

GlobalUS and CanadaEuropeAsiaLatin America—[Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)[Bacs
Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)[BECS
Direct Debit](https://docs.stripe.com/payments/au-becs-debit)—[ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit)[SEPA Direct
Debit](https://docs.stripe.com/payments/sepa-debit)[Canadian
PADs](https://docs.stripe.com/payments/acss-debit)
## Bank redirects

Bank redirects let customers pay online using their bank account, using a
secure, intuitive checkout flow. They’re popular among European and Asian
consumers and can improve conversion and reduce fraud. See [bank
redirects](https://docs.stripe.com/payments/bank-redirects) to learn more.

GlobalUS and CanadaEuropeAsiaLatin
America——[Bancontact](https://docs.stripe.com/payments/bancontact)[FPX](https://docs.stripe.com/payments/fpx)—[BLIK](https://docs.stripe.com/payments/blik)[PayNow](https://docs.stripe.com/payments/paynow)[EPS](https://docs.stripe.com/payments/eps)UPIInvite
only[iDEAL](https://docs.stripe.com/payments/ideal)NetbankingInvite
only[P24](https://docs.stripe.com/payments/p24)[TWINT](https://docs.stripe.com/payments/twint)
To request access to one of our invite only payment methods, [contact
us](https://support.stripe.com/contact).

## Bank transfers

Customers or other businesses can use bank transfers to send money directly to
your bank account and are common for accepting large payments from other
businesses. In some countries, bank transfers are popular for consumer payments
as well. See [bank transfers](https://docs.stripe.com/payments/bank-transfers)
to learn more.

GlobalUS and CanadaEuropeAsiaLatin America—[USD Bank
Transfer](https://docs.stripe.com/payments/bank-transfers)[SEPA Bank
Transfer](https://docs.stripe.com/payments/bank-transfers)[Japan Bank Transfer
(Furikomi)](https://docs.stripe.com/payments/bank-transfers)[Mexico Bank
Transfer](https://docs.stripe.com/payments/bank-transfers)[UK Bank
Transfer](https://docs.stripe.com/payments/bank-transfers)
## Buy now, pay later

Buy now, pay later payment methods help retailers reach customers that want to
pay in installments. Your business is paid immediately and in full, and your
customer pays nothing or a portion of the total cost at checkout. See [buy now,
pay later](https://docs.stripe.com/payments/buy-now-pay-later) to learn more.

Payment methodUS and CanadaEuropeAsiaLatin
America[Affirm](https://docs.stripe.com/payments/affirm)[Afterpay /
Clearpay](https://docs.stripe.com/payments/afterpay-clearpay)[Klarna](https://docs.stripe.com/payments/klarna)[Meses
sin
intereses](https://docs.stripe.com/payments/mx-installments)[Zip](https://docs.stripe.com/payments/zip)
Invite Only
To request access to one of our invite only payment methods, [contact
us](https://support.stripe.com/contact).

## Real-time payments

Real-time payments let customers send money directly from their bank account or
other funding source using an intermediary to authenticate, such as a phone
number or other account. They’re a common payment type in Asia and Latin
America. See [real-time payments](https://docs.stripe.com/payments/real-time) to
learn more.

GlobalUS and CanadaEuropeAsiaLatin America——[SwishInvite
only](https://docs.stripe.com/payments/swish)[PayNow](https://docs.stripe.com/payments/paynow)[PixInvite
only](https://docs.stripe.com/payments/pix)———[PromptPay](https://docs.stripe.com/payments/promptpay)—
To request access to one of our invite only payment methods, [contact
us](https://support.stripe.com/contact).

## Vouchers

Vouchers are a popular way for customers in Asia and Latin America to complete
online purchases in-person. At checkout, customers receive a digital voucher
with pending transaction details and then complete the payment at local stores.
See [vouchers](https://docs.stripe.com/payments/vouchers) to learn more.

GlobalUS and CanadaEuropeAsiaLatin
America——[Multibanco](https://docs.stripe.com/payments/multibanco)[Konbini](https://docs.stripe.com/payments/konbini)[OXXO](https://docs.stripe.com/payments/oxxo)————[Boleto](https://docs.stripe.com/payments/boleto)
## Wallets

Wallets provide a fast and secure way for consumers to pay with a saved card or
a stored balance. Wallets improve conversion and reduce fraud, especially on
mobile. See [wallets](https://docs.stripe.com/payments/wallets) to learn more.

GlobalUS and CanadaEuropeAsiaLatin America[Apple PayNot available in
India](https://docs.stripe.com/apple-pay)[Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay)[PayPal](https://docs.stripe.com/payments/paypal)[Alipay](https://docs.stripe.com/payments/alipay)—[Google
PayNot available in
India](https://docs.stripe.com/google-pay)[MobilePay](https://docs.stripe.com/payments/mobilepay)[WeChat
Pay](https://docs.stripe.com/payments/wechat-pay)[Link](https://docs.stripe.com/payments/link)[GrabPay](https://docs.stripe.com/payments/grabpay)[Secure
Remote Commerce](https://docs.stripe.com/secure-remote-commerce)[Revolut
Pay](https://docs.stripe.com/payments/revolut-pay)[Kakao
Pay](https://docs.stripe.com/payments/countries/korea)[Naver
Pay](https://docs.stripe.com/payments/countries/korea)[Samsung
Pay](https://docs.stripe.com/payments/countries/korea)[PayCo](https://docs.stripe.com/payments/countries/korea)
To request access to one of our invite only payment methods, [contact
us](https://support.stripe.com/contact).

## See also

- [Guide to Payment Methods](https://stripe.com/payments/payment-methods-guide)
- [Supported card
brands](https://docs.stripe.com/payments/cards#supported-card-brands)
- [Faster checkout with Link](https://docs.stripe.com/payments/link)
- [Wallets](https://docs.stripe.com/payments/wallets)
- [Vouchers](https://docs.stripe.com/payments/vouchers)

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [payment method guide](https://stripe.com/payments/payment-methods-guide)
- [card brands](https://docs.stripe.com/payments/cards#supported-card-brands)
- [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires)
- [InteracIn-person
only](https://docs.stripe.com/terminal/payments/regional?country=CA)
- [South Korean Cards](https://docs.stripe.com/payments/countries/korea)
- [supported card
brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands#in-person-brand-capabilities)
- [bank debits documentation](https://docs.stripe.com/payments/bank-debits)
- [Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [Canadian PADs](https://docs.stripe.com/payments/acss-debit)
- [bank redirects](https://docs.stripe.com/payments/bank-redirects)
- [Bancontact](https://docs.stripe.com/payments/bancontact)
- [FPX](https://docs.stripe.com/payments/fpx)
- [BLIK](https://docs.stripe.com/payments/blik)
- [PayNow](https://docs.stripe.com/payments/paynow)
- [EPS](https://docs.stripe.com/payments/eps)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [P24](https://docs.stripe.com/payments/p24)
- [TWINT](https://docs.stripe.com/payments/twint)
- [contact us](https://support.stripe.com/contact)
- [bank transfers](https://docs.stripe.com/payments/bank-transfers)
- [buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later)
- [Affirm](https://docs.stripe.com/payments/affirm)
- [Afterpay / Clearpay](https://docs.stripe.com/payments/afterpay-clearpay)
- [Klarna](https://docs.stripe.com/payments/klarna)
- [Meses sin intereses](https://docs.stripe.com/payments/mx-installments)
- [Zip](https://docs.stripe.com/payments/zip)
- [real-time payments](https://docs.stripe.com/payments/real-time)
- [SwishInvite only](https://docs.stripe.com/payments/swish)
- [PixInvite only](https://docs.stripe.com/payments/pix)
- [PromptPay](https://docs.stripe.com/payments/promptpay)
- [vouchers](https://docs.stripe.com/payments/vouchers)
- [Multibanco](https://docs.stripe.com/payments/multibanco)
- [Konbini](https://docs.stripe.com/payments/konbini)
- [OXXO](https://docs.stripe.com/payments/oxxo)
- [Boleto](https://docs.stripe.com/payments/boleto)
- [wallets](https://docs.stripe.com/payments/wallets)
- [Apple PayNot available in India](https://docs.stripe.com/apple-pay)
- [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Alipay](https://docs.stripe.com/payments/alipay)
- [Google PayNot available in India](https://docs.stripe.com/google-pay)
- [MobilePay](https://docs.stripe.com/payments/mobilepay)
- [WeChat Pay](https://docs.stripe.com/payments/wechat-pay)
- [Link](https://docs.stripe.com/payments/link)
- [GrabPay](https://docs.stripe.com/payments/grabpay)
- [Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce)
- [Revolut Pay](https://docs.stripe.com/payments/revolut-pay)