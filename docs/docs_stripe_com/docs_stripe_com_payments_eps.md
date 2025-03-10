# EPS payments

## Learn about EPS, a common payment method in Austria.

EPS is an Austria-based payment method that lets customers complete transactions
online using their bank credentials. All Austrian banks support EPS, and over
80% of Austrian online retailers accept it.

EPS redirects customers to their bank’s website to [authenticate a
payment](https://docs.stripe.com/payments/payment-methods#customer-actions). You
receive [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
about the success or failure of a payment.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Austria
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-authenticated
- **Payment method family**

Authenticated bank debit
- **Recurring payments**

No
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/eps#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/eps#refunds)

## Payment flow

!

Customer selects EPS at checkout

!

Customer chooses their bank and is redirected to that bank’s login page

!

Customer enters account credentials

!

Customer completes authorization process (with scanner or SMS)

!

Customer is notified that payment is complete

!

(Optional) Customer returns back to the business’s site for payment confirmation

## Get started

You don’t have to integrate EPS and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
EPS. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add EPS from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If your integration requires manually listing payment methods, learn how to
[manually configure EPS as a
payment](https://docs.stripe.com/payments/eps/accept-a-payment).

## Disputes

The risk of fraud or unrecognized payments is low because the customer must
authenticate the payment with their bank. As a result, you won’t have disputes
that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

EPS payments can be refunded up to 180 days after the original payment date.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [authenticate a
payment](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [No](https://docs.stripe.com/payments/eps#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/eps#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure EPS as a
payment](https://docs.stripe.com/payments/eps/accept-a-payment)