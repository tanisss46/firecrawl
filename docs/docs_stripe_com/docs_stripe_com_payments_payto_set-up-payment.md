# Set up future PayTo paymentsInvite only

## Learn how to set up future PayTo payments.

PayTo allows customers in Australia to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
PayTo agreements for one-off and recurring payments in their banking apps.
[Customers](https://docs.stripe.com/api/customers) pay with PayTo by receiving
notification of a pending agreement request, authorizing the terms of the
agreement, then returning to your app.

Setting up a PayTo agreement for future payments allows you to get customer
authorization now for collecting future payments. Customers can view, manage,
pause, and cancel their PayTo agreements in their banking apps.

#### Caution

Stripe doesn’t support modification or pausing of PayTo agreements by customers.
If a customer attempts to pause or modify an agreement, we cancel the agreement
and send you a [mandate.updated
webhook](https://docs.stripe.com/api/events/types#event_types-mandate.updated).
After receiving the webhook, you can reach out to your customer to find out why
they adjusted their agreement, as well as setup a new agreement.

Advanced integrationDirect API
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, update your integration
to [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

[Set up
StripeServer-side](https://docs.stripe.com/payments/payto/set-up-payment#web-set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

To access the Stripe API from your application, use our official libraries:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create a
CustomerServer-side](https://docs.stripe.com/payments/payto/set-up-payment#create-customer)
Create a [Customer](https://docs.stripe.com/api/customers) after they create an
account with your business and associate it with your internal representation of
their account. This enables you to retrieve and use their saved payment method
details later.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny@example.com"
```

[Create a
SetupIntentServer-side](https://docs.stripe.com/payments/payto/set-up-payment#web-create-setup-intent)
A [SetupIntent](https://docs.stripe.com/api/setup_intents/object) is an object
that represents your intent to collect a future payment from a customer and
tracks the authorization process. To create a SetupIntent that accepts a PayTo
payment method, specify the terms of the agreement, and `payto` in the
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
list. If you maintain a list of payment method types that you pass when creating
a SetupIntent, add `payto` to it.

Specify the terms of the agreement you want your customer to agree to using
[payment method
options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-payto).

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=payto \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_options[payto][mandate_options][amount_type]"=maximum \
 -d "payment_method_options[payto][mandate_options][payment_schedule]"=annual \
 -d "payment_method_options[payto][mandate_options][amount]"=150000 \
 -d "payment_method_options[payto][mandate_options][payments_per_period]"=13 \
 -d "payment_method_options[payto][mandate_options][start_date]"=2026-12-25 \
 -d "payment_method_options[payto][mandate_options][end_date]"=2036-12-25 \
 -d "payment_method_options[payto][mandate_options][purpose]"=mortgage
```

Stripe supports various types of agreements, with controls for the amount,
duration, cadence, and purpose of the agreement. Specify agreement terms that
match your requirements as closely as possible—customers see these precise terms
at authorization time, so accuracy can improve your conversion rate.

The default `purpose` is set to `retail`. Override this field using [any of the
valid
values](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-payto-mandate_options-purpose)
if `retail` doesn’t accurately represent the purpose of the agreement.

### Retrieve the client secret

The SetupIntent includes a [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
that the client side uses to securely complete the payment process. You can use
different approaches to pass the client secret to the client side.

Single-page applicationServer-side rendering
Retrieve the client secret from an endpoint on your server, using the browser’s
`fetch` function. This approach is best if your client side is a single-page
application, particularly one built with a modern frontend framework like React.
Create the server endpoint that serves the client secret:

```
get '/secret' do
 intent = # ... Create or retrieve the SetupIntent
 {client_secret: intent.client_secret}.to_json
end
```

And then fetch the client secret with JavaScript on the client side:

```
(async () => {
 const response = await fetch('/secret');
 const {client_secret: clientSecret} = await response.json();
 // Render the form using the clientSecret
})();
```

[Collect payment method details and submit the request for
authorizationClient-side](https://docs.stripe.com/payments/payto/set-up-payment#web-collect-payment-method-details)
Collect payment details on the client with the [Payment
Element](https://docs.stripe.com/payments/payment-element). The Payment Element
is a prebuilt UI component that simplifies collecting payment details for a
variety of payment methods.

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
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx', {
 betas: 'payto_pm_beta_1',
});
```

### Add the Payment Element to your payment page

The Payment Element needs a place to live on your payment page. Create an empty
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

When the previous form loads, create an instance of the Payment Element and
mount it to the container DOM node. Pass the [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
from the previous step into `options` when you create the
[Elements](https://docs.stripe.com/js/elements_object/create) instance:

Handle the client secret carefully because it can complete the charge. Don’t log
it, embed it in URLs, or expose it to anyone but the customer.

```
const options = {
 clientSecret: '{{CLIENT_SECRET}}',
 // Fully customizable with appearance API.
 appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form, passing the client
secret obtained in a previous step
const elements = stripe.elements(options);
// Optional: Autofill user's saved payment methods. If the customer's
// email is known when the page is loaded, you can pass the email
// to the linkAuthenticationElement on mount:
//
// linkAuthenticationElement.mount("#link-authentication-element", {
// defaultValues: {
// email: 'jenny.rosen@example.com',
// }
// })

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

Use
[stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup) to
complete the setup using details from the Payment Element. This sends an
authorization request to the buyer.

#### Note

`stripe.confirmSetup` might take several seconds to complete while waiting for
customers to authorize the payment. During that time, disable your form from
being resubmitted and show a waiting indicator like a spinner. If you receive an
error, show it to the customer, re-enable the form, and hide the waiting
indicator.

HTML + JSReact
```
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {error, setupIntent} = await stripe.confirmSetup({
 //`Elements` instance that was used to create the Payment Element
 elements,
 redirect: 'if_required',
 confirmParams: {
 mandate_data: {
 customer_acceptance: {
 type: 'online',
 online: {
 infer_from_client: true,
 },
 },
 }
 }
 });

 const message = document.querySelector('#message')
 if (error) {
 // This point will only be reached if there is an immediate error when
// confirming the SetupIntent. Show error to your customer (for example, payment
 // details incomplete)
 message.innerText = error.message;
 } else {
 // This will execute if the confirm request is successful, or if the
 // setup fails asynchronously.
 switch (setupIntent.status) {
 case 'succeeded':
 message.innerText = 'Success! Payment received.';
 break;

 case 'processing':
message.innerText = "Payment processing. We'll update you when payment is
received.";
 break;

 case 'requires_payment_method':
message.innerText = 'Payment failed. Please try another payment method.';
 // Redirect your user back to your payment page to attempt collecting
 // payment details again
 break;

 default:
 message.innerText = 'Something went wrong.';
 break;
 }
 }
});
```

[Charge the PayTo PaymentMethod
later](https://docs.stripe.com/payments/payto/set-up-payment#web-charge-payto-pm)
When you need to charge your customer, create a new PaymentIntent. Find the
mandate ID, customer ID, and payment method ID by
[retrieving](https://docs.stripe.com/api/setup_intents/retrieve) the previous
SetupIntent.

```
curl https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

View the necessary IDs in the response below.

```
{
 // ...
 "customer": "cus_PW6rQWRGAaBD7z", // <---- Here is the customer
 "mandate": "mandate_1Ok6ZrA8DuEjWaGw2nrO9xeS", // <---- Here is the mandate
 "metadata": {},
 "next_action": null,
 "on_behalf_of": null,
"payment_method": "pm_1Ok4l9A8DuEjWaGwhB4SGrWh", // <---- Here is the payment
method
 "payment_method_configuration_details": null,
 "payment_method_options": {
 "payto": {
 "mandate_options": {
 "amount": 150000,
 "amount_type": "maximum",
 "start_date": "2026-12-25",
 "end_date": "2036-12-25",
 "payment_schedule": "annual",
 "payments_per_period": 13,
 "purpose": "mortgage",
 }
 }
 },
 "payment_method_types": [
 "payto"
 ],
 "single_use_mandate": null,
 "status": "succeeded",
 "usage": "off_session"
 // ...
}
```

Create a PaymentIntent with the PaymentMethod, Mandate, and Customer IDs.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=payto \
 -d amount=1099 \
 -d currency=aud \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d mandate={{MANDATE_ID}} \
 -d confirm=true
```

[Test your
integration](https://docs.stripe.com/payments/payto/set-up-payment#web-test-integration)
Test your PayTo integration with your test API keys by using the various test
PayIDs and bank account details below. Each set of details results in a
different scenario your integration might commonly face in live mode.

PayIDAccount + BSB numbersPayIDDescription`{any_prefix}+succeed@{any_domain}`The
PaymentIntent status transitions from `requires_action` to `processing` after 60
seconds, then transitions to `succeeded` after an additional 2 seconds. The
mandate enters an `active` state.`{any_prefix}+decline@{any_domain}`The
PaymentIntent status transitions from `requires_action` to
`requires_payment_method` after 60 seconds. Stripe returns the
`payment_method_provider_decline` error code and an `invalid_authorization`
decline code. The mandate enters an `inactive`
state.`{any_prefix}+expire@{any_domain}`The PaymentIntent status transitions
from `requires_action` to `requires_payment_method` after 5 minutes. Stripe
returns the `payment_method_provider_decline` error code and a `generic_decline`
decline code. The mandate enters an `inactive`
state.`{any_prefix}+insufficient_funds@{any_domain}`The PaymentIntent status
transitions from `requires_action` to `processing` after 60 seconds, then
transitions to `requires_payment_method` after an additional 2 seconds. Stripe
returns the `payment_method_provider_decline` error code and an
`insufficient_funds` decline code. The mandate enters an `inactive`
state.`{any_prefix}+revoke@{any_domain}`The PaymentIntent status transitions
from `requires_action` to `processing` after 60 seconds then to `succeeded`
after a further 2 seconds. The mandate begins in an `active` state and
transitions to `inactive` after 5 minutes.[OptionalHandle post-payment
events](https://docs.stripe.com/payments/payto/set-up-payment#post-payment-events)

## Links

-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [mandate.updated
webhook](https://docs.stripe.com/api/events/types#event_types-mandate.updated)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Register now](https://dashboard.stripe.com/register)
- [SetupIntent](https://docs.stripe.com/api/setup_intents/object)
-
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
- [payment method
options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-payto)
- [any of the valid
values](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-payto-mandate_options-purpose)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [enable it](https://docs.stripe.com/security/guide#tls)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [Elements](https://docs.stripe.com/js/elements_object/create)
- [stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup)
- [retrieving](https://docs.stripe.com/api/setup_intents/retrieve)