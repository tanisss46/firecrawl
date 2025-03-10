# Display Affirm messagingDeprecated

## Increase conversion by informing customers that you offer Affirm ahead of checkout.

#### Caution

The content in this topic refers to a Legacy feature. We recommend that you use
the [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging) to
dynamically show your customers relevant buy now, pay later payment options for
a given purchase. Stripe continues to maintain continuity for the
`affirmMessage` Element, but has halted new feature development.

Let your customers know you accept payments with Affirm by including the Affirm
messaging Element on your site. We suggest adding the messaging Element to your
product, cart, and payment pages. The Affirm messaging Element takes care of:

- Calculating and displaying the installments amount
- Displaying the Affirm information modal
The Making of Prince of Persia: Journals 1985-1993Jordan Mechner$50
## Include the Element

#### Caution

Affirm’s minimum transaction amount is 50 USD or 50 CAD. The promotional message
isn’t rendered if the amount parameter is set to a number less than 50 USD or 50
CAD.

HTML + JSReact
Use Stripe Elements to include the
[affirmMessage](https://docs.stripe.com/js/elements_object/create_element?type=affirmMessage)
Element on your site.

If you haven’t already, include the Stripe.js script on your page by adding it
to the `head` of your HTML file:

```
<script src="https://js.stripe.com/v3/"></script>
```

Create a placeholder element on your page where you want to mount the messaging
Element:

```
<div id="affirm-message"></div>
```

On your product, cart, and payment pages, include the following code to create
an instance of Stripe.js and mount the messaging Element:

```
// Set your publishable key. Remember to change this to your live publishable
key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const elements = stripe.elements();

const options = {
 amount: 5000, // $50.00 USD
 currency: 'USD'
};

const affirmMessageElement =
 elements.create('affirmMessage', options);

affirmMessageElement.mount('#affirm-message');
```

## Customize the message

There are many options available to customize the appearance and contents of the
messaging Element. See the [API
reference](https://docs.stripe.com/js/elements_object/create_element?type=affirmMessage)
for the full list of options.

### Logo color

Use the `logoColor` option to choose between the following styles:

primaryblackwhite
### Style with CSS

Additional configuration options allow you to use CSS to style the messaging to
better fit the look and feel of your site. You can customize the `fontColor`,
`fontSize`, and `textAlign` of the messaging:

Code Example
```
const options = {
 amount: 5000,
 currency: 'USD',
 fontColor: '#5B63FF',
 logoColor: 'black',
 fontSize: '16px',
 textAlign: 'center',
};

const affirmMessageElement = elements.create('affirmMessage', options);
```

## Links

- [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging)
-
[affirmMessage](https://docs.stripe.com/js/elements_object/create_element?type=affirmMessage)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)