# Wallets

## Learn about wallet payments with Stripe.

Customers can use wallets to pay online with a saved card or a digital wallet
balance. Retailers often use wallets to:

- Reduce fraud and increase conversion on mobile.
- Reach buyers in China, where wallets are the most popular way to pay.

Wallets might not be a good fit for your business if you sell
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating). Some
wallets don’t support recurring payments.

## Payment flow

Customers confirm the transaction by authenticating their wallet credentials at
checkout. If using mobile, they can authenticate with fingerprint or face
recognition, their mobile passcode, or by logging into their wallet app. On the
web, they can also scan a QR code with their mobile phone to complete the
transaction.

### Customer-facing mobile flow

!

Selects wallet at checkout

!

Enters wallet credentials

!

Gets notification that payment is complete

### Customer-facing web flow

!

Selects wallet at checkout

!

Uses mobile to confirm payment

!

Gets notification that payment is complete

## Product support

The following table shows which Stripe products support each wallet:

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

## API support

The following table describes each wallet’s compatibility with API-based payment
flows:

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

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
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
- [Alipay](https://docs.stripe.com/payments/alipay)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [GrabPay](https://docs.stripe.com/payments/grabpay)
- [Link](https://docs.stripe.com/payments/wallets/link)
- [MB WAY](https://docs.stripe.com/payments/mb-way)
- [MobilePay](https://docs.stripe.com/payments/mobilepay)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Revolut Pay](https://docs.stripe.com/payments/revolut-pay)
- [WeChat Pay](https://docs.stripe.com/payments/wechat-pay)
- [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
-
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [SetupIntents](https://docs.stripe.com/payments/setup-intents)
- [Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Setup future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)
- [Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
-
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)