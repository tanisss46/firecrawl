# Satispay paymentsPrivate preview

## Learn how to accept payments with Satispay, a digital wallet popular with Italian customers.

[Satispay](https://satispay.com/) is a stored value wallet payment method
available to businesses in Italy. When customers select Satispay as their
payment method, Stripe redirects them to Satispay’s website to finish the
transaction. You’re paid immediately.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

IT Customers
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Wallets
- **Recurring payments**

No
- **Payout timing**

Standard
- **Connect support**

Yes
- **Dispute support**

Yes
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

Yes / Yes

## Interested in getting early access to Satispay?

To learn more or get early access, enter your email address below. We’ll work
with you to determine your eligibility and add you to the waitlist if you
qualify.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Payment flow

Below is a demonstration of the Satispay payment flow from your checkout page:

## Get started

You don’t have to integrate Satispay and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Satispay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Satispay from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

If your integration requires manually listing payment methods, learn how to
[manually configure Satispay as a
payment](https://docs.stripe.com/payments/satispay/accept-a-payment).

## Payment options

The minimum charge limit is 0.50 EUR.

The maximum charge limit is 999,999.99 EUR.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses
[restricted from using Stripe
overall](https://stripe.com/restricted-businesses), the following categories are
prohibited from using Satispay:

- Automobile Associations
- Betting/Casino Gambling
- Civic, Social, Fraternal Associations
- Direct Marketing - Catalog Merchant
- Financial Institutions
- Government Services (Not Elsewhere Classified)
- Other categories at the discretion of Satispay

## Disputes

Satispay has a claims process that allows transaction disputes. Customers can
open disputes for cases of suspected fraud, double payments, or a difference
between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to
receive [webhooks](https://docs.stripe.com/webhooks))

Stripe holds back the disputed amount from your balance until Satispay resolves
the dispute.

We request that you upload compelling evidence proving that you fulfilled the
purchase order [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond). This evidence
can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or
proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the
API](https://docs.stripe.com/disputes/api).

This information helps Satispay determine if a dispute is valid. Make sure the
evidence you provide contains as much detail as possible from what the customer
provided at checkout. You must submit the requested information within 12
calendar days. If Satispay resolves the dispute with you winning, we return the
disputed amount to your Stripe balance. If Satispay rules in favor of the
customer, the balance charge becomes permanent.

## Refunds

Satispay supports full and partial refunds. The refund period is up to 180 days
after the purchase. Refunds for Satispay payments are asynchronous and take up
to 5 minutes to complete. Stripe notifies you of the final refund status using
the `refund.updated` or `refund.failed`
[webhook](https://docs.stripe.com/webhooks) event. When a refund succeeds, the
[Refund](https://docs.stripe.com/api/refunds/object) object’s status transitions
to `succeeded`. If a refund fails, the `Refund` object’s status transitions to
`failed` and we return the amount to your Stripe balance. You’ll then need to
arrange an alternative way of providing your customer with a refund.

## Connect

If you use [Connect](https://docs.stripe.com/connect), you must consider the
following before you enable and use Satispay.

### Request Satispay capabilities for your connected accounts

Set the `satispay_payments` capability to `active` on your platform account, and
on any connected accounts you want to enable Satispay for. You can also [request
more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges) of Connect payments
might change the default statement descriptor and the merchant name that appears
on the customer’s banking application and confirmation emails.

Charge typeDescriptor taken fromDirectConnected
accountDestinationPlatformSeparate charge and transferPlatformDestination (with
`on_behalf_of`)Connected accountSeparate charge and transfer (with
`on_behalf_of`)Connected account
## Supported currencies

You can create Satispay payments in the currencies that map to your country. The
default local currency for Satispay is `eur` and customers also see their
purchase amount in `eur`.

CurrencyCountry`eur`Italy

## Links

- [Satispay](https://satispay.com/)
- [privacy policy](https://stripe.com/privacy)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure Satispay as a
payment](https://docs.stripe.com/payments/satispay/accept-a-payment)
- [restricted from using Stripe
overall](https://stripe.com/restricted-businesses)
- [webhooks](https://docs.stripe.com/webhooks)
- [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond)
- [respond to disputes using the API](https://docs.stripe.com/disputes/api)
- [Refund](https://docs.stripe.com/api/refunds/object)
- [Connect](https://docs.stripe.com/connect)
- [request more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
- [charge type](https://docs.stripe.com/connect/charges)