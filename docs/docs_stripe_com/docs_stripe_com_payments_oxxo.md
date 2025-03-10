# OXXO payments

## Learn how to accept payments with OXXO.

OXXO is a Mexican chain of convenience stores with thousands of locations across
Latin America and represents nearly 20% of online transactions in Mexico. OXXO
allows customers to pay bills and online purchases in-store with cash.

To complete a transaction, customers receive a voucher that includes a reference
number for the transaction. Customers then bring their voucher to an OXXO store
to make a cash payment. You’ll receive payment confirmation by the next business
day along with the settled funds.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Mexico
- **Presentment currency**

MXN
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Cash-based payment method
- **Recurring payments**

No
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/oxxo#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[No / No](https://docs.stripe.com/payments/oxxo#refunds)

## Payment flow

!

Step 1. Selects OXXO at checkout

!

Step 2. Receives voucher with transaction reference

!

Step 3. Provides voucher and cash payment at OXXO store

!

Step 4. Receives notification that payment is complete

## Get started

You don’t have to integrate OXXO and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
OXXO. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

[Payment Links](https://docs.stripe.com/payment-links) also supports adding OXXO
from the Dashboard.

If your integration requires manually listing payment methods, learn how to
[manually configure OXXO as a
payment](https://docs.stripe.com/payments/oxxo/accept-a-payment).

Check out the OXXO [sample on
GitHub](https://github.com/stripe-samples/accept-a-payment).

## Disputes

OXXO payments have a low risk of fraud or unrecognized payments because the
customer must provide cash payment in person at an OXXO convenience store.
Customers can’t dispute OXXO payments.

## Refunds

OXXO payments can’t be refunded. Some businesses have created a separate process
to credit their customers who reach out directly.

## Amount limits

The amount for a single OXXO must be at least 10.00 MXN and no more than
10,000.00 MXN.

## Links

- [No](https://docs.stripe.com/payments/oxxo#disputed-payments)
- [No / No](https://docs.stripe.com/payments/oxxo#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure OXXO as a
payment](https://docs.stripe.com/payments/oxxo/accept-a-payment)
- [sample on GitHub](https://github.com/stripe-samples/accept-a-payment)