# React Stripe.js reference

## Learn about React components for Stripe.js and Stripe Elements.

React Stripe.js is a thin wrapper around [Stripe
Elements](https://docs.stripe.com/payments/elements). It allows you to add
Elements to any React app.

The [Stripe.js
reference](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options)
covers complete Elements customization details.

You can use Elements with any Stripe product to collect online payments. To find
the right integration path for your business, [explore our
docs](https://docs.stripe.com/).

#### Note

This reference covers the full React Stripe.js API. If you prefer to learn by
doing, check out our documentation on [accepting a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web) or take
a look at a [sample integration](https://docs.stripe.com/payments/quickstart).

## Before you begin

This doc assumes that you already have a basic working knowledge of
[React](https://reactjs.org/) and that you have already set up a React project.
If you’re new to React, we recommend that you take a look at the [Getting
Started](https://react.dev/learn) guide before continuing.

## Setup

npmumd
Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from
the npm public registry.

```
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

## Elements provider

The `Elements` provider allows you to use [Element
components](https://docs.stripe.com/sdks/stripejs-react#element-components) and
access the [Stripe object](https://docs.stripe.com/js/initializing) in any
nested component. Render an `Elements` provider at the root of your React app so
that it is available everywhere you need it.

To use the `Elements` provider, call
[loadStripe](https://github.com/stripe/stripe-js/blob/master/README.md#loadstripe)
from `@stripe/stripe-js` with your publishable key. The `loadStripe` function
asynchronously loads the Stripe.js script and initializes a Stripe object. Pass
the returned `Promise` to `Elements`.

```
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

export default function App() {
 const options = {
 // passing the client secret obtained from the server
 clientSecret: '{{CLIENT_SECRET}}',
 };

 return (
 <Elements stripe={stripePromise} options={options}>
 <CheckoutForm />
 </Elements>
 );
};
```

propdescription
`stripe`

required `Stripe | null | Promise<Stripe | null>`

A [Stripe object](https://docs.stripe.com/js/initializing) or a `Promise`
resolving to a Stripe object. The easiest way to initialize a Stripe object is
with the [Stripe.js wrapper
module](https://github.com/stripe/stripe-js/blob/master/README.md#readme). After
you set this prop, you can’t change it.

You can also pass in `null` or a `Promise` resolving to `null` if you’re
performing an initial server-side render or when generating a static site.

`options`

optional `Object`

Optional Elements configuration options. [See available
options](https://docs.stripe.com/js/elements_object/create#stripe_elements-options).
To create Payment Elements, you must include the Intent’s `clientSecret` unless
[you render the element before creating the
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?platform=web).

Because props are immutable, you can’t change `options` after setting it.
However, you can change the appearance of an element by calling the
[elements.update](https://docs.stripe.com/js/elements_object/update#elements_update-options-appearance)
method.

## Element components

Element components provide a flexible way to securely collect payment
information in your React app.

You can mount individual Element components inside of your `Elements` tree. Note
that you can only mount one of each type of Element in a single `<Elements>`
group.

```
import {PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
 return (
 <form>
 <PaymentElement />
 <button>Submit</button>
 </form>
 );
};

export default CheckoutForm;
```

prop description
`id`

optional `string`

Passes through to the [Element’s
container](https://docs.stripe.com/js/element/the_element_container).

`className`

optional `string`

Passes through to the [Element’s
container](https://docs.stripe.com/js/element/the_element_container).

`options`

optional `Object`

An object containing Element configuration options. [See available
options](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options)
for the Payment Element or [available
options](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options)
for individual payment method Elements.

`onBlur`

optional `() => void`

Triggered when the Element loses focus.

`onChange`

optional `(event: Object) => void`

Triggered when data exposed by this Element is changed (for example, when there
is an error).

For more information, refer to the [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_change?type=paymentElement#element_on_change-handler).

`onClick`

optional `(event: Object) => void`

Triggered by the `<PaymentRequestButtonElement>` when it is clicked.

For more information, refer to the [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_click#element_on_click-handler).

`onEscape`

optional `(event: Object) => void`

Triggered when the escape key is pressed within an Element.

For more information, refer to the [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_escape).

`onFocus`

optional `() => void`

Triggered when the Element receives focus.

`onLoaderror`

optional `(event: Object) => void`

Triggered when the Element fails to load.

This event is only emitted from the `payment`, `linkAuthentication`, `address`,
and `expressCheckout` Elements.

For more information, refer to the [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_loaderror).

`onLoaderStart`

optional `(event: Object) => void`

Triggered when the
[loader](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-loader)
UI is mounted to the DOM and ready to be displayed.

This event is only emitted from the `payment`, `linkAuthentication`, and
`address` Elements.

For more information, refer to the [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_loaderstart).

`onReady`

optional `(element: Element) => void`

Triggered when the Element is fully rendered and can accept imperative
`element.focus()` calls. Called with a reference to the underlying Element
instance.

### Available Element components

There are many different kinds of Elements, useful for collecting different
kinds of payment information. These are the available Elements today.

ComponentUsage`AddressElement`Collects address details for 236+ regional
formats. See the [Address
Element](https://docs.stripe.com/elements/address-element/collect-addresses?platform=web&client=react)
docs.`AfterpayClearpayMessageElement`Displays installments messaging for
Afterpay payments.`AuBankAccountElement`Collects Australian bank account
information (BSB and account number) for use with BECS Direct Debit
payments.`CardCvcElement`Collects the card‘s CVC number.`CardElement`A flexible
single-line input that collects all necessary card
details.`CardExpiryElement`Collects the card‘s expiration
date.`CardNumberElement`Collects the card number.`ExpressCheckoutElement`Allows
you to accept card or wallet payments through one or more payment buttons,
including Apple Pay, Google Pay, Link, or PayPal. See the [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
docs.`FpxBankElement`The customer’s bank, for use with FPX
payments.`IbanElement`The International Bank Account Number (IBAN). Available
for SEPA countries.`IdealBankElement`The customer’s bank, for use with iDEAL
payments.`LinkAuthenticationElement`Collects email addresses and allows users to
log in to Link. See the [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
docs.`PaymentElement`Collects payment details for [25+ payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
from around the globe. See the [Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements&client=react)
docs.`PaymentRequestButtonElement`An all-in-one checkout button backed by either
Apple Pay or the Payment Request API. See the [Payment Request
Button](https://docs.stripe.com/stripe-js/elements/payment-request-button) docs.
## useElements hook

#### `useElements(): Elements | null`

To safely pass the payment information collected by the Payment Element to the
Stripe API, access the `Elements` instance so that you can use it with
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment).
If you use the [React Hooks API](https://react.dev/reference/react), then
`useElements` is the recommended way to access a mounted Element. If you need to
access an Element from a class component, use
[ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react#elements-consumer)
instead.

#### Note

Note that if you pass a `Promise` to the [Elements
provider](https://docs.stripe.com/sdks/stripejs-react#elements-provider) and the
`Promise` hasn’t yet resolved, then `useElements` will return `null`.

```
import {useStripe, useElements, PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
 const stripe = useStripe();
 const elements = useElements();

 const handleSubmit = async (event) => {
 // We don't want to let default form submission happen here,
 // which would refresh the page.
 event.preventDefault();

 if (!stripe || !elements) {
 // Stripe.js hasn't yet loaded.
 // Make sure to disable form submission until Stripe.js has loaded.
 return;
 }

 const result = await stripe.confirmPayment({
 //`Elements` instance that was used to create the Payment Element
 elements,
 confirmParams: {
 return_url: "https://example.com/order/123/complete",
 },
 });

 if (result.error) {
 // Show error to your customer (for example, payment details incomplete)
 console.log(result.error.message);
 } else {
 // Your customer will be redirected to your `return_url`. For some payment
 // methods like iDEAL, your customer will be redirected to an intermediate
// site first to authorize the payment, then redirected to the `return_url`.
 }
 };

 return (
 <form onSubmit={handleSubmit}>
 <PaymentElement />
 <button disabled={!stripe}>Submit</button>
 </form>
 )
};

export default CheckoutForm;
```

## useStripe hook

#### `useStripe(): Stripe | null`

The `useStripe` [hook](https://react.dev/reference/react) returns a reference to
the [Stripe](https://docs.stripe.com/js/initializing) instance passed to the
[Elements](https://docs.stripe.com/sdks/stripejs-react#elements-provider)
provider. If you need to access the Stripe object from a class component, use
[ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react#elements-consumer)
instead.

#### Note

Note that if you pass a `Promise` to the [Elements
provider](https://docs.stripe.com/sdks/stripejs-react#elements-provider) and the
`Promise` hasn’t yet resolved, then `useStripe` will return `null`.

```
import {useStripe, useElements, PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
 const stripe = useStripe();
 const elements = useElements();

 const handleSubmit = async (event) => {
 // We don't want to let default form submission happen here,
 // which would refresh the page.
 event.preventDefault();

 if (!stripe || !elements) {
 // Stripe.js hasn't yet loaded.
 // Make sure to disable form submission until Stripe.js has loaded.
 return;
 }

 const result = await stripe.confirmPayment({
 //`Elements` instance that was used to create the Payment Element
 elements,
 confirmParams: {
 return_url: "https://example.com/order/123/complete",
 },
 });

 if (result.error) {
 // Show error to your customer (for example, payment details incomplete)
 console.log(result.error.message);
 } else {
 // Your customer will be redirected to your `return_url`. For some payment
 // methods like iDEAL, your customer will be redirected to an intermediate
// site first to authorize the payment, then redirected to the `return_url`.
 }
 };

 return (
 <form onSubmit={handleSubmit}>
 <PaymentElement />
 <button disabled={!stripe}>Submit</button>
 </form>
 )
};

export default CheckoutForm;
```

## ElementsConsumer

To safely pass the payment information collected by the Payment Element to the
Stripe API, access the `Elements` instance so that you can use it with
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment).
If you need to access the Stripe object or an Element from a class component,
then `ElementsConsumer` provides an alternative to the
[useElements](https://docs.stripe.com/sdks/stripejs-react#useElements-hook) and
[useStripe](https://docs.stripe.com/sdks/stripejs-react#useStripe-hook) hooks.

```
import {ElementsConsumer, PaymentElement} from '@stripe/react-stripe-js';

class CheckoutForm extends React.Component {
 handleSubmit = async (event) => {
 // We don't want to let default form submission happen here,
 // which would refresh the page.
 event.preventDefault();

 const {stripe, elements} = this.props;

 if (!stripe || !elements) {
 // Stripe.js hasn't yet loaded.
 // Make sure to disable form submission until Stripe.js has loaded.
 return;
 }

 const result = await stripe.confirmPayment({
 //`Elements` instance that was used to create the Payment Element
 elements,
 confirmParams: {
 return_url: "https://example.com/order/123/complete",
 },
 });

 if (result.error) {
 // Show error to your customer (for example, payment details incomplete)
 console.log(result.error.message);
 } else {
 // Your customer will be redirected to your `return_url`. For some payment
 // methods like iDEAL, your customer will be redirected to an intermediate
// site first to authorize the payment, then redirected to the `return_url`.
 }
 };

 render() {
 return (
 <form onSubmit={this.handleSubmit}>
 <PaymentElement />
 <button disabled={!this.props.stripe}>Submit</button>
 </form>
 );
 }
}

export default function InjectedCheckoutForm() {
 return (
 <ElementsConsumer>
 {({stripe, elements}) => (
 <CheckoutForm stripe={stripe} elements={elements} />
 )}
 </ElementsConsumer>
 )
}
```

prop description
`children`

required `({elements, stripe}) => ReactNode`

This component takes a [function as
child](https://reactjs.org/docs/render-props.html#using-props-other-than-render).
The function that you provide will be called with the [Elements
object](https://docs.stripe.com/js/elements_object) that is managing your
Element components and the [Stripe
object](https://docs.stripe.com/js/initializing) that you passed to
[<Elements>](https://docs.stripe.com/sdks/stripejs-react#elements-provider).

Note that if you pass a `Promise` to the [Elements
provider](https://docs.stripe.com/sdks/stripejs-react#elements-provider) and the
`Promise` hasn’t yet resolved, then `stripe` and `elements` will be `null`.

## Customization and styling

Each element is mounted in an `iframe`, which means that Elements probably won’t
work with any existing styling and component frameworks that you have. Despite
this, you can still configure Elements to match the design of your site.
Customizing Elements consists of [responding to
events](https://docs.stripe.com/js/element/events) and configuring Elements with
the [appearance](https://docs.stripe.com/elements/appearance-api) option. The
layout of each Element stays consistent, but you can modify colors, fonts,
borders, padding, and more.

This demo only displays Google Pay or Apple Pay if you have an active card with
either wallet.
## Next steps

Build an integration with React Stripe.js and Elements.

- [Accept a payment](https://docs.stripe.com/payments/quickstart)
- [Accept a payment with the Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment)
- [Adding the Payment Request
Button](https://docs.stripe.com/stripe-js/elements/payment-request-button)
- [Learn about the Elements Appearance
API](https://docs.stripe.com/elements/appearance-api)
- [Stripe.js reference](https://docs.stripe.com/js)

## Links

- [project on GitHub](https://github.com/stripe/react-stripe-js)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Stripe.js
reference](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options)
- [explore our docs](https://docs.stripe.com/)
- [accepting a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web)
- [sample integration](https://docs.stripe.com/payments/quickstart)
- [React](https://reactjs.org/)
- [Getting Started](https://react.dev/learn)
- [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
- [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js)
- [Stripe object](https://docs.stripe.com/js/initializing)
-
[loadStripe](https://github.com/stripe/stripe-js/blob/master/README.md#loadstripe)
- [Stripe.js wrapper
module](https://github.com/stripe/stripe-js/blob/master/README.md#readme)
- [See available
options](https://docs.stripe.com/js/elements_object/create#stripe_elements-options)
- [you render the element before creating the
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?platform=web)
-
[elements.update](https://docs.stripe.com/js/elements_object/update#elements_update-options-appearance)
- [Element’s
container](https://docs.stripe.com/js/element/the_element_container)
- [available
options](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options)
- [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_change?type=paymentElement#element_on_change-handler)
- [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_click#element_on_click-handler)
- [Stripe.js reference](https://docs.stripe.com/js/element/events/on_escape)
- [Stripe.js reference](https://docs.stripe.com/js/element/events/on_loaderror)
-
[loader](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-loader)
- [Stripe.js
reference](https://docs.stripe.com/js/element/events/on_loaderstart)
- [Address
Element](https://docs.stripe.com/elements/address-element/collect-addresses?platform=web&client=react)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
- [25+ payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements&client=react)
- [Payment Request
Button](https://docs.stripe.com/stripe-js/elements/payment-request-button)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
- [React Hooks API](https://react.dev/reference/react)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
- [function as
child](https://reactjs.org/docs/render-props.html#using-props-other-than-render)
- [Elements object](https://docs.stripe.com/js/elements_object)
- [compliant with industry
regulation](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [responding to events](https://docs.stripe.com/js/element/events)
- [appearance](https://docs.stripe.com/elements/appearance-api)
- [Accept a payment with the Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment)
- [Stripe.js reference](https://docs.stripe.com/js)