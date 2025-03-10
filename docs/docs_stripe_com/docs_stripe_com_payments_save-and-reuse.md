# Save a customer's payment method without making a payment

## Learn how to save a customer's payment method using a SetupIntent.

The [Setup Intents API](https://docs.stripe.com/api/setup_intents) lets you save
a customer’s payment details without an initial payment. This is helpful if you
want to onboard customers now, set them up for payments, and charge them in the
future—when they’re offline.

Use this integration to set up recurring payments or to create one-time payments
with a final amount determined later, often after the customer receives your
service.

#### Card-present transactions

Card-present transactions, such as collecting card details through Stripe
Terminal, use a different process for saving the payment method. For details,
see [the Terminal
documentation](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. These requirements
generally apply if you want to save your customer’s payment method for future
use, such as displaying a customer’s payment method to them in the checkout flow
for a future purchase or charging them when they’re not actively using your
website or app. Add terms to your website or app that state how you plan to save
payment method details and allow customers to opt in.

When you save a payment method, you can only use it for the specific usage you
have included in your terms. To charge a payment method when a customer is
offline and save it as an option for future purchases, make sure that you
explicitly collect consent from the customer for this specific use. For example,
include a “Save my payment method for future use” checkbox to collect consent.

To charge them when they’re offline, make sure your terms include the following:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges
are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

#### Note

If you need to use manual server-side confirmation or your integration requires
presenting payment methods separately, see our [alternative
guide](https://docs.stripe.com/payments/save-and-reuse-cards-only).

[Set up
StripeServer-side](https://docs.stripe.com/payments/save-and-reuse#set-up-stripe)
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
methods](https://docs.stripe.com/payments/save-and-reuse#enable-payment-methods)
View your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) and enable the
payment methods you want to support. You need at least one payment method
enabled to create a [SetupIntent](https://docs.stripe.com/api/setup_intents).

By default, Stripe enables cards and other prevalent payment methods that can
help you reach more customers, but we recommend turning on additional payment
methods that are relevant for your business and customers. See [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
for product and payment method support, and our [pricing
page](https://stripe.com/pricing/local-payment-methods) for fees.

[Create a
CustomerServer-side](https://docs.stripe.com/payments/save-and-reuse#create-customer)
To set up a payment method for future payments, you must attach it to a
[Customer](https://docs.stripe.com/api/customers). Create a `Customer` object
when your customer creates an account with your business. `Customer` objects
allow for reusing payment methods and tracking across multiple payments.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a
SetupIntentServer-side](https://docs.stripe.com/payments/save-and-reuse#create-intent)
#### Note

If you want to render the Payment Element without first creating a SetupIntent,
see [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?type=setup).

A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent to set up a customer’s payment method for future
payments. The payment methods shown to customers during the checkout process are
also included on the `SetupIntent`. You can let Stripe automatically pull
payment methods from your Dashboard settings or you can list them manually.

Unless your integration requires a code-based option for offering payment
methods, Stripe recommends the automated option. This is because Stripe
evaluates the currency, payment method restrictions, and other parameters to
determine the list of supported payment methods. Payment methods that increase
conversion and that are most relevant to the currency and customer’s location
are prioritized. Lower priority payment methods are hidden beneath an overflow
menu.

Manage payment methods from the DashboardManually list payment methods
Some payment methods can’t be saved for future payments, and customers don’t see
them as options when setting up future payments. For more details about managing
payment methods, see [Payment method integration
options](https://docs.stripe.com/payments/payment-methods/integration-options).

You can optionally create a SetupIntent with `automatic_payment_methods`
enabled, and the SetupIntent is created using the payment methods you configured
in the Dashboard. Specifying the `automatic_payment_methods` parameter is
optional because Stripe enables its functionality by default in the latest
version of the API.

You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow.

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "automatic_payment_methods[enabled]"=true
```

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

#### Using Radar

When saving a customer’s payment method without an initial payment,
[Radar](https://docs.stripe.com/radar) doesn’t act on the SetupIntent by
default. If you want to activate this as the default, go to the [Radar
settings](https://dashboard.stripe.com/settings/radar) and enable **Use Radar on
payment methods saved for future use**.

[Collect payment
detailsClient-side](https://docs.stripe.com/payments/save-and-reuse#collect-payment-details)
You’re ready to collect payment details on the client with the [Payment
Element](https://docs.stripe.com/payments/payment-element). The Payment Element
is a prebuilt UI component that simplifies collecting payment details for a
variety of payment methods.

The Payment Element contains an iframe that securely sends payment information
to Stripe over an HTTPS connection. The checkout page address must start with
`https://` rather than `http://` for your integration to work. You can test your
integration without doing so, but remember to [enable
HTTPS](https://docs.stripe.com/security/guide#tls) when you’re ready to accept
live payments.

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

### Add the Payment Element to your payment setup page

The Payment Element needs a place to live on your payment setup page. Create an
empty DOM node (container) with a unique ID in your payment form:

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
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
from the previous step into `options` when you create the
[Elements](https://docs.stripe.com/js/elements_object/create) instance:

```
const options = {
 clientSecret: '{{CLIENT_SECRET}}',
 // Fully customizable with appearance API.
 appearance: {/*...*/},
};

// Set up Stripe.js and Elements using the SetupIntent's client secret
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

The Payment Element renders a dynamic form that allows your customer to pick a
payment method. For each payment method, the form automatically asks the
customer to fill in all necessary payment details.

### Customize appearance

Customize the Payment Element to match the design of your site by passing the
[appearance
object](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-appearance)
into `options` when creating the `Elements` provider.

### Request Apple Pay merchant token

If you accept Apple Pay payments, we recommend configuring the Apple Pay
interface to return a [merchant
token](https://docs.stripe.com/apple-pay/merchant-tokens?pay-element=web-pe) to
enable merchant initiated transactions (MIT). [Request the relevant merchant
token
type](https://docs.stripe.com/apple-pay/merchant-tokens?pay-element=web-pe) in
the Payment Element. The following example shows a request for the deferred
payments merchant token.

```
const paymentElement = elements.create('payment', {
 applePay: {
 deferredPaymentRequest: {
 paymentDescription: 'My deferred payment',
 managementURL: 'https://example.com/billing',
 deferredBilling: {
 amount: 2500,
 label: 'Deferred Fee',
 deferredPaymentDate: new Date('2024-01-05')
 },
 }
 },
 // Other options
});
```

### Configure currency

When using SetupIntents with
[automatic_payment_methods](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-automatic_payment_methods),
you can specify the currency when you [create the Payment
Element](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-currency).
The Payment Element renders the enabled payment methods that support the
provided currency. For more details, see [the Payment Element
documentation](https://docs.stripe.com/payments/payment-methods/integration-options).

### Collect addresses

By default, the Payment Element only collects the necessary billing address
details. To collect a customer’s full billing address (to calculate the tax for
digital goods and services, for example) or shipping address, use the [Address
Element](https://docs.stripe.com/elements/address-element).

[OptionalLink in your checkout
pageClient-side](https://docs.stripe.com/payments/save-and-reuse#enable-checkout-link)[OptionalSave
and retrieve customer payment
methods](https://docs.stripe.com/payments/save-and-reuse#save-payment-methods)[Submit
the payment details to
StripeClient-side](https://docs.stripe.com/payments/save-and-reuse#submit-payment-details)
Use
[stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup) to
complete the setup using details collected by the Payment Element. Provide a
[return_url](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-return_url)
to this function so that Stripe can redirect the user after they complete setup.
We may first redirect them to an intermediate site, like a bank authorization
page, before redirecting them to the `return_url`.

If your customer saves their card details, we immediately redirect them to the
`return_url` when setup is successful. If you don’t want to redirect for card
payments, you can set
[redirect](https://docs.stripe.com/js/setup_intents/confirm_setup#confirm_setup_intent-options-redirect)
to `if_required`. This only redirects customers that check out with
redirect-based payment methods.

HTML + JSReact
```
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {error} = await stripe.confirmSetup({
 //`Elements` instance that was used to create the Payment Element
 elements,
 confirmParams: {
 return_url: 'https://example.com/account/payments/setup-complete',
 }
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

Make sure the `return_url` corresponds to a page on your website that [provides
the status](https://docs.stripe.com/payments/payment-intents/verifying-status)
of the `SetupIntent`. Stripe provides the following URL query parameters to
verify the status when we redirect the customer to the `return_url`. You can
also append your own query parameters when providing the `return_url`, and they
persist through the redirect process.

ParameterDescription`setup_intent`The unique identifier for the
`SetupIntent`.`setup_intent_client_secret`The [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
of the `SetupIntent` object.
You can use
[stripe.retrieveSetupIntent](https://docs.stripe.com/js/setup_intents/retrieve_setup_intent)
to retrieve the SetupIntent using the `setup_intent_client_secret` query
parameter. Successful confirmation of the SetupIntent saves the resulting
`PaymentMethod` ID (in `result.setupIntent.payment_method`) to the provided
`Customer`.

HTML + JSReact
```
// Initialize Stripe.js using your publishable key
const stripe = Stripe('{PUBLISHABLE_KEY}');

// Retrieve the "setup_intent_client_secret" query parameter appended to
// your return_url by Stripe.js
const clientSecret = new URLSearchParams(window.location.search).get(
 'setup_intent_client_secret'
);

// Retrieve the SetupIntent
stripe.retrieveSetupIntent(clientSecret).then(({setupIntent}) => {
 const message = document.querySelector('#message')

 // Inspect the SetupIntent `status` to indicate the status of the payment
 // to your customer.
 //
 // Some payment methods will [immediately succeed or fail][0] upon
 // confirmation, while others will first enter a `processing` state.
 //
 // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
 switch (setupIntent.status) {
 case 'succeeded': {
 message.innerText = 'Success! Your payment method has been saved.';
 break;
 }

 case 'processing': {
message.innerText = "Processing payment details. We'll update you when
processing is complete.";
 break;
 }

 case 'requires_payment_method': {
message.innerText = 'Failed to process payment details. Please try another
payment method.';

 // Redirect your user back to your payment page to attempt collecting
 // payment again

 break;
 }
 }
});
```

#### Caution

If you have tooling that tracks the customer’s browser session, you might need
to add the `stripe.com` domain to the referrer exclude list. Redirects cause
some tools to create new sessions which prevents you from tracking the complete
session.

[Charge the saved payment method
laterServer-side](https://docs.stripe.com/payments/save-and-reuse#charge-saved-payment-method)
#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. When rendering past
payment methods to your end customer for future purchases, make sure you’re
listing payment methods where you’ve collected consent from the customer to save
the payment method details for this specific future use. To differentiate
between payment methods attached to customers that can and can’t be presented to
your end customer as a saved payment method for future purchases, use the
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
parameter.

When you’re ready to charge your customer off-session, use the Customer and
PaymentMethod IDs to create a PaymentIntent. To find a payment method to charge,
list the payment methods associated with your customer. This example lists cards
but you can list any supported
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).

```
curl -G https://api.stripe.com/v1/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d type=card
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with
the amount and currency of the payment. Set a few other parameters to make the
off-session payment:

- Set
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
to `true` to indicate that the customer isn’t in your checkout flow during a
payment attempt and can’t fulfill an authentication request made by a partner,
such as a card issuer, bank, or other payment institution. If, during your
checkout flow, a partner requests authentication, Stripe requests exemptions
using customer information from a previous on-session transaction. If the
conditions for exemption aren’t met, the PaymentIntent might throw an error.
- Set the value of the PaymentIntent’s
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
property to `true`, which causes confirmation to occur immediately when the
PaymentIntent is created.
- Set
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
to the ID of the PaymentMethod and
[customer](https://docs.stripe.com/api#create_payment_intent-customer) to the ID
of the Customer.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1099 \
 -d currency=usd \
# In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 -d "automatic_payment_methods[enabled]"=true \
 -d customer="{{CUSTOMER_ID}}" \
 -d payment_method="{{PAYMENT_METHOD_ID}}" \
 -d return_url="https://example.com/order/123/complete" \
 -d off_session=true \
 -d confirm=true
```

When a payment attempt fails, the request also fails with a 402 HTTP status code
and the status of the PaymentIntent is
[requires_payment_method](https://docs.stripe.com/upgrades#2019-02-11). You must
notify your customer to return to your application to complete the payment (for
example, by sending an email or in-app notification).

Check the code of the [error](https://docs.stripe.com/api/errors/handling)
raised by the Stripe API library. If the payment failed due to an
[authentication_required](https://docs.stripe.com/declines/codes) decline code,
use the declined PaymentIntent’s client secret with confirmPayment to allow the
customer to authenticate the payment.

```
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {error} = await stripe.confirmPayment({
 // The client secret of the PaymentIntent
 clientSecret,
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

`stripe.confirmPayment` can take several seconds to complete. During that time,
disable your form from being resubmitted and show a waiting indicator like a
spinner. If you receive an error, show it to the customer, re-enable the form,
and hide the waiting indicator. If the customer must perform additional steps to
complete the payment, such as authentication, Stripe.js walks them through that
process.

If the payment failed for other reasons, such as insufficient funds, send your
customer to a payment page to enter a new payment method. You can reuse the
existing PaymentIntent to attempt the payment again with the new payment
details.

[Test the
integration](https://docs.stripe.com/payments/save-and-reuse#test-the-integration)
Use test payment details and the test redirect page to verify your integration.
Click the tabs below to view details for each payment method.

CardsBank redirectsBank debitsPayment methodScenarioHow to testCredit cardThe
card setup succeeds and doesn’t require
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number `4242 4242 4242 4242` with
any expiration, CVC, and postal code.Credit cardThe card requires authentication
for the initial setup, then succeeds for subsequent payments.Fill out the credit
card form using the credit card number `4000 0025 0000 3155` with any
expiration, CVC, and postal code.Credit cardThe card requires authentication for
the initial setup and also requires authentication for subsequent payments.Fill
out the credit card form using the credit card number `4000 0027 6000 3184` with
any expiration, CVC, and postal code.Credit cardThe card is declined during
setup.Fill out the credit card form using the credit card number `4000 0000 0000
9995` with any expiration, CVC, and postal code.
### Test charging a saved SEPA Debit PaymentMethod

Confirming the SetupIntent using iDEAL, Bancontact, or Sofort, generates a [SEPA
Direct Debit](https://docs.stripe.com/payments/sepa-debit)
[PaymentMethod](https://docs.stripe.com/api/payment_methods). SEPA Direct Debit
is a [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method that transitions to an intermediate `processing` state before
transitioning several days later to a `succeeded` or `requires_payment_method`
state.

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
immediately.[OptionalCustomize the
layoutClient-side](https://docs.stripe.com/payments/save-and-reuse#customize-layout)[OptionalApple
Pay and Google
PayClient-side](https://docs.stripe.com/payments/save-and-reuse#apple-pay-and-google-pay)
## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## See also

- [Accept a payment](https://docs.stripe.com/payments/accept-a-payment)
- [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment)
- [The Elements Appearance API](https://docs.stripe.com/elements/appearance-api)
- [Optimizing your Radar Integration](https://docs.stripe.com/radar/integration)

## Links

- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [the Terminal
documentation](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly)
- [alternative
guide](https://docs.stripe.com/payments/save-and-reuse-cards-only)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [pricing page](https://stripe.com/pricing/local-payment-methods)
- [Customer](https://docs.stripe.com/api/customers)
- [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?type=setup)
- [Payment method integration
options](https://docs.stripe.com/payments/payment-methods/integration-options)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [Radar](https://docs.stripe.com/radar)
- [Radar settings](https://dashboard.stripe.com/settings/radar)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [enable HTTPS](https://docs.stripe.com/security/guide#tls)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
- [Elements](https://docs.stripe.com/js/elements_object/create)
- [Elements docs](https://docs.stripe.com/payments/elements)
- [appearance
object](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-appearance)
- [merchant
token](https://docs.stripe.com/apple-pay/merchant-tokens?pay-element=web-pe)
- [https://example.com/billing](https://example.com/billing)
-
[automatic_payment_methods](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-automatic_payment_methods)
- [create the Payment
Element](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-currency)
- [Address Element](https://docs.stripe.com/elements/address-element)
- [stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup)
-
[return_url](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-return_url)
-
[redirect](https://docs.stripe.com/js/setup_intents/confirm_setup#confirm_setup_intent-options-redirect)
-
[https://example.com/account/payments/setup-complete](https://example.com/account/payments/setup-complete)
- [provides the
status](https://docs.stripe.com/payments/payment-intents/verifying-status)
-
[stripe.retrieveSetupIntent](https://docs.stripe.com/js/setup_intents/retrieve_setup_intent)
-
[https://stripe.com/docs/payments/payment-methods#payment-notification](https://stripe.com/docs/payments/payment-methods#payment-notification)
-
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
-
[type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
-
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
-
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
-
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
- [customer](https://docs.stripe.com/api#create_payment_intent-customer)
- [requires_payment_method](https://docs.stripe.com/upgrades#2019-02-11)
- [error](https://docs.stripe.com/api/errors/handling)
- [authentication_required](https://docs.stripe.com/declines/codes)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)
- [Accept a payment](https://docs.stripe.com/payments/accept-a-payment)
- [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment)
- [The Elements Appearance API](https://docs.stripe.com/elements/appearance-api)
- [Optimizing your Radar Integration](https://docs.stripe.com/radar/integration)