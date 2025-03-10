# PayPal payments

## Learn about PayPal, a digital wallet popular with businesses in Europe.

PayPal is a payment method that enables customers in any country to pay using
their PayPal account.

To pay using PayPal, customers are redirected from your website to PayPal. They
choose a funding source: PayPal wallet, linked card or bank account, or buy now,
pay later. Then they authenticate the payment. After successful authorization,
the customer is redirected back to your website. You receive an [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
of the payment’s success or failure.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Worldwide
- **Presentment currency**

EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD
- **Payment method family**

Wallets
- **Payment confirmation**

Customer-initiated
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Connect support**

Partial (requires manual approval, see details
[below](https://docs.stripe.com/payments/paypal#connect))
- **Recurring payments**

Requires approval
- **Dispute support**

[Yes](https://docs.stripe.com/payments/paypal#disputed-payments)
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/paypal#refunds)

## Payment flow

!

[Customer](https://docs.stripe.com/api/customers) selects PayPal at checkout

!

Customer is redirected to PayPal and enters login details

!

Customer completes authorization process

!

Customer is notified that payment is complete

!

(Optional) Customer returns back to business’s site for payment confirmation

## Connect

PayPal is available for online marketplaces using [Stripe
Connect](https://stripe.com/connect). These online marketplaces include
businesses such as Deliveroo and ManoMano that collect payments from customers,
and later pay out to sub-accounts or service providers. PayPal isn’t available
for platforms that onboard other businesses and enable them to accept payments
directly, such as Shopify or Squarespace.

#### Note

Online marketplaces need to submit an onboarding request from the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) to get access
to PayPal. Stripe sends email updates about the progress of all requests, and
the current status is also reflected on the [Payment Method Settings
page](https://dashboard.stripe.com/settings/payment_methods).

The following [Connect charges](https://docs.stripe.com/connect/charges) types,
typically used by online marketplaces, are available to businesses using PayPal.

Destination chargesSeparate charges and transfersDirect chargeson_behalf_of
## Get started

Add PayPal and other payment methods from the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) without making
updates to your code. For each customer, Stripe determines the list of supported
payment methods most likely to drive conversion. Learn how to [accept PayPal and
other payment methods
automatically](https://docs.stripe.com/payments/accept-a-payment) with Checkout
or Elements. To accept PayPal and other payment methods without any code, use
[Payment Links](https://docs.stripe.com/payment-links).

When you’re ready to go live, follow the steps to [activate PayPal
payments](https://docs.stripe.com/payments/paypal/activate).

## Disputed payments

Customers must authenticate payments with their PayPal accounts, helping to
reduce the risk of fraud or unrecognized payments. However, customers can still
dispute transactions after they complete payment. Some common reasons for
disputes are customers determining that items weren’t as described, or not
receiving items at all. You can submit evidence to contest a dispute directly
from the Stripe Dashboard.

Learn how to [manage PayPal
disputes](https://docs.stripe.com/payments/paypal/disputed-payments) in the
Dashboard.

For certain dispute types, PayPal enables you communicate directly to customers
to try resolving the dispute. Contacting customers directly must be handled
through the PayPal dashboard, and not the Stripe Dashboard.

## Refunds

PayPal payments can be refunded up to 180 days after the original payment.
Stripe uses either your Stripe balance or your PayPal balance to refund the
payment, depending on the [settlement preference you
selected](https://docs.stripe.com/payments/paypal/choose-settlement-preference).

You can use the Stripe Dashboard or API to initiate refund requests, as with
other payment methods. If you choose to settle funds to Stripe, refunds will be
withdrawn from the funds available in your Stripe account. If you choose to
settle funds to PayPal, refunds funded using your PayPal balance or any other
funding source available on your PayPal account.

## Reporting

PayPal fees are included in the **Less fees** sections of [Balance and Balance
Activity reports](https://dashboard.stripe.com/reports/balance). PayPal fees
aren’t included in your [tax invoice from
Stripe](https://dashboard.stripe.com/settings/documents). You can access these
documents from your PayPal dashboard.

## Seller protection

PayPal’s Seller Protection program offers coverage for sellers under eligible
transactions. It includes scenarios such as unauthorized transactions or buyers’
claims of non-receipt of item. For more information on the Seller Protection
program and eligibility, visit [PayPal Seller
Protection](https://www.paypal.com/uk/legalhub/seller-protection).

## Prohibited business categories

In addition to the business categories restricted from using Stripe overall,
PayPal requires pre-approval to accept payments for certain services. Refer to
the [PayPal Acceptable Use
Policy](https://www.paypal.com/us/legalhub/acceptableuse-full) for details.

## Minimum and maximum charge amounts

PayPal doesn’t have a minimum charge amount, but Stripe enforces the same
[minimum and maximum charge
amounts](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
for PayPal as for other payment methods.

## Links

- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [below](https://docs.stripe.com/payments/paypal#connect)
- [Yes](https://docs.stripe.com/payments/paypal#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/paypal#refunds)
- [Customer](https://docs.stripe.com/api/customers)
- [Stripe Connect](https://stripe.com/connect)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Connect charges](https://docs.stripe.com/connect/charges)
- [accept PayPal and other payment methods
automatically](https://docs.stripe.com/payments/accept-a-payment)
- [Payment Links](https://docs.stripe.com/payment-links)
- [activate PayPal payments](https://docs.stripe.com/payments/paypal/activate)
- [manage PayPal
disputes](https://docs.stripe.com/payments/paypal/disputed-payments)
- [settlement preference you
selected](https://docs.stripe.com/payments/paypal/choose-settlement-preference)
- [Balance and Balance Activity
reports](https://dashboard.stripe.com/reports/balance)
- [tax invoice from Stripe](https://dashboard.stripe.com/settings/documents)
- [PayPal Seller
Protection](https://www.paypal.com/uk/legalhub/seller-protection)
- [PayPal Acceptable Use
Policy](https://www.paypal.com/us/legalhub/acceptableuse-full)
- [minimum and maximum charge
amounts](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)