# Accept a payment using Stripe Elements and the Charges APICharges API

## Accept online payments from US and Canadian customers.

#### Legacy API

The content of this section refers to a Legacy feature. Use the [Payment Intents
API](https://docs.stripe.com/payments/accept-a-payment) instead.

The Charges API doesn’t support the following features, many of which are
required for credit card compliance:

- Merchants in India
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
WebiOSAndroid
Use Stripe Elements, our prebuilt UI components, to create a payment form that
lets you securely collect a customer’s card details without handling the
sensitive data. The card details are then converted to a representative
[Token](https://docs.stripe.com/api#tokens) that you can safely send to your
servers. Your server can use that token to create a charge.

[Set up
Stripe](https://docs.stripe.com/payments/accept-a-payment-charges#web-setup)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create your payment
formClient-side](https://docs.stripe.com/payments/accept-a-payment-charges#web-create-payment-form)
To securely collect card details from your customers, Stripe Elements creates UI
components for you that are hosted by Stripe. They’re then placed into your
payment form, rather than you creating them directly.

### Set up Stripe Elements

HTML + JSReact
To have Elements available in your webpage, add this script tag in the `head` of
your HTML page:

```
<script src="https://js.stripe.com/v3/"></script>
```

That script should always be loaded directly from **https://js.stripe.com**.

Create an instance of Elements with the following JavaScript on your payment
page:

```
// Set your publishable key: remember to change this to your live publishable
key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
```

Once Elements is loaded, you can create an empty DOM container with a unique ID
within your payment form wherever you want Elements to add its input field. We
recommend placing that container within a `<label>` or next to a `<label>` with
a `for` attribute that matches the unique `id` of the Element container. By
doing so, the Element automatically gains focus when the customer clicks on the
corresponding label.

For example:

```
<form action="/charge" method="post" id="payment-form">
 <div class="form-row">
 <label for="card-element">
 Credit or debit card
 </label>
 <div id="card-element">
 <!-- A Stripe Element will be inserted here. -->
 </div>

 <!-- Used to display Element errors. -->
 <div id="card-errors" role="alert"></div>
 </div>

 <button>Submit Payment</button>
</form>
```

When the form above has loaded, [create an
instance](https://docs.stripe.com/js#elements-create) of a `card` Element and
mount it to the Element container created above:

```
// Custom styling can be passed to options when creating an Element.
const style = {
 base: {
 // Add your base input styles here. For example:
 fontSize: '16px',
 color: '#32325d',
 },
};

// Create an instance of the card Element.
const card = elements.create('card', {style});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');
```

The `card` Element simplifies the form and minimizes the number of required
fields by inserting a single, flexible input field that securely collects all
necessary card details.

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

Refer to our [Stripe.js reference](https://docs.stripe.com/js#elements_create)
documentation for a full list of supported Element types.

[Create a
tokenClient-side](https://docs.stripe.com/payments/accept-a-payment-charges#web-create-token)HTML
+ JSReact
Add an event listener for when your customer submits their card information and
use `stripe.createToken(card)` to tokenize that information:

```
// Create a token or display an error when the form is submitted.
const form = document.getElementById('payment-form');
form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {token, error} = await stripe.createToken(card);

 if (error) {
 // Inform the customer that there was an error.
 const errorElement = document.getElementById('card-errors');
 errorElement.textContent = error.message;
 } else {
 // Send the token to your server.
 stripeTokenHandler(token);
 }
});
```

[createToken](https://docs.stripe.com/js/tokens/create_token?type=cardElement)
also accepts an optional second parameter containing additional card information
collected from the customer, which is not used in this example. The function
returns a `Promise` which resolves with a `result` object. This object has
either:

- `result.token`: a [Token](https://docs.stripe.com/api#tokens) was created
successfully.
- `result.error`: there was an error. This includes client-side validation
errors. Refer to the [API reference](https://docs.stripe.com/api#errors) for all
possible errors.

If the object contains a `result.token`, send it to your server. Otherwise, show
the customer an error.

[Submit the token to your
serverClient-side](https://docs.stripe.com/payments/accept-a-payment-charges#web-submit-payment)
Send the token to your server along with any additional information that has
been collected:

HTML + JSReact
```
const stripeTokenHandler = (token) => {
 // Insert the token ID into the form so it gets submitted to the server
 const form = document.getElementById('payment-form');
 const hiddenInput = document.createElement('input');
 hiddenInput.setAttribute('type', 'hidden');
 hiddenInput.setAttribute('name', 'stripeToken');
 hiddenInput.setAttribute('value', token.id);
 form.appendChild(hiddenInput);

 // Submit the form
 form.submit();
}
```

[Create a charge with the
tokenServer-side](https://docs.stripe.com/payments/accept-a-payment-charges#web-create-charge)
After the client posts the token to your server, you can use it to create a
charge. On your server, grab the Stripe token in the POST parameters submitted
by your form. From there, it’s one API call to charge the card:

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=999 \
 -d "currency"="usd" \
 -d "description"="Example charge" \
 -d "source"="tok_visa"
```

The response from creating a charge will either be a
[charge](https://docs.stripe.com/api/charges/object) or an
[error](https://docs.stripe.com/api/errors) with an [error
code](https://docs.stripe.com/error-codes). If the response succeeds, fulfill
the customer’s order and show them a success page. Otherwise, show them an error
page.

## Test your integration

If you can reliably enter a test card in your HTML form, submit it to the
server, and see that your server created the charge, then your integration is
finished.

Congratulations! You completed a basic payments integration with the Charges
API. This API doesn’t support scaling businesses or customers outside of the US
and Canada. For more robust and global payments, learn to accept a payment with
the [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment).

## See also

You can learn more about Elements and how to save cards with the Charges API.

- [Learn about Stripe Elements](https://docs.stripe.com/payments/elements)
- [Saving cards with the Charges API](https://docs.stripe.com/saving-cards)

## Links

- [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment)
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Token](https://docs.stripe.com/api#tokens)
- [Register now](https://dashboard.stripe.com/register)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [create an instance](https://docs.stripe.com/js#elements-create)
- [single line Card
Element](https://docs.stripe.com/js/element/other_element?type=card)
- [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber)
- [Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry)
- [CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)
- [Stripe.js reference](https://docs.stripe.com/js#elements_create)
- [createToken](https://docs.stripe.com/js/tokens/create_token?type=cardElement)
- [API reference](https://docs.stripe.com/api#errors)
- [charge](https://docs.stripe.com/api/charges/object)
- [error](https://docs.stripe.com/api/errors)
- [error code](https://docs.stripe.com/error-codes)
- [Learn about Stripe Elements](https://docs.stripe.com/payments/elements)
- [Saving cards with the Charges API](https://docs.stripe.com/saving-cards)