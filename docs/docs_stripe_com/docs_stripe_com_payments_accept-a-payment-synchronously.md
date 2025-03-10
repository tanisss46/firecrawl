# Accept card payments without webhooks

## Learn how to confirm a card payment on your server and handle card authentication requests.

WebiOSAndroidReact Native
#### Caution

Stripe recommends using the newer [Payment
Element](https://docs.stripe.com/payments/quickstart) instead of the Card
Element. It allows you to accept multiple payment methods with a single Element.
Learn more about [when to use the Card Element and Payment
Element](https://docs.stripe.com/payments/payment-card-element-comparison).

For a wider range of support and future proofing, use the [standard
integration](https://docs.stripe.com/payments/accept-a-payment) for asynchronous
payments.

This integration waits for the returned response from the client and finalizes a
payment on the server, without using
[webhooks](https://docs.stripe.com/webhooks) or processing offline events. While
it may seem simpler, this integration is difficult to scale as your business
grows and has several limitations:

- **Only supports cards**—You’ll have to write more code to support ACH and
popular regional payment methods separately.
- **Double-charge risk**—By synchronously creating a new PaymentIntent each time
your customer attempts to pay, you risk accidentally double-charging your
customer. Be sure to follow [best
practices](https://docs.stripe.com/error-low-level#idempotency).
- **Extra trip to client**—​​Cards with 3D Secure or those that are subject to
regulations such as [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) require
extra steps on the client. ​

Keep these limitations in mind if you decide to use this integration. Otherwise,
use the [standard
integration](https://docs.stripe.com/payments/accept-a-payment).

[Set up
Stripe](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-setup)
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

[Collect card
detailsClient-side](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-collect-card-details)
Collect card information on the client with Stripe.js and Stripe Elements.
Elements is a set of prebuilt UI components for collecting and validating card
number, postal code, and expiration date.

A Stripe Element contains an iframe that securely sends the payment information
to Stripe over an HTTPS connection. The checkout page address must also start
with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. [Enable
it](https://docs.stripe.com/security/guide#tls) when you’re ready to accept live
payments.

HTML + JSReact
Include the [Stripe.js](https://docs.stripe.com/js) script in the head of every
page on your site. Elements is automatically available as a feature of
Stripe.js.

```
<script src="https://js.stripe.com/v3/"></script>
```

Including the script on every page of your site lets you take advantage of
Stripe’s [advanced fraud functionality](https://docs.stripe.com/radar) and
ability to detect anomalous browsing behavior.

### Build the payment form

To securely collect card details from your customers, Elements creates UI
components for you that are hosted by Stripe. They’re then placed into your
payment form as an iframe. To determine where to insert these components, create
empty DOM elements (containers) with unique IDs within your payment form.

```
<form id='payment-form'>
 <label>
 Card details
 <!-- placeholder for Elements -->
 <div id="card-element"></div>
 </label>
 <button type="submit">Submit Payment</button>
</form>
```

Next, create an instance of the [Stripe
object](https://docs.stripe.com/js#stripe-function), providing your publishable
[API key](https://docs.stripe.com/keys) as the first parameter. Afterwards,
create an instance of the [Elements
object](https://docs.stripe.com/js#stripe-elements) and use it to
[mount](https://docs.stripe.com/js#element-mount) a Card element in the relevant
placeholder in the page.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
// Set up Stripe.js and Elements to use in checkout form
const style = {
 base: {
 color: "#32325d",
 fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
 fontSmoothing: "antialiased",
 fontSize: "16px",
 "::placeholder": {
 color: "#aab7c4"
 }
 },
 invalid: {
 color: "#fa755a",
 iconColor: "#fa755a"
 },
};
const cardElement = elements.create('card', {style});
cardElement.mount('#card-element');
```

The `card` Element simplifies the form and minimizes the number of fields
required by inserting a single, flexible input field that securely collects all
necessary card details.

Otherwise, combine `cardNumber`, `cardExpiry`, and `cardCvc` Elements for a
flexible, multi-input card form.

#### Note

Always collect a postal code to increase card acceptance rates and reduce fraud.

The [single line Card
Element](https://docs.stripe.com/js/element/other_element?type=card)
automatically collects and sends the customer’s postal code to Stripe. If you
build your payment form with split Elements ([Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber),
[Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry),
[CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)), add a
separate input field for the customer’s postal code.

### Create a PaymentMethod

Finally, use
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method)
on your client to collect the card details and create a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) when the user
clicks the submit button.

```
const form = document.getElementById('payment-form');
form.addEventListener('submit', async (event) => {
 // We don't want to let default form submission happen here,
 // which would refresh the page.
 event.preventDefault();
 const result = await stripe.createPaymentMethod({
 type: 'card',
 card: cardElement,
 billing_details: {
 // Include any additional collected billing details.
 name: 'Jenny Rosen',
 },
 })
 stripePaymentMethodHandler(result);
});
```

[Submit the PaymentMethod to your
serverClient-side](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-send-to-server)
If the [PaymentMethod](https://docs.stripe.com/api/payment_methods) was created
successfully, send its ID to your server.

```
const stripePaymentMethodHandler = async (result) => {
 if (result.error) {
 // Show error in payment form
 } else {
 // Otherwise send paymentMethod.id to your server (see Step 4)
 const res = await fetch('/pay', {
 method: 'POST',
 headers: { 'Content-Type': 'application/json' },
 body: JSON.stringify({
 payment_method_id: result.paymentMethod.id,
 }),
 })
 const paymentResponse = await res.json();
 // Handle server response (see Step 4)
 handleServerResponse(paymentResponse);
 }
}
```

[Create a
PaymentIntentServer-side](https://docs.stripe.com/payments/accept-a-payment-synchronously#create-payment-intent)
Set up an endpoint on your server to receive the request. This endpoint will
also be used
[later](https://docs.stripe.com/payments/accept-a-payment-synchronously#confirm-payment)
to handle cards that require an extra step of authentication.

[Create a new
PaymentIntent](https://docs.stripe.com/payments/payment-intents#creating-a-paymentintent)
with the ID of the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) created on
your client. You can
[confirm](https://docs.stripe.com/api/payment_intents/confirm) the PaymentIntent
by setting the
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
property to true when the PaymentIntent is created or by calling
[confirm](https://docs.stripe.com/api/payment_intents/confirm) after creation.
[Separate authorization and
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method) is
also supported for card payments.

If the payment requires additional actions such as 3D Secure authentication, the
PaymentIntent’s status will be set to `requires_action`. If the payment failed,
the status is set back to `requires_payment_method` and you should show an error
to your user. If the payment doesn’t require any additional authentication then
a charge is created and the PaymentIntent status is set to `succeeded`.

#### Note

On versions of the API before
[2019-02-11](https://docs.stripe.com/upgrades#2019-02-11),
`requires_payment_method` appears as `requires_source` and `requires_action`
appears as `requires_source_action`.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method"="{{PAYMENT_METHOD_ID}}" \
 -d "amount"=1099 \
 -d "currency"="usd" \
 -d "confirmation_method"="manual" \
 -d "confirm"="true"
```

If you want to save the card to reuse later, create a
[Customer](https://docs.stripe.com/api/customers/create) to store the
[PaymentMethod](https://docs.stripe.com/api/payment_methods) and pass the
following additional parameters when creating the PaymentIntent:

-
[customer](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-customer).
Set to the ID of the [Customer](https://docs.stripe.com/api/customers).
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
Set to `off_session` to tell Stripe that you plan to reuse this PaymentMethod
for off-session payments when your customer is not present. Setting this
property saves the PaymentMethod to the Customer after the PaymentIntent is
confirmed and any required actions from the user are complete. See the code
sample on [saving cards after a
payment](https://github.com/stripe-samples/saving-card-after-payment/tree/master/without-webhooks)
for more details.
[Handle any next
actionsClient-side](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-handle-next-actions)
Write code to handle situations that require your customer to intervene. A
payment normally succeeds after you confirm it on the server in [step
4](https://docs.stripe.com/payments/accept-a-payment-synchronously#create-payment-intent).
However, when the PaymentIntent requires additional action from the customer,
such as authenticating with [3D
Secure](https://docs.stripe.com/payments/3d-secure), this code comes into play.

Use
[stripe.handleCardAction](https://docs.stripe.com/js/payment_intents/handle_card_action)
to trigger the UI for handling customer action. If authentication succeeds, the
PaymentIntent has a status of `requires_confirmation`. Confirm the PaymentIntent
again on your server to finish the payment.

While testing, use a [test card
number](https://docs.stripe.com/testing#regulatory-cards) that requires
authentication (for example, 4000002760003184) to force this flow. Using a card
that doesn’t require authentication (for example, 4242424242424242) skips this
part of the flow and completes at step 4.

```
const handleServerResponse = async (response) => {
 if (response.error) {
 // Show error from server on payment form
 } else if (response.requires_action) {
 // Use Stripe.js to handle the required card action
 const { error: errorAction, paymentIntent } =
 await stripe.handleCardAction(response.payment_intent_client_secret);
 if (errorAction) {
 // Show error from Stripe.js in payment form
 } else {
 // The card action has been handled
 // The PaymentIntent can be confirmed again on the server
 const serverResponse = await fetch('/pay', {
 method: 'POST',
 headers: { 'Content-Type': 'application/json' },
 body: JSON.stringify({ payment_intent_id: paymentIntent.id })
 });
 handleServerResponse(await serverResponse.json());
 }
 } else {
 // Show success message
 }
}
```

#### Note

`stripe.handleCardAction` may take several seconds to complete. During that
time, disable your form from being resubmitted and show a waiting indicator like
a spinner. If you receive an error, show it to the customer, re-enable the form,
and hide the waiting indicator. If the customer must perform additional steps to
complete the payment, such as authentication, Stripe.js walks them through that
process.

[Confirm the PaymentIntent
againServer-side](https://docs.stripe.com/payments/accept-a-payment-synchronously#confirm-payment)
This code is only executed when a payment requires additional
authentication—just like the handling in the previous step. The code itself
isn’t optional because any payment could require this extra step.

Using the same endpoint you set up
[above](https://docs.stripe.com/payments/accept-a-payment-synchronously#create-payment-intent),
confirm the PaymentIntent again to finalize the payment and fulfill the order.
Make sure this confirmation happens within one hour of the payment attempt.
Otherwise, the payment fails and transitions back to `requires_payment_method`.

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST"
```

[Test the
integration](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-test-integration)
​​Several test cards are available for you to use in a sandbox to make sure this
integration is ready. Use them with any CVC and an expiration date in the
future.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000002500003155Requires authentication. Stripe triggers a modal asking
for the customer to authenticate.4000000000009995Always fails with a decline
code of `insufficient_funds`.
For the full list of test cards see our guide on
[testing](https://docs.stripe.com/testing).

[OptionalRecollect a
CVC](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-recollect-cvc)

## Links

- [Payment Element](https://docs.stripe.com/payments/quickstart)
- [when to use the Card Element and Payment
Element](https://docs.stripe.com/payments/payment-card-element-comparison)
- [standard integration](https://docs.stripe.com/payments/accept-a-payment)
- [webhooks](https://docs.stripe.com/webhooks)
- [migration guide](https://docs.stripe.com/payments/payment-intents/migration)
- [best practices](https://docs.stripe.com/error-low-level#idempotency)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Register now](https://dashboard.stripe.com/register)
- [Enable it](https://docs.stripe.com/security/guide#tls)
- [Stripe.js](https://docs.stripe.com/js)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [advanced fraud functionality](https://docs.stripe.com/radar)
- [Stripe object](https://docs.stripe.com/js#stripe-function)
- [API key](https://docs.stripe.com/keys)
- [Elements object](https://docs.stripe.com/js#stripe-elements)
- [mount](https://docs.stripe.com/js#element-mount)
- [View full
sample](https://github.com/stripe-samples/accept-a-payment/blob/main/custom-payment-flow/client/html/card.js#L63-L73)
- [single line Card
Element](https://docs.stripe.com/js/element/other_element?type=card)
- [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber)
- [Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry)
- [CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)
-
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Create a new
PaymentIntent](https://docs.stripe.com/payments/payment-intents#creating-a-paymentintent)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
- [confirm](https://docs.stripe.com/api/payment_intents/confirm)
-
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
- [Separate authorization and
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [2019-02-11](https://docs.stripe.com/upgrades#2019-02-11)
- [Customer](https://docs.stripe.com/api/customers/create)
-
[customer](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-customer)
- [Customer](https://docs.stripe.com/api/customers)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [saving cards after a
payment](https://github.com/stripe-samples/saving-card-after-payment/tree/master/without-webhooks)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
-
[stripe.handleCardAction](https://docs.stripe.com/js/payment_intents/handle_card_action)
- [test card number](https://docs.stripe.com/testing#regulatory-cards)
- [testing](https://docs.stripe.com/testing)