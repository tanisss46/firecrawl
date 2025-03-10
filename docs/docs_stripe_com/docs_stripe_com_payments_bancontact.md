# Bancontact payments

## Learn about Bancontact, a common payment method in Belgium.

Bancontact is the most popular online payment method in Belgium, with over 15
million cards in circulation. Customers use a Bancontact card or mobile app
linked to a Belgian bank account to make online payments.

To pay with Bancontact, customers are redirected to the Bancontact website or
mobile app to [authorize the
payment](https://docs.stripe.com/payments/payment-methods#customer-actions) and
then return to your website where there is [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
about the success or failure of the payment.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Belgium
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-authenticated
- **Payment method family**

Authenticated bank-debit
- **Recurring payments**

with [SEPA Direct
Debit](https://docs.stripe.com/billing/subscriptions/bancontact)
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/bancontact#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/bancontact#refunds)

## Payment flows

!

Customer selects Bancontact at checkout

!

Customer is redirected to Bancontact and enters credentials

!

Customer is notified that payment is complete

!

(Optional) Customer returns back to business’s site for payment confirmation

!

Customer selects Bancontact at checkout

!

Customer is redirected to Bancontact and scans QR code

!

Customer enters pincode

!

Customer is notified that payment is complete

!

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t have to integrate Bancontact and other payment methods individually.
If you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Bancontact. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Bancontact from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If you prefer to manually list payment methods or want to save Bancontact
details for future payments, see the following guides:

- [Manually configure Bancontact as a
payment](https://docs.stripe.com/payments/bancontact/accept-a-payment)
- [Save Bancontact details for future
payments](https://docs.stripe.com/payments/bancontact/set-up-payment)

## Disputes

The risk of fraud or unrecognized payments is low because the customer must
authenticate the payment with their bank. As a result, you won’t have disputes
that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Bancontact payments can be refunded up to 180 days after the original payment
date.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [authorize the
payment](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [SEPA Direct Debit](https://docs.stripe.com/billing/subscriptions/bancontact)
- [No](https://docs.stripe.com/payments/bancontact#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/bancontact#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Manually configure Bancontact as a
payment](https://docs.stripe.com/payments/bancontact/accept-a-payment)
- [Save Bancontact details for future
payments](https://docs.stripe.com/payments/bancontact/set-up-payment)