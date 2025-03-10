# GrabPay payments

## Learn about GrabPay, a common payment method in Southeast Asia.

GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/pay/).
GrabPay is a digital wallet. Customers maintain a balance in their wallets that
they pay out with.

To pay with GrabPay, customers are redirected to GrabPay’s website, where they
have to authenticate the transaction using a one-time password. After
authenticating, customers are redirected back to your website.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Singapore, Malaysia
- **Presentment currency**

SGD, MYR
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Wallet
- **Recurring payments**

No
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/grabpay#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/grabpay#refunds)

## Payment flow

Below is a demonstration of the GrabPay payment flow from your checkout page:

## Get started

You don’t have to integrate GrabPay and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
GrabPay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add GrabPay from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If your integration requires manually listing payment methods, learn how to
[manually configure GrabPay as a
payment](https://docs.stripe.com/payments/grabpay/accept-a-payment).

Check out the GrabPay [sample on
GitHub](https://github.com/stripe-samples/accept-a-payment).

## Refunds

GrabPay payments can be refunded up to 90 days after the original payment.
Refunds for GrabPay payments are asynchronous and take up to 5 minutes to
complete. We will notify you of the final refund status using the
`refund.updated` or `refund.failed` [webhook](https://docs.stripe.com/webhooks)
event. When a refund succeeds, the
[Refund](https://docs.stripe.com/api/refunds/object) object’s status transitions
to `succeeded`. If a refund fails, the Refund object’s status transitions to
`failed` and we return the amount to your Stripe balance. You then need to
arrange an alternative way of providing your customer with a refund.

## Disputes

GrabPay payments have a low risk of fraud or unrecognized payments because the
customer must authenticate the payment with Grab. Therefore, there is no dispute
process that can result in a chargeback and funds being withdrawn from your
Stripe account.

## Branding guidelines

Use the [branding
guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf)
provided by GrabPay when building your checkout page. Assets such as logos and
buttons are available for download [as a zip
file](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip).

## Links

- [Grab](https://www.grab.com/sg/pay/)
- [No](https://docs.stripe.com/payments/grabpay#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/grabpay#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure GrabPay as a
payment](https://docs.stripe.com/payments/grabpay/accept-a-payment)
- [sample on GitHub](https://github.com/stripe-samples/accept-a-payment)
- [webhook](https://docs.stripe.com/webhooks)
- [Refund](https://docs.stripe.com/api/refunds/object)
- [branding
guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf)
- [as a zip
file](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip)