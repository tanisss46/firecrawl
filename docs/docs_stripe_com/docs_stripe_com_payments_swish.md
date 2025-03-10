# Swish paymentsPrivate preview

## Learn about Swish, a popular payment method in Sweden.

Swish is a [single-use](https://docs.stripe.com/payments/payment-methods#usage)
payment method used in Sweden. It allows customers to [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
payments using the Swish mobile app and the Swedish BankID mobile app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Sweden
- **Presentment currency**

SEK
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Real-time payments
- **Recurring payments**

No
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Connect support**

[Yes](https://docs.stripe.com/payments/swish#connect)
- **Dispute support**

No
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/swish#refunds)
- **Legal terms**

[Swish terms](https://stripe.com/legal/swish) apply, including the factoring
addendum

## Interested in getting access to Swish?

Due to changes to our Swish payments integration, we're pausing access to Swish
for new businesses. Enter your email address to be notified when access to Swish
becomes available again.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Payment flows

MobileDesktop

![The customer follows a mobile redirect flow to pay with
Swish.](https://d37ugbyn3rpeym.cloudfront.net/docs/payments/swish/mobile-payment-flow-2160.png)

The customer follows a mobile redirect flow to pay with Swish.

Customers pay with Swish by using one of the following methods:

- **Mobile**: Customers follow a mobile redirect from your website or mobile app
to the Swish app, where they authorize the payment, then return to your website
or mobile app.
- **Desktop**: Customers scan a QR code you present on your website using the
Swish app, which allows them to authorize the payment.

## Get started

Learn how to [manually configure Swish as a payment
method](https://docs.stripe.com/payments/swish/accept-a-payment).

You don’t have to integrate Swish and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Swish. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Swish from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

## Merchant of record

For Swish payments, Stripe operates as the merchant of record. Therefore,
Stripe’s name appears as the recipient of payments in the Swish app and as the
statement descriptor in the customer’s bank statements. Your business name
appears in the message field in the Swish app. The factoring addendum in the
[Swish terms](https://stripe.com/legal/swish) applies.

## Prohibited business categories

In addition to the industry and business categories listed in [Prohibited and
Restricted Businesses](https://stripe.com/restricted-businesses), the following
categories aren’t allowed to use Swish:

- Precious stones and metals, watches and jewelry
- Digital wallet top-ups

For more information about Swish eligibility for your account, navigate to your
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

## Refunds

You can refund Swish charges up to 365 days after the payment completes. Refunds
usually take a few minutes to complete. Swish supports full and partial refunds.
You can also issue multiple partial refunds up to the amount of the original
charge.

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
with Swish to process payments on behalf of a connected account. Connect users
can use Swish with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

## Links

- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [Yes](https://docs.stripe.com/payments/swish#connect)
- [Yes / Yes](https://docs.stripe.com/payments/swish#refunds)
- [Swish terms](https://stripe.com/legal/swish)
- [privacy policy](https://stripe.com/privacy)
- [manually configure Swish as a payment
method](https://docs.stripe.com/payments/swish/accept-a-payment)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Prohibited and Restricted
Businesses](https://stripe.com/restricted-businesses)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)