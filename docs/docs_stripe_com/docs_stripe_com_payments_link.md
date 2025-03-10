# Faster checkout with Link

## Let your customers check out faster with Link.

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

#### Country availability

Link isn’t available in India. In Brazil and Thailand, the [Payment
Element](https://docs.stripe.com/payments/payment-element) doesn’t support Link.

![Add Link to your prebuilt checkout
page](https://b.stripecdn.com/docs-statics-srv/assets/link-in-checkout.2eb9f8d06da3dca74af9b81fa7524049.png)

Add Link to your prebuilt checkout page

## Link authentication

Here’s how Link authenticates existing customers:

- Link automatically detects if a customer is enrolled by using their email
address, phone number, or browser cookie.
- The customer receives a one-time passcode to authenticate their session.
- After authentication succeeds, Link autofills their card or bank payment
details and shipping information.

After a customer enrolls with Link, they can add backup payment methods and
change shipping addresses.

Link works with [Checkout](https://docs.stripe.com/payments/checkout), [Payment
Links](https://docs.stripe.com/payment-links), [Web
Elements](https://docs.stripe.com/payments/elements), [Mobile
Elements](https://docs.stripe.com/payments/link/mobile-payment-element-link),
and [Invoicing](https://docs.stripe.com/invoicing). To accept payments using
Link, go to your [payment method
settings](https://dashboard.stripe.com/settings/payment_methods).

## Link on no-code surfaces

[Link with CheckoutUse Link in your prebuilt checkout page, allowing your
customers to securely save and reuse their payment
information.](https://docs.stripe.com/payments/link/checkout-link)[Link with
InvoicingEnable Link in the Hosted Invoice
Page.](https://docs.stripe.com/payments/link/invoicing)
## Link with Elements

[Link in the Payment ElementTrigger Link in the Payment Element whenever a
customer selects a supported payment
method.](https://docs.stripe.com/payments/link/payment-element-link)[Link in the
Express Checkout ElementDisplay Link alongside Apple Pay, Google Pay, and PayPal
using the Express Checkout
Element.](https://docs.stripe.com/payments/link/express-checkout-element-link)[Link
in the Mobile Payment ElementAdd Link to your native iOS, Android, and React
Native apps.](https://docs.stripe.com/payments/link/mobile-payment-element-link)
## Link integrations

[Link in different payment integrationsLearn about using Link with dynamic
payment methods and other
integrations.](https://docs.stripe.com/payments/link/link-payment-integrations)[Build
a custom checkout page that includes LinkUse the Payment Intents API with the
Link Authentication Element or Payment Element to create a Link-enabled custom
checkout
page.](https://docs.stripe.com/payments/link/add-link-elements-integration)[Set
up future payments using Elements and LinkSave your Link customers’ details and
charge them later.](https://docs.stripe.com/payments/link/save-and-reuse)
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
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Web Elements](https://docs.stripe.com/payments/elements)
- [Mobile
Elements](https://docs.stripe.com/payments/link/mobile-payment-element-link)
- [Invoicing](https://docs.stripe.com/invoicing)
- [payment method
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Link with CheckoutUse Link in your prebuilt checkout page, allowing your
customers to securely save and reuse their payment
information.](https://docs.stripe.com/payments/link/checkout-link)
- [Link with InvoicingEnable Link in the Hosted Invoice
Page.](https://docs.stripe.com/payments/link/invoicing)
- [Link in the Payment ElementTrigger Link in the Payment Element whenever a
customer selects a supported payment
method.](https://docs.stripe.com/payments/link/payment-element-link)
- [Link in the Express Checkout ElementDisplay Link alongside Apple Pay, Google
Pay, and PayPal using the Express Checkout
Element.](https://docs.stripe.com/payments/link/express-checkout-element-link)
- [Build a custom checkout page that includes LinkUse the Payment Intents API
with the Link Authentication Element or Payment Element to create a Link-enabled
custom checkout
page.](https://docs.stripe.com/payments/link/add-link-elements-integration)
- [Set up future payments using Elements and LinkSave your Link customers’
details and charge them
later.](https://docs.stripe.com/payments/link/save-and-reuse)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)