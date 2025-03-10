# PayNow payments

## Learn about PayNow, a popular payment method in Singapore.

PayNow is a Singapore based payment method that allows customers to make a
payment using their preferred app from participating banks and participating
non-bank financial institutions.

Customers see a QR code when checking out with PayNow. They complete the payment
by scanning it using [a participating
app](https://www.abs.org.sg/consumer-banking/pay-now). You receive confirmation
from Stripe instantly when they complete the payment.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Singapore
- **Presentment currency**

SGD
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Real-time payments
- **Billing support**

[Yes](https://docs.stripe.com/payments/paynow#billing)
- **Payout timing**

T+1 availability
- **Connect support**

Yes
- **Dispute support**

[Not applicable](https://docs.stripe.com/payments/paynow#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/paynow#refunds)
- **Pricing**

1.3

## Get started

You don’t have to integrate PayNow and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
PayNow. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add PayNow from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to
[manually configure PayNow as a
payment](https://docs.stripe.com/payments/paynow/accept-a-payment).

## Refunds

You can refund PayNow payments up to 90 days after the original payment. Refunds
for PayNow payments are asynchronous and Stripe notifies you of the final refund
status using the `refund.updated` or `refund.failed`
[webhook](https://docs.stripe.com/webhooks) event. When a refund succeeds, the
status of the [Refund](https://docs.stripe.com/api/refunds/object) object
transitions to `succeeded`.

If a refund fails, the status of the Refund object transitions to `failed` and
Stripe returns the amount to your Stripe balance. At this point, you need to
arrange an alternative way of providing your customer with a refund.

## Statement descriptors

Customized statement descriptors aren’t supported by PayNow, the value specified
in the
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)
is ignored. Stripe’s company name (`STRIPE PAYMENTS SINGAPORE PTE. LTD.`) is
shown when your customers complete payments on their mobile app. It’s also shown
on bank statements along with the amount and a Stripe-generated reference code.

## Repeated payments

To prevent your customers from being charged multiple times, after your customer
successfully completes a transaction, any subsequent attempts to pay using the
same QR code are rejected. The rejection behavior depends on the bank and
payment app used by the customer to attempt the transaction. If your customers
contact you about repeated payments, you can advise them to check for text
messages or notifications from their bank or payment app, which will show that
the payment attempt was rejected.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create PayNow supported
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
[invoices](https://docs.stripe.com/api/invoices).

PayNow payments don’t support [automatically
charging](https://docs.stripe.com/invoicing/automatic-charging) invoices. You
need to configure invoices and subscriptions with `send_invoice`
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).

## Payout timing

By default, it takes 1 day from the time of the transaction for the funds to be
available in your Stripe balance. Stripe pays out available funds to your bank
account according to the payout schedule set on your Stripe account.

For example, if the payment was made on Wednesday, the funds are available in
your Stripe balance on Thursday. If you’re on an automatic daily payout
schedule, the funds are paid out on Thursday. If you’re on a weekly (Monday)
payout schedule, the funds are paid out on the coming Monday.

## Disputes

PayNow payments have a low risk of fraud or unrecognized payments because the
customer must authenticate the payment through participating apps. As a result,
there’s no dispute process that can result in a chargeback and funds being
withdrawn from your Stripe account.

## Prohibited business categories

In addition to the categories of [businesses restricted from using Stripe
overall](https://stripe.com/restricted-businesses), the following categories are
specifically prohibited from using PayNow:

- Petroleum and Petroleum Products
- Fuel Dealers
- Service Stations
- Automated Fuel Dispensers

## Links

- [a participating app](https://www.abs.org.sg/consumer-banking/pay-now)
- [Yes](https://docs.stripe.com/payments/paynow#billing)
- [Not applicable](https://docs.stripe.com/payments/paynow#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/paynow#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [manually configure PayNow as a
payment](https://docs.stripe.com/payments/paynow/accept-a-payment)
- [webhook](https://docs.stripe.com/webhooks)
- [Refund](https://docs.stripe.com/api/refunds/object)
-
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)
- [Stripe Billing](https://stripe.com/billing)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoices](https://docs.stripe.com/api/invoices)
- [automatically charging](https://docs.stripe.com/invoicing/automatic-charging)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [businesses restricted from using Stripe
overall](https://stripe.com/restricted-businesses)