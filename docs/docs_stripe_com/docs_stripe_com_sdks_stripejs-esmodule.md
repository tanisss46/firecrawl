# ES Module Stripe.js SDK

## Set up the ES Module Stripe.js client-side SDK in your web application.

This introductory guide shows you how to install the [ES Module
Stripe.js](https://github.com/stripe/stripe-js) client-side SDK with a script
tag or package manager. The SDK wraps the global `Stripe` function provided by
the Stripe.js script as an ES module. It allows you to use
[Elements](https://docs.stripe.com/payments/elements), our prebuilt UI
components, to create a payment form that lets you securely collect a customer’s
card details without handling the sensitive data.

## Before you begin

Enable the payment methods you want to support on the [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) page.

## Manually load the Stripe.js script

### Installation

To install by script, add the [Stripe.js ES
Module](https://github.com/stripe/stripe-js) as a script to the `<head>` element
of your **HTML**. This allows any newly created [Stripe
objects](https://docs.stripe.com/js#stripe-function) to be globally accessible
in your code.

```
<head>
 <title>Checkout</title>
 <script src="https://js.stripe.com/v3/" async></script>
</head>
```

### Stripe.js constructor

Next, set the [API publishable key](https://dashboard.stripe.com/test/apikeys)
to allow Stripe to [tokenize](https://docs.stripe.com/api/tokens) customer
information and collect sensitive payment details. For example:

```
var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

## Load Stripe.js as an ES Module

### Installation

To install by package manager, install the [Stripe.js ES
Module](https://github.com/stripe/stripe-js) from the [npm public
registry](https://www.npmjs.com/).

```
npm install @stripe/stripe-js
```

### Stripe.js constructor

Next, import the module into a **JavaScript** file. The following function
returns a `Promise` that resolves with a newly created [Stripe
object](https://docs.stripe.com/js#stripe-function) after Stripe.js loads.

```
import {loadStripe} from '@stripe/stripe-js';

const stripe = await loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

## See also

This wraps up the introductory guide to setting up the ES Module Stripe.js SDK.
See the links below to get started with your integration.

- [Accept a payment with a payment element on
GitHub](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)
- [Accept a payment with a payment element in
Docs](https://docs.stripe.com/payments/accept-a-payment?ui=elements&client=html)
- [Custom payment flow builder](https://docs.stripe.com/payments/quickstart)
- [Stripe.js reference](https://docs.stripe.com/js)

## Links

- [project on GitHub](https://github.com/stripe/stripe-js)
- [Elements](https://docs.stripe.com/payments/elements)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Stripe objects](https://docs.stripe.com/js#stripe-function)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [API publishable key](https://dashboard.stripe.com/test/apikeys)
- [tokenize](https://docs.stripe.com/api/tokens)
- [npm public registry](https://www.npmjs.com/)
- [Accept a payment with a payment element on
GitHub](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)
- [Accept a payment with a payment element in
Docs](https://docs.stripe.com/payments/accept-a-payment?ui=elements&client=html)
- [Custom payment flow builder](https://docs.stripe.com/payments/quickstart)
- [Stripe.js reference](https://docs.stripe.com/js)