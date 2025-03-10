# Bank Debits

## Learn how to accept bank debits with Stripe.

With bank debits, you can pull funds directly from your customer’s bank account
for both one-time and recurring purchases. Bank debits are often used by:

- Businesses collecting recurring payments from other businesses.
- Retail and services businesses that want a low-cost alternative to cards for
large consumer payments, like rent or tuition.

Bank debits might not be a good fit for your business if:

- You deliver goods immediately after checkout because payment confirmation
takes 3-7 days.
- Your business is sensitive to disputes—consider other payment methods because
some bank debit methods favor the customer during disputes.

## Payment flow

To initiate a bank debit, a customer enters their bank account details during
checkout and gives you permission to debit the account. This permission is
called a mandate.

![Flow chart of the three step process the customer experiences. First, they
select bank debit at checkout. Next the customer provides banking details and
authorizes mandate. Finally, the customer gets notification that the payment is
complete.](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.e4fcc05342cae882b39c41b497e5a24d.svg)

To reduce fraud with some bank debits, verify the bank account before the
payment by confirming microdeposits or bank login. Verifying bank login can
improve the user experience because customers pay by logging into their bank
rather than entering bank account details.

## Product support

You can use a single integration for all bank debits that works across Stripe
products. With [Stripe Checkout](https://docs.stripe.com/payments/checkout),
[Payment Element](https://docs.stripe.com/payments/payment-element), and
[Payment Links](https://docs.stripe.com/payment-links), you can enable bank
debits directly from the Dashboard with no integration work.

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

## API support

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

## Migrating from the Sources, Tokens, or Charges APIs

If your current bank debit integration uses the Sources, Tokens, or Bank
Accounts API, we recommend following the appropriate migration guide to
transition to [Payment Intents
API](https://docs.stripe.com/payments/payment-intents):

- [ACH migration
guide](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges)
- For all other bank debit payment methods, follow the general [migration
guide](https://docs.stripe.com/payments/payment-intents/migration)

## Links

- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Connect](https://docs.stripe.com/connect)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Mobile Payment Element](https://docs.stripe.com/payments/mobile)
- [Subscriptions](https://docs.stripe.com/subscriptions)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Customer Portal](https://docs.stripe.com/customer-management)
- [Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit)
- [BECS Debit](https://docs.stripe.com/payments/au-becs-debit)
- [Pre-authorized debit in Canada](https://docs.stripe.com/payments/acss-debit)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [create a PaymentIntent before rendering the Payment
Element](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [Contact us](https://support.stripe.com/contact)
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
- [ACH migration
guide](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges)
- [migration guide](https://docs.stripe.com/payments/payment-intents/migration)