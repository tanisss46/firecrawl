# PromptPay payments

## Learn about PromptPay, a popular payment method in Thailand.

PromptPay is a Thailand based payment method that allows customers to make a
payment using their preferred app from participating banks.

Customers see a QR code when checking out with PromptPay. They complete the
payment by scanning it using a Thailand bank app. You receive confirmation from
Stripe instantly when they complete the payment.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Thailand
- **Presentment currency**

THB
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Real-time payments
- **Billing support**

Yes
- **Connect support**

Yes
- **Dispute support**

[Not applicable](https://docs.stripe.com/payments/promptpay#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/promptpay#refunds)

## Payment flow

!

1. Selects PromptPay at checkout

!

2. Scans displayed QR code with preferred app

!

3. Authorizes payment

!

4. Gets notification that payment is complete

## Get started

You don’t have to integrate PromptPay and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
PromptPay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add PromptPay from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

#### Note

Invoices and Subscriptions only support the `send_invoice` [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method).

If you prefer to manually list payment methods, learn how to [manually configure
PromptPay as a
payment](https://docs.stripe.com/payments/promptpay/accept-a-payment).

## Refunds

Stripe supports refunds of PromptPay payments either through the
[Dashboard](https://dashboard.stripe.com/payments) or
[API](https://docs.stripe.com/api#create_refund). To complete a refund, your
customer must tell us where to return the funds. Stripe automatically contacts
the customer at the email address provided at time of PaymentIntent confirmation
and requests refund account information from them. Your customer must provide
the account number of the bank account from which the payment was made,
otherwise the refund might fail. We process the refund automatically after
receiving the refund account information.

## Statement descriptors

PromptPay doesn’t support customized statement descriptors, and it ignores the
value specified in the
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor).
Customers see the Stripe company name (`STRIPE PAYMENTS (THAILAND) LTD`) when
they complete payments on their banking app. They also see it on bank
statements, along with the amount and a unique reference code.

## Repeated payments

After a customer successfully completes a transaction, any attempt to use the
same QR code again can result in having the funds deducted from their bank
account. If Stripe receives any excess funds from your customers, we reimburse
them to your account balance and notify you. You’ll need to issue the refund to
your customers outside of Stripe (for example, with a check, cash, or store
credit).

## Disputes

PromptPay payments have a low risk of fraud or unrecognized payments because the
customer must authenticate the payment through banking apps. However, cases of
irregularities similar to disputes, or other unexpected or repeated payments can
occur. Stripe reviews these cases, and might contact you or take other action if
required.

## Links

- [Not applicable](https://docs.stripe.com/payments/promptpay#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/promptpay#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [collection
method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [manually configure PromptPay as a
payment](https://docs.stripe.com/payments/promptpay/accept-a-payment)
- [Dashboard](https://dashboard.stripe.com/payments)
- [API](https://docs.stripe.com/api#create_refund)
-
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)