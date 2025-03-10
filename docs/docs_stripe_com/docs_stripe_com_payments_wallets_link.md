# Link

## Learn about Link's core features.

[Link](https://docs.stripe.com/payments/link) allows your customers to select a
saved payment method at checkout instead of entering payment information. Your
customers can save their credit cards, debit cards, or US bank accounts for
faster checkout at any Link-enabled business. Link also lets you accept [Instant
Bank Payments](https://docs.stripe.com/payments/link/instant-bank-payments). All
Link transactions confirm immediately, and successful payments settle to your
Stripe balance on the same timeline as card payments, regardless of the payment
method that funds the payment.

Customers can make changes to their account, view their purchase history, or
reach out to the Link customer support team by visiting
[link.com](https://www.link.com/). For information about how your payment
integration affects Link, see [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations).

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Worldwide except India
- **Presentment currency**

See [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
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

[Yes](https://docs.stripe.com/payments/wallets/link#disputes)
- **Manual capture support**

Yes
- **Refunds or partial refunds**

[Yes and Yes](https://docs.stripe.com/payments/wallets/link#refunds)

## Payment flow

The Link payment flow varies depending on the Stripe product that you’re using.
To learn more, see [Faster checkout with
link](https://docs.stripe.com/payments/link).

## Get started

For eligible transactions, Stripe automatically displays Link when it’s enabled
under **Wallets** in your [payment method
settings](https://dashboard.stripe.com/settings/payment_methods). All Link
transactions confirm immediately, and successful payments settle to your Stripe
balance on the same timeline as card payments, regardless of the payment method
that funds the payment.

You can integrate Link in two ways: as a payment method, or by incorporating it
into a card-specific integration. Stripe recommends using Link as a payment
method, because it’s a simpler integration and works with [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
out of the box. However, if you only accept card payments, or you require access
to card details such as the brand or last 4 digits, add Link to your card
integration.

Both Link integrations accept all types of payment methods supported by Link,
including credit cards, debit cards, and [Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments).

If you integrate [Link as a payment
method](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-payment-method),
then each Link transaction has a [PaymentMethod
object](https://docs.stripe.com/api/payment_methods/object) with a
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
of `link` and no `wallet` hash.

If you incorporate [Link into a card-specific
integration](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-card-integrations),
then each Link transaction has a [PaymentMethod
object](https://docs.stripe.com/api/payment_methods/object) with a
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
of `card` and a `card.wallet` hash with a
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-wallet-type)
of `link`.

## Refunds

Link supports full and partial refunds. You can initiate refunds through the
Stripe Dashboard or API, similar to other payment methods. The refund process is
typically completed within 5-10 business days, depending on your bank.

## Disputes

[Disputes](https://docs.stripe.com/disputes) for Link payments follow a similar
process to card disputes. You can respond to disputes through the Stripe
Dashboard or API. The dispute process and timelines might vary, depending on
whether the saved payment method used for the transaction was a card or bank
account.

#### Note

If you prefer to handle disputes programmatically, you can [respond to
disputes](https://docs.stripe.com/disputes/api) using the API.

## Supported currencies

Link supports all [currencies](https://docs.stripe.com/currencies) that Stripe
supports for card payments.

## See also

- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)
- [Link with Invoicing](https://docs.stripe.com/payments/link/invoicing)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)
- [link.com](https://www.link.com)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)
- [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [payment method
settings](https://dashboard.stripe.com/settings/payment_methods)
- [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Link as a payment
method](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-payment-method)
- [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object)
-
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
- [Link into a card-specific
integration](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-card-integrations)
-
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-wallet-type)
- [Disputes](https://docs.stripe.com/disputes)
- [respond to disputes](https://docs.stripe.com/disputes/api)
- [currencies](https://docs.stripe.com/currencies)
- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)
- [Link with Invoicing](https://docs.stripe.com/payments/link/invoicing)