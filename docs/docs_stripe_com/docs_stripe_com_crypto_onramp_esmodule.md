# Install the Stripe Crypto SDK ES ModulePublic preview

## Set up the Stripe crypto client-side SDK in your web application.

This guide demonstrates how to install the [Stripe Crypto ES
module](https://www.npmjs.com/@stripe/crypto) client-side SDK using a script tag
or package manager. The SDK wraps the global `StripeOnramp` function provided by
the Stripe crypto script as an ES module. It lets you use the
[onramp](https://docs.stripe.com/crypto/onramp) widget to help your customers
acquire crypto using fiat.

## Manually load the script

Include the following scripts using script tags within the `<head>` element of
your HTML. These scripts must always load directly from Stripe’s domains,
*https://js.stripe.com* and *https://crypto-js.stripe.com*, for compatibility
and [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance).
Don’t include the scripts in a bundle or host a copy yourself. If you do, your
integration might break without warning.

```
<head>
 <title>Onramp</title>
 <script src="https://js.stripe.com/v3/"></script>
 <script src="https://crypto-js.stripe.com/crypto-onramp-outer.js"></script>
</head>
```

### StripeOnramp constructor

Set the [API publishable key](https://dashboard.stripe.com/test/apikeys) to
allow Stripe to retrieve the `OnrampSession` object created by your back end.
For example:

```
const stripeOnramp = StripeOnramp('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

## Load the crypto SDK as an ES module

To install the module through the package manager, first install the [Stripe.js
ES module](https://github.com/stripe/stripe-js) and [Stripe crypto ES
module](https://www.npmjs.com/package/@stripe/crypto) from the [npm public
registry](https://www.npmjs.com/). The package includes Typescript type
definitions.

```
npm install @stripe/stripe-js @stripe/crypto
```

### StripeOnramp constructor

Import the module and set the [API publishable
key](https://dashboard.stripe.com/test/apikeys) to allow Stripe to retrieve the
`OnrampSession` object created by your back end. The function returns a
`Promise` object that resolves with a newly created `StripeOnramp` object after
the scripts load.

```
import {loadStripeOnramp} from '@stripe/crypto';

const stripeOnramp = await loadStripeOnramp('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

## Links

- [npm](https://www.npmjs.com/@stripe/crypto)
- [onramp](https://docs.stripe.com/crypto/onramp)
- [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
-
[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)
- [API publishable key](https://dashboard.stripe.com/test/apikeys)
- [Stripe.js ES module](https://github.com/stripe/stripe-js)
- [Stripe crypto ES module](https://www.npmjs.com/package/@stripe/crypto)
- [npm public registry](https://www.npmjs.com/)