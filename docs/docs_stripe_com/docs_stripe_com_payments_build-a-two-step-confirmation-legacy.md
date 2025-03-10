# Build two-step confirmationLegacy

## Add an optional review page or run validations after a user enters their payment details.

#### Warning

You’re currently viewing an unsupported implementation. If you’re using an older
integration with `createPaymentMethod`, we recommend you use our latest docs to
[Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation)
and [Migrate to Confirmation
Tokens](https://docs.stripe.com/payments/payment-element/migration-ct).

While we recommend the [standard
integration](https://docs.stripe.com/payments/accept-a-payment-deferred) for
most scenarios, this integration allows you to add an extra step in your
checkout. This provides the buyer an opportunity to review their order details
or for you to run additional validations before confirming the order.

[Set up
Stripe](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Enable payment
methods](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#enable-payment-methods)
#### Caution

This integration path doesn’t support BLIK or pre-authorized debits that use the
Automated Clearing Settlement System (ACSS).

View your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) and enable the
payment methods you want to support. You need at least one payment method
enabled to create a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents).

By default, Stripe enables cards and other prevalent payment methods that can
help you reach more customers, but we recommend turning on additional payment
methods that are relevant for your business and customers. See [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
for product and payment method support, and our [pricing
page](https://stripe.com/pricing/local-payment-methods) for fees.

[Collect payment
detailsClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#web-collect-payment-details)
You’re ready to collect payment details on the client with the Payment Element.
The Payment Element is a prebuilt UI component that simplifies collecting
payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information
to Stripe over an HTTPS connection. Avoid placing the Payment Element within
another iframe because some payment methods require redirecting to another page
for payment confirmation.

The checkout page address must start with `https://` rather than `http://` for
your integration to work. You can test your integration without using HTTPS, but
remember to [enable it](https://docs.stripe.com/security/guide#tls) when you’re
ready to accept live payments.

HTML + JSReact
### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js.
Include the Stripe.js script on your checkout page by adding it to the `head` of
your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI
compliant. Don’t include the script in a bundle or host a copy of it yourself.

```
<head>
 <title>Checkout</title>
 <script src="https://js.stripe.com/v3/"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout
page:

```
// Set your publishable key: remember to change this to your live publishable
key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

### Add the Payment Element to your checkout page

The Payment Element needs a place to live on your checkout page. Create an empty
DOM node (container) with a unique ID in your payment form:

```
<form id="payment-form">
 <div id="payment-element">
 <!-- Elements will create form elements here -->
 </div>
 <button id="submit">Submit</button>
 <div id="error-message">
 <!-- Display error message to your customers here -->
 </div>
</form>
```

When the form above has loaded, create an Elements instance with the mode,
amount, and currency. These values determine which payment methods are shown to
your customer.

Then, create an instance of the Payment Element and mount it to the container
DOM node.

```
const options = {
 mode: 'payment',
 amount: 1099,
 currency: 'usd',
 paymentMethodCreation: 'manual',
 // Fully customizable with appearance API.
 appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

The Payment Element renders a dynamic form that allows your customer to pick a
payment method. The form automatically collects all necessary payments details
for the payment method selected by the customer.

You can customize the Payment Element to match the design of your site by
passing the [appearance object](https://docs.stripe.com/elements/appearance-api)
into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address
details. To collect a customer’s full billing address (to calculate the tax for
digital goods and services, for example) or shipping address, use the [Address
Element](https://docs.stripe.com/elements/address-element).

[OptionalCustomize the
layoutClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#customize-layout)[OptionalCustomize
the
appearanceClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#customize-appearance)[OptionalSave
and retrieve customer payment
methods](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#save-payment-methods)[OptionalAdditional
Elements
optionsClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#additional-options)[Create
a
PaymentMethodClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#create-pm)
When the customer submits your payment form, you can create a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) to send to your
server for additional validation or business logic prior to confirmation.

#### Caution

You must immediately use a created PaymentMethod to confirm a PaymentIntent or
SetupIntent and attach it to a [Customer](https://docs.stripe.com/api/customers)
if you intend to use it in the future.

HTML + JSReact
```
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
 const {error: submitError} = await elements.submit();
 if (submitError) {
 handleError(submitError);
 return;
 }

 // Create the PaymentMethod using the details collected by the Payment Element
 const {error, paymentMethod} = await stripe.createPaymentMethod({
 elements,
 params: {
 billing_details: {
 name: 'Jenny Rosen',
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

// Now that you have a PaymentMethod, you can use it in the following steps to
render a confirmation page or run additional validations on the server
});
```

[Show the payment method details on the confirmation
page](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#show-details)
At this point, you have all of the information you need to render the
confirmation page. Call the server to obtain the necessary information and
render the confirmation page accordingly.

```
// Using Express
const express = require('express');
const app = express();
app.use(express.json());

app.post('/summarize-payment', async (req, res) => {
 try {
 let details;
 if (request.body.payment_method_id) {
 const intent = await stripe.paymentIntents.create({
 payment_method: request.body.payment_method_id,
 amount: 1099,
 currency: 'usd',
// In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 automatic_payment_methods: {enabled: true},
 { expand: ['payment_method'] }
 });
 details = summarizePaymentMethod(intent.payment_method);
 }
 // Send the response to the client
 response.send(generateResponse(details));
 } catch (e) {
 // Display error on client
 return response.send({ error: e.message });
 }
});

function summarizePaymentMethod(paymentMethod) {
 // Use paymentMethod.type to derive the applicable summary fields for your UI
}
```

```
const fetchAndRenderSummary = async () => {
 const res = await fetch('/summarize-payment', {
 method: "POST",
 body: JSON.stringify({ payment_method_id: '{PAYMENT_METHOD_ID}' });
 });

 const summary = await res.json();

 // Render the summary object returned by your server
};
```

[Submit the payment to
Stripe](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy#submit-payment)
When your user confirms their order, use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to complete the payment with the details they entered into the Payment Element.
Provide a
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
to this function to indicate where Stripe needs to redirect the user after they
complete the payment. Your user might be redirected to an intermediate site
first (such as a bank authorization page) before being redirected to the
`return_url`. Card payments immediately redirect to the `return_url` when a
payment is successful.

If you don’t want to redirect for card payments, set
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
to `if_required`. This only redirects customers that check out with
redirect-based payment methods.

```
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {error} = await stripe.confirmPayment({
 clientSecret: '{PAYMENT_INTENT_CLIENT_SECRET}',
 confirmParams: {
 return_url: 'https://example.com/order/123/complete',
 },
 });

 if (error) {
 // This point will only be reached if there is an immediate error when
 // confirming the payment. Show error to your customer.
 const messageContainer = document.querySelector('#error-message');
 messageContainer.textContent = error.message;
 } else {
 // Your customer will be redirected to your `return_url`. For some payment
 // methods like iDEAL, your customer will be redirected to an intermediate
 // site first to authorize the payment, then redirected to the `return_url`.
 }
});
```

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## Links

- [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation)
- [Migrate to Confirmation
Tokens](https://docs.stripe.com/payments/payment-element/migration-ct)
- [standard
integration](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [Register now](https://dashboard.stripe.com/register)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing page](https://stripe.com/pricing/local-payment-methods)
- [enable it](https://docs.stripe.com/security/guide#tls)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [appearance object](https://docs.stripe.com/elements/appearance-api)
- [Address Element](https://docs.stripe.com/elements/address-element)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Customer](https://docs.stripe.com/api/customers)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
-
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)