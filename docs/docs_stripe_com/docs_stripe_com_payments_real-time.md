# Real-time payments

## Learn about real-time payments with Stripe.

Real-time payment methods let customers directly transfer money from their bank
account or alternate funding source using an authenticating intermediary, like a
phone number. Because this payment method type increases transaction speeds, it
can improve conversion rates. Stripe supports real-time payments in Brazil,
Singapore, Thailand, Sweden, and India.

## Payment process

The real-time payment method process is as follows:

- Stripe sends the customer an identifier that lists the payable amount.
- The customer makes the payment through their application or third-party
service.
- The application or third-party service communicates with the customers bank to
secure the funds.

When a customer uses a real-time payment method, their statement lists the
application or third-party service as the payment type.

## Product support

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

## API support

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

## Links

- [Contact us](https://support.stripe.com/contact)
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
- [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
- [PayNow](https://docs.stripe.com/payments/paynow)
- [PromptPay](https://docs.stripe.com/payments/promptpay)
- [Swish](https://docs.stripe.com/payments/swish)
-
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
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