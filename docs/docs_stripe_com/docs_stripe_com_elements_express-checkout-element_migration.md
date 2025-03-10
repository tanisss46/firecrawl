# Migrate to the Express Checkout Element

## Migrate your existing integration with the Payment Request Button Element to the Express Checkout Element.

The [Payment Request Button
Element](https://docs.stripe.com/stripe-js/elements/payment-request-button)
allows you to accept card payments only through [Apple
Pay](https://docs.stripe.com/apple-pay), [Google
Pay](https://docs.stripe.com/google-pay), or
[Link](https://docs.stripe.com/payments/link). When you migrate to the [Express
Checkout Element](https://docs.stripe.com/elements/express-checkout-element),
you can accept card or [wallet](https://docs.stripe.com/payments/wallets)
payments through one or more payment buttons, including
[PayPal](https://docs.stripe.com/payments/paypal). See the [comparison
guide](https://docs.stripe.com/elements/express-checkout-element/comparison) for
more details.

If your existing integration usesDo the following[Payment
Intents](https://docs.stripe.com/api/payment_intents) API to create and track
payments or save card details during a paymentFollow the steps in this guide to
use the Express Checkout Element.[Charges](https://docs.stripe.com/api/charges)
API with tokensMigrate to the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration#web) before
proceeding.[Enable payment
methods](https://docs.stripe.com/elements/express-checkout-element/migration#enable-payment-methods)
Enable the payment methods you want to support in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). You must
enable at least one payment method.

By default, Stripe enables cards and other common payment methods. You can
enable additional payment methods that are relevant for your business and
customers. See the [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
for product and payment method support and our [pricing
page](https://stripe.com/pricing/local-payment-methods) for fees.

[Update Elements
instanceClient-side](https://docs.stripe.com/elements/express-checkout-element/migration#one-time-update-elements)
Next, update your client-side code to pass the mode (payment), amount, and
currency. These values determine which payment methods to show to your
customers.

For example, if you pass the `eur` currency on the `PaymentIntent` and enable
OXXO in the Dashboard, your customer won’t see OXXO because OXXO doesn’t support
`eur` payments.

Stripe evaluates the currency, payment method restrictions, and other parameters
to determine the list of supported payment methods. We prioritize payment
methods that increase conversion and are most relevant to the currency and
customer location.

HTML + JSReactBeforeAfter
```
const stripe =
 Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
```

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const options = {
 mode: 'payment',
 amount: 1099,
 currency: 'usd',
};
const elements = stripe.elements(options);
```

[OptionalSave payment details during a
payment](https://docs.stripe.com/elements/express-checkout-element/migration#one-time-save-payment-details)[Update
your PaymentIntent creation
callServer-side](https://docs.stripe.com/elements/express-checkout-element/migration#one-time-payment-intent)
The `PaymentIntent` includes the payment methods shown to customers during
checkout. You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia" \
 -d "amount"=1099 \
 -d "currency"="usd" \
 -d "automatic_payment_methods[enabled]"=true \
```

If your existing integration supports multiple payment methods or you want to
accept payment methods other than cards, you can [enable more payment
methods](https://dashboard.stripe.com/settings/payment_methods) in the
Dashboard.

[Add the Express Checkout
ElementClient-side](https://docs.stripe.com/elements/express-checkout-element/migration#one-time-add-express-checkout-element)
Replace the Payment Request Button Element with the Express Checkout Element.
The examples below demonstrate how to replace `PaymentRequestButtonElement` with
`ExpressCheckoutElement`.

You no longer need to create a `paymentRequest` object. Instead, pass the
options when creating the `ExpressCheckoutElement`.

HTML + JSReactBeforeAfter
```
<div id="payment-request-button">
</div>
```

```
<div id="express-checkout-element">
 <!-- Mount the Express Checkout Element here -->
</div>
```

BeforeAfter
```
const paymentRequest = stripe.paymentRequest({
 country: 'US',
 currency: 'usd',
 total: {
 label: 'Demo total',
 amount: 1099,
 },
 requestPayerName: true,
 requestPayerEmail: true,
});
const paymentRequestButton = elements.create('paymentRequestButton', {
 paymentRequest: paymentRequest,
});
paymentRequestButton.mount("#payment-request-button");
paymentRequest.canMakePayment().then(function(result) {
 if (result) {
 prButton.mount('#payment-request-button');
 } else {
 document.getElementById('payment-request-button').style.display = 'none';
 }
});
```

```
const expressCheckoutElement = elements.create("expressCheckout", {
 emailRequired: true
});
expressCheckoutElement.mount("#express-checkout-element");
```

[OptionalRequest an Apple Pay merchant token
(MPAN)](https://docs.stripe.com/elements/express-checkout-element/migration#mpan)[OptionalListen
to the ready
event](https://docs.stripe.com/elements/express-checkout-element/migration#ready-event)[OptionalStyle
the Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element/migration#customize-express-checkout-element)[Update
the confirm payment
methodClient-side](https://docs.stripe.com/elements/express-checkout-element/migration#one-time-update-method)
Listen to the
[confirm](https://docs.stripe.com/js/elements_object/express_checkout_element_confirm_event)
event to handle confirmation. To collect and submit payment information to
Stripe, use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
instead of individual confirmation methods like `stripe.confirmCardPayment`.

Instead of a PaymentMethod ID, `stripe.confirmPayment` uses the Elements
instance from the Express Checkout Element and the client secret from the
created `PaymentIntent`.

When called, `stripe.confirmPayment` attempts to complete any required actions,
such as authenticating your customers by displaying a 3DS dialog or redirecting
them to a bank authorization page. After confirmation completes, users are
directed to the
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
that you configured, which corresponds to a page on your website that provides
the payment status.

If you want the checkout flow for card payments to redirect only for payment
methods that require it, you can set
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
to `if_required`. This doesn’t apply to the Express Checkout Element.

The example below replaces `stripe.confirmCardPayment` with
`stripe.confirmPayment`.

HTML + JSReactBeforeAfter
```
paymentRequest.on('paymentmethod', function(ev) {
 stripe.confirmCardPayment(
 '{{CLIENT_SECRET}}',
 {payment_method: ev.paymentMethod.id},
 {handleActions: false}
 ).then(function(confirmResult) {
 if (confirmResult.error) {
 ev.complete('fail');
 } else {
 ev.complete('success');
 if (confirmResult.paymentIntent.status === "requires_action") {
 stripe.confirmCardPayment(clientSecret).then(
 function(result) {
 if (result.error) {
// The payment failed -- ask your customer for a new payment method.
 } else {
 // The payment succeeded.
 }
 }
 );
 } else {
 // The payment succeeded.
 }
 }
 });
});
```

```
expressCheckoutElement.on('confirm', async (event) => {
 const {error} = await stripe.confirmPayment({
 // `Elements` instance that's used to create the Express Checkout Element.
 elements,
 // `clientSecret` from the created PaymentIntent
 clientSecret,
 confirmParams: {
 return_url: 'https://example.com/order/123/complete',
 },
 // Uncomment below if you only want redirect for redirect-based payments.
 // redirect: 'if_required',
 });

 if (error) {
// This point is reached only if there's an immediate error when confirming the
payment. Show the error to your customer (for example, payment details
incomplete).
 } else {
 // Your customer will be redirected to your `return_url`.
 }
});
```

[Handle post-payment
eventsServer-side](https://docs.stripe.com/elements/express-checkout-element/migration#post-payment)
Stripe sends a
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
event when the payment completes. Use the [Dashboard webhook
tool](https://dashboard.stripe.com/webhooks) or follow the [webhook
guide](https://docs.stripe.com/webhooks/quickstart) to receive these events and
run actions, such as sending an order confirmation email to your customer,
logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On
the client, the customer could close the browser window or quit the app before
the callback executes, and malicious clients could manipulate the response.
Setting up your integration to listen for asynchronous events is what enables
you to accept [different types of payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

In addition to handling the `payment_intent.succeeded` event, we recommend
handling these other events when collecting payments with the Payment Element:

EventDescriptionAction[payment_intent.succeeded](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.succeeded)Sent
when a customer successfully completes a payment.Send the customer an order
confirmation and fulfill their
order.[payment_intent.processing](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.processing)Sent
when a customer successfully initiates a payment, but the payment has yet to
complete. This event is most commonly sent when the customer initiates a bank
debit. It’s followed by either a `payment_intent.succeeded` or
`payment_intent.payment_failed` event in the future.Send the customer an order
confirmation that indicates their payment is pending. For digital goods, you
might want to fulfill the order before waiting for payment to
complete.[payment_intent.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent
when a customer attempts a payment, but the payment fails.If a payment
transitions from `processing` to `payment_failed`, offer the customer another
attempt to pay.

## Links

- [Payment Request Button
Element](https://docs.stripe.com/stripe-js/elements/payment-request-button)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [Link](https://docs.stripe.com/payments/link)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [wallet](https://docs.stripe.com/payments/wallets)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [comparison
guide](https://docs.stripe.com/elements/express-checkout-element/comparison)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Charges](https://docs.stripe.com/api/charges)
- [Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration#web)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing page](https://stripe.com/pricing/local-payment-methods)
- [React Stripe.js](https://github.com/stripe/react-stripe-js)
-
[confirm](https://docs.stripe.com/js/elements_object/express_checkout_element_confirm_event)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
-
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
- [Dashboard webhook tool](https://dashboard.stripe.com/webhooks)
- [webhook guide](https://docs.stripe.com/webhooks/quickstart)
- [different types of payment
methods](https://stripe.com/payments/payment-methods-guide)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.succeeded)
-
[payment_intent.processing](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.processing)
-
[payment_intent.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)