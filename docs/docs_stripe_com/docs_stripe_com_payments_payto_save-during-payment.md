# Save a mandate for future PayTo paymentsInvite only

## Learn how to collect a PayTo payment and authorize future payments.

PayTo allows customers in Australia to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
PayTo agreements for one-off and recurring payments in their banking apps.
[Customers](https://docs.stripe.com/api/customers) pay with PayTo by receiving
notification of a pending agreement request, authorizing the terms of the
agreement, then returning to your app where you get [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

Setting up a PayTo agreement for future payments allows you to collect future
recurring payments without needing customer authorization again. Customers can
view, manage, pause, and cancel their PayTo agreements in their banking apps.

#### Caution

Stripe doesn’t support modification or pausing of PayTo agreements by customers.
If a customer attempts to pause or modify an agreement, we cancel the agreement
and send you a [mandate.updated
webhook](https://docs.stripe.com/api/events/types#event_types-mandate.updated).
After receiving the webhook, you can reach out to your customer to find out why
they adjusted their agreement, as well as setup a new agreement.

Advanced integrationDirect API
To accept PayTo payments, create a
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) object to
track a payment, collect payment method details, then submit the payment to
Stripe for processing. Stripe uses the PaymentIntent to track and handle all the
states of the payment until the payment completes. Use the ID of the
[Mandate](https://docs.stripe.com/api/mandates) collected from your initial
PayTo PaymentIntent to create future payments.

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
StripeServer-side](https://docs.stripe.com/payments/payto/save-during-payment#web-set-up-stripe)
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
CustomerServer-side](https://docs.stripe.com/payments/payto/save-during-payment#create-customer)
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
PaymentIntentServer-side](https://docs.stripe.com/payments/payto/save-during-payment#web-create-payment-intent)
Create a PaymentIntent on your server and specify the `amount` to collect, the
`aud` currency, the customer ID, and `off_session` as an argument for [setup
future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
The minimum charge amount is 0.50 AUD and PayTo doesn’t support other
currencies. If you have an existing [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) integration, add `payto`
to the list of [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types).

You can specify the terms of the agreement for your customer’s consent in the
[PayTo payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-payto).

#### Common mistake

The payment method options `amount` must match the PaymentIntent `amount` unless
you set the `amount_type` to `maximum`, in which case you can set payment method
options value that’s higher than the PaymentIntent.

The following code sample shows a PaymentIntent amount of 10 AUD and a payment
method options amount of 1500 AUD because the `amount_type` is `maximum`.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=aud \
 -d "payment_method_types[]"=payto \
 -d customer={{CUSTOMER_ID}} \
 -d setup_future_usage=off_session \
 -d "payment_method_options[payto][mandate_options][amount_type]"=maximum \
 -d "payment_method_options[payto][mandate_options][payment_schedule]"=annual \
 -d "payment_method_options[payto][mandate_options][amount]"=150000 \
 -d "payment_method_options[payto][mandate_options][payments_per_period]"=13 \
 -d "payment_method_options[payto][mandate_options][end_date]"=2036-12-25 \
 -d "payment_method_options[payto][mandate_options][purpose]"=mortgage
```

Stripe supports various types of agreements, with controls for the amount,
duration, cadence, and purpose of the agreement. Specify agreement terms that
match your requirements as closely as possible—customers see these precise terms
at authorization time, so accuracy can improve your conversion rate.

The default `purpose` is set to `retail`. Override this field using [any of the
valid
values](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-payto-mandate_options-purpose)
if `retail` doesn’t accurately represent the purpose of the agreement.

### Retrieve the client secret

The PaymentIntent includes a [client
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
 intent = # ... Create or retrieve the PaymentIntent
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

[Collect payment method details and submit the
paymentClient-side](https://docs.stripe.com/payments/payto/save-during-payment#web-collect-payment-method-details)
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
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to complete the payment using details from the Payment Element. This sends an
authorization request to the buyer.

#### Note

`stripe.confirmPayment` might take several seconds to complete while waiting for
customers to authorize the payment. During that time, disable your form from
being resubmitted and show a waiting indicator like a spinner. If you receive an
error, show it to the customer, re-enable the form, and hide the waiting
indicator.

HTML + JSReact
```
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {error, paymentIntent} = await stripe.confirmPayment({
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
 },
 });

 const message = document.querySelector('#message')
 if (error) {
 // This point will only be reached if there is an immediate error when
 // confirming the payment. Show error to your customer (for example, payment
 // details incomplete)
 message.innerText = error.message;
 } else {
 // This will execute if the confirm request is successful, or if the
 // payment fails asynchronously.
 switch (paymentIntent.status) {
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
 // payment again
 break;

 default:
 message.innerText = 'Something went wrong.';
 break;
 }
 }
});
```

[Charge the PayTo PaymentMethod
later](https://docs.stripe.com/payments/payto/save-during-payment#web-charge-payto-pm)
When you need to charge your customer again, create a new PaymentIntent. To find
the mandate ID, customer ID, and payment method ID,
[retrieve](https://docs.stripe.com/api/payment_intents/retrieve) the previous
PaymentIntent and [expand](https://docs.stripe.com/api/expanding_objects) the
`latest_charge` field.

```
curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=latest_charge
```

View the necessary IDs in the response below.

```
{
 // ...
 "customer": "cus_PW6rQWRGAaBD7z", // <---- Here's the customer
 "latest_charge": {
"payment_method": "pm_1Ok4l9A8DuEjWaGwhB4SGrWh", // <---- Here's the payment
method
 "payment_method_details": {
 "payto": {
 "bsb_number": null,
 "last4": null,
"mandate": "mandate_1Ok4lVA8DuEjWaGwu0uTwI94", // <----- Here's the mandate
 "pay_id": "jenny@example.com"
 },
 "type": "payto"
 },
 },
 "payment_method_types": [
 "payto"
 ],
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
integration](https://docs.stripe.com/payments/payto/save-during-payment#web-test-integration)
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
events](https://docs.stripe.com/payments/payto/save-during-payment#web-fulfillment)

## Links

-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [mandate.updated
webhook](https://docs.stripe.com/api/events/types#event_types-mandate.updated)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [Mandate](https://docs.stripe.com/api/mandates)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Register now](https://dashboard.stripe.com/register)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
- [PayTo payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-payto)
- [any of the valid
values](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-payto-mandate_options-purpose)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [enable it](https://docs.stripe.com/security/guide#tls)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [Elements](https://docs.stripe.com/js/elements_object/create)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
- [retrieve](https://docs.stripe.com/api/payment_intents/retrieve)
- [expand](https://docs.stripe.com/api/expanding_objects)