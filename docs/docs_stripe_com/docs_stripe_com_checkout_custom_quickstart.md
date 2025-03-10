# Build a checkout page with embedded componentsPublic preview

## Use Elements and the Checkout Sessions API to build a checkout page.

Build a checkout page on your website using [Stripe
Elements](https://docs.stripe.com/payments/elements) and the [Checkout
Sessions](https://docs.stripe.com/api/checkout/sessions) API, an integration
that manages tax, discounts, shipping rates, and more.

This demo only displays Google Pay or Apple Pay if you have an active card with
either wallet.[Set up the
serverServer-side](https://docs.stripe.com/checkout/custom/quickstart#set-up-server)
Before you begin, you need to [register](https://dashboard.stripe.com/register)
for a Stripe account.

Use the official Stripe libraries to access the API from your application.

```
npm install stripe@17.4.0-beta.2 --save
```

Set the SDK to use the `custom_checkout_beta=v1` beta version header.

```
// Set your secret key. Remember to switch to your live secret key in
production.
// See your keys here: https://dashboard.stripe.com/apikeys
import Stripe from 'stripe';
const stripe = new Stripe('sk_test_BQokikJOvBiI2HlWgH4olfQ2', {
 apiVersion: '2025-02-24.acacia; custom_checkout_beta=v1' as any,
});
```

[Create a Checkout
SessionServer-side](https://docs.stripe.com/checkout/custom/quickstart#create-checkout-session)
Add an endpoint on your server that creates a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create) and returns its
[client
secret](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_secret)
to your front end. A Checkout Session represents your customer’s session as they
pay for one-time purchases or subscriptions. Checkout Sessions expire 24 hours
after creation.

```
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res:
Express.Response) => {
 const session = await stripe.checkout.sessions.create({
 line_items: [
 {
 price_data: {
 currency: 'usd',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 },
 ],
 mode: 'payment',
 ui_mode: 'custom',
 // The URL of your payment completion page
 return_url: '{{RETURN_URL}}'
 });

 res.json({clientSecret: session.client_secret});
});

app.listen(3000, () => {
 console.log('Running on port 3000');
});
```

[Set up the front
endClient-side](https://docs.stripe.com/checkout/custom/quickstart#set-up-frontend)ReactHTML
+ JS
Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from
the npm public registry. You need at least version 3.0.0 for React Stripe.js and
version 5.2.0 for the Stripe.js loader.

```
npm install --save @stripe/react-stripe-js@^3.0.0 @stripe/stripe-js@^5.2.0
```

Initialize a `stripe` instance on your front end with your publishable key,
passing in the `custom_checkout_beta_5` beta.

```
import {loadStripe} from '@stripe/stripe-js';
const stripe = loadStripe("pk_test_TYooMQauvdEDq54NiTphI7jx", {
 betas: ['custom_checkout_beta_5'],
});
```

[Initialize
CheckoutClient-side](https://docs.stripe.com/checkout/custom/quickstart#initialize-checkout)ReactHTML
+ JS
Retrieve the `clientSecret` from your server and wrap your application with the
[CheckoutProvider](https://docs.stripe.com/js/custom_checkout/react/checkout_provider)
component.

Use the
[useCheckout](https://docs.stripe.com/js/custom_checkout/react/use_checkout)
hook in your components to get the `checkout` object, which contains data from
the Checkout Session as well as methods to update it. For now, render the line
items as text and log the `checkout` object to the console to see what’s
available.

```
import React from 'react';
import {CheckoutProvider} from '@stripe/react-stripe-js';
import CheckoutForm from './CheckoutForm';

const App = () => {
 const [clientSecret, setClientSecret] = React.useState(null);
 React.useEffect(() => {
 fetch('/create-checkout-session', {method: 'POST'})
 .then((response) => response.json())
 .then((json) => setClientSecret(json.clientSecret))
 }, []);

 if (clientSecret) {
 return (
 <CheckoutProvider
 stripe={stripe}
 options={{clientSecret}}
 >
 <CheckoutForm />
 </CheckoutProvider>
 );
 } else {
 return null;
 }
};

export default App;
```

```
import React from 'react';
import {useCheckout} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
 const checkout = useCheckout();
 console.log(checkout);
 return (
 <pre>
 {JSON.stringify(checkout.lineItems, null, 2)}
 </pre>
 )
};
```

[Collect customer
emailClient-side](https://docs.stripe.com/checkout/custom/quickstart#collect-email)ReactHTML
+ JS
Create a component to collect your customer’s email address. Call
[updateEmail](https://docs.stripe.com/js/custom_checkout/react/update_email)
when your customer finishes the input to validate and save the email address.

- If you have a multi-step form, call `updateEmail` before moving to the next
step, such as clicking a **Save** button.
- If you have a single-page form, call `updateEmail` before [submitting the
payment](https://docs.stripe.com/checkout/custom/quickstart#submit-payment). You
can also call `updateEmail` to validate earlier, such as on input blur.

```
import React from 'react';
import {useCheckout} from '@stripe/react-stripe-js';

const EmailInput = () => {
 const checkout = useCheckout();
 const [email, setEmail] = React.useState('');
 const [error, setError] = React.useState(null);

 const handleBlur = () => {
 checkout.updateEmail(email).then((result) => {
 if (result.error) {
 setError(result.error);
 }
 })
 };

 const handleChange = (e) => {
 setError(null);
 setEmail(e.target.value);
 };
 return (
 <div>
 <input
 type="text"
 value={email}
 onChange={handleChange}
 onBlur={handleBlur}
 />
 {error && <div>{error.message}</div>}
 </div>
 );
};

export default EmailInput;
```

[Collect payment
detailsClient-side](https://docs.stripe.com/checkout/custom/quickstart#collect-payment-details)
Collect payment details on the client with the [Payment
Element](https://docs.stripe.com/payments/payment-element). The Payment Element
is a prebuilt UI component that simplifies collecting payment details for a
variety of payment methods.

ReactHTML + JS
Mount the [Payment Element](https://docs.stripe.com/payments/payment-element)
component within the
[CheckoutProvider](https://docs.stripe.com/js/custom_checkout/react/checkout_provider).

```
import React from 'react';
import {PaymentElement, useCheckout} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
 const checkout = useCheckout();
 return (
 <form>
 <PaymentElement options={{layout: 'accordion'}}/>
 </form>
 )
};

export default CheckoutForm;
```

See the [Stripe.js
docs](https://docs.stripe.com/js/custom_checkout/create_element?type=payment#custom_checkout_create_element-options)
to view what options are supported.

You can [customize the
appearance](https://docs.stripe.com/payments/checkout/customization/appearance)
of all Elements by passing
[elementsOptions.appearance](https://docs.stripe.com/js/custom_checkout/react/checkout_provider#custom_checkout_react_checkout_provider-options-elementsOptions-appearance)
to the
[CheckoutProvider](https://docs.stripe.com/js/custom_checkout/react/checkout_provider).

[Submit the
paymentClient-side](https://docs.stripe.com/checkout/custom/quickstart#submit-payment)ReactHTML
+ JS
Render a “pay” button that calls
[confirm](https://docs.stripe.com/js/custom_checkout/confirm) from
[useCheckout](https://docs.stripe.com/js/custom_checkout/react/use_checkout) to
submit the payment.

```
import React from 'react';
import {useCheckout} from '@stripe/react-stripe-js';

const PayButton = () => {
 const {confirm} = useCheckout();
 const [loading, setLoading] = React.useState(false);
 const [error, setError] = React.useState(null);

 const handleClick = () => {
 setLoading(true);
 confirm().then((result) => {
 if (result.type === 'error') {
 setError(result.error)
 }
 setLoading(false);
 })
 };

 return (
 <div>
 <button disabled={loading} onClick={handleClick}>
 Pay
 </button>
 {error && <div>{error.message}</div>}
 </div>
 )
};

export default PayButton;
```

[Test your
integration](https://docs.stripe.com/checkout/custom/quickstart#test-the-integration)-
Navigate to your checkout page.
- Fill out the payment details with a payment method from the following table.
For card payments:- Enter any future date for card expiry.
- Enter any 3-digit number for CVC.
- Enter any billing postal code.
- Submit the payment to Stripe.
- Go to the Dashboard and look for the payment on the [Transactions
page](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful). If
your payment succeeded, you’ll see it in that list.
- Click your payment to see more details, like billing information and the list
of purchased items. You can use this information to [fulfill the
order](https://docs.stripe.com/checkout/fulfillment).
CardsWalletsBank redirectsBank debitsVouchersCard numberScenarioHow to
test4242424242424242The card payment succeeds and doesn’t require
authentication.Fill out the credit card form using the credit card number with
any expiration, CVC, and postal code.4000002500003155The card payment requires
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number with any expiration, CVC,
and postal code.4000000000009995The card is declined with a decline code like
`insufficient_funds`.Fill out the credit card form using the credit card number
with any expiration, CVC, and postal code.6205500000000000004The UnionPay card
has a variable length of 13-19 digits.Fill out the credit card form using the
credit card number with any expiration, CVC, and postal code.
See [Testing](https://docs.stripe.com/testing) for additional information to
test your integration.

## See also

- [Collect billing and shipping
addresses](https://docs.stripe.com/payments/collect-addresses)
- [Add discounts for one-time
payments](https://docs.stripe.com/payments/checkout/discounts)
- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes)
- [Enable adjustable line item
quantities](https://docs.stripe.com/payments/checkout/adjustable-quantity)
- [Fulfill orders after a customer
pays](https://docs.stripe.com/checkout/fulfillment)

## Links

- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [register](https://dashboard.stripe.com/register)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create)
- [client
secret](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_secret)
- [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
- [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js)
-
[CheckoutProvider](https://docs.stripe.com/js/custom_checkout/react/checkout_provider)
- [useCheckout](https://docs.stripe.com/js/custom_checkout/react/use_checkout)
- [updateEmail](https://docs.stripe.com/js/custom_checkout/react/update_email)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Stripe.js
docs](https://docs.stripe.com/js/custom_checkout/create_element?type=payment#custom_checkout_create_element-options)
- [customize the
appearance](https://docs.stripe.com/payments/checkout/customization/appearance)
-
[elementsOptions.appearance](https://docs.stripe.com/js/custom_checkout/react/checkout_provider#custom_checkout_react_checkout_provider-options-elementsOptions-appearance)
- [confirm](https://docs.stripe.com/js/custom_checkout/confirm)
- [Transactions
page](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful)
- [fulfill the order](https://docs.stripe.com/checkout/fulfillment)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Testing](https://docs.stripe.com/testing)
- [Collect billing and shipping
addresses](https://docs.stripe.com/payments/collect-addresses)
- [Add discounts for one-time
payments](https://docs.stripe.com/payments/checkout/discounts)
- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes)
- [Enable adjustable line item
quantities](https://docs.stripe.com/payments/checkout/adjustable-quantity)