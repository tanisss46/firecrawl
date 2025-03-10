# Stripe Payment Element

## Accept payment methods from around the globe with a secure, embeddable UI component.

#### Interested in using Stripe Tax, discounts, shipping, or currency conversion?

We’re developing a Payment Element integration that manages tax, discounts,
shipping, and currency conversion. Read the [Build a checkout
page](https://docs.stripe.com/checkout/custom/quickstart) guide to learn more.

The Payment Element is a UI component for the web that accepts 40+ payment
methods, validates input, and handles errors. Use it alone or with other
elements in your web app’s front end.

#### Country availability

In Brazil and Thailand, Payment Elements don’t support Link.

This demo only displays Google Pay or Apple Pay if you have an active card with
either wallet.
You can integrate the Payment Element with:

- The [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions) to
[build a checkout
page](https://docs.stripe.com/payments/checkout/build-integration).
- The [Payment Intents API](https://docs.stripe.com/api/payment_intents) to
[build an advanced integration](https://docs.stripe.com/payments/advanced).
[Build a checkout page with Payment ElementBuild an integration with the Payment
Element using the Checkout Sessions API.Public
preview](https://docs.stripe.com/checkout/custom/quickstart)[Build an advanced
integration with Payment ElementBuild an integration with the Payment Element
using the Payment Intents
API.](https://docs.stripe.com/payments/quickstart)[Clone a sample app on
GitHubHTML · React ·
Vue](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)[View
the Stripe.js reference](https://docs.stripe.com/js/element/payment_element)
## Create a Payment Element

This code
[creates](https://docs.stripe.com/js/elements_object/create_payment_element) a
Payment Element and [mounts](https://docs.stripe.com/js/element/mount) it to the
DOM:

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = { /* appearance */ };
const options = { layout: 'accordion', /* options */ };
const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#payment-element');
```

Accepting payments with the Payment Element requires additional backend code.
See the [quickstart](https://docs.stripe.com/payments/quickstart) or [sample
app](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)
to learn how this works.

## Combine elements

The Payment Element interoperates with other elements. For instance, this form
uses one additional element to [autofill checkout
details](https://docs.stripe.com/payments/link), and another to [collect the
shipping address](https://docs.stripe.com/elements/address-element).

#### Note

You can’t remove the Link legal agreement because it’s required to ensure
compliance with proper user awareness of terms of services and privacy policies.
The
[terms](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-terms)
object doesn’t apply to the Link legal agreement.

![A form with contact info, shipping address, and payment fields. The contact
info is labeled Link Authentication Element, the shipping address is labeled
Address Element, and the payment fields are labeled Payment
Element](https://b.stripecdn.com/docs-statics-srv/assets/link-with-elements.f60af275f69b6e6e73c766d1f9928457.png)

For the complete code for this example, see [Add Link to an Elements
integration](https://docs.stripe.com/payments/link/add-link-elements-integration).

You can also combine the Payment Element with the [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element). In this
case, wallet payment methods such as Apple Pay and Google Pay are only displayed
in the Express Checkout Element to avoid duplication.

## Payment methods

Stripe enables certain payment methods for you by default. We might also enable
additional payment methods after notifying you. Use the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) to enable or
disable payment methods at any time. With the Payment Element, you can use
[Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
to:

- Manage payment methods in the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) without
coding
- Dynamically display the most relevant payment options based on factors such as
location, currency, and transaction amount

For instance, if a customer in Germany is paying in EUR, they see all the active
payment methods that accept EUR, starting with ones that are widely used in
Germany.

![A variety of payment
methods.](https://b.stripecdn.com/docs-statics-srv/assets/payment-element-methods.26cae03aff199d6f02b0d92bd324c219.png)

Show payment methods in order of relevance to your customer

To further customize how payment methods render, such as by filtering card
brands that you don’t want to support, see [Customize payment
methods](https://docs.stripe.com/payments/customize-payment-methods). To add
payment methods integrated outside of Stripe, see [External payment
methods](https://docs.stripe.com/payments/external-payment-methods).

If your integration requires you to list payment methods manually, see [Manually
list payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options#listing-payment-methods-manually).

## Layout

You can customize the Payment Element’s layout to fit your checkout flow. The
following image is the same Payment Element rendered using different layout
configurations.

![Examples of the three checkout forms. The image shows the tab option, where
customers pick from payment methods shown as tabs or the two accordion options,
where payment methods are vertically listed. You can choose to either display
radio buttons or not in the accordion view.
](https://b.stripecdn.com/docs-statics-srv/assets/pe_layout_example.525f78bcb99b95e49be92e5dd34df439.png)

Payment Element with different layouts.

TabsAccordion with radio buttonsAccordion without radio buttons
The tabs layout displays payment methods horizontally using tabs. To use this
layout, set the value for
[layout.type](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout-type)
to `tabs`. You can also specify other properties, such as
[layout.defaultCollapsed](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout-defaultCollapsed).

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = { /* appearance */ };
const options = {
 layout: {
 type: 'tabs',
 defaultCollapsed: false,
 }
};
```

See all 12 lines
## Appearance

Use the Appearance API to control the style of all elements. Choose a theme or
update specific details.

![Examples of light and dark modes for the payment element checkout
form.](https://b.stripecdn.com/docs-statics-srv/assets/appearance_example.e076cc750983bf552baf26c305e7fc90.png)

For instance, choose the “flat” theme and override the primary text color.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = {
 theme: 'flat',
 variables: { colorPrimaryText: '#262626' }
};
```

See all 10 lines
See the [Appearance API](https://docs.stripe.com/elements/appearance-api)
documentation for a full list of themes and variables.

## Options

Stripe elements support more options than these. For instance, display your
business name using the
[business](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-business)
option.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = { /* appearance */};
const options = {
 business: "RocketRides"
};
```

See all 10 lines
The Payment Element supports the following options. See each options’s reference
entry for more information.

[layout](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout)Layout
for the Payment
Element.[defaultValues](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)Initial
customer information to display in the Payment
Element.[business](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-business)Information
about your business to display in the Payment
Element.[paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-business)Order
to list payment methods
in.[fields](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-fields)Whether
to display certain
fields.[readOnly](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-readOnly)Whether
payment details can be
changed.[terms](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-terms)Whether
mandates or other legal agreements are displayed in the Payment Element. The
default behavior is to show them only when
necessary.[wallets](https://docs.stripe.com/js/elements_object/create_payment_element)Whether
to show wallets like Apple Pay or Google Pay. The default is to show them when
possible.
## Errors

Payment Element automatically shows localized customer-facing error messages
during client confirmation for the following error codes:

- `generic_decline`
- `insufficient_funds`
- `incorrect_zip`
- `incorrect_cvc`
- `invalid_cvc`
- `invalid_expiry_month`
- `invalid_expiry_year`
- `expired_card`
- `fraudulent`
- `lost_card`
- `stolen_card`
- `card_velocity_exceeded`

To display messages for other types of errors, refer to [error
codes](https://docs.stripe.com/error-codes) and [error
handling](https://docs.stripe.com/error-handling).

## Links

- [Build a checkout page](https://docs.stripe.com/checkout/custom/quickstart)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)
- [build a checkout
page](https://docs.stripe.com/payments/checkout/build-integration)
- [Payment Intents API](https://docs.stripe.com/api/payment_intents)
- [build an advanced integration](https://docs.stripe.com/payments/advanced)
- [Build an advanced integration with Payment ElementBuild an integration with
the Payment Element using the Payment Intents
API.](https://docs.stripe.com/payments/quickstart)
- [Clone a sample app on GitHubHTML · React ·
Vue](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)
- [View the Stripe.js
reference](https://docs.stripe.com/js/element/payment_element)
- [creates](https://docs.stripe.com/js/elements_object/create_payment_element)
- [mounts](https://docs.stripe.com/js/element/mount)
- [autofill checkout details](https://docs.stripe.com/payments/link)
- [collect the shipping
address](https://docs.stripe.com/elements/address-element)
-
[terms](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-terms)
- [Add Link to an Elements
integration](https://docs.stripe.com/payments/link/add-link-elements-integration)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Customize payment
methods](https://docs.stripe.com/payments/customize-payment-methods)
- [External payment
methods](https://docs.stripe.com/payments/external-payment-methods)
- [Manually list payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options#listing-payment-methods-manually)
-
[layout.type](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout-type)
-
[layout.defaultCollapsed](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout-defaultCollapsed)
- [Appearance API](https://docs.stripe.com/elements/appearance-api)
-
[business](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-business)
-
[layout](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout)
-
[defaultValues](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)
-
[fields](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-fields)
-
[readOnly](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-readOnly)
- [error codes](https://docs.stripe.com/error-codes)
- [error handling](https://docs.stripe.com/error-handling)