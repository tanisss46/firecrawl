# Save bank details during an iDEAL payment

## Learn how to save your customer's IBAN bank details from an iDEAL payment.

#### Caution

We recommend that you follow the [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment) guide. If you’ve
already integrated with Elements, see the [Payment Element migration
guide](https://docs.stripe.com/payments/payment-element/migration).

iDEAL is a popular [single
use](https://docs.stripe.com/payments/payment-methods#usage) payment method in
the Netherlands where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. [Customers](https://docs.stripe.com/api/customers) pay with iDEAL
by redirecting to a webview, authorizing the payment, then returning to your app
where you get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

You can also use iDEAL to save your customer’s
[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) bank
details into a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
[PaymentMethod](https://docs.stripe.com/api/payment_methods). You can then use
the SEPA Direct Debit PaymentMethod to [accept
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment) or [set
up a subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit).
This reduces friction for your customer as they don’t have to enter their IBAN
again. You also receive their verified name and validated IBAN.

#### Caution

To use iDEAL to set up SEPA Direct Debit payments, you must activate SEPA Direct
Debit in the
[Dashboard](https://dashboard.stripe.com/account/payments/settings). You must
also comply with the [iDEAL Terms of Service](https://stripe.com/ideal/legal)
and [SEPA Direct Debit Terms of
Service](https://stripe.com/sepa-direct-debit/legal).

WebiOSAndroidReact Native
Accepting iDEAL payments consists of creating a
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) object to
track a payment, collecting payment method details and mandate acknowledgement,
and submitting the payment to Stripe for processing. Stripe uses the
PaymentIntent to track and handle all the states of the payment until the
payment completes. Use the ID of the SEPA Direct Debit
[PaymentMethod](https://docs.stripe.com/api/payment_methods) collected from your
initial iDEAL PaymentIntent to create future payments.

[Set up
StripeServer-side](https://docs.stripe.com/payments/ideal/save-during-payment#web-set-up-stripe)
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

[Create a
CustomerServer-side](https://docs.stripe.com/payments/ideal/save-during-payment#create-customer)
Create a [Customer](https://docs.stripe.com/api/customers) when they create an
account with your business and associate it with your internal representation of
their account. This enables you to retrieve and use their saved payment method
details later.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a
PaymentIntentServer-side](https://docs.stripe.com/payments/ideal/save-during-payment#web-create-payment-intent)
Create a `PaymentIntent` on your server and specify the `amount` to collect, the
`eur` currency, the customer ID, and `off_session` as an argument for [setup
future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
There is no minimum charge amount and iDEAL doesn’t support other currencies. If
you have an existing [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) integration, add `ideal`
to the list of [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types).

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=eur \
 -d "payment_method_types[]"=ideal \
 -d customer={{CUSTOMER_ID}} \
 -d setup_future_usage=off_session
```

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

[Collect payment method
detailsClient-side](https://docs.stripe.com/payments/ideal/save-during-payment#web-collect-payment-method-details)
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
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
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

[Submit the payment to
StripeClient-side](https://docs.stripe.com/payments/ideal/save-during-payment#web-submit-payment)
Use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to complete the payment using details from the Payment Element. Provide a
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
to this function to indicate where Stripe should redirect the user after they
complete the payment. Your user may be first redirected to an intermediate site,
like a bank authorization page, before being redirected to the `return_url`.
Card payments immediately redirect to the `return_url` when a payment is
successful.

HTML + JSReact
```
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {error} = await stripe.confirmPayment({
 //`Elements` instance that was used to create the Payment Element
 elements,
 confirmParams: {
 return_url: 'https://example.com/order/123/complete',
 },
 });

 if (error) {
 // This point will only be reached if there is an immediate error when
 // confirming the payment. Show error to your customer (for example, payment
 // details incomplete)
 const messageContainer = document.querySelector('#error-message');
 messageContainer.textContent = error.message;
 } else {
 // Your customer will be redirected to your `return_url`. For some payment
 // methods like iDEAL, your customer will be redirected to an intermediate
 // site first to authorize the payment, then redirected to the `return_url`.
 }
});
```

#### Note

`stripe.confirmPayment` may take several seconds to complete. During that time,
disable your form from being resubmitted and show a waiting indicator like a
spinner. If you receive an error, show it to the customer, re-enable the form,
and hide the waiting indicator. If the customer must perform additional steps to
complete the payment, such as authentication, Stripe.js walks them through that
process.

If the payment succeeded, the card is saved to the Customer object. This is
reflected on the [PaymentMethod](https://docs.stripe.com/api/payment_methods)’s
[customer](https://docs.stripe.com/api/payment_methods/object#payment_method_object-customer)
field. At this point, associate the ID of the
[Customer](https://docs.stripe.com/api/customers) object with your own internal
representation of a customer, if you have one. Now you can use the stored
PaymentMethod object to collect payments from your customer in the future
without prompting them for their payment details again.

Make sure the `return_url` corresponds to a page on your website that provides
the status of the payment. When Stripe redirects the customer to the
`return_url`, we provide the following URL query parameters:

ParameterDescription`payment_intent`The unique identifier for the
`PaymentIntent`.`payment_intent_client_secret`The [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
of the `PaymentIntent` object.
#### Caution

If you have tooling that tracks the customer’s browser session, you might need
to add the `stripe.com` domain to the referrer exclude list. Redirects cause
some tools to create new sessions, which prevents you from tracking the complete
session.

Use one of the query parameters to retrieve the PaymentIntent. Inspect the
[status of the
PaymentIntent](https://docs.stripe.com/payments/paymentintents/lifecycle) to
decide what to show your customers. You can also append your own query
parameters when providing the `return_url`, which persist through the redirect
process.

HTML + JSReact
```
// Initialize Stripe.js using your publishable key
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

// Retrieve the "payment_intent_client_secret" query parameter appended to
// your return_url by Stripe.js
const clientSecret = new URLSearchParams(window.location.search).get(
 'payment_intent_client_secret'
);

// Retrieve the PaymentIntent
stripe.retrievePaymentIntent(clientSecret).then(({paymentIntent}) => {
 const message = document.querySelector('#message')

 // Inspect the PaymentIntent `status` to indicate the status of the payment
 // to your customer.
 //
 // Some payment methods will [immediately succeed or fail][0] upon
 // confirmation, while others will first enter a `processing` state.
 //
 // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
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
});
```

[Charge the SEPA Direct Debit PaymentMethod
later](https://docs.stripe.com/payments/ideal/save-during-payment#web-charge-sepa-pm)
When you need to charge your customer again, create a new PaymentIntent. Find
the ID of the SEPA Direct Debit payment method by
[retrieving](https://docs.stripe.com/api/payment_intents/retrieve) the previous
PaymentIntent and [expanding](https://docs.stripe.com/api/expanding_objects) the
`latest_charge` field where you will find the `generated_sepa_debit` ID inside
of `payment_method_details`.

```
curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=latest_charge
```

The SEPA Direct Debit payment method ID is the `generated_sepa_debit` ID under
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-ideal)
in the response.

```
{
 "latest_charge": {
 "payment_method_details": {
 "ideal": {
 "bank": "ing",
 "bic": "INGBNL2A",
 "iban_last4": "****",
 "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
 "verified_name": "JENNY ROSEN"
 },
 "type": "ideal"
 },
 },
 "payment_method_options": {
 "ideal": {}
```

See all 30 lines
Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=sepa_debit \
 -d amount=1099 \
 -d currency=eur \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{SEPA_DEBIT_PAYMENT_METHOD_ID}} \
 -d confirm=true
```

[Test your
integration](https://docs.stripe.com/payments/ideal/save-during-payment#test-your-integration)
Use your [test API keys](https://docs.stripe.com/keys#test-live-modes) to
confirm the PaymentIntent. After confirming, you’re redirected to a test page
with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is
successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to
authenticate. The PaymentIntent transitions from `requires_action` to
`requires_payment_method`.

### Test your SEPA Direct Debit integration

EmailPaymentMethod
Set `payment_method.billing_details.email` to one of the following values to
test the PaymentIntent status transitions. You can include your own custom text
at the beginning of the email address followed by an underscore. For example,
`test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct
Debit PaymentMethod that always fails when used with a PaymentIntent.

Email AddressDescription`generatedSepaDebitIntentsSucceed@example.com`The
PaymentIntent status transitions from `processing` to
`succeeded`.`generatedSepaDebitIntentsSucceedDelayed@example.com`The
PaymentIntent status transitions from `processing` to `succeeded` after at least
three minutes.`generatedSepaDebitIntentsFail@example.com`The PaymentIntent
status transitions from `processing` to
`requires_payment_method`.`generatedSepaDebitIntentsFailDelayed@example.com`The
PaymentIntent status transitions from `processing` to `requires_payment_method`
after at least three
minutes.`generatedSepaDebitIntentsSucceedDisputed@example.com`The PaymentIntent
status transitions from `processing` to `succeeded`, but a dispute is created
immediately.[OptionalHandle post-payment
events](https://docs.stripe.com/payments/ideal/save-during-payment#web-fulfillment)[OptionalHandle
the iDEAL redirect
manually](https://docs.stripe.com/payments/ideal/save-during-payment#web-handle-redirect)
## See also

- [Accept a SEPA Direct Debit
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Set up a subscription with SEPA Direct Debit in the
EU](https://docs.stripe.com/billing/subscriptions/sepa-debit)

## Links

- [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment)
- [Payment Element migration
guide](https://docs.stripe.com/payments/payment-element/migration)
- [accepting SEPA Direct Debit
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [set up a
subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [iDEAL Terms of Service](https://stripe.com/ideal/legal)
- [SEPA Direct Debit Terms of
Service](https://stripe.com/sepa-direct-debit/legal)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [Register now](https://dashboard.stripe.com/register)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [enable it](https://docs.stripe.com/security/guide#tls)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [Elements](https://docs.stripe.com/js/elements_object/create)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
-
[customer](https://docs.stripe.com/api/payment_methods/object#payment_method_object-customer)
- [status of the
PaymentIntent](https://docs.stripe.com/payments/paymentintents/lifecycle)
-
[https://stripe.com/docs/payments/payment-methods#payment-notification](https://stripe.com/docs/payments/payment-methods#payment-notification)
- [retrieving](https://docs.stripe.com/api/payment_intents/retrieve)
- [expanding](https://docs.stripe.com/api/expanding_objects)
-
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-ideal)
- [test API keys](https://docs.stripe.com/keys#test-live-modes)