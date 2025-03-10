# iDEAL payments

## Learn about iDEAL, a common payment method in the Netherlands.

iDEAL is a Netherlands-based payment method that allows customers to complete
transactions online using their bank credentials. All major Dutch banks are
members of Currence, the scheme that operates iDEAL, making it the most popular
online payment method in the Netherlands with a share of online transactions
close to 55%.

iDEAL redirects customers to their online banking environment to authenticate a
payment using a [second factor of
authentication](https://docs.stripe.com/payments/payment-methods#customer-actions)
and there is [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
about the success or failure of a payment. The exact customer experience depends
on their bank.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Netherlands
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Authenticated bank transfer
- **Recurring payments**

with [SEPA Direct Debit](https://docs.stripe.com/billing/subscriptions/ideal)
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/ideal#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/ideal#refunds)

## Payment flow

Below is a demonstration of the iDEAL payment flow from your checkout page:

## Get started

You don’t have to integrate iDEAL and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
iDEAL. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add iDEAL from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If you prefer to manually list payment methods or want to save iDEAL details for
future payments, see the following guides:

- [Manually configure iDEAL as a payment
method](https://docs.stripe.com/payments/ideal/accept-a-payment)
- [Save iDEAL details for future
payments](https://docs.stripe.com/payments/ideal/set-up-payment)

Check out the iDEAL [sample on
GitHub](https://github.com/stripe-samples/accept-a-payment).

## Disputes

Customers can’t dispute iDEAL payments with their bank. Encourage your customers
to reach out to you directly with any concerns.

## Refunds

iDEAL payments can be refunded up to 180 days after the original payment.

## Website requirements

If you’re based in the Netherlands, your website must comply with iDEAL scheme
rules by clearly displaying your KVK (company registration) number with the
Chamber of Commerce. If you aren’t based in the Netherlands, your website must
display your registration number with the equivalent local official body.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [second factor of
authentication](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [SEPA Direct Debit](https://docs.stripe.com/billing/subscriptions/ideal)
- [No](https://docs.stripe.com/payments/ideal#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/ideal#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Manually configure iDEAL as a payment
method](https://docs.stripe.com/payments/ideal/accept-a-payment)
- [Save iDEAL details for future
payments](https://docs.stripe.com/payments/ideal/set-up-payment)
- [sample on GitHub](https://github.com/stripe-samples/accept-a-payment)