# Migrate to the Payment Element

## Accept many payment methods with a single Element.

#### Note

If your integration still uses the Charges API with tokens, follow the
[Migrating to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration#web) guide
first.

#### Interested in using Stripe Billing, Tax, discounts, shipping, or currency conversion?

We’re developing a Payment Element integration that manages subscriptions, tax,
discounts, shipping, and currency conversion. To learn more, see [Build a
checkout page](https://docs.stripe.com/checkout/custom/quickstart).

Previously, each payment method (cards, iDEAL, and so on) required a separate
Element. By migrating to the Payment Element, you can accept many payment
methods with a single Element.

PaymentIntents and SetupIntents each have their own set of migration guidelines.
See the appropriate guide for your integration path, including example code.

PaymentIntent migrationSetupIntent migration
If your existing integration uses the [Payment
Intents](https://docs.stripe.com/payments/payment-intents) API to create and
track payments or save card details during a payment, follow the steps below to
use the Payment Element.

[Enable payment
methods](https://docs.stripe.com/payments/payment-element/migration#enable-payment-methods)
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

[Update Elements
instanceClient-side](https://docs.stripe.com/payments/payment-element/migration#one-time-update-elements)
Next, update your client-side code to pass `mode`, `currency`, and `amount` when
you create the Elements instance. For use with a PaymentIntent, set the `mode`
to `'payment'` and the `currency` and `amount` to what you’ll charge your
customer.

JavascriptReactBeforeAfter
```
const stripe =
 Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
```

```
const stripe =
 Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const options = {
 mode: 'payment',
 currency: 'usd',
 amount: 1099,
};
const elements = stripe.elements(options);
```

[OptionalSave payment details during a
payment](https://docs.stripe.com/payments/payment-element/migration#one-time-save-payment-details)[OptionalAdditional
Elements
optionsClient-side](https://docs.stripe.com/payments/payment-element/migration#additional-options)[Add
the Payment
ElementClient-side](https://docs.stripe.com/payments/payment-element/migration#one-time-add-payment-element)
You can now replace the Card Element and individual payment methods Elements
with the Payment Element. The Payment Element automatically adjusts to collect
input fields based on the payment method and country (for example, full billing
address collection for SEPA Direct Debit) so you don’t have to maintain
customized input fields anymore.

The following example replaces `CardElement` with `PaymentElement`:

```
<form id="payment-form">
 <div id="card-element">
 </div>
 <div id="payment-element">
 <!-- Mount the Payment Element here -->
 </div>
 <button id="submit">Submit</button>
</form>
```

```
const cardElement = elements.create("card");
cardElement.mount("#card-element");
const paymentElement = elements.create("payment");
paymentElement.mount("#payment-element");
```

If your payment flow already always collects details like the customer’s name or
email address, you can prevent the Payment Element from collecting this
information by passing the
[fields](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-fields)
option when creating the Payment Element. If you disable the collection of a
certain field, you must pass that same data back with
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment).

[Update your PaymentIntent creation
callServer-side](https://docs.stripe.com/payments/payment-element/migration#one-time-payment-intent)
The Payment Element allows you to accept multiple payment methods. You can
manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow. We prioritize payment methods
that increase conversion and are most relevant to the customer’s currency and
location.

Any of the additional elements options passed when creating the Elements group
in the earlier step should also be passed when creating the PaymentIntent.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia" \
 -d "amount"=1099 \
 -d "currency"="usd" \
 -d "payment_method_types[]"=card \
 -d "automatic_payment_methods[enabled]"=true \
```

#### Caution

Each payment method needs to support the currency passed in the PaymentIntent
and your business needs to be based in one of the countries each payment method
supports. See the [Payment method integration
options](https://docs.stripe.com/payments/payment-methods/integration-options)
page for more details about what’s supported.

[Update the submit
handlerClient-side](https://docs.stripe.com/payments/payment-element/migration#one-time-update-method)
Instead of using individual confirm methods like `stripe.confirmCardPayment` or
`stripe.confirmP24Payment`, use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to collect payment information and submit it to Stripe.

To confirm the PaymentIntent, make the following updates to your submit handler:

- Call `await elements.submit()` to trigger form validation and collect any data
required for
[wallets](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-wallets).
- Optional: Move PaymentIntent creation to the submit handler. This way you only
create the PaymentIntent when you’re sure of the final amount.
- Pass the `elements` instance you used to create the Payment Element and the
`clientSecret` from the PaymentIntent as parameters to `stripe.confirmPayment`.

When called, `stripe.confirmPayment` attempts to complete any [required
actions](https://docs.stripe.com/payments/paymentintents/lifecycle), such as
authenticating your customers by displaying a 3DS dialog or redirecting them to
a bank authorization page. When confirmation is complete, users are directed to
the `return_url` you configured, which normally corresponds to a page on your
website that [provides the status of the
payment](https://docs.stripe.com/payments/accept-a-payment#web-post-payment).

If you want to keep the same checkout flow for card payments and only redirect
for redirect-based payment methods, you can set
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
to `if_required`.

The following code example replaces `stripe.confirmCardPayment` with
`stripe.confirmPayment`:

BeforeAfter
```
// Create the PaymentIntent and obtain clientSecret
const res = await fetch("/create-intent", {
 method: "POST",
 headers: {"Content-Type": "application/json"},
});

const {client_secret: clientSecret} = await res.json();

const handleSubmit = async (event) => {
 event.preventDefault();

 if (!stripe) {
 // Stripe.js hasn't yet loaded.
 // Make sure to disable form submission until Stripe.js has loaded.
 return;
 }

 setLoading(true);

 const {error} = await stripe.confirmCardPayment(clientSecret, {
 payment_method: {
 card: elements.getElement(CardElement)
 }
 });

 if (error) {
 handleError(error);
 }
};
```

```
const handleSubmit = async (event) => {
 event.preventDefault();

 if (!stripe) {
 // Stripe.js hasn't yet loaded.
 // Make sure to disable form submission until Stripe.js has loaded.
 return;
 }

 setLoading(true);

 // Trigger form validation and wallet collection
 const {error: submitError} = await elements.submit();
 if (submitError) {
 handleError(submitError);
 return;
 }

 // Create the PaymentIntent and obtain clientSecret
 const res = await fetch("/create-intent", {
 method: "POST",
 headers: {"Content-Type": "application/json"},
 });

 const {client_secret: clientSecret} = await res.json();

 // Use the clientSecret and Elements instance to confirm the setup
 const {error} = await stripe.confirmPayment({
 elements,
 clientSecret,
 confirmParams: {
 return_url: 'https://example.com/order/123/complete',
 },
 // Uncomment below if you only want redirect for redirect-based payments
 // redirect: "if_required",
 });

 if (error) {
 handleError(error);
 }
};
```

[Handle post-payment
eventsServer-side](https://docs.stripe.com/payments/payment-element/migration#post-payment)
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
attempt to pay.[Test the
integration](https://docs.stripe.com/payments/payment-element/migration#test-the-integration)CardsWalletsBank
redirectsBank debitsVouchersCard numberScenarioHow to test4242424242424242The
card payment succeeds and doesn’t require authentication.Fill out the credit
card form using the credit card number with any expiration, CVC, and postal
code.4000002500003155The card payment requires
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number with any expiration, CVC,
and postal code.4000000000009995The card is declined with a decline code like
`insufficient_funds`.Fill out the credit card form using the credit card number
with any expiration, CVC, and postal code.6205500000000000004The UnionPay card
has a variable length of 13-19 digits.Fill out the credit card form using the
credit card number with any expiration, CVC, and postal code.
See [Testing](https://docs.stripe.com/testing) for additional information to
test your integration.

## Links

- [Migrating to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration#web)
- [Build a checkout page](https://docs.stripe.com/checkout/custom/quickstart)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing page](https://stripe.com/pricing/local-payment-methods)
- [React Stripe.js](https://github.com/stripe/react-stripe-js)
-
[fields](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-fields)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
- [Payment method integration
options](https://docs.stripe.com/payments/payment-methods/integration-options)
-
[wallets](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-wallets)
- [required actions](https://docs.stripe.com/payments/paymentintents/lifecycle)
- [provides the status of the
payment](https://docs.stripe.com/payments/accept-a-payment#web-post-payment)
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
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Testing](https://docs.stripe.com/testing)