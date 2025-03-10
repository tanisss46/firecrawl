# Use Payment Element across multiple processors

## Learn how to collect card details with Payment Element and use them with a third-party processor.

Use [Payment Element](https://docs.stripe.com/payments/payment-element) to build
a custom payment flow that allows you to collect card details, create a
[PaymentMethod](https://docs.stripe.com/api/payment_methods), and
[forward](https://docs.stripe.com/api/forwarding/request) the payment method to
a third-party processor.

#### Request access

To gain access to use Stripe’s forwarding service, contact [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

Client

Server

Stripe

Third-party processor

Create a PaymentMethod

Process the payment on your server

Call the Vault and Forward API with the provided payment method

Stripe forwards the request with card data

Third-party processor returns a response

Stripe redacts identified PCI-sensitive data and relays the response

Handle server response

Forward card details to a third-party processor[Create a
PaymentMethodClient-side](https://docs.stripe.com/payments/forwarding-third-party-processors#create-payment-method)
Use a Payment Element to collect payment details. If you’re not integrated with
the Payment Element, learn how to [get
started](https://docs.stripe.com/payments/accept-a-payment). After the customer
submits your payment form, call
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method)
to create a [PaymentMethod](https://docs.stripe.com/api/payment_methods). Pass
the PaymentMethod ID to the ForwardingRequest endpoint on your server.

HTML + JSReact
```
// Set your publishable key: remember to change this to your live publishable
key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const options = {
 mode: 'payment',
 amount: 1099,
 currency: 'usd',
 paymentMethodCreation: 'manual',
 // Fully customizable with appearance API.
 appearance: {
 theme: 'stripe'
 }
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

const paymentElementOptions = {
layout: "tabs",
};

// Create and mount the Payment Element
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');

const form = document.getElementById('payment-form');
const submitBtn = document.getElementById('submit');

const handleError = (error) => {
 const messageContainer = document.querySelector('#error-message');
 messageContainer.textContent = error.message;
 submitBtn.disabled = false;
}

form.addEventListener('submit', async (event) => {
 // We don't want to let default form submission happen here,
 // which would refresh the page.
 event.preventDefault();

 // Prevent multiple form submissions
 if (submitBtn.disabled) {
 return;
 }

 // Disable form submission while loading
 submitBtn.disabled = true;

 // Trigger form validation and wallet collection
 const { error: submitError } = await elements.submit();
 if (submitError) {
 handleError(submitError);
 return;
 }

// Create the PaymentMethod using the details collected by the Payment Element
 const { error, paymentMethod } = await stripe.createPaymentMethod({
 elements,
 params: {
 billing_details: {
 name: 'John Doe',
 }
 }
 });

 if (error) {
 // This point is only reached if there's an immediate error when
// creating the PaymentMethod. Show the error to your customer (for example,
payment details incomplete)
 handleError(error);
 return;
 }

 // Call the ForwardingRequest endpoint on your server
 const res = await fetch("/create-forwarding-request", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify({
 paymentMethodId: paymentMethod.id,
 }),
 });
 const data = await res.json();

 // Handle the response or errors
 handleServerResponse(data);
});
```

[Create a
ForwardingRequest](https://docs.stripe.com/payments/forwarding-third-party-processors#create-forwarding-request)
Contact Stripe support to
[configure](https://docs.stripe.com/payments/vault-and-forward#configuring) your
destination endpoint and begin forwarding transactions. Send the card details to
this test endpoint before you connect your integration with your third-party
processor.

```
const stripe = require("stripe")("sk_test_BQokikJOvBiI2HlWgH4olfQ2");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());
app.use(express.static("."));

app.post('/create-forwarding-request', async (req, res) => {
 try {
 const forwardedReq = await stripe.forwarding.requests.create(
 {
 payment_method: req.body.paymentMethodId,
 url: '{{DESTINATION_ENDPOINT}}',
 request: {
 headers: [{
 name: 'Destination-API-Key',
 value: '{{DESTINATION_API_KEY}}'
 },{
 name: 'Destination-Idempotency-Key',
 value: '{{DESTINATION_IDEMPOTENCY_KEY}}'
 }],
 body: JSON.stringify({
 "amount": {
 "currency": "USD",
 "value": 1099
 },
 "reference": "Your order number",
 "card": {
 "number": "",
 "exp_month": "",
 "exp_year": "",
 "cvc": "",
 "name": "",
 }
 })
 },
replacements: ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name'],
 }
 );

 if (forwardedReq.response_details.status != 200) {
 // Return error based on third-party API response code
 } else {
 // Parse and handle the third-party API response
const forwardedResult = JSON.parse(forwardedReq.response_details.body);
 res.json({
 status: forwardedReq.response_details.status
 });
 }
 } catch (err) {
 res.json({
 error: err
 });
 }
});

app.listen(3000, () => {
 console.log('Running on port 3000');
});
```

[Handle the
ResponseClient-side](https://docs.stripe.com/payments/forwarding-third-party-processors#handle-response)
After you send the request, you must handle the response.

```
const handleServerResponse = async (response) => {
 if (response.error) {
 // Show error on payment form
 } else if (response.status != 200) {
 // Show error based on response code
 } else {
 // Parse the response body to render your payment form
 }
}
```

## Links

- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [forward](https://docs.stripe.com/api/forwarding/request)
- [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)
- [get started](https://docs.stripe.com/payments/accept-a-payment)
-
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [configure](https://docs.stripe.com/payments/vault-and-forward#configuring)