# giropay paymentsDeprecated

## Learn about giropay, a common payment method in Germany.

#### Warning

Our financial partners are deprecating Giropay. No new business onboarding or
transactions will be possible after June 30, 2024. Read our [support
page](https://support.stripe.com/questions/june-2024-update-to-giropays-availability)
for more details.

giropay is a German payment method based on online banking, introduced in 2006.
It allows customers to complete transactions online using their online banking
environment, with funds debited from their bank account. Depending on their
bank, customers confirm payments on giropay using a second factor of
authentication or a PIN. giropay accounts for 10% of online checkouts in
Germany.

giropay redirects customers to their website to [authenticate a
payment](https://docs.stripe.com/payments/payment-methods#customer-actions) and
there is [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
about the success or failure of a payment.

Payment method propertiesCountry availability- **Customer locations**

Germany
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

No
- **Refunds / Partial refunds**

Yes / yes

## Payment flow

This demo shows the customer experience when using Giropay.

## Get started

You don’t have to integrate giropay and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
giropay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add giropay from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If your integration requires manually listing payment methods, learn how to
[manually configure giropay as a
payment](https://docs.stripe.com/payments/giropay/accept-a-payment).

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must
authenticate the payment with their bank. As a result, you won’t have disputes
that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

giropay payments can be refunded up to 180 days after the original payment date.

## Links

- [support
page](https://support.stripe.com/questions/june-2024-update-to-giropays-availability)
- [authenticate a
payment](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure giropay as a
payment](https://docs.stripe.com/payments/giropay/accept-a-payment)