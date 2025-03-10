# Buy now, pay later

## Learn about buy now, pay later methods with Stripe.

Buy now, pay later methods let customers pay in installments over time. You’re
paid immediately and in full and your customers pay nothing or a portion of the
total at purchase time. Buy now, pay later methods are often used by:

- Retailers selling high value goods and services like luxury items or travel
fares that want to boost conversion.
- Retailers selling low value goods and services that want to increase average
cart size and reach new customers who might not have credit cards.
- Regional banks that allow consumers to split credit card payments over
multiple billing cycles.

Buy now, pay later methods might **not** be a good fit for your business if:

- Your customers are businesses. Buy now, pay later methods offered on Stripe
are only supported for consumers.
- Your business relies on subscriptions or recurring purchases. Buy now, pay
later methods don’t currently support
[Invoicing](https://docs.stripe.com/invoicing) or
[Subscriptions](https://docs.stripe.com/billing).

Read our [Buy Now, Pay Later Guide](https://stripe.com/guides/buy-now-pay-later)
for more information.

## Payments

At checkout, the customer chooses to pay with a buy now, pay later service. Then
the customer creates or logs into an account with the buy now, pay later
provider. Next, the customer accepts or declines the terms of the repayment
plan, and then returns to the business’ site.

!

## Product support

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

## API support

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

## Transaction support

Payment methodCustomer countryRepayment optionsTransaction
limit[Affirm](https://docs.stripe.com/payments/affirm)1Canada, United States-
Pay in 4 interest-free installments
- Monthly payments for up to 36 months
50 USD minimum; 30,000 USD maximum or local
equivalent-[Afterpay/Clearpay](https://docs.stripe.com/payments/afterpay-clearpay)Australia,
Canada, New Zealand, United Kingdom, United States- Pay in 4 interest-free
installments
- Monthly USD payments for up to 12 months
1 USD minimum; 4,000 USD maximum or local
equivalent[Klarna](https://docs.stripe.com/payments/klarna)Australia, Austria,
Belgium, Canada, Czechia, Denmark, Finland, France, Germany, Greece, Ireland,
Italy, Netherlands, New Zealand, Norway, Poland, Portugal, Spain, Sweden,
Switzerland, United Kingdom, United States- Pay in 3 or 4 interest-free
installments
- Pay in 30 days
- Pay now with stored payment details
- Monthly payments for up to 36 months
10 USD minimum or local equivalent. (Amounts over 5,000 USD for financing
possible; maximum varies by customer)[Meses sin
intereses](https://docs.stripe.com/payments/mx-installments)MexicoExtend
payments over 3 to 24 months of billing cycles[Minimum
transaction](https://docs.stripe.com/payments/mx-installments#fees) amount of
100 MXN per month of
extension[Zip](https://docs.stripe.com/payments/zip)2Australia, United States
(Invite Only)- Zip Pay: Pay using a 1,000 AUD credit, repay in your own time
- Zip Money: Pay in a minimum of 3 monthly interest-free installments
- Pay in 4 installments
0.01 AUD minimum. 50,000 AUD maximum for Australia or 35 USD minimum and 1,500
USD maximum for United States**
1 The maximum credit limit for Affirm is 20,000 USD or 20,000 CAD. However,
Affirm supports transactions up to 30,000 USD or 30,000 CAD. These transactions
require a down payment from the customer at time of purchase. Term lengths and
cart ranges are determined by Affirm and may change at their discretion.2 Zip
Australia offers two products, Zip Pay with a credit limit of 1,000 AUD and Zip
Money with a maximum credit limit of 50,000 AUD depending on the users’
eligibility. Zip US offers Pay in 4 with transactions up to 1,500 USD.

## Adding on site messaging to your website

Let your customers know you accept one or more of these payment methods by
including the [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging) on your
product and cart pages.

## Links

- [installment
plans](https://docs.stripe.com/billing/subscriptions/subscription-schedules/use-cases#installment-plans)
- [Subscription Schedules
API](https://docs.stripe.com/api/subscription_schedules)
- [accepting payments in
installments](https://docs.stripe.com/recurring-payments#installment-plans)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Subscriptions](https://docs.stripe.com/billing)
- [Buy Now, Pay Later Guide](https://stripe.com/guides/buy-now-pay-later)
- [Connect](https://docs.stripe.com/connect)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Mobile Payment Element](https://docs.stripe.com/payments/mobile)
- [Subscriptions](https://docs.stripe.com/subscriptions)
- [Customer Portal](https://docs.stripe.com/customer-management)
- [Affirm](https://docs.stripe.com/payments/affirm)
- [Afterpay (Clearpay)](https://docs.stripe.com/payments/afterpay-clearpay)
- [Alma](https://docs.stripe.com/payments/alma)
- [Billie](https://docs.stripe.com/payments/billie)
- [Capchase Pay](https://docs.stripe.com/payments/capchase-pay)
- [Klarna](https://docs.stripe.com/payments/klarna)
- [Kriya](https://docs.stripe.com/payments/kriya)
- [Mondu](https://docs.stripe.com/payments/mondu)
- [SeQura](https://docs.stripe.com/payments/sequra)
- [Sunbit](https://docs.stripe.com/payments/sunbit)
- [Zip](https://docs.stripe.com/payments/zip)
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
- [Meses sin intereses](https://docs.stripe.com/payments/mx-installments)
- [Minimum transaction](https://docs.stripe.com/payments/mx-installments#fees)
- [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging)