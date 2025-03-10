# BLIK payments

## Learn about BLIK, a common payment method in Poland.

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payments. When customers want to pay online using BLIK, they request a
six-digit code from their banking application and enter it into the payment
collection form.

The bank sends a push notification to your customer’s mobile phone asking to
authorize the payment inside their banking application. The BLIK code is valid
for 2 minutes; customers have 60 seconds to authorize the payment after starting
a payment. After 60 seconds, it times out and they must request a new BLIK code.
Customers typically approve BLIK payments in less than 10 seconds.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Poland
- **Presentment currency**

PLN
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Authenticated bank debit
- **Recurring payments**

No
- **Payout timing**

Standard payout timing applies
- **Connect support**

[Yes](https://docs.stripe.com/payments/blik#connect)
- **Dispute support**

[Yes](https://docs.stripe.com/payments/blik#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/blik#refunds)

## Payment flow

!

Customer selects BLIK at checkout.

!

Customer is directed to their mobile banking app to generate a 6-digit code.

!

Customer puts the code into the checkout.

!

Customer is notified that payment is complete.

## Get started

You don’t have to integrate BLIK and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
BLIK. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

If you prefer to manually list payment methods, learn how to [manually configure
BLIK as a payment](https://docs.stripe.com/payments/blik/accept-a-payment).

## Disputes

BLIK has a claims process that allows transaction disputes. Customers can open
disputes for cases of suspected fraud, double payments, or a difference between
an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to
receive [webhooks](https://docs.stripe.com/webhooks))

Stripe holds back the disputed amount from your balance until BLIK resolves the
dispute.

We request that you upload compelling evidence proving that you fulfilled the
purchase order [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond). This evidence
can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or
proof of receipt
- Record of refund (for purchase you have already refunded)

To handle disputes programmatically, [respond to disputes using the
API](https://docs.stripe.com/disputes/api).

This information helps BLIK determine if a dispute is valid. Make sure the
evidence you provide contains as much detail as possible from what the customer
provided at checkout. You must submit the requested information within 12
calendar days. If BLIK resolves the dispute with you winning, we return the
disputed amount to your Stripe balance. If BLIK rules in favor of the customer,
the balance charge becomes permanent.

## Refunds

BLIK supports full and partial refunds. Depending on the bank, refunds are
processed immediately or within a couple of hours.

## Connect

If you use [Connect](https://docs.stripe.com/connect), you must consider the
following before you enable and use BLIK.

### Request BLIK capabilities for your connected accounts

Set the `blik_payments` capability to `active` on your platform account, and on
any connected accounts you want to enable BLIK for. You can also [request more
account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges) of Connect payments
might change the default statement descriptor and the merchant name that appears
on the customer’s banking application and confirmation emails.

Charge typeDescriptor taken fromDirectConnected
AccountDestinationPlatformSeparate charge and transferPlatformDestination (with
`on_behalf_of`)Connected AccountSeparate charge and transfer (with
`on_behalf_of`)Connected Account

## Links

- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Yes](https://docs.stripe.com/payments/blik#connect)
- [Yes](https://docs.stripe.com/payments/blik#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/blik#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [manually configure BLIK as a
payment](https://docs.stripe.com/payments/blik/accept-a-payment)
- [webhooks](https://docs.stripe.com/webhooks)
- [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond)
- [respond to disputes using the API](https://docs.stripe.com/disputes/api)
- [Connect](https://docs.stripe.com/connect)
- [request more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
- [charge type](https://docs.stripe.com/connect/charges)