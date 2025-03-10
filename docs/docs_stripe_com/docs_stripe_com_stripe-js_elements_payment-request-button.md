# Payment Request ButtonDeprecated

## Collect payment and address information from customers who use Apple Pay, Google Pay, or Link.

#### Legacy feature

The content on this page refers to a Legacy
[Element](https://docs.stripe.com/payments/elements). Use the [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element) instead. If
you have an existing Payment Request Button integration, use our [migration
guide](https://docs.stripe.com/elements/express-checkout-element/migration) to
switch to Express Checkout Element.

The Payment Request Button has the following limitations:

- Only supports card payment methods
- [Link](https://docs.stripe.com/payments/link) is supported, but only when card
[funding
sources](https://docs.stripe.com/payments/link/add-link-elements-integration#multiple-funding-sources)
are used
- Only shows one payment option

## Demo

#### Caution

Either your browser does not support the Payment Request API, or you do not have
a saved payment method. To try out the Payment Request Button live demo, switch
to one of the [supported
browsers](https://docs.stripe.com/stripe-js/elements/payment-request-button#html-js-testing)
below, and make sure you have a saved payment method.HTML + JSReact
The Payment Request Button Element dynamically displays wallet options during
checkout, giving you a single integration for [Apple
Pay](https://docs.stripe.com/apple-pay), [Google
Pay](https://docs.stripe.com/google-pay), and
[Link](https://docs.stripe.com/stripe-js/elements/payment-request-button#link-prb).
Alternatively, you can use the [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element) to offer
multiple one-click payment buttons to your customers.
[Compare](https://docs.stripe.com/elements/express-checkout-element/comparison)
the Express Checkout Element and Payment Request Button.

Customers see Apple Pay or Google Pay if they enabled them on their device, and
depending on the browser they use. If Link appears, it could be because
customers:

- Don’t have Apple Pay or Google Pay enabled on their device.
- Use Chrome with active, authenticated Link sessions.
Browser + WalletPayment ButtonSafari + Apple Pay enabledApple PayChrome + Link
authenticatedLinkChrome + Google Pay enabled and Link not authenticatedGoogle
PayChrome on iOS 16 + Apple Pay and Google Pay enabledApple PayAny browser + No
active Apple Pay or Google PayLink
## Prerequisites

Before you start, you need to:

- Review the requirements for each payment button type:

- Apple Pay and Google Pay don’t display for IP addresses in India, so plan your
integration testing accordingly.
- Apple Pay requires macOS 10.12.1+ or iOS 10.1+.
- Compatible devices automatically support Google Pay.
- **Register your domain** in both test mode and live mode.
- **Add a payment method to your browser.** For example, you can save a card in
Chrome, add a card to your Google Pay account, or add a card to your Wallet for
Safari.
- **Serve your application over HTTPS.** This is a requirement both in
development and production. One way to get started is to use a service such as
[ngrok](https://ngrok.com/).
[Set up Stripe
ElementsClient-side](https://docs.stripe.com/stripe-js/elements/payment-request-button#set-up-stripe-elements)
Elements is available as part of
[Stripe.js](https://docs.stripe.com/payments/elements). Include this in your
page and create a container to use for the `paymentRequestButton` Element:

```
<script src="https://js.stripe.com/v3/"></script>
<div id="payment-request-button">
 <!-- A Stripe Element will be inserted here. -->
</div>
```

Your Stripe publishable [API key](https://docs.stripe.com/keys) is also required
as it identifies your website to Stripe:

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx', {
 apiVersion: "2025-02-24.acacia",
});
```

[Create a paymentRequest
instanceClient-side](https://docs.stripe.com/stripe-js/elements/payment-request-button#create-payment-request-instance)
Create an instance of
[stripe.paymentRequest](https://docs.stripe.com/js#stripe-payment-request) with
all required options.

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
```

#### Note

Use the `requestPayerName` parameter to collect the payer’s billing address for
Apple Pay and Link. You can use the billing address to perform address
verification and block fraudulent payments. All other payment methods
automatically collect the billing address when one is available.

[Create and mount the
paymentRequestButtonClient-side](https://docs.stripe.com/stripe-js/elements/payment-request-button#mount-element)
Create the `paymentRequestButton` Element and check to make sure that your
customer has an active payment method using `canMakePayment()`. If they do,
mount the Element to the container to display the **Payment Request** button. If
they don’t, you can’t mount the Element, and we recommend that you show a
traditional checkout form instead.

#### Note

If you accept Apple Pay with the Payment Request Button, you must offer Apple
Pay as the primary payment option on your website per [Apple
guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/#:~:text=canMakePaymentWithActiveCard).
Internally, the Payment Request Button uses the Apple Pay
`canMakePaymentWithActiveCard` API.

```
const elements = stripe.elements();
const prButton = elements.create('paymentRequestButton', {
 paymentRequest,
});

(async () => {
 // Check the availability of the Payment Request API first.
 const result = await paymentRequest.canMakePayment();
 if (result) {
 prButton.mount('#payment-request-button');
 } else {
 document.getElementById('payment-request-button').style.display = 'none';
 }
})();
```

[Create a
PaymentIntentServer-side](https://docs.stripe.com/stripe-js/elements/payment-request-button#create-payment)
Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents)
object to represent your intent to collect payment from a customer, tracking
charge attempts and payment state changes throughout the process.

!

Create a `PaymentIntent` on your server with an amount and currency. Always
decide how much to charge on the server side, a trusted environment, as opposed
to the client. This prevents malicious customers from being able to choose their
own prices.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card
```

Included in the returned PaymentIntent is a [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret),
which you use to securely complete the payment process instead of passing the
entire PaymentIntent object. Send the client secret back to the client to use in
the next step.

[Complete the
paymentClient-side](https://docs.stripe.com/stripe-js/elements/payment-request-button#complete-payment)
Listen to the `paymentmethod` event to receive a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) object. Pass the
PaymentMethod ID and the PaymentIntent’s client secret to
[stripe.confirmCardPayment](https://docs.stripe.com/js#stripe-confirm-card-payment)
to complete the payment.

```
paymentRequest.on('paymentmethod', async (ev) => {
 // Confirm the PaymentIntent without handling potential next actions (yet).
 const {paymentIntent, error: confirmError} = await stripe.confirmCardPayment(
 clientSecret,
 {payment_method: ev.paymentMethod.id},
 {handleActions: false}
 );

 if (confirmError) {
 // Report to the browser that the payment failed, prompting it to
 // re-show the payment interface, or show an error message and close
 // the payment interface.
 ev.complete('fail');
 } else {
 // Report to the browser that the confirmation was successful, prompting
 // it to close the browser payment method collection interface.
 ev.complete('success');
 // Check if the PaymentIntent requires any actions and, if so, let Stripe.js
 // handle the flow. If using an API version older than "2019-02-11"
 // instead check for: `paymentIntent.status === "requires_source_action"`.
 if (paymentIntent.status === "requires_action") {
 // Let Stripe.js handle the rest of the payment flow.
 const {error} = await stripe.confirmCardPayment(clientSecret);
 if (error) {
 // The payment failed -- ask your customer for a new payment method.
 } else {
 // The payment has succeeded -- show a success message to your customer.
 }
 } else {
 // The payment has succeeded -- show a success message to your customer.
 }
 }
});
```

#### Caution

The customer can dismiss the payment interface in some browsers even after they
authorize the payment. This means that you might receive a [cancel
event](https://docs.stripe.com/js#payment-request-on) on your PaymentRequest
object after receiving a `paymentmethod` event. If you use the `cancel` event as
a hook for canceling the customer’s order, make sure you also refund the payment
that you just created.

[Test your
integration](https://docs.stripe.com/stripe-js/elements/payment-request-button#testing)
To test your integration, you must use HTTPS and a supported browser. If you use
the `paymentRequestButton` Element within an iframe, the iframe must have the
[allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest)
attribute set to equal “payment *”.

#### Regional TestingIndia

Stripe Elements doesn’t support Google Pay or Apple Pay for Stripe accounts and
customers in India. Therefore, you can’t test your Google Pay or Apple Pay
integration if the tester’s IP address is in India, even if the Stripe account
is based outside India.

In addition, each payment method and browser has specific requirements:

Apple PayGoogle PayLink
#### Safari

- Safari on Mac running macOS Sierra or later
- A compatible device with a card in its Wallet paired to your Mac with Handoff,
or a Mac with TouchID. You can find instructions on the [Apple Support
site](https://support.apple.com/en-us/HT204681).
- A [registered domain with Apple
Pay](https://docs.stripe.com/payments/payment-methods/pmd-registration).
- When using an iframe, its origin must match the top-level origin (except for
Safari 17+ when specifying `allow="payment"` attribute). Two pages have the same
origin if the protocol, host (full domain name), and port (if specified) are the
same for both pages.

#### Mobile Safari

- Mobile Safari on iOS 10.1 or later
- A card in your Wallet (go to **Settings** > **Wallet & Apple Pay**).
- A [registered domain with Apple
Pay](https://docs.stripe.com/payments/payment-methods/pmd-registration).
- When using an iframe, its origin must match the top-level origin (except for
Safari 17+ when specifying `allow="payment"` attribute). Two pages have the same
origin if the protocol, host (full domain name), and port (if specified) are the
same for both pages.

As of iOS 16, Apple Pay might work in some non-Safari mobile browsers with a
card saved in your Wallet.

## Collect shipping information

To collect shipping information, begin by including `requestShipping: true` when
creating the payment request.

You can also provide an array of `shippingOptions` at this point, if your
shipping options don’t depend on the customer’s address.

```
const paymentRequest = stripe.paymentRequest({
 country: 'US',
 currency: 'usd',
 total: {
 label: 'Demo total',
 amount: 1099,
 },

 requestShipping: true,
 // `shippingOptions` is optional at this point:
 shippingOptions: [
 // The first shipping option in this list appears as the default
 // option in the browser payment interface.
 {
 id: 'free-shipping',
 label: 'Free shipping',
 detail: 'Arrives in 5 to 7 days',
 amount: 0,
 },
 ],
});
```

Next, listen to the `shippingaddresschange` event to detect when a customer
selects a shipping address. Use the address to fetch valid shipping options from
your server, update the total, or perform other business logic. You can
anonymize the address data on the `shippingaddresschange` event in the browser
to not reveal sensitive information that isn’t necessary for shipping cost
calculation.

The customer must provide valid `shippingOptions` at this point to proceed in
the flow.

```
paymentRequest.on('shippingaddresschange', async (ev) => {
 if (ev.shippingAddress.country !== 'US') {
 ev.updateWith({status: 'invalid_shipping_address'});
 } else {
 // Perform server-side request to fetch shipping options
 const response = await fetch('/calculateShipping', {
 data: JSON.stringify({
 shippingAddress: ev.shippingAddress
 })
 });
 const result = await response.json();

 ev.updateWith({
 status: 'success',
 shippingOptions: result.supportedShippingOptions,
 });
 }
});
```

## Display line items

Use
[displayItems](https://docs.stripe.com/js/payment_request/create#stripe_payment_request-options-displayItems)
to display
[PaymentItem](https://docs.stripe.com/js/appendix/payment_item_object) objects
and show the price breakdown in the browser’s payment interface.

```
const paymentRequest = stripe.paymentRequest({
 country: 'US',
 currency: 'usd',
 total: {
 label: 'Demo total',
 amount: 2000,
 },

 displayItems: [
 {
 label: 'Sample item',
 amount: 1000,
 },
 {
 label: 'Shipping cost',
 amount: 1000,
 }
 ],
});
```

## Style the button

Use the following parameters to customize the Element:

```
elements.create('paymentRequestButton', {
 paymentRequest,
 style: {
 paymentRequestButton: {
 type: 'default',
 // One of 'default', 'book', 'buy', or 'donate'
 // Defaults to 'default'

 theme: 'dark',
 // One of 'dark', 'light', or 'light-outline'
 // Defaults to 'dark'

 height: '64px',
 // Defaults to '40px'. The width is always '100%'.
 },
 },
});
```

### Using your own button

If you want to design your own button instead of using the
`paymentRequestButton` Element, you can show your custom button based on the
result of
[paymentRequest.canMakePayment()](https://docs.stripe.com/js#payment-request-can-make-payment).
Then, use
[paymentRequest.show()](https://docs.stripe.com/js#payment-request-show) to
display the browser interface when your button is clicked.

When building your own button, follow the Apple Pay [Human Interface
Guidelines](https://developer.apple.com/design/human-interface-guidelines) and
Google Pay [Brand
Guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines).

#### Caution

Link isn’t supported in custom button configurations and won’t display for the
customer if you decide to use one.

## Add an Apple Pay merchant token for merchant initiated transactions

Set up your Payment Request Button to request an [Apple Pay
MPAN](https://docs.stripe.com/apple-pay/merchant-tokens) to facilitate merchant
initiated transactions (MIT) for recurring, auto-load, or deferred payments.

- Create an instance of the [Payment
Request](https://docs.stripe.com/stripe-js/elements/payment-request-button#create-payment-request-instance).
- Pass the `applePay` object relevant to your MPAN use case (choose from the
drop-down to see use case code samples).
- Include relevant parameters for your use case.
MPAN use case:Recurring paymentsAutomatic reloadDeferred payment
```
const paymentRequest = stripe.paymentRequest({
 applePay: {
 recurringPaymentRequest: {
 paymentDescription: 'My subscription',
 managementURL: 'https://example.com/billing',
 regularBilling: {
 amount: 2500,
 label: 'Monthly subscription fee',
 recurringPaymentIntervalUnit: 'month',
 recurringPaymentIntervalCount: 1,
 },
 },
 },
 // Other options
});
```

## Use the Payment Request Button with Stripe Connect

[Connect](https://docs.stripe.com/connect) platforms that either create direct
charges or add the token to a Customer on the connected account must take
additional steps when using the Payment Request Button.

- On your frontend, before creating the `PaymentRequest` instance, set the
`stripeAccount` option on the Stripe instance:

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx', {
 apiVersion: "2025-02-24.acacia",
 stripeAccount: 'CONNECTED_STRIPE_ACCOUNT_ID',
});
```

- [Register all
domains](https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=api#register-your-domain-while-using-connect)
where you plan to show the Payment Request Button.

## Link for the Payment Request Button

When new customers come to your site, they can use [Link in the Payment Request
Button](https://docs.stripe.com/payments/link/payment-request-button-link) to
pay with their saved payment details. With
[Link](https://docs.stripe.com/payments/link), they don’t need to manually enter
their payment information. Link requires [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration).

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## See also

- [Learn about Apple Pay](https://docs.stripe.com/apple-pay)
- [Learn about Google Pay](https://docs.stripe.com/google-pay)

## Links

- [Element](https://docs.stripe.com/payments/elements)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [migration
guide](https://docs.stripe.com/elements/express-checkout-element/migration)
- [Link](https://docs.stripe.com/payments/link)
- [funding
sources](https://docs.stripe.com/payments/link/add-link-elements-integration#multiple-funding-sources)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
-
[Compare](https://docs.stripe.com/elements/express-checkout-element/comparison)
- [Register your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [ngrok](https://ngrok.com)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [API key](https://docs.stripe.com/keys)
- [stripe.paymentRequest](https://docs.stripe.com/js#stripe-payment-request)
- [Apple
guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/#:~:text=canMakePaymentWithActiveCard)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
-
[stripe.confirmCardPayment](https://docs.stripe.com/js#stripe-confirm-card-payment)
- [cancel event](https://docs.stripe.com/js#payment-request-on)
-
[allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest)
- [Apple Support site](https://support.apple.com/en-us/HT204681)
-
[displayItems](https://docs.stripe.com/js/payment_request/create#stripe_payment_request-options-displayItems)
- [PaymentItem](https://docs.stripe.com/js/appendix/payment_item_object)
-
[paymentRequest.canMakePayment()](https://docs.stripe.com/js#payment-request-can-make-payment)
- [paymentRequest.show()](https://docs.stripe.com/js#payment-request-show)
- [Human Interface
Guidelines](https://developer.apple.com/design/human-interface-guidelines)
- [Brand
Guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines)
- [Apple Pay MPAN](https://docs.stripe.com/apple-pay/merchant-tokens)
- [https://example.com/billing](https://example.com/billing)
- [Connect](https://docs.stripe.com/connect)
- [Register all
domains](https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=api#register-your-domain-while-using-connect)
- [Link in the Payment Request
Button](https://docs.stripe.com/payments/link/payment-request-button-link)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)