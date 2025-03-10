# Payment method integration options

## Learn about the different ways to integrate payment methods.

The [payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options#payment-method-availability)
you can offer depend on the currency, country, and Stripe products you integrate
with. Use this guide to make sure your chosen payment methods work for your
business and to determine how you want to add payment methods. See [payment
method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
to learn which countries, currencies, products, and APIs support which payment
methods.

## Choose your integration

The table below describes several of the ways you can get started with your
integration, including no-code, low-code, and advanced integration paths. You
can also compare [payment scenario
support](https://docs.stripe.com/payments/online-payments#compare-payment-scenario-support),
[features](https://docs.stripe.com/payments/online-payments#compare-features),
and [product
support](https://docs.stripe.com/payments/online-payments#compare-product-support).

In addition to the paths described below, you can use [Stripe
Invoicing](https://docs.stripe.com/invoicing) to automatically charge your
customer’s saved payment method or email invoices [without writing any
code](https://docs.stripe.com/invoicing/no-code-guide). See the [payment methods
supported by
Invoicing](https://docs.stripe.com/invoicing/payment-methods#supported).

[PAYMENT LINKS](https://docs.stripe.com/payment-links)[STRIPE-HOSTED
PAGE](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)[EMBEDDED
FORM](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form)[EMBEDDED
COMPONENTS](https://docs.stripe.com/checkout/custom/quickstart) Public
preview[ADVANCED
INTEGRATION](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)UIPayment
Links +
Checkout[Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=stripe-hosted)
[Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form)
[Elements](https://docs.stripe.com/payments/elements)[Elements](https://docs.stripe.com/payments/elements)API[Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions) [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions) [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions) [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions)
[PaymentIntents](https://docs.stripe.com/payments/payment-intents) Integration
effortNo code requiredLow codingLow codingMore codingMost
codingHostingStripe-hosted page (optional [custom
domains](https://docs.stripe.com/payments/checkout/custom-domains))
Stripe-hosted page (optional [custom
domains](https://docs.stripe.com/payments/checkout/custom-domains)) Embed on
your site Embed on your site Embed on your site UI customizationLimited
customization1 Limited customization1 Limited customization1 Extensive
customization with [Appearance
API](https://docs.stripe.com/elements/appearance-api) Extensive customization
with [Appearance API](https://docs.stripe.com/elements/appearance-api) PAYMENT
METHODS2 [Dynamically
display](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
40+ payment methods Manage payment methods in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) without coding
[Faster checkout with Link](https://docs.stripe.com/payments/link) and more
wallet payment methods such as [Apple Pay](https://docs.stripe.com/apple-pay),
[Google Pay](https://docs.stripe.com/google-pay), and [Amazon
Pay](https://docs.stripe.com/payments/amazon-pay) 3 3 3[External payment
methods](https://docs.stripe.com/payments/external-payment-methods)
1Limited customization provides [20 preset
fonts](https://docs.stripe.com/payments/checkout/customization/appearance#font-compatibility),
3 preset border radius options, logo and background customization, and custom
button color.

2For detailed support for each payment method, see [learn more about payment
methods](https://docs.stripe.com/payments/payment-methods/overview).

3Wallet payment methods require [registering your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration).

## Payment method support

Payment methods only support certain currencies, countries, products, and API
features. Make sure your chosen payment methods work for your scenario by
reviewing the [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
page.

## Add payment methods

Your customers see the available payment methods during the checkout process.
You can either manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) or list
payment methods manually in code. See the [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment) guide for detailed
steps.

### Use dynamic payment methods

Stripe dynamically displays the most relevant payment methods to your customers
based on the payment method preferences you set in the Dashboard and eligibility
factors such as transaction amount, currency, and payment flow. To enable and
manage your payment method preferences, go to the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
enables certain payment methods for you by default and might enable additional
payment methods after notifying you.

Unless you have to list payment methods manually, we recommend using dynamic
payment methods. Dynamic payment methods automatically determines whether to
display payment methods according to set rules.

See [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
to learn more.

### Manually list payment methods

Listing payment methods manually requires some coding. Every payment method you
want your PaymentIntent to accept must be added to `payment_method_types`.
Unless your integration requires that you list payment methods manually, we
recommend that you manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow.

CheckoutPayment Element
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 --data-urlencode success_url="https://example.com/success" \
 -d "payment_method_types[0]"=bancontact \
 -d "payment_method_types[1]"=card \
 -d "payment_method_types[2]"=eps \
 -d "payment_method_types[3]"=ideal \
 -d "payment_method_types[4]"=p24 \
 -d "payment_method_types[5]"=sepa_debit
```

If multiple payment methods are passed, Checkout dynamically reorders them to
prioritize the most relevant payment methods based on the customer’s location
and other characteristics. The payments acceptance page prioritizes showing
payment methods known to increase conversion for your customer’s location while
lower priority payment methods are hidden in an overflow menu.

## Links

- [payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [payment scenario
support](https://docs.stripe.com/payments/online-payments#compare-payment-scenario-support)
- [features](https://docs.stripe.com/payments/online-payments#compare-features)
- [product
support](https://docs.stripe.com/payments/online-payments#compare-product-support)
- [Stripe Invoicing](https://docs.stripe.com/invoicing)
- [without writing any code](https://docs.stripe.com/invoicing/no-code-guide)
- [payment methods supported by
Invoicing](https://docs.stripe.com/invoicing/payment-methods#supported)
- [PAYMENT LINKS](https://docs.stripe.com/payment-links)
- [STRIPE-HOSTED
PAGE](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [EMBEDDED
FORM](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form)
- [EMBEDDED COMPONENTS](https://docs.stripe.com/checkout/custom/quickstart)
- [ADVANCED
INTEGRATION](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)
-
[Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=stripe-hosted)
-
[Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form)
- [Elements](https://docs.stripe.com/payments/elements)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [custom domains](https://docs.stripe.com/payments/checkout/custom-domains)
- [Appearance API](https://docs.stripe.com/elements/appearance-api)
- [Dynamically
display](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Faster checkout with Link](https://docs.stripe.com/payments/link)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
- [External payment
methods](https://docs.stripe.com/payments/external-payment-methods)
- [20 preset
fonts](https://docs.stripe.com/payments/checkout/customization/appearance#font-compatibility)
- [learn more about payment
methods](https://docs.stripe.com/payments/payment-methods/overview)
- [registering your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [Accept a payment](https://docs.stripe.com/payments/accept-a-payment)
- [https://example.com/success](https://example.com/success)