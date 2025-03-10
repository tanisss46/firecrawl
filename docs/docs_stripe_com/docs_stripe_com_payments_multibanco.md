# Multibanco payments

## Learn how to accept payments with Multibanco.

Multibanco is a voucher-based payment method in Portugal. If your business is
based in Europe or the United States, you can accept Multibanco payments from
customers in Portugal using the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents).

To complete a transaction, customers receive a voucher that includes Multibanco
entity and reference numbers. Customers use these voucher details to make a
payment outside your checkout flow through online banking or from an ATM.

Payment confirmation might be delayed by several days due to the initiation of a
bank transfer when a customer pays for a Multibanco voucher. Bank transfers can
encounter delays, particularly over weekends, contributing to the delay in
payment confirmation.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Portugal
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Voucher
- **Recurring payments**

[Yes](https://docs.stripe.com/payments/multibanco#billing)
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Refunds / partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/multibanco#refunds)
- **Connect support**

[Yes](https://docs.stripe.com/payments/multibanco#connect)
- **Dispute support**

[No](https://docs.stripe.com/payments/multibanco#disputes)
- **Manual capture support**

No
- **Minimum charge amount**

0.50 EUR
- **Maximum charge amount**

99,999 EUR

## Payment flows

### Online banking flow

!

Selects Multibanco at checkout

!

Receives voucher details (incl. entity, reference, and amount)

!

Logs into online banking

!

Uses voucher details to complete the payment with online banking

!

Receives confirmation of funds sent

### ATM flow

!

Selects Multibanco at checkout

!

Receives voucher details (incl. entity, reference, and amount)

!

Uses voucher details to complete the payment at an ATM

!

Receives confirmation of funds sent

## Get started

You don’t have to integrate Multibanco and other payment methods individually.
If you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Multibanco. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Multibanco from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If you prefer to manually list payment methods, learn how to [manually configure
Multibanco as a payment
method](https://docs.stripe.com/payments/multibanco/accept-a-payment).

## Disputes

The risk of fraud or unrecognized payments is low with Multibanco because the
customer must push funds from their bank account. As a result, there’s no
dispute process that can result in a chargeback and funds withdrawn from your
Stripe account.

## Refunds

You can refund Multibanco payments in the
[Dashboard](https://dashboard.stripe.com/payments) or using the [Refunds
API](https://docs.stripe.com/api/refunds).

The refund period for Multibanco is up to 365 days after the original payment.
Full and partial refunds are supported. Customers typically receive refunds in
their bank accounts within 1 day. However, this time frame varies by bank.

If a Multibanco [Refund](https://docs.stripe.com/api/refunds/object) object’s
`status` transitions to `succeeded`, the
[destination_details.multibanco.reference](https://docs.stripe.com/api/refunds/object#refund_object-destination_details-multibanco-reference)
property contains a refund identifier that you can provide the customer.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create Multibanco supported
[invoices](https://docs.stripe.com/api/invoices) and
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating).
Multibanco invoices and subscriptions only support the `send_invoice`
[collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
with Multibanco to process payments on behalf of a connected account. Connect
users can use Multibanco with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

### Enable Multibanco for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable Multibanco in their
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) in the
Dashboard.

### Enable Multibanco for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Request the `multibanco_payments` capability on any connected account you want
to enable Multibanco for. Follow the instructions to [enable payment methods for
your connected accounts](https://docs.stripe.com/connect/account-capabilities).

## Links

- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [Yes](https://docs.stripe.com/payments/multibanco#billing)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [Yes / Yes](https://docs.stripe.com/payments/multibanco#refunds)
- [Yes](https://docs.stripe.com/payments/multibanco#connect)
- [No](https://docs.stripe.com/payments/multibanco#disputes)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [manually configure Multibanco as a payment
method](https://docs.stripe.com/payments/multibanco/accept-a-payment)
- [Dashboard](https://dashboard.stripe.com/payments)
- [Refunds API](https://docs.stripe.com/api/refunds)
- [Refund](https://docs.stripe.com/api/refunds/object)
-
[destination_details.multibanco.reference](https://docs.stripe.com/api/refunds/object#refund_object-destination_details-multibanco-reference)
- [Stripe Billing](https://stripe.com/billing)
- [invoices](https://docs.stripe.com/api/invoices)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities)