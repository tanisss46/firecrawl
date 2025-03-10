# Vouchers

## Learn about voucher payment methods with Stripe.

With vouchers, customers complete online purchases in-person at authorized
locations like convenience stores. Vouchers are often used by:

- Businesses with customers that don’t have cards or bank accounts.
- Retailers with consumers in countries like Mexico, where card authorizations
rates are low and offering a backup payment option improves conversion.

Vouchers might not be a good fit for your business if:

- You deliver goods immediately after checkout. Some customers may not complete
payment and it can take 1 business day to receive a payment confirmation.
- You need to send refunds. Not all vouchers support refunds. Some businesses
create separate processes to credit customers who ask for a refund directly.

## Payment flow

When a customer chooses a voucher method for payment, they receive a digital
voucher through email or in an app with a transaction summary and a voucher
code. The customer scans the voucher code at an authorized location like a
convenience store and pays in-person, often with cash.

![Figure describing the four step voucher payment flow. First, customer selects
voucher payment at checkout. Next, they receive a voucher with transaction
reference. Then, they provide voucher and cash at a store, ATM, or bank.
Finally, receive notification that payment is
complete.](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.7acf8f7f09d6fa1883720435f7c2589b.svg)

## Product support

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

## API support

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

## Migrating from the Sources or Tokens APIs

If you currently use the Sources or Tokens API, see [migrating to
PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration) to
use the latest integrations.

## Links

- [Checkout](https://docs.stripe.com/payments/checkout/discounts)
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
- [Boleto](https://docs.stripe.com/payments/boleto)
- [Konbini](https://docs.stripe.com/payments/konbini)
- [Multibanco](https://docs.stripe.com/payments/multibanco)
- [OXXO](https://docs.stripe.com/payments/oxxo)
-
[send_invoice](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Request an
invite](https://support.stripe.com/contact/email?topic=payment_apis)
- [on behalf of](https://docs.stripe.com/connect/charges#on_behalf_of)
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
- [migrating to
PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration)