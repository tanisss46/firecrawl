# TWINT payments

## Learn about TWINT, a popular payment method in Switzerland.

TWINT is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method used in Switzerland. It allows customers to [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
payments using an approved TWINT mobile app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Switzerland
- **Presentment currency**

CHF
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Bank redirects
- **Recurring payments**

No
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Connect support**

[Yes](https://docs.stripe.com/payments/twint#connect)
- **Dispute support**

[Yes](https://docs.stripe.com/payments/twint#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/twint#refunds)
- **Maximum Amount** 5000.00 CHF

## Payment flows

Customers pay with TWINT by using one of the following methods:

- **Mobile**: Customers follow a mobile redirect from your website or mobile app
to a TWINT app, where they authorize the payment, then return to your website or
mobile app.
- **Desktop**: Customers scan a QR code you present on your website using a
TWINT app, which allows them to authorize the payment.

## Get started

You don’t have to integrate TWINT and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
TWINT. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add TWINT from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

If you prefer to manually list payment methods, learn how to [manually configure
TWINT as a payment
method](https://docs.stripe.com/payments/twint/accept-a-payment).

## Refunds

You can refund TWINT charges up to 180 days after the payment completes. Refunds
usually take a few minutes to complete. TWINT supports full and partial refunds.
You can also issue multiple partial refunds up to the amount of the original
charge.

## Disputes

Buyers can dispute TWINT transactions by filing a complaint with their bank.
TWINT disputes are rare, with 25-50 disputes recorded for every 1,000,000
transactions.

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
with TWINT to process payments on behalf of a connected account. Connect users
can use TWINT with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

### Enable TWINT for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable TWINT in their
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) in the
Dashboard. To check which accounts have enabled TWINT, use the `capabilities`
hash in our [accounts webhooks or
APIs](https://docs.stripe.com/api/accounts/object#account_object-capabilities-twint_payments)
to see if the `twint_payments` capability is set to `active`.

### Enable TWINT for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Follow the instructions to [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities). The name of
your connected account is the name customers see during checkout and in the
TWINT app.

## Links

- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [Yes](https://docs.stripe.com/payments/twint#connect)
- [Yes](https://docs.stripe.com/payments/twint#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/twint#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure TWINT as a payment
method](https://docs.stripe.com/payments/twint/accept-a-payment)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [accounts webhooks or
APIs](https://docs.stripe.com/api/accounts/object#account_object-capabilities-twint_payments)
- [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities)