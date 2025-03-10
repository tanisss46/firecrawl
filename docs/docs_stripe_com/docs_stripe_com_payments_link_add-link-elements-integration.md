# Build a custom checkout page that includes Link

## Integrate Link using the Payment Element or Link Authentication Element.

This guide walks you through how to accept payments with
[Link](https://docs.stripe.com/payments/link) using the [Payment Intents
API](https://docs.stripe.com/api/payment_intents) and either the [Payment
Element](https://docs.stripe.com/payments/payment-element) or [Link
Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element).

There are three ways you can secure a customer email address for Link
authentication and enrollment:

- **Pass in an email address:** You can pass an email address to the Payment
Element using
[defaultValues](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-defaultValues).
If you’re already collecting the email address and or customer’s phone number in
the checkout flow, we recommend this approach.
- **Collect an email address:** You can collect an email address directly in the
Payment Element. If you’re not collecting the email address anywhere in the
checkout flow, we recommend this approach.
- **Link Authentication Element:** You can use the Link Authentication Element
to create a single email input field for both email collection and Link
authentication. We recommend doing this if you use the [Address
Element](https://docs.stripe.com/elements/address-element).

![Authenticate or enroll with Link directly in the Payment Element during
checkout](https://b.stripecdn.com/docs-statics-srv/assets/link-in-pe.2efb5138a4708b781b8a913ebddd9aba.png)

Collect a customer email address for Link authentication or enrollment

[Set up
StripeServer-side](https://docs.stripe.com/payments/link/add-link-elements-integration#set-up-stripe)
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

[Create a
PaymentIntentServer-side](https://docs.stripe.com/payments/link/add-link-elements-integration#web-create-intent)
Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents)
object to represent your intent to collect payment from a customer, tracking
charge attempts and payment state changes throughout the process.

![An overview diagram of the entire payment
flow](https://b.stripecdn.com/docs-statics-srv/assets/accept-a-payment-payment-element.5cf6795a02f864923f9953611493d735.svg)

If you collect card details for [future usage with Setup
Intents](https://docs.stripe.com/payments/save-and-reuse), list payment methods
manually instead of using dynamic payment methods. To use Link without dynamic
payment methods, update your integration to pass `link` to
`payment_method_types`.

When you create a PaymentIntent, [dynamically offer your customers the most
relevant payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods),
including Link, by using dynamic payment methods. To use dynamic payment
methods, don’t include the `payment_method_types` parameter. Optionally, you can
also enable `automatic_payment_methods`.

#### Note

When your integration doesn’t set the `payment_method_types` parameter, some
payment methods turn on automatically, including cards and wallets.

To add Link to your Elements integration using dynamic payment methods:

- In your Dashboard [payment method
settings](https://dashboard.stripe.com/settings/payment_methods), turn on Link.
- If you have an existing integration that manually lists payment methods,
remove the
[payment_method_types](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)
parameter from your integration.

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

[Collect customer
email](https://docs.stripe.com/payments/link/add-link-elements-integration#design-your-integration)
Link authenticates a customer by using their email address. Depending on your
checkout flow, you have the following options: pass an email to the Payment
Element, collect it directly within the Payment Element, or use the Link
Authentication Element. Of these, Stripe recommends passing a customer email
address to the Payment Element if available.

Pass in an emailCollect an emailUse the Link Authentication Element
If *any* of the following apply to you:

- You want a single, optimized component for email collection and Link
authentication.
- You need to collect a shipping address from your customer.

Then use the integration flow that implements these elements: the Link
Authentication Element, Payment Element and optional Address Element.

A Link-enabled checkout page has the Link Authentication Element at the
beginning, followed by the Address Element, and the Payment Element at the end.
You can also display the Link Authentication Element on separate pages, in this
same order, for multi-page checkout flows.

![Create a payment form using multiple
Elements](https://b.stripecdn.com/docs-statics-srv/assets/link-with-elements.f60af275f69b6e6e73c766d1f9928457.png)

Create a payment form using multiple Elements

The integration works as follows:

Customer

Stripe

Link

Merchant

Customer enters email into Link Authentication Element

Customer authenticates to Link

The Payment Element displays Link-stored payment information in your Stripe
payment page

Customer pays

Payment with payment_method_type=link

A diagram describing how to integrate Link using the Link Authentication
Element[Set up your payment
formClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#web-collect-payment-details)
Now you can set up your custom payment form with the Elements prebuilt UI
components. Your payment page address must start with `https://` rather than
`http://` for your integration to work. You can test your integration without
using HTTPS. [Enable HTTPS](https://docs.stripe.com/security/guide#tls) when
you’re ready to accept live payments.

Pass in an emailCollect an emailUse the Link Authentication Element
The Link Authentication Element renders an email address input. When Link
matches a customer email with an existing Link account, it sends the customer a
secure, one-time code to their phone to authenticate. If the customer
successfully authenticates, Stripe displays their Link-saved addresses and
payment methods automatically for them to use.

This integration also creates the Payment Element, which renders a dynamic form
that allows your customer to pick a payment method type. The form automatically
collects all necessary payments details for the payment method type selected by
the customer. The Payment Element also handles the display of Link-saved payment
methods for authenticated customers.

ReactHTML + JS
### Set up Stripe Elements

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from
the npm public registry.

```
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

On your payment page, wrap your payment form with the `Elements` component,
passing the [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
from [the previous
step](https://docs.stripe.com/payments/link/add-link-elements-integration#web-create-intent).
​​If you already collect the customer’s email in another part of your form,
replace your existing input with the `linkAuthenticationElement​`.

If you don’t collect email, add the `linkAuthenticationElement​` to your
checkout flow. You must place the `linkAuthenticationElement` before the
`ShippingAddressElement` (optional if you collect shipping addresses) and the
`PaymentElement` for Link to autofill Link-saved details for your customer in
the `ShippingAddressElement` and `PaymentElement`. You can also pass in the
[appearance option](https://docs.stripe.com/elements/appearance-api),
customizing the Elements to match the design of your site.

If you have the customer’s email, pass it to the `defaultValues` option of the
`linkAuthenticationElement`. This prefills their email address and initiates the
Link authentication process.

If you have other customer information, pass it to the
`defaultValues.billingDetails` object for the `PaymentElement`. Prefilling as
much information as possible simplifies Link account creation and reuse for your
customers.

Then, render the `linkAuthenticationElement` and `PaymentElement` components in
your payment form:

```
import {loadStripe} from "@stripe/stripe-js";
import {
 Elements,
 LinkAuthenticationElement,
 PaymentElement,
} from "@stripe/react-stripe-js";

const stripe = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

// Customize the appearance of Elements using the Appearance API.
const appearance = {/* ... */};

// Enable the skeleton loader UI for the optimal loading experience.
const loader = 'auto';

```

See all 49 lines
The `linkAuthenticationElement`, `PaymentElement`, and `ShippingAddressElement`
don’t need to be on the same page. If you have a process where customer contact
information, shipping details, and payment details display to the customer in
separate steps, you can display each Element in the appropriate step or page.
Include the `linkAuthenticationElement` as the email input form in the contact
info collection step to make sure the customer can take full advantage of the
shipping and payment autofill provided by Link.

If you collect your customer’s email with the Link Authentication Element early
in the checkout flow, you don’t need to show it again on the shipping or payment
pages.

### Retrieve an email address

You can retrieve the email address details using the `onChange` prop on the
`linkAuthenticationElement` component. The `onChange` handler fires whenever the
user updates the email field, or when a saved customer email is autofilled.

```
<linkAuthenticationElement onChange={(event) => {
 setEmail(event.value.email);
}} />
```

### Prefill a customer email address

The Link Authentication Element accepts an email address. Providing a customer’s
email address triggers the Link authentication flow as soon as the customer
lands on the payment page using the `defaultValues` option.

```
<linkAuthenticationElement options={{defaultValues: {email: 'foo@bar.com'}}}/>
```

[OptionalPrefill additional customer
dataClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#prefill-customer-data)[OptionalCollect
shipping
addressesClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#collect-shipping)[OptionalCustomize
the
appearanceClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#customize-appearance)[Submit
the payment to
StripeClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#web-submit-payment)
Use
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
to complete the payment with details collected from your customer in the
different Elements forms. Provide a
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
to this function to indicate where Stripe redirects the user after they complete
the payment.

Your user might be first redirected to an intermediate site, like a bank
authorization page, before Stripe redirects them to the `return_url`.

By default, card and bank payments immediately redirect to the `return_url` when
a payment is successful. If you don’t want to redirect to the `return_url`, you
can use
[if_required](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
to change the behavior.

ReactHTML + JS
```
import {loadStripe} from "@stripe/stripe-js";
import {
 useStripe,
 useElements,
 Elements,
 LinkAuthenticationElement,
 PaymentElement,
 // If collecting shipping
 AddressElement,
} from "@stripe/react-stripe-js";

const stripe = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = {/* ... */};

// Enable the skeleton loader UI for the optimal loading experience.
const loader = 'auto';

const CheckoutPage =({clientSecret}) => (
 <Elements stripe={stripe} options={{clientSecret, appearance, loader}}>
 <CheckoutForm />
 </Elements>
);

export default function CheckoutForm() {
 const stripe = useStripe();
 const elements = useElements();

 const handleSubmit = async (event) => {
 event.preventDefault();

 const {error} = await stripe.confirmPayment({
 elements,
 confirmParams: {
 return_url: "https://example.com/order/123/complete",
 },
 });

 if (error) {
 // handle error
 }
 };

 return (
 <form onSubmit={handleSubmit}>
 <h3>Contact info</h3>
 <LinkAuthenticationElement />
 {/* If collecting shipping */}
 <h3>Shipping</h3>
 <AddressElement options={{mode: 'shipping', allowedCountries: ['US']}} />
 <h3>Payment</h3>
 <PaymentElement />

 <button type="submit">Submit</button>
 </form>
 );
}
```

The `return_url` corresponds to a page on your website that provides [the
payment
status](https://docs.stripe.com/payments/payment-intents/verifying-status) of
the `PaymentIntent` when you render the return page. When Stripe redirects the
customer to the `return_url`, you can use the following URL query parameters to
verify payment status. You can also append your own query parameters when
providing the `return_url`. These query parameters persist through the redirect
process.

ParameterDescription`payment_intent`The unique identifier for the
`PaymentIntent``payment_intent_client_secret`The [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
of the `PaymentIntent` object.[OptionalSeparate authorization and
captureServer-side](https://docs.stripe.com/payments/link/add-link-elements-integration#manual-capture)[Handle
post-payment
eventsServer-side](https://docs.stripe.com/payments/link/add-link-elements-integration#web-post-payment)
Stripe sends a
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
event when the payment completes. [Use a webhook to receive these
events](https://docs.stripe.com/webhooks/quickstart) and run actions, like
sending an order confirmation email to your customer, logging the sale in a
database, or starting a shipping workflow.

Configure your integration to listen for these events rather than waiting on a
callback from the client. When you wait on a callback from the client, the
customer can close the browser window or quit the app before the callback
executes. Setting up your integration to listen for asynchronous events enables
you to accept [different types of payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

In addition to handling the `payment_intent.succeeded` event, you can also
handle two other important events when collecting payments with the Payment
Element:

EventDescriptionAction[payment_intent.succeeded](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.succeeded)Sent
from Stripe when a customer has successfully completed a payment.Send the
customer an order confirmation and fulfill their
order.[payment_intent.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent
from Stripe when a customer attempted a payment, but the payment didn’t
succeed.If a payment transitioned from `processing` to `payment_failed`, offer
the customer another attempt to pay.[Test the
integration](https://docs.stripe.com/payments/link/add-link-elements-integration#web-test-the-integration)
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
invalid000002Error, code expired000003Error, max attempts exceeded
For testing specific payment methods, refer to the [Payment Element testing
examples](https://docs.stripe.com/payments/accept-a-payment?platform=web#additional-testing-resources).

### Multiple funding sources

As Stripe adds additional funding source support, you don’t need to update your
integration. Stripe automatically supports them with the same transaction
settlement time and guarantees as card and bank account payments.

### Card authentication and 3D Secure

Link supports [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2)
authentication for card payments. 3DS2 requires customers to complete an
additional verification step with the card issuer when paying. Payments that
have been successfully authenticated using 3D Secure are covered by a liability
shift.

To trigger 3DS2 authentication challenge flows with Link in a sandbox, use the
following test card with any CVC, postal code, and future expiration date:
4000000000003220.

In a sandbox, the authentication process displays a mock authentication page. On
that page, you can either authorize or cancel the payment. Authorizing the
payment simulates successful authentication and redirects you to the specified
return URL. Clicking the **Failure** button simulates an unsuccessful attempt at
authentication.

For more details, refer to the [3D Secure authentication
page](https://docs.stripe.com/payments/3d-secure).

#### Note

When testing 3DS flows, only test cards for 3DS2 will trigger authentication on
Link.

[OptionalDisplay customer-saved
dataServer-sideClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#display-customer-saved-data)[OptionalSave
Link payment
methodsServer-sideClient-side](https://docs.stripe.com/payments/link/add-link-elements-integration#saving-link-payment-methods)
## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## See also

- [What is Link](https://docs.stripe.com/payments/link)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)
- [Link in the Payment
Element](https://docs.stripe.com/payments/link/payment-element-link)
- [Explore the Link Authentication
Element](https://docs.stripe.com/payments/link/link-authentication-element)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Payment Intents API](https://docs.stripe.com/api/payment_intents)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
-
[defaultValues](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)
- [Address Element](https://docs.stripe.com/elements/address-element)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [future usage with Setup
Intents](https://docs.stripe.com/payments/save-and-reuse)
- [dynamically offer your customers the most relevant payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [payment method
settings](https://dashboard.stripe.com/settings/payment_methods)
-
[payment_method_types](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [Enable HTTPS](https://docs.stripe.com/security/guide#tls)
- [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
- [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js)
- [appearance option](https://docs.stripe.com/elements/appearance-api)
-
[stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
-
[if_required](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)
- [the payment
status](https://docs.stripe.com/payments/payment-intents/verifying-status)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
- [Use a webhook to receive these
events](https://docs.stripe.com/webhooks/quickstart)
- [different types of payment
methods](https://stripe.com/payments/payment-methods-guide)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.succeeded)
-
[payment_intent.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)
- [sandbox](https://docs.stripe.com/sandboxes)
- [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [Payment Element testing
examples](https://docs.stripe.com/payments/accept-a-payment?platform=web#additional-testing-resources)
- [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2)
- [3D Secure authentication page](https://docs.stripe.com/payments/3d-secure)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)
- [Link in the Payment
Element](https://docs.stripe.com/payments/link/payment-element-link)
- [Explore the Link Authentication
Element](https://docs.stripe.com/payments/link/link-authentication-element)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)