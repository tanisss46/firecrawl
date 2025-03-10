# Save a card without bank authentication

## Collect card details and charge your customer at a later time.

​​Stripe allows you to collect card details and charge your customer at a later
time. ​​In some regions, banks require a second form of authentication such as
entering a code sent to a phone. ​​The extra step decreases conversion if your
customer isn’t actively using your website or application because they aren’t
available to authenticate the purchase.

​​If you primarily do business in the US and Canada, banks don’t require
authentication, so you can follow this simpler integration. This integration
will be non-compliant in countries that require authentication for saving cards
(for example, India) so building this integration means that expanding to other
countries or adding other payment methods will require significant changes.
Learn how to [save cards that require
authentication](https://docs.stripe.com/payments/save-and-reuse).

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. For instance, if you
want to save their payment method for future use, such as charging them when
they’re not actively using your website or app. Add terms to your website or app
that state how you plan to save payment method details and allow customers to
opt in. If you want to charge them when they’re offline, make sure your terms
include the following:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges
are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

[Collect card
detailsClient-side](https://docs.stripe.com/payments/save-card-without-authentication#web-collect-card-details)
Before starting this guide, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Build a checkout page to collect your customer’s card details. Use [Stripe
Elements](https://docs.stripe.com/payments/elements), a UI library that helps
you build custom payment forms. To get started with Elements, include the
Stripe.js library with the following script on your checkout page.

```
<script src="https://js.stripe.com/v3/"></script>
```

Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t
include the script in a bundle or host a copy of it yourself.

To best leverage Stripe’s [advanced fraud
functionality](https://docs.stripe.com/radar), include this script on every page
on your site, not just the checkout page. Including the script on every page
[allows Stripe to detect suspicious
behavior](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)
that might indicate fraud when users browse your website.

### Add Elements to your page

To securely collect card details from your customers, Elements creates UI
components for you hosted by Stripe. They’re then placed into your payment form,
rather than you creating them directly. To determine where to insert these
components, create empty DOM elements (containers) with unique IDs within your
payment form.

```
<input id="cardholder-name" type="text">
<!-- placeholder for Elements -->
<div id="card-element"></div>
<div id="card-result"></div>
<button id="card-button">Save Card</button>
```

Next, create an instance of the [Stripe
object](https://docs.stripe.com/js#stripe-function), providing your publishable
[API key](https://docs.stripe.com/keys) as the first parameter. After, create an
instance of the [Elements object](https://docs.stripe.com/js#stripe-elements)
and use it to mount a `card` element in the DOM.

The `card` Element simplifies the payment form and minimizes the number of
required fields by inserting a single, flexible input field that securely
collects all necessary card details.

Otherwise, combine `cardNumber`, `cardExpiry`, and `cardCvc` Elements for a
flexible, multi-input card form.

#### Note

Always collect a postal code to increase card acceptance rates and reduce fraud.

The [single line Card
Element](https://docs.stripe.com/js/element/other_element?type=card)
automatically collects and sends the customer’s postal code to Stripe. If you
build your payment form with split Elements ([Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber),
[Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry),
[CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)), add a
separate input field for the customer’s postal code.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const elements = stripe.elements();
const cardElement = elements.create('card');
cardElement.mount('#card-element');
```

A Stripe Element contains an iframe that securely sends the payment information
to Stripe over an HTTPS connection. The checkout page address must also start
with `https://` rather than `http://` for your integration to work.

You can test your integration without using HTTPS. [Enable
it](https://docs.stripe.com/security/guide#tls) when you’re ready to accept live
payments.

```
const cardholderName = document.getElementById('cardholder-name');
const cardButton = document.getElementById('card-button');
const resultContainer = document.getElementById('card-result');

cardButton.addEventListener('click', async (ev) => {
 const {paymentMethod, error} = await stripe.createPaymentMethod({
 type: 'card',
 card: cardElement,
 billing_details: {
 name: cardholderName.value,
 },
 }
 );

 if (error) {
 // Display error.message in your UI.
 resultContainer.textContent = error.message;
 } else {
 // You have successfully created a new PaymentMethod
 resultContainer.textContent = "Created payment method: " + paymentMethod.id;
 }
});
```

Send the resulting [PaymentMethod](https://docs.stripe.com/api/payment_methods)
ID to your server.

[Set up
StripeServer-side](https://docs.stripe.com/payments/save-card-without-authentication#web-setup)
Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Save the
cardServer-side](https://docs.stripe.com/payments/save-card-without-authentication#web-save-card)
Save the card by attaching the PaymentMethod to a
[Customer](https://docs.stripe.com/api/customers). You can use the Customer
object to store other information about your customer, such as shipping details
and email address.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_method={{PAYMENT_METHOD_ID}}
```

If you have an existing Customer, you can attach the PaymentMethod to that
object instead.

```
curl https://api.stripe.com/v1/payment_methods/{{PAYMENT_METHOD_ID}}/attach \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}}
```

At this point, associate the Customer ID and the PaymentMethod ID with your own
internal representation of a customer, if you have one.

[Charge the saved
cardServer-side](https://docs.stripe.com/payments/save-card-without-authentication#web-charge-card)
When you’re ready, fetch the PaymentMethod and Customer IDs to charge. You can
do this by either storing the IDs of both in your database, or by using the
Customer ID to look up all the Customer’s available PaymentMethods.

```
curl -G https://api.stripe.com/v1/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d type=card
```

Use the PaymentMethod ID and the Customer ID to create a new PaymentIntent. Set
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
to true to decline payments that require any actions from your customer, such as
two-factor authentication.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d error_on_requires_action=true \
 -d confirm=true
```

When a payment attempt fails, the request also fails with a 402 HTTP status code
and Stripe throws an error. You need to notify your customer to return to your
application (for example, by sending an email) to complete the payment. Check
the code of the [Error](https://docs.stripe.com/api/errors/handling) raised by
the Stripe API library or check the
[last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
on the PaymentIntent to inspect why the card issuer declined the payment.

[Handle any card
errors](https://docs.stripe.com/payments/save-card-without-authentication#web-handle-errors)
Notify your customer that the payment failed and direct them to the payment form
you made in Step 1 where they can enter new card details. Send that new
PaymentMethod ID to your server to
[attach](https://docs.stripe.com/api/payment_methods/attach) to the Customer
object and make the payment again.

Alternatively, you can create a PaymentIntent and save a card all in one API
call if you have already created a Customer.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d error_on_requires_action=true \
 -d confirm=true \
 -d setup_future_usage=on_session
```

Setting
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
to `on_session` indicates to Stripe that you wish to save the card for later,
without triggering unnecessary authentication.

[Test the
integration](https://docs.stripe.com/payments/save-card-without-authentication#web-test-integration)
Stripe provides [test cards](https://docs.stripe.com/testing) you can use in a
sandbox to simulate different cards’ behavior. Use these cards with any CVC,
postal code, and expiry date in the future.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000000000009995Always fails with a decline code of
`insufficient_funds`.4000002500003155Requires authentication, which in this
integration will decline with a code of
`authentication_required`.[OptionalRe-collect a
CVC](https://docs.stripe.com/payments/save-card-without-authentication#web-recollect-cvc)
## Upgrade your integration to handle card authentication

This integration **declines cards that require authentication during payment**.
If you start seeing many payments in the Dashboard listed as `Failed`, then it’s
time to [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions).
Stripe’s global integration handles these payments instead of automatically
declining.

## Links

- [save cards that require
authentication](https://docs.stripe.com/payments/save-and-reuse)
- [Register now](https://dashboard.stripe.com/register)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [advanced fraud functionality](https://docs.stripe.com/radar)
- [allows Stripe to detect suspicious
behavior](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)
- [example payment forms](https://stripe.com/payments/elements/examples)
- [Stripe object](https://docs.stripe.com/js#stripe-function)
- [API key](https://docs.stripe.com/keys)
- [Elements object](https://docs.stripe.com/js#stripe-elements)
- [single line Card
Element](https://docs.stripe.com/js/element/other_element?type=card)
- [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber)
- [Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry)
- [CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)
- [Enable it](https://docs.stripe.com/security/guide#tls)
- [View full
sample](https://github.com/stripe-samples/saving-card-without-payment/blob/master/client/script.js#L41-L46)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Customer](https://docs.stripe.com/api/customers)
-
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
- [Error](https://docs.stripe.com/api/errors/handling)
-
[last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
- [attach](https://docs.stripe.com/api/payment_methods/attach)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [test cards](https://docs.stripe.com/testing)
- [upgrade your
integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions)