# Boleto payments

## Learn how to accept payments with Boleto.

Boleto is an official (regulated by the Central Bank of Brazil) payment method
in Brazil.

To complete a transaction, customers receive a voucher stating the amount to pay
for services or goods. Customers then pay the boleto before its expiration date
in one of several different methods, including at authorized agencies or banks,
ATMs, or online bank portals. You’ll receive payment confirmation after 1
business day, and funds will be available for payout 2 business days after
payment confirmation.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Brazil
- **Payment method family**

Cash-based payment method
- **Connect support**

Yes
- **Presentment currency**

BRL
- **Recurring Payments**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/boleto#disputed-payments)
- **Manual capture support**

No
- **Payment confirmation**

Customer-initiated
- **Payout timing**

2 business days
- **Refunds / Partial refunds**

[No / No](https://docs.stripe.com/payments/boleto#refunds)

## Payment flow

!

1. Selects Boleto at checkout

!

2. Receives payment codes and a confirmation number

!

3. Makes a payment at banks or online bank portals.

!

4. Receives notification that payment is complete

## Get started

You don’t have to integrate Boleto and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Boleto. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Boleto from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to
[manually configure Boleto as a
payment](https://docs.stripe.com/payments/boleto/accept-a-payment).

Check out the Boleto [sample on
GitHub](https://github.com/stripe-samples/accept-a-payment).

## Disputes

Generally Boleto payments can’t be disputed by the customer. However, in some
instances irregularities similar to disputes (by the bank) can occur (for
example, due to mishandling). In these cases, Stripe will need to reach out to
you for next steps.

## Refunds

Boleto payments can’t be refunded. You need to create a separate process to
credit customers who require a refund.

## Amount limits

The amount for a single Boleto must be at least R$5.00 and no more than
R$49,999.99.

## Links

- [No](https://docs.stripe.com/payments/boleto#disputed-payments)
- [No / No](https://docs.stripe.com/payments/boleto#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [manually configure Boleto as a
payment](https://docs.stripe.com/payments/boleto/accept-a-payment)
- [sample on GitHub](https://github.com/stripe-samples/accept-a-payment)