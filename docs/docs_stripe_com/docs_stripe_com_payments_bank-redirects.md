# Bank redirects

## Learn about bank redirects with Stripe.

Bank redirects let customers pay online using their bank account. They drive
more than half of online commerce in Germany, the Netherlands, and Malaysia.
Bank redirects are often used by:

- Retailers that want to improve conversion and reduce fraud with consumers in
Europe and Asia Pacific.
- Software or service businesses collecting one-time payments from other
businesses.

Bank redirects might not be a good fit for your business if you sell
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating). Some
bank redirects don’t support recurring payments.

## Payment flow

At checkout, the customer is redirected to their online banking portal, logs in
with their bank credentials, approves the transaction, and then returns to your
site. Some bank redirects verify the user through SMS or other two-factor
authentication for additional security.

![Bank redirect payment flow from checkout to payment
confirmation.](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.d6b9be158ecbb4b70a85d2497da2e405.svg)

## Product support

We’ve created a single integration for all bank redirects that works across
Stripe products. With [Stripe
Checkout](https://docs.stripe.com/payments/checkout), you can add any bank
redirect by changing one line of code.

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

## API support

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

## Migrating from the Sources or Tokens APIs

If you currently use the Sources or Tokens API, see [migrating to
PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration) to
use the latest integrations.

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Connect](https://docs.stripe.com/connect)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Mobile Payment Element](https://docs.stripe.com/payments/mobile)
- [Subscriptions](https://docs.stripe.com/subscriptions)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Customer Portal](https://docs.stripe.com/customer-management)
- [Bancontact](https://docs.stripe.com/payments/bancontact)
- [BLIK](https://docs.stripe.com/payments/blik)
- [EPS](https://docs.stripe.com/payments/eps)
- [FPX](https://docs.stripe.com/payments/fpx)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [P24](https://docs.stripe.com/payments/p24)
- [TWINT](https://docs.stripe.com/payments/twint)
- [Contact us](https://support.stripe.com/contact)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [SetupIntents](https://docs.stripe.com/payments/setup-intents)
- [Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Setup future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)
- [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
-
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
- [migrating to
PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration)