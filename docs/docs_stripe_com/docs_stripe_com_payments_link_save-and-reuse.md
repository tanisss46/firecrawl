# Set up future payments using Elements and Link

## Save your Link customers' details and charge them later.

This guide walks you through how to accept payments with
[Link](https://docs.stripe.com/payments/link) using the [Setup Intents
API](https://docs.stripe.com/api/setup_intents) and either the [Payment
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
StripeServer-side](https://docs.stripe.com/payments/link/save-and-reuse#set-up-stripe)
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
CustomerServer-side](https://docs.stripe.com/payments/link/save-and-reuse#create-customer)
To set up a payment method for future payments, you must attach it to a
[Customer](https://docs.stripe.com/api/customers). Create a `Customer` object
when your customer creates an account with your business. `Customer` objects
allow for reusing payment methods and tracking across multiple payments.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a
SetupIntentServer-side](https://docs.stripe.com/payments/link/save-and-reuse#web-create-intent)
#### Note

If you want to render the Payment Element without first creating a SetupIntent,
see [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?type=setup).

A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent to set up a customer’s payment method for future payments
during a session and tracks the status of that session. Create a SetupIntent on
your server with `link` and the other payment methods you want to support:

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=card \
 -d "payment_method_types[]"=link
```

To see how to set up other payment methods, see the [Set up future
payments](https://docs.stripe.com/payments/save-and-reuse) guide.

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

[Collect customer
email](https://docs.stripe.com/payments/link/save-and-reuse#design-your-integration)
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
formClient-side](https://docs.stripe.com/payments/link/save-and-reuse#web-collect-payment-details)
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
step](https://docs.stripe.com/payments/link/save-and-reuse#web-create-intent).
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
dataClient-side](https://docs.stripe.com/payments/link/save-and-reuse#prefill-customer-data)[OptionalCollect
shipping
addressesClient-side](https://docs.stripe.com/payments/link/save-and-reuse#collect-shipping)[OptionalCustomize
the
appearanceClient-side](https://docs.stripe.com/payments/link/save-and-reuse#customize-appearance)[Submit
the
SetupIntentClient-side](https://docs.stripe.com/payments/link/save-and-reuse#web-submit-payment)
Use
[stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup) to
complete the setup with the details you collected. Provide a
[return_url](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-return_url)
to this function so that Stripe can redirect users after they complete their
setup. When a payment is successful, Stripe immediately redirects Link and card
payments to the `return_url`.

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

 const {error} = await stripe.confirmSetup({
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

[Charge the saved payment method
laterServer-side](https://docs.stripe.com/payments/link/save-and-reuse#charge-saved-payment-method)
When you’re ready to charge your customer, use the Customer and PaymentMethod
IDs to create a PaymentIntent. To find a payment method to charge, list the
payment methods associated with your customer.

```
curl https://api.stripe.com/v1/payment_methods \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "type"="link" \
 -G
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with
the amount and currency of the payment with these parameters:

- Set the value of the PaymentIntent’s
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
property to `true`, which causes confirmation to occur immediately when the
PaymentIntent is created.
- Set
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
to the ID of the PaymentMethod
- Set [customer](https://docs.stripe.com/api#create_payment_intent-customer) to
the ID of the Customer.
- Set
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
to `true`. This causes the PaymentIntent to send an error if authentication is
required when your customer isn’t actively using your site or app.

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

[Test the
integration](https://docs.stripe.com/payments/link/save-and-reuse#web-test-the-integration)
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

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## See also

- [Link in the Payment
Element](https://docs.stripe.com/payments/link/payment-element-link)
- [Explore the Link Authentication
Element](https://docs.stripe.com/payments/link/link-authentication-element)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
-
[defaultValues](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)
- [Address Element](https://docs.stripe.com/elements/address-element)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [Customer](https://docs.stripe.com/api/customers)
- [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred?type=setup)
- [Set up future payments](https://docs.stripe.com/payments/save-and-reuse)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [Enable HTTPS](https://docs.stripe.com/security/guide#tls)
- [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js)
- [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js)
- [appearance option](https://docs.stripe.com/elements/appearance-api)
- [stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup)
-
[return_url](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-return_url)
-
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
-
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
- [customer](https://docs.stripe.com/api#create_payment_intent-customer)
-
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
- [sandbox](https://docs.stripe.com/sandboxes)
- [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [Payment Element testing
examples](https://docs.stripe.com/payments/accept-a-payment?platform=web#additional-testing-resources)
- [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2)
- [3D Secure authentication page](https://docs.stripe.com/payments/3d-secure)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)
- [Link in the Payment
Element](https://docs.stripe.com/payments/link/payment-element-link)
- [Explore the Link Authentication
Element](https://docs.stripe.com/payments/link/link-authentication-element)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)