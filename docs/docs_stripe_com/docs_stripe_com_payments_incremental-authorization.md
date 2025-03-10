# Increment an authorization

## Increase an existing authorization on a confirmed PaymentIntent before you capture it.

Stripe-hosted pageEmbedded formAdvanced integration
Incremental authorization allows you to increase the authorized amount on a
confirmed PaymentIntent before you capture it. Before capture, each incremental
authorization appears on the credit card statement as an additional pending
entry (for example, a 10 USD authorization incremented to 15 USD appears as
separate 10 USD and 5 USD pending entries). After capture, the pending
authorizations are removed, and the total captured amount appears as one final
entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- It’s only available with Visa, Mastercard, or Discover.
- Certain card brands have merchant category restrictions (see below).
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
is set to `payment` and
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
is set to `manual` on the
[CheckoutSession](https://docs.stripe.com/api/checkout/sessions/).

To learn more about incremental authorization and in-person payments made using
Terminal, see [Incremental
Authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations).

#### IC+ feature

We offer incremental authorizations to users on
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
pricing. If you’re on standard Stripe pricing and want access to this feature,
you can learn more at [support.stripe.com](https://support.stripe.com/).

### Availability by card network and merchant category

Use incremental authorizations on payments that fulfill the criteria below. You
can find your user category in the
[Dashboard](https://dashboard.stripe.com/settings/update/company/update).

Attempting to perform an incremental authorization on a payment that doesn’t
fulfill the below criteria results in an error.

Card brandMerchant countryPayment typeMerchant categoryVisaGlobalAll card
payment typesAll user categoriesMastercardGlobal*All card payment typesAll user
categoriesDiscoverGlobalAll card payment typesCar rental, hotels, local/suburban
commuter, passenger transportation, including ferries, passenger railways, bus
lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery
stores and supermarkets, electric vehicle charging, eating places and
restaurants, drinking places (alcoholic beverages), hotels, motels, resorts,
trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile
rental agency, truck and utility trailer rentals, motor home and rec vehicle
rentals, parking lots, parking meters, and garages, amusement parks, circuses,
fortune tell, recreation services (not classified)DiscoverGlobalCard not
presentTaxicabs and limousines
* Excludes MX users and JPY transactions for JP users

### Networks with limited support (beta)

### Incremental authorizations with Strong Customer Authentication (SCA)

If you and the cardholder are in a [country with SCA
requirements](https://support.stripe.com/questions/countries-in-the-european-economic-area-(eea)-impacted-by-strong-customer-authentication-(sca)-regulation),
there are important considerations to keep in mind when using incremental
authorization.

When you request the incremental authorization feature during the initial
authorization, Stripe automatically configures the payment method for future
off-session usage. Although this requires 3D Secure (3DS) for the initial
authorization, subsequent incremental authorizations on this payment is
considered merchant-initiated, potentially exempting any additional SCA. Clearly
indicate to your customer during the initial transaction that their payment will
be saved for future off-session usage with the incremental authorizations.

With some 3DS transactions, the [liability for fraudulent chargebacks (stolen or
counterfeit cards) shifts from you to the card
issuer](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments).
You don’t benefit from liability shift when submitting merchant-initiated
transactions.

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. For instance, if you
want to save their payment method for future use, such as charging them when
they’re not actively using your website or app. Add terms to your website or app
that state how you plan to save payment method details and allow customers to
opt in.

If you want to charge them when they’re offline, make sure your terms include
the following:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges
are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

## Best practices

When using incremental authorization, proactively notify your end customer with
the details of any authorizations for estimated amounts, which might be followed
by incremental authorizations that increase those amounts. Here are some best
practices for doing so:

- Disclose that an authorization is for an estimated amount and that subsequent
authorization requests might follow at the time of checkout, before purchase.
- Base estimated amounts on a genuine estimate of what the total transaction
amount will be.

You can use the
[custom_text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_text)
field when creating a new
[CheckoutSession](https://docs.stripe.com/api/checkout_sessions) to display
additional text on the checkout page to help meet compliance requirements.

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when using incremental authorization. Consult the network
rules for the card networks that you plan to use this feature with to make sure
your sales comply with applicable rules, which vary by network. For example,
most card networks restrict how you can calculate estimated amounts included in
the initial authorization, and prohibit the use of incremental authorizations
for transactions where the transaction amount should be known at the time of
authorization (for example, charges for recurring subscriptions).

The information provided on this page relating to your compliance with these
requirements is for your general guidance, and isn’t legal, tax, accounting, or
other professional advice. Consult with a professional if you’re unsure about
your obligations.

[Create a
CheckoutSession](https://docs.stripe.com/payments/incremental-authorization#create-and-confirm)
Add a checkout button to your website that calls a server-side endpoint to
create a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create).

```
<html>
 <head>
 <title>Buy cool new product</title>
 </head>
 <body>
<!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

A Checkout Session is the programmatic representation of what your customer sees
when they’re redirected to the payment form. You can configure it with options
such as:

- [Line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
to charge
- Currencies to use

You must populate `success_url` with the URL value of a page on your website
that Checkout returns your customer to after they complete the payment. You can
optionally also provide a `cancel_url` value of a page on your website that
Checkout returns your customer to if they terminate the payment process before
completion.

#### Note

Checkout Sessions expire 24 hours after creation by default.

After creating a Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

Lastly, set
[request_incremental_authorization](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_incremental_authorization)
as `if_available` to enable the incremental authorization feature.

```
# This example sets up an endpoint using the Sinatra framework.
# Watch this video to get started: https://youtu.be/8aA9Enb8NVc.

require 'json'
require 'sinatra'
require 'stripe'

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/create-checkout-session' do
 session = Stripe::Checkout::Session.create({
 line_items: [{
 price_data: {
 currency: 'usd',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 payment_method_options: {
 card: {
 request_incremental_authorization: 'if_available',
 },
 },
 mode: 'payment',
 # These placeholder URLs will be replaced in a following step.
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
 })

 redirect session.url, 303
end
```

After the customer has completed checkout, the
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
field on the [latest_charge](https://docs.stripe.com/api/charges/object) in the
[PaymentIntent](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_intent)
contains `available` or `unavailable` based on the customer’s payment method and
[the availability criteria mentioned
above](https://docs.stripe.com/payments/incremental-authorization#availability),
which determines whether a PaymentIntent is eligible for incremental
authorization or not. (If you didn’t request incremental authorization when
creating the CheckoutSession, it will be `unavailable`.)

```
{
 "id": "pi_ANipwO3zNfjeWODtRPIg",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 1000,
 "amount_received": 0,
 ...
 // if latest_charge is expanded
 {
 "latest_charge": {
 "amount": 1000,
 "payment_method_details": {
 "card": {
 "incremental_authorization": {
 "status": "available" // or "unavailable"
 }
 }
 }
 ...
 }
 }

}
```

[Mount
Checkout](https://docs.stripe.com/payments/incremental-authorization#mount-checkout)HTML
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

[Show a return
page](https://docs.stripe.com/payments/incremental-authorization#return-page)
After your customer attempts payment, Stripe redirects them to a return page
that you host on your site. When you created the Checkout Session, you specified
the URL of the return page in the
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
parameter. Read more about other options for [customizing redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form).

When rendering your return page, retrieve the Checkout Session status using the
Checkout Session ID in the URL. Handle the result according to the session
status as follows:

- `complete`: The payment succeeded. Use the information from the Checkout
Session to render a success page.
- `open`: The payment failed or was canceled. Remount Checkout so that your
customer can try again.

```
get '/session-status' do
 session = Stripe::Checkout::Session.retrieve(params[:session_id])

{status: session.status, customer_email: session.customer_details.email}.to_json
end
```

```
const session = await fetch(`/session_status?session_id=${session_id}`)
if (session.status == 'open') {
 // Remount embedded Checkout
} else if (session.status == 'complete') {
 // Show success page
 // Optionally use session.payment_status or session.customer_email
 // to customize the success page
}
```

#### Redirect-based payment methods

During payment, some payment methods redirect the customer to an intermediate
page, such as a bank authorization page. When they complete that page, Stripe
redirects them to your return page.

Learn more about [redirect-based payment methods and redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form#redirect-based-payment-methods).

[Perform an incremental
authorization](https://docs.stripe.com/payments/incremental-authorization#increment-authorization)
To increase the authorized amount on a PaymentIntent, use the
[increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization)
endpoint and provide the updated total [authorization
amount](https://docs.stripe.com/api/payment_intents/increment_authorization#increment_authorization-amount)
to increment to, which must be greater than the original authorized amount. This
attempts to authorize for a higher amount on your customer’s card. A single
PaymentIntent can call this endpoint multiple times to further increase the
authorized amount.

You have a maximum of 10 incremental authorization attempts per PaymentIntent.

```
curl
https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/increment_authorization
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=1500
```

If the incremental authorization succeeds, it returns the PaymentIntent object
with the updated amount. If the authorization fails, it returns a
[card_declined](https://docs.stripe.com/error-codes#card-declined) error
instead. The PaymentIntent object remains capturable for the previously
authorized amount. Any potential updates to other PaymentIntent fields (for
example,
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount),
[transfer_data](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-transfer_data),
[metadata](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-metadata),
[description](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-description),
and
[statement_descriptor](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-statement_descriptor))
aren’t saved if the incremental authorization fails.

Incremental authorization has a maximum cap of either 500 USD (or local
equivalent) over, or 500% over the previously authorized amount (whichever is
higher) for each individual increment.

[Capture the
PaymentIntent](https://docs.stripe.com/payments/incremental-authorization#capture-payment-intent)
Whether you increase the authorized amount on a PaymentIntent with an
incremental authorization or not, you need to capture the funds before the
initial authorization expires–incremental authorizations don’t extend [the
validity
period](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method). To
capture the authorized amount on a PaymentIntent with prior incremental
authorizations, use the [capture
endpoint](https://docs.stripe.com/api/payment_intents/capture) as usual.

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

If the incremental authorization succeeds, it returns the captured PaymentIntent
object with the updated amount. If the authorization fails, it returns a
[card_declined error](https://docs.stripe.com/error-codes#card-declined)
instead. The PaymentIntent isn’t captured, but it remains capturable for the
previously authorized amount. Any potential updates to other PaymentIntent
fields (for example,
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount),
[transfer_data](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-transfer_data),
[metadata](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-metadata),
[description](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-description)
and
[statement_descriptor](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-statement_descriptor))
aren’t saved if the incremental authorization fails.

[Test your
integration](https://docs.stripe.com/payments/incremental-authorization#test-your-integration)
Use the incremental authorization Stripe test card with any CVC, postal code,
and future expiration to trigger incremental authorization while in test mode:

- First create the CheckoutSession using the test card in the [create a
CheckoutSession
step](https://docs.stripe.com/payments/incremental-authorization#create-and-confirm)
above.
- Perform the incremental authorization with the parameters specified in the
[perform an incremental authorization
step](https://docs.stripe.com/payments/incremental-authorization#increment-authorization)
above, and use the test card to trigger an incremental authorization.
NumberPayment
MethodDescription4000058400000063`pm_card_debit_incrementalAuthAuthorized`This
increases the authorization amount to the amount provided in the request.

## Links

-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
-
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
- [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/)
- [Incremental
Authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations)
-
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [support.stripe.com](https://support.stripe.com/)
- [Dashboard](https://dashboard.stripe.com/settings/update/company/update)
- [country with SCA
requirements](https://support.stripe.com/questions/countries-in-the-european-economic-area-(eea)-impacted-by-strong-customer-authentication-(sca)-regulation)
- [liability for fraudulent chargebacks (stolen or counterfeit cards) shifts
from you to the card
issuer](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
-
[custom_text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_text)
- [CheckoutSession](https://docs.stripe.com/api/checkout_sessions)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create)
- [Line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[request_incremental_authorization](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_incremental_authorization)
- [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
- [latest_charge](https://docs.stripe.com/api/charges/object)
-
[PaymentIntent](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_intent)
- [Stripe.js](https://docs.stripe.com/js)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [branding settings](https://dashboard.stripe.com/settings/branding)
-
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
- [customizing redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form)
- [redirect-based payment methods and redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form#redirect-based-payment-methods)
-
[increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization)
- [authorization
amount](https://docs.stripe.com/api/payment_intents/increment_authorization#increment_authorization-amount)
- [card_declined](https://docs.stripe.com/error-codes#card-declined)
-
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount)
-
[transfer_data](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-transfer_data)
-
[metadata](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-metadata)
-
[description](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-description)
-
[statement_descriptor](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-statement_descriptor)
- [the validity
period](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [capture endpoint](https://docs.stripe.com/api/payment_intents/capture)