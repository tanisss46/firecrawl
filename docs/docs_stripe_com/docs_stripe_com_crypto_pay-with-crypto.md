# Pay with CryptoPublic preview

## Accept stablecoin payments that settle as fiat in your Stripe balance.

Pay with Crypto lets you accept stablecoin payments that settle as fiat in your
Stripe balance. You can accept USDC payments on Ethereum, Solana, and Polygon
without the complexity of holding or converting crypto to fiat yourself. We
[charge](https://docs.stripe.com/crypto/pay-with-crypto#feature-set) 1.5% of the
transaction amount (in USD).

Pay with Crypto works with
[Checkout](https://docs.stripe.com/payments/checkout),
[Elements](https://docs.stripe.com/payments/elements), or can be directly
integrated through the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents). When integrated, the
option to pay with **Crypto** appears that redirects your customers to a page
hosted by *crypto.link.com* to complete their payment. There, they can connect
their wallet and save and reuse their account using
[Link](https://docs.stripe.com/payments/link). Before you get started, see our
[demo](https://buy.stripe.com/test_28o4ig0SY9Xq8co3cc) showcasing Pay with
Crypto in action.

## Overview

The following example assumes you’ve added Pay with Crypto to the [Payment
Element](https://docs.stripe.com/payments/payment-element):

- After you set up Pay with Crypto, the option to select **Crypto** as a payment
method appears in your checkout form.
- When your customer clicks this option, they’re redirected to a page hosted by
*crypto.link.com*, where they can:

- Confirm the amount they need to pay.
- Connect the wallet they want to pay with.
- Confirm the payment by signing the transaction that transfers the USDC from
their wallet.
- After Stripe confirms the payment, the customer sees that the transaction is
complete. And just like any other Stripe transaction, you see an update to your
Stripe balance.

![Pay with
Crypto](https://b.stripecdn.com/docs-statics-srv/assets/hypernian-pay-with-crypto.3cdcc246f271a82bb6a9368cd4d8ac72.png)

Add crypto as a payment option to your checkout page

## Feature set

The following table contains the feature snapshot for Pay with Crypto:

AvailabilityUS-based businessesFeatures- Implementable through Stripe’s Payment
Element, Checkout, or directly through the Payment Intents API.
- Zero dispute liability for integrating businesses.
- Returning customers get one-click checkout using Link.
Recurring
payments[Supported](https://docs.stripe.com/crypto/pay-with-crypto#billing) with
`send_invoice` [collection
method](https://docs.stripe.com/billing/collection-method) subscriptions.[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)Not
supportedCurrencies- USDC on Ethereum, Solana, and Polygon
- USDP on Ethereum and Solana
End customersGlobal (except for sanctioned countries)TransactionsTransaction
limits on the end customer are 10,000 USD per transaction and 100,000 USD per
month.Pricing1.5% of the transaction amount (in USD)
#### Public preview

Pay with Crypto is a new feature. If you have any questions or feedback, contact
[pay-with-crypto@stripe.com](mailto:pay-with-crypto@stripe.com).

## Onboarding

Before you can enable Pay with Crypto:

- [Activate](https://docs.stripe.com/get-started/account/activate) a Stripe
account, if you haven’t already, ensuring that we’ve approved you to process
payments.
- Go to your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods), and request
the **Crypto** payment method.
- Fill out your business’s information and accept the terms on the page.
- After we review your information and approve you, the **Crypto** payment
method becomes active in the Dashboard. If the payment method appears as
pending, we’re still reviewing your candidacy and might reach out to you for
more details.

Consider the following before integrating Pay with Crypto:

- **Refunds:** To issue a refund, follow the [refund
flow](https://docs.stripe.com/refunds). For crypto payments, the refund goes
back as stablecoins in the customer’s original wallet.
- **Holding crypto:** Transactions settle in USD to your Stripe balance.
- **Settlement currencies:** We currently only support USD settlement.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create Crypto supported
[invoices](https://docs.stripe.com/api/invoices) and
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating). Crypto
invoices and subscriptions only support the `send_invoice` [collection
method](https://docs.stripe.com/billing/collection-method).

## Connect support

The following [Connect charge](https://docs.stripe.com/connect/charges) types,
typically used by Connect platforms, are available to businesses using Pay with
Crypto. Connected accounts must directly enable **Crypto** in their [payment
method settings](https://dashboard.stripe.com/settings/payment_methods) before
they can accept crypto payments. You can’t enable crypto payments through the
[Accounts API](https://docs.stripe.com/api/accounts/) or [Capabilities
API](https://docs.stripe.com/api/capabilities).

Destination chargesSeparate charges and transfersDirect chargeson_behalf_of

## Links

- [Checkout](https://docs.stripe.com/payments/checkout)
- [Elements](https://docs.stripe.com/payments/elements)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Link](https://docs.stripe.com/payments/link)
- [demo](https://buy.stripe.com/test_28o4ig0SY9Xq8co3cc)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Supported](https://docs.stripe.com/crypto/pay-with-crypto#billing)
- [collection method](https://docs.stripe.com/billing/collection-method)
- [Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Activate](https://docs.stripe.com/get-started/account/activate)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [refund flow](https://docs.stripe.com/refunds)
- [Stripe Billing](https://stripe.com/billing)
- [invoices](https://docs.stripe.com/api/invoices)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Connect charge](https://docs.stripe.com/connect/charges)
- [Accounts API](https://docs.stripe.com/api/accounts/)
- [Capabilities API](https://docs.stripe.com/api/capabilities)