# Card payments without bank authentication

## Build a simpler integration with regional limitations.

This integration supports businesses accepting only US and Canadian cards. It’s
simpler up front, but does not scale to support a global customer base.

### How does this integration work?

### How does it compare to the global integration?

Growing or global businesses should use Stripe’s [global
integration](https://docs.stripe.com/payments/accept-a-payment) to support bank
requests for two-factor authentication and allow customers to pay with more
payment methods.

Customer

Client

Server

Stripe

Provides card details and clicks Pay button

Calls `stripe.createPaymentMethod`

Returns `PaymentMethod`

Finalizes payment with order details and `PaymentMethod` ID

`POST /v1/payment_intents confirm=true`

Attempts payment

If no authentication required, returns new `PaymentIntent` with status
“succeeded”

Attempts payment

If authentication required, returns new Error with code
“authentication_required”

Payment flow you're integrating[Build a checkout
formClient-side](https://docs.stripe.com/payments/without-card-authentication#web-collect-payment-details)
[Elements](https://docs.stripe.com/payments/elements), part of Stripe.js,
provides drop-in UI components for collecting card information from customers.
Stripe hosts them and places them into your payment form as an iframe so your
customer’s card details never touch your code.

HTML + JSReact
First, include the [Stripe.js](https://docs.stripe.com/js) script in the head of
every page on your site.

```
<script src="https://js.stripe.com/v3/"></script>
```

Including the script on every page of your site lets you take advantage of
Stripe’s [advanced fraud functionality](https://docs.stripe.com/radar) and
ability to detect anomalous browsing behavior.

### Security requirements

This script must always load directly from **js.stripe.com** to remain [PCI
compliant](https://docs.stripe.com/security/guide). You can’t include the script
in a bundle or host a copy of it yourself.

When you use Elements, all payment information is submitted over a secure HTTPS
connection.

The address of the page that contains Elements must also start with **https://**
rather than **http://**. For more information about getting SSL certificates and
integrating them with your server to enable a secure HTTPS connection, see the
[security](https://docs.stripe.com/security) documentation.

### Add Elements to your page

Next, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Create empty DOM elements (containers) with unique IDs within your payment form.

```
<form id="payment-form">
 <div id="card-element"><!-- placeholder for Elements --></div>
 <button id="card-button">Submit Payment</button>
<p id="payment-result"><!-- we'll pass the response from the server here --></p>
</form>
```

Create an instance of the [Stripe
object](https://docs.stripe.com/js#stripe-function), providing your publishable
[API key](https://docs.stripe.com/keys) as the first parameter. Afterwards,
create an instance of the [Elements
object](https://docs.stripe.com/js#stripe-elements) and use it to
[mount](https://docs.stripe.com/js#element-mount) a Card element in the empty
DOM element container on the page.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const elements = stripe.elements();
const cardElement = elements.create('card');
cardElement.mount('#card-element');
```

Use
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method)
on your client to collect the card details and create a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) when the customer
submits the payment form. Send the ID of the PaymentMethod to your server.

```
const form = document.getElementById("payment-form");

var resultContainer = document.getElementById('payment-result');

// cardElement is defined in the previous step
cardElement.on('change', function(event) {
 if (event.error) {
 resultContainer.textContent = event.error.message;
 } else {
 resultContainer.textContent = '';
 }
});

form.addEventListener('submit', async event => {
 event.preventDefault();
 resultContainer.textContent = '';
 const result = await stripe.createPaymentMethod({
 type: 'card',
 card: cardElement,
 });
 handlePaymentMethodResult(result);
});

const handlePaymentMethodResult = async ({ paymentMethod, error }) => {
 if (error) {
// An error happened when collecting card details, show error in payment form
 resultContainer.textContent = result.error.message;
 } else {
 // Send paymentMethod.id to your server (see Step 3)
 const response = await fetch("/pay", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify({ payment_method_id: paymentMethod.id })
 });

 const responseJson = await response.json();

 handleServerResponse(responseJson);
 }
};

const handleServerResponse = async responseJson => {
 if (responseJson.error) {
 // An error happened when charging the card, show it in the payment form
 resultContainer.textContent = responseJson.error;
 } else {
 // Show a success message
 resultContainer.textContent = 'Success!';
 }
};
```

[Set up
StripeServer-side](https://docs.stripe.com/payments/without-card-authentication#web-setup)
Use an official library to make requests to the Stripe API from your
application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Make a
paymentServer-side](https://docs.stripe.com/payments/without-card-authentication#web-create-payment-intent)
Set up an endpoint on your server to receive the request from the client.

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents)
object to represent your intent to collect payment from a customer, tracking
charge attempts and payment state changes throughout the process.

Always decide how much to charge on the server, a trusted environment, as
opposed to the client. This prevents malicious customers from being able to
choose their own prices.

Create an HTTP endpoint to respond to the AJAX request from step 1. In that
endpoint, you should decide how much to charge the customer. To create a
payment, create a PaymentIntent using the
[PaymentMethod](https://docs.stripe.com/api/payment_methods) ID from step 1 with
the following code:

```
# Check the status of the PaymentIntent to make sure it succeeded

curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1099 \
 -d currency=usd \

# A PaymentIntent can be confirmed some time after creation,
# but here we want to confirm (collect payment) immediately.
 -d confirm=true \
 -d payment_method="{{PAYMENT_METHOD_ID}}" \

# If the payment requires any follow-up actions from the
# customer, like two-factor authentication, Stripe will error
# and you will need to prompt them for a new payment method.
 -d error_on_requires_action=true
```

#### Warning

If you set
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
to `true` when confirming a payment, Stripe automatically fails the payment if
it requires two-factor authentication from the user.

#### Payment Intents API response

When you make a payment with the API, the response includes a status of the
PaymentIntent. If the payment was successful, it will have a status of
`succeeded`.

```
{
 "id": "pi_0FdpcX589O8KAxCGR6tGNyWj",
 "object": "payment_intent",
 "amount": 1099,
 "charges": {
 "object": "list",
 "data": [
 {
 "id": "ch_GA9w4aF29fYajT",
 "object": "charge",
 "amount": 1099,
 "refunded": false,
 "status": "succeeded",
 }
 ]
 },
"client_secret": "pi_0FdpcX589O8KAxCGR6tGNyWj_secret_e00tjcVrSv2tjjufYqPNZBKZc",
 "currency": "usd",
 "last_payment_error": null,
 "status": "succeeded",
}
```

If the payment is declined, the response includes the error code and error
message. Here’s an example of a payment that failed because two-factor
authentication was required for the card.

```
{
 "error": {
 "code": "authentication_required",
 "decline_code": "authentication_not_handled",
 "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
"message": "This payment required an authentication action to complete, but
`error_on_requires_action` was set. When you're ready, you can upgrade your
integration to handle actions at
https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
 "payment_intent": {
 "id": "pi_1G8JtxDpqHItWkFAnB32FhtI",
 "object": "payment_intent",
 "amount": 1099,
 "status": "requires_payment_method",
 "last_payment_error": {
 "code": "authentication_required",
 "decline_code": "authentication_not_handled",
"doc_url": "https://docs.stripe.com/error-codes#authentication-required",
"message": "This payment required an authentication action to complete, but
`error_on_requires_action` was set. When you're ready, you can upgrade your
integration to handle actions at
https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
 "type": "card_error"
 },
 },
 "type": "card_error"
 }
}
```

[Test the
integration](https://docs.stripe.com/payments/without-card-authentication#web-test)
There are several test cards you can use in test mode to make sure this
integration is ready. Use them with any CVC, postal code, and future expiration
date.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000000000009995Always fails with a decline code of
`insufficient_funds`.4000002500003155Requires authentication, which in this
integration will fail with a decline code of `authentication_not_handled`.
See the full list of [test cards](https://docs.stripe.com/testing).

[Upgrade your integration to handle card
authentication](https://docs.stripe.com/payments/without-card-authentication#web-upgrade-to-handle-card-authentication)
Congratulations! You completed a payments integration for basic card payments.
Note that this integration **declines cards that require authentication during
payment**.

If you start seeing payments in the Dashboard listed as `Failed`, then it’s time
to [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions).
Stripe’s global integration handles these payments instead of automatically
declining them.

## Links

- [global integration](https://docs.stripe.com/payments/accept-a-payment)
- [Elements](https://docs.stripe.com/payments/elements)
- [Stripe.js](https://docs.stripe.com/js)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [advanced fraud functionality](https://docs.stripe.com/radar)
- [PCI compliant](https://docs.stripe.com/security/guide)
- [security](https://docs.stripe.com/security)
- [Register now](https://dashboard.stripe.com/register)
- [Stripe object](https://docs.stripe.com/js#stripe-function)
- [API key](https://docs.stripe.com/keys)
- [Elements object](https://docs.stripe.com/js#stripe-elements)
- [mount](https://docs.stripe.com/js#element-mount)
-
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
-
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
-
[https://docs.stripe.com/error-codes#authentication-required](https://docs.stripe.com/error-codes#authentication-required)
-
[https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.](https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions)
- [test cards](https://docs.stripe.com/testing)
- [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions)