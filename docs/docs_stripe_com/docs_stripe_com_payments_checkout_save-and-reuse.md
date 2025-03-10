# Set up future payments

## Learn how to save payment details in a Checkout session and charge your customers later.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
To collect customer payment details that you can reuse later, use Checkout’s
setup mode. Setup mode uses the [Setup Intents
API](https://docs.stripe.com/api/setup_intents) to create [Payment
Methods](https://docs.stripe.com/api/payment_methods).

[Set up
StripeServer-side](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries to access the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#create-checkout-session)
From your server, create a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) and set the
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
to `embedded`. To create a setup mode Checkout Session, set the
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
to `setup`.

To return customers to a custom page that you host on your website, specify that
page’s URL in the
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL to
retrieve the session’s status on the return page. Checkout automatically
substitutes the variable with the Checkout Session ID before redirecting.

Read more about [configuring the return
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form#return-page)
and other options for [customizing redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form).

You can optionally specify the [customer
parameter](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
to automatically attach the created payment method to an existing customer.

After you create the Checkout Session, use the `client_secret` returned in the
response to [mount
Checkout](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#mount-checkout).

```
# This example sets up an endpoint using the Sinatra framework.
# To learn more about Sinatra, watch this video: https://youtu.be/8aA9Enb8NVc.
require 'json'
require 'sinatra'
require 'stripe'

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/create-checkout-session' do
 session = Stripe::Checkout::Session.create({
 currency: 'usd',
 mode: 'setup',
 ui_mode: 'embedded',
 return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
 })

 {clientSecret: session.client_secret}.to_json
end
```

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn
individual payment methods on or off in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout,
Stripe evaluates the currency and any restrictions, then dynamically presents
the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or
set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). By default,
Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe
filters them out even when they’re enabled. We filter Google Pay if you [enable
automatic tax](https://docs.stripe.com/tax/checkout) without collecting a
shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple
Pay or Google Pay. Stripe handles these payments the same way as other card
payments.

[Mount
CheckoutClient-side](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#mount-checkout)HTML
+ JSReact
Checkout is available as part of [Stripe.js](https://docs.stripe.com/js).
Include the Stripe.js script on your page by adding it to the head of your HTML
file. Next, create an empty DOM node (container) to use for mounting.

```
<head>
 <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
 <div id="checkout">
 <!-- Checkout will insert the payment form here -->
 </div>
</body>
```

Initialize Stripe.js with your publishable API key.

Create an asynchronous `fetchClientSecret` function that makes a request to your
server to create the Checkout Session and retrieve the client secret. Pass this
function into `options` when you create the Checkout instance:

```
// Initialize Stripe.js
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

initialize();

// Fetch Checkout Session and retrieve the client secret
async function initialize() {
 const fetchClientSecret = async () => {
 const response = await fetch("/create-checkout-session", {
 method: "POST",
 });
 const { clientSecret } = await response.json();
 return clientSecret;
 };

 // Initialize Checkout
 const checkout = await stripe.initEmbeddedCheckout({
 fetchClientSecret,
 });

 // Mount Checkout
 checkout.mount('#checkout');
}
```

Checkout renders in an iframe that securely sends payment information to Stripe
over an HTTPS connection.

#### Common mistake

Avoid placing Checkout within another iframe because some payment methods
require redirecting to another page for payment confirmation.

### Customize appearance

Customize Checkout to match the design of your site by setting the background
color, button color, border radius, and fonts in your account’s [branding
settings](https://dashboard.stripe.com/settings/branding).

By default, Checkout renders with no external padding or margin. We recommend
using a container element such as a div to apply your desired margin (for
example, 16px on all sides).

[Retrieve the Checkout
SessionServer-side](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#retrieve-checkout-session)
After a customer successfully completes their Checkout Session, you need to
retrieve the Session object. There are two ways to do this:

- **Asynchronously**: Handle `checkout.session.completed`
[webhooks](https://docs.stripe.com/webhooks), which contain a Session object.
Learn more about [setting up webhooks](https://docs.stripe.com/webhooks).
- **Synchronously**: Obtain the Session ID from the `return_url` when a user
redirects back to your site. Use the Session ID to
[retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve) the Session
object.

```
curl
https://api.stripe.com/v1/checkout/sessions/cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

The right choice depends on your tolerance for dropoff, as customers may not
always reach the `return_url` after a successful payment. It’s possible for them
close their browser tab before the redirect occurs. Handling webhooks prevents
your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the `setup_intent`
key, which is the ID for the SetupIntent created during the Checkout Session. A
[SetupIntent](https://docs.stripe.com/payments/setup-intents) is an object used
to set up the customer’s bank account information for future payments.

Example `checkout.session.completed` payload:

```
{
 "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
 "object": "event",
 "api_version": "2019-03-14",
 "created": 1561420781,
 "data": {
 "object": {
 "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
 "object": "checkout.session",
 "billing_address_collection": null,
 "client_reference_id": null,
 "customer": "",
 "customer_email": null,
 "display_items": [],
 "mode": "setup",
 "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
 "submit_type": null,
 "subscription": null,
 "success_url": "https://example.com/success"
 }
 },
 "livemode": false,
 "pending_webhooks": 1,
 "request": {
 "id": null,
 "idempotency_key": null
 },
 "type": "checkout.session.completed"
}
```

Note the `setup_intent` ID for the next step.

[Retrieve the
SetupIntentServer-side](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#retrieve-setup-intent)
Using the SetupIntent ID,
[retrieve](https://docs.stripe.com/api/setup_intents/retrieve) the SetupIntent
object. The returned object contains a `payment_method` ID that you can attach
to a customer in the next step.

```
curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

#### Note

If you’re requesting this information synchronously from the Stripe API (as
opposed to handling webhooks), you can combine the previous step with this step
by [expanding](https://docs.stripe.com/api/expanding_objects) the SetupIntent
object in the request to the /v1/checkout/session endpoint. Doing this prevents
you from having to make two network requests to access the newly created
PaymentMethod ID.

[Charge the payment method
laterServer-side](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=embedded-form#charge-saved-payment-method)
If you didn’t create the Checkout Session with an existing customer, use the ID
of the PaymentMethod to
[attach](https://docs.stripe.com/api/payment_methods/attach) the
[PaymentMethod](https://docs.stripe.com/api/payment_methods) to a
[Customer](https://docs.stripe.com/api/customers). After you attach the
PaymentMethod to a customer, you can make an off-session payment using a
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method):

- Set [customer](https://docs.stripe.com/api#create_payment_intent-customer) to
the ID of the Customer and
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
to the ID of the PaymentMethod.
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
property to `true`, which causes confirmation to occur immediately when you
create the PaymentIntent.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d off_session=true \
 -d confirm=true
```

When a payment attempt fails, the request also fails with a 402 HTTP status code
and the status of the PaymentIntent is
[requires_payment_method](https://docs.stripe.com/upgrades#2019-02-11). Notify
your customer to return to your application (for example, by sending an email or
in-app notification) and direct your customer to a new Checkout Session to
select another payment method.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=1099 \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d ui_mode=embedded \
--data-urlencode
return_url="https://example.com/return?session_id={CHECKOUT_SESSION_ID}"
```

## Links

- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [Payment Methods](https://docs.stripe.com/api/payment_methods)
- [Register now](https://dashboard.stripe.com/register)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
-
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
- [configuring the return
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form#return-page)
- [customizing redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form)
- [customer
parameter](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
- [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://example.com/return?session_id={CHECKOUT_SESSION_ID}](https://example.com/return?session_id={CHECKOUT_SESSION_ID})
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [enable automatic tax](https://docs.stripe.com/tax/checkout)
- [Stripe.js](https://docs.stripe.com/js)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [branding settings](https://dashboard.stripe.com/settings/branding)
- [webhooks](https://docs.stripe.com/webhooks)
- [retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve)
- [SetupIntent](https://docs.stripe.com/payments/setup-intents)
- [https://example.com/success](https://example.com/success)
- [retrieve](https://docs.stripe.com/api/setup_intents/retrieve)
- [expanding](https://docs.stripe.com/api/expanding_objects)
- [attach](https://docs.stripe.com/api/payment_methods/attach)
- [Customer](https://docs.stripe.com/api/customers)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method)
- [customer](https://docs.stripe.com/api#create_payment_intent-customer)
-
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
-
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
-
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
- [requires_payment_method](https://docs.stripe.com/upgrades#2019-02-11)