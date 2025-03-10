# Build two-step confirmation

## Add an optional review page or run validations after a user enters their payment details.

While we recommend the [standard
integration](https://docs.stripe.com/payments/accept-a-payment-deferred) for
most scenarios, this integration allows you to add an extra step in your
checkout. This provides the buyer an opportunity to review their order details
or for you to run additional validations before confirming the order.

[Set up
Stripe](https://docs.stripe.com/payments/build-a-two-step-confirmation#set-up-stripe)
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
methods](https://docs.stripe.com/payments/build-a-two-step-confirmation#enable-payment-methods)
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
detailsClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#web-collect-payment-details)
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
layoutClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#customize-layout)[OptionalCustomize
the
appearanceClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#customize-appearance)[OptionalSave
and retrieve customer payment
methods](https://docs.stripe.com/payments/build-a-two-step-confirmation#save-payment-methods)[OptionalAdditional
Elements
optionsClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#additional-options)[Create
a
ConfirmationTokenClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#create-ct)
#### Use createPaymentMethod through a legacy implementation

If you’re using a legacy implementation, you might be using the information from
`stripe.createPaymentMethod` to finalize payments on the server. Although we
encourage you to follow this guide to [Migrate to Confirmation
Tokens](https://docs.stripe.com/payments/payment-element/migration-ct), you can
still access our old documentation to [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy).

When the customer submits your payment form, call
[stripe.createConfirmationToken](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token)
to create a [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens)
to send to your server for additional validation or business logic before
confirmation. You can inspect the
[payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)
field to run the additional logic.

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

// Create the ConfirmationToken using the details collected by the Payment
Element
 const {error, confirmationToken} = await stripe.createConfirmationToken({
 elements,
 params: {
 payment_method_data: {
 billing_details: {
 name: 'Jenny Rosen',
 }
 }
 }
 });

 if (error) {
 // This point is only reached if there's an immediate error when
// creating the ConfirmationToken. Show the error to your customer (for example,
payment details incomplete)
 handleError(error);
 return;
 }

// Now that you have a ConfirmationToken, you can use it in the following steps
to render a confirmation page or run additional validations on the server
 return fetchAndRenderSummary(confirmationToken)
});
```

[Show the payment details on the confirmation
page](https://docs.stripe.com/payments/build-a-two-step-confirmation#show-details)
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
 // Retrieve the confirmationTokens and generate the response
const confirmationToken = await
stripe.confirmationTokens.retrieve(req.body.confirmation_token_id);
 const response = summarizePaymentDetails(confirmationToken);

 // Send the response to the client
 res.json(response);
 } catch (e) {
 // Display error on client
 return res.json({ error: e.message });
 }
});

function summarizePaymentDetails(confirmationToken) {
// Use confirmationToken.payment_method_preview to derive the applicable summary
fields for your UI
 return {
 type: confirmationToken.payment_method_preview.type,
 // Add other values as needed here
 };
}
```

```
const fetchAndRenderSummary = async (confirmationToken) => {
 const res = await fetch('/summarize-payment', {
 method: "POST",
 body: JSON.stringify({ confirmation_token_id: confirmationToken.id }),
 });

 const summary = await res.json();

 // Render the summary object returned by your server
};
```

[Create a
PaymentIntentServer-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#create-intent)
#### Run custom business logic immediately before payment confirmation

Navigate to [step
5](https://docs.stripe.com/payments/finalize-payments-on-the-server?platform=web&type=payment#submit-payment)
in the finalize payments guide to run your custom business logic immediately
before payment confirmation. Otherwise, follow the steps below for a simpler
integration, which uses `stripe.confirmPayment` on the client to both confirm
the payment and handle any next actions.

When the customer submits your payment form, use a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) to facilitate
the confirmation and payment process. Create a PaymentIntent on your server with
an `amount` and `currency` enabled. In the latest version of the API, specifying
the `automatic_payment_methods` parameter is optional because Stripe enables its
functionality by default. You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow. To prevent malicious customers
from choosing their own prices, always decide how much to charge on the
server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret).
Return this value to your client for Stripe.js to use to securely complete the
payment process.

```
require 'stripe'
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/create-intent' do
 intent = Stripe::PaymentIntent.create({
 # To allow saving and retrieving payment methods, provide the Customer ID.
 customer: customer.id,
# In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 automatic_payment_methods: {enabled: true},
 amount: 1099,
 currency: 'usd',
 })
 {client_secret: intent.client_secret}.to_json
end
```

[Submit the payment to
StripeClient-side](https://docs.stripe.com/payments/build-a-two-step-confirmation#submit-the-payment)
Use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to complete the payment using details from the Payment Element.

Provide the `confirmation_token` parameter with the ID of the ConfirmationToken
you created on the previous page, which contains the payment information
collected from the Payment Element.

Provide a
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
to this function to indicate where Stripe redirects the user after they complete
the payment. Your user might be initially redirected to an intermediate site,
such as a bank authorization page, before being redirected to the `return_url`.
Card payments immediately redirect to the `return_url` when a payment is
successful.

If you don’t want to redirect for card payments after payment completion, you
can set
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
to `if_required`. This only redirects customers that check out with
redirect-based payment methods.

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

 // Create the PaymentIntent and obtain clientSecret
 const res = await fetch("/create-intent", {
 method: "POST",
 });

 const {client_secret: clientSecret} = await res.json();

// Confirm the PaymentIntent using the details collected by the
ConfirmationToken
 const {error} = await stripe.confirmPayment({
 clientSecret,
 confirmParams: {
 confirmation_token: '{{CONFIRMATION_TOKEN_ID}}',
 return_url: 'https://example.com/order/123/complete',
 },
 });

 if (error) {
 // This point is only reached if there's an immediate error when
// confirming the payment. Show the error to your customer (for example, payment
details incomplete)
 handleError(error);
 } else {
 // Your customer is redirected to your `return_url`. For some payment
 // methods like iDEAL, your customer is redirected to an intermediate
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

## See also

[Design an
integration](https://docs.stripe.com/payments/payment-element/design-an-integration)

## Links

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
- [Migrate to Confirmation
Tokens](https://docs.stripe.com/payments/payment-element/migration-ct)
- [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy)
-
[stripe.createConfirmationToken](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token)
- [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens)
-
[payment_method_preview](https://docs.stripe.com/api/confirmation_tokens/object#confirmation_token_object-payment_method_preview)
- [step
5](https://docs.stripe.com/payments/finalize-payments-on-the-server?platform=web&type=payment#submit-payment)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
-
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)
- [Design an
integration](https://docs.stripe.com/payments/payment-element/design-an-integration)