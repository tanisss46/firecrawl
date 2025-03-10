# Revolut Pay payments

## Learn about Revolut Pay, a digital wallet payment method used in the United Kingdom and the European Union.

Revolut Pay, developed by
[Revolut](https://www.revolut.com/business/revolut-pay/), a global finance app,
is a digital wallet payment method. Revolut Pay uses the customer’s stored
balance or cards to fund the payment, and offers the option for non-Revolut
customers to save their details after their first purchase.

When customers select Revolut Pay as their payment method, Stripe redirects them
to Revolut Pay’s website, where they have to authenticate with their account
details or checkout as a first time user. After authenticating, Revolut Pay
redirects customers back to your website.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

UK and EU
- **Presentment currency**

EUR, GBP
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Wallet
- **Recurring payments**

Yes
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[Yes](https://docs.stripe.com/payments/revolut-pay#disputed-payments)
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/revolut-pay#refunds)

## Payment flow

Below is a demonstration of the Revolut Pay payment flow from your checkout
page:

## Get started

You don’t have to integrate Revolut Pay and other payment methods individually.
If you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Revolut Pay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Revolut Pay from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to
[manually configure Revolut Pay as a
payment](https://docs.stripe.com/payments/revolut-pay/accept-a-payment).

Check out the Revolut Pay [sample on
GitHub](https://github.com/stripe-samples/accept-a-payment).

## Refunds

Revolut Pay supports full and partial refunds. The refund period is up to 180
days after the purchase. Refunds for Revolut Pay payments are asynchronous and
take up to 5 minutes to complete. We notify you of the final refund status using
the `refund.updated` or `refund.failed`
[webhook](https://docs.stripe.com/webhooks) event. When a refund succeeds, the
status of the [Refund object](https://docs.stripe.com/api/refunds/object)
transitions to `succeeded`. If a refund fails, the status of the Refund object
transitions to `failed` and we return the amount to your Stripe balance. You
then need to arrange an alternative way of providing a refund.

## Disputes

Customers must authenticate Revolut Pay payments by logging into their Revolut
account. This requirement helps reduce the risk of fraud or unrecognized
payments. With [Revolut’s Buyer Protection
Policy](https://www.revolut.com/legal/buyer-protection-policy/), customers can
file a dispute, which can result in a chargeback and funds being withdrawn from
your Stripe account.

Customers have up to 120 calendar days from the date of purchase to file a
dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the
Stripe Dashboard, and an API `charge.dispute.created` event (if your integration
is set up to receive [webhooks](https://docs.stripe.com/webhooks)).
- Stripe holds back the disputed amount from your balance until Revolut resolves
the dispute.
- Stripe requests that you upload compelling evidence that you fulfilled the
purchase order [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond). This evidence
can include:

- A received return confirmation (for shipped goods returned from the customer
to you)
- The tracking ID
- The shipping date
- A record of purchase for intangible goods, such as IP address or email receipt
- A record of purchase for services or physical goods, such as phone number or
proof of receipt

This information helps Revolut determine if a dispute is valid or if they need
to reject it. Make sure the evidence you provide contains as much detail as
possible from what the customer provided at checkout. You must submit the
requested information within 14 calendar days. Revolut makes a decision within
35 calendar days of evidence submission. If Revolut resolves the dispute in your
favor, Stripe returns the disputed amount to your Stripe balance. If Revolut
rules in favor of the customer, the balance charge becomes permanent.

#### Note

If you prefer to handle disputes programmatically, you can [respond to disputes
using the API](https://docs.stripe.com/disputes/api).

## Supported currencies

You can create Revolut Pay payments in the currencies that map to your country.
Currently, we support `gbp` and `eur`. The default local currency for Revolut
Pay UK customers is `gbp` and for other EU customers it’s `eur`.

CurrencyCountry`gbp`United Kingdom`eur`Austria, Belgium, Bulgaria, Croatia,
Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece,
Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta,
Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain,
Sweden

## Links

- [Revolut](https://www.revolut.com/business/revolut-pay/)
- [Yes](https://docs.stripe.com/payments/revolut-pay#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/revolut-pay#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [manually configure Revolut Pay as a
payment](https://docs.stripe.com/payments/revolut-pay/accept-a-payment)
- [sample on GitHub](https://github.com/stripe-samples/accept-a-payment)
- [webhook](https://docs.stripe.com/webhooks)
- [Refund object](https://docs.stripe.com/api/refunds/object)
- [Revolut’s Buyer Protection
Policy](https://www.revolut.com/legal/buyer-protection-policy/)
- [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond)
- [respond to disputes using the API](https://docs.stripe.com/disputes/api)