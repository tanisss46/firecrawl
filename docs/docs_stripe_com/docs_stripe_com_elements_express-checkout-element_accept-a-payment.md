# Accept a payment with the Express Checkout Element

## Use a single integration to accept payments through one-click payment buttons.

The [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element) gives you a
single integration for accepting payments through one-click payment buttons,
including [Link](https://docs.stripe.com/payments/link),
[PayPal](https://docs.stripe.com/payments/paypal), [Apple
Pay](https://docs.stripe.com/apple-pay), [Google
Pay](https://docs.stripe.com/google-pay), and [Amazon
Pay](https://docs.stripe.com/payments/amazon-pay).

[Customers](https://docs.stripe.com/api/customers) see different payment buttons
depending on what their device and browser combination supports. Compatible
devices automatically support Google Pay and Link. Supporting Apple Pay and
PayPal requires additional steps.

#### Klarna on the Express Checkout Element

Klarna on the Express Checkout Element is currently in private preview with
limited availability. Reach out here to request access.

Merchant CountryUnited StatesBackground ColorLightSizeDesktopMax ColumnsMax
ColumnsMax RowsMax RowsOverflowCollect Shipping AddressThe Express Checkout
Element displays multiple buttons at the same time in the order that maximizes
payment conversion on your page. The demo sets the
[wallets](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets)
parameter to 'always' for all wallets. Google Pay and Apple Pay are displayed
only on their available platforms. Amazon Pay and Paypal are only displayed if
they are available in the selected business country.OptionDescriptionMerchant
countrySet this using the [publishable
key](https://docs.stripe.com/keys#obtain-api-keys) that you use to [initialize
Stripe.js](https://docs.stripe.com/js/initializing). To change the country, you
must unmount the Express Checkout Element, update the publishable key, then
re-mount the Express Checkout Element.Background colorSet colors using the
[Elements Appearance API](https://docs.stripe.com/elements/appearance-api).
Button themes are inherited from the Appearance API but you can also [define
them directly when you create the
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme).Desktop
and mobile sizeUse the dropdown to set the max pixel width of the parent element
that the Express Checkout Element is mounted to. You can set it to 750px
(Desktop) or 320px (Mobile).Max columns and max rowsSet these values using the
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
parameter when you [Create the Express Checkout
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element).Overflow
menuSet this using the
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
parameter when you [Create the Express Checkout
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element).Collect
shipping addressTo collect shipping information, you must pass options when
[creating](https://docs.stripe.com/js/elements_object/create_express_checkout_element)
the Express Checkout Element. Learn more about [collecting customer details and
displaying line
items](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#handle-create-event).
We recommend that you collect payment details before creating an Intent when
using the Express Checkout Element. If you previously integrated with the
[Payment Element](https://docs.stripe.com/payments/payment-element), you might
need to [update your
integration](https://docs.stripe.com/payments/accept-a-payment-deferred) to this
preferred approach.

## Before you begin

- Add a payment method to your browser. For example, you can add a card to your
Google Pay account or to your Wallet for Safari.
- Serve your application over HTTPS. This is required in development and in
production. You can use a service such as [ngrok](https://ngrok.com/).
- [Register your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration) in
both test mode and live mode.
- [Create a PayPal Sandbox
account](https://developer.paypal.com/tools/sandbox/accounts/) to test your
integration.
[Set up
StripeServer-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#set-up-stripe)
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
methods](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#enable-payment-methods)
By default, Stripe uses your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) to determine
which payment methods are enabled in the Express Checkout Element.

To manually override which payment methods are enabled, list any that you want
to enable using the `payment_method_types` attribute.

- If you collect payments before creating an intent, then list payment methods
in the [paymentMethodTypes attribute on your Elements provider
options](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodTypes).
- If you create an intent before rendering Elements, then list payment methods
in the [payment_method_types attribute on your
Intent](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types).

### Supported payment methods

Apple Pay and Google Pay are automatically enabled when using `card` payment
method type. When using Link, you must also pass the `card` payment method type.

Payment method namePayment method API parametersApple Pay`card`Google
Pay`card`Link`link, card`PayPal`paypal`Amazon Pay`amazon_pay`[Set up Stripe
ElementsClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#set-up-elements)HTML
+ JSReact
The Express Checkout Element is automatically available as a feature of
Stripe.js. Include the Stripe.js script on your checkout page by adding it to
the head of your HTML file. Always load Stripe.js directly from js.stripe.com to
remain PCI compliant. Don’t include the script in a bundle or host a copy of it
yourself.

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

Then, create an instance of Elements with the
[mode](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-mode)
(payment, setup, or subscription),
[amount](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-amount),
and
[currency](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-currency).
These values determine which payment methods to show to your customer. See the
next step for more configurable Elements options.

```
const options = {
 mode: 'payment',
 amount: 1099,
 currency: 'usd',
 // Customizable by using the Appearance API.
 appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form.
const elements = stripe.elements(options);
```

[OptionalAdditional Elements
optionsClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#additional-options)[Create
and mount the Express Checkout
ElementClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#create-and-mount)
The Express Checkout Element contains an iframe that securely sends the payment
information to Stripe over an HTTPS connection. The checkout page address must
also start with `https://`, rather than `http://`, for your integration to work.

HTML + JSReact
The Express Checkout Element needs a place to live on your payment page. Create
an empty DOM node (container) with a unique ID in your payment form.

```
<div id="express-checkout-element">
 <!-- Express Checkout Element will be inserted here -->
</div>
<div id="error-message">
 <!-- Display an error message to your customers here -->
</div>
```

When the form has loaded, create an instance of the Express Checkout Element and
mount it to the container DOM node:

```
// Create and mount the Express Checkout Element
const expressCheckoutElement = elements.create('expressCheckout');
expressCheckoutElement.mount('#express-checkout-element');
```

[Collect customer details and display line
itemsClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#handle-create-event)
Pass options when
[creating](https://docs.stripe.com/js/elements_object/create_express_checkout_element)
the Express Checkout Element.

HTML + JSReact
### Collect payer information

Set `emailRequired: true` to collect emails, and `phoneNumberRequired: true` to
collect phone numbers. `billingAddressRequired` is `true` by default.

```
elements.create('expressCheckout', {
 emailRequired: true,
 phoneNumberRequired: true
});
```

When using PayPal with the Express Checkout Element, Stripe typically only
receives and exposes the country from the billing address. Because of how PayPal
shares information with third-party payment processors, the confirm event
payload might show `billingDetails[address]` fields as empty strings, except for
the country field.

### Collect shipping information

Set `shippingAddressRequired: true` and pass an array of
[shippingRates](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-shippingRates).

```
elements.create('expressCheckout', {
 shippingAddressRequired: true,
 allowedShippingCountries: ['US'],
 shippingRates: [
 {
 id: 'free-shipping',
 displayName: 'Free shipping',
 amount: 0,
 deliveryEstimate: {
 maximum: {unit: 'day', value: 7},
 minimum: {unit: 'day', value: 5}
 }
 },
 ]
});
```

Listen to the [shippingaddresschange
event](https://docs.stripe.com/js/elements_object/express_checkout_element_shippingaddresschange_event)
to detect when a customer selects a shipping address. You must call either
`resolve` or `reject` if you choose to handle this event.

```
expressCheckoutElement.on('shippingaddresschange', async (event) => {
 const response = await fetch('/calculate-shipping', {
 data: JSON.stringify({
 shippingAddress: event.address
 })
 });
 const result = await response.json();
 event.resolve({
 lineItems: result.updatedLineItems,
 });
});
```

Listen to the [shippingratechange
event](https://docs.stripe.com/js/elements_object/express_checkout_element_shippingratechange_event)
to detect when a customer selects a shipping rate. You must call either
`resolve` or `reject` if you choose to handle this event.

```
expressCheckoutElement.on('shippingratechange', async (event) => {
 const response = await fetch('/calculate-and-update-amount', {
 data: JSON.stringify({
 shippingRate: event.shippingRate
 })
 });
 const result = await response.json();
 elements.update({amount: result.amount})
 event.resolve({
 lineItems: result.updatedLineItems,
 });
});
```

Listen to the [cancel
event](https://docs.stripe.com/js/elements_object/express_checkout_element_cancel_event)
to detect when a customer dismisses the payment interface. Reset the amount to
the initial amount.

```
expressCheckoutElement.on('cancel', () => {
 elements.update({amount: 1099})
});
```

### Display line items

Pass in an array of
[lineItems](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-lineItems):

```
elements.create('expressCheckout', {
 lineItems: [
 {
 name: 'Sample item',
 amount: 1000
 },
 {
 name: 'Tax',
 amount: 100
 },
 {
 name: 'Shipping cost',
 amount: 1000
 }
 ]
});
```

### Configure the Apple Pay interface

Learn how to configure the Apple Pay interface.

### Merchant initiated transactions (MIT)

You can set up recurring payments, deferred payments, or automatic reload
payments when a user checks out with Apple Pay by requesting the relevant
[merchant token
type](https://docs.stripe.com/apple-pay/merchant-tokens?pay-element=ece&mpan=auto-reload#merchant-token-types)
in the Express Checkout Element `click` event. We recommend implementing Apple
Pay merchant tokens to align with Apple Pay’s latest guidelines and to future
proof your integration.

[OptionalListen to the ready
eventClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#ready-event)[OptionalControl
when to show payment
buttonsClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#payment-button-control)[OptionalStyle
the
buttonClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#style-button)[OptionalCreate
a
ConfirmationTokenClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#create-ct)[Create
a
PaymentIntentServer-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#create-pi)
Stripe uses a [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
object to represent your intent to collect payment from a customer, tracking
charge attempts and payment state changes throughout the process.

Create a PaymentIntent on your server with an amount and currency. This must
match what you set on the `stripe.elements` instance in [step
3](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#set-up-elements).
Always decide how much to charge on the server-side, a trusted environment, as
opposed to the client-side. This prevents malicious customers from choosing
their own prices.

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

The returned PaymentIntent includes a [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret),
which the client-side uses to securely complete the payment process instead of
passing the entire PaymentIntent object. You can use different approaches to
pass the client secret to the client-side.

[Submit the payment to
StripeClient-side](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#submit-the-payment)
Use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to complete the payment using details from the Express Checkout Element.

#### Note

For Amazon Pay and PayPal, the amount you confirm in the PaymentIntent must
match the amount the buyer pre-authorized. If the amounts don’t match, the
payment is declined.

Provide a
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
to this function to indicate where Stripe should redirect the user after they
complete the payment. Your user might be initially redirected to an intermediate
site before being redirected to the `return_url`. Payments immediately redirect
to the `return_url` when a payment is successful.

If you don’t want to redirect after payment completion, set
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
to `if_required`. This only redirects customers that check out with
redirect-based payment methods.

HTML + JSReact
```
const handleError = (error) => {
 const messageContainer = document.querySelector('#error-message');
 messageContainer.textContent = error.message;
}

expressCheckoutElement.on('confirm', async (event) => {
 const {error: submitError} = await elements.submit();
 if (submitError) {
 handleError(submitError);
 return;
 }

 // Create the PaymentIntent and obtain clientSecret
 const res = await fetch('/create-intent', {
 method: 'POST',
 });
 const {client_secret: clientSecret} = await res.json();

 const {error} = await stripe.confirmPayment({
 // `elements` instance used to create the Express Checkout Element
 elements,
 // `clientSecret` from the created PaymentIntent
 clientSecret,
 confirmParams: {
 return_url: 'https://example.com/order/123/complete',
 },
 });

 if (error) {
 // This point is only reached if there's an immediate error when
// confirming the payment. Show the error to your customer (for example, payment
details incomplete)
 handleError(error);
 } else {
 // The payment UI automatically closes with a success animation.
 // Your customer is redirected to your `return_url`.
 }
});
```

[Test the
integration](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#test-integration)
Before you go live, [test](https://docs.stripe.com/testing) each payment method
integration. To determine a payment method’s browser compatibility, see
[supported
browsers](https://docs.stripe.com/elements/express-checkout-element#supported-browsers).
If you use the Express Checkout Element within an iframe, the iframe must have
the
[allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest)
attribute set to `payment *`.

LinkWalletsAmazon Pay
#### Caution

Don’t store real user data in [sandbox](https://docs.stripe.com/sandboxes) Link
accounts. Treat them as if they’re publicly available, because these test
accounts are associated with your publishable key.

Currently, Link only works with credit cards, debit cards, and qualified US bank
account purchases. Link requires [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration).

You can create sandbox accounts for Link using any valid email address. The
following table shows the fixed one-time passcode values that Stripe accepts for
authenticating sandbox accounts:

ValueOutcomeAny other 6 digits not listed belowSuccess000001Error, code
invalid000002Error, code expired000003Error, max attempts exceeded[OptionalUse
the Express Checkout Element with Stripe
Connect](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#connect)
## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## See also

- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)

## Links

- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Link](https://docs.stripe.com/payments/link)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
- [Customers](https://docs.stripe.com/api/customers)
-
[wallets](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets)
- [publishable key](https://docs.stripe.com/keys#obtain-api-keys)
- [initialize Stripe.js](https://docs.stripe.com/js/initializing)
- [Elements Appearance API](https://docs.stripe.com/elements/appearance-api)
- [define them directly when you create the
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme)
-
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
- [Create the Express Checkout
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element)
- [collecting customer details and displaying line
items](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#handle-create-event)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [update your
integration](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [ngrok](https://ngrok.com/)
- [Register your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [Create a PayPal Sandbox
account](https://developer.paypal.com/tools/sandbox/accounts/)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [paymentMethodTypes attribute on your Elements provider
options](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodTypes)
- [payment_method_types attribute on your
Intent](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[mode](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-mode)
-
[amount](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-amount)
-
[currency](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-currency)
-
[shippingRates](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-shippingRates)
- [shippingaddresschange
event](https://docs.stripe.com/js/elements_object/express_checkout_element_shippingaddresschange_event)
- [shippingratechange
event](https://docs.stripe.com/js/elements_object/express_checkout_element_shippingratechange_event)
- [cancel
event](https://docs.stripe.com/js/elements_object/express_checkout_element_cancel_event)
-
[lineItems](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-lineItems)
- [merchant token
type](https://docs.stripe.com/apple-pay/merchant-tokens?pay-element=ece&mpan=auto-reload#merchant-token-types)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
-
[redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
- [test](https://docs.stripe.com/testing)
- [supported
browsers](https://docs.stripe.com/elements/express-checkout-element#supported-browsers)
-
[allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest)
- [sandbox](https://docs.stripe.com/sandboxes)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)