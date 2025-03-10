# Finalize payments on the serverLegacy

## Build an integration where you render the Payment Element before you create a PaymentIntent or SetupIntent, then confirm the Intent from your server.

WebiOSAndroidReact NativeAccept a paymentSet up a payment methodCreate a
subscription
#### Warning

You’re currently viewing an unsupported implementation. If you’re using an older
integration with `createPaymentMethod`, we recommend you use our latest docs to
[Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server) and
[Migrate to Confirmation
Tokens](https://docs.stripe.com/payments/payment-element/migration-ct).

The Payment Element allows you to accept multiple payment methods using a single
integration. In this integration, you’ll build a custom payment flow where you
render the Payment Element, create the
[PaymentIntent](https://docs.stripe.com/payments/payment-intents), and confirm
the payment from your server.

[Set up
StripeServer-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#set-up-stripe)
First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign
in](https://dashboard.stripe.com/login).

Use our official libraries to access the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Enable payment
methods](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#enable-payment-methods)
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
detailsClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#web-collect-payment-details)
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
layoutClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#customize-layout)[OptionalCustomize
the
appearanceClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#customize-appearance)[OptionalSave
and retrieve customer payment
methods](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#save-payment-methods)[OptionalDynamically
update payment
detailsClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#dynamic-updates)[OptionalAdditional
Elements
optionsClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#additional-options)[Create
the
PaymentMethodClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#create-pm)
When the customer submits your payment form, you can create a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) to send to your
server for additional validation or business logic prior to confirmation.

#### Caution

You must immediately use a created PaymentMethod to confirm a PaymentIntent and
attach it to a [Customer](https://docs.stripe.com/api/customers) if you intend
to use it in the future.

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

 // Create the PaymentIntent
 const res = await fetch("/create-confirm-intent", {
 method: "POST",
 headers: {"Content-Type": "application/json"},
 body: JSON.stringify({
 paymentMethodId: paymentMethod.id,
 }),
 });

 const data = await res.json();

// Handle any next actions or errors. See the Handle any next actions step for
implementation.
 handleServerResponse(data);
});
```

[OptionalInsert custom business
logicServer-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#insert-custom-logic)[Create
and submit the payment to
StripeServer-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#submit-payment)
When the customer submits your payment form, use a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) to facilitate
the confirmation and payment process. Create a PaymentIntent on your server with
an `amount` and `currency` specified. In the latest version of the API,
specifying the `automatic_payment_methods` parameter is optional because Stripe
enables its functionality by default. You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow. To prevent malicious customers
from choosing their own prices, always decide how much to charge on the
server-side (a trusted environment) and not the client.

You can use the PaymentMethod sent by your client to create and confirm the
PaymentIntent in a single request.

#### Note

When confirming an Intent from the server, pass `mandate_data` to acknowledge
that you’ve shown the customer the proper
[terms](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-terms)
for collecting their payment details. To make sure you display the proper terms,
all [Elements](https://docs.stripe.com/js/elements_object/create) options should
match your Intent options (for example,`setup_future_usage`, `amount`, and
`currency`).

```
const stripe = require("stripe")("sk_test_BQokikJOvBiI2HlWgH4olfQ2");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());
app.use(express.static("."));

app.post('/create-confirm-intent', async (req, res) => {
 try {
 const intent = await stripe.paymentIntents.create({
 confirm: true,
 amount: 1099,
 currency: 'usd',
// In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 automatic_payment_methods: {enabled: true},
payment_method: req.body.paymentMethodId, // the PaymentMethod ID sent by your
client
 use_stripe_sdk: true,
 return_url: 'https://example.com/order/123/complete',
 mandate_data: {
 customer_acceptance: {
 type: "online",
 online: {
 ip_address: req.ip,
 user_agent: req.get("user-agent"),
 },
 },
 },
 });
 res.json({
 client_secret: intent.client_secret,
 status: intent.status
 });
 } catch (err) {
 res.json({
 error: err
 })
 }
});

app.listen(3000, () => {
 console.log('Running on port 3000');
});
```

[Handle any next
actionsClient-side](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#next-actions)
When the PaymentIntent requires additional action from the customer, such as
authenticating with 3D Secure or redirecting to a different site, you need to
trigger those actions. Use `stripe.handleNextAction` to trigger the UI for
handling customer action and completing the payment.

```
const handleServerResponse = async (response) => {
 if (response.error) {
 // Show error from server on payment form
 } else if (response.status === "requires_action") {
 // Use Stripe.js to handle the required next action
 const {
 error,
 paymentIntent
 } = await stripe.handleNextAction({
 clientSecret: response.clientSecret
 });

 if (error) {
 // Show error from Stripe.js in payment form
 } else {
 // Actions handled, show success message
 }
 } else {
 // No actions needed, show success message
 }
}
```

[OptionalHandle post-payment
events](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy#web-fulfillment)
## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## Links

- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)
- [Migrate to Confirmation
Tokens](https://docs.stripe.com/payments/payment-element/migration-ct)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
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
[terms](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-terms)
- [Elements](https://docs.stripe.com/js/elements_object/create)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)