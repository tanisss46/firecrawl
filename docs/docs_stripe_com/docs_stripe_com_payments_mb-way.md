# MB WAY paymentsInvite only

## Learn about MB WAY, a digital wallet payment method in Portugal.

MB WAY is a digital wallet payment method in Portugal. When paying with MB WAY,
customers initiate payments using their phone number, and [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions) them
using their MB WAY app.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
of whether the payment succeeded or failed.

#### Note

MB WAY supports international phone numbers, but the majority of customers use a
Portuguese phone number starting with +351. You can test your integration in a
[sandbox](https://docs.stripe.com/sandboxes) using [test phone
numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment#web-test-integration).

Payment method propertiesCountry availabilityProduct support- **Customer
locations**

Portugal
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Wallet
- **Recurring payments**

No
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Connect support**

[Yes](https://docs.stripe.com/payments/mb-way#connect)
- **Dispute support**

Yes
- **Manual capture support**

No
- **Refunds / Partial refunds**

Yes / Yes

## Interested in getting early access to MB WAY?

To learn more or get early access, enter your email address below. We’ll work
with you to determine your eligibility, and from there, add you to the waitlist.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Payment flows

Customers pay with MB WAY using a phone number linked to their MB WAY app. After
providing their phone number, customers receive a push notification in their MB
WAY app, authorize the payment, then return to your website.

## Get started

Learn how to [configure MB WAY as a payment
method](https://docs.stripe.com/payments/mb-way/accept-a-payment).

You don’t have to integrate MB WAY and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable MB
WAY. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add MB WAY from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

## Refunds

You can refund MB WAY charges up to 365 days after the payment completes.
Refunds usually take a few minutes to complete. MB WAY supports full and partial
refunds. You can also issue multiple partial refunds up to the amount of the
original charge.

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
with MB WAY to process payments on behalf of a connected account. Connect users
can use MB WAY with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

### Enable MB WAY for connected accounts that use the Stripe Dashboard

Reach out to your Stripe representative to enable MB WAY for connected accounts
that use the Stripe Dashboard or [email us](mailto:mb-way-support@stripe.com).
These accounts must onboard manually.

### Enable MB WAY for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

To onboard connected accounts that use the Express Dashboard or a dashboard that
isn’t hosted by Stripe, request the `mb_way_payments` capability using the
[Capabilities API](https://docs.stripe.com/api/capabilities). For more details,
follow the instructions to [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities).

## Links

- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [sandbox](https://docs.stripe.com/sandboxes)
- [test phone
numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment#web-test-integration)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [Yes](https://docs.stripe.com/payments/mb-way#connect)
- [privacy policy](https://stripe.com/privacy)
- [configure MB WAY as a payment
method](https://docs.stripe.com/payments/mb-way/accept-a-payment)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Capabilities API](https://docs.stripe.com/api/capabilities)
- [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities)