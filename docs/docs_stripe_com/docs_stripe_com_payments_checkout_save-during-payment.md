# Save payment details during payment

## Learn how to accept a payment and save your customer's payment details for future purchases.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Use [Stripe Checkout](https://docs.stripe.com/payments/checkout) to embed a
prebuilt payment form on your website that allows your customers to save their
payment details for future purchases.

[Set up
StripeServer-side](https://docs.stripe.com/payments/checkout/save-during-payment?payment-ui=embedded-form#set-up-stripe)
First, [register](https://dashboard.stripe.com/register) for a Stripe account.

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
customerServer-side](https://docs.stripe.com/payments/checkout/save-during-payment?payment-ui=embedded-form#create-a-customer)
To set a card up for future payments, you must attach it to a
[Customer](https://docs.stripe.com/api/customers). Create a Customer object when
your customer creates an account with your business. Customer objects allow for
reusing payment methods and tracking across multiple payments.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jennyrosen@example.com"
```

Successful creation returns the
[Customer](https://docs.stripe.com/api/customers/object) object. You can inspect
the object for the customer `id` and store the value in your database for later
retrieval.

You can find these customers in the
[Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/checkout/save-during-payment?payment-ui=embedded-form#create-checkout-session)
From your server, create a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) and set the
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
to `embedded`. You can configure the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create) with [line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
to include and options such as
[currency](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-currency).

You can also create a Checkout Session for an [existing
customer](https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted),
allowing you to prefill Checkout fields with known contact information and unify
your purchase history for that customer.

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

After you create the Checkout Session, use the `client_secret` returned in the
response to [mount
Checkout](https://docs.stripe.com/payments/checkout/save-during-payment?payment-ui=embedded-form#mount-checkout).

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
 mode: 'payment',
 ui_mode: 'embedded',
return_url:
'https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}'
 })

 {clientSecret: session.client_secret}.to_json
end
```

[Mount
CheckoutClient-sideServer-side](https://docs.stripe.com/payments/checkout/save-during-payment?payment-ui=embedded-form#mount-checkout)HTML
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

[Save payment
methodServer-side](https://docs.stripe.com/payments/checkout/save-during-payment?payment-ui=embedded-form#save-payment-method)
After setting up your embedded Checkout integration, choose a configuration for
your integration to save the payment methods used by your customers.

By default, payment methods used to make a one-time payment with Checkout aren’t
available for future use.

### Save payment methods to charge them off-session

You can set Checkout to save payment methods used to make a one-time payment by
passing the
[payment_intent_data.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage)
argument. This is useful if you need to capture a payment method on-file to use
for future fees, such as cancellation or no-show fees.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer_creation=always \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return" \
 -d "payment_intent_data[setup_future_usage]"=off_session
```

If you use Checkout in `subscription` mode, Stripe automatically saves the
payment method to charge it for subsequent payments. Card payment methods saved
to customers using either `setup_future_usage` or `subscription` mode don’t
appear for return purchases in Checkout (more on this below). We recommend using
[custom text](https://docs.stripe.com/payments/checkout/customization/policies)
to link out to any relevant terms regarding the usage of saved payment
information.

#### Caution

Global privacy laws are complicated and nuanced. We recommend contacting your
legal and privacy team prior to implementing
[setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage)
because it might implicate your existing privacy compliance framework. Refer to
[the guidance issued by the European Protection
Board](https://edpb.europa.eu/system/files/2021-05/recommendations022021_on_storage_of_credit_card_data_en_1.pdf)
to learn more about saving payment details.

### Save payment methods to prefill them in Checkout

By default, Checkout uses
[Link](https://docs.stripe.com/payments/checkout/customization/behavior#link) to
provide your customers with the option to securely save and reuse their payment
information. If you prefer to manage payment methods yourself, use
[saved_payment_method_options.payment_method_save](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-saved_payment_method_options-payment_method_save)
when creating a Checkout Session to let your customers save their payment
methods for future purchases in Checkout.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer_creation=always \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d ui_mode=embedded \
 --data-urlencode return_url="https://example.com/return" \
 -d "saved_payment_method_options[payment_method_save]"=enabled
```

Passing this parameter in either
[payment](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
or
[subscription](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
mode displays an optional checkbox to let customers explicitly save their
payment method for future purchases. When customers check this checkbox,
Checkout saves the payment method with [allow_redisplay:
always](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay).
Checkout uses this parameter to determine whether a payment method can be
prefilled on future purchases. When using
`saved_payment_method_options.payment_method_save`, you don’t need to pass in
`setup_future_usage` to save the payment method.

Using
[saved_payment_method_options.payment_method_save](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-saved_payment_method_options-payment_method_save)
requires a `Customer`. To save a new customer, set the Checkout Session’s
[customer_creation](https://docs.stripe.com/api/checkout/sessions/create) to
`always`. Otherwise, the session doesn’t save the customer or the payment
method.

If `payment_method_save` isn’t passed in or if the customer doesn’t agree to
save the payment method, Checkout still saves payment methods created in
`subscription` mode or using `setup_future_usage`. These payment methods have an
`allow_redisplay` value of `limited`, which prevents them from being prefilled
for returning purchases and allows you to comply with card network rules and
data protection regulations. Learn how to [change the default behavior enabled
by these
modes](https://support.stripe.com/questions/prefilling-saved-cards-in-checkout)
and how to change or override `allow_redisplay` behavior.

#### Note

You can use Checkout to save cards and other payment methods to charge them
off-session, but Checkout only prefills saved cards. Learn how to [prefill saved
cards](https://support.stripe.com/questions/prefilling-saved-cards-in-checkout).
To save a payment method without an initial payment, [use Checkout in setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout).

## Links

- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [register](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [Customer](https://docs.stripe.com/api/customers/object)
- [Customers](https://dashboard.stripe.com/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[ui_mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-ui_mode)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create)
- [line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
-
[currency](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-currency)
- [existing
customer](https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted)
-
[return_url](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-return_url)
- [configuring the return
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=embedded-form#return-page)
- [customizing redirect
behavior](https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui=embedded-form)
- [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}](https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID})
- [Stripe.js](https://docs.stripe.com/js)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
-
[payment_intent_data.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage)
- [https://example.com/return](https://example.com/return)
- [custom
text](https://docs.stripe.com/payments/checkout/customization/policies)
- [the guidance issued by the European Protection
Board](https://edpb.europa.eu/system/files/2021-05/recommendations022021_on_storage_of_credit_card_data_en_1.pdf)
- [Link](https://docs.stripe.com/payments/checkout/customization/behavior#link)
-
[saved_payment_method_options.payment_method_save](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-saved_payment_method_options-payment_method_save)
-
[payment](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
- [allow_redisplay:
always](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
- [change the default behavior enabled by these
modes](https://support.stripe.com/questions/prefilling-saved-cards-in-checkout)
- [use Checkout in setup
mode](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)